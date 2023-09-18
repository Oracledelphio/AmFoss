def max_sint_sum(t, test_cases):
    results =[]
    
    for test_case in test_cases:
        n, phone_models= test_case
        counts={}
        for model in phone_models:
            counts[model] = counts.get(model,0) +1
        snint_A=0
        snint_B=0
        
        for i in range(101):
            if i not in counts:
                snint_A= i
                break
        for i in range(101):
            if i not in counts or counts[i] < 2:
                snint_B= i
                break
        results.append(snint_A +snint_B)
        
    return results
t=int(input())
test_cases= []
for _ in range(t):
    n=int(input())
    phone_models = list(map(int,input().split()))
    test_cases.append((n,phone_models))
    
results=max_sint_sum(t, test_cases)
for result in results:
    print(result)