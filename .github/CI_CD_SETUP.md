# GitHub Actions CI/CD 配置文档

本项目已配置了针对 Python 和 Java 项目的 GitHub Actions CI/CD 工作流。

## 📋 工作流文件说明

### 1. **python-ci.yml** - Python CI/CD 工作流
自动运行以下任务：
- ✅ 代码语法检查 (flake8)
- ✅ 单元测试 (pytest)
- ✅ 代码覆盖率分析
- ✅ 构建分发包

**触发条件：**
- 推送到 `main` 或 `develop` 分支（涉及 Python 文件）
- 创建 Pull Request 到 `main` 或 `develop` 分支（涉及 Python 文件）

**支持的 Python 版本：** 3.12

### 2. **java-ci.yml** - Java CI/CD 工作流
自动运行以下任务：
- ✅ 使用 Maven 编译和测试
- ✅ 使用 Gradle 编译和测试
- ✅ 代码质量分析 (SonarCloud)
- ✅ 构建 JAR/WAR 包

**触发条件：**
- 推送到 `main` 或 `develop` 分支（涉及 Java 文件）
- 创建 Pull Request 到 `main` 或 `develop` 分支（涉及 Java 文件）

**支持的 JDK 版本：** 21

### 3. **ci-cd.yml** - 综合CI/CD管道
整合的工作流，包括：
- ✅ Python 代码检查 (Black, isort, Pylint)
- ✅ Java 代码检查 (Checkstyle)
- ✅ 安全漏洞扫描 (Trivy)
- ✅ 定时扫描 (每天 UTC 00:00)

## 🔧 项目配置需求

### Python 项目配置
在项目根目录创建以下文件（如果需要）：

**requirements.txt** - 生产依赖
```
requests==2.28.0
numpy==1.23.0
```

**requirements-dev.txt** - 开发依赖
```
pytest==7.2.0
pytest-cov==4.0.0
black==22.10.0
flake8==5.0.4
```

**setup.py** - 项目配置（可选）
```python
from setuptools import setup, find_packages

setup(
    name='your-project-name',
    version='0.1.0',
    packages=find_packages(),
    python_requires='>=3.12',
    install_requires=[
        'requests>=2.28.0',
    ],
)
```

### Java 项目配置

**Maven 项目** - 必须包含 `pom.xml`
```xml
<project>
    <modelVersion>4.0.0</modelVersion>
    <groupId>com.example</groupId>
    <artifactId>my-project</artifactId>
    <version>1.0.0</version>
    
    <dependencies>
        <!-- 依赖配置 -->
    </dependencies>
    
    <build>
        <plugins>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-surefire-plugin</artifactId>
                <version>3.0.0-M7</version>
            </plugin>
        </plugins>
    </build>
</project>
```

**Gradle 项目** - 必须包含 `build.gradle` 或 `build.gradle.kts`、`gradlew` 以及 `gradle/wrapper/gradle-wrapper.jar`（注意：需要提交到 Git）
```gradle
plugins {
    id 'java'
}

group = 'com.example'
version = '1.0.0'

repositories {
    mavenCentral()
}

dependencies {
    // 依赖配置
    testImplementation 'junit:junit:4.13.2'
}

test {
    useJUnit()
}
```

## 🔐 Secrets 配置

### SonarCloud 集成（可选）
如果要启用 SonarCloud 代码质量分析：

1. 访问 [SonarCloud](https://sonarcloud.io)
2. 关联你的 GitHub 仓库
3. 获取 `SONAR_TOKEN`
4. 在 GitHub 仓库 Settings → Secrets and variables → Actions 中添加：
   - `SONAR_TOKEN`: 你的 SonarCloud token

## 📊 工作流状态徽章

在 README.md 中添加以下内容来显示 CI/CD 状态：

```markdown
[![Python CI](https://github.com/YOUR_USERNAME/YOUR_REPO/actions/workflows/python-ci.yml/badge.svg)](https://github.com/YOUR_USERNAME/YOUR_REPO/actions/workflows/python-ci.yml)

[![Java CI](https://github.com/YOUR_USERNAME/YOUR_REPO/actions/workflows/java-ci.yml/badge.svg)](https://github.com/YOUR_USERNAME/YOUR_REPO/actions/workflows/java-ci.yml)

[![CI/CD Pipeline](https://github.com/YOUR_USERNAME/YOUR_REPO/actions/workflows/ci-cd.yml/badge.svg)](https://github.com/YOUR_USERNAME/YOUR_REPO/actions/workflows/ci-cd.yml)
```

## 🚀 使用步骤

1. **提交工作流文件**
   ```bash
   git add .github/workflows/
   git commit -m "feat: add GitHub Actions CI/CD workflows"
   git push origin main
   ```

2. **查看工作流运行**
   - 访问仓库的 **Actions** 标签页
   - 可以看到工作流的执行状态和详细日志

3. **检查工作流结果**
   - 如果有失败，点击失败的工作流查看错误日志
   - 根据错误信息调整项目配置或代码

## 📝 常见问题排查

### Python 工作流失败
- **检查 Python 文件存在性** - 确保有 `.py` 文件
- **检查依赖** - 更新 `requirements.txt`
- **查看测试日志** - 检查 pytest 输出

### Java 工作流失败
- **Maven 构建失败** - 检查 `pom.xml` 配置
- **Gradle 构建失败** - 确保有 `gradlew` 脚本
- **JDK 版本兼容性** - 调整支持的 JDK 版本

### 缓存问题
- Maven 和 Gradle 依赖会自动缓存
- 如果需要清除缓存，访问 Actions → 选择工作流 → 清除所有缓存

## 🔗 参考文档

- [GitHub Actions 文档](https://docs.github.com/en/actions)
- [Python 与 GitHub Actions](https://docs.github.com/en/actions/automating-builds-and-testing/building-and-testing-python)
- [Java 与 GitHub Actions](https://docs.github.com/en/actions/automating-builds-and-testing/building-and-testing-java-with-maven)
- [SonarCloud 文档](https://docs.sonarcloud.io/)

---

**最后更新：** 2025-12-13
**配置状态：** 
- ✅ Java CI 使用 JDK 21
- ✅ Python CI 使用 Python 3.12
- ✅ 所有 Actions 已升级到最新版本 (upload-artifact v4)
- ✅ Gradle wrapper 已正确配置

需要帮助？查看 [GitHub Actions 故障排除指南](https://docs.github.com/en/actions/monitoring-and-troubleshooting-workflows)
