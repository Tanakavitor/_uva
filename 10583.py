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

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    case_number = 1
    
    while True:
        n = int(data[index])
        m = int(data[index + 1])
        index += 2
        
        if n == 0 and m == 0:
            break
        
        new = DisjSet(n)
        
        for _ in range(m):
            a = int(data[index])
            b = int(data[index + 1])
            index += 2
            new.union(a - 1, b - 1)
        
        unique_religions = len(set(new.find(k) for k in range(n)))
        print(f"Case {case_number}: {unique_religions}")
        case_number += 1

if __name__ == '__main__':
    main()