import tensorflow as tf
import os,sys
sys.path.insert(0,'../../../../Machine-Learning/OOPS_ML/')
from functions.OS.OS import OS
component='irisData'
model1=''
model2=''
model_dir=''
if OS.checkDir(OS,component) :
    model,model_dir=OS.get_meta_path(OS,component)
    model2=model_dir+'irisDataSep-100.meta'
    model1=model_dir+'irisDataPet-100.meta'


saver1=tf.train.import_meta_graph(model1)

saver2=tf.train.import_meta_graph(model2)

with tf.Session() as sess:
    saver1.restore(sess,tf.train.latest_checkpoint(model_dir))
    print("Petal Details")
    print("Weight : ",sess.run('Weight:0'))
    print("Bias : ",sess.run('Bias:0'))
    print()
#with tf.Session() as sess1:
    saver2.restore(sess,tf.train.latest_checkpoint(model_dir))
    print("Sepal Details")
    print("Weight : ",sess.run('Weight:0'))
    print("Bias : ",sess.run('Bias:0'))
