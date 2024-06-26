# Copyright 2021-2024 Avaiga Private Limited
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with
# the License. You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
# an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
# specific language governing permissions and limitations under the License.
import taipy as tp
from taipy.gui import Gui

from taipy import Core
from pages import *

stylekit = {
    "color_background_light": "#38A296",
    "color_background_dark": "#38A296",
    "color_primary": "#ffffff",
    "root_margin": 0
}


if __name__ == "__main__":
    core = Core()
    core.run()
    # #############################################################################
    # PLACEHOLDER: Create and submit your scenario here                           #
    #                                                                             #
    # Example:                                                                    #
    # from configuration import scenario_config                                   #
    # scenario = tp.create_scenario(scenario_config)                              #
    # scenario.submit()                                                           #
    # Comment, remove or replace the previous lines with your own use case        #
    # #############################################################################

    gui = Gui(page=home)
    gui.run(title="Noracle", stylekit=stylekit, css_file='main.css')
