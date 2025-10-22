


#this is a raw string r""
# print(r'\tTab')



import re 
text="""abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTU
VWXYZ1234567890


Ha HaHa
Metacharaters (need to be escaped):
. ^ $ * + { } [ ]  | ( )
coreysms.com
321-112-112-4564
Mr. mani
mr smith"""
#pattern = re.compile(r'abc')
#need to keep backslsh for period "."
#"d" mateches 0-9 and oppisite "D" 
# 'w' word charatecerssame like digits,'s' same spaces

"""anchors 
word boundary"""


# pattern = re.compile(r'\d')
pattern = re.compile(r'\BHa')


matches = pattern.finditer(text)


for match in matches:
    print(match)
