arr = [[1,2,3], [4,5,6], [7,8,9]]
arr.reverse()
rotate = list(zip(*arr))

# [1,2,3]
# [4,5,6]
# [7,8,9]
print(rotate)