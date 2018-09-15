class IrisData:


    def urls():
        url='https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
        return url


    def columns():
        column_name=['sepal length','sepal width','petal length','petal width','class']
        return column_name




    def description():
        def title():
            titles ='Title: Iris Plants Database'
            return titles
        def source():
            sources='''Sources:
     \t(a) Creator: R.A. Fisher
     \t(b) Donor: Michael Marshall (MARSHALL%PLU@io.arc.nasa.gov)
     \t(c) Date: July, 1988'''
            return sources
        def info():
            descri='''Relevant Information:
     \t--- This is perhaps the best known database to be found in the pattern recognition literature. Fisher's paper is a classic in the field and is referenced frequently to this day.  (See Duda & Hart, for
 example.
     \t--- The data set contains 3 classes of 50 instances each, where each class refers to a type of iris plant. One class is linearly separable from the other 2; the latter are NOT linearly
 separable from each other.
     \t--- Predicted attribute: class of iris plant.
     \t--- This is an exceedingly simple domain.
     \t--- This data differs from the data presented in Fishers article (identified by Steve Chadwick,  spchadwick@espeedaz.net )
	 \tThe 35th sample should be: 4.9,3.1,1.5,0.2,"Iris-setosa"
	 \twhere the error is in the fourth feature.
	 \tThe 38th sample: 4.9,3.6,1.4,0.1,"Iris-setosa"
	 \twhere the errors are in the second and third features. '''
            return descri
        def attribute():
            attri="""Attribute Information:
   1. sepal length in cm
   2. sepal width in cm
   3. petal length in cm
   4. petal width in cm
   5. class: 
      -- Iris Setosa
      -- Iris Versicolour
      -- Iris Virginica"""
            return attri
