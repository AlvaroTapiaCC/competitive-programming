def read_input():
    cases = []
    n = int(input().strip())

    for _ in range(n):
        case = {"graph": {}, "letters_before": {}}

        blank = input()
        letters = input().strip().split()

        for letter in letters:
            case["graph"][letter] = set()
            case["letters_before"][letter] = 0

        constraints = input().strip().split()

        for constraint in constraints:
            a, b = constraint[0], constraint[2]
            case["graph"][a].add(b)
            case["letters_before"][b] += 1

        cases.append(case)

    return cases

def map_constraints(case: dict):    
    for constraint in case["constraints"]:
        if constraint[1] == "<":
            case["graph"][constraint[0]]["next"] = constraint[2]
            case["graph"][constraint[2]]["prev"] = constraint[0]
        else:
            case["graph"][constraint[2]]["next"] = constraint[0]
            case["graph"][constraint[0]]["prev"] = constraint[2]
            
def get_initial_ordering(case: dict):
    ordering = []
    for letter in case["graph"].keys():
        if case["graph"][letter]["next"] is not None and case["graph"][letter]["prev"] is None:
            break
    while case["graph"][letter]["next"] is not None:
        ordering.append(letter)
        letter = case["graph"][letter]["next"]
    return ordering

def compute_orderings(case: dict, initial_ordering: list):
    unordered_letters = set()
    for letter in case["graph"].keys():
        if case["graph"][letter] not in initial_ordering:
            unordered_letters.add(letter)
    
    


def main():
    for case in read_input():
        compute_orderings(case)
        
        
if __name__ == "__main__":
    main()