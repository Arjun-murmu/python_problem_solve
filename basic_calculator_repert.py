while True:
    i = int(input("Enter a first number : "))
    j = int(input("Enter a second number : "))
    print(i,"+",j," = ",i+j)
    print(i,"-",j, " = ", i - j)
    print(i, "*", j, " = ", i * j)
    print(i, "/", j, " = ", i / j)
    repert = input("Do you want to continue this programm : ")
    if (repert == "no") or (repert in "N,n") or (repert == "NO"):
        break
