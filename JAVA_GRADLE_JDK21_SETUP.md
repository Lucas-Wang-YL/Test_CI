# Java Gradle + JDK 21 配置完成

## ✅ 已完成的配置

### 1. **JDK 21 配置**
- ✅ `sourceCompatibility = JavaVersion.VERSION_21`
- ✅ `targetCompatibility = JavaVersion.VERSION_21`

### 2. **Gradle 构建系统**
- ✅ Gradle 8.5 Wrapper
- ✅ build.gradle.kts（Kotlin DSL）
- ✅ gradlew（Linux/Mac 脚本）
- ✅ gradlew.bat（Windows 脚本）

### 3. **项目结构**
```
java/
├── build.gradle.kts                 # Gradle 配置
├── gradlew                           # Unix Wrapper 脚本
├── gradlew.bat                       # Windows Wrapper 脚本
├── gradle/
│   └── wrapper/
│       └── gradle-wrapper.properties # Wrapper 配置
├── src/
│   ├── main/
│   │   └── java/
│   │       └── Calculator.java       # 源代码
│   └── test/
│       └── java/
│           └── CalculatorTest.java   # 测试代码
├── build/                            # 输出目录（自动生成）
└── GRADLE_SETUP.md                  # 配置说明
```

### 4. **GitHub Actions 工作流更新**
- ✅ 移除 Maven 支持，仅使用 Gradle
- ✅ 支持 JDK 17 和 JDK 21 多版本测试
- ✅ 使用 Gradle cache 加速编译
- ✅ 自动生成 JaCoCo 代码覆盖率报告
- ✅ 集成 Checkstyle 代码风格检查

## 🚀 快速开始

### 首次初始化（如果没有 Gradle Wrapper JAR）

```bash
cd java

# 方法 1: 使用本地 Gradle（如果已安装）
gradle wrapper --gradle-version 8.5 --gradle-distribution-type bin

# 方法 2: 使用网络下载（CI/CD 自动完成）
./gradlew --version
```

### 编译和测试

```bash
cd java

# 清理并构建
./gradlew clean build

# 仅运行测试
./gradlew test

# 生成代码覆盖率报告
./gradlew jacocoTestReport

# 运行代码检查
./gradlew checkstyleMain

# 查看详细信息
./gradlew test --info
```

## 📊 build.gradle.kts 配置详解

```kotlin
// 1. 应用插件
plugins {
    java                  // Java 编译插件
    checkstyle            // 代码风格检查
    jacoco                // 代码覆盖率分析
}

// 2. 项目信息
group = "com.example"
version = "1.0.0"

// 3. Java 版本配置 - JDK 21
java {
    sourceCompatibility = JavaVersion.VERSION_21
    targetCompatibility = JavaVersion.VERSION_21
}

// 4. 依赖配置
dependencies {
    testImplementation("junit:junit:4.13.2")
}

// 5. 测试配置
tasks.test {
    useJUnit()
    testLogging {
        events("passed", "skipped", "failed")
    }
}

// 6. 代码覆盖率配置
tasks.jacocoTestReport {
    dependsOn(tasks.test)
    reports {
        xml.required.set(true)
        html.required.set(true)
    }
}
```

## 🔧 GitHub Actions 工作流说明

### 触发条件
- 推送到 `main` 或 `develop` 分支
- 创建 PR 到 `main` 或 `develop` 分支
- 仅当 `.java` 或 `build.gradle.kts` 文件变更时触发

### 工作流任务

| 任务 | JDK 版本 | 操作 |
|------|---------|------|
| test | 17, 21 | 编译 + 运行单元测试 + JaCoCo 报告 |
| code-quality | 21 | Checkstyle 检查 + SonarCloud 扫描 |
| build | 21 | 打包 JAR/WAR，上传制品 |

## 📝 测试覆盖

当前项目包含 30 个测试用例：

```
CalculatorTest
├── Addition (3 tests)
├── Subtraction (3 tests)
├── Multiplication (3 tests)
├── Division (4 tests)
├── Greeting (2 tests)
└── Fibonacci (10 tests)
```

## ✨ 新增特性

### 1. JaCoCo 代码覆盖率
```bash
./gradlew jacocoTestReport

# 生成 HTML 报告在 build/reports/jacoco/test/html/index.html
```

### 2. Checkstyle 代码检查
```bash
./gradlew checkstyleMain

# 报告在 build/reports/checkstyle/main.html
```

### 3. 详细测试输出
```bash
./gradlew test --info
```

## 🔐 本地 JDK 21 设置

```bash
# Linux/Mac
export JAVA_HOME=/path/to/jdk21
export PATH=$JAVA_HOME/bin:$PATH

# Windows PowerShell
$env:JAVA_HOME = "C:\path\to\jdk21"
$env:PATH = "$env:JAVA_HOME\bin;$env:PATH"

# 验证
java -version
# 应该显示 "java version 21.x.x"
```

## 📦 工件输出

构建成功后的输出文件：

```
build/
├── libs/
│   └── java-ci-demo-1.0.0.jar      # 可执行 JAR
├── reports/
│   ├── jacoco/test/html/index.html  # 覆盖率报告
│   └── checkstyle/main.html         # 风格检查报告
└── test-results/                    # 测试结果
```

## 🐛 常见问题

### Q: gradlew: No such file or directory
**A:** 文件权限问题（Linux/Mac）
```bash
chmod +x gradlew
```

### Q: java.lang.UnsupportedClassVersionError
**A:** JDK 版本不匹配，需要 JDK 21
```bash
./gradlew --version  # 查看使用的 Java 版本
java -version        # 查看系统 Java 版本
```

### Q: Could not find gradle-wrapper.jar
**A:** 第一次运行时会自动下载，或手动初始化：
```bash
gradle wrapper --gradle-version 8.5 --gradle-distribution-type bin
```

## 🎯 下一步

1. ✅ 推送代码到 GitHub
2. ✅ 检查 Actions 标签页的工作流运行
3. ✅ 查看构建日志和测试报告
4. ✅ 添加更多测试用例

---

**配置日期**: 2025-12-13  
**Gradle 版本**: 8.5  
**JDK 版本**: 21  
**项目版本**: 1.0.0
