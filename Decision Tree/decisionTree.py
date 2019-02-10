class node:
    """ This class handles the nodes in a decision tree
    """

    def __init__(self, attr):
        self.attribute = attr
        self.childs = []  
        self.leaf = False
        self.label = '' 

    def add_childs(self, child):
        self.childs.append(child)

    def is_leaf(self):
        self.leaf = True

    def set_label(self, lab):
        self.label = lab


class decisionTree:
    """ this class makes and uses the decision tree
    """

    def __init__(self, attributes, dep, bina):
        """ this takes int # of attributes, int max depth of the tree (<zero if no limit),
            boolean value if tree labels are binary
        """ 
        self.attr = attributes
        self.depth = dep
        self.type = ''
        self.binary = bina
        self.training = []
        self.start = node('temp')
        self.attributes = dict()

    def add_training(self, train):
        """ takes a training string of the format attribute1, atr2, . . .to finally the label last all seperated by commas
        """
        self.training.append(train)

    def add_attribute(self, input):
        """ add attributes in the format
            attribute, val1, val2, . . . until all values are in
        """
        atr = [x.strip() for x in input.split(',')]

        #add all attrubutes and values to the dictionary
        self.attributes[atr[0]] = atr[1]
        for current in range(2, len(atr)):
            self.attributes[atr[0]].append(atr[current])

    def run(self, input):
        """ runs the input on the built tree
            returns the value it predicts 
        """ 
        test = [x.strip() for x in input.split(',')]
        current = self.start

        while len(test) > 0:
            rem = ''
            ll = False
            for one in test:
                if one in self.attributes:
                    #correct attribute chosen at level
                    current = self.attributes[one]
                    rem = one
                    ll = current.leaf
                    break
            
            test.remove(rem)
            #leaf node reached
            if ll == True:
                return current.label

        return current.label

    def make_tree(self, ty):
        """make the tree with the type of 'ID3', 'gini', or 'ME'
        """
        #compute information gain for each attribute

    


    def __
