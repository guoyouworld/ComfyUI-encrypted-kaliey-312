"""
ComfyUI-kaliey 加密插件主节点注册模块
负责注册所有自定义节点到ComfyUI
"""

# 导入系统模块
import os
import sys

# 尝试导入ComfyUI核心模块
try:
    import comfy
    import nodes
    import folder_paths
except ImportError:
    # 如果无法导入，添加当前目录到sys.path
    current_dir = os.path.dirname(os.path.abspath(__file__))
    if current_dir not in sys.path:
        sys.path.append(current_dir)
    
    try:
        import comfy
        import nodes
        import folder_paths
    except ImportError:
        print("警告: 无法导入ComfyUI核心模块")

def safe_import_module(module_name):
    """安全导入模块，处理编译后的模块导入问题"""
    try:
        # 首先尝试直接导入
        return __import__(module_name, fromlist=[None])
    except (ImportError, SyntaxError) as e:
        # 如果直接导入失败，尝试通过文件路径导入
        try:
            import importlib.util
            import glob
            
            # 查找当前目录下的.pyc文件
            current_dir = os.path.dirname(__file__)
            pyc_pattern = f"{module_name}*.pyc"
            pyc_files = glob.glob(os.path.join(current_dir, pyc_pattern))
            
            if pyc_files:
                # 使用第一个找到的.pyc文件
                pyc_file = pyc_files[0]
                # 尝试使用文件路径直接加载模块
                spec = importlib.util.spec_from_file_location(module_name, pyc_file)
                if spec and spec.loader:
                    module = importlib.util.module_from_spec(spec)
                    # 尝试执行模块
                    try:
                        spec.loader.exec_module(module)
                        return module
                    except Exception:
                        # 如果执行失败，可能是Python版本不兼容，尝试其他方法
                        pass
            
            # 如果通过.pyc文件导入失败，尝试导入源文件（如果存在）
            py_files = glob.glob(os.path.join(current_dir, f"{module_name}.py"))
            if py_files:
                spec = importlib.util.spec_from_file_location(module_name, py_files[0])
                if spec and spec.loader:
                    module = importlib.util.module_from_spec(spec)
                    spec.loader.exec_module(module)
                    return module
                    
        except Exception:
            pass
        
        # 如果所有方法都失败，重新抛出原始异常
        raise e

# 导入自定义模块
# 机器码相关节点
try:
    from .machine_id_nodes import MACHINE_ID_NODE_CLASS_MAPPINGS, MACHINE_ID_NODE_DISPLAY_NAME_MAPPINGS
except ImportError:
    try:
        from machine_id_nodes import MACHINE_ID_NODE_CLASS_MAPPINGS, MACHINE_ID_NODE_DISPLAY_NAME_MAPPINGS
    except ImportError:
        # When modules are compiled to .pyc files, we need special handling
        try:
            machine_id_nodes = safe_import_module("machine_id_nodes")
            MACHINE_ID_NODE_CLASS_MAPPINGS = machine_id_nodes.MACHINE_ID_NODE_CLASS_MAPPINGS
            MACHINE_ID_NODE_DISPLAY_NAME_MAPPINGS = machine_id_nodes.MACHINE_ID_NODE_DISPLAY_NAME_MAPPINGS
        except Exception as e:
            print(f"无法导入 machine_id_nodes 模块: {e}")
            raise

# 加密相关节点
try:
    from .encrypt_nodes import ENCRYPT_NODE_CLASS_MAPPINGS, ENCRYPT_NODE_DISPLAY_NAME_MAPPINGS
except ImportError:
    try:
        from encrypt_nodes import ENCRYPT_NODE_CLASS_MAPPINGS, ENCRYPT_NODE_DISPLAY_NAME_MAPPINGS
    except ImportError:
        # When modules are compiled to .pyc files, we need special handling
        try:
            encrypt_nodes = safe_import_module("encrypt_nodes")
            ENCRYPT_NODE_CLASS_MAPPINGS = encrypt_nodes.ENCRYPT_NODE_CLASS_MAPPINGS
            ENCRYPT_NODE_DISPLAY_NAME_MAPPINGS = encrypt_nodes.ENCRYPT_NODE_DISPLAY_NAME_MAPPINGS
        except Exception as e:
            print(f"无法导入 encrypt_nodes 模块: {e}")
            raise

# 解密加载相关节点
try:
    from .decrypt_loader_nodes import DECRYPT_LOADER_NODE_CLASS_MAPPINGS, DECRYPT_LOADER_NODE_DISPLAY_NAME_MAPPINGS
except ImportError:
    try:
        from decrypt_loader_nodes import DECRYPT_LOADER_NODE_CLASS_MAPPINGS, DECRYPT_LOADER_NODE_DISPLAY_NAME_MAPPINGS
    except ImportError:
        # When modules are compiled to .pyc files, we need special handling
        try:
            decrypt_loader_nodes = safe_import_module("decrypt_loader_nodes")
            DECRYPT_LOADER_NODE_CLASS_MAPPINGS = decrypt_loader_nodes.DECRYPT_LOADER_NODE_CLASS_MAPPINGS
            DECRYPT_LOADER_NODE_DISPLAY_NAME_MAPPINGS = decrypt_loader_nodes.DECRYPT_LOADER_NODE_DISPLAY_NAME_MAPPINGS
        except Exception as e:
            print(f"无法导入 decrypt_loader_nodes 模块: {e}")
            raise

# 手动路径解密加载相关节点
try:
    from .decrypt_loader_manual_path import MANUAL_PATH_DECRYPT_LOADER_NODE_CLASS_MAPPINGS, MANUAL_PATH_DECRYPT_LOADER_NODE_DISPLAY_NAME_MAPPINGS
except ImportError:
    try:
        from decrypt_loader_manual_path import MANUAL_PATH_DECRYPT_LOADER_NODE_CLASS_MAPPINGS, MANUAL_PATH_DECRYPT_LOADER_NODE_DISPLAY_NAME_MAPPINGS
    except ImportError:
        # When modules are compiled to .pyc files, we need special handling
        try:
            decrypt_loader_manual_path = safe_import_module("decrypt_loader_manual_path")
            MANUAL_PATH_DECRYPT_LOADER_NODE_CLASS_MAPPINGS = decrypt_loader_manual_path.MANUAL_PATH_DECRYPT_LOADER_NODE_CLASS_MAPPINGS
            MANUAL_PATH_DECRYPT_LOADER_NODE_DISPLAY_NAME_MAPPINGS = decrypt_loader_manual_path.MANUAL_PATH_DECRYPT_LOADER_NODE_DISPLAY_NAME_MAPPINGS
        except Exception as e:
            print(f"无法导入 decrypt_loader_manual_path 模块: {e}")
            raise

# Nunchaku LoRA加载节点
try:
    from .nunchaku_lora_loader import NUNCHAKU_NODE_CLASS_MAPPINGS, NUNCHAKU_NODE_DISPLAY_NAME_MAPPINGS
except ImportError:
    try:
        from nunchaku_lora_loader import NUNCHAKU_NODE_CLASS_MAPPINGS, NUNCHAKU_NODE_DISPLAY_NAME_MAPPINGS
    except ImportError:
        # When modules are compiled to .pyc files, we need special handling
        try:
            nunchaku_lora_loader = safe_import_module("nunchaku_lora_loader")
            NUNCHAKU_NODE_CLASS_MAPPINGS = nunchaku_lora_loader.NUNCHAKU_NODE_CLASS_MAPPINGS
            NUNCHAKU_NODE_DISPLAY_NAME_MAPPINGS = nunchaku_lora_loader.NUNCHAKU_NODE_DISPLAY_NAME_MAPPINGS
        except Exception as e:
            print(f"无法导入 nunchaku_lora_loader 模块: {e}")
            raise

# 合并所有节点映射
NODE_CLASS_MAPPINGS = {}
NODE_DISPLAY_NAME_MAPPINGS = {}

# 合并机器码节点
NODE_CLASS_MAPPINGS.update(MACHINE_ID_NODE_CLASS_MAPPINGS)
NODE_DISPLAY_NAME_MAPPINGS.update(MACHINE_ID_NODE_DISPLAY_NAME_MAPPINGS)

# 合并加密节点
NODE_CLASS_MAPPINGS.update(ENCRYPT_NODE_CLASS_MAPPINGS)
NODE_DISPLAY_NAME_MAPPINGS.update(ENCRYPT_NODE_DISPLAY_NAME_MAPPINGS)

# 合并解密加载节点
NODE_CLASS_MAPPINGS.update(DECRYPT_LOADER_NODE_CLASS_MAPPINGS)
NODE_DISPLAY_NAME_MAPPINGS.update(DECRYPT_LOADER_NODE_DISPLAY_NAME_MAPPINGS)

# 合并手动路径解密加载节点
NODE_CLASS_MAPPINGS.update(MANUAL_PATH_DECRYPT_LOADER_NODE_CLASS_MAPPINGS)
NODE_DISPLAY_NAME_MAPPINGS.update(MANUAL_PATH_DECRYPT_LOADER_NODE_DISPLAY_NAME_MAPPINGS)

# 合并Nunchaku节点
NODE_CLASS_MAPPINGS.update(NUNCHAKU_NODE_CLASS_MAPPINGS)
NODE_DISPLAY_NAME_MAPPINGS.update(NUNCHAKU_NODE_DISPLAY_NAME_MAPPINGS)

# 为所有显示名称添加kaliey标识
kaliey_display_names = {}
for node_id, display_name in NODE_DISPLAY_NAME_MAPPINGS.items():
    # 在显示名称后添加kaliey标识
    kaliey_display_names[node_id] = f"{display_name} - kaliey"
NODE_DISPLAY_NAME_MAPPINGS = kaliey_display_names

# 输出加载信息
print("\n" + "="*60)
print("🔐 ComfyUI-kaliey 加密插件已加载")
print("="*60)
print("✅ 提供以下功能:")
print("   • 机器码生成与验证")
print("   • Lora文件加密保护")
print("   • 加密Lora文件解密加载")
print("   • Nunchaku模型专用LoRA加载")
print("="*60)

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']