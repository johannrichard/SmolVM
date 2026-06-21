# Copyright 2026 Celesto AI
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

"""GitHub Copilot CLI preset."""

from __future__ import annotations

from smolvm.presets._scripts import NODE20_BOOTSTRAP, npm_install_global
from smolvm.presets._types import Preset

COPILOT_PRESET = Preset(
    name="copilot",
    summary="Start a sandbox with GitHub Copilot CLI preinstalled.",
    setup_script=NODE20_BOOTSTRAP,
    install_script=npm_install_global("@github/copilot"),
    host_env_vars=("COPILOT_GITHUB_TOKEN",),
    launch_command="copilot",
    no_env_hint=(
        "No Copilot token found. Set COPILOT_GITHUB_TOKEN on your machine, or run"
        " 'copilot login' inside the sandbox."
    ),
)
