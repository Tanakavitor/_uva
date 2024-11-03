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
    while i < len(data):
        n = int(data[i].strip())
        for _ in range(n):
            i+=1
            x,y,r = map(int,data[i].split())
            
        
       