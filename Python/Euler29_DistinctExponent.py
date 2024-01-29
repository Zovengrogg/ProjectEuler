# Distinct Exponent https://projecteuler.net/problem=29

def exp(a, b):
    return a**b

index = []
distinct = []
for a in range(2,101):
    for b in range(2,101):
        value = exp(a,b)
        if(not value in distinct):
            distinct.append(value)

print(len(distinct))