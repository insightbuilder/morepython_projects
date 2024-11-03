from prompt_toolkit import print_formatted_text
from prompt_toolkit.shortcuts import (
    button_dialog,
    checkboxlist_dialog,
    input_dialog,
    message_dialog,
    yes_no_dialog,
)

# message_dialog(title="message me", text="Where you want to go?").run()

# intext = input_dialog(title="Getting text", text="Enter something").run()

# print_formatted_text(intext)

# res = yes_no_dialog(title="Confirm", text="What you want to do?").run()
# print_formatted_text(res)

select_res = button_dialog(
    title="Buttons all over",
    text="Where you want to go",
    buttons=[("Bahamas", 1), ("Mediterranian", 2), ("Blue lagoon", 3)],
).run()

print_formatted_text(f"You selected: {select_res}")

checked_res = checkboxlist_dialog(
    title="Buttons all over",
    text="Where you want to go",
    values=[("Bahamas", "one"), ("Mediterranian", "two"), ("Blue lagoon", "three")],
).run()

print_formatted_text(f"You choose: {checked_res}")
