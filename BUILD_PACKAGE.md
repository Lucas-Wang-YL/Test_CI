# Build & Package Guide

完整的 Java 和 Python 项目打包指南。

## Java 项目打包

### 构建 JAR

```bash
cd java
./gradlew jar
```

生成文件：`build/libs/calculator-1.0.0.jar`

**特性：**
- Fat JAR（包含所有依赖）
- 可执行 JAR（带 Main-Class manifest）
- 版本号自动包含

### 构建完整分发包

```bash
./gradlew distZip    # 生成 ZIP 压缩包
./gradlew distTar    # 生成 TAR 压缩包
```

生成文件：
- `build/distributions/java-1.0.0.zip`
- `build/distributions/java-1.0.0.tar`

**包含内容：**
- JAR 文件
- 启动脚本（Windows/Linux）
- 配置文件
- 依赖库

### 运行

```bash
# 直接运行 JAR
java -jar build/libs/calculator-1.0.0.jar

# 使用分发包
unzip build/distributions/java-1.0.0.zip
cd java-1.0.0/bin
./java   # Linux/Mac
java.bat # Windows
```

### Gradle 打包任务

```bash
./gradlew tasks --group=build
```

常用任务：
- `jar` - 构建 JAR 文件
- `build` - 完整构建（测试 + JAR）
- `distZip` - 创建 ZIP 分发包
- `distTar` - 创建 TAR 分发包
- `assembleDist` - 创建所有分发包

## Python 项目打包

### 安装打包工具

```bash
pip install --upgrade pip setuptools wheel build
```

### 构建分发包

```bash
cd python
python -m build
```

生成文件：
- `dist/stdf_parser-1.0.0-py3-none-any.whl` (wheel)
- `dist/stdf-parser-1.0.0.tar.gz` (source)

### 安装本地包

```bash
# 开发模式安装（可编辑）
pip install -e .

# 从 wheel 安装
pip install dist/stdf_parser-1.0.0-py3-none-any.whl

# 从源码安装
pip install dist/stdf-parser-1.0.0.tar.gz
```

### 验证安装

```bash
# 检查包是否安装
pip show stdf-parser

# 测试命令行工具
stdf --help
stdf generate sample.stdf --tests 10
stdf parse sample.stdf --summary
```

### 发布到 PyPI（可选）

```bash
# 安装 twine
pip install twine

# 上传到 TestPyPI（测试）
twine upload --repository testpypi dist/*

# 上传到 PyPI（生产）
twine upload dist/*
```

## CI/CD 自动打包

### GitHub Actions 工作流

所有提交到 `main` 分支会自动触发：

**Java CI:**
1. 运行测试
2. 构建 JAR
3. 创建分发包
4. 上传 artifacts:
   - `calculator-jar` - JAR 文件
   - `calculator-distributions` - ZIP/TAR 包

**Python CI:**
1. 运行测试
2. 构建 wheel 和 sdist
3. 验证安装
4. 上传 artifacts:
   - `python-stdf-dist` - wheel 和 tar.gz

### 下载 Artifacts

1. 进入 GitHub Actions 页面
2. 选择成功的 workflow run
3. 在 "Artifacts" 区域下载

## 本地测试完整流程

### Java

```bash
cd java

# 清理
./gradlew clean

# 构建和测试
./gradlew build

# 创建分发包
./gradlew distZip

# 解压测试
cd build/distributions
unzip java-1.0.0.zip
cd java-1.0.0
./bin/java
```

### Python

```bash
cd python

# 清理旧构建
rm -rf build/ dist/ *.egg-info

# 构建
python -m build

# 测试安装
pip install dist/*.whl

# 验证
stdf --help
python -c "from stdf import STDFParser; print('Import OK')"

# 卸载
pip uninstall stdf-parser -y
```

## 配置文件说明

### Java: build.gradle.kts

```kotlin
application {
    mainClass.set("Calculator")  // 设置主类
}

tasks.jar {
    manifest {
        attributes["Main-Class"] = "Calculator"  // JAR manifest
    }
    archiveBaseName.set("calculator")  // JAR 名称
    archiveVersion.set("1.0.0")       // 版本号
}
```

### Python: pyproject.toml

```toml
[project]
name = "stdf-parser"
version = "1.0.0"

[project.scripts]
stdf = "stdf.cli:main"  # 命令行入口点
```

### Python: setup.py

传统打包配置，与 pyproject.toml 功能相同。

## 版本管理

### 更新版本号

**Java:**
编辑 `java/build.gradle.kts`:
```kotlin
version = "1.1.0"
```

**Python:**
编辑 `python/pyproject.toml` 和 `python/setup.py`:
```toml
version = "1.1.0"
```

### 版本命名规范

使用语义化版本 (SemVer): `MAJOR.MINOR.PATCH`
- MAJOR: 不兼容的 API 改动
- MINOR: 向后兼容的功能新增
- PATCH: 向后兼容的问题修正

例如：
- `1.0.0` - 初始发布
- `1.0.1` - Bug 修复
- `1.1.0` - 新功能
- `2.0.0` - 破坏性更新

## 故障排查

### Java 打包失败

```bash
# 检查 Gradle 版本
./gradlew --version

# 清理并重建
./gradlew clean build --stacktrace

# 检查主类是否存在
ls src/main/java/Calculator.java
```

### Python 打包失败

```bash
# 检查项目结构
tree stdf/

# 验证 setup.py 配置
python setup.py check

# 详细构建日志
python -m build --verbose
```

### 安装失败

```bash
# Python: 检查依赖
pip install --dry-run dist/*.whl

# Java: 检查 JAR 内容
jar tf build/libs/calculator-1.0.0.jar | grep Calculator.class
```

## 最佳实践

1. **版本控制**: 不提交 `build/`, `dist/`, `*.egg-info/`
2. **自动化**: 使用 CI/CD 自动构建和测试
3. **文档**: README 包含安装和使用说明
4. **测试**: 打包前确保所有测试通过
5. **签名**: 生产发布使用 GPG 签名
6. **变更日志**: 维护 CHANGELOG.md
