#number digit check
num = int(input("Enter any number : "))
if num>=0 and num < 9:
    print("Number is single digit.")
elif num>=10 and num<99:
    print("Number is two digit.")
elif num>=100 and num<999:
    print("Number is three digit.")
elif num>=1000 and num<9999:
    print("Number is four digit.")
elif num>=10000 and num<99999:
    print("Number is five digit.")
else:
    print("Number is more then five digit.")
