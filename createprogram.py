#string reversal of large text
s = input()
reverse_s = s[::-1]
print(reverse_s)

#string reversal
s = "sai supriya"
reverse_s = s[::-1]
print(reverse_s)

#time complexity
import time
start=time.time()
n=input()
print(n[::-1])
end=time.time()
print(end-start)
