# -*- coding: utf-8 -*-
# 9학년 수학 8단원 Fractions
# 출처 = y9m_ch8_problems.html (선생님 OneNote CHAPTER 8 · 8.1 Fractions and recurring decimals, 8.2 Fractions and the correct order of operations, 8.3 Multiplying fractions, 8.4 Dividing fractions, 8.5 Making calculations easier)
VOCAB = [
# ── organ : 분수와 소수 (8.1) ──
("Fraction","분수","A number written as one whole number over another, such as 5/8.","5/8 처럼 위·아래 두 수로 쓴 수. a/b = a ÷ b.","organ"),
("Decimal","소수","A number written with a decimal point, such as 0.625.","0.625 처럼 소수점으로 쓴 수. 분수를 나누면 소수가 된다.","organ"),
("Convert","변환하다","To change a number into another form.","수를 다른 꼴로 바꾸는 것. 분수 → 소수는 분자 ÷ 분모.","organ"),
("Written method","필산(손으로 푸는 방법)","Working out a calculation on paper, step by step, without a calculator.","계산기 없이 종이에 단계별로 푸는 것. 5 ÷ 8 을 5.000 ÷ 8 로 나눈다.","organ"),
("Long division","긴 나눗셈","A written method for dividing, one digit at a time.","한 자리씩 나누고 나머지를 내려 붙이는 필산. short division 은 그 짧은 꼴.","organ"),
("Terminating decimal","유한소수","A decimal that ends, because the division leaves no remainder.","나머지가 0 이 되어 끝나는 소수. 5/8 = 0.625.","organ"),
("Recurring decimal","순환소수","A decimal in which a digit or group of digits repeats forever.","같은 숫자가 끝없이 되풀이되는 소수. 5/6 = 0.8333… = 0.83̇.","organ"),
("Dot","점(순환 표시)","A dot over the digits that repeat in a recurring decimal.","되풀이되는 숫자 위에 점을 찍는다. 0.83̇ 은 3 만, 0.1̇2̇ 는 12 가 되풀이.","organ"),
("Equivalent","같은 값의, 동치인","Having the same value, written in a different way.","꼴은 달라도 값이 같은 것. 1/8 의 decimal equivalent 는 0.125.","organ"),
("Deduce","추론하다","To work something out from facts you already know.","다시 계산하지 않고 아는 사실로 알아내기. 1/5 = 0.2 → 3/5 = 0.6.","organ"),
("Prime","소수(素數)","A number with exactly two factors: 1 and itself.","1 과 자기 자신만으로 나뉘는 수. 2, 3, 5, 7, 11. 소수(decimal)와 다른 말이다.","organ"),
("Simplest form","기약분수","A fraction that cannot be cancelled any more.","더 약분할 수 없는 분수. 3/9 → 1/3, 18/12 → 3/2.","organ"),
# ── process : 대분수와 계산 순서 (8.2) ──
("Mixed number","대분수","A whole number and a fraction together, such as 3 1/2.","정수와 분수를 붙여 쓴 수. 3 1/2. 답은 보통 대분수로 쓰라고 한다.","process"),
("Whole number","정수","A number with no fraction part, such as 3.","분수 부분이 없는 수. 대분수 3 1/2 의 3.","process"),
("Improper fraction","가분수","A fraction whose top number is bigger than the bottom, such as 7/2.","분자가 분모보다 큰 분수. 7/2. 곱셈·나눗셈 전에 대분수를 가분수로 바꾼다.","process"),
("Top heavy fraction","가분수(위가 무거운 분수)","Another name for an improper fraction.","improper fraction 의 다른 이름. 44/35 처럼 위가 더 크다.","process"),
("Denominator","분모","The bottom number of a fraction.","분수의 아래 수. 더하기·빼기는 분모를 먼저 맞춘다.","process"),
("Common denominator","공통분모","The same bottom number used for two or more fractions.","분모를 같게 맞춘 것(통분). 4/5 + 7/10 → 8/10 + 7/10.","process"),
("LCM","최소공배수","Lowest common multiple: the smallest number that both numbers divide into.","두 수의 공배수 중 가장 작은 수. 4 와 3 → 12. 통분할 때 쓴다.","process"),
("Simplify","간단히 하다","To make a fraction simpler by dividing the top and bottom by the same number.","분자·분모를 같은 수로 나눠 간단히 하는 것. 15/10 = 3/2.","process"),
("Order of operations","계산 순서","The rule for which part of a calculation to do first.","어느 계산을 먼저 하는지 정한 규칙. 분수도 정수와 똑같다.","process"),
("BIDMAS","계산 순서 규칙","Brackets, Indices, Division and Multiplication, Addition and Subtraction.","괄호 → 거듭제곱 → ÷·× (왼쪽부터) → +·− (왼쪽부터).","process"),
("Brackets","괄호","The symbols ( ) that show which part to work out first.","( ) 안을 가장 먼저 계산한다. B.","process"),
("Indices","지수(복수형)","Powers, such as the 2 in 5².","5² 의 2 같은 지수. 괄호 다음으로 먼저 한다. I.","process"),
("Calculation","계산","A sum that you work out.","풀어야 하는 식. Work out these calculations.","process"),
# ── blood : 분수의 곱셈 (8.3) ──
("Multiplication","곱셈","Finding the product of numbers, using ×.","× 계산. 분수는 분자끼리, 분모끼리 곱한다.","blood"),
("Common factor","공약수","A number that divides exactly into two or more numbers.","두 수를 모두 나누어떨어지게 하는 수. 12 와 30 의 공약수 6.","blood"),
("Cancel","약분하다(지우다)","To divide a top number and a bottom number by the same factor.","분자 하나·분모 하나를 같은 수로 나누는 것. 곱하기 전에 미리 한다.","blood"),
("HCF","최대공약수","Highest common factor: the biggest number that divides into both numbers.","두 수의 공약수 중 가장 큰 수. HCF(14, 35) = 7. 한 번에 약분하기 좋다.","blood"),
("Distributive law","분배법칙","Multiplying each part inside separately and adding the results.","나눠서 각각 곱한 뒤 더하는 법칙. 5 2/3 × 12 = 5 × 12 + 2/3 × 12.","blood"),
("Work out","계산하다","To calculate the answer.","답을 계산해서 구하라는 말.","blood"),
# ── gas : 분수의 나눗셈과 계산 전략 (8.4·8.5) ──
("Division","나눗셈","Sharing or grouping, using ÷.","÷ 계산. 분수로 나누면 뒤 분수를 뒤집어 곱한다.","gas"),
("Reciprocal","역수","A fraction turned upside down, such as 4/3 for 3/4.","분수를 위아래로 뒤집은 수. 3/4 → 4/3, 5 → 1/5.","gas"),
("Keep Flip Change","KFC(그대로·뒤집기·바꾸기)","Keep the first fraction, flip the second, change ÷ to ×.","앞은 그대로(Keep), 뒤는 뒤집고(Flip), ÷ 를 × 로(Change).","gas"),
("Inverse operation","역연산","The operation that undoes another, such as ÷ for ×.","반대 계산. × 의 반대는 ÷. 9/11 × □ = 3/4 → □ = 3/4 ÷ 9/11.","gas"),
("Missing number","빈칸의 수","The unknown number in a calculation, shown by a box.","식의 □ 에 들어갈 모르는 수. 역연산으로 구한다.","gas"),
("Share","나누다(나눠 갖다)","To divide something between people.","여러 명이 나눠 갖는 것. 5/8 를 6 명이 → 5/8 ÷ 6.","gas"),
("Enough","충분한","As much as is needed.","필요한 만큼 있나? 필요한 양을 구해 가진 양과 비교한다.","gas"),
("Round down","내림(버림)","To round to the whole number below.","아래 정수로 자르는 것. 4 3/8 잔 → 다 찬 잔은 4 잔.","gas"),
("Area","넓이","The amount of space inside a flat shape.","평면 도형 안쪽 크기. 직사각형 넓이 = 가로 × 세로.","gas"),
("Spot the mistake","틀린 곳 찾기","To find the error in someone's working.","남의 풀이에서 틀린 단계를 찾는 것. 뒤집기를 빼먹은 곳을 본다.","gas"),
("Mentally","암산으로","In your head, without writing or a calculator.","계산기·종이 없이 머릿속으로 계산하는 것.","gas"),
("Strategy","계산 전략","A clever way to make a calculation easier.","계산이 쉬워지게 하는 방법. 1.5 = 3/2 처럼 쉬운 쪽으로 바꾼다.","gas"),
]
CATS = [("organ","🔢 분수와 소수 Decimals"),("process","🧮 대분수·계산 순서 BIDMAS"),
        ("blood","✖️ 분수의 곱셈 Multiplying"),("gas","➗ 나눗셈·계산 전략 Dividing")]
