from dataclasses import dataclass
from typing import List
import math

EPS = 1E-8


def read_input():
    roads = []
    num_roads = int(input())
    
    for i in range(num_roads):
        K, T = map(int, input().split())
        points = []
        for j in range(K):
            x, y = map(float, input().split())
            points.append((x, y))
        roads.append((points, T))
    
    return roads

def compute_distance(p1, p2):
    d = math.sqrt((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2)
    return d

def find_point(p1, p2, distance, total_distance):
    ratio = distance / total_distance

    x = p1[0] + ratio * (p2[0] - p1[0])
    y = p1[1] + ratio * (p2[1] - p1[1])

    return (x, y)

def main():
    roads = read_input()
    count = 0
    for road in roads:
        count += 1
        points = road[0]
        num_trees = road[1]
        distances = []
        for p in range(len(points)-1):
            distances.append(compute_distance(points[p], points[p+1]))
        total_distance = sum(distances)
        tree_distance = total_distance / (num_trees - 1)

        trees = []
        tree_count = 0

        cumulative = [0]
        for distance in distances:
            cumulative.append(cumulative[-1] + distance)

        for segment in range(len(distances)):
            start = cumulative[segment]
            end = cumulative[segment + 1]

            while tree_count < num_trees:
                tree = tree_count * tree_distance
                if tree <= end + EPS:
                    if tree >= start - EPS:
                        offset = tree - start
                        tree_point = find_point(points[segment], points[segment+1], offset, distances[segment])
                        trees.append(tree_point)
                        tree_count += 1
                    else: 
                        break
                else:
                    break

        print(f"Road #{count}:")
        for tree in trees:
            print(f"{tree[0]:.2f} {tree[1]:.2f}")
        print("\n")

main()