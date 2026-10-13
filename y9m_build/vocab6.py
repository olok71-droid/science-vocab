# -*- coding: utf-8 -*-
# 9학년 수학 6단원 Statistical Investigations
# 출처 = y9m_ch6_problems.html (선생님 OneNote CHAPTER 6 · 6.1 Data collection and sampling, 6.2 Bias)
VOCAB = [
# ── organ : 자료의 종류 (6.1) ──
("Data","자료(데이터)","Facts or numbers collected to answer a question.","질문에 답하려고 모은 사실이나 수.","organ"),
("Categorical data","범주형 자료","Data in groups or names, not numbers.","숫자가 아니라 이름·종류로 나뉘는 자료. 좋아하는 색, short/average/tall.","organ"),
("Qualitative data","질적 자료","Another name for categorical data.","범주형 자료의 다른 이름. 성질(quality)을 말로 적는다.","organ"),
("Numerical data","수치 자료","Data given as numbers.","숫자로 세거나 잰 자료.","organ"),
("Quantitative data","양적 자료","Another name for numerical data.","수치 자료의 다른 이름. 양(quantity)을 수로 적는다.","organ"),
("Discrete data","이산 자료","Numerical data that can only take certain values; you count it.","세는(count) 자료. 정해진 값만 나온다. 형제 수, 신발 치수.","organ"),
("Continuous data","연속 자료","Numerical data that can take any value in a range; you measure it.","재는(measure) 자료. 어떤 값이든 나온다. 키 162.4 cm, 시간, 무게.","organ"),
("Shoe size","신발 치수","The number of a shoe, such as 38 or 38½.","38, 38½ 처럼 정해진 값만 있어 이산 자료다.","organ"),
("Hand span","손 뼘","The distance from the tip of the thumb to the tip of the little finger.","손을 쫙 폈을 때 엄지 끝에서 새끼손가락 끝까지 길이.","organ"),
# ── process : 조사 계획 (6.1) ──
("Statistical investigation","통계 조사","A plan to answer a question by collecting and analysing data.","자료를 모아 질문에 답하는 조사. 6단원 제목이다.","process"),
("Statistical question","통계적 질문","A question that can be answered by collecting data.","자료를 모아야 답할 수 있는 질문.","process"),
("Prediction","예측","What you think the result will be, which you then test.","결과가 어떨지 미리 말한 것. 자료로 맞는지 확인한다.","process"),
("Collect data","자료를 모으다","To gather the information for an investigation.","조사에 필요한 정보를 모으는 것. 모으기 쉬운지·예의에 맞는지도 따진다.","process"),
("Trial","시행(시험 조사)","A small test run to check the method before the real survey.","본조사 전에 방법이 괜찮은지 작게 해 보는 것.","process"),
("Accurate","정확한","Close to the true value.","참값에 가까운 것. 재는 자료가 보통 더 정확하다.","process"),
("Embarrassing","민망한","Making people feel uncomfortable.","사람을 불편하고 쑥스럽게 만드는 것. 자료를 고를 때 단점이 된다.","process"),
("Assumption","가정","Something you believe is true without checking.","확인하지 않고 맞다고 믿는 것. 먼저 의심해 본다.","process"),
("Conclusion","결론","What you decide after looking at the results.","결과를 보고 내린 판단. 성급하게 내리면 틀린다.","process"),
("Give a reason","이유를 쓰시오","An instruction asking you to explain why.","까닭을 영어 문장으로 쓰라는 지시문. 답만 쓰면 점수가 깎인다.","process"),
# ── blood : 편향 (6.2) ──
("Whole population","모집단","The whole group you want to find out about.","알고 싶은 사람·물건 전체.","blood"),
("Sample","표본","The part of the population you actually survey.","모집단 중에서 실제로 조사한 일부.","blood"),
("Survey","설문 조사","Asking people questions to collect data.","사람들에게 물어서 자료를 모으는 것.","blood"),
("Bias","편향","Something that pushes the results one way.","결과를 한쪽으로 치우치게 만드는 것.","blood"),
("Biased sample","편향된 표본","A sample that does not fairly represent the population.","모집단을 고르게 대표하지 못하는 표본.","blood"),
("Representative","대표성이 있는","Having the same mix as the whole population.","표본이 모집단과 비슷한 비율로 섞여 있는 것.","blood"),
("Reliability","신뢰도(신뢰성)","How much you can trust the results.","결과를 믿을 수 있는 정도. 모은 자료의 질에 달려 있다.","blood"),
("Valid","타당한","Correct and fair for the question asked.","질문에 맞고 공정한 것. 편향된 표본의 결과는 타당하지 않을 수 있다.","blood"),
("Misleading","오해를 부르는","Giving a wrong idea.","틀린 인상을 주는 정보나 그래프.","blood"),
("Leading question","유도 질문","A question that pushes people towards one answer.","\"You agree that …, don't you?\" 처럼 한쪽 답으로 몰아가는 질문.","blood"),
("Ambiguous","애매한","Able to be understood in more than one way.","두 가지 이상으로 읽힐 수 있는 것. 질문은 누구나 같은 뜻으로 읽게 쓴다.","blood"),
("Voluntary response","자발적 응답","Only people who choose to answer are counted.","관심 있는 사람만 답해서 생기는 편향.","blood"),
("Underrepresented","너무 적게 대표된","Having too few in the sample compared with the population.","모집단에 비해 표본에 너무 적게 들어간 것.","blood"),
("Overrepresented","너무 많이 대표된","Having too many in the sample compared with the population.","모집단에 비해 표본에 너무 많이 들어간 것.","blood"),
("Random sample","무작위 표본","A sample where every member has the same chance of being chosen.","모두가 뽑힐 기회가 똑같은 표본. 편향을 줄인다.","blood"),
# ── gas : 비율대로 뽑기 (Worked example 6.3) ──
("Stratified sampling","층화 표본 추출","Choosing a sample so each group is in the same proportion as in the population.","무리마다 모집단 비율대로 뽑는 방법.","gas"),
("Proportion","비율(비례)","A part compared with the whole.","전체에 대한 부분의 크기. 187 ÷ 549 처럼 구한다.","gas"),
("Sample size","표본 크기","The number of people or items in the sample.","표본에 든 수. 너무 작으면 편향된다.","gas"),
("Nearest whole number","가장 가까운 정수","Rounding to a whole number.","소수를 반올림해 정수로 만드는 것. 13.62 → 14.","gas"),
("Other factors","다른 요인","Other things that can affect the result.","결과에 영향을 줄 수 있는 다른 것. 나이·직업·월급.","gas"),
]
CATS = [("organ","🔢 자료의 종류 Types of data"),("process","📝 조사 계획 Planning"),
        ("blood","⚠️ 편향 Bias"),("gas","⚖️ 비율대로 뽑기 Stratified sampling")]
