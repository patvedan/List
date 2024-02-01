def second_largest(numbers):
    if len(numbers) < 2:
        return "List should have at least two elemnets"
    
    sorted_number = sorted(numbers, reverse=True)
 
    return sorted_number[1]

my_list = [1,21,9,7,15]
result = second_largest(my_list)
print("Second Largest Number:", result)