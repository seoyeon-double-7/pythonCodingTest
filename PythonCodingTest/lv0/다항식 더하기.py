# 내가 짠 코드

def solution(polynomial):
    xcount = 0
    count = 0

    for i in polynomial.split(' + '):
        if i.isdigit():
            count += int(i)
        else:
            xcount = xcount + 1 if i == 'x' else xcount + int(i[:-1])

    #   상수항이 없는 경우
    if count == 0:
        if xcount == 0:
            return '0'
        else:
            #            x의 계수가 1일 경우 생략
            if xcount == 1:
                return 'x'
            else:
                return str(xcount) + 'x'

    #   상수항이 있는 경우
    else:
        if xcount == 0:
            return str(count)
        else:
            if xcount == 1:
                return 'x + ' + str(count)
            else:
                return str(xcount) + 'x + ' + str(count)

# fstring으로 간단하게 표현
def solution(polynominal):
    xcount = 0  # x의 계수
    const = 0  # 상수

    for i in polynominal.split(' + '):
        if i.isdigit():  # 상수
            const += int(i)
        else:  # x의 계수 계산
            xcount = xcount + 1 if i == 'x' else xcount + int(i[:-1])

    #    항이 없을때(x)
    if xcount == 0:
        return f'{const}'

    #    x의 계수가 1일때
    elif xcount == 1:
        #        상수항이 있을 때 / 상수항이 없을 때
        return f'x + {const}' if const else 'x'
    #    x의 계수가 2 이상일때
    else:
        #        상수항이 있을 때 / 상수항이 없을 때
        return f'{xcount}x + {const}' if const != 0 else f'{xcount}x'