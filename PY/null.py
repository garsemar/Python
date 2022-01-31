import re

match = re.match(r"Goodbye", "Hello, World!")
print(match)
if match is None:
    print("It doesn't match.")
