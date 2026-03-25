from dataclasses import dataclass
from typing import List
import math

EPS = 1E-8

@dataclass
class point:
    x: float
    y: float

    def __add__(self, t):
        return point(self.x + t.x, self.y + t.y)
    
    def __sub__(self, t):
        return point(self.x - t.x, self.y - t.y)
    
    def angle(self, a, c):
        s1 = a - self
        d1 = math.sqrt(s1.x*s1.x + s1.y*s1.y)

        s2 = c - self
        d2 = math.sqrt(s2.x*s2.x + s2.y*s2.y)

        return math.acos((s1.x*s2.x + s1.y*s2.y)/(d1*d2))

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
    
    @property
    def segments(self):
        for i in range(len(self.vertices)):
            v1 = self.vertices[i]
            v2 = self.vertices[(i + 1) % len(self.vertices)]
            yield segment(v1, v2)
    
    @property
    def area(self):
        result = 0.0
        for i in range(len(self.vertices)):
            p1 = self.vertices[i]
            p2 = self.vertices[(i + 1) % len(self.vertices)]
            result += p2.y * p1.x - p2.x * p1.y
        return abs(result * 0.5)
    
    def is_inside(self, q):
        p = min(self.vertices, key=lambda v: v.x) - point(1, 0)
        crosses = sum(1 if segment(p, q).does_intersect(s, include_p=True) else 0 for s in self.segments)
        return crosses % 2 == 1

def read_input():
    kingdoms = []
    missiles = []
    
    while True:
        try:
            num_points = int(input())
            if num_points == -1:
                break
            
            power_station = None
            houses = []
            
            for i in range(num_points):
                x, y = map(int, input().split())
                if i == 0:
                    power_station = (x, y)
                else:
                    houses.append((x, y))
            
            kingdoms.append({'power_station': power_station, 'houses': houses})
        except:
            break
    
    try:
        while True:
            x, y = map(int, input().split())
            missiles.append((x, y))
    except:
        pass
    
    return kingdoms, missiles


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

def main():
    kingdoms, missiles = read_input()
    
    kingdom_hulls = []
    for kingdom in kingdoms:
        points = []
        ps = kingdom['power_station']
        points.append(point(ps[0], ps[1]))
        for house in kingdom['houses']:
            points.append(point(house[0], house[1]))
        
        ch = hull(points)
        kingdom_hulls.append(ch)
    
    affected_areas = set()
    total_area = 0.0
    
    for missile in missiles:
        missile_point = point(missile[0], missile[1])
        for idx, ch in enumerate(kingdom_hulls):
            if ch.is_inside(missile_point):
                if idx not in affected_areas:
                    affected_areas.add(idx)
                    total_area += ch.area
    
    print(f"{total_area:.2f}")

main()