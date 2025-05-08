
# Jenkins CI/CD Pipeline Guide

## Overview
Jenkins is an automation server used to build, test, and deploy code continuously.

## Steps to Setup
1. Install Jenkins plugins: Git, Pipeline, Docker
2. Create a Jenkinsfile in your repo
3. Configure Jenkins job to track your branch

## Example Jenkinsfile
```groovy
pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        echo 'Building...'
      }
    }
    stage('Test') {
      steps {
        echo 'Running tests...'
      }
    }
    stage('Deploy') {
      steps {
        echo 'Deploying...'
      }
    }
  }
}
```
