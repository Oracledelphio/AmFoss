t = int(input())
for _ in range(t):
    s= input().strip()
    reference = "amfoss"
    count=0
    for i in range(len(reference)):
        if i>+len(s) or s[i]!=reference[i]:
            count+=1
    count+=abs(len(s)-len(reference))
    print(count)