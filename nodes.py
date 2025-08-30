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

# 导入自定义模块
# 机器码相关节点
try:
    from .machine_id_nodes import MACHINE_ID_NODE_CLASS_MAPPINGS, MACHINE_ID_NODE_DISPLAY_NAME_MAPPINGS
except ImportError:
    from machine_id_nodes import MACHINE_ID_NODE_CLASS_MAPPINGS, MACHINE_ID_NODE_DISPLAY_NAME_MAPPINGS

# 加密相关节点
try:
    from .encrypt_nodes import ENCRYPT_NODE_CLASS_MAPPINGS, ENCRYPT_NODE_DISPLAY_NAME_MAPPINGS
except ImportError:
    from encrypt_nodes import ENCRYPT_NODE_CLASS_MAPPINGS, ENCRYPT_NODE_DISPLAY_NAME_MAPPINGS

# 解密加载相关节点
try:
    from .decrypt_loader_nodes import DECRYPT_LOADER_NODE_CLASS_MAPPINGS, DECRYPT_LOADER_NODE_DISPLAY_NAME_MAPPINGS
except ImportError:
    from decrypt_loader_nodes import DECRYPT_LOADER_NODE_CLASS_MAPPINGS, DECRYPT_LOADER_NODE_DISPLAY_NAME_MAPPINGS

# 手动路径解密加载相关节点
try:
    from .decrypt_loader_manual_path import MANUAL_PATH_DECRYPT_LOADER_NODE_CLASS_MAPPINGS, MANUAL_PATH_DECRYPT_LOADER_NODE_DISPLAY_NAME_MAPPINGS
except ImportError:
    from decrypt_loader_manual_path import MANUAL_PATH_DECRYPT_LOADER_NODE_CLASS_MAPPINGS, MANUAL_PATH_DECRYPT_LOADER_NODE_DISPLAY_NAME_MAPPINGS

# Nunchaku LoRA加载节点
try:
    from .nunchaku_lora_loader import NUNCHAKU_NODE_CLASS_MAPPINGS, NUNCHAKU_NODE_DISPLAY_NAME_MAPPINGS
except ImportError:
    from nunchaku_lora_loader import NUNCHAKU_NODE_CLASS_MAPPINGS, NUNCHAKU_NODE_DISPLAY_NAME_MAPPINGS

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