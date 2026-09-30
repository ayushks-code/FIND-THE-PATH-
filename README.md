# Shortest Path in a Weighted Grid

## 📌 Project Description

This project finds the **minimum possible weight of a path between two cells in a weighted 2D grid**.

Each cell in the grid contains an integer value representing the cost of visiting that cell.

A path can move only between cells that share a side:

* ⬆️ Up
* ⬇️ Down
* ⬅️ Left
* ➡️ Right

The goal is to find the path with the **minimum total weight** between the given starting and ending cells.

---

## 🧠 Algorithm Used

The project uses **Dijkstra's Shortest Path Algorithm**.

Dijkstra's algorithm is suitable because all cell weights are **non-negative**.

For every query:

1. Start from the given source cell.
2. Store the current minimum distance to every cell.
3. Use a priority queue to process the cell with the smallest distance.
4. Check its four possible neighboring cells.
5. Update the distance if a cheaper path is found.
6. Continue until the destination cell is reached.

---

## 📊 Example Grid

```text
0 0 0 0 0
1 9 9 9 1
0 0 0 0 0
```

For example, consider the query:

```text
0 0 2 4
```

This means:

```text
Start      = (0, 0)
Destination = (2, 4)
```

One minimum-cost path is:

```text
(0,0)
  ↓
(1,0)
  ↓
(2,0) → (2,1) → (2,2) → (2,3) → (2,4)
```

Its total weight is:

```text
0 + 1 + 0 + 0 + 0 + 0 + 0 = 1
```

Therefore, the answer is:

```text
1
```

---

## 💻 Technologies Used

* Python 3
* Dijkstra's Algorithm
* Priority Queue
* 2D Arrays
* Graph/Shortest Path Concepts

---
## 💻 Source Code

```python
import heapq


def shortestPath(a, queries):

    n = len(a)
    m = len(a[0])

    INF = 10**18

    def dijkstra(sr, sc, tr, tc):

        dist = [[INF] * m for _ in range(n)]

        dist[sr][sc] = a[sr][sc]

        pq = [(a[sr][sc], sr, sc)]

        while pq:

            d, r, c = heapq.heappop(pq)

            if d != dist[r][c]:
                continue

            if r == tr and c == tc:
                return d

            # UP
            if r > 0:
                nr, nc = r - 1, c
                nd = d + a[nr][nc]

                if nd < dist[nr][nc]:
                    dist[nr][nc] = nd
                    heapq.heappush(pq, (nd, nr, nc))

            # DOWN
            if r < n - 1:
                nr, nc = r + 1, c
                nd = d + a[nr][nc]

                if nd < dist[nr][nc]:
                    dist[nr][nc] = nd
                    heapq.heappush(pq, (nd, nr, nc))

            # LEFT
            if c > 0:
                nr, nc = r, c - 1
                nd = d + a[nr][nc]

                if nd < dist[nr][nc]:
                    dist[nr][nc] = nd
                    heapq.heappush(pq, (nd, nr, nc))

            # RIGHT
            if c < m - 1:
                nr, nc = r, c + 1
                nd = d + a[nr][nc]

                if nd < dist[nr][nc]:
                    dist[nr][nc] = nd
                    heapq.heappush(pq, (nd, nr, nc))

        return dist[tr][tc]

    result = []

    for r1, c1, r2, c2 in queries:
        result.append(dijkstra(r1, c1, r2, c2))

    return result
```
## 📥 Input Format

The program takes:

```text
n m
```

where:

* `n` = number of rows
* `m` = number of columns

Then `n` rows containing the grid values.

Next:

```text
q
```

where `q` is the number of queries.

Each query contains:

```text
r1 c1 r2 c2
```

where:

* `(r1, c1)` = starting cell
* `(r2, c2)` = destination cell

---

## 📤 Output Format

For every query, the program prints one integer representing the **minimum possible path weight**.

Example:

```text
1
1
18
```

---

## 🧪 Sample Input

```text
3 5
0 0 0 0 0
1 9 9 9 1
0 0 0 0 0
3
0 0 2 4
0 3 2 3
1 1 1 3
```

## ✅ Sample Output

```text
1
1
18
```

---

## ⚙️ How It Works

The grid can be considered as a **weighted graph**.

Each cell is a vertex, and neighboring cells are connected by edges.

For example:

```text
      (0,1)
        |
(0,0) -- (0,2)
  |
(1,0)
```

Each cell has its own weight.

When moving to a neighboring cell, that cell's weight is added to the current path cost.

Dijkstra's algorithm continuously selects the currently cheapest path and explores it.

---

## 🚀 Running the Project

### 1. Clone the repository

```bash
git clone <your-repository-url>
```

### 2. Open the project

```bash
cd <repository-name>
```

### 3. Run the Python program

```bash
python shortest_path.py
```

---

## 📁 Project Structure

```text
Shortest-Path-Grid/
│
├── shortest_path.py
└── README.md
```

---

## 🎯 Learning Objectives

This project demonstrates:

* Graph representation using a grid
* Shortest path algorithms
* Dijkstra's algorithm
* Priority queues
* Path cost calculation
* Handling multiple queries
* Python implementation of graph algorithms

---

## 👨‍💻 Author

**Ayush**

This project was created as a learning implementation of the **Shortest Path Problem using Dijkstra's Algorithm**.
