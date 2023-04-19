def solution(emergency):
    answer = []
    e = sorted(emergency, reverse=True)

    for i in emergency:
        answer.append(e.index(i)+1)
    return answer

# list comprehension 사용
def solution(emergency):
    e = sorted(emergency, reverse=True)
    return [(e.index(i)+1) for i in emergency]


# dictionary 사용
def solution(emergency):
    answer = []
    #     emergency 내림차순하기
    #     i=> 키값(인덱스)
    #     e => 수 정렬된 배열
    #     enumerate => key와 value 값 반환
    emer_ls = {e: i + 1 for i, e in enumerate(sorted(emergency, reverse=True))}

    # 원래 수가 들어있는 emergency 값 e를 순서가 담겨있는 딕셔너리 emer_ls의
    # 배열 값과 비교해서 인덱스(위치)값을 추출 해냄
    for e in emergency:
        answer.append(emer_ls[e])
    return answer