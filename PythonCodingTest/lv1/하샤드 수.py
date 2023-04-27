# def solution(x):
#     answer = list(str(x))
#     xSum = sum(map(lambda x:int(x), answer))
#     return True if not x % xSum else False

def solution(n):
    return n%sum(int(x) for x in str(n)) == 0

a = ['a', 'b']

