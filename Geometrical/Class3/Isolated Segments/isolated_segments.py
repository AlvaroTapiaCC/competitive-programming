from dataclasses import dataclass
import math

EPS = 1E-8

@dataclass
class point:
    x: float
    y: float

    def __sub__(self, t):
        return point(self.x - t.x, self.y - t.y)

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

def read_input():
    tests = []
    num_tests = int(input())
    
    for _ in range(num_tests):
        num_segments = int(input())
        segments = []
        
        for _ in range(num_segments):
            xi, yi, xj, yj = map(int, input().split())
            p = point(xi, yi)
            q = point(xj, yj)
            segments.append(segment(p, q))
        
        tests.append(segments)
    
    return tests

def segments_collide(seg1, seg2):
    # Check if segments overlap or touch
    
    seg1_min_x = min(seg1.p.x, seg1.q.x)
    seg1_max_x = max(seg1.p.x, seg1.q.x)
    seg1_min_y = min(seg1.p.y, seg1.q.y)
    seg1_max_y = max(seg1.p.y, seg1.q.y)
    
    seg2_min_x = min(seg2.p.x, seg2.q.x)
    seg2_max_x = max(seg2.p.x, seg2.q.x)
    seg2_min_y = min(seg2.p.y, seg2.q.y)
    seg2_max_y = max(seg2.p.y, seg2.q.y)
    
    boxes_overlap = not (seg1_max_x < seg2_min_x - EPS or seg1_min_x > seg2_max_x + EPS or
                         seg1_max_y < seg2_min_y - EPS or seg1_min_y > seg2_max_y + EPS)
    
    vec1 = (seg1.q.x - seg1.p.x, seg1.q.y - seg1.p.y)
    vec2 = (seg2.q.x - seg2.p.x, seg2.q.y - seg2.p.y)
    cross = vec1[0] * vec2[1] - vec1[1] * vec2[0]
    
    collinear = abs(cross) < EPS
    
    if collinear:
        return boxes_overlap
    
    return seg1.does_intersect(seg2, include_p=True, include_q=True)

def count_isolated_segments(segments):
    isolated_count = 0
    
    for i, seg1 in enumerate(segments):
        is_isolated = True
        
        for j, seg2 in enumerate(segments):
            if i == j:
                continue
            
            if segments_collide(seg1, seg2):
                is_isolated = False
                break
        
        if is_isolated:
            isolated_count += 1
    
    return isolated_count

def main():
    tests = read_input()
    
    for segments in tests:
        isolated = count_isolated_segments(segments)
        print(isolated)

main()
