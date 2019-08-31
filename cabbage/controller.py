from cabbage.model import CabbageModel
import tensorflow as tf
import numpy as np

class CabbageController:
    def __init__(self, avg_temp, min_temp, max_temp, rain_fall):
        self._avg_temp = avg_temp
        self._min_temp = min_temp
        self._max_temp = max_temp
        self._rain_fall = rain_fall

    def service(self):
        X = tf.placeholder(tf.float32, shape=[None, 4])
        W = tf.Variable(tf.random_normal([4, 1]), name='weight')
        b = tf.Variable(tf.random_normal([1]), name='bias')
        saver = tf.train.Saver()
        with tf.Session() as sess: #세션공간 생성. 세션공간내에서 실행되도록
            sess.run(tf.global_variables_initializer())
            saver.restore(sess, 'cabbage/saved_model/saved.ckpt') #세션에 경로할당. 저장 -> 상대경로. 호출 -> 절대경로(cabbage부터 시작)
            data = [[self._avg_temp, self._min_temp, self._max_temp, self._rain_fall],] #[[]]매트릭스 구조. 맨첫줄만 지정.
            arr = np.array(data, dtype = np.float32)
            dict = sess.run(tf.matmul(X, W) + b, {X: arr[0:4]})
#            print('>>>> '+dict[0]) # 여기까지 코딩이 잘 되었는지 확인 -> str값으로 인식해서 충돌? 실행하면 에러남
        return int(dict[0])


