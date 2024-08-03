userINPUT = int(input("The Number: "))
userMessage = ""
if userINPUT < 0:
    userMessage = "Negative Number!"
else:
    userMessage = "Positve Number!"
print(userMessage)