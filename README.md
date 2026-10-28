# Competitive Programming

Personal log of my progress through the Competitive Programming course at Universidad de los Andes (Chile), 2026. It contains my Python attempts at [UVa Online Judge](https://onlinejudge.org/) problems, organized by unit, each with the sample input/output cases I used while working on it.

This is a learning record, not a polished solution set: many problems are solved, while others are partial attempts or left in progress.

## Units

| Folder | Topic | Main techniques |
|--------|-------|-----------------|
| `01_Intro` | Ad hoc | Simulation, brute force |
| `02_Numerical` | Number theory | GCD/LCM, logarithms, recursion |
| `03_Geometrical` | Computational geometry | Cross product, segment intersection, convex hull, polygon area |
| `04_Backtracking` | Backtracking | Search with pruning, board placement, prime checks |
| `05_BinarySearch` | Binary search | Binary search on the answer, `bisect` |
| `06_Graphs` | Graphs I | DFS/BFS, connected components, bipartite check |
| `07_Graphs2` | Graphs II | Shortest paths, minimum spanning trees, flows |
| `08_DynamicProg` | Dynamic programming I | Coin change, counting, stacking (LIS-style) |
| `09_DynamicProg2` | Dynamic programming II | Memoization, sequence and grid DP |
| `10_Bonus` | Mixed | Dijkstra, geometry, DP |
| `Prueba1-3` | Timed exams | Problems solved under exam conditions |

## Structure

```
<unit>/
└── <Problem Name>/
    ├── solution.py        # reads from stdin, writes to stdout
    └── cases/
        ├── case1.0.in
        └── case1.0.out
```

Several units also have a `template.py` with the input-reading skeleton I used for that unit.

To try a solution (Python 3.10+, no dependencies):

```bash
cd "06_Graphs/Counting Stars"
python solution.py < cases/case1.0.in
```

## Useful links

- Problem set: https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=210
- uDebug (extra test cases): https://www.udebug.com/
- Competitive Programmer's Handbook: https://github.com/pllk/cphb/
