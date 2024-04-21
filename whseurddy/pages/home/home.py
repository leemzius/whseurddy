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
# from bkend.noracle import get_chat_completion 
from bkend.flip import coin_flip
import threading, time

transition0 = True
transition1 = False
transition2 = False
is_heads = False
is_tails = False
question = ""
quote = ""
get_chat_completion = lambda x, y: x
outcome = coin_flip()

with tgb.Page() as home:
    with tgb.part(render="{transition0}"):
        # coin
        # src: https://dribbble.com/shots/1466662-Heads-tails
        tgb.image(content="../../assets/coinflip.gif", label="Coin")

        # page title
        tgb.text("Noracle", id="title")
        tgb.text("Flip a coin. Save time.", id="subtitle")

        # input box
        #save the user input
        tgb.input("{question}", multiline=True, lines_shown=3, id="question", hover_text="Placeholder")

        # descripion
        tgb.text("Heads is No.")
        tgb.text("Tails is Yes.")

        # button
        def on_press(state):
            state.transition0 = False
            state.transition1 = True
            state.outcome = outcome
            state.is_tails = outcome == 'Tails'     
            state.quote = get_chat_completion(state.question, outcome)

            if outcome == 'Heads':
                state.is_heads = True
                time.sleep(3.42 + 0.05)
                state.transition1 = False
                state.transition2 = True
            else:
                state.is_tails = True
                time.sleep(4.35 + 0.05)
                state.transition1 = False
                state.transition2 = True

        tgb.button(label="Flip", on_action=on_press, class_name="")

    with tgb.part(render="{transition1}"):
        # coin spinning
        with tgb.part(render="{is_heads}"):
            tgb.image(content="../../assets/coinflip-heads.gif", label="Coin", id='mid', class_name="")
        with tgb.part(render="{is_tails}"):
            tgb.image(content="../../assets/coinflip-tails.gif", label="Coin", id='mid', class_name="")

    with tgb.part(render="{transition2}"):
        # coin
        with tgb.part(render="{is_heads}"):
            tgb.image(content="../../assets/heads.png", label="Coin", class_name="")
        with tgb.part(render="{is_tails}"):
            tgb.image(content="../../assets/tails.png", label="Coin", class_name="")

        # result
        # quote = get_chat_completion(question, outcome)
        tgb.text(f"The result is... {outcome}")
        tgb.text("{quote}")
