def solution(data, n):
    count_dict = {}  # Dictionary to store the count of each element
    result = []      # List to store the final result
    
    # Count the occurrences of each element in the data list
    for element in data:
        if element in count_dict:
            count_dict[element] += 1
        else:
            count_dict[element] = 1

    # Iterate through the original list and append elements that occur less than or equal to n times
    for element in data:
        if count_dict[element] <= n:
            result.append(element)
    
    print (result)

# Test cases
(solution([1, 2, 3], 0))  # Output: [1, 2, 3]
(solution([1, 2, 2, 3, 3, 3, 4, 5, 5], 1))  # Output: [1, 4]