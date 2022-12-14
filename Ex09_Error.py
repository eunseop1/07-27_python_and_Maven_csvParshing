class MyError(Exception):  # 사용자만의 예외 클래스 생성(아무 내용도 없을시 가능)
    pass

class MyCalc:
    def div(self, a, b):
        if b == 0:
            raise BaseException("에러가 발생했습니다")  #예외를 발생시킨다
        return a / b
    def div2(self, a, b):
        if b == 0:
            raise MyError("에러가 발생했습니다!!")  #예외를 발생시킨다
        return a / b


m = MyCalc()
print(m.div(11,4))

try:
    print(m.div(11,0))
except BaseException as e:
    print(e)

try:
    print(m.div2(11,0))
except MyError as e:
    print(e)

