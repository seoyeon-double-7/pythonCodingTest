# def solution(sizes):
#     width = []
#     height = []

#     for n1, n2 in sizes:
#         width.append(max(n1, n2))
#         height.append(min(n1, n2))

#     width.sort(reverse=True)
#     height.sort(reverse=True)
#     return width[0] * height[0]

def solution(sizes):
    return max(max(i) for i in sizes) * max(min(i) for i in sizes)