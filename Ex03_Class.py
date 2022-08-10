class Family:
    # self는 생성자가 아닌한 쓸수 없다
    last_name = None

kimc = Family()
leec = Family()

kimc.last_name = "김"
leec.last_name = "이"
print(kimc.last_name)
print(leec.last_name)
print()

Family.last_name = "신"  #클래스 이름으로 접근하면 자바의 static처럼 사용가능
kimc.last_name = "김"
leec.last_name = "이"
sinc = Family()
print(kimc.last_name)
print(leec.last_name)
print(sinc.last_name)
print(Family.last_name)
print()