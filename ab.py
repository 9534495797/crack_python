
def count_inversions(arr):
    if len(arr) <= 1:
        return arr, 0

    mid = len(arr) // 2
    left, inv_left = count_inversions(arr[:mid])
    right, inv_right = count_inversions(arr[mid:])
    merged, split_inv = merge_and_count_split_inversions(left, right)

    return merged, inv_left + inv_right + split_inv

def merge_and_count_split_inversions(left, right):
    merged = []
    i = j = split_inv = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            split_inv += len(left) - i
            j += 1

    merged += left[i:]
    merged += right[j:]

    return merged, split_inv

# Read the file and convert it to a list of integers
with open('IntegerArray.txt', 'r') as file:
    integer_array = [int(line.strip()) for line in file]

# Call the function to count inversions
sorted_array, inversions = count_inversions(integer_array)

# Print the number of inversions
print(inversions)
