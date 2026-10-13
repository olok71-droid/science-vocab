# -*- coding: utf-8 -*-
NOTES = [
("🔢", "6.1 Data collection and sampling", "자료 모으기와 표본 뽑기", [
 ("자료는 두 갈래, 수치 자료는 또 두 갈래",
  "① 범주형 자료 <b>categorical data</b> (= 질적 자료 <b>qualitative data</b>)<br>"
  "숫자가 아니라 이름·종류로 나뉜다. 좋아하는 색, 혈액형, short / average / tall<br><br>"
  "② 수치 자료 <b>numerical data</b> (= 양적 자료 <b>quantitative data</b>)<br>"
  "숫자로 세거나 잰다. 이것이 다시 둘로 나뉜다.<br>"
  "• 이산 자료 <b>discrete data</b> — <b>세는(count)</b> 값. 정해진 값만 나온다.<br>"
  "&nbsp;&nbsp;형제 수 2명, 신발 치수 shoe size 38·38½<br>"
  "• 연속 자료 <b>continuous data</b> — <b>재는(measure)</b> 값. 어떤 값이든 나온다.<br>"
  "&nbsp;&nbsp;키 162.4 cm, 시간, 무게<br><br>"
  "★ 구별법: <b>세면 discrete, 재면 continuous.</b>"),
 ("★ 함정 1 — 신발 치수는 숫자지만 연속이 아니다",
  "shoe size 는 38, 38½, 39 … 처럼 <b>정해진 값만</b> 있다. 38.27 짜리 신발은 없다.<br>"
  "→ 그래서 <b>discrete data</b> 다.<br><br>"
  "반대로 발 길이 foot length 를 자로 재면 24.3 cm, 24.35 cm … 어떤 값이든 나온다.<br>"
  "→ <b>continuous data</b> 다.<br><br>"
  "★ '숫자로 적혀 있다 = 연속'이 아니다. <b>값이 띄엄띄엄이냐, 아무 값이나 되느냐</b>로 가린다."),
 ("★ 함정 2 — 같은 키도 모으는 방법에 따라 종류가 바뀐다",
  "키 height 를 줄자 tape measure 로 재면 → <b>continuous data</b><br>"
  "키를 short / average / tall 세 칸으로 나눠 적으면 → <b>categorical data</b><br><br>"
  "선생님 문제: \"what type of data are height and shoe size?\"<br>"
  "답 → Height: continuous (재면) 또는 categorical (칸으로 나누면)<br>"
  "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Shoe size: <b>discrete numerical data</b><br><br>"
  "★ 자료의 종류는 '무엇을 모으느냐'가 아니라 <b>'어떻게 기록하느냐'</b>로 정해진다."),
 ("통계 조사 계획 순서 — 6단계",
  "통계 조사 <b>statistical investigation</b> 은 이 순서로 계획한다.<br><br>"
  "① 통계적 질문 <b>statistical question</b> 을 정한다<br>"
  "② 예측 <b>prediction</b> 을 세운다 (예: Taller boys have a larger shoe size)<br>"
  "③ 어떤 자료를 모을지 <b>collect data</b> 정한다<br>"
  "④ 표본 <b>sample</b> 을 고른다<br>"
  "⑤ 작은 시험 조사 <b>trial</b> 로 방법을 점검한다<br>"
  "⑥ 필요하면 계획을 고친다<br><br>"
  "★ 예측은 '맞다'고 정해 놓은 것이 아니다. 자료로 <b>test(시험)</b> 해서 맞는지 틀리는지 본다."),
 ("★ 함정 3 — '정확한 자료'가 늘 정답은 아니다",
  "Worked example 6.1: 발이 작은 사람은 손도 작은가?<br><br>"
  "발 길이를 재면 <b>더 정확 more accurate</b> 하다. 그런데 남의 발을 재는 것은<br>"
  "<b>민망하다 embarrassing</b> → 그래서 <b>shoe size</b> 가 더 알맞다. 모으기도 쉽다.<br><br>"
  "손은 hand span (엄지 끝 ~ 새끼손가락 끝) 또는 hand length (손목 ~ 가운뎃손가락 끝)를 잰다.<br>"
  "둘 다 <b>trial</b> 해 보고 더 나은 쪽을 고른다.<br><br>"
  "★ 자료를 고를 때 따질 것: 정확한가 accurate · <b>모으기 쉬운가 easy to collect</b> · "
  "<b>예의에 맞는가</b> (uncomfortable / embarrassing 하지 않은가)"),
 ("'give a reason' — 답을 쓰는 틀",
  "① 무엇을 잴지 what to measure<br>"
  "② 그 자료의 종류 continuous / discrete<br>"
  "③ 장점 accurate, easy to collect<br>"
  "④ 단점 embarrassing, takes time<br>"
  "⑤ 그래서 고른 것과 이유 reason<br><br>"
  "영어 문장 예:<br>"
  "<b>\"I would use shoe size because it is easy to collect and not embarrassing.\"</b><br><br>"
  "★ 'give a reason' 이 붙으면 답만 쓰면 점수가 깎인다. <b>because …</b> 로 이유를 꼭 붙인다."),
 ("Starter 퍼즐 — 성급한 결론을 의심하라",
  "\"A man pushes a car up to a hotel and realises he's bankrupt.\"<br>"
  "→ 진짜 자동차·호텔이 아니라 <b>모노폴리 Monopoly</b> 보드게임이다.<br><br>"
  "★ 통계와 이어지는 점: 자료 data 만 보고 성급하게 결론 <b>conclusion</b> 을 내리면 틀린다.<br>"
  "내가 가진 가정 <b>assumption</b> 을 먼저 의심하고, 다른 설명이 가능한지 생각한다."),
]),
("⚠️", "6.2 Bias", "치우침(편향)", [
 ("모집단과 표본 — 낱말부터 정확히",
  "• 모집단 <b>population</b>: 알고 싶은 사람·물건 <b>전체</b><br>"
  "• 표본 <b>sample</b>: 그중 <b>실제로 조사한 일부</b><br>"
  "• 대표성 있는 <b>representative</b>: 표본이 모집단과 비슷한 비율로 섞여 있음<br>"
  "• 편향 <b>bias</b>: 결과를 한쪽으로 치우치게 만드는 것<br>"
  "• 신뢰도 <b>reliability</b>: 결과를 믿을 수 있는 정도 — 자료의 질 quality 에 달려 있다<br>"
  "• 오해를 부르는 <b>misleading</b>: 틀린 인상을 주는 정보·그래프<br><br>"
  "★ 편향된 표본 <b>biased sample</b> = 모집단을 고르게 대표하지 <b>못하는</b> 표본.<br>"
  "이런 표본의 결과는 <b>valid(타당)</b> 하지 않을 수 있다."),
 ("편향이 생기는 5곳",
  "① <b>언제·어디서</b> 조사했나 — 특정 시간·장소엔 특정한 사람만 있다<br>"
  "② <b>누구에게</b> 물었나 — 친구만, 한 반만, 한 성별만<br>"
  "③ 표본이 <b>너무 작다</b> sample too small<br>"
  "④ 질문이 몰아간다 — 유도 질문 <b>leading question</b><br>"
  "&nbsp;&nbsp;\"You agree that …, don't you?\"<br>"
  "⑤ 답한 사람만 셌다 — 자발적 응답 <b>voluntary response</b>. 관심 있는 사람만 답한다.<br><br>"
  "편향을 줄이는 법:<br>"
  "여러 장소·여러 시간 <b>different places and at different times</b> 에 조사 · "
  "무작위 표본 <b>random sample</b> · 표본을 크게 · 모집단 비율대로 뽑기"),
 ("★ 함정 4 — 평일 오전 슈퍼마켓 (Worked example 6.2)",
  "새 도서관을 원하는지 <b>수요일·목요일 09:00~12:00 슈퍼마켓</b>에서 물었다.<br><br>"
  "a. 왜 편향인가?<br>"
  "→ 평일 낮에는 <b>일하는 사람 people who are at work during the day</b> 이 슈퍼마켓에 거의 없다.<br>"
  "→ 그 사람들이 표본에서 <b>underrepresented (너무 적게 대표됨)</b> 이다.<br>"
  "→ 또 지금 도서관을 쓰지 않아 의견이 없는 사람도 섞인다.<br><br>"
  "b. 어떻게 고치나?<br>"
  "→ <b>different places and at different times</b> 에 조사한다. 지금 있는 도서관에서도, 다른 시간·다른 요일에.<br><br>"
  "★ 푸는 순서: ① 그 장소에 누가 있고 누가 없나? ② 그 시간·요일에 누가 빠지나? "
  "③ 빠진 사람들이 <b>다른 의견</b>을 가질 수 있나?<br>"
  "답에 <b>underrepresented / overrepresented</b> 를 쓰면 좋다."),
 ("★ 함정 5 — 질문 낱말 하나가 결론을 바꾼다",
  "Starter 퍼즐: 방에 죽은 남자, 금·보석, 샹들리에, 창문으로 들어오는 <b>rays</b>.<br>"
  "→ rays 를 햇빛으로 읽으면 이상하지만, <b>가오리(물고기)</b>로 읽으면<br>"
  "바닷속에 가라앉은 배의 선실이고, 보물을 찾던 잠수부가 산소가 떨어져 죽은 것이다.<br><br>"
  "★ 설문 survey 질문도 같다. 낱말이 <b>애매 ambiguous</b> 하거나 한쪽으로 몰아가면 "
  "(<b>leading question</b>) 답이 치우친다.<br>"
  "질문은 <b>누구나 같은 뜻으로</b> 읽게 써야 한다."),
 ("비율대로 뽑기 — 층화 표본 (Worked example 6.3)",
  "남자 187명, 여자 362명인 회사에서 <b>대표성 있는 representative</b> 표본 40명을 뽑는다.<br><br>"
  "① 전체 = 187 + 362 = <b>549명</b><br>"
  "② 공식: 표본 속 그 무리 수 = <b>(그 무리 수 ÷ 전체 수) × 표본 크기 sample size</b><br>"
  "③ 남자 = 187 ÷ 549 × 40 = 13.62 → <b>14명</b><br>"
  "④ 여자 = 362 ÷ 549 × 40 = 26.38 → <b>26명</b><br>"
  "⑤ 확인: 14 + 26 = <b>40</b> ✓<br><br>"
  "답: <b>The sample should have 14 men and 26 women.</b><br><br>"
  "이렇게 무리마다 모집단 비율대로 뽑는 것을 층화 표본 <b>stratified sampling</b> "
  "(= proportional sampling) 이라 한다."),
 ("★ 함정 6 — 반올림한 뒤 합계를 꼭 맞춰라",
  "각각을 가장 가까운 정수 <b>nearest whole number</b> 로 반올림하면 "
  "합이 표본 크기와 <b>안 맞을 때</b>가 있다.<br><br>"
  "13.62 → 14, 26.38 → 26 → 합 40 ✓ (이번엔 맞음)<br><br>"
  "★ 안 맞으면 <b>소수 부분이 더 큰 쪽</b>을 올린다.<br>"
  "★ 34.1% 처럼 <b>백분율만</b> 구하고 멈추면 안 된다. 문제는 '<b>몇 명</b>'을 묻는다.<br>"
  "★ 사람 수는 <b>정수</b>로 답한다. 13.62명은 답이 아니다."),
 ("'다른 요인'을 3개 쓰라는 문제",
  "b. List three <b>other factors</b> to consider when choosing a representative sample.<br><br>"
  "성별 말고 결과에 영향을 줄 수 있는 것이면 된다.<br>"
  "• 나이 <b>age</b><br>"
  "• 직업 <b>job</b><br>"
  "• 월급 <b>salary</b><br>"
  "• 근무 부서 <b>department</b><br>"
  "• 근무 기간 <b>length of service</b><br>"
  "• 정규직 / 시간제 <b>full-time / part-time</b><br><br>"
  "★ 이미 문제에 나온 성별(men / women)을 다시 쓰면 점수가 안 된다. <b>새로운</b> 요인을 쓴다."),
]),
]
