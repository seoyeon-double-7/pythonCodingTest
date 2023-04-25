# 첫풀이
def solution(A, B):

    for i in range(0, len(A)):
#       끝에서 i개가져오기 + 처음부터 -i까지
        s = A[-i::] + A[0:-i:]
        if(s == B):
            return i

    return -1


# find 함수 활용하기 
#  => 찾는 문자가 존재 한다면 해당 위치의 index를 반환해주고
#  => 찾는 문자가 존재 하지 않는다면 -1 을 반환
# 옆으로 민 문자열 b에 b를 또 붙이면 가운데에 a 숫자가 나옴 => 인덱스 번호가 a를 밀은 개수 => ohellohll \> lohellohel
solution=lambda a,b:(b*2).find(a)

# deque rotate 함수 사용하기
# deque를 적용해줄 변수를 매개변수 안에 넣는다!
from collections import deque
def solution(A, B):
    a = deque(A)
    b = deque(B)

    for i in range(0, len(a)):
        if a == b:
            return i
        a.rotate(1)
    return -1
