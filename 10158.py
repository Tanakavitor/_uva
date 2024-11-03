class DisjSet:
    def __init__(self, n):
        self.rank = [1] * n
        self.parent = [i for i in range(n)]

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX == rootY:
            return False
        if self.rank[rootX] < self.rank[rootY]:
            self.parent[rootX] = rootY
        elif self.rank[rootX] > self.rank[rootY]:
            self.parent[rootY] = rootX
        else:
            self.parent[rootY] = rootX
            self.rank[rootX] += 1
        return True

    def areConnected(self, x, y):
        return self.find(x) == self.find(y)

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split('\n')
    i = 0
    n = int(data[i].strip())
    friends = DisjSet(n * 2)
    enemies = DisjSet(n * 2)
    output = []

    while True:
        i += 1
        if i >= len(data):
            break
        c, x, y = map(int, data[i].strip().split())
        if c == 0 and x == 0 and y == 0:
            break

        fx = friends.find(x)
        fy = friends.find(y)
        ex = friends.find(x + n)
        ey = friends.find(y + n)

        if c == 1: 
            if fx == ey or fy == ex:
                output.append("-1")
            else:
                friends.union(fx, fy)
                friends.union(ex, ey)
        elif c == 2:  
            if fx == fy:
                output.append("-1")
            else:
                friends.union(fx, ey)
                friends.union(fy, ex)
        elif c == 3: 
            output.append("1" if friends.areConnected(fx, fy) else "0")
        elif c == 4:  
            output.append("1" if friends.areConnected(fx, ey) else "0")

    for line in output:
        print(line)

if __name__ == "__main__":
    main()