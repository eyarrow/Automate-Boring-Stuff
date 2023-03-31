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

phoneNumRegex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My phone number is (503) 290-7777.')
print(mo.group(1))
print(mo.group(2))

heroRegex = re.compile(r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey')
print(mo1.group())

mo2 = heroRegex.search('Tina Fey and Batman')
print(mo2.group())

# Search for Batman, Batmobile, Batcopter, Batbat
batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost its wheel')
print(mo.group())

# The question mark deals with optional Characters
batRegex = re.compile(r'Bat(wo)?man')
mo = batRegex.search('The adventures of Batman')
print(mo.group())

# We can use this to help the program identify phone numbers with the area code
# as optional

phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo = phoneRegex.search('my phone number is 290-6666')
mo2 = phoneRegex.search('my phone number is 503-290-6666')
print(mo.group())
print(mo2.group())

