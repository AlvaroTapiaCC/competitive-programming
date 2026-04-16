#STEPS
# 1) get the input numbers
# 2) define the function
# 3) first try the direct case ( >= 101)
# 4) if not, use the recursive funcion for <= 100

data = []

while True:
    line = input().strip()

    if line == '0':
        break
    
    data.append(int(line))

def f91(N):
    if N >= 101:
        return N - 10

    else:
        return f91(f91(N + 11))
    
for i in data:
    print(f"f91({i}) = {f91(i)}")