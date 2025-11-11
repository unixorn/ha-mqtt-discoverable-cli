#
# sensor_driver.py
#
# Copyright 2022-2023, Joe Block <jpb@unixorn.net>

"""
Code to support the hmd-create-binary-sensor script
"""

import logging
import sys

from ha_mqtt_discoverable import Settings

from ha_mqtt_discoverable_cli.cli import create_base_parser
from ha_mqtt_discoverable.sensors import BinarySensor, BinarySensorInfo
from ha_mqtt_discoverable_cli.settings import binary_sensor_settings
from ha_mqtt_discoverable_cli.utils import HA_MQTT_DISCOVERABLE_CLI, HA_MQTT_DISCOVERABLE


def binary_sensor_parser():
    parser = create_base_parser(
        description="Create a binary sensor on MQTT that will be automatically discovered by Home Assistant"
    )
    parser.add_argument(
        "--state",
        type=str.upper,
        choices=["OFF", "ON"],
        help="Set the binary sensor's state",
    )
    parser.add_argument("--name", type=str, help="Sensor Name")
    return parser


def binary_sensor_cli():
    parser = binary_sensor_parser()
    cli = parser.parse_args()
    log_level = getattr(logging, cli.log_level.upper(), None)
    log_format = "[%(asctime)s][%(levelname)8s][%(filename)s:%(lineno)s - %(funcName)20s() ] %(message)s"
    logging.basicConfig(level=log_level, format=log_format)
    logging.info("Set log level to %s", cli.log_level.upper())
    return cli


def create_binary_sensor():
    """
    Create a binary sensor from the command line, and set its state.
    """
    cli = binary_sensor_cli()
    if cli.version:
        print(f"ha-mqtt-discoverable-cli version {HA_MQTT_DISCOVERABLE_CLI}")
        print(f"ha-mqtt-discoverable version {HA_MQTT_DISCOVERABLE}")
        sys.exit(0)
    logging.info(f"cli: {cli}")
    settings = binary_sensor_settings(path=cli.settings_file, cli=cli)
    logging.info(f"{settings}")
    mqtt_settings = Settings.MQTT(**settings)
    # Information about the sensor
    sensor_info = BinarySensorInfo(**settings)
    settings = Settings(mqtt=mqtt_settings, entity=sensor_info)
    # Instantiate the sensor
    sensor = BinarySensor(settings=settings)
    if cli.state == "ON":
        sensor.on()
    else:
        sensor.off()
