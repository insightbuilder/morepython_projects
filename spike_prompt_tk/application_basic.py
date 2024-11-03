from prompt_toolkit import Application
from prompt_toolkit.buffer import Buffer
from prompt_toolkit.layout.containers import VSplit, Window, HSplit
from prompt_toolkit.layout.controls import BufferControl, FormattedTextControl
from prompt_toolkit.layout.layout import Layout
from prompt_toolkit.key_binding import KeyBindings

buffer1 = Buffer()
kb = KeyBindings()


@kb.add("c-q")
def exit_(event):
    """Press ctrl-Q will exit the interface.
    Setting a return value means: quit the event loop"""
    print("Quit")
    event.app.exit()


hsplit = HSplit(
    [
        Window(content=FormattedTextControl(text="Top Half")),
        Window(width=1, char="-"),
        Window(content=FormattedTextControl(text="Bottom Half")),
    ]
)
root = VSplit(
    [
        Window(content=BufferControl(buffer=buffer1)),
        Window(width=1, char="|"),
        # Window(content=FormattedTextControl(text="Hey there")),
        hsplit,
    ]
)
layout = Layout(root)
app = Application(layout=layout, full_screen=True, key_bindings=kb)

app.run()
