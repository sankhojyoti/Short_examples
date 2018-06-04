# Add bullet point or stars or hashtags at the begining of each line.

import pyperclip
text = pyperclip.paste()

# Editing the stars in
lines = text.split("\n")
for i in range(len(lines)):
    lines[i] = "# " + lines[i]

# Joining them again
text = "\n".join(lines)

pyperclip.copy(text)
