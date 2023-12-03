input_str = "(1, 1)"

# 쉼표로 문자열 분리
parts = input_str.strip("()").split(',')

print(parts)

# 숫자 부분 추출 및 공백 제거
number1 = parts[0].strip('() ')
number2 = parts[1].strip()

# 결과 출력
print("첫 번째 숫자:", number1)
print("두 번째 숫자:", number2)


