def solution(n):

    for i in range(1, n+1):
        if n%i == 1:
            return i

# list comprehension 사용
# def solution(n):
#     return [i for i in range(1, n + 1) if n % i == 1][0]

# 람다로

solution = lambda n: min(list(filter(lambda x:n%x==1,range(1,n+1))))