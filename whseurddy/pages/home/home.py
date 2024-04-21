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

"""
A page of the application.
Page content is imported from the home.md file.

Please refer to https://docs.taipy.io/en/latest/manuals/gui/pages for more details.
"""

from taipy.gui import Markdown
import taipy.gui.builder as tgb
import random

transition0 = True
transition1 = False
transition2 = False

with tgb.Page() as home:
    with tgb.part(render="{transition0}"):
        # coin
        # src: https://dribbble.com/shots/1466662-Heads-tails
        # tgb.image(content="https://cdn.dribbble.com/users/120141/screenshots/1466662/800x600_dribbble.gif", label="Coin", on_action=(lambda x: x), class_name="")

        # page title
        tgb.text("Describe", mode="md")

        # input box
        tgb.input("What decision are you making?")

        # descripion
        tgb.text("HEADS is Yes\nTails is No")

        # button
        def on_press(state):
            state.transition0 = False
            state.transition1 = True
        tgb.button(label="Flip", on_action=on_press, class_name="")

    with tgb.part(render="{transition1}"):
        # coin spinning
        tgb.image(content="url", label="Coin", on_action=(lambda x: x), class_name="")

    with tgb.part(render="{transition2}"):
        # coin
        tgb.image(content="url", label="Coin", on_action=(lambda x: x), class_name="")

        # result
        get_rand_result = lambda: 'Yes' if (random.randint(0, 1) == 1) else 0
        tgb.text(f"The result is... {get_rand_result()}")

        # quote
        tgb.text("<Motivational quote")
