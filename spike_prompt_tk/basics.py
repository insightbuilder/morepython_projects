# gettin simple prompt
from prompt_toolkit import prompt
from prompt_toolkit import print_formatted_text, HTML
from prompt_toolkit.styles import Style

# text = prompt("Do you have a name? ")
text = "ansired"
print(f"You said: {text}")
print_formatted_text(f"You said: {text}")

# color = prompt("What is the color: ")
color = "ansiwhite"
print_formatted_text(HTML(f"<{color}>this is {color} text</{color}>"))

style = Style.from_dict(
    {
        "aaa": "#ff0066",
        "bbb": "#44ff00 italic",
    }
)

print_formatted_text(HTML("<aaa>Helllo</aaa> <bbb>world</bbb>"))
