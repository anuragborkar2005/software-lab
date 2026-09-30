def average_of_list(numbers):
    total = 0
    for i in range(len(numbers)): # fixed: removed the "+ 1"
        total += numbers[i]
    return total / len(numbers)
marks = [72, 85, 90, 66, 78]
print("Average marks:", average_of_list(marks))