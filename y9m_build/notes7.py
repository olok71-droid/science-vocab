# -*- coding: utf-8 -*-
NOTES = [
("⭕", "7.1 Circumference and area of a circle", "원의 둘레와 넓이", [
 ("원의 낱말과 공식 두 개",
  "① 반지름 <b>radius (r)</b> — 중심 <b>centre</b> 에서 원 위까지<br>"
  "② 지름 <b>diameter (d)</b> — 중심을 지나 끝에서 끝까지<br>"
  "&nbsp;&nbsp;→ <b>d = 2r</b>, <b>r = d ÷ 2</b><br>"
  "③ 원둘레 <b>circumference (C)</b> — 원 한 바퀴의 길이 = 원의 둘레 <b>perimeter</b><br><br>"
  "공식 <b>formulae</b><br>"
  "• <b>C = πd = 2πr</b> — 길이라서 단위 cm, m<br>"
  "• <b>A = πr²</b> — 넓이 <b>area</b> 라서 단위 cm², m²<br><br>"
  "π (<b>pi</b>) = 3.14159… 끝없이 이어지는 무리수 <b>irrational number</b> 다.<br>"
  "계산기의 <b>π 버튼</b>을 쓴다. 3.14 로 치면 답이 조금씩 어긋난다."),
 ("★ 함정 1 — 넓이에 지름을 그대로 넣으면 답이 4 배",
  "넓이 공식 A = πr² 에는 꼭 <b>반지름 radius</b> 을 넣는다.<br><br>"
  "Worksheet Q4 (a): 지름 <b>diameter</b> 2 cm<br>"
  "✔ r = 2 ÷ 2 = 1 → π × 1² = <b>3.1 cm²</b><br>"
  "✘ π × 2² = 12.6 cm² ← 지름을 그대로 제곱한 틀린 답 (4 배)<br><br>"
  "Worked example 7.1 b: 지름 7 m → r = 3.5 → π × 3.5² = <b>38.5 m²</b><br><br>"
  "★ 그림에서 선이 <b>중심을 지나 끝에서 끝까지</b> 가면 지름, <b>중심에서 원까지만</b> 가면 반지름이다.<br>"
  "★ 문제를 풀기 전에 '이게 r 인가 d 인가'를 먼저 적어 둔다."),
 ("★ 함정 2 — πr² 는 (πr)² 가 아니다",
  "계산 순서 <b>order of operations</b>: 제곱이 곱셈보다 먼저다.<br><br>"
  "r = 4 일 때<br>"
  "✔ π × 4² = π × 16 = <b>50.3 cm²</b><br>"
  "✘ (π × 4)² = 157.9 ← π 까지 같이 제곱한 틀린 답<br><br>"
  "★ r 을 <b>먼저 제곱</b>하고 그다음 π 를 곱한다."),
 ("★ 함정 3 — 반올림 자리: d.p. 와 s.f. 는 다르다",
  "① 소수 자리 <b>decimal places (d.p.)</b> — 소수점 뒤 자리 수<br>"
  "&nbsp;&nbsp;37.699… → 2 d.p. = <b>37.70</b><br>"
  "&nbsp;&nbsp;★ 끝의 0 을 지워 37.7 로 쓰면 2 d.p. 가 아니다.<br><br>"
  "② 유효숫자 <b>significant figures (s.f.)</b> — 0 이 아닌 첫 숫자부터 센다<br>"
  "&nbsp;&nbsp;50.265… → 3 s.f. = <b>50.3</b><br>"
  "&nbsp;&nbsp;38.484… → 3 s.f. = <b>38.5</b><br><br>"
  "③ 가장 가까운 밀리미터 <b>nearest millimetre</b><br>"
  "&nbsp;&nbsp;1 cm = 10 mm 라서 cm 로는 소수 첫째 자리(1 d.p.)까지다.<br>"
  "&nbsp;&nbsp;d = 15 ÷ π = 4.774… cm → <b>4.8 cm</b> (= 48 mm)<br><br>"
  "★ 반올림은 <b>맨 마지막에 한 번만</b> 한다. 중간에 반올림하면 답이 어긋난다."),
 ("π 를 남겨서 답하기 — in terms of π",
  "\"Leave your answer <b>in terms of π</b>\" = π 를 3.14 로 바꾸지 말고 글자처럼 남겨라.<br>"
  "그래서 답이 반올림 안 된 정확한 값 <b>exact value</b> 이다.<br><br>"
  "원둘레 C = πd = 2πr<br>"
  "• 지름 8 cm → <b>8π cm</b><br>"
  "• 반지름 10 cm → 2 × 10 = <b>20π cm</b><br>"
  "• 반지름 1.7 mm → <b>3.4π mm</b><br><br>"
  "넓이 A = πr²<br>"
  "• 지름 8 cm → r = 4 → <b>16π cm²</b><br>"
  "• 반지름 1 cm → 1² = 1 → <b>π cm²</b> (1π 라고 쓰지 않는다)<br><br>"
  "★ 원둘레는 반지름을 <b>두 배</b>, 넓이는 반지름을 <b>제곱</b>해서 π 앞에 쓴다. 섞지 않는다."),
 ("거꾸로 구하기 — working backwards",
  "원둘레나 넓이를 주고 지름·반지름을 묻는 문제.<br><br>"
  "① 원둘레 → 지름: <b>d = C ÷ π</b><br>"
  "&nbsp;&nbsp;C = 12 cm → d = 12 ÷ π = <b>3.82 cm</b><br>"
  "② 원둘레 → 반지름: <b>r = C ÷ (2π)</b><br>"
  "&nbsp;&nbsp;C = 80 cm → r = 80 ÷ (2π) = <b>12.73 cm</b><br>"
  "③ 넓이 → 반지름: <b>r = √(A ÷ π)</b><br>"
  "&nbsp;&nbsp;A = 20 → r = √(20 ÷ π) = <b>2.52 cm</b><br>"
  "④ 넓이 → 지름: 반지름을 구한 뒤 <b>× 2</b><br>"
  "&nbsp;&nbsp;A = 400 → r = 11.28… → d = <b>22.57 cm</b><br><br>"
  "★ 계산기에 <b>괄호</b>를 꼭 친다: 80 ÷ (2π). 80 ÷ 2 × π 로 누르면 틀린다.<br>"
  "★ 넓이에 π 가 붙어 있으면 (36π) πr² = 36π → r² = 36 → <b>r = 6</b>. 계산기가 필요 없다.<br>"
  "★ 지름을 물었는데 반지름에서 멈추는 실수가 많다. 마지막 × 2 를 잊지 않는다."),
 ("★ 함정 4 — 두 단계 문제: 넓이 ↔ 원둘레",
  "넓이를 주고 원둘레를 묻거나, 원둘레를 주고 넓이를 묻는다. 바로 못 간다.<br><br>"
  "넓이 → <b>반지름</b> → 원둘레<br>"
  "&nbsp;&nbsp;A = 40 cm² → r = √(40 ÷ π) = 3.568… → C = 2πr = <b>22.42 cm</b><br><br>"
  "원둘레 → <b>반지름</b> → 넓이<br>"
  "&nbsp;&nbsp;C = 60 cm → r = 60 ÷ (2π) = 9.549… → A = πr² = <b>286.48 cm²</b><br><br>"
  "★ 가운데 반지름 3.568… 을 3.6 으로 반올림하지 말고 계산기에 그대로 둔다(<b>ANS</b> 버튼).<br>"
  "★ 문제지에 '40cm' 라고 적혀 있어도 넓이라면 단위는 <b>cm²</b> 다."),
 ("★ 함정 5 — 바퀴 문제: 한 바퀴 = 원둘레, 단위 맞추기",
  "바퀴가 한 바퀴 <b>revolution</b> 구르면 땅 위로 <b>원둘레만큼</b> 간다.<br><br>"
  "Apply Q3: 지름 62 cm 바퀴가 80 바퀴<br>"
  "&nbsp;&nbsp;거리 = π × 62 × 80 = 15582.3 cm → ÷ 100 → <b>155.8 m</b><br>"
  "&nbsp;&nbsp;★ 답을 <b>metres</b> 로 달라고 했다. cm 로 내면 틀린다.<br><br>"
  "Apply Q6: 지름 15 cm 바퀴가 50 m 간다. 몇 바퀴?<br>"
  "&nbsp;&nbsp;① 먼저 단위를 맞춘다: 50 m = <b>5000 cm</b><br>"
  "&nbsp;&nbsp;② 한 바퀴 = π × 15 = 47.12 cm<br>"
  "&nbsp;&nbsp;③ 5000 ÷ 47.12 = 106.10…<br>"
  "&nbsp;&nbsp;④ <b>complete revolutions</b> (다 돈 바퀴) → <b>106</b><br><br>"
  "★ 106.1 바퀴면 107 번째는 다 돌지 못했다. 그래서 반올림이 아니라 <b>내림 round down</b>."),
 ("★ 함정 6 — 올림이냐 내림이냐는 상황이 정한다",
  "계산 결과가 소수로 나와도 답은 사람·물건 수라 정수다. 어느 쪽으로 자를지 따진다.<br><br>"
  "① <b>내림 round down</b> — 모자라면 안 되는 자리가 '한 사람/한 마리 몫'일 때<br>"
  "&nbsp;&nbsp;• 테이블 하나에 565.5 ÷ 70 = 8.07… → <b>8명</b> (0.07명은 못 앉는다)<br>"
  "&nbsp;&nbsp;• 닭 12,050 ÷ 3 = 4016.67 → <b>4016 마리</b> (<b>maximum</b>)<br>"
  "&nbsp;&nbsp;• 다 돈 바퀴 106.1 → <b>106</b><br><br>"
  "② <b>올림 round up</b> — 덜 사면 일이 다 안 끝날 때<br>"
  "&nbsp;&nbsp;• 잔디씨 4087.67 ÷ 50 = 81.75 봉지 → <b>82 봉지</b><br>"
  "&nbsp;&nbsp;&nbsp;&nbsp;값 = 82 × £1.49 = <b>£122.18</b><br><br>"
  "★ 기계적으로 반올림(81.75 → 82 는 맞지만 8.07 → 8, 4016.67 → 4017 은 틀림)하지 말고 "
  "<b>'실제로 가능한가'</b>를 생각한다."),
 ("★ 함정 7 — 'Are there enough …?' 는 비교 문장으로 답한다",
  "Apply Q8: 지름 180 cm 테이블 18 개, 손님 145 명, 한 명당 70 cm 필요<br><br>"
  "① 테이블 둘레 = π × 180 = 565.5 cm<br>"
  "② 한 테이블 = 565.5 ÷ 70 = 8.07… → <b>8명</b> (내림)<br>"
  "③ 18 × 8 = <b>144 seats</b><br>"
  "④ 144 &lt; 145<br><br>"
  "답: <b>\"18 × 8 = 144 seats, but there are 145 guests, so there are not enough tables.\"</b><br><br>"
  "★ Yes / No 만 쓰면 점수가 안 된다. <b>두 수와 비교</b>를 같이 쓴다.<br>"
  "★ 8.07 을 그대로 18 에 곱하면 145.3 이 나와 '충분하다'는 틀린 결론이 된다."),
 ("★ 함정 8 — 둘레는 테두리 전부, 고리는 테두리가 두 개",
  "둘레 <b>perimeter</b> = 모양을 한 바퀴 도는 <b>모든 테두리</b> 길이.<br><br>"
  "① 고리 <b>ring</b> 모양 (Apply Q7, 지름 8 cm·5 cm)<br>"
  "&nbsp;&nbsp;바깥 원둘레 + <b>안쪽 원둘레</b> = π × 8 + π × 5 = 13π = <b>40.84 cm</b><br>"
  "&nbsp;&nbsp;★ 안쪽 테두리를 빼먹기 쉽다.<br><br>"
  "② L 모양 (Apply Q4)<br>"
  "&nbsp;&nbsp;안쪽으로 꺾인 변을 바깥으로 밀면 큰 직사각형이 된다 → 2 × (11 + 12) = <b>46 cm</b><br>"
  "&nbsp;&nbsp;원 (r = 7) = 2π × 7 = 43.98 cm → <b>Shape A has the greatest perimeter.</b><br><br>"
  "③ 'same perimeter' (Apply Q5)<br>"
  "&nbsp;&nbsp;정사각형 4 × 60 = 240 → 2πx = 240 → x = 240 ÷ (2π) = <b>38.20 cm</b><br>"
  "&nbsp;&nbsp;★ 그림에서 x 가 중심에서 원까지면 반지름이다."),
 ("★ 함정 9 — 버린 비율의 분모는 처음 전체",
  "Apply Q11: 한 변 6 cm 정사각형 금속판에서 지름 6 cm 원을 잘라낸다.<br><br>"
  "① 정사각형 = 6 × 6 = 36 cm²<br>"
  "② 원 (r = 3) = 9π = 28.27 cm²<br>"
  "③ 버린 부분 = 36 − 9π = 7.73 cm²<br>"
  "④ <b>percentage wasted</b> = 7.73 ÷ <b>36</b> × 100 = <b>21.5%</b><br><br>"
  "★ 분모는 원(28.27)이 아니라 <b>처음 금속판(36)</b>이다. 28.27 로 나누면 27.3% 로 틀린다.<br>"
  "★ 원이 정사각형 안에 꼭 맞으면(<b>inscribed</b>) 정사각형 한 변 = 원의 <b>지름</b>."),
]),
("🧩", "7.2 Areas of compound shapes", "복합 도형의 넓이", [
 ("복합 도형 3단계 + 넓이 공식",
  "복합 도형 <b>compound shape</b> = 간단한 도형 여러 개를 붙인 모양.<br><br>"
  "① 간단한 도형으로 나눈다 <b>divide</b><br>"
  "② 각각 넓이를 구한다<br>"
  "③ 더하거나 <b>add</b> 빼서 <b>subtract</b> 원하는 넓이를 구한다<br><br>"
  "넓이 공식<br>"
  "• 직사각형 <b>rectangle</b>: A = bh<br>"
  "• 삼각형 <b>triangle</b>: A = ½bh<br>"
  "• 사다리꼴 <b>trapezium</b>: A = ½(a + b)h<br>"
  "• 원 <b>circle</b>: A = πr²<br>"
  "• 반원 <b>semicircle</b>: A = ½ × πr²<br><br>"
  "★ 삼각형은 <b>½</b> 을 꼭 곱한다. 직사각형의 반이다."),
 ("★ 함정 1 — 그림에 없는 길이는 빼기로 찾는다",
  "Starter a: 전체 높이 5 cm, 위 조각 높이 3 cm → 아래 조각 높이 = 5 − 3 = <b>2 cm</b><br><br>"
  "Q1 (h) T 모양<br>"
  "&nbsp;&nbsp;기둥 너비 = 20 − 7 − 6 = <b>7</b>, 막대 높이 = 16 − 9 = <b>7</b><br>"
  "&nbsp;&nbsp;20 × 7 + 7 × 9 = 140 + 63 = <b>203 cm²</b><br><br>"
  "★ <b>가로는 가로끼리, 세로는 세로끼리</b> 빼고 더한다. 가로 길이를 세로에서 빼면 안 된다.<br>"
  "★ 같은 길이를 두 번 세지 않도록 나눈 조각에 선을 그어 표시한다."),
 ("★ 함정 2 — 색칠한 넓이 = 큰 도형 − 빈 도형",
  "색칠한 부분의 넓이 <b>shaded area</b> 는 대부분 <b>빼기</b>로 구한다.<br><br>"
  "Worked example 7.2 b: 원 − 삼각형 = 78.5 − 14 = <b>64.5 cm²</b><br>"
  "Q2 (b) 테두리 액자: 10 × 12 − (10 − 2.5 − 2.5) × (12 − 1 − 1) = 120 − 50 = <b>70 cm²</b><br>"
  "&nbsp;&nbsp;★ 안쪽 크기는 테두리 두께를 <b>양쪽에서</b> 뺀다 (한 번만 빼면 틀린다).<br><br>"
  "Apply Q4 (b) 고리: π × 11² − π × 9² = <b>40π = 125.66 cm²</b><br>"
  "&nbsp;&nbsp;★ π(11 − 9)² = 4π 로 계산하면 틀린다. 제곱한 뒤에 뺀다.<br><br>"
  "★ H 모양처럼 홈이 파인 도형도 '큰 직사각형 − 홈'이 더 빠르다.<br>"
  "&nbsp;&nbsp;Q1 (i): 14 × 16 − 2 × 28 = <b>168 cm²</b>"),
 ("★ 함정 3 — 반원의 곧은 변이 지름이다",
  "반원 <b>semicircle</b> 이 도형에 붙어 있으면 <b>붙어 있는 곧은 변 = 지름</b>.<br><br>"
  "Worked example 7.2 a: 9 cm 변에 반원 → r = 9 ÷ 2 = <b>4.5</b><br>"
  "&nbsp;&nbsp;½ × π × 4.5² = 31.8 → 직사각형 27 + 31.8 = <b>58.8 cm²</b><br><br>"
  "Your turn c: 4.6 cm 는 중심 점에서 아래까지 → 이번엔 <b>반지름</b>이다.<br>"
  "&nbsp;&nbsp;그래서 지름 = 9.2 cm = 삼각형 높이.<br><br>"
  "Your turn d: 28 mm + 28 mm<br>"
  "&nbsp;&nbsp;위 큰 반원은 <b>반지름</b> 28, 아래 작은 반원은 <b>지름</b> 28 (반지름 14)<br><br>"
  "★ 숫자가 같아도 <b>어디서 어디까지 잰 길이인지</b>로 r 인지 d 인지 정한다.<br>"
  "★ 반원 넓이에 <b>½</b> 을 빼먹으면 원 넓이가 되어 두 배로 틀린다."),
 ("★ 함정 4 — 높이는 밑변에 수직, 빗변은 쓰지 않는다",
  "삼각형·사다리꼴의 높이 <b>height (h)</b> 는 밑변 <b>base</b> 에 <b>수직 perpendicular</b> 으로 잰다.<br><br>"
  "① 비스듬한 변 길이를 높이로 쓰면 틀린다.<br><br>"
  "② Q4 (b): 높이 12 m 가 삼각형 <b>밖</b>(밑변을 늘인 선까지)에 그려져 있어도 그대로 쓴다.<br>"
  "&nbsp;&nbsp;½ × 14.4 × 12 = 86.4 − 직사각형 10.5 = <b>75.9 m²</b><br><br>"
  "③ Q4 (c): 흰 사각형은 65 m 대각선으로 나뉜 <b>직각삼각형 right-angled triangle</b> 두 개<br>"
  "&nbsp;&nbsp;직각을 낀 두 변으로: ½ × 25 × 60 = 750, ½ × 39 × 52 = 1014<br>"
  "&nbsp;&nbsp;28 000 − 750 − 1014 = <b>26,236 m²</b><br>"
  "&nbsp;&nbsp;★ 65 m 는 빗변이라 넓이 계산에 쓰지 않는다 (함정 숫자)."),
 ("★ 함정 5 — 실생활 문제는 넓이 다음 한 단계가 더 있다",
  "Apply Q1 페인트<br>"
  "&nbsp;&nbsp;벽 = 15 × (10 − 4) + ½ × 15 × 4 = 90 + 30 = 120 m²<br>"
  "&nbsp;&nbsp;★ 전체 높이 10 m 에서 지붕 4 m 를 빼야 벽 높이 6 m 다.<br>"
  "&nbsp;&nbsp;페인트 = 8 × 16 = 128 m² → 128 ≥ 120<br>"
  "&nbsp;&nbsp;답: <b>\"Yes, he has enough paint, because 128 m² is more than 120 m².\"</b><br><br>"
  "Apply Q2 닭<br>"
  "&nbsp;&nbsp;밭 = 140 × 85 + ½ × 20 × 15 = 12,050 m²<br>"
  "&nbsp;&nbsp;12,050 ÷ 3 = 4016.67 → <b>maximum</b> 이니 내림 → <b>4016 chickens</b><br><br>"
  "★ 넓이만 구하고 멈추면 반쪽 답이다. 문제가 <b>무엇을 묻는지</b>(페인트가 충분한가, 닭 몇 마리) 끝까지 답한다."),
]),
("📏", "7.3 Large and small units", "아주 크고 아주 작은 단위", [
 ("세 가지 양과 기본 단위",
  "① 길이 <b>length</b> — 얼마나 긴가 → metre (m)<br>"
  "&nbsp;&nbsp;millimetres, centimetres, metres, kilometres<br>"
  "② 질량 <b>mass</b> — 얼마나 무거운가 → gram (g)<br>"
  "&nbsp;&nbsp;grams, kilograms, 톤 <b>tonne</b> (1 t = 1000 kg)<br>"
  "③ 들이 <b>capacity</b> — 그릇에 얼마나 담기나 → litre (L)<br>"
  "&nbsp;&nbsp;litres, millilitres<br><br>"
  "★ litre 는 <b>capacity</b>, gram 은 <b>mass</b> 다. 무게와 들이를 섞지 않는다."),
 ("접두어 표 — prefix 는 '몇 배' 표시",
  "접두어 <b>prefix</b> 는 기본 단위(m, L, g) 앞에 붙는다.<br><br>"
  "• tera <b>T</b> = 10¹² (1조 배)<br>"
  "• giga <b>G</b> = 10⁹ (10억 배)<br>"
  "• mega <b>M</b> = 10⁶ (100만 배)<br>"
  "• kilo <b>k</b> = 10³ (1000 배)<br>"
  "• hecto <b>h</b> = 10² (100 배)<br>"
  "• centi <b>c</b> = 10⁻² (100 분의 1)<br>"
  "• milli <b>m</b> = 10⁻³ (1000 분의 1)<br>"
  "• micro <b>μ</b> = 10⁻⁶ (100만 분의 1)<br>"
  "• nano <b>n</b> = 10⁻⁹ (10억 분의 1)<br><br>"
  "kilo + metre = kilometre = 1000 m<br>"
  "micro + litre = microlitre = 0.000 001 L"),
 ("★ 함정 1 — 대문자 M 과 소문자 m 은 완전히 다르다",
  "• <b>M</b> = mega = <b>100만 배</b> (10⁶) → 1 Mm (megametre) = 1 000 000 m<br>"
  "• <b>m</b> = milli = <b>1000 분의 1</b> (10⁻³) → 1 mm (millimetre) = 0.001 m<br><br>"
  "둘의 차이는 10⁹ 배, 10억 배다.<br><br>"
  "★ 'Mm' 를 'mm' 로 읽으면 답이 10억 배 틀린다. <b>대소문자를 꼭 본다.</b><br>"
  "★ μ 는 그리스 글자 '뮤 mu'. 'u' 나 'm' 이 아니다."),
 ("★ 함정 2 — 큰 단위 → 작은 단위는 곱하고, 반대는 나눈다",
  "단위 변환표 <b>conversion chart</b><br>"
  "mass: t —×1000→ kg —×1000→ g —×1000→ mg<br>"
  "length: km —×1000→ m —×100→ cm —×10→ mm<br>"
  "capacity: L —×1000→ mL<br><br>"
  "• 큰 단위 → 작은 단위: <b>곱한다</b><br>"
  "&nbsp;&nbsp;2.5 Mm = 2.5 × 1 000 000 = <b>2 500 000 m</b><br>"
  "• 작은 단위 → 큰 단위: <b>나눈다</b><br>"
  "&nbsp;&nbsp;6820 g = 6820 ÷ 1000 = <b>6.82 kg</b><br><br>"
  "★ 답을 보고 감으로 확인한다: 큰 단위로 바꾸면 숫자가 <b>작아져야</b> 맞다.<br>"
  "★ m → cm 는 1000 이 아니라 <b>100</b>, cm → mm 는 <b>10</b> 이다. 전부 1000 이라고 외우면 틀린다."),
 ("10 의 거듭제곱 곱셈·나눗셈 — 소수점 옮기기",
  "× 10, × 100, × 1000 … 은 0 의 개수만큼 소수점을 옮긴다.<br><br>"
  "• 3.2 × 100 000 (0 이 5 개) → 오른쪽 5 칸 → <b>320 000</b><br>"
  "• 0.56 × 1 000 000 000 (0 이 9 개) → 오른쪽 9 칸 → <b>560 000 000</b><br>"
  "• 6820 ÷ 1000 (0 이 3 개) → 왼쪽 3 칸 → <b>6.82</b><br>"
  "• 4 500 000 ÷ 1 000 000 → 왼쪽 6 칸 → <b>4.5</b><br><br>"
  "★ 곱하면 <b>오른쪽</b>(커짐), 나누면 <b>왼쪽</b>(작아짐).<br>"
  "★ 칸이 모자라면 0 을 채운다: 0.56 → 560 000 000."),
 ("'Describe a microlitre' — 세 가지를 쓴다",
  "Worked example 7.3 모범답<br><br>"
  "① 무엇을 재는 단위인가: <b>A microlitre is a very small measure of capacity.</b><br>"
  "② 기호: <b>It is represented by the letters μL.</b><br>"
  "③ 기본 단위와의 관계: <b>1 μL = 0.000 001 L = 1 × 10⁻⁶ L</b><br>"
  "&nbsp;&nbsp;= <b>There are one million microlitres in a litre.</b><br>"
  "&nbsp;&nbsp;= 1 microlitre is <b>one millionth</b> of a litre.<br><br>"
  "★ '아주 작은 단위다'만 쓰면 반쪽 답이다. <b>양(capacity) · 기호(μL) · 10⁻⁶</b> 셋을 다 쓴다.<br>"
  "★ 1 L 안에 μL 가 100만 개, 1 μL 는 1 L 의 100만 분의 1. 두 말은 같은 뜻이다."),
 ("★ 함정 3 — 크기 순서는 숫자가 아니라 접두어로",
  "Your turn: 8 micrometres, 8 millimetres, 8 centimetres, 8 metres, 8 kilometres, 8 gigametres<br><br>"
  "숫자(8)가 모두 같으니 <b>접두어 크기</b>만 비교한다.<br>"
  "micro (10⁻⁶) &lt; milli (10⁻³) &lt; centi (10⁻²) &lt; 기본 (1) &lt; kilo (10³) &lt; giga (10⁹)<br><br>"
  "답 (smallest first): <b>8 μm, 8 mm, 8 cm, 8 m, 8 km, 8 Gm</b><br><br>"
  "★ 'starting with the smallest' — <b>작은 것부터</b>. 순서를 거꾸로 쓰면 다 맞아도 틀린다.<br>"
  "★ 숫자가 다르면(예: 5000 mm 와 3 m) 먼저 <b>같은 단위로 바꾼 뒤</b> 비교한다."),
]),
]
