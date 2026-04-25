def read_input():
    cases = []
    m = int(input().strip())
    blank = input()
    for i in range(m):
        people = {}
        n = int(input().strip())
        for j in range(n):
            people[j+1] = {"enemies": [], "friends": []}
            line = list(map(int, input().strip().split()))
            if line[0] != 0:
                people[j+1]["enemies"] = line[1:]
        cases.append(people)
        if i < m - 1:
            blank = input()
    return cases

def fill_friends(people: dict[int: dict["enemies": list], "friends": list]):
    for person in people.keys():
        for enemy in people[person]["enemies"]:
            for friend in people[enemy]["enemies"]:
                if friend not in people[person]["enemies"] and person not in people[friend]["enemies"] and friend != person and friend not in people[person]["friends"]:
                    people[person]["friends"].append(friend)
                    people[friend]["friends"].append(person)
    return people

def fill_enemies(people: dict[int: dict["enemies": list], "friends": list]):
    for person in people.keys():
        for enemy in people[person]["enemies"]:
            people[enemy]["enemies"].append(person)
    return people

def check_solution(guests: list):
    for guest in guests:
        pass
    return

def compute_max_guests(people: dict[int: dict["enemies": list], "friends": list]):
    max_guests = 0
    for i in range(1, len(people.keys()) + 1):
        banned = set()
        guests = []
        first_guest = people[i]
        guests.append(i)
        for enemy in first_guest["enemies"]:
            banned.add(enemy)
        for person in people.keys():
            if person != i and person not in banned:
                guests.append(person)
                for enemy in people[person]["enemies"]:
                    banned.add(enemy)
        if len(guests) > max_guests and check_solution(guests):
            max_guests = len(guests)
    print(max_guests)

def main():
    cases = read_input()
    for case in cases:
        people = fill_friends(case)
        people = fill_enemies(people)
        compute_max_guests(people)


if __name__ == "__main__":
    main()


'''
NOTES

casi listo, falta verificar si es posible:
    b es enemigo de a, pero a es amigo de b (relaciones)

'''