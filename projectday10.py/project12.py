import time

seconds = int(input("enter a seconds timer :"))

while seconds > 0:
    print("f left time {seconds} seconds")

    time.sleep(1)

    seconds = seconds - 1

print("time up")