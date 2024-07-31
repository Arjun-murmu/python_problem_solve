print("Hello")
print("Welcome our game.")
print("Level no 1.")
print("What is the value of 15+15 ? ")
user_input = int(input("My answer : "))
if user_input == 30:
    print("WOW Nice.")
    print("Level No 2.")
    print("What is the value of 25*25 ? ")
    user_input_l2 = int(input("My answer : "))
    if user_input_l2 == 625:
        print("That greate.")
        print("Level No 3.")
        print("What is the area of square (side = 12) ? ")
        user_input_l3 = float(input("My answer : "))
        if user_input_l3 == 144:
            print("That greate.")
            print("Level No 4.")
            print("What is the capital of india ? ")
            print("Note : plese enter capitalization style/small latter.")
            user_input_l4 = input("My answer : ")
            if (user_input_l4 == "New Delhi") or (user_input_l4 == "new delhi"):
                print("Good knowalage.")
                print("Final Level.")
                print("Note : plese enter capitalization style/small latter.")
                user_input_l5 = input("Odisha is known for its classical dance form called: ")
                if (user_input_l5 == "Odissi") or (user_input_l5 == "odissi"):
                    print("Congradulation.")
                    print("Your are selected.")
                    print("Your Feedback: ")
                    print("""
                    1. Good Question.
                    2. Normal question.
                     3. Essay Question.
                     4. other.""")
                    user_f = int(input("Choice one number (1 to 4) : "))
                    if user_f == 1:
                        print("Thank you , give the feedback.")
                    elif user_f == 2:
                        print("OK,Thank you.")
                    elif user_f == 3:
                        print("Ok, Thank you.\n i try give hard time question.")
                    elif user_f == 4:
                        user_prom = input("Ok, Write your problem here : ")
                        print("Thank you , give me the feedback.")
                    else:
                        print("Invalid Number.")
                else:
                    print("re attempt the exam.")
            else:
                print("Wrong answer re attempt the exam.")
        else:
            print("re attempt the exam.")
    else:
        print("Pless check the math formula, and give repeat exam.")
else:
    print("You give wrong answer, Basic math.")
    print("You perpare caurfully and give next time best.\n all the best.")
print("Thanks you.")
