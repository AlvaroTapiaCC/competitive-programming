import math
from itertools import islice, cycle
from dataclasses import dataclass
from typing import List

EPS = 1E-8


def read_input():
    cases = []
    while True:
        cops = []
        robbers = []
        citizens = []
        first_line = list(map(int, input().split()))
        if first_line == [0,0,0]:
            break

        for i in range(first_line[0]):
            cops.append(list(map(int, input().split())))
        for j in range(first_line[1]):
            robbers.append(list(map(int, input().split())))
        for k in range(first_line[2]):
            citizens.append(list(map(int, input().split())))
        blank = input()
        case = [first_line, cops, robbers, citizens]
        cases.append(case)

    return cases


@dataclass
class point:
    x: float
    y: float

    def __add__(self, t):
        return point(self.x + t.x, self.y + t.y)
    def __sub__(self, t):
        return point(self.x - t.x, self.y - t.y)
    def dot(self, a):
        return self.x*a.x + self.y*a.y

    def norm(self):
        return math.sqrt(self.dot(self))

    def rotate(self, theta):
        return point(
            self.x * math.cos(theta) - self.y * math.sin(theta),
            self.x * math.sin(theta) + self.y * math.cos(theta),
        )

    def angle(self, a, c):
        s1 = a - self
        d1 = s1.norm()

        s2 = c - self
        d2 = s2.norm()

        return math.acos(s1.dot(s2)/(d1*d2))

    def cross(self, p):
        return self.x*p.y - p.x*self.y


@dataclass
class segment:
    p: point
    q: point

    def does_intersect(self, seg2, *, include_p=False, include_q=False):
        cross1 = (seg2.q - self.p).cross(self.q - self.p)
        cross2 = (seg2.p - self.p).cross(self.q - self.p)
        cross3 = (self.q - seg2.p).cross(seg2.q - seg2.p)
        cross4 = (self.p - seg2.p).cross(seg2.q - seg2.p)
        return (
            (cross1 * cross2 < 0 or
                (include_p and math.fabs(cross2) < EPS)
                or (include_q and math.fabs(cross1) < EPS))
            and (cross3 * cross4 < 0
                or (include_p and math.fabs(cross4) < EPS)
                or (include_q and math.fabs(cross3) < EPS))
        )


@dataclass
class polygon:
    vertices: List[point]

    def shifted_vertices(self, shift=1):
        # v2, v3, ...., vN, v1
        yield from islice(cycle(self.vertices), shift, len(self.vertices) + shift)

    @property
    def segments(self):
        for v1, v2 in zip(self.vertices, self.shifted_vertices()):
            yield segment(v1, v2)


    @property
    def perimeter(self):
        return sum((v1 - v2).norm() for v1, v2 in zip(self.vertices, self.shifted_vertices()))
    
    def is_inside(self, q):
        p = min(self.vertices, key=lambda v: v.x) - point(1, 0)
        crosses = sum(1 if segment(p, q).does_intersect(s, include_p=True) else 0 for s in self.segments)
        return crosses % 2 == 1



def hull(points):
    if len(points) < 3:
        return polygon(points)
    q = min(points, key=lambda v: v.x)
    p = point(q.x, q.y - 1)
    ch = [p, q]
    while True:
        p, q = ch[-2], ch[-1]
        u = max((v for v in points if v != p and v != q),
        key=lambda x: q.angle(p, x))
        if u in ch:
            break
        ch.append(u)
    return polygon(ch[1:])


def check_safety(index, case):
    population = case[0]
    cops = []
    robbers = []
    citizens = []

    for i in range(population[0]):
        cop = point(x=case[1][i][0], y=case[1][i][1])
        cops.append(cop)
    for i in range(population[1]):
        robber = point(x=case[2][i][0], y=case[2][i][1])
        robbers.append(robber)
    for i in range(population[2]):
        citizen = point(x=case[3][i][0], y=case[3][i][1])
        citizens.append(citizen)

    return_message = [f"Data set {index+1}:"]
    if len(cops) < 3 and len(robbers) < 3:
        for citizen in citizens:
            return_message.append(f"    Citizen at ({citizen.x},{citizen.y}) is neither.")
        return_message.append("\n")
        return return_message

        
    
    elif len(cops) >= 3 and len(robbers) < 3:
        cop_area = hull(cops)
        for citizen in citizens:
            if cop_area.is_inside(citizen):
                return_message.append(f"    Citizen at ({citizen.x},{citizen.y}) is safe.")
            else:
                return_message.append(f"    Citizen at ({citizen.x},{citizen.y}) is neither.")
        return_message.append("\n")
        return return_message

    
    elif len(cops) < 3 and len(robbers) >= 3:
        robber_area = hull(robbers)
        for citizen in citizens:
            if robber_area.is_inside(citizen):
                return_message.append(f"    Citizen at ({citizen.x},{citizen.y}) is robbed.")
            else:
                return_message.append(f"    Citizen at ({citizen.x},{citizen.y}) is neither.")
        return_message.append("\n")
        return return_message
    
    else:
        cop_area = hull(cops)
        robber_area = hull(robbers)
        for citizen in citizens:
            if cop_area.is_inside(citizen):
                return_message.append(f"    Citizen at ({citizen.x},{citizen.y}) is safe.")
            elif robber_area.is_inside(citizen):
                return_message.append(f"    Citizen at ({citizen.x},{citizen.y}) is robbed.")
            else:
                return_message.append(f"    Citizen at ({citizen.x},{citizen.y}) is neither.")
        return_message.append("\n")
        return return_message      






for i, case in enumerate(read_input()):
    message = check_safety(i, case)
    for m in message:
        print(m)