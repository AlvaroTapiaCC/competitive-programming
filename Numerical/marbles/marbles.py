def find_min_cost(N, c1, n1, c2, n2):
    best_combination = None
    min_cost = None
    
    max_boxes_type1 = N // n1 + 1
    
    for x1 in range(max_boxes_type1 + 1):
        marbles_covered = x1 * n1
        remaining = N - marbles_covered
        
        if remaining >= 0 and remaining % n2 == 0:
            x2 = remaining // n2
            cost = x1 * c1 + x2 * c2
            
            if min_cost is None or cost < min_cost:
                min_cost = cost
                best_combination = (x1, x2)
    
    return best_combination


results = []

while True:
    N = input().strip()
    if N == '0':
        break
    N = int(N)
    c1, n1 = map(int, input().strip().split())
    c2, n2 = map(int, input().strip().split())
    
    result = find_min_cost(N, c1, n1, c2, n2)
    
    if result is None:
        results.append("failed")
    else:
        x1, x2 = result
        results.append(f"{x1} {x2}")

for result in results:
    print(result)