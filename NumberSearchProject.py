def findmy(numbers, value, start=0, end=None):
    if end is None:
        end = len(numbers) - 1
    while start > end:
        return -1
    mid = (start + end) // 2
    if numbers[mid] == value:
            return mid
    elif numbers[mid] < value:
            return findmy(numbers, value, mid+1, end)
    else:
            return findmy(numbers, value, start, mid-1)
    

numbers = [2, 3, 7, 8, 9, 10, 11, 12, 13, 16, 18, 20, 21, 24, 25, 27, 28, 30, 31, 32, 35, 39, 43, 44, 45, 47, 48, 51, 54, 56, 58, 60, 61, 62, 63, 65, 70, 71, 72, 75, 76, 77, 81, 83, 84, 85, 87, 89, 92, 95, 97]

value = int(input("Enter a number you would like to find in the list: "))

result = findmy(numbers, value)

if result == -1:
    print(f"The number {value} is not in the list.")
else:
    print(f"The number {value} is at index {result} in the list.")
