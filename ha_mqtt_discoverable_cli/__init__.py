#    Copyright 2022-2023 Joe Block <jpb@unixorn.net>
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

from importlib import metadata

__version__ = metadata.version(__package__)


def module_version():
    print(__version__)


def module_info():
    m = metadata.metadata(__package__)
    print(m["Summary"])
    print(f"Version: {__version__}")
    print()
    print("Commands:")
    for command_name in metadata.entry_points()["console_scripts"]:
        if command_name.value.split(".")[0] == __package__:
            print(f" - {command_name.name}")
    print()
    print("Run commands with '--help' for usage details.")
