def reverse(string):
    if len(string) == 0:
        return string
    else:
        return reverse(string[1:]) + string[0]
x = str(input("Enter a string : "))
print(reverse(x))
