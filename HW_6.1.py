def count_positives_sum_negatives(arr):
    positive_numbers = [num for num in arr if num > 0]
    negative_numbers = [num for num in arr if num < 0]
    result = [len(positive_numbers), sum(negative_numbers)]
    
    if arr == []:
        return arr
    
    
    
    return result