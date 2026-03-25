import sys

def read_input():
    cases = []

    for line in sys.stdin:
        line = line.strip()

        if not line:
            break
        
        cases.append(list(map(int, line.split())))
    return cases


def sort_bins(case):
    bins = [case[0:3], case[3:6], case[6:9]]
    options = ['BGC', 'BCG', 'GBC', 'GCB', 'CGB', 'CBG']
    colors = ['B', 'G' ,'C']

    best_order = ''
    min_movements = 9999999


    for option in options:
        movements = 0
        for bin_idx, bin in enumerate(bins):
            for col_idx, color in enumerate(colors):
                if color != option[bin_idx]:
                    movements += bin[col_idx]
        if (movements < min_movements) or (movements == min_movements and option < best_order):
            min_movements = movements
            best_order = option

    print(f"{best_order} {min_movements}")


for i in read_input():
    sort_bins(i)
