from ha_mqtt_discoverable_cli import __version__


def test_read_version():
    assert __version__ is not None
