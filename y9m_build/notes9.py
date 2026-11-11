# -*- coding: utf-8 -*-
NOTES = [
("🔢", "9.1 Generating sequences", "수열 만들기", [
 ("두 가지 규칙 — term-to-term 과 position-to-term",
  "수열 <b>sequence</b> 의 수 하나하나가 항 <b>term</b> 이다.<br><br>"
  "① 항에서 항으로 가는 규칙 <b>term-to-term rule</b> — 앞 항으로 다음 항을 만든다. 'add 2'<br>"
  "② 위치에서 항으로 가는 규칙 <b>position-to-term rule</b> = <b>nth term</b> — 위치 번호 <b>position number</b> n 만 넣으면 바로 나온다. '2n + 3'<br><br>"
  "Starter 2 (점 그림 <b>pattern</b>): 5, 7, 9, 11<br>"
  "• term-to-term rule: <b>add 2</b><br>"
  "• position-to-term rule: <b>2 × position number + 3</b> → nth term = <b>2n + 3</b><br><br>"
  "★ 'Write the term-to-term rule' 에 2n + 3 을 쓰면 틀린다. 둘을 바꿔 쓰지 않는다."),
 ("★ 함정 1 — 줄어드는 수열과 분수 항",
  "Starter 1 a: 4, 4 2/5, 4 4/5, 5 1/5 → <b>add 2/5</b><br>"
  "다음 두 항 <b>next two terms</b>: 5 1/5 + 2/5 = <b>5 3/5</b>, 5 3/5 + 2/5 = 5 5/5 = <b>6</b><br>"
  "&nbsp;&nbsp;✘ 5 5/5 ← 분자가 분모와 같으면 정수로 올린다<br><br>"
  "Starter 1 b: 8.5, 8.2, 7.9, 7.6 → <b>subtract 0.3</b> (= add −0.3)<br>"
  "다음 두 항: <b>7.3, 7</b><br><br>"
  "★ 줄어드는 수열은 '−0.3' 처럼 <b>빼기</b>로 쓴다. 'add 0.3' 이라고 쓰면 반대 방향이다."),
 ("★ 함정 2 — linear 인가 non-linear 인가: 차이를 전부 구한다",
  "선형 수열 <b>linear sequence</b> — 차이 <b>difference</b> 가 늘 같다<br>"
  "비선형 수열 <b>non-linear sequence</b> — 차이가 매번 다르다<br><br>"
  "뒤 항 − 앞 항 을 <b>하나도 빼지 않고</b> 다 구한다.<br><br>"
  "Your turn Q1<br>"
  "• a: 11, 15, 19, 23, 27 → 4, 4, 4, 4 → <b>linear</b><br>"
  "• d: 20, 18, 15, 11, 6 → −2, −3, −4, −5 → <b>non-linear</b><br>"
  "• h: 3 1/2, 5 1/2, 9 1/2, 17 1/2, 33 1/2 → 2, 4, 8, 16 → <b>non-linear</b> (두 배씩 커짐)<br>"
  "• i: 20, 12, 4, −4, −12 → −8, −8, −8, −8 → <b>linear</b> (음수로 내려가도 같으면 linear)<br><br>"
  "★ 'Explain your answers' — \"The terms go up/down by the <b>same amount</b> each time.\" 처럼 이유를 쓴다."),
 ("★ 함정 3 — 두 단계 규칙은 쓰인 순서대로",
  "두 단계 규칙 <b>two-step rule</b>: 쓰인 순서대로 계산한다. BIDMAS 가 아니다.<br>"
  "첫째 항 <b>first term</b> 은 그대로 쓰고 규칙을 두 번 쓴다.<br><br>"
  "Your turn Q2 b: first term 2, Add 1/2, then multiply by 2<br>"
  "✔ (2 + 1/2) × 2 = <b>5</b> → (5 + 1/2) × 2 = <b>11</b> → 2, 5, 11<br>"
  "✘ 2 + 1/2 × 2 = 3 ← × 를 먼저 해 버린 틀린 풀이<br><br>"
  "Worked example 9.1 c: first term 3, square, then subtract 5<br>"
  "✔ 3² − 5 = <b>4</b> → 4² − 5 = <b>11</b> → 3, 4, 11<br>"
  "✘ (3 − 5)² = 4 ← 순서를 바꿔 버린 풀이 (첫 답이 우연히 같아도 다음 항이 틀어진다)"),
]),
("📍", "9.2 Using the nth term", "n번째 항(일반항) 쓰기", [
 ("nth term 에 n 을 대입하기",
  "n 자리에 1, 2, 3 … 을 넣는다 = 대입 <b>substitute</b>.<br>"
  "3n 은 <b>3 × n</b> 이다.<br><br>"
  "Your turn Q2<br>"
  "• a: 4n + 3 → 7, 11, 15 · 10번째 항 <b>tenth term</b> = 4 × 10 + 3 = <b>43</b><br>"
  "• b: 2n − 5 → <b>−3</b>, −1, 1 · 10th = 15 ← 음수가 나와도 된다<br>"
  "• d: n/5 → 1/5, 2/5, 3/5 · 10th = 10/5 = <b>2</b><br><br>"
  "Worked example 9.2 b: n/4 의 5th term = 5/4 = 1 1/4<br>"
  "★ 가분수 <b>improper fraction</b> 5/4 와 대분수 <b>mixed number</b> 1 1/4 둘 다 맞다."),
 ("★ 함정 1 — n² 는 2n 이 아니다",
  "n² = <b>n × n</b> (제곱 <b>squared</b>), 2n = 2 × n<br><br>"
  "• n = 2 일 때 2² = 4, 2 × 2 = 4 ← 우연히 같다<br>"
  "• n = 3 일 때 3² = <b>9</b>, 2 × 3 = 6 ← 다르다<br><br>"
  "Worked example 9.2 a: n² + 4 → 5, 8, <b>13</b> · 10th = 10² + 4 = <b>104</b><br>"
  "&nbsp;&nbsp;✘ 3번째 항 10, 10번째 항 24 ← n² 을 2n 으로 계산한 답<br>"
  "Your turn Q2 e: n² − 1 → 0, 3, 8 · 10th = <b>99</b>"),
 ("선형 수열의 nth term 구하기 — 세 단계",
  "① 공차 <b>common difference</b> d 를 구한다 → nth term 은 <b>dn + □</b><br>"
  "② 0번째 항 <b>zero term</b> = 첫째 항 − d → 이것이 □<br>"
  "③ 확인: n = 1, 2 를 넣어 처음 항이 나오는지 본다.<br><br>"
  "Starter 4 a: 8, 11, 14, 17 → d = 3 → 3n, 8 − 3 = 5 → <b>3n + 5</b><br>"
  "확인 n = 2 → 6 + 5 = 11 ✓<br><br>"
  "Example: 6, 8, 10, 12 → 2n 줄 2, 4, 6, 8 과 비교 → 늘 4 크다 → <b>2n + 4</b><br>"
  "★ 'multiply by 2' 는 term-to-term rule 이 아니다. 6, 8, 10 의 term-to-term rule 은 <b>add 2</b>."),
 ("★ 함정 2 — 줄어드는 수열은 차이가 음수",
  "Starter 4 b: 19, 14, 9, 4 → d = <b>−5</b> → <b>−5n</b><br>"
  "0번째 항 = 19 − (−5) = <b>24</b> → <b>24 − 5n</b> (= −5n + 24)<br>"
  "&nbsp;&nbsp;✘ 5n + 14 ← 차이를 +5 로 본 답 (n = 1 → 19 지만 n = 2 → 24 로 커진다)<br><br>"
  "Your turn Q12<br>"
  "• a: 9 1/4, 9, 8 3/4 → d = −1/4 → 9 1/4 + 1/4 = 9 1/2 → <b>9½ − ¼n</b><br>"
  "• b: 20, 19.8, 19.6 → d = −0.2 → <b>20.2 − 0.2n</b><br>"
  "• d: −5, −6.5, −8 → d = −1.5 → −5 + 1.5 = −3.5 → <b>−1.5n − 3.5</b><br><br>"
  "★ 0번째 항 = 첫째 항 − 차이. 차이가 음수면 <b>더해진다</b>(빼기의 빼기). 마지막에 n = 1, 2 로 꼭 확인한다."),
 ("이차 수열 — Serge's method",
  "1차 차이 <b>first differences</b> 가 다르면 2차 차이 <b>second differences</b>(차이의 차이)를 본다.<br>"
  "2차 차이가 같으면 이차 수열 <b>quadratic sequence</b> → nth term 에 <b>n²</b> 이 들어 있다.<br><br>"
  "Serge: 2, 5, 10, 17, 26<br>"
  "• 1차 차이 +3, +5, +7, +9 → 2차 차이 <b>+2, +2, +2</b><br>"
  "• n² 줄 1, 4, 9, 16 과 비교 → 늘 1 크다 → <b>n² + 1</b><br><br>"
  "Your turn Q6 (모두 2차 차이 2 → n² + c, c = 첫째 항 − 1)<br>"
  "• a: 4, 7, 12 → <b>n² + 3</b> · c: 0, 3, 8 → <b>n² − 1</b> · d: −8, −5, 0 → <b>n² − 9</b><br><br>"
  "★ c 를 구할 때 첫째 항에서 <b>1² = 1</b> 을 뺀다. 2 나 차이(3)를 빼지 않는다.<br>"
  "★ 1차 차이만 보고 'non-linear' 에서 멈추지 말고 2차 차이까지 간다."),
]),
("⚙️", "9.3 Representing functions", "함수 나타내기", [
 ("function machine — 입력에서 출력으로",
  "함수 기계 <b>function machine</b>: 입력 <b>input</b> x 가 상자를 왼쪽부터 차례로 지나 출력 <b>output</b> y 가 된다.<br>"
  "값의 표 <b>table of values</b>: x 줄과 y 줄.<br><br>"
  "Starter 5 a1: x → ÷2 → +3 → y<br>"
  "• x = 6 → 6 ÷ 2 + 3 = <b>6</b><br>"
  "• x = 11 → 11 ÷ 2 + 3 = <b>8 1/2</b>"),
 ("★ 함정 1 — y 에서 x 로: 오른쪽 상자부터 거꾸로",
  "역 <b>inverse</b>: 오른쪽 상자부터 <b>반대 연산</b>을 한다.<br>"
  "+3 ↔ −3, ÷2 ↔ ×2, ×5 ↔ ÷5, −1 ↔ +1<br><br>"
  "Starter 5 a1 (x → ÷2 → +3 → y), y = 12<br>"
  "✔ 12 − 3 = 9 → 9 × 2 = <b>18</b><br>"
  "✘ 12 × 2 − 3 = 21 ← 왼쪽 상자부터 거꾸로 한 답<br><br>"
  "Starter 5 a2 (x → −1 → ×5 → y), y = 35<br>"
  "✔ 35 ÷ 5 = 7 → 7 + 1 = <b>8</b><br>"
  "★ 답을 다시 기계에 넣어 확인한다: (8 − 1) × 5 = 35 ✓"),
 ("★ 함정 2 — 식으로 쓸 때 괄호",
  "식 <b>equation</b> 은 'y =' 를 왼쪽에 쓰고 기계 순서대로 만든다.<br><br>"
  "• x → ÷2 → +3 → y : 나누고 더하기 → <b>y = x/2 + 3</b><br>"
  "• x → −1 → ×5 → y : 먼저 빼고 그다음 곱하기 → <b>y = 5(x − 1)</b><br>"
  "&nbsp;&nbsp;✘ y = 5x − 1 ← 이것은 '×5 먼저, −1 나중' 기계다<br><br>"
  "★ + 나 − 가 <b>먼저</b> 오고 × 가 나중이면 괄호가 꼭 필요하다."),
 ("제곱·세제곱 기계와 mapping diagram",
  "□² = 제곱 <b>squared</b>, □³ = 세제곱 <b>cubed</b><br><br>"
  "Worked example 9.3: x → □² → +1 → y<br>"
  "x 0, 1, 2, 3 → y <b>1, 2, 5, 10</b> → <b>y = x² + 1</b><br>"
  "대응도 <b>mapping diagram</b>: x 수직선과 y 수직선을 그리고 0→1, 1→2, 2→5, 3→10 으로 화살표.<br><br>"
  "Your turn Q2 ii: x → □³ → −3 → y<br>"
  "• 1³ − 3 = <b>−2</b> (1³ = 1, 3 이 아니다)<br>"
  "• 5³ − 3 = 125 − 3 = <b>122</b><br>"
  "• 10³ − 3 = 1000 − 3 = <b>997</b><br><br>"
  "★ 5³ 을 5 × 3 = 15 로 하면 틀린다. <b>5 × 5 × 5</b>.<br>"
  "★ y = (x + 1)² 와 y = x² + 1 은 다르다. 기계 순서가 □² 먼저면 x² + 1."),
]),
]
