# ComfyUI-encrypted-kaliey

🔐 **Lora模型加密保护插件** - 为您的ComfyUI Lora模型提供专业级安全保护

## 📋 项目概述

ComfyUI-encrypted-kaliey 是一个专门为ComfyUI设计的插件，提供对 Lora 模型文件的加密保护功能，防止未经授权的使用。通过AES-256加密算法和基于硬件特征的机器码绑定技术，确保您的Lora模型文件安全。

该插件支持多Python版本（3.10-3.13），为不同环境提供兼容的版本。

### 🌟 核心特性

- **🔒 军用级AES-256加密**：采用AES-256加密算法保护您的Lora文件
- **🖥️ 基于硬件特征的机器码绑定**：基于硬件特征的机器码生成，确保文件只能在授权设备上使用
- **📦 智能压缩**：内置gzip压缩，减小加密文件体积
- **🔍 完整性校验**：SHA-256校验和确保文件完整性
- **⚡ 批量处理**：支持批量处理多个Lora文件
- **🎯 无缝集成**：完美融入ComfyUI工作流
- **🔄 多版本支持**：支持Python 3.10-3.13版本
- **🛡️ 代码保护**：提供代码混淆和字节码编译功能，防止代码被轻易阅读和盗取

## 🚀 快速开始

### 安装步骤

1. **下载插件**
   ```bash
   # 将插件复制到ComfyUI custom_nodes目录
   git clone https://github.com/your-repo/ComfyUI-encrypted-kaliey.git
   # 或直接下载ZIP文件解压到 ComfyUI/custom_nodes/ 目录
   ```

2. **安装依赖**
   ```bash
   cd ComfyUI/custom_nodes/ComfyUI-encrypted-kaliey
   pip install -r requirements.txt
   ```

   > **💡 虚拟环境提示**: 如果您使用Python虚拟环境，请确保在安装依赖前激活您的虚拟环境：
   > ```bash
   > # 对于venv创建的虚拟环境
   > source venv/bin/activate    # Linux/macOS
   > # 或
   > venv\Scripts\activate       # Windows
   >
   > # 对于conda创建的虚拟环境
   > conda activate your_env_name
   >
   > # 然后安装依赖
   > pip install -r requirements.txt
   > ```

3. **重启ComfyUI**
   
   重启ComfyUI后，在节点菜单中找到"Lora加密工具"分类

### 📦 依赖要求

- Python 3.8+
- ComfyUI 最新版本
- cryptography >= 41.0.0
- torch >= 1.13.0
- safetensors >= 0.3.0

## 🔧 功能节点

### 1. 获取机器码节点
- **功能**：获取当前设备的唯一机器码
- **用途**：用于加密时指定目标设备

### 2. 机器码加密Lora节点
- **功能**：使用指定机器码加密Lora文件
- **输入**：
  - `input_path`：要加密的Lora文件路径
  - `target_machine_code`：目标机器码
  - `backup_original`：是否备份原文件
  - `compression`：是否启用压缩

### 3. 加载加密Lora节点
- **功能**：自动解密并加载加密的Lora文件
- **特点**：自动获取当前机器码，无需手动输入密码
- **支持**：完整模型+CLIP或仅模型模式

## 💼 使用示例

### 基本加密流程

1. **获取机器码**
   - 添加"获取机器码"节点
   - 运行工作流，复制机器码

2. **加密Lora文件**
   - 添加"机器码加密Lora"节点
   - 设置文件路径和目标机器码
   - 运行加密

3. **使用加密文件**
   - 添加"加载加密Lora"节点
   - 设置加密文件路径
   - 连接到模型和CLIP

### 工作流示例

```
[获取机器码] → [机器码加密Lora] → [加密文件]
                     ↓
[模型] → [加载加密Lora] → [受保护的模型]
[CLIP] →        ↑
```

## 🛡️ 安全特性

### 加密技术
- **算法**：AES-256-CBC加密
- **密钥派生**：基于64位完整机器码生成
- **完整性**：SHA-256校验和验证
- **压缩**：可选gzip压缩减小体积

### 设备绑定
- **机器码生成**：基于硬件特征生成唯一标识
- **跨机器保护**：加密文件仅在指定设备可用
- **自动验证**：解密时自动验证设备授权

## 🔧 代码保护工具

### 使用方法

**方式一：一键脚本**
```bash
# Windows
.\protect_code.bat

# 选择保护级别：
# [1] 低级保护 - 字节码编译
# [2] 中级保护 - 代码混淆 + 字节码编译  
# [3] 高级保护 - 加密字节码加载器
```

**方式二：命令行**
```bash
python protect_code.py --source . --output protected_code --level medium
```

### 保护级别

- **低级保护**：字节码编译，移除源码可读性
- **中级保护**：代码混淆，变量名混淆，字符串加密
- **高级保护**：加密字节码加载器，动态解密执行

## 📁 项目结构

```
ComfyUI-encrypted-kaliey/
├── __init__.py              # 插件入口
├── nodes.py                 # 节点集成文件
├── machine_id_nodes.py      # 机器码节点
├── encrypt_nodes.py         # 加密节点
├── decrypt_loader_nodes.py  # 解密加载节点
├── machine_id.py           # 机器码生成模块
├── encrypt.py              # 加密核心模块
├── decrypt.py              # 解密核心模块
├── encrypted_lora_loader.py # 加密Lora加载器
├── utils.py                # 工具函数
├── config.py               # 配置管理
└── requirements.txt        # 依赖列表
```

## 🔄 多版本支持

本项目提供多Python版本支持，编译后的版本将生成在项目根目录中：
```bash
ComfyUI-encrypted-kaliey-310/    # Python 3.10版本
ComfyUI-encrypted-kaliey-311/    # Python 3.11版本
ComfyUI-encrypted-kaliey-312/    # Python 3.12版本
ComfyUI-encrypted-kaliey-313/    # Python 3.13版本
```

在实际使用中，您可以使用通配符来引用不同版本的目录，例如：
```bash
# 使用通配符引用所有版本目录
ComfyUI-encrypted-kaliey-*/      

# 或者在脚本中使用通配符匹配特定版本
ComfyUI-encrypted-kaliey-31*     # 匹配310, 311, 312, 313版本
```

## 🔨 编译项目

### 使用build.bat编译（推荐）

```bash
# Windows
.\build.bat
```

### 使用特定Conda环境编译

如果您有预定义的Conda环境，可以使用以下脚本：

```bash
# Windows
.\compile_with_env.bat
```

这将使用以下命名规则的环境进行编译：
- comfyui_encrypted_kaliey_py310
- comfyui_encrypted_kaliey_py311
- comfyui_encrypted_kaliey_py312
- comfyui_encrypted_kaliey_py313

### 自定义Anaconda路径

如果您的Anaconda安装在非默认位置，可以设置环境变量：

```batch
set ANACONDA_PATH=C:\Your\Anaconda\Path
.\build.bat
```

## ⚠️ 注意事项

### 重要提醒
- **密钥安全**：机器码是解密的唯一凭证，请妥善保管
- **文件备份**：加密前建议备份原始文件
- **兼容性**：加密文件仅在指定设备可用
- **版本兼容**：确保ComfyUI版本兼容性

### 故障排除
- **解密失败**：检查机器码是否匹配
- **文件损坏**：验证文件完整性
- **依赖错误**：确认所有依赖已安装

## 📄 许可证

本项目仅供学习和研究使用，请遵守相关法律法规，不要用于任何商业用途。

## 🤝 贡献

欢迎提交Issue和Pull Request来帮助改进项目！

## 📞 支持

如有问题或建议，请通过以下方式联系：
- 提交GitHub Issue
- 发送邮件至：guoyouworld@163.com

---

**⭐ 如果这个项目对您有帮助，请给我们一个Star！**