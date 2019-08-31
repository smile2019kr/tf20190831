import tensorflow as tf
import pandas as pd
import numpy as np

class CabbageModel:
    def __init__(self):
        pass

    def create_model(self):
        model = tf.global_variables_initializer()
        data = pd.read_csv('./data/price_data.csv', sep=',') #pandas에서 제공하는 파일 불러들이기
        xy = np.array(data, dtype=np.float32) # tf는 float32가 기본형
        x_data = xy[:,1:-1] #feature
        y_data = xy[:,[-1]] #가격. 끝에서 첫번째열을 뽑아내는 구문
        X = tf.placeholder(tf.float32, shape=[None, 4]) #입력받은 4개의 feature로 가격(y)을 예측
        Y = tf.placeholder(tf.float32, shape=[None, 1]) #대문자 -> 확률변수. 소문자 -> variable
        W = tf.Variable(tf.random_normal([4, 1]), name='weight')
        b = tf.Variable(tf.random_normal([1]), name='bias')
        hypothesis = tf.matmul(X, W) + b
        cost = tf.reduce_mean(tf.square(hypothesis - Y))
        optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.000005)
        train = optimizer.minimize(cost)
        sess = tf.Session()
        sess.run(tf.global_variables_initializer())
        # 학습
        for step in range(100000):
            cost_, hypo_, _ = sess.run([cost, hypothesis, train],
                                       feed_dict={X: x_data, Y: y_data}) # cost_ , hypo_ , _임시변수
            if step % 500 == 0:
                print('# %d 손실비용 : %d'%(step, cost_))
                print("- 배추가격 : %d" % (hypo_[0])) #예측값

        # 저장 - 학습이 끝나면 모델 저장
        saver = tf.train.Saver()
        saver.save(sess, 'saved_model/saved.ckpt')
        print('저장완료') # 학습 및 저장이 완료되었음을 확인하기 위함. print하지않으면 계속 대기해야함

