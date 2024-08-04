word = str(input("Enter word: "))
number = int(input("Enter number: "))
message = ""
if len(word) >= 7 and len(word)<=15 and number >= 7 and number <= 15:
   message = ("IT's good.")
else:
    message = ("IT's bad.")
print(message)