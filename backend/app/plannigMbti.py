class plan():
    def __init__(self, plan_id, period) -> None:
        self.plan_id = plan_id
        self.period = period

class date():
    period = 0
    # 필요한 인자
    """
    start {
        'year':년도:int
        'month':월:int
        'day':일:int
    }

    end {
        'year':년도 # int
        'month':월 # int
        'day':일 # int
    }
    """
    def __init__(self, start:dict, end:dict) -> None:
        for year in range(start['year'], end['year']+1):
            # 윤년 계산 제작
            self.period += 365    
        self.year = end['year'] - start['year']
        self.month = end['month'] - start['month']
        self.day = end['day'] - start['day']
        
        




def matching_plan_style(plan_id:str, date:dict, unit:dict, mbti:str) -> None:
    # 다른 사람과 함께 공부
    bool_study_with = True
    # 이미지를 그리며 공부
    bool_study_image = True
    # 논리적인 질문을 반복하며 공부
    bool_study_why = True
    # 짧은 시간 공부
    bool_study_short = True
    # 기간 구하기
    period = cal_period()


    if mbti[0] == "I":
        bool_study_with = False

    if mbti[1] == "S":
        bool_study_image = False

    if mbti[2] == "F":
        bool_study_why = False

    if mbti[3] == "J":
        bool_study_short = False

