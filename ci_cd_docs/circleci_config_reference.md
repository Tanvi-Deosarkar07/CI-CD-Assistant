
# CircleCI Configuration Reference

## Getting Started
1. Add `.circleci/config.yml` to your repo
2. Define jobs and workflows

## Sample Config
```yaml
version: 2.1
jobs:
  build:
    docker:
      - image: cimg/python:3.9
    steps:
      - checkout
      - run: pip install -r requirements.txt
      - run: pytest
workflows:
  version: 2
  build_and_test:
    jobs:
      - build
```
