def merge_and_count(arr, start, mid, end):
    temp = []
    inversions = 0
    i = start
    j = mid
    while i < mid and j < end:
        if arr[i] <= arr[j]:
            temp.append(arr[i])
            i += 1
        else:
            temp.append(arr[j])
            j += 1
            inversions += mid - i
    temp += arr[i:mid]
    temp += arr[j:end]
    arr[start:end] = temp
    return inversions

def count_inversions(arr, start, end):
    if end - start <= 1:
        return 0
    mid = (start + end) // 2
    return (count_inversions(arr, start, mid) +
            count_inversions(arr, mid, end) +
            merge_and_count(arr, start, mid, end))

def inversion_count(string):
    arr = list(string)
    return count_inversions(arr, 0, len(arr))

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split("\n")
    
    index = 0
    test_cases = int(data[index])
    index += 1
    
    results = []
    
    for _ in range(test_cases):
        index += 1  
        len_strings, num_strings = map(int, data[index].strip().split())
        index += 1
        
        strings = []
        for _ in range(num_strings):
            string = data[index].strip()
            inversions = inversion_count(string)
            strings.append((string, inversions))
            index += 1
        
        sorted_strings = sorted(strings, key=lambda item: item[1])
        
        result = [string for string, _ in sorted_strings]
        results.append("\n".join(result))
    
    print("\n\n".join(results))

if __name__ == "__main__":
    main()
