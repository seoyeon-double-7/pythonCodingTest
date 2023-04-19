data_list = ['but','i','wont','hesitate','no','more','no','more','it','cannot','wait','im','yours']

#중복 제거
data_list = list(set(data_list))

data_list.sort()
print(data_list)

data_list.sort(key=lambda x : len(x))

print(data_list)