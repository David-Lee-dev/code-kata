# 개인정보 수집 유효기간
# https://school.programmers.co.kr/learn/courses/30/lessons/150370#

def calc_days(date):
    year, month, day = map(int, date.split("."))
    
    return (year * 12 * 28) + (month * 28) + day

def solution(today, terms, privacies):
    term_table = {term[0] : int(term[2:]) * 28 for term in terms}
    answer = []
    
    today_days = calc_days(today)
    
    for idx, privacy in enumerate(privacies):
        date, term = privacy.split(" ")
        expired_days = calc_days(date) + term_table[term]
        
        if today_days >= expired_days:
            answer.append(idx + 1)
    
    return answer


