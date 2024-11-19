name: Hello World
on:
  push: 
    branches:
      - main
jobs:
  first-hello-world-job:
    runs-on: ubuntu-latest
    steps:
    - name: Checkout code
      uses: actions/checkout@v3
    - name: Print message
      run: echo "Hello world GA Testing"
run-pytest:
  runs-on: ubuntu-latest
 steps:
- name: Checkout code
  uses: actions/checkout@v3
- name: Setup Python
  uses: actions/setup-python@v3
  with: 
    python-version: 3.9
- name: Install dependecies
  run: |
  python -n pip install --upgrade pip 
  pip install pytest
- name: Run testcases
  run: pytest
