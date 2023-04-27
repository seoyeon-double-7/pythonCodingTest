# def solution(arr, divisor):
#     answer = [n for n in arr if not n%divisor]

#     return sorted(answer) if len(answer) != 0 else [-1]

def solution(arr, divisor):
    return sorted([n for n in arr if not n % divisor]) or [-1]