# ha-mqtt-discoverable-cli

[![License](https://img.shields.io/github/license/unixorn/ha-mqtt-discoverable-cli.svg)](https://opensource.org/license/apache-2-0/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![GitHub last commit (branch)](https://img.shields.io/github/last-commit/unixorn/ha-mqtt-discoverable-cli/main.svg)](https://github.com/unixorn/ha-mqtt-discoverable-cli)
[![Downloads](https://static.pepy.tech/badge/ha-mqtt-discoverable-cli)](https://pepy.tech/project/ha-mqtt-discoverable-cli)

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
## Table of Contents

- [Installing](#installing)
  - [Native install](#native-install)
  - [Docker](#docker)
  - [ZSH Frameworks](#zsh-frameworks)
- [Scripts Provided](#scripts-provided)
  - [`hmd`](#hmd)
  - [`hmd create binary sensor`](#hmd-create-binary-sensor)
  - [`hmd create device`](#hmd-create-device)
- [Contributing](#contributing)
- [Contributors](#contributors)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

This repository contains CLI scripts for CRUD operations on MQTT entities that will be autodetected by Home Assistant.

It is a set of wrapper scripts for the [ha-mqtt-discoverable](https://github.com/unixorn/ha-mqtt-discoverable) python module.

## Installing

### Native install

`pip install ha-mqtt-discoverable-cli` will install the cli tools. If you prefer to keep your system python clear of extra modules, you can use the `unixorn/ha-mqtt-discoverable-cli` docker image instead.

### Docker

If you only need to use the command line tools, the simplest way is to use them with `docker` or `nerdctl`. It won't interfere with your system python and potentially cause you issues there.

You can use the [unixorn/ha-mqtt-discoverable-cli](https://hub.docker.com/repository/docker/unixorn/ha-mqtt-discoverable-cli) image on dockerhub directly, but if you add `$reporoot/bin` to your `$PATH`, the `hmd` script there will automatically run the command line tools inside a docker container with `docker` or `nerdctl`, depending on what it finds in your `$PATH`.

### ZSH Frameworks

You can load the tools with your ZSH framework of choice by referring to `unixorn/ha-mqtt-discoverable-cli`.

If you're using [Zgenom](https://github.com/jandamm/zgenom):

1. Add `zgenom load unixorn/ha-mqtt-discoverable-cli` to your `.zshrc` along with your other `zgenom load` commands.
2. `zgenom reset && zgenom save`


## Scripts Provided

The `ha_mqtt_discoverable-cli` module installs the following helper scripts you can use in your own shell scripts.

### `hmd`

Uses the [gitlike-commands](https://github.com/unixorn/gitlike-commands/) module to find and execute `hmd` subcommands. Allows you to run `hmd create binary sensor` and `hmd` will find and run `hmd-create-binary-sensor` and pass it all the command line options.

### `hmd create binary sensor`

Create/Update a binary sensor and set its state.

Usage: `hmd create binary sensor --device-name mfsmaster --device-id 8675309 --mqtt-user HASS_MQTT_USER --mqtt-password HASS_MQTT_PASSWORD --client-name inquisition --mqtt-server mqtt.unixorn.net --metric-name tamper --device-class motion --state off`

### `hmd create device`

Create/Update a device and set the state of multiple metrics on it.

Usage: `hmd create device --device-name coyote --device-id 8675309 --mqtt-user HASS_MQTT_USER --mqtt-password HASS_MQTT_PASSWORD --mqtt-server mqtt.example.com --model 'Rocket Skates' --manufacturer 'Acme Products' --metric-data '{"name":"Left Rocket Skate","value":93}' --metric-data '{"name":"Right Rocket Skate","value":155}' --unique-id 'hmd-26536'`

## Contributing

Please run `black` on your code before submitting. There are `git` hooks already configured to run `black` and other checks before every commit, please run `pre-commit install` to enable them.

## Contributors

<a href="https://github.com/unixorn/ha-mqtt-discoverable-cli/graphs/contributors">
  <img src="https://contributors-img.web.app/image?repo=unixorn/ha-mqtt-discoverable-cli" />
</a>

Made with [contributors-img](https://contributors-img.web.app).
