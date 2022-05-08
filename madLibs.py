#! python3
# mad libs program reading a file, taking input from a user for replacements and saving processed text into another file
import re
sourcePath = 'madLibs'
# import source text into variable
with open(f'{sourcePath}.txt') as src:
    text = src.read()
# compile regex object for replaced text
rgx = re.compile(r'(ADJECTIVE|ADVERB|NOUN|VERB)')
# find all strings to be replaced
found = rgx.findall(text)
# replace all strings
for element in found:
    element = element.lower()
    # ask for input
    tmp = input('Enter ' + ('an ' if element[0] in 'aeiou' else 'a ') + f'{element}:\n')
    # replace text
    text = re.sub(rgx, tmp, text, count=1)
# print out result
print('Processed text:\n', text)
# save processed text into a file
with open(f'{sourcePath}Output.txt', 'w') as output:
    output.write(text)