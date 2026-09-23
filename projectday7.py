#quix game making using python
print("Welocome to my computer quiz!")

playing = input("Do you want to play?")

if playing.lower() != "yes":
    # print("ouit")
    quit()

print("Okay! Let's play :)")

answer = input("What does CPU stand for?")

if answer.lower() == "central processing unit":
  print("Correct!")
else:
   print("Incorrect!")


answer = input("What does GPU stand for?")

if answer.lower() == "graphic processing unit":
  print("Correct!")
else:
   print("Incorrect!")


answer = input("What does RAM stand for?")

if answer.lower() == "random access memory":
  print("Correct!")
else:
   print("Incorrect!")


answer = input("What does PSU stand for?")

if answer.lower() == "power supply":
  print("Correct!")
else:
   print("Incorrect!")
