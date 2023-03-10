# Contributing

## Setup

`ha-mqtt-discovery-cli` uses [poetry](https://python-poetry.org/) to manage module dependencies and make packaging the module easier. Once you install `poetry`, run `poetry install` to have it create a venv for you to use during development.

This module is meant to contain entrypoints for functions provided by the [ha-mqtt-discoverable](https://github.com/unixorn/ha-mqtt-discovery) module. If you're adding functionality that isn't just a new entrypoint, it probably belongs in the `ha-mqtt-discoverable` module and not here.

We use [pre-commit](https://pre-commit.com/) to run our pre-commit/postcheckout etc `git` hooks.  Please run `pre-commit install` at the root of the repository to enable automatic handling of the `git` pre-commit scripts. This won't affect any of your other repositories, just this one. The pre-commit scripts run `black` on the `.py` files that you are committing along with some other checks (preventing accidental large file additions, merge conflict checks, whitespace trimming, etc). Their configuration is managed in [.pre-commit-config.yaml](https://github.com/unixorn/ha-mqtt-discoverable-cli/blob/main/.pre-commit-config.yaml.

## Contribution Guidelines

- PRs should include readme updates with code examples for any added/changed/removed entrypoint scripts.
- Please use `pydantic` to validate input settings and provide default values.
- Please use Google-style docstrings - see their [style guide](https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings) for details.

## Linting the project files

This project uses [Megalinter](https://megalinter.io/latest/) to check the codebase automatically using Github Actions.

It is also possible to run the linter locally to better understand the problems and check the code before a commit.
You can use the [mega-linter-runner](https://megalinter.io/latest/mega-linter-runner/#installation), if you have `Node` and `Docker` locally available.

To run all the linters as configured in the `.mega-linter.yml` file, use:

```bash
npx mega-linter-runner --flavor python
```

It will print out the results in the console, as well as generate a `megalinter-reports` directory with all its reports.
