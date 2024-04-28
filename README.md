## Django Basic Setup

# Table of Content

- [ ] 1. Setup code formatting
- [ ] 2. Setup isort
- [ ] 3. Setup mypy
- [ ] 4. Setup pylint
- [ ] 5. Setup pre-commit
- [ ] 6. GHA workflow
- [ ] 7. Model with test
- [ ] 8. FormAPI based form with test
- [ ] 9. Model Form based form with test
- [ ] 10. Function base CRUD view with test
- [ ] 11. Class based CRUD view with test
- [ ] 12. Custom template tag with test
- [ ] 13. Custom template filter with test
- [ ] 14. Context processor with test
- [ ] 15. Middleware with test

# Setup

- If pip is not in your system
  ```
  $ sudo apt-get install python-pip
  ```
- Then install virtualenv
  ```
  $ pip install virtualenv
  ```
- Create Virtual Environment
  ```
  python3 -m venv .venv
  ```
- Activate venv
  ```
    source .venv/bin/activate
  ```
- ## Install django and add django app , take help from django official docs

  see documentation [here](https://docs.djangoproject.com/en/4.2/intro/tutorial01/)

- ## Setup mypy

  - References

    - [here](https://www.ralphminderhoud.com/blog/django-mypy-check-runs/)
    - [here](https://kracekumar.com/post/type_check_your_django_app/)

  - Install mypy for type checking
    ```
     pip install mypy
    ```
  - Install django stubs for django type checking

    ```
    pip install django-stubs
    ```

  - Configure django-stubs mypy plugin -

    - Create a mypy.ini configuration file at the top-level of your project added the plugin to the config.

      ```
      [mypy]
      pretty = True
      strict = True
      show_error_codes = True
      show_error_context = True
      show_column_numbers = True
      namespace_packages = True
      plugins = mypy_django_plugin.main
      mypy_path=./basic_setup

      # Throwing errors on migrations so we wanted to ignore errors on the migrations
      [mypy-*.migrations.*]
      ignore_errors = True

      [mypy.plugins.django-stubs]
      django_settings_module = "basic_setup.settings"
      ```

- ## Setup isort

  - References

    - [here](https://github.com/timothycrosley/isort/wiki/isort-Settings)

  - Install isort for type checking

    ```
     pip install isort
    ```

    - Configure isort plugin -
    - Create a isort.cfg configuration file at the top-level of your project added the plugin to the config.

      ```
      # https://github.com/timothycrosley/isort/wiki/isort-Settings
      [settings]

      ; Used when our repo import something from other repo so commented now
      ; default_section = THIRDPARTY
      include_trailing_comma = true
      sections=FUTURE,STDLIB,TESTING,FIRSTPARTY,LOCALFOLDER
      use_parentheses = true
      verbose = true
      skip_glob = **/migrations/*
      ```

- ## Setup python formatter

  - Reference Links

    - [black](https://black.readthedocs.io/en/stable/)
    - [Blog Link](https://ctrlzblog.com/how-to-set-up-black-to-automatically-format-your-django-project/)

  - Install black

    ```bash
    pip install black
    ```

  - Run black

    ```bash
    black .
    ```

  - Check black formatting

    ```bash
    black --check .
    ```

  - If you are using vscode, you need to add this in settings.json, it will organize import and remove unused import on save

    ```json
    {
      "editor.formatOnSave": true,
      "[python]": {
        "editor.defaultFormatter": "ms-python.black-formatter",
        "source.unusedImports": true
      }
    }
    ```

  ## Setup pylint

  - Reference Links

    - [pylint](https://github.com/PyCQA/pylint/)

    - [pylint-django](https://github.com/PyCQA/pylint-django/)

    - Blog: [How to setup pylint for django project](https://dkolodzey.medium.com/pylint-django-with-github-actions-2e3ef05dd34a)

  - Install pylint for code analysis and linting

    ```bash
    pip install pylint
    ```

  - Install pylint-django pylint plugin

    ```bash
    pip install pylint-django
    ```

  - Create pylint config file if you want to customize

    ```bash
    pylint --generate-rcfile > .pylintrc
    ```

  - Add pylint_django in load-plugins to pylint config file

    ```text
    [MASTER]
    load-plugins=pylint_django
    ```

  - Add django settings module in pylint config file

    ```text
    [pylint-django]
    django-settings-module=<project_name>.settings
    ```

  - Run pylint

    ```bash
    pylint **/*.py
    ```

  - NOTE: if you not want to create pylint config file, you can run pylint with

    ```bash
    pylint --load-plugins=pylint_django --django-settings-module=<project_name>.settings **/*.py
    ```
