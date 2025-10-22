def cal_sum(x, y):
    return x + y
def cal_sum2(x, y):
    return x - y
def cal_sum3(x, y):
    return x * y
def cal_sum4(x, y):
    return x / y

print("""
====================================
🥰나만의 계산기에 오신 것을 환영합니다🎇

사용 가능한 연산:
1. 덧셈 (+)
2. 뺄셈 (-)
3. 곱셈 (*)
4. 나눗셈(/)

====================================
""")

while True:
    cal = input("연산자와 숫자 2개를 띄어쓰기로 입력해주세요 (예: + 1.0 3.0)\n종료하려면 q 입력: ").strip()
    if cal.lower() == 'q':
        print("계산기를 종료합니다.")
        break
    try:
        op, num1, num2 = cal.split()
        x = float(num1)
        y = float(num2)

        if op == '+':
            print(f"{x} + {y} = {cal_sum(x, y)}")
        elif op == '-':
            print(f"{x} - {y} = {cal_sum2(x, y)}")
        elif op == '*':
            print(f"{x} * {y} = {cal_sum3(x, y)}")
        elif op == '/':
            print(f"{x} / {y} = {cal_sum4(x, y)}")
        else:
            print("잘못된 연산자입니다. +, -, *, / 중 하나를 입력하세요.")
    except Exception:
        print("입력 형식 오류! 예시처럼 입력해주세요: + 1.0 3.0")