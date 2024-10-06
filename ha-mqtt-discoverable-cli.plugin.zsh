# Copyright 2024 Joseph Block <jpb@unixorn.net>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Add our plugin's bin diretory to user's path per
# https://zdharma-continuum.github.io/Zsh-100-Commits-Club/Zsh-Plugin-Standard.html#zero-handling

0="${ZERO:-${${0:#$ZSH_ARGZERO}:-${(%):-%N}}}"
0="${${(M)0:#/*}:-$PWD/$0}"

local mqtt_commands_bindir="${0:h}/bin"

if [[ -z "${path[(r)${mqtt_commands_bindir}]}" ]]; then
    path+=( "${mqtt_commands_bindir}" )
fi

# Skipped:
#   incoming-commits  (appears to be a dupe of grab)
#   mark-all-resolved (git: 'conflicts' is not a git command.)
zstyle ':completion:*:*:git:*' user-commands \
  hmd:'Driver script for the hmd command suite ' \
  hmd-create-binary-sensor:'Create an MQTT binary sensor that will be autodetected by Home Assistant' \
  hmd-create-device:'Create a MQTT device that will be autodetected by Home Assistant' \
  hmd-module-info:'Shows the version of the hmd scripts that are installed' \
  hmd-info:'Shows the version of the hmd scripts that are installed' \
  hmd-version:'Show the version of the ha-mqtt-discoverable module that is installed'
