# 사칙연산을 하는 클래스를 만들어 보자
class FourCal:
    # __ 는 생성자를 의미
    def __init__(self):  #생성자 - 초기값을 통해서 미리 정해두는게 더 안전하다
        self.first = 0  #초기값
        self.second = 0

    def __init__(self, first=0, second=0):
        self.first = first
        self.second = second

    def set_data(self, first, second):  #메서드
        self.first = first
        self.second = second

    def add(self):
        return self.first + self.second
    def sub(self):
        return self.first - self.second
    def mul(self):
        return self.first * self.second
    def div_float(self):
        return self.first / self.second
    def div_int(self):
        return self.first // self.second
    def mod(self):
        return self.first % self.second

a = FourCal()
print(type(a))
a.set_data(10, 20)

print(a.first)
print(a.second)

print("덧셈: {}".format(a.add()))
print("뺄셈: {}".format(a.sub()))
print("곱셈: {}".format(a.mul()))
print("실수몫: {}".format(a.div_float()))
print("정수몫: {}".format(a.div_int()))
print("나머지: {}".format(a.mod()))

b = FourCal()
print("덧셈: {}".format(b.add()))
b.set_data(11, 4)
print("덧셈: {}".format(b.add()))

c = FourCal(10)
print(c.first)
print(c.second)
#print("정수몫: {}".format(c.div_int()))  # 10/0이기에 에러

d = FourCal(10, 4)
print(d.first)
print(d.second)
print("정수몫: {}".format(d.div_int()))

class MoreCalc(FourCal):  #상속
    def pow(self):  #기능추가
        return self.first ** self.second
    def mod(self):  #기능 오버라이딩
        return self.first % self.second + 1

if __name__ == '__main__':
    m = MoreCalc()
    m.set_data(11, 5)
    print("덧셈: {}".format(m.add()))
    m = MoreCalc(2, 3)
    print("제곱: {}".format(m.pow()))
    print("나머지+1: {}".format(m.mod()))




