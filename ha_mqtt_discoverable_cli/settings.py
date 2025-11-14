#
#    Copyright 2022-2024 Joe Block <jpb@unixorn.net>
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

import logging

from ha_mqtt_discoverable_cli.utils import read_yaml_file

logger = logging.getLogger(__name__)


def load_mqtt_settings(path: str = None, cli=None) -> dict:
    """
    Base settings loader & validator

    Valid characters for object_id and node_id are [a-zA-Z0-9_-]
    """
    try:
        settings = read_yaml_file(path=path)
    except TypeError:
        settings = {}

    settings["debug"] = cli.debug
    # CLI args override stuff in the settings file

    # These are mandatory
    settings["client_name"] = cli.client_name
    settings["device_class"] = cli.device_class
    settings["device_id"] = cli.device_id
    settings["device_name"] = cli.device_name
    settings["password"] = cli.mqtt_password
    settings["host"] = cli.mqtt_server
    settings["port"] = cli.mqtt_port
    settings["username"] = cli.mqtt_user

    # Optional settings - make sure we don't raise an exception if they're unset
    if hasattr(cli, "model"):
        settings["model"] = cli.model
    if hasattr(cli, "icon"):
        settings["icon"] = cli.icon
    if hasattr(cli, "unique_id"):
        settings["unique_id"] = cli.unique_id

    # ssl
    settings["use_tls"] = cli.use_tls
    if cli.use_tls:
        settings["tls_certfile"] = cli.tls_certfile
        settings["tls_key"] = cli.tls_key
        settings["tls_ca_cert"] = cli.tls_ca_cert

    # TODO: refactor code, remove ignore
    # jscpd:ignore-start
    # Validate that we have all the settings data we need
    if "client_name" not in settings:
        raise RuntimeError("No client_name was specified")
    if "device_class" not in settings:
        raise RuntimeError("No device_class was specified")
    if "device_id" not in settings:
        raise RuntimeError("No device_id was specified")
    if "device_name" not in settings:
        raise RuntimeError("No device_name was specified")
    if "port" not in settings:
        raise RuntimeError("You need to specify an mqtt port")
    if "username" not in settings:
        raise RuntimeError("No mqtt_user was specified")
    if "password" not in settings:
        raise RuntimeError("No mqtt_password was specified")
    # jscpd:ignore-end

    return settings


def binary_sensor_settings(path: str = None, cli=None) -> dict:
    """
    Load settings for a binary sensor
    """
    print(cli)
    settings = load_mqtt_settings(path=path, cli=cli)
    settings["state"] = cli.state
    settings["name"] = cli.name
    logger.debug(f"settings: {settings}")
    return settings


def device_settings(path: str = None, cli=None) -> dict:
    """
    Load settings for a device
    """
    settings = load_mqtt_settings(path=path, cli=cli)
    logger.debug(f"settings: {settings}")
    if "unique_id" not in settings:
        raise RuntimeError("No unique_id was specified")
    return settings
