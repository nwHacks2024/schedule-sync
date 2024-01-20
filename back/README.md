Create a Python virtual environment.
  13     python3 -m venv env
  14
  15 Upgrade packaging tools.
  16     env/bin/pip install --upgrade pip setuptools
  17
  18 Install the project in editable mode with its testing requirements.
  19     env/bin/pip install -e ".[testing]"
  20
  21 Run your project's tests.
  22     env/bin/pytest
  23
  24 Run your project.
  25     env/bin/pserve development.ini
