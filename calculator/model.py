import tensorflow as tf

class CalculatorModel:
    def __init__(self):
        pass

    def create_add_model(self):
        w1 = tf.placeholder(tf.float32, name='w1') # tf의 변수 하나 w1 -> 입력되는 숫자가 매칭되도록 placeholder
        w2 = tf.placeholder(tf.float32, name='w2')
        feed_dict = {'w1':8.0, 'w2':2.0}
        # feed_dict 는 input과 유사함. 초기화작업. 값이 어떤 값이 나오는지 체크하기 위한 더미값이므로 어느 숫자가 들어가도 상관없음.
        r = tf.add(w1, w2, name='op_add') # 합산하는 모델을 op_add로 설정
        sess = tf.Session()
        _ = tf.Variable(initial_value='fake_variable') # _ 로 설정한 것은 임시변수(fake_variable)
        sess.run(tf.global_variables_initializer()) #초기화작업
        saver = tf.train.Saver() # 학습결과를 저장. 데이터에 대한 누적이 중요하므로 저장해서 훈련반복하면서 성능 높아지도록함
        result = sess.run(r, {w1: feed_dict['w1'], w2: feed_dict['w2']})
        print('TF 덧셈결과: {}'.format(result))
        saver.save(sess, './saved_add_model/model', global_step=1000)
        # 덧셈이었다면 더하기 모델에 "모델"으로 저장. 1000번 반복


    def create_sub_model(self):
        w1 = tf.placeholder(tf.float32, name='w1')  # tf의 변수 하나 w1 -> 입력되는 숫자가 매칭되도록 placeholder
        w2 = tf.placeholder(tf.float32, name='w2')
        feed_dict = {'w1': 8.0, 'w2': 2.0}
        # feed_dict 는 input과 유사함. 초기화작업. 값이 어떤 값이 나오는지 체크하기 위한 더미값이므로 어느 숫자가 들어가도 상관없음.
        r = tf.subtract(w1, w2, name='op_sub')  # 합산하는 모델을 op_add로 설정
        sess = tf.Session()
        _ = tf.Variable(initial_value='fake_variable')  # _ 로 설정한 것은 임시변수(fake_variable)
        sess.run(tf.global_variables_initializer())  # 초기화작업
        saver = tf.train.Saver()  # 학습결과를 저장. 데이터에 대한 누적이 중요하므로 저장해서 훈련반복하면서 성능 높아지도록함
        result = sess.run(r, {w1: feed_dict['w1'], w2: feed_dict['w2']})
        print('TF 뺄셈결과: {}'.format(result))
        saver.save(sess, './saved_sub_model/model', global_step=1000)


    def create_mul_model(self):
        w1 = tf.placeholder(tf.float32, name='w1')  # tf의 변수 하나 w1 -> 입력되는 숫자가 매칭되도록 placeholder
        w2 = tf.placeholder(tf.float32, name='w2')
        feed_dict = {'w1': 8.0, 'w2': 2.0}
        # feed_dict 는 input과 유사함. 초기화작업. 값이 어떤 값이 나오는지 체크하기 위한 더미값이므로 어느 숫자가 들어가도 상관없음.
        r = tf.multiply(w1, w2, name='op_mul')  # 합산하는 모델을 op_add로 설정
        sess = tf.Session()
        _ = tf.Variable(initial_value='fake_variable')  # _ 로 설정한 것은 임시변수(fake_variable)
        sess.run(tf.global_variables_initializer())  # 초기화작업
        saver = tf.train.Saver()  # 학습결과를 저장. 데이터에 대한 누적이 중요하므로 저장해서 훈련반복하면서 성능 높아지도록함
        result = sess.run(r, {w1: feed_dict['w1'], w2: feed_dict['w2']})
        print('TF 곱셈결과: {}'.format(result))
        saver.save(sess, './saved_mul_model/model', global_step=1000)


    def create_div_model(self):
        w1 = tf.placeholder(tf.float32, name='w1')  # tf의 변수 하나 w1 -> 입력되는 숫자가 매칭되도록 placeholder
        w2 = tf.placeholder(tf.float32, name='w2')
        feed_dict = {'w1': 8.0, 'w2': 2.0}
        # feed_dict 는 input과 유사함. 초기화작업. 값이 어떤 값이 나오는지 체크하기 위한 더미값이므로 어느 숫자가 들어가도 상관없음.
        r = tf.divide(w1, w2, name='op_div')  # 합산하는 모델을 op_add로 설정
        sess = tf.Session()
        _ = tf.Variable(initial_value='fake_variable')  # _ 로 설정한 것은 임시변수(fake_variable)
        sess.run(tf.global_variables_initializer())  # 초기화작업
        saver = tf.train.Saver()  # 학습결과를 저장. 데이터에 대한 누적이 중요하므로 저장해서 훈련반복하면서 성능 높아지도록함
        result = sess.run(r, {w1: feed_dict['w1'], w2: feed_dict['w2']})
        print('TF 나눗셈결과: {}'.format(result))
        saver.save(sess, './saved_div_model/model', global_step=1000)


