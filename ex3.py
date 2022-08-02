import re
pattern = re.compile(r'UBa[0-9]+[E/P][A-Z]?[0-9]+')
# matches = partern.finditer

with open('uba.txt', 'r') as file:
    contents = file.read()
    matches = pattern.findall(contents)
    for match in matches:
        print(match)
