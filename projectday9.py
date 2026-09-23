#project day 9 try to build anything using ourmindset

n = (input("Check your mobile number?:"))
m = (input("please tell me your date of birth:?"))

if len(n) == 10 and m == "2009":
    print("Mobile number or dob dono sahi ha ....")
elif len(n) != 10:
     print("Mobile nummber is correct but DOB is wrong")
elif len(m) != "2009":
       print("Mobile nummber is wrong but DOB is correct")
elif len(n)  ==  9:
    print("invalid number")
else:
    print("checking is in the processs")



