[![Python application test with GitHub Actions](https://github.com/ngothanhtinh/python-for-devops/actions/workflows/devops.yml/badge.svg)](https://github.com/ngothanhtinh/python-for-devops/actions/workflows/devops.yml)

# python-for-devops

## Scaffold

```.
|---libs
|   |---__init__.py
|   |---logic.py
|---Makefile
|---requirements.txt
|---Source
|---test
|---Dockerfile
|---[IAC]
```

## Step-by-step

**1. Creat a Python Virtual Environment**
   - Windows:
     - `python3 -m venv .venv` or `virtualenv .venv`
     - `.\.venv\Scripts\activate`
   - Mac:
     - `python3 -m venv ~/.venv` or `virtualenv ~/.venv`
     - `vim ~/.bashrc`: `source ~/.venv/bin/activate`

**2. Creat empty file and folder**
- Windows/Mac:
     - `touch requirement.txt`
     - `touch Dokerfile`
     - `touch Makefile`
     - `mkdir libs`
     - `touch libs/__init__.py`
     - `touch libs/logic.py`
     - `touch main.py`

**3. Populate `Makefile`**
```.makefile
install:
    # install commands
format:
    # format code
lint:
    #flake8 or #pylint
test:
    #test
deploy:
    #deploy
all: install lint test deploy
```
- `make install`
- `make format`
- ...

**4. Populate `requirements.txt`**
- Windows: `py -m pip freeze`
- macOS: `python -m pip freeze`

**5. Setup Continuous Integration (CI) `.github/workflows/devops.yml`**
- Configure `Deploy to Amazon ECS`
```.
name: Python application test with GitHub Actions
on: [push]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Set up Python 3.9
        uses: actions/setup-python@v5
        with:
          python-version: 3.9
      - name: Install dependencies
        run: |
          make install
          python -m textblob.download_corpora
      - name: Lint with pylint
        run: |
          make lint
      - name: Test with pytest
        run: |
          make test
      - name: Format code
        run: |
          make format
      - name: Build container
        run: |
          make build
```

**6. Build cli using Python Fire library `cli-fire.py`**
- Windows cmd: `cli-fire.py phrase --name "Ho Chi Minh"`
- macOS: `chmod +x cli-fire.py`, `./cli-fire.py --help`
- Use: ipython `exit()`
