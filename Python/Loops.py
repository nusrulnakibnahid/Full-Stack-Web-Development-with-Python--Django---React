#While Loop
nahid = 1

while nahid < 10:
    print("Myself Nahid", nahid)

    nahid = nahid +1


# while loop (break statement)
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1



# while loop (continue statement)
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)


# while loop (else statement)
i = 1
while i < 6:
   print(i)
   i += 1
else:
   print("i is no longer less than 6")









#For Loop
name = ["N", "A", "H", "I", "D"]

for x in name:
    print(x)



# For loop (break statement)
fruits = ["apple", "banana", "cherry", "orange"]
for a in fruits:
   
   if a == "cherry":
      break
   print(a)



# For loop (continue statement)
a = ["x", "y", "z", "w"]

for b in a:
   if b == "z":
      continue
   print(b)