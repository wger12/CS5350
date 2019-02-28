import decisionTree
import random

class bagging:

    def __init__(self):
        self.classifiers = []
        self.training = []
        self.attributes = []
        self.labels = ''

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

    def make_full(self, trees, amount):
        """ make the many decision tree classifiers 
            trees = how many trees to make
            amount = how large the subset of training will go to each tree
        """
        self.classifiers = []
        #main loop for trees
        for tree in range(0,trees):
            victim = decisionTree.decisionTree(len(self.attributes), True)

            for att in self.attributes:
                victim.add_attribute(att)

            victim.add_labels(self.labels)
            
            #pick random training amount times
            for trn in range(0,amount):
                rng = random.randint(0,len(self.training)-1)
                victim.add_training(self.training[rng])
            
            #make the individual tree and add it to the list
            victim.make_tree('ID3', -1)
            self.classifiers.append(victim)


    def make_forest(self, trees, amount):
        """ make the many decision tree classifiers 
            trees = how many trees to make
            amount = how large the subset of training will go to each tree
        """
        self.classifiers = []
        #main loop for trees
        for tree in range(0,trees):
            victim = decisionTree.decisionTree(len(self.attributes), True)

            for att in self.attributes:
                victim.add_attribute(att)
            victim.add_labels(self.add_labels)
            
            #pick random training amount times
            for trn in range(0,amount):
                rng = random.randint(0,len(self.training))
                victim.add_training(self.training[rng])
            
            #make the individual tree and add it to the list
            victim.make_random('ID3', -1)
            self.classifiers.append(victim)

    def run(self, input):
        totals = dict()
        for victim in range(0, len(self.classifiers)):
            weak = self.classifiers[victim]
            result = weak.run(input)

            if result in totals:
                totals[result] += 1
            else:
                totals[result] = 1

        #after totals are in find the one with the highest        
        most = list(totals.keys())[0]
        for one in totals.keys():
            if totals[one] > totals[most]:
                most = one
        
        return most
