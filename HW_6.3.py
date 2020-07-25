def solution(number):
    dividable_numbers = [num for num in range(number) if num % 3 == 0 or num % 5 == 0]
    
    return sum(dividable_numbers)
