import re
value="this is a string"
output=re.search("^this.*string$,value")
print(output)