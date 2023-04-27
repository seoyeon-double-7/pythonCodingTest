def solution(s):
    len_s = len(s)//2
    return  s[(len_s-1):(len_s+1)] if not len(s)%2 else s[len_s]

#   인덱스는 길이보다 1 작으므로 1빼주고, 가운데 글자를 반환해야하므로 2로 나눠줌
#
    return str[(len(s)-1)//2 : len(s)//2 + 1]