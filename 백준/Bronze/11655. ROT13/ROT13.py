code = input()
new = ''

for i in code :
    if i >= 'A' and i <= 'Z' :
        new += chr(((ord(i)-ord('A') + 13) % 26) + ord('A'))
    elif i >= 'a' and i <= 'z' :
        new += chr(((ord(i)-ord('a') + 13) % 26) + ord('a'))
    else :
        new += i

print(new)