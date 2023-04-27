def solution(numbers):
    n = [0,1,2,3,4,5,6,7,8,9]
    return sum(i for i in n if not i in numbers)


def solution(numbers):
    return 45 - sum(numbers)

solution = lambda x: sum(range(10)) - sum(x)