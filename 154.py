colors = {'r': 0, 'o': 1, 'y': 2, 'g': 3, 'b': 4}

def main():
    import sys
    input_data = sys.stdin.read().strip().split('\n')
    
    results = [] 
    block = []  

    for line in input_data:
        line = line.strip()
        
        if line == 'e':
            min_changes = float('inf')
            best_city_index = 0

            for i in range(len(block)):
                total_changes = 0
                changes = 0
                for a, b in zip(block[i], block[j]):
                    if a != b:
                        changes += 1
                    total_changes += changes

                if total_changes < min_changes:
                    min_changes = total_changes
                    best_city_index = i + 1 

            results.append(str(best_city_index))
            block.clear()  

        elif line == '#':
            break

        else:
            bins = line.split(',')
            city_bins = [''] * 5 

            for bin in bins:
                color, waste = bin.split('/')
                city_bins[colors[color]] = waste 

            block.append("".join(city_bins)) 

    for result in results:
        print(result)

if __name__ == '__main__':
    main()
