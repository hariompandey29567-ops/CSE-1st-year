a = int(input("enter length of string\n"))
b = input("enter the string\n")
c = int(input("enter the values to check\n"))
ans = a
for i in range(a-c+1):
    count = (b[i:i+c].count("W"))
    ans=min(ans,count)
print(ans)
