def merge_sort(arr):
    if len(arr) <= 1:
        return arr, 0

    mid = len(arr) // 2
    left, inv_left = merge_sort(arr[:mid])
    right, inv_right = merge_sort(arr[mid:])
    merged, inv_merge = merge(left, right)

    return merged, inv_left + inv_right + inv_merge

def merge(left, right):
    inv_count = 0
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1
            inv_count += len(left) - left_index

    merged.extend(left[left_index:])
    merged.extend(right[right_index:])

    return merged , inv_count





def main():
    while True:
        n = int(input())
        if n == 0:
            break

        arr = []
        for _ in range(n):
            arr.append(int(input()))

        _, inversions = merge_sort(arr)
        print(inversions)




if __name__ == "__main__":
    main()
