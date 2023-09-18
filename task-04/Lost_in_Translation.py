s = input().strip()
hello="hello"
hello_idx=0
for char in s:
    if char== hello[hello_idx]:
        hello_idx+=1
        if hello_idx == len(hello):
            print("YES")
            break
if hello_idx< len(hello):
    print("NO")