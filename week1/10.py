s=input("输入的字符串:")

flag=0
for i in range(1,len(s)):
    if s[i]==s[i-1]:
        flag=1
        break
if(flag): print("YES")
else: print("NO")