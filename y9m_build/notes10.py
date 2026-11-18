# -*- coding: utf-8 -*-
NOTES = [
("📈", "10.1 Functions", "함수 — 요금 문제를 식으로", [
 ("요금 문제는 y = (하루 요금)x + (기본요금)",
  "함수 <b>function</b> — x 값 하나를 넣으면 y 값이 하나 나오는 규칙.<br><br>"
  "기본요금 <b>fixed charge</b> — 날 수와 상관없이 한 번 낸다 → <b>더하는 수</b><br>"
  "하루마다 <b>per day</b> 요금 — 날마다 붙는다 → <b>x 앞의 수</b><br><br>"
  "Starter Q1: ladder, $10 + $3 per day<br>"
  "→ total cost <b>y = 3x + 10</b> (x = 날 수, y = 달러)<br><br>"
  "★ 'Explain why y = 3x + 10' 은 영어 문장으로 이유를 쓴다:<br>"
  "\"The cost is $3 for each day, so <b>3x</b> for x days, plus the fixed charge of <b>$10</b>.\""),
 ("★ 함정 1 — one week 는 x = 1 이 아니다",
  "x 는 <b>날 수(days)</b> 다. 문제 단위를 먼저 확인한다.<br><br>"
  "Starter Q1 a: one week = <b>7 days</b><br>"
  "✔ 10 + 3 × 7 = 10 + 21 = <b>$31</b><br>"
  "✘ 10 + 3 × 1 = $13 ← week 를 그대로 1 로 넣은 답"),
 ("★ 함정 2 — 거꾸로 풀 때는 기본요금부터 뺀다",
  "Starter Q2 a: chainsaw, $15 + $10 per day, Aran pays $45<br>"
  "✔ 15 + 10n = 45 → 10n = <b>30</b> → n = <b>3 days</b><br>"
  "✘ 45 ÷ 10 = 4.5 ← 기본요금을 안 빼고 나눈 답<br><br>"
  "순서: ① 전체 비용 − 기본요금 (45 − 15) ② ÷ 하루 요금 (30 ÷ 10)<br><br>"
  "Starter Q2 b: 글자가 바뀌어도 꼴은 같다<br>"
  "비용 t, 날 수 n → <b>t = 10n + 15</b><br>"
  "★ 문제가 준 글자(t, n)를 그대로 쓴다. y = 10x + 15 라고 쓰면 감점될 수 있다."),
]),
("✖️", "10.2 Plotting graphs", "그래프 그리기 · 축과 절편", [
 ("그래프 그리는 네 단계",
  "일차 함수 <b>linear function</b> — 그래프가 직선 <b>straight line</b>. y = 2x + 3, 2x + 3y = 12<br><br>"
  "① x 값 몇 개를 고른다<br>"
  "② 식에 넣어 y 를 구하고 값의 표 <b>table of values</b> 에 쓴다<br>"
  "③ 좌표 <b>coordinates</b> (x, y) 를 점으로 찍는다 <b>plot</b><br>"
  "④ 자로 직선을 긋고 점 밖으로도 늘인다<br><br>"
  "y = 2x + 3 의 표<br>"
  "x: −2, −1, 0, 1, 2, 3<br>"
  "y: <b>−1</b>, 1, 3, 5, 7, 9<br>"
  "★ x = −2 → 2 × (−2) + 3 = −4 + 3 = <b>−1</b>. 음수 계산에서 부호를 놓치지 않는다."),
 ("★ 함정 1 — x절편은 y = 0, y절편은 x = 0",
  "x절편 <b>x-intercept</b> — 그래프가 x축 <b>x-axis</b> 을 지나는 <b>cross</b> 점 → 이때 <b>y = 0</b><br>"
  "y절편 <b>y-intercept</b> — 그래프가 y축 <b>y-axis</b> 을 지나는 점 → 이때 <b>x = 0</b><br><br>"
  "글자가 반대라서 헷갈린다. <b>x축 위에서는 높이(y)가 0</b> 이라고 기억한다.<br><br>"
  "y = 2x + 3<br>"
  "• x-axis: 2x + 3 = 0 → x = −1.5 → <b>(−1.5, 0)</b><br>"
  "• y-axis: x = 0 → y = 3 → <b>(0, 3)</b><br><br>"
  "★ 'Write the coordinates' 는 숫자 하나가 아니라 <b>(x, y) 두 개</b>를 쓴다. 6 이 아니라 (6, 0)."),
 ("★ 함정 2 — ax + by = c 꼴은 넣고 푼다 (cover-up)",
  "y 가 혼자 있지 않으니 x 나 y 하나를 넣고 남은 글자를 방정식으로 푼다.<br><br>"
  "Worked example 10.2: 2x + 3y = 12<br>"
  "• x = 0 → 3y = 12 → y = <b>4</b><br>"
  "• y = 3 → 2x + 9 = 12 → x = <b>1.5</b><br>"
  "• y = 0 → 2x = 12 → x = <b>6</b><br>"
  "→ x-axis (6, 0), y-axis (0, 4)<br><br>"
  "Your turn Q7: 3x + 2y = 18<br>"
  "x: 0, 1, 2, 4, 6 / y: <b>9, 7.5, 6, 3, 0</b><br>"
  "→ i. x-axis <b>(6, 0)</b> ii. y-axis <b>(0, 9)</b><br><br>"
  "★ 표의 빈칸이 y 줄에 있으면 y 를, x 줄에 있으면 x 를 구한다(y = 7.5 → x = 1).<br>"
  "★ 확인: 점이 모두 한 직선 위에 있어야 한다. x 가 2 늘 때마다 y 가 3 씩 준다(9 → 6 → 3 → 0)."),
 ("★ 함정 3 — x² 그래프는 곡선, 음수 제곱은 양수",
  "Worked example 10.3: y = x² − 3<br>"
  "x: −3, −2, −1, 0, 1, 2, 3<br>"
  "y: <b>6, 1, −2, −3, −2, 1, 6</b><br><br>"
  "• (−3)² = <b>+9</b> → 9 − 3 = 6 (The square of any negative number is positive.)<br>"
  "&nbsp;&nbsp;✘ −9 − 3 = −12 ← 계산기에 −3² 로 친 답. 괄호 (−3)² 를 꼭 친다<br><br>"
  "• 점이 직선 위에 없다 → 자로 잇지 말고 부드러운 곡선 <b>smooth curve</b> 로 잇는다<br>"
  "• y축 양쪽이 똑같다 = 대칭 <b>symmetrical</b> → 표의 y 도 6, 1, −2, −3, −2, 1, 6<br>"
  "• x축과 만나는 점 = 근 <b>root</b>: x² = 3 → x = ±√3 ≈ <b>±1.73</b> (두 개!)<br>"
  "• y축과 만나는 점: <b>(0, −3)</b>"),
 ("★ 함정 4 — 점이 직선 위에 있나 (Does the point lie on the line?)",
  "점의 <b>x</b> 를 식에 넣어 y 를 계산 → 점의 <b>y</b> 와 같으면 Yes, 다르면 No.<br><br>"
  "Add on (a): (−1, 8) on y = 2x + 11 → 2 × (−1) + 11 = <b>9</b> ≠ 8 → <b>No</b><br>"
  "Add on (b): (12, 60) on y = 7x − 18 → 84 − 18 = <b>66</b> ≠ 60 → <b>No</b><br><br>"
  "10.3 Starter<br>"
  "• (a) (2, 5) on y = 3x − 1 → 5 → <b>Yes</b><br>"
  "• (d) (5, 7) on y = −3x + 22 → −15 + 22 = 7 → <b>Yes</b><br>"
  "• (e) (−4, −8) on y = −2x → −2 × (−4) = <b>+8</b> ≠ −8 → <b>No</b><br>"
  "&nbsp;&nbsp;✘ Yes ← 음수 × 음수 = 양수를 놓친 답"),
]),
("📐", "10.3 Gradient and intercepts", "기울기와 절편 — y = mx + c", [
 ("y = mx + c 에서 m 과 c",
  "직선의 식 <b>straight line equation</b> 은 언제나 일반형 <b>general form</b> <b>y = mx + c</b> 로 쓸 수 있다.<br><br>"
  "• m = 기울기 <b>gradient</b> — x 가 1 늘 때 y 가 얼마나 변하나<br>"
  "• c = y절편 <b>y-intercept</b> — x = 0 일 때 y, y축을 지나는 높이<br><br>"
  "y = 2x + 3 → gradient <b>2</b>, y-intercept <b>3</b><br>"
  "Real life: ladder y = 3x + 10 → m = 3 = 하루 요금(rate), c = 10 = 기본요금(fixed charge)<br><br>"
  "오른쪽 아래로 내려가는 직선 = 음의 기울기 <b>negative gradient</b>"),
 ("★ 함정 1 — 순서가 바뀌어도 x 앞의 수가 gradient (부호까지)",
  "Your turn Q1<br>"
  "• a: y = 4x − 6 → gradient <b>4</b>, y-intercept <b>−6</b> (부호 −도 같이)<br>"
  "• c: y = 4 − 6x = −6x + 4 → gradient <b>−6</b>, y-intercept <b>4</b><br>"
  "&nbsp;&nbsp;✘ gradient 4 ← 맨 앞 숫자를 m 으로 착각한 답<br><br>"
  "★ m 은 '맨 앞 수'가 아니라 <b>x 에 붙은 수</b>, c 는 <b>x 가 없는 수</b>다."),
 ("★ 함정 2 — y 를 주어로 (y as the subject) 바꾼 뒤 읽는다",
  "ax + by = c 꼴은 바로 읽으면 틀린다. 먼저 <b>y = …</b> 로 바꾼다 = y 를 주어 <b>subject</b> 로.<br>"
  "① y 가 없는 항을 반대편으로 (부호 바뀜) ② y 앞의 수로 <b>양변 전체</b>를 나눈다<br><br>"
  "Worked example 10.4: 2x + 3y = 12 → 3y = 12 − 2x → y = <b>−⅔x + 4</b><br>"
  "→ gradient <b>−2/3</b>, y-intercept <b>4</b><br>"
  "&nbsp;&nbsp;✘ gradient 2, intercept 12 ← 바꾸지 않고 읽은 답<br><br>"
  "• d: 7x = 1 − 2y → 2y = 1 − 7x → y = ½ − 7/2 x → gradient <b>−7/2</b>, y-intercept <b>1/2</b><br>"
  "• e: 15y − 6x = 8 → y = 6/15 x + 8/15 → gradient <b>2/5</b>, y-intercept <b>8/15</b><br>"
  "• f: ⅔x + 2y = 5 → y = −⅓x + 5/2 → gradient <b>−1/3</b>, y-intercept <b>5/2</b><br><br>"
  "★ 나눌 때 c 도 같이 나눈다(8 → 8/15). 분수는 기약분수 <b>lowest terms</b> 로 줄인다(6/15 → 2/5)."),
 ("★ 함정 3 — gradient = y-change ÷ x-increase (거꾸로 나누지 않는다)",
  "gradient = y 변화량 <b>y-change</b> ÷ x 증가량 <b>x-increase</b> = (y₂ − y₁) / (x₂ − x₁)<br><br>"
  "• a: (2, 4), (4, 10) → (10 − 4) / (4 − 2) = 6/2 = <b>3</b><br>"
  "&nbsp;&nbsp;✘ 2/6 = 1/3 ← x 를 위에 둔 답<br>"
  "• b: (2, 1), (4, 0) → (0 − 1) / (4 − 2) = <b>−1/2</b><br>"
  "&nbsp;&nbsp;✘ 1/2 ← 내려가는 직선인데 부호를 뺀 답<br><br>"
  "★ 그래프에서는 눈금이 딱 맞는 격자점 두 개를 고른다.<br>"
  "★ 왼쪽 → 오른쪽으로 갈 때 내려가면 gradient 는 <b>음수</b>."),
 ("직선의 식 찾기 (Find the equation of each line)",
  "① y축과 만나는 눈금을 읽어 c — 관찰 <b>observation</b><br>"
  "② 격자점 하나를 더 골라 gradient m<br>"
  "③ y = mx + c 로 쓰고, 다른 점을 넣어 확인<br><br>"
  "Question 5<br>"
  "• (d) (0, −1), (3, 8) → m = 9/3 = 3 → <b>y = 3x − 1</b><br>"
  "• (e) (0, 6), (6, 0) → m = −1 → <b>y = −x + 6</b><br>"
  "• (g) (0, −4), (1, 0) → m = 4 → <b>y = 4x − 4</b><br>"
  "• (h) (0, 3), (3, 0) → m = −1 → <b>y = −x + 3</b><br><br>"
  "★ m = −1 이면 1 을 빼고 <b>y = −x + c</b> 로 쓴다. c 가 음수면 + 가 아니라 − 로 쓴다(y = 3x − 1)."),
]),
("🚗", "10.4 Interpreting graphs", "그래프 읽고 해석하기", [
 ("실생활 그래프에서 gradient = rate, y절편 = 처음 값",
  "그래프 해석하기 <b>interpreting graphs</b> — 기울기·절편이 실제로 무엇인지 말한다.<br><br>"
  "• gradient = 변화율 <b>rate</b> → 단위는 <b>y 단위 ÷ x 단위</b> (°C/minute, m/s)<br>"
  "• y-intercept = 처음 값 (시작 온도, 시작 거리)<br>"
  "• 그래프가 직선 → rate 가 일정 <b>constant</b><br><br>"
  "Worked example 10.5 (metal bar)<br>"
  "a. 그래프가 straight line 이라서 rate of cooling 이 constant<br>"
  "b. (0, 500), (50, 300) → (300 − 500) / 50 = <b>−4</b><br>"
  "c. 1분에 4 °C 씩 식는다 — rate of cooling <b>4 °C/minute</b><br>"
  "d. <b>y = 500 − 4t</b><br><br>"
  "★ c 'What does the gradient tell you?' 에 '−4' 숫자만 쓰면 부족하다. <b>단위 + 뜻</b>을 문장으로 쓴다."),
 ("★ 함정 1 — 시간 단위를 맞춘다 (hours → minutes)",
  "Worked example 10.5 e: 같은 빠르기로 계속 식을 때 1½ hours 뒤 온도<br>"
  "t 는 <b>분(minutes)</b> 이다 → 1½ × 60 = <b>90</b><br>"
  "✔ y = 500 − 4 × 90 = 500 − 360 = <b>140 °C</b><br>"
  "✘ 500 − 4 × 1.5 = 494 ← hours 를 그대로 넣은 답<br><br>"
  "★ 10.1 의 one week = 7 days 와 같은 함정이다. 식의 글자가 어떤 단위인지 먼저 본다."),
 ("★ 함정 2 — distance–time graph 의 gradient 는 speed",
  "거리–시간 그래프 <b>distance–time graph</b>: 가로 time, 세로 distance<br>"
  "gradient = 거리 ÷ 시간 = 속력 <b>speed</b><br><br>"
  "Your turn Q1 (car)<br>"
  "a. t = 20 에서 <b>위로</b> 올라가 읽는다 → <b>250 m</b><br>"
  "b. d = 200 에서 <b>옆으로</b> 가 읽는다 → <b>16 s</b><br>"
  "c. speed = 250 ÷ 20 = <b>12.5 m/s</b><br>"
  "d. (0, 0) 에서 시작 → c = 0 → <b>d = 12.5t</b> — 'd in terms of t' = d = (t 가 든 식)<br>"
  "e. 12.5 × 50 = <b>625 m</b><br><br>"
  "★ 격자 한 칸 = 가로 5 s, 세로 50 m. 칸 수를 그대로 답으로 쓰지 않는다.<br>"
  "★ 그래프 밖(50 s)은 읽지 말고 <b>식으로</b> 계산한다."),
 ("Starter 22 — 합동인 짝 찾기 (congruent)",
  "합동 <b>congruent</b> — 돌리거나(rotate) 뒤집어도(reflect) 꼭 겹치는 모양.<br><br>"
  "짝 찾는 순서<br>"
  "① 조각 수를 센다 (정사각형 몇 개, 삼각형 몇 개)<br>"
  "② 조각이 붙은 위치를 비교한다 (같은 쪽 끝인가, 반대쪽 끝인가)<br><br>"
  "• B · C = 정사각형 4개<br>"
  "• D · G = 정사각형 3개 + 삼각형 1개<br>"
  "• A – F: 삼각형이 반대쪽 두 끝 / E – H: 같은 쪽 두 끝<br><br>"
  "★ 조각 수만 같다고 짝이 아니다. A · E · F · H 는 모두 3 + 2 개라서 ② 위치까지 봐야 갈린다."),
]),
]
