#
# device_driver.py
#
# Copyright 2022-2023, Joe Block <jpb@unixorn.net>

"""
Code to support the hmd-create-device script
"""

import json
import logging
import sys


from ha_mqtt_discoverable_cli.cli import create_base_parser
from ha_mqtt_discoverable_cli.device import Device
from ha_mqtt_discoverable_cli.settings import device_settings
from ha_mqtt_discoverable_cli.utils import HA_MQTT_DISCOVERABLE_CLI, HA_MQTT_DISCOVERABLE


def device_parser():
    parser = create_base_parser(description="Create a MQTT device entry that will be discoverable by Home Assistant")
    parser.add_argument(
        "--manufacturer",
        type=str,
        help="Name to set device manufacturer",
    )
    parser.add_argument(
        "--metric-data",
        type=str,
        required=True,
        action="append",
        help="Metric data to create on device. JSON format.",
    )
    parser.add_argument(
        "--model",
        type=str,
        required=True,
        help="What model for the created MQTT device",
    )
    return parser


def device_cli():
    parser = device_parser()
    cli = parser.parse_args()
    log_level = getattr(logging, cli.log_level.upper(), None)
    log_format = "[%(asctime)s][%(levelname)8s][%(filename)s:%(lineno)s - %(funcName)20s() ] %(message)s"
    logging.basicConfig(level=log_level, format=log_format)
    logging.info("Set log level to %s", cli.log_level.upper())
    return cli


def create_device():
    """
    Create a device from the command line, and set its state.
    """
    cli = device_cli()
    if cli.version:
        print(f"ha-mqtt-discoverable-cli version {HA_MQTT_DISCOVERABLE_CLI}")
        print(f"ha-mqtt-discoverable version {HA_MQTT_DISCOVERABLE}")
        sys.exit(0)
    logging.debug(f"cli: {cli}")
    settings = device_settings(path=cli.settings_file, cli=cli)
    sensor = Device(settings=settings)
    for raw in cli.metric_data:
        try:
            metric_data = json.loads(raw)
        except json.JSONDecodeError:
            logging.error(f"{raw} is not valid JSON, skipping!")
            continue
        logging.debug(f"metric_data = {metric_data}")

        if "name" not in metric_data:
            logging.error(f"No name provided in {raw}")
            continue
        if "value" not in metric_data:
            logging.error(f"No value provided in {raw}")
            continue
        if "configuration" not in metric_data:
            configuration = {"name": metric_data["name"], "value": metric_data["value"]}
            logging.warning(f"No configuration provided in {raw}, creating {configuration}")
        else:
            configuration = metric_data["configuration"]

        sensor.add_metric(
            name=metric_data["name"],
            value=metric_data["value"],
            configuration=configuration,
        )
    sensor.publish()
