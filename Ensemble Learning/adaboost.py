import decisionTree
import math

class adaboost:

    def __init__(self):
        self.classifiers = []
        self.classweights = []
        self.trainweights = []
        self.training = []
        self.attributes = []
        self.labels = ''
        self.z = 1

    def add_training(self, train):
        """ add a training example in order of attributes
        """
        self.training.append(train)

    def add_labels(self, labs):
        """ add labels to separated by ','
        """
        self.labels = labs

    def add_attribute(self, input):
        """ add attributes in the format
            attribute name, val1, val2, . . . until all values are in and attributes are added 
            MUST BE ADDED IN SAME ORDER AS TRAINING AND TESTS
        """
        self.attributes.append(input)

    def make_boost(self, t):
        #initialize training weights
        self.trainweights = []
        self.classweights = []
        self.classifiers = []
        for x in range(0, len(self.training)):
            self.trainweights.append(1/len(self.training))

        #main loop determined by t
        for iter in range(0, t):
            stump = decisionTree.decisionTree(len(self.attributes), True)
            for at in self.attributes:
                stump.add_attribute(at)
            for tr in self.training:
                stump.add_training(tr)
            stump.add_labels(self.labels) 

            stump.make_stump(self.trainweights)
            error = 0
            correct = []
            #compute error 
            for x in range(0, len(self.training)):
                ans = self.training[x].split(',')
                ans = ans[len(ans)-1].strip()
                atm = stump.run(self.training[x])
                if ans != atm:
                    error += self.trainweights[x]
                    correct.append(-1)
                else:
                    correct.append(1)
            #compute vote
            b = (1-error) / error
            a = 0.5*math.log(b)
            self.classweights.append(a)
            self.classifiers.append(stump)

            #update weights
            temp = []
            for x in range(0, len(self.training)):
                #self.trainweights[x] = (self.trainweights[x]/self.z) * math.exp(-a * correct[x])
                temp.append((self.trainweights[x]/self.z) * math.exp(-a * correct[x]))
            self.trainweights = temp

        #return the final hypothesis


    def run(self, input):
        """ runs the adaboost on the input and returns the result label as a string
        """
        totals = dict()
        for victim in range(0, len(self.classifiers)):
            weak = self.classifiers[victim]
            result = weak.run(input)

            right = input.split(',')
            right = right[len(right)-1].strip()

            if result in totals:
                totals[result] += self.trainweights[victim]
            else:
                totals[result] = self.trainweights[victim]

        #after totals are in find the one with the highest 
        most = list(totals.keys())[0]
        for one in totals.keys():
            if totals[one] > totals[most]:
                most = one
        
        return most