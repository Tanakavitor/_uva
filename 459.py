class UnionFindDisjointSets:
    def __init__(self, n):
        self.rank = [1] * n
        self.parent = [i for i in range(n)]

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        xset = self.find(x)
        yset = self.find(y)

        if xset == yset:
            return

        if self.rank[xset] < self.rank[yset]:
            self.parent[xset] = yset
        elif self.rank[xset] > self.rank[yset]:
            self.parent[yset] = xset
        else:
            self.parent[yset] = xset
            self.rank[xset] += 1

def main():
    n = int(input().strip())
    input()
    for _ in range(n):
        input()
        largest = input().strip()

        uf = UnionFindDisjointSets(ord(largest) - ord('a') + 1)
        
        a,b = input().strip().split()
        while a != "":
            uf.union(ord(a) - ord('a')+1, ord(b) - ord('a')+1)
            a,b = input().strip().split()
        set1 = set()
        for i in range(ord(largest) - ord('a') + 1):
            set1.add(uf.find(i))
        print(len(set1))

if __name__ == "__main__":
    main()