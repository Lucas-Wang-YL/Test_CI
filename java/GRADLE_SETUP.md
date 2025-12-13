# Gradle Wrapper Setup Instructions
# This file explains how to properly set up the Gradle wrapper

## Quick Setup (macOS/Linux)

```bash
# 从java目录运行
cd java

# 创建Gradle包装器（使用Gradle 8.5）
gradle wrapper --gradle-version 8.5 --gradle-distribution-type bin

# 使脚本可执行
chmod +x gradlew
```

## For Windows

```bash
# 从java目录运行
cd java

# 如果安装了Gradle，运行：
gradle wrapper --gradle-version 8.5 --gradle-distribution-type bin
```

## Or Download Pre-built Wrapper

如果上述方法不可行，可以：

1. 访问 https://gradle.org/releases/
2. 下载 gradle-8.5-bin.zip
3. 解压到项目目录的 `gradle/wrapper/` 下

## Verify Installation

```bash
# 测试Gradle是否正确安装
./gradlew --version

# 应该输出类似于：
# Gradle 8.5
# ...
# Java version used by Gradle: 21.x.x (Oracle Corporation 21.x.x)
```

## Run Tests

```bash
# 编译
./gradlew clean build

# 只运行测试
./gradlew test

# 生成测试覆盖率报告
./gradlew jacocoTestReport
```

## 项目结构

```
java/
├── build.gradle.kts          # Gradle配置文件（Kotlin DSL）
├── gradlew                     # Gradle Wrapper脚本（Linux/Mac）
├── gradlew.bat                 # Gradle Wrapper脚本（Windows）
├── gradle/
│   └── wrapper/
│       └── gradle-wrapper.properties  # Wrapper配置
├── src/
│   ├── main/
│   │   └── java/              # 源代码
│   └── test/
│       └── java/              # 测试代码
└── build/                      # 编译输出（自动生成）
```

## JDK 21 配置

build.gradle.kts 已配置：
- `sourceCompatibility = JavaVersion.VERSION_21`
- `targetCompatibility = JavaVersion.VERSION_21`

确保你的系统安装了 JDK 21。

## 故障排除

### 问题：gradlew 不可执行
**解决方案：**
```bash
chmod +x gradlew
```

### 问题：Cannot find gradle-wrapper.jar
**解决方案：**
运行初始化命令生成Wrapper JAR：
```bash
gradle wrapper --gradle-version 8.5 --gradle-distribution-type bin
```

### 问题：Java version mismatch
**解决方案：**
确保安装了JDK 21，并设置JAVA_HOME：
```bash
export JAVA_HOME=/path/to/jdk21  # Linux/Mac
set JAVA_HOME=C:\path\to\jdk21   # Windows
```
