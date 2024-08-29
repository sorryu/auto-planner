from datetime import datetime

class Plan():
    def __init__(self, plan_id:int, period:int, unit:dict, bool_study_short:bool) -> None:
        self.plan_id = plan_id
        self.period = period
        # 기간 동안 unit를 여러 개 작업.
        




class Date():
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
        s_date = datetime(start['year'], start['month'], start['day'])
        e_date = datetime(end['year'], end['month'], end['day'])

        self.period = (e_date - s_date).days+ + 1

    def return_period(self):
        return self.period
        




def matching_plan_style(plan_id:str, date:dict, unit:dict, mbti:str) -> None:
    # 스터디 방법 설명
    how_to_study = ""
    # 짧은 시간 공부
    bool_study_short = True
    
    if mbti[0] == "I":
        how_to_study += "조용한 곳에서 혼자 공부하는 것을 선호하는 스타일인 것 같아요. "
    else:
        how_to_study += "다른 사람과 같이 공부하거나, 다른 사람을 가르쳐주며 공부하는 것이 적합한 스타일로 보여요. "

    if mbti[1] == "S":
        how_to_study += "경험한 내용을 떠올리며 공부하는 방법이 적합한 스타일이에요. "
    else:
        how_to_study += "이미지로 만들어서 공부하는 것이 이해하는 데 큰 도움이 될 거에요. "

    if mbti[2] == "F":
        how_to_study += "이론을 수용하고, 그것을 바탕으로 공부를 해나가면 좋을 것 같아요. "
    else:
        how_to_study += "논리가 맞는지 계속 따져보며 공부하기에 적합하신 것 같아요. "

    if mbti[3] == "J":
        bool_study_short = False
        how_to_study += "실현 가능한 수준의 계획을 짜서 계획을 성공하는 것이 중요하실 것 같아요. "
    else:
        how_to_study += "짧은 시간 충동적으로 하는 공부에 더 흥미를 가지실 것 같네요. "


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

    # 객체 만들기
    plan_data = Plan(plan_id, period, unit, bool_study_short)

    return plan_data




