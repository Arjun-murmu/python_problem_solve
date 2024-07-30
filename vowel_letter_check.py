#Vowel latter or not
letter = input("Enter any one latter A-Z OR a-z : ")
if (letter in "a,e,i,o,u") or (letter in "A,E,I,O,U"):
    print("It is vowel.")
else:
    print("Not vowel.")
