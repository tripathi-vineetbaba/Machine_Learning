import tensorflow as tf

class Regression:

    def LinearRegression(Data,Weight,Bias):
        variable=tf.add(tf.multiply(Weight,Data),Bias)
        return variable

    def computeRegression(self,sess,epochs,X_axis_Data,Y_axis_Data,optimizer,display_steps,X,Y,cost,W,B,model,global_steps=100):

        saver=tf.train.Saver()
        storage=[]
        for epoch in range(epochs):
            for (x,y) in zip(X_axis_Data,Y_axis_Data):
                sess.run(optimizer,feed_dict={X:x,Y:y})
                if (epoch+1)%display_steps==0:
                    c=sess.run(cost,feed_dict={X:X_axis_Data,Y:Y_axis_Data})
                    w=sess.run(W)
                    b=sess.run(B)
                    storage.append([epoch,c,w,b])
        save_path=saver.save(sess,model,global_step=global_steps)
        return storage,save_path

    