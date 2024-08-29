class Plan():
    def __init__(self, plan_id, period) -> None:


class Date():
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
            if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
                self.period += 366
            else:
                self.period += 365

        for month in range(1, end['month'] - start['month'] + 1):
            match month:
                case 1|3|5|7|8|10|12:
                    self.period += 31
                case 2:
                    if end['year'] % 400 == 0 or (end['year'] % 4 == 0 and end['year'] % 100 != 0):
                        self.period += 29
                    else:
                        self.period += 28
                case 4|6|9|11:
                    self.period += 30
        self.period += end['day'] - start['day']
        
    def return_period(self):
        return self.period
        




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
    """
    date = {
        'start_date': {
            'year': int
            'month': int
            'day': int
        }
        'end_date': {
            'year': int
            'month': int
            'day': int
        }
    }
    """
    start_date = date['start_date']
    end_date = date['end_date']
    dateclass = Date(start_date, end_date)
    period = dateclass.return_period()

    if mbti[0] == "I":
        bool_study_with = False

    if mbti[1] == "S":
        bool_study_image = False

    if mbti[2] == "F":
        bool_study_why = False

    if mbti[3] == "J":
        bool_study_short = False

    # 객체 만들기