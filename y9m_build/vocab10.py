# -*- coding: utf-8 -*-
# 9학년 수학 10단원 Graphs
# 출처 = y9m_ch10_problems.html (선생님 OneNote CHAPTER 10 · 10.1 Functions, 10.2 Plotting graphs, 10.3 Gradient and intercepts, 10.4 Interpreting graphs)
VOCAB = [
# ── organ : 함수와 그래프 그리기 (10.1, 10.2) ──
("Function","함수","A rule that gives one value of y for each value of x.","x 값 하나를 넣으면 y 값이 하나 나오는 규칙. y = 3x + 10.","organ"),
("Fixed charge","기본요금","An amount you pay once, however long you hire something.","날 수와 상관없이 한 번 내는 돈. 식에서 더하는 수가 된다. $10 → y = 3x + 10.","organ"),
("Per day","하루마다","For each day.","하루에 붙는 요금. 식에서 x 앞의 수가 된다. $3 per day → 3x.","organ"),
("Total cost","총액(전체 비용)","The whole amount you pay.","기본요금 + 하루 요금 × 날 수. 문제에서 y 또는 t 로 쓴다.","organ"),
("Linear function","일차 함수","A function whose graph is a straight line.","x 에 제곱이 없는 함수. y = 2x + 3, 2x + 3y = 12.","organ"),
("Straight line","직선","A line that does not bend.","일차 함수의 그래프. 점을 찍고 자로 곧게 긋는다.","organ"),
("Table of values","값의 표","A table that shows x values and their y values.","x 줄과 y 줄로 된 표. 'Copy and complete' = 빈칸을 채운다.","organ"),
("Plot","(점을) 찍다","To mark points on a graph using their coordinates.","표의 (x, y) 를 좌표평면에 점으로 찍는 것. Plotting graphs.","organ"),
("Coordinates","좌표","A pair of numbers (x, y) that gives the position of a point.","(x, y) 순서로 쓴다. 가로 x 먼저, 세로 y 나중. (6, 0).","organ"),
# ── process : 축·절편·곡선 (10.2) ──
("x-axis","x축","The horizontal axis of a graph.","가로축. x-axis 위의 점은 언제나 y = 0.","process"),
("y-axis","y축","The vertical axis of a graph.","세로축. y-axis 위의 점은 언제나 x = 0.","process"),
("x-intercept","x절편","The point where a graph crosses the x-axis.","그래프가 x축을 지나는 점. y = 0 을 넣어 구한다. 2x + 3y = 12 → (6, 0).","process"),
("y-intercept","y절편","The point where a graph crosses the y-axis.","그래프가 y축을 지나는 점. x = 0 을 넣어 구한다. y = 2x + 3 → (0, 3).","process"),
("Cross","지나다(가로지르다)","To go across a line or an axis.","'Where does this graph cross the x-axis?' = x절편이 어디인가.","process"),
("Lie on the line","직선 위에 있다","A point lies on a line if its coordinates fit the equation.","점의 x 를 식에 넣어 나온 y 가 점의 y 와 같으면 Yes. (2, 5) on y = 3x − 1 → Yes.","process"),
("Smooth curve","부드러운 곡선","A curved line drawn without corners through all the points.","점이 한 직선 위에 없을 때 자 없이 둥글게 잇는 선. y = x² − 3.","process"),
("Root","근","A value of x where a graph crosses the x-axis.","이차 그래프의 x절편. x² − 3 = 0 → x = ±√3 ≈ ±1.73.","process"),
("Symmetrical","대칭인","The same on both sides of a line.","y = x² − 3 은 y축 양쪽이 똑같다. 표의 y 도 6, 1, −2, −3, −2, 1, 6.","process"),
# ── blood : 기울기와 절편 (10.3) ──
("Gradient","기울기","How much y changes when x increases by 1.","y = mx + c 의 m. 오른쪽 위로 올라가면 +, 내려가면 −.","blood"),
("y = mx + c","직선의 식 y = mx + c","The general form of the equation of a straight line.","m = gradient, c = y-intercept. 직선의 식은 언제나 이 꼴로 쓸 수 있다.","blood"),
("General form","일반형(일반적인 꼴)","The usual way to write a type of equation.","직선은 y = mx + c 꼴. 'special general form'.","blood"),
("Subject","주어(혼자 남는 글자)","The letter on its own on one side of a formula.","'y as the subject' = 식을 y = … 꼴로 바꾼다. 2x + 3y = 12 → y = −⅔x + 4.","blood"),
("Negative gradient","음의 기울기","The gradient of a line that goes down from left to right.","오른쪽 아래로 내려가는 직선. y = 4 − 6x → gradient −6.","blood"),
("y-change","y 변화량","How much y goes up or down between two points.","y₂ − y₁. 내려가면 음수.","blood"),
("x-increase","x 증가량","How much x goes up between two points.","x₂ − x₁. gradient = y-change ÷ x-increase.","blood"),
("Lowest terms","기약분수(가장 간단한 꼴)","A fraction that cannot be simplified any more.","분자·분모를 더 나눌 수 없을 때까지 줄인 분수. 6/15 → 2/5.","blood"),
("Observation","관찰(눈으로 읽기)","Finding something by looking carefully.","'finding c through observation' = 직선이 y축과 만나는 눈금을 그래프에서 읽는다.","blood"),
("Straight line equation","직선의 식","The equation that every point on a straight line fits.","'Find the equation of each line' → c 와 m 을 구해 y = mx + c 로 쓴다.","blood"),
# ── gas : 그래프 읽고 해석하기 (10.4) ──
("Interpreting graphs","그래프 해석하기","Working out what a graph tells you about a real situation.","실생활 그래프에서 기울기·절편이 무엇을 뜻하는지 읽는 것.","gas"),
("Rate of cooling","식는 빠르기","How fast the temperature goes down.","실생활 그래프의 gradient 가 rate(변화율). 1분에 4 °C 씩 식는다 → 4 °C/minute. 직선이면 rate 가 constant(일정).","gas"),
("Distance–time graph","거리–시간 그래프","A graph of distance travelled against time taken.","가로 time, 세로 distance. gradient = speed.","gas"),
("Speed","속력","The distance travelled in each unit of time.","거리 ÷ 시간. 250 m ÷ 20 s = 12.5 m/s.","gas"),
("In terms of","~로 나타낸(~의 식으로)","Using that letter in the formula.","'d in terms of t' = d = (t 가 든 식). d = 12.5t.","gas"),
("Congruent","합동인","Exactly the same shape and size.","돌리거나(rotate) 뒤집어도(reflect) 꼭 겹치는 모양. Starter 22 의 짝 찾기.","gas"),
]
CATS = [("organ","📈 함수와 그래프 Functions"),("process","✖️ 축과 절편 Intercepts"),
        ("blood","📐 기울기 Gradient"),("gas","🚗 그래프 해석 Interpreting")]
