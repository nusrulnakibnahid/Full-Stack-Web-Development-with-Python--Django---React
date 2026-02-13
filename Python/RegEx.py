import re
text = "Nahid Is a Software Engineer"


#Find all lower case characters alphabetically between "a" and "m"

a = re.findall('[a-z]', text)

print(a)


# Check if the string starts with 'hello'
b = re.match('Nahid',text)
if b:
    print("yes, The string starts with 'Nahid'")

else:
    print("No, The string does not start with 'Nahid'")




# Check if the string ends with 'Engineer'
c = re.findall('Engineer$', text)

if c:
    print("yes,true")

else:
    print("No")



# Special Sequences (Another Example)
#\A
d = re.findall("\ANahid", text)
if d:
    print("yes,true")

else:
    print("No,not true")