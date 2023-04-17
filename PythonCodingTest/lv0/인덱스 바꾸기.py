def solution(my_string, num1, num2):
    #   스트링을 리스트 타입으로 바꾸고, 값을 변경한 후 다시 string 타입으로!
    answer = ''
    my_string = list(my_string)
    my_string[num1], my_string[num2] = my_string[num2], my_string[num1]

    return answer.join(my_string)