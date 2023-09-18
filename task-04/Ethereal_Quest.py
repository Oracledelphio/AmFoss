n=int(input())
coordinates=[]
for _ in range(n):
    coordinates.append(list(map(int,input().split())))

sum_x = sum([coordinate[0] for coordinate in coordinates])
sum_y = sum([coordinate[1] for coordinate in coordinates])
sum_z = sum([coordinate[2] for coordinate in coordinates])

if sum_x ==0 and sum_y ==0 and sum_z==0:
    print("YES")
else:
    print("NO")