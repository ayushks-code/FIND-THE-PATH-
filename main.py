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

a = [
    [0, 0, 0, 0, 0],
    [1, 9, 9, 9, 1],
    [0, 0, 0, 0, 0]
]

queries = [
    [0, 0, 2, 4],
    [0, 3, 2, 3],
    [1, 1, 1, 3]
]

answer = shortestPath(a, queries)

print(answer)
