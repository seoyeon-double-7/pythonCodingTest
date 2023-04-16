def solution(numbers):
    #   기본풀이
    # answer = []
    # for i in numbers:
    #     answer.append(i*2)

    #   리스트 컴프리헨션 활용
    # return [num*2 for num in numbers]

    #   람다로 간단하게!
    return list(map(lambda n: n * 2, numbers))
