import re
text = "Nahid Is a Software Engineer. "


#Find all lower case characters alphabetically between "a" and "m"

a = re.findall('[a-z]', text)

print(a)


# Check if the string starts with 'hello'
b = re.match('Nahid',text)
if b:
    print("yes, The string starts with 'Nahid'")

else:
    print("No, The string does not start with 'Nahid'")