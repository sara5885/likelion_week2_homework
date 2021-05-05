
# 1번
# money=int(input("가격을 입력하세요"))

# if money >= 10000:
#     print("고기 먹어요")
# elif money >= 5000:
#     print("국밥을 먹어요")
# else:
#     print("라면 먹어요")


#2번

# myfruit=list()

# for i in range (5):
#     print(i+1,"번 과일을 입력하세요!")
#     fruit=input("")
#     myfruit.append(fruit)

# for i in range(5):
#     print(i+1,"번째 과일은 ",myfruit[i],"입니다")


# #3번
# cookies={'탱커':'우유맛쿠키','딜러:칠리맛쿠키','힐러:천사맛쿠키','서포터:석류맛쿠키'}

# for cookie in cookies.keys():
#     if cookie=="탱커":
#         cookies.get('cookie')='다크초코맛쿠키'
#     elif cookie=="딜러":
#         cookies.get('cookie')='라떼맛쿠키'
#     elif cookie="힐러":
#         cookies.get('cookie')='허브맛쿠키'
#     else:
#         continue


# 4번

# def add():
#     a=int(input("숫자 1을 입력하세요"))
#     b=int(input("숫자 2를 입력하세요"))
#     print(a,"+",b,"=",a+b)
# def sub():
#     a=int(input("숫자 1을 입력하세요"))
#     b=int(input("숫자 2를 입력하세요"))
#     print(a,"-",b,"=",a-b)

# def mul():
#     a=int(input("숫자 1을 입력하세요"))
#     b=int(input("숫자 2를 입력하세요"))
#     print(a,"*",b,"=",a*b)

# def div():
#     a=int(input("숫자 1을 입력하세요"))
#     b=int(input("숫자 2를 입력하세요"))
#     print(a,"/",b,"=",a/b)


# while True:
#     num=int(input("말하는 숫자를 입력하세요 1.더하기 2.빼기 3.곱하기 4.나누기 5.종료"))

#     if num==5:
#         print("종료합니다")
#         break
#     elif num==1:
#         add()

#     elif num==2:
#         sub()
#     elif num==3:
#         mul()
#     elif num==4:
#         div()
    


#5번
class Person:
    def __init__(self,name):
        self.name=name

    def hello(self):
        print("안녕 내 이름은",name,"이야")
    
    def walk(self):
        print("나는 걷는 중")

class Worker(Person):
    def __init(self,name,company,mental):
        Person.__init__(self,name)
        self.mental=50
        self.company=company


    def hello(self):
        print("안녕 내 이름은",name,"이고 내가 다니는 회사는 ",company)

    def work(self):
        mental-=10


worker=Worker("빍이츠","삼성")
worker.hello()
worker.walk()
for i in range(7):
    worker.work()
