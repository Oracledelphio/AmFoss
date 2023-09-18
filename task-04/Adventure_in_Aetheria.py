def find_town(n,times):
    min_time =min(times)
    min_town = times.index(min_time)+1
    if times.count(min_time)>1:
        return "Still Aetheria"
    else:
        return min_town
n=int(input())
times= list(map(int,input().split()))
result= find_town(n,times)
print(result)