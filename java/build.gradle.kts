plugins {
    java
    application
    // checkstyle   // 禁用，直到配置文件准备好
    jacoco
}

group = "com.example"
version = "1.0.0"

application {
    mainClass.set("Calculator")
}

java {
    sourceCompatibility = JavaVersion.VERSION_21
    targetCompatibility = JavaVersion.VERSION_21
}

repositories {
    mavenCentral()
}

dependencies {
    // JUnit for testing
    testImplementation("junit:junit:4.13.2")
}

// JaCoCo report configuration
tasks.test {
    useJUnit()
    testLogging {
        events("passed", "skipped", "failed")
        exceptionFormat = org.gradle.api.tasks.testing.logging.TestExceptionFormat.FULL
    }
}

// JaCoCo report configuration
tasks.jacocoTestReport {
    dependsOn(tasks.test)
    reports {
        xml.required.set(true)
        csv.required.set(false)
        html.required.set(true)
    }
}

// JAR packaging configuration
tasks.jar {
    manifest {
        attributes(
            "Implementation-Title" to project.name,
            "Implementation-Version" to project.version,
            "Main-Class" to "Calculator"
        )
    }
    archiveBaseName.set("calculator")
    archiveVersion.set(project.version.toString())
    
    // Create fat JAR with dependencies
    from(configurations.runtimeClasspath.get().map { if (it.isDirectory) it else zipTree(it) })
    duplicatesStrategy = DuplicatesStrategy.EXCLUDE
}

// Distribution packaging
distributions {
    main {
        contents {
            from("src/main/resources") {
                into("config")
            }
        }
    }
}

tasks.test {
    finalizedBy(tasks.jacocoTestReport)
}
