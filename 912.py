class DisjSet: 
    def __init__(self, n): 
        self.rank = [1] * n 
        self.parent = [i for i in range(n)] 
  
  
    def find(self, x): 
          

        if (self.parent[x] != x): 
              
   
            self.parent[x] = self.find(self.parent[x]) 
 
  
        return self.parent[x] 

    def Union(self, x, y): 
          
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
            self.rank[xset] = self.rank[xset] + 1
            
def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split('\n')
    i = 0
    while i < len(data):
        n = int(data[i].strip())
        i += 1
        uf = DisjSet(n)
        lista1 = []
        lista2 = []
        for _ in range(n):
            a = input().strip()
            if a.isdigit():
                a = int(a)
            lista1.append(a)
        for _ in range(n):
            a = input().strip()
            if a.isdigit():
                a = int(a)
            lista2.append(a)
        for i2 in range(n):
            if not lista1[i2].isdigit() and lista2[i2].isdigit():
                if uf.find(ord(lista1[i2]) - ord('a')) != uf.find(lista2[i2]):
                    uf.Union(ord(lista1[i2]) - ord('a'), lista2[i2])
            if lista1[i2].isdigit() and not lista2[i2].isdigit():
                uf.Union(lista1[i2], ord(lista2[i2]) - ord('a'))
               
            
            

  