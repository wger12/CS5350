import numpy
import random

class svm:

    def __init__(self):
        self.training = []
        self.weight = self.weight = numpy.zeros (1)
        self.ep = 0
        self.attr = 0
        self.rate = 0
        self.c = 0

    def add_training(self, training):
        """ add training with attributes separated by commas and label last
            assuming the attributes are continuous values
        """
        add = [x.strip() for x in training.split(',')]
        self.attr = len(add)
        if(add[self.attr-1] == '0'):
            add[self.attr-1] = '-1'
        self.training.append(add)

    def make_primal(self, epochs, rate, hyp, d):
        """ make the SVM with the primal form and stocastic sub-gradient decent
        """
        self.ep = epochs
        self.rate = rate
        self.c = hyp
        self.weight = numpy.zeros (self.attr)
        
        for _ in range(self.ep):
            #shullfe the training
            random.shuffle(self.training)

            t = 0
            for train in self.training:
                #mke the x
                arx = numpy.zeros(self.attr)
                for n in range(0, self.attr-1):
                    arx[n] = float(train[n])
                
                #make the new rate
                rate = self.rate/(1+(self.rate/d)*t)

                #see if <= 1
                y = int(train[len(train)-1])
                guess = self.weight.T @ arx
                guess = guess * y
                
                if guess <= 1:
                    rr = 1-self.rate
                    add = arx * rate * self.c * len(self.training) * y
                    self.weight = (rr * self.weight) + add
                
                else:
                    rr = 1-self.rate
                    self.weight = self.weight * rr


    def run(self, test):
        """ runs the test on the SVM 
            retuns 1 or -1 for classification
            expectig the tests to have the correct answer as the last attibute like the training examples
        """
        #multiply the test with the wweight and check the sign
        arx = numpy.zeros(self.attr)
        add = [x.strip() for x in test.split(',')]
        for x in range(0, self.attr-1):
            arx[x] = float(add[x])

        guess = self.weight.T @ arx

        if guess < 0:
            return -1
        else:
            return 1


