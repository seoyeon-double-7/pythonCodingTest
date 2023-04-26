def solution(nums):
    # 골라야하는 폰켓몬의 갯수
    l = len(nums) / 2
    # 종류의 수를 출력하려면, key의 갯수만큼 출력이 될 것.
    # l < key의 갯수: l출력, key의 갯수 > l : key의 갯수 출력
    map = {}
    for i in nums:
        if i in map:
            map[i] += 1
        else:
            map[i] = 1
    print(map)  # {3: 2, 1: 1, 2: 1}
    if l < len(map.keys()):
        return l
    else:
        return len(map.keys())


def solution(nums):
    cnt = len(nums) // 2

    monster = list(set(nums))
    if len(monster) < cnt:
        return len(monster)

    return cnt


def solution(ls):
    return min(len(ls) / 2, len(set(ls)))