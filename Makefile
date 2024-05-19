.PHONY: c clean \
	f format \
	h help \
	local \
	multiarch_image \
	publish \
	t test \
	version \
	wheel

h: help
c: clean
f: format
t: test

help:
	@echo "Options:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

# If this pukes trying to import paho, try running 'poetry install'
MODULE_VERSION=$(shell grep '^version' pyproject.toml | cut -d= -f2 | sed s/\"//g | sed s/\ //g)

version:
	@echo "version: $(MODULE_VERSION)"

clean: ## Cleans out stale wheels, generated tar files, .pyc and .pyo files
	rm -fv dist/*.tar dist/*.whl
	find . -iname '*.py[co]' -delete

format: ## Runs 'ruff' on all our python source files
	poetry run ruff check .

test: ## Run tests with 'nosetests'
	nosestests -v

install_hooks: ## Install the git hooks
	poetry run pre-commit install

local: wheel requirements.txt ## Makes a docker image for only the architecture we're running on. Does not push to dockerhub.
	docker buildx build --load -t unixorn/ha-mqtt-discoverable-cli-testing -f Dockerfile.testing .

trial: wheel requirements.txt
	docker buildx build --build-arg application_version=${MODULE_VERSION} --load -t unixorn/ha-mqtt-discoverable-cli-testing:$(MODULE_VERSION) -f Dockerfile.testing .
	docker buildx build --build-arg application_version=${MODULE_VERSION} --load -t unixorn/ha-mqtt-discoverable-cli-testing -f Dockerfile.testing .

multiarch_image: wheel ## Makes a multi-architecture docker image for linux/arm64, linux/amd64 and linux/arm/v7 and pushes it to dockerhub
	docker buildx build --no-cache --build-arg application_version=${MODULE_VERSION} --platform linux/arm64,linux/amd64,linux/arm/v7 --push -t unixorn/ha-mqtt-discoverable-cli:$(MODULE_VERSION) .
	docker buildx build --build-arg application_version=${MODULE_VERSION} --platform linux/arm64,linux/amd64,linux/arm/v7 --push -t unixorn/ha-mqtt-discoverable-cli .
	docker pull unixorn/ha-mqtt-discoverable-cli
	docker pull unixorn/ha-mqtt-discoverable-cli:${MODULE_VERSION}

wheel: clean format ## Builds a wheel for our modules. 'poetry' bakes the dependencies into the wheel metadata.
	poetry build

publish: multiarch_image ## Builds a multi-architecture docker image and publishes the module to pypi
	poetry publish

# We use this to enable the Dockerfile.testing have a separate layer for the
# dependencies so we don't have to reinstall every time we test a new change.
# Our wheel includes its dependencies in the metadata so you don't need a
# requirements.txt file to use them
requirements.txt: poetry.lock pyproject.toml Makefile ## Builds a requirements.txt to Dockerfile.testing can cache installing the python dependencies. poetry includes the deps in our wheel metadata, requirements.txt is not needed other than for test images.
	poetry export -o requirements.txt
