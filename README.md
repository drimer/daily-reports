# daily-reports
Bunch of reports I would like to receive automatically


Setting up development environment
==================================

Ensure you are using the right Python version:

1. Install UV: https://docs.astral.sh/uv/getting-started/installation/

2. Install all dependencies:

.. code-block:: bash

        $ uv sync --all-extras
        $ uv run python --version
        Python 3.10.11

3. Running unit tests:

.. code-block:: bash

    $ uv run pytest

5. Linting:

.. code-block:: bash

    $ uv run flake8 src test --count --max-complexity=10 --max-line-length=120 --show-source --statistics
