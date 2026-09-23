# Simple Quiz Game
print("What is the capital of india?")
print("1 Delhi")
print("2 Mumbai")
print("3 haryana")
print("4 Uttar pradesh")

user_choice = input("Choose number btw 1- 4: ")
score = 0

if user_choice == "1":
    print("Correct answer")
    score += 1
      
else:
    print("Incorrect answer")

print("What is the know as pink city?")
print("1 Delhi")
print("2 jaipur")
print("3 haryana")
print("4 Uttar pradesh")

user_choice = input("Choose number btw 1- 4: ")

if user_choice == "2":
    print("Correct answer")
    score += 1
else:
    print("Incorrect answer")
   

print("What is the national bird of india?")
print("1 peakcook")
print("2 sparrow")
print("3 owl")
print("4 crow")

user_choice = input("Choose number btw 1- 4: ")

if user_choice == "1":
    print("Correct answer")
    score += 1
else:
    print("Incorrect answer")
    

print("What is the short form of central processing unit?")
print("1 RAM")
print("2 GPU")
print("3 CPU")
print("4 USC")

user_choice = input("Choose number btw 1- 4: ")

if user_choice == "3":
    print("Correct answer")
    score += 1
else:
    print("Incorrect answer")
  

print("What is the Prime minister of india?")
print("1 Pm modi")
print("2 Rahul gandhi")
print("3 bhajpa")
print("4 chai wala")

user_choice = input("Choose number btw 1- 4: ")

if user_choice == "1":
    print("Correct answer")
    score += 1
else:
    print("Incorrect answer")

print("you got" +str(score) + "question correct!")
print("You got" + str((score / 5) * 100) + "%.")