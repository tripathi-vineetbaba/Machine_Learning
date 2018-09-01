import tensorflow as tf

class Cost:

    def RMSE(prediction,actual,number_of_sample):
        return tf.reduce_sum(tf.pow(tf.subtract(prediction,actual),2),name="RMSE_Cost")/(2*number_of_sample)

    def MAE(prediction,actual,number_of_sample):
        return tf.reduce_sum(tf.abs(prediction,actual),name="MAE_Cost")/(number_of_sample)

    def MAPE(prediction,actual,number_of_sample):
        return((tf.reduce_sum(tf.divide(tf.abs(actual-prediction)/tf.abs(actual)),name="MAPE_cost")/(number_of_sample))*100)
