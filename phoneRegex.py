import re

# returns a regex pattern object
# mo is a generic name for "Match objects"
phoneNumRegex = re.compile(r'\d{3}-\d{3}-\d{4}')
mo = phoneNumRegex.search('My number is 415-555-4242')
print('Phone number found: ' + mo.group())

# Use parantheses to produce groupings
phoneNumRex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRex.search('My number is 503-290-6666')
print(mo.group(1))
print(mo.group(2))
print(mo.group(0))
print(mo.group())
print(mo.groups())

areaCode, mainNumber = mo.groups()

print(areaCode)
print(mainNumber)

