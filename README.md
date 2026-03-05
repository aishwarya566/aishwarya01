<project xmlns="http://maven.apache.org/POM/4.0.0"
 xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
 xsi:schemaLocation="http://maven.apache.org/POM/4.0.0
 http://maven.apache.org/xsd/maven-4.0.0.xsd">
 <modelVersion>4.0.0</modelVersion>
 <groupId>com.example</groupId>
 <artifactId>simple-maven-app</artifactId>
 <version>1.0-SNAPSHOT</version>
 <dependencies>
 <dependency>
 <groupId>junit</groupId>
 <artifactId>junit</artifactId>
 <version>4.13.2</version>
 <scope>test</scope>
 </dependency>
 </dependencies>
</project>





appjava:
package com.example;
public class App {
 public int add(int a, int b) {
 return a + b;
 }
}


app2:
package com.example;
import org.junit.Test;
import static org.junit.Assert.*;
public class AppTest {
 @Test
 public void testAdd() {
 App app = new App();
 assertEquals(5, app.add(2, 3));
 }
}


script:
pipeline {
 agent any
 tools {
 maven 'MAVEN_HOME'
 }
 stages {
 stage('Checkout Git') {
 steps {
 git branch: 'master',
 url: 'https://github.com/manishragvendra/jm.git'
 }
 }
 stage('Build and Test') {
 steps {
 bat 'mvn clean test'
 }
 }
 }
}



