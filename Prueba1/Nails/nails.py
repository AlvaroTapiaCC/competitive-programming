import math
from itertools import islice, cycle
from dataclasses import dataclass
from typing import List


def read_input():
    cases = []
    n = int(input())
    for i in range(n):
        case = []
        first_line = list(map(int, input().split()))
        case.append(first_line)
        for j in range(first_line[1]):
            line = list(map(int, input().split()))
            case.append(line)
        cases.append(case)
        if i == (n-1):
            break
        blank = input()
        
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
    
    def angle(self, a, c):
        s1 = a - self
        d1 = s1.norm()

        s2 = c - self
        d2 = s2.norm()

        return math.acos(s1.dot(s2)/(d1*d2))




@dataclass
class polygon:
    vertices: List[point]

    def shifted_vertices(self, shift=1):
        # v2, v3, ...., vN, v1
        yield from islice(cycle(self.vertices), shift, len(self.vertices) + shift)


    @property
    def perimeter(self):
        return sum((v1 - v2).norm() for v1, v2 in zip(self.vertices, self.shifted_vertices()))



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




def rubber_lenght(case):
    final_lenght = case[0][0]
    vert = []
    for i in range(case[0][1]):
        p = point(x=case[i+1][0], y=case[i+1][1])
        vert.append(p)

    nails_hull = hull(vert)
    lenght = nails_hull.perimeter

    if lenght > final_lenght:
        final_lenght = lenght

    return f"{final_lenght:.5f}"


for i in read_input():
    print(rubber_lenght(i))