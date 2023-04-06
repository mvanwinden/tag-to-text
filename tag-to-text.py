import os
import sys
import re

sourceXML = sys.argv[1]
tagName = sys.argv[2]

if len(sys.argv) != 3:
    print("Usage: python script.py <sourceXML> <tagName> <outputFile> (optional)")
    exit()

# If outputFile is not defined, set it to the name of the sourceXML file plus "_tags.txt"
if len(sys.argv) < 4:
    outputFile = os.path.splitext(os.path.basename(sourceXML))[0] + '_tags.txt'
else:
    outputFile = sys.argv[3]

with open(sourceXML, 'r', encoding='utf-8') as file:
    contents = file.read()

matches = re.findall(f'<{tagName}>(.*?)</{tagName}>', contents, re.DOTALL)

with open(outputFile, 'w', encoding='utf-8') as file:
    for match in matches:
        file.write(match.strip() + '\n')
