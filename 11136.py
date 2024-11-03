def main():
    days = int(input().strip())  
    lista = []
    for _ in range(days):
        n,list = (map,input().strip())  
        while n!=0:
            lista.append(list)
        if _ == (days-1):
            print(max(lista)-min(lista))
            lista.remove(max(lista))
            lista.remove(min(lista))



if __name__ == "__main__":
    main()