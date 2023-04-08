a = [1,4,3]
b = [1,4,3]

print("기본 리스트 : ", a)


# 리스트에 원소 삽입
a.append(2)
print("삽입 : ", a)

# 오름차순 정렬
a.sort()
print("오름차순 정렬 : ", a)

# 내림차순 정렬
a.sort(reverse=True)
print("내림차순 정렬 : ", a)

print("=======================")

# 리스트 원소 뒤집기
b.reverse()
print("원소 뒤집기 : ", b)

# 특정 인덱스에 데이터 추가
b.insert(2, 3)
print("인덱스 2에 3 추가: ", b)

# 특정 값인 데이터 개수 세기
print("값이 3인 데이터 개수 : ", b.count(3))

# 특정 값 데이터 삭제
b.remove(1)
print("값이 1인 데이터 삭제: ", b)

print("=======================")

c = [1,2,3,4,5,5,5]
remove_set = {3,5}  # 집합 자료형

# remove_set에 포함되지 않은 값만을 저장
result = [i for i in c if i not in remove_set]
print(result)