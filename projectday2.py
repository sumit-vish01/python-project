import random

n = int(input("Pickup  number  from 1 to 10 that u like?"))
message = ["Grea job","Nice choice","Welldone","NiceTry","Keepgoing","Newtry"]
if n  % 2 != 0:
    print("ur are looser")
elif n >= 5:
    print('mid winner')
elif n == 5:
    print('u are lucky')
else:
    print('u are final winner')

print(random.choice(message))