from prompt_toolkit import HTML
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.patch_stdout import patch_stdout
from prompt_toolkit.shortcuts import ProgressBar
from prompt_toolkit import print_formatted_text


import os
import time
import signal

bottom_tb = HTML("<b>[f]</b> Print 'f' <b>[x]</b> Abort")

kb = KeyBindings()
cancel = [False]


@kb.add("f")
def _(event):
    print_formatted_text("Pressed f")


@kb.add("x")
def _(event):
    "Send abort signal"
    cancel[0] = True
    os.kill(os.getpid(), signal.SIGINT)


with patch_stdout():
    with ProgressBar(key_bindings=kb, bottom_toolbar=bottom_tb) as pb:
        for i in pb(range(800)):
            time.sleep(0.01)

            if cancel[0]:
                break
