import numpy

class perceptron:
    def __init__(self, attributes):
        """ takse the number of attributes
        """
        self.rate = 0
        self.ee = 0
        self.training = []
        self.attribs = attributes
        self.weight = numpy.zeros(attributes)
        self.vote = False


    def add_training(self, train):
        """ add training with attributes separated by commas and label last
            assuming the attributes are continuous values
        """
        add = [x.strip() for x in train.split(',')]
        add = list(map(float,add))
        self.training.append(add)
    

    def make_regular(self, learning_rate, epochs):
        """ makes the regular perceptron final weight in self.weight
        """
        self.rate = learning_rate
        self.ee = epochs
        self.weight = numpy.zeros(self.attribs)
        self.vote = False

        for round in range(self.ee):
            for victim in self.training:
                #remove the label fro the training
                victim = list.copy(victim)
                ans = victim.pop(len(victim)-1)
                ans = int(ans)
                
                ans = int(numpy.sign(ans))

                pred = numpy.inner(victim,self.weight)
                pred = int(numpy.sign(pred))

                #incorrect and update
                if(pred != ans):
                    neww = [i * self.rate for i in victim]
                    www = []
                    for x in range(self.attribs):
                        if(ans == 1):
                            www.append(neww[x] + self.weight[x])
                        else:
                            www.append(neww[x] - self.weight[x])

                    self.weight = www


    def make_vote(self, learning_rate, epochs):
        """ makes the voting perceptron final weight in self.weight
        """
        self.rate = learning_rate
        self.ee = epochs
        self.weight = numpy.zeros(self.attribs)
        self.vote = True
        vote = 1
        totals = []

        for round in range(self.ee):
            for victim in self.training:
                #remove the label fro the training
                victim = list.copy(victim)
                ans = victim.pop(len(victim)-1)
                ans = int(numpy.sign(ans))

                pred = numpy.inner(victim,self.weight)
                pred = int(numpy.sign(pred))

                #incorrect and update
                if(pred != ans):
                    neww = [i * self.rate for i in victim]
                    www = []
                    for x in range(self.attribs):
                        if(ans == 1):
                            www.append(neww[x] + self.weight[x])
                        else:
                            www.append(neww[x] - self.weight[x])

                    self.weight = www
                    #add to vote list
                    totals.append((vote,www))
                    vote = 1

                else:
                    vote += 1

    

    def make_average(self, learning_rate, epochs):
        """ makes the averaged perceptron final weight in self.weight
        """
        self.rate = learning_rate
        self.ee = epochs
        self.weight = [0] * self.attribs
        self.vote = False
        average = [0] * self.attribs

        for round in range(self.ee):
            for victim in self.training:
                #remove the label fro the training
                victim = list.copy(victim)
                ans = victim.pop(len(victim)-1)
                ans = int(numpy.sign(ans))

                pred = numpy.inner(victim,self.weight)
                pred = int(numpy.sign(pred))

                #incorrect and update
                if(pred != ans):
                    neww = [i * self.rate for i in victim]
                    www = []
                    #make new weight
                    for x in range(self.attribs):
                        if(ans == 1):
                            www.append(neww[x] + self.weight[x])
                        else:
                            www.append(neww[x] - self.weight[x])

                    self.weight = www
                    #add to the average
                    new_avg = list.copy(average)
                    for x in range(self.attribs):
                        new_avg[x] = average[x] + www[x]
                    average = new_avg

        self.weight = average


    def run(self, test):
        """ runs the test
            the test should have the attributes seperated by comma and optional label last
            returns 0 for negative and 1 for positive
        """
        #if the label is on the test
        if len(test) > self.attribs:
            tt = [x.strip() for x in test.split(',')]
            tt = list(map(float,tt))
            label = tt.pop(len(tt)-1)

            guess = numpy.inner(tt, self.weight)
            pred = int(numpy.sign(guess))

            if pred < 0:
                return 0
            else:
                return 1
    