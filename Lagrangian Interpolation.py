# 라그랑주 보간법은 여러 점이 주어졌을 때 가장 근사한 식을 산출하는 것으로, 이 식에 x좌표 첫점과 끝점을 일정 간격으로 잘라서 넣으면 궤적을 추정할 수 있을 것으로 예상한다.
import sympy

def inputdata():
    p = int(input('▶ 좌표의 개수를 입력하세요: '))
    data,x,y = [],0,0
    for i in range(p):
        x,y = map(float,input('').split())
        data.append([x,y])
    return data

def polynomialfunc(data):
    n = len(data)
    x = sympy.Symbol('x')
    l,L = 1,0
    for i in range(n):
        for h in range(n):
            if i == h:
                pass
            else:
                l *= (x-data[h][0])/(data[i][0]-data[h][0])
        L += data[i][1]*l
        l = 1
    print(sympy.expand(L))

if __name__ == "__main__":
    data = inputdata()
    print(data)
    polynomialfunc(data)
