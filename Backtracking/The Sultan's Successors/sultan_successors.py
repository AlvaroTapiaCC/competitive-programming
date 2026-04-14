

def read_input():
    k = int(input().strip())
    for i in range(k):
        set = []
        for j in range(8):
            line = list(map(int, input().strip().split()))
            set.append(line)
        yield set

def locate_queens(indexes):

    pass


for i, set in enumerate(read_input()):
    #locate_queens(i)
    #print(f"{i}, set: {set}\n")
    for line in set:
        print(line)