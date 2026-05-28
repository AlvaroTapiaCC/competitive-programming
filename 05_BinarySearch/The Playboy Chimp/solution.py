from bisect import bisect_left, bisect_right

def read_input():
    case = {}
    n = input()
    case['ladies'] = list(map(int, input().strip().split()))
    q = input()
    case['luchu'] = list(map(int, input().strip().split()))
    return case

def find_ladies(breakpoints: list, height: int):
    ladies = [None]
    for lady in breakpoints:
        ladies.append(lady)
    ladies.append(None)

    s = bisect_left(breakpoints, height)
    if ladies[s]:
        smaller = ladies[s]
    else:
        smaller = "X"
    
    t = bisect_right(breakpoints, height)
    if ladies[t+1]:
        taller = ladies[t+1]
    else:
        taller = "X"
    print(f"{smaller} {taller}")

def main():
    case = read_input()
    breakpoints = case['ladies']
    heights = case['luchu']
    for height in heights:
        find_ladies(breakpoints, height)

if __name__ == "__main__":
    main()
