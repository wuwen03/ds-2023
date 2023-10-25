def Statistic(file):
    f=open(file,encoding='UTF-8')
    dictionary={}
    for line in f.readlines():
        if len(line)>10:
            mark=[',','.',':','\\','s',';','?','(',')']
        for m in mark:
            line=line.replace(m,'')
        lineattr=line.strip().split(" ")
        for char in lineattr:
            if char not in dictionary:
                dictionary[char]=1
            else :
                dictionary[char]+=1

    a=sorted(dictionary.items(),key=lambda x:x[1],reverse=True)
    return a

def printwords(file,n):
    a=Statistic(file)
    for i in range(n):
        print(a[i])

printwords("十四行诗.txt",20)