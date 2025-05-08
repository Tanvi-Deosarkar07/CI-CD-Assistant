
# GitHub Actions CI/CD Guide

## Overview
This guide helps you understand how to set up CI/CD pipelines using GitHub Actions.

## CI Workflow
- Trigger: Push to `main` branch
- Jobs:
  - `install`: Set up Python and dependencies
  - `test`: Run unit tests
  - `deploy`: Deploy to production on success

## Example YAML
```yaml
name: CI/CD Pipeline
on:
  push:
    branches: [ main ]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Install Dependencies
        run: pip install -r requirements.txt
      - name: Run Tests
        run: pytest
```
