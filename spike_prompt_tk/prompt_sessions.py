from prompt_toolkit import PromptSession, prompt
from pygments.lexers.html import HtmlLexer
from prompt_toolkit.lexers import PygmentsLexer
from prompt_toolkit.shortcuts import prompt
from prompt_toolkit.styles import Style

style = Style.from_dict(
    {
        "": "#ff0066",
        "username": "#884444",
        "at": "#00aa00",
        "colon": "#0000aa",
        "pound": "#00aa00",
        "host": "#00ffff bg:#444400",
        "path": "ansicyan underline",
    }
)

message = [
    ("class:username", "uberdev"),
    ("class:at", "@"),
    ("class:host", "localhost"),
    ("class:colon", ":"),
    ("class:path", "/path/uber"),
    ("class:pound", "# "),
]

# text = prompt("enter html:", lexer=PygmentsLexer(HtmlLexer))
text = prompt(message, style=style, lexer=PygmentsLexer(HtmlLexer))
print(f"Html said: {text}")
