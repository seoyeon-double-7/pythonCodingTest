def solution(s):
    #   s.lower()은 s 자체가 바뀌는건 아니라서 s = s.lower()로 해줘야함
    s = s.lower()

    return True if s.count('p') == s.count('y') else False