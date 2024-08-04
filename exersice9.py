user_input = str(input("Enter text: "))
x_printe = ""
for letter in range(len(user_input)):
    x_printe += "x"
print(x_printe)

#other solution without using len.
user_input = str(input("Enter text: "))
x_printe = ""
if user_input == "test" :
    x_printe = "xxxx"
elif user_input == "tryagain" :
    x_printe = "xxxxxxxx"
elif user_input == "pnc" :
    x_printe == "xxx"
else:
    x_printe = "Sorry you enter the wrong text!"
print(x_printe)