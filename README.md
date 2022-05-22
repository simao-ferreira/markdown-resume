# Markdown resume

- [how-to](#how-to)
    - [environment](#environment)
    - [requirements](#requirements)
      - [pip freeze](#pip-freeze)
      - [pip tools](#pip-tools)
    - [run](#run)
    - [tests](#tests)
- [technologies](#technologies)

## How to

### Environment

```shell
# Create a new environment
$ python3 -m venv venv

# Activate environment
$ source venv/bin/activate

# Install dependencies
$ pip install -r requirements.txt

# Deactivate
$ deactivate
```

### Requirements

#### Pip freeze

```shell
# Create a requirements file from all installed modules and versions
# If file exist it will need to be deleted
$ pip freeze > requirements.txt

# List outdated packages
$ pip list --outdated

# Update one package
$ pip install -U <package-name>

# Update all
$ pip install -U -r requirements.txt

# Check missing dependencies
$ python -m pip check
```

#### Pip tools

```shell
# Install pip-tools
$ pip install pip-tools

# Generate requirements.txt
$ pip-compile requirements.in

# Update requirements.txt
$ pip-compile --upgrade

# Update single package
$ pip-compile --upgrade-package <package-name>

# Update single package to a specific version
# e.g. --upgrade-package requests==2.0.0
$ pip-compile --upgrade-package <package-name>==<version>
```

### Run

```shell
# Main
$ python main.py

# Scratch files
$ python <module>/<folder>/create_argument_filtered_csv.py <argument>

# Module files
$ python -m <module>.<folder>.file
```

### Tests

```shell
# Run all tests
$ pytest

# Run class test
$ pytest tests/<test_file_name>.py
```

### Technologies

* Python3
* Markdown
* [md2pdf](https://github.com/jmaupetit/md2pdf)