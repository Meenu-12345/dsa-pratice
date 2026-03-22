# two sum
def two_sum(numbers, target):
    num_dict = {}
    for i, num in enumerate(numbers):
        complement = target - num
        if complement in num_dict:
            return (num_dict[complement], i)
        num_dict[num] = i
    return None

# Example usage:
numbers = [2, 7, 11, 15]
target = 9
result = two_sum(numbers, target)
if result:
    print(f"Indices: {result[0]}, {result[1]}")
else:    print("No two numbers add up to the target.")