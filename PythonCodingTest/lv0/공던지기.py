def solution(numbers, k):
#     배열길이 -1에 두배 곱해주고, 길이로 잘라주기
    return numbers[2 * (k - 1) % len(numbers)]