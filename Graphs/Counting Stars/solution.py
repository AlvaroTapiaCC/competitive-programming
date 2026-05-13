from sys import stdin

def read_input():
    cases = []
    while True:
        header = list(map(int, input().strip().split()))
        if sum(header) == 0:
            break
        case = []
        for _ in range(header[0]):
            line = input().strip()
            case.append([line[c] for c in range(len(line))])
        cases.append(case)
    return cases


def check_adjacent(short_case: list, col: int):
    for i in range(3):
        for j in range(-1, 2):
            if (i == 1 and j == 0) or (col + j + 1) > len(short_case[0]) or (col + j) < 0:
                continue           
            
            elif short_case[i][col + j] == "*":
                return False
    return True

def count_stars(case: list): 
    stars = 0
    
    for row in range(len(case)):
        for col in range(len(case[0])):
            empty = ["." for _ in range(len(case[0]))]
            if case[row][col] == "*":
                if row == 0:
                    short_case = [empty] + case[row : row+2]
                    is_star = check_adjacent(short_case, col)
                    if is_star:
                        stars += 1
                
                elif row == len(case) - 1:
                    short_case = case[row-1 : row+1] + [empty]
                    is_star = check_adjacent(short_case, col)
                    if is_star:
                        stars += 1
                        
                else:
                    is_star = check_adjacent(case[row-1 : row+2], col)
                    if is_star:
                        stars += 1
            else:
                continue
    return stars

def main():
    for case in read_input():
        print(count_stars(case))


if __name__ == "__main__":
    main()