"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 곱하기 혹은 더하기
description : 각 자리가 숫자(0부터 9)로만 이루어진 문자열 S가 주어졌을 때,
왼쪽부터 오른쪽으로 하나씩 모든 숫자를 확인하며 숫자 사이에 'X' 혹은 '+' 연산자를 넣어 결과적으로 만들어질 수 있는 가장 큰 수를 구하는 프로그램을 작성하세요.
단, +보다 X를 먼저 계산하는 일반적인 방식과 달리, 모든 연산은 왼쪽에서부터 순서대로 이루어진다고 가정합니다.
예를 들어 02984라는 문자열이 주어지면, 만들어질 수 있는 가장 큰 수는 ((((0 + 2) X 9) X 8) X 4) = 576 입니다.
"""

nums = list(map(int, input()))
result = nums[0]

for i in range(1, len(nums)):
    if nums[i-1] <= 1 or nums[i] <= 1:
        result += nums[i]
    else:
        result *= nums[i]

print(result)
