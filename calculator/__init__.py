from calculator.model import CalculatorModel
import os

if __name__ == '__main__':
    calc = CalculatorModel()

   # calc.create_add_model()  -> add_model만 설정했을 경우

    if not os.path. exists('saved_add_model/checkpoint'): # 체크포인트를 기준으로 모델이 존재하는지 아닌지 판단
        calc.create_add_model() # 모델이 없으면 만든다는 구문
    if not os.path. exists('saved_sub_model/checkpoint'):
        calc.create_sub_model()
    if not os.path.exists('saved_mul_model/checkpoint'):
        calc.create_mul_model()
    if not os.path.exists('saved_div_model/checkpoint'):
        calc.create_div_model()

"""    
    if not os.path. exists('saved_sub_model/checkpoint'):
        calc.create_sub_model()
    calc.create_mul_model()
    
    을 만든 후
    다음 조건 설정
    if not os.path. exists('saved_sub_model/checkpoint'):
        calc.create_sub_model()
    if not os.path.exists('saved_mul_model/checkpoint'):
        calc.create_mul_model()
    calc.create_div_model()

    하면서 순차적으로 4개 연산 모델을 생성    
"""