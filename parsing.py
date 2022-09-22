# %% [markdown]
# * practice one of the workflows for using HTMLParser
# * use predefined HTML variables with raw content that can be parsed

# %%
content = """
<!DOCTYPE html>
<html class="client-nojs" lang="en" dir="ltr">
<head>
<meta charset="UTF-8"/>
<title>1992 World Junior Championships in Athletics – Men's high jump - Wikipedia</title>
"""

# %%
from html.parser import HTMLParser


class Parser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.recording = False

    def handle_starttag(self, tag, attrs):
        if tag == "title":
            self.recording = True
        else:
            self.recording = False

    def handle_data(self, data):
        if self.recording:
            print(f"Found data for tag: {repr(data)}")


# %% [markdown]
#  The Python repr() built-in function returns the printable representation of the specified object as a string. example shown below '\n'

# %%
p = Parser()
p.feed(content)

# %%
# repr() helps when there are hidden characters that `print()` wouldn't show.
empty = ""
print(f"A string with an empty string var wouldn't show the variable: {empty}")
print(f"A string with an empty string var wouldn't show the variable: {repr(empty)}")

# %% [markdown]
# An alternative you could try is to append the data found to a list instead of printing, and when the parsing is completed, joining the data found. Here is how that would look with an example data.

# %%
captured_data = [
    "1992 World Junior Championships in Athletics – Men's high jump",
    "\n",
    "\n",
    "Wikipedia",
]
print("".join(captured_data))
print(captured_data)
