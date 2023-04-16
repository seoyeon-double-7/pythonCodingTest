def solution(dot):
    if(dot[0] > 0):
        if(dot[1] > 0):
            return 1
        return 4
    else:
        if(dot[1]>0):
            return 2
        return 3


# 간단한 방법
# def solution(dot):
#     quad = [(3,2),(4,1)]
#     return quad[dot[0] > 0][dot[1] > 0]