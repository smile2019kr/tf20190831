import tensorflow as tf
# pip install 후 tf 1.14버젼으로 설치되어있음을 확인

class CalculatorController:
    def __init__(self, num1, num2, opcode):
        self._num1 = num1
        self._num2 = num2
        self._opcode = opcode

    def calc(self):
        n1 = self._num1
        n2 = self._num2
        opcode = self._opcode

        print('app.py 에서 받은 n1 = {}, n2 = {}, opcode = {}'.format(n1, n2, opcode))

        tf.reset_default_graph()
        with tf.Session() as sess: #세션에 있는 모델을 호출하도록 세션영역 설정
            sess.run(tf.global_variables_initializer()) #세션영역에서 사용할수 있게 초기화
            saver = tf.train.import_meta_graph('calculator/saved_'+opcode+'_model/model-1000.meta')
            saver.restore(sess, tf.train.latest_checkpoint('calculator/saved_'+opcode+'_model')) #체크포인트를 가져와서 최신의 데이터 확인
            # 매 체크포인트마다 훈련한 기록들이 남아있지만 그중에서 제일 최신의 것을 호출

            graph = tf.get_default_graph() # 각각의 숫자를 바탕으로 좌표를 찍어서 그래프 표기
            w1 = graph.get_tensor_by_name('w1:0') # w1, w2, opcode각 변수값을 초기화
            w2 = graph.get_tensor_by_name('w2:0')
            feed_dict = {w1: float(n1), w2:float(n2)} # 외부에서 투입된 값이 w1, w2에 각각 들어감
            op_to_restore = graph.get_tensor_by_name('op_'+opcode+':0')
            result = sess.run(op_to_restore, feed_dict)
            print('텐서가 계산한 결과: {}'.format(result))
        return result #텐서는 세션 안에서만 작동하므로 with와 return result는 동급으로 설정해야 함


"""
    def input_number(self):
        self.a = int(input("number 1"))
        self.b = int(input("number 1"))

    def hook(self, menu):
        self.input_number()
        if menu == 1: result = self.plus()
        elif menu == 2: result = self.minus()
        elif menu == 3: result = self.multi()
        elif menu == 4: result = self.divid()

    def plus(self):
        pass

    def minus(self):
        pass

    def multi(self):
        pass

    def divid(self):
        pass

"""