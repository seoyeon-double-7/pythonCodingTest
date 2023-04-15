# sum() => 합
result = sum([1,2,3,4,5])
print(result)

# min(), max() => 최대 최소
min_result = min(7,3,5,2)
max_result = max(7,3,5,2)
print(min_result, max_result)

# eval() => 문자열을 식으로
result = eval("(3+5)*7")
print(result)

# sorted() => 정렬
result = sorted([9,1,8,5,4]) # 오름차순
reverse_result = sorted([9,1,8,5,4], reverse=True)  # 내림차순
print(result)
print(reverse_result)

# sorted() with key
# array = [('홍길동, 50'), ('이순신', 32), ('배서연', 74)]
# result = sorted(array, key=lambda x: x[1], reverse=True)
# print(result)