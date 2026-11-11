# -*- coding: utf-8 -*-
# 9학년 수학 9단원 Sequences and Functions
# 출처 = y9m_ch9_problems.html (선생님 OneNote CHAPTER 9 · 9.1 Generating sequences, 9.2 Using the nth term, 9.3 Representing functions)
VOCAB = [
# ── organ : 수열 만들기 (9.1) ──
("Sequence","수열","A list of numbers that follow a rule.","규칙에 따라 늘어놓은 수. 4, 4 2/5, 4 4/5, 5 1/5, …","organ"),
("Term","항","Each number in a sequence.","수열 안의 수 하나하나. 5, 7, 9 의 5 는 1st term.","organ"),
("First term","첫째 항","The number at the start of a sequence.","수열의 맨 앞 수. 그대로 쓰고 규칙을 써서 다음 항을 만든다.","organ"),
("Term-to-term rule","항에서 항으로 가는 규칙","The rule that changes one term into the next term.","앞 항에서 다음 항을 만드는 규칙. 'add 2/5', 'subtract 0.3'.","organ"),
("Next term","다음 항","The term that comes after the last one given.","주어진 마지막 항 다음 수. 7.6 − 0.3 = 7.3.","organ"),
("Pattern","패턴(모양 배열)","One of a set of drawings that grow by a rule.","점(dot)으로 만든 그림. Pattern 1, 2, 3 의 점 개수가 수열이 된다.","organ"),
("Position number","위치 번호","The place of a term in the sequence: 1st, 2nd, 3rd, …","몇 번째 항인지 나타내는 번호 n. 1, 2, 3, 4.","organ"),
("Position-to-term rule","위치에서 항으로 가는 규칙","A rule that uses the position number to work out the term.","위치 번호만 넣으면 그 항이 바로 나오는 규칙. term = 2 × position number + 3.","organ"),
("Linear sequence","선형 수열(등차수열)","A sequence whose terms go up or down by the same amount each time.","이웃한 항의 차이가 늘 같은 수열. 11, 15, 19, 23 (차이 4).","organ"),
("Non-linear sequence","비선형 수열","A sequence whose terms go up or down by a different amount each time.","차이가 매번 달라지는 수열. 4, 5, 7, 10, 14 (차이 1, 2, 3, 4).","organ"),
("Difference","차이","The amount between one term and the next.","뒤 항 − 앞 항. 줄어드는 수열은 음수(−0.3)다.","organ"),
("Two-step rule","두 단계 규칙","A rule with two operations done in order.","두 계산을 쓰인 순서대로. 'add 1/2, then multiply by 2' → (2 + 1/2) × 2.","organ"),
# ── process : n번째 항 (9.2) ──
("nth term","n번째 항(일반항)","A rule in n that gives any term of a sequence.","n 자리에 위치 번호를 넣으면 그 항이 나오는 식. 3n − 1.","process"),
("Common difference","공차(늘 같은 차이)","The same amount added or subtracted each time in a linear sequence.","선형 수열에서 늘 같은 차이 d. nth term 은 dn + □ 꼴.","process"),
("Zero term","0번째 항","The term before the first term: first term minus the difference.","첫째 항 − 차이. nth term 의 뒤 숫자가 된다. 8, 11, 14 → 8 − 3 = 5.","process"),
("Substitute","대입하다","To put a number in place of a letter.","n 자리에 1, 2, 3 … 을 넣는 것. 4n + 3 에 n = 10 → 43.","process"),
("Expression","식(대수식)","A group of numbers and letters with no equals sign.","등호 없는 식. 'Work out an expression for the nth term' → 3n + 5.","process"),
("Tenth term","10번째 항","The term in position 10.","n = 10 을 넣은 값. 1/2 n + 12 → 17.","process"),
("Mixed number","대분수","A whole number and a fraction together, such as 1 1/4.","정수와 분수를 붙여 쓴 수. n/4 의 5th term = 1 1/4.","process"),
("Improper fraction","가분수","A fraction whose top number is bigger than the bottom, such as 5/4.","분자가 분모보다 큰 분수. 5/4 와 1 1/4 둘 다 맞는 답이다.","process"),
# ── blood : 이차 수열과 Serge 방법 (9.2) ──
("Quadratic sequence","이차 수열","A sequence whose nth term has n² in it.","nth term 에 n² 이 든 수열. 2, 5, 10, 17, 26 = n² + 1.","blood"),
("First differences","1차 차이","The differences between neighbouring terms.","이웃한 항의 차이. 2, 5, 10, 17 → +3, +5, +7.","blood"),
("Second differences","2차 차이(차이의 차이)","The differences between the first differences.","1차 차이끼리의 차이. +3, +5, +7 → +2, +2. 같으면 n² 꼴.","blood"),
("Squared","제곱된","Multiplied by itself, written with a small 2, such as n².","같은 수를 두 번 곱한 것(square). n² = n × n. 3² = 9 (6 이 아니다).","blood"),
("Serge's method","세르게 방법","Using second differences and an n² row to find an nth term.","2차 차이가 같으면 n² 줄을 쓰고, 항 − n² 이 늘 같은 수를 더한다.","blood"),
# ── gas : 함수 나타내기 (9.3) ──
("Function","함수","A rule that changes each input into one output.","입력 하나가 규칙을 지나 출력 하나가 되는 것. y = x² + 1.","gas"),
("Function machine","함수 기계","A diagram of boxes that shows the steps of a function.","x → ÷2 → +3 → y 처럼 상자를 차례로 지나는 그림.","gas"),
("Input","입력","The number that goes into a function machine.","기계에 넣는 수 x.","gas"),
("Output","출력","The number that comes out of a function machine.","기계에서 나오는 수 y.","gas"),
("Table of values","값의 표","A table that shows x values and their y values.","x 줄과 y 줄로 된 표. 빈칸(missing values)을 채운다.","gas"),
("Inverse","역(거꾸로)","The opposite operation that undoes another.","y 에서 x 를 구할 때 오른쪽 상자부터 반대로. +3 ↔ −3, ÷2 ↔ ×2.","gas"),
("Mapping diagram","대응도","Two number lines with arrows from each x to its y.","x 수직선과 y 수직선을 그리고 x 에서 y 로 화살표를 긋는 그림.","gas"),
("Equation","방정식(등식)","A statement with an equals sign, such as y = 5(x − 1).","등호가 있는 식. 함수 기계를 'y =' 로 쓴다.","gas"),
("Cubed","세제곱된","Multiplied by itself three times, written with a small 3, such as x³.","같은 수를 세 번 곱한 것(cube). 5³ = 5 × 5 × 5 = 125.","gas"),
]
CATS = [("organ","🔢 수열 만들기 Sequences"),("process","📍 n번째 항 nth term"),
        ("blood","🟰 이차 수열 Quadratic"),("gas","⚙️ 함수 Functions")]
