import re

text="The quick brown fox jumps over the lazy dog"

match=re.search("brown",text)
print(match)
if match:
    print("Match is found")
    print("Start index:",match.start())
    print("End index:",match.end())

mt=re.findall("the",text,re.IGNORECASE)
print("Matches:",mt)

new=re.sub("fox","cat",text)
print(new)