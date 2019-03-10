import math
import random

class node:
    """ This class handles the nodes in a decision tree
    """

    def __init__(self, attr):
        self.attribute = attr
        self.childs = dict()  
        self.leaf = False
        self.label = '' 

    def is_leaf(self):
        self.leaf = True

    def set_label(self, lab):
        self.label = lab


class decisionTree:
    """ this class makes and uses the decision tree
    """

    def __init__(self, attributes, bina):
        """ this takes int # of attributes,
            boolean value if tree labels are discrete
        """ 
        self.attr = attributes
        self.depth = 0
        self.type = ''
        self.binary = bina
        self.training = []
        self.start = node('temp')
        self.attributes = dict()
        self.labels = []
        self.weights = []
        self.stump = False
        self.random = False

    def add_training(self, train):
        """ takes a training string of the format attribute1, atr2, . . .to finally the label last all seperated by commas
        """
        trainlist = [x.strip() for x in train.split(',')]
        self.training.append(trainlist)

    def add_attribute(self, input):
        """ add attributes in the format
            attribute name, val1, val2, . . . until all values are in and attributes are added 
            MUST BE ADDED IN SAME ORDER AS TRAINING AND TESTS
        """
        atr = [x.strip() for x in input.split(',')]

        #add all attrubutes and values to the dictionary
        self.attributes[atr[0]] = [atr[1]]
        for current in range(2, len(atr)):
            self.attributes[atr[0]].append(atr[current])

    def add_labels(self, lab):
        """ add labels in a string seperated by ,
        """
        labs = [x.strip() for x in lab.split(',')]
        for one in labs:
            self.labels.append(one)

    def run(self, input):
        """ runs the input on the built tree
            returns the value it predicts 
        """ 
        test = [x.strip() for x in input.split(',')]
        current = self.start

        while len(test) > 0:
            if current.leaf:
                return current.label
            else:
                atrindex = list(self.attributes.keys())
                index = atrindex.index(current.attribute)
                #move to next node
                current = current.childs[test[index]]
                #change data in test to better debug
                test[index] = current.attribute


    def make_t(self, depth, data):
        if depth == 0:
            #find majoriy label
            counter = dict()
            for ex in data:
                label = ex[len(ex)-1]
                if label not in counter.keys():
                    counter[label] = 1
                else:
                    counter[label] += 1
            #find highest
            most = list(counter.keys())[0]
            if len(most) == 0:
                leaf = node('leaf')
                leaf.is_leaf()
                leaf.set_label('error')
                return leaf

            for victim in list(counter.keys()):
                if counter[victim] > counter[most]:
                    most = victim
            #make leaf with most common label
            leaf = node('leaf')
            leaf.is_leaf()
            leaf.set_label(most)
            return leaf

        #depth is not zero
        else:
            #check if labels are the same
            prev = data[0][len(data[0])-1]
            same = True
            for victim in data:
                if prev != victim[len(victim)-1]:
                    same = False
                    break
            #if all same label then make leaf
            if same:
                leaf = node('leaf')
                leaf.is_leaf()
                leaf.set_label(prev)
                return leaf

            #not all same so calculate gain 
            else:
                temp = data
                #looking for lowest value in gain
                gain = dict()
                anum = 0
                for atrib in self.attributes.keys():
                    if temp[0][anum] != atrib:
                        gain[atrib] = 0

                        if self.type == 'Gini':
                            gain[atrib] = 1

                        mecounter = dict()
                        #if attribute has not been used to split
                        for val in self.attributes[atrib]:
                            counter = dict()
                            denom = 0
            
                            for ll in self.labels:
                                counter[ll] = 0
                                mecounter[ll] = 0 

                            #for each example atr in data 
                            for atr in temp:
                                #if attribute value in this example
                                if val in atr[anum]:
                                    counter[atr[len(atr)-1]] += 1
                                    mecounter[atr[len(atr)-1]] += 1
                                    denom += 1
                                        
                            s = len(data)
                            for a in counter.keys():
                                if counter[a] != 0:
                                    #calculate the gain for different types
                                    if self.type == 'ID3':
                                        gain[atrib] += ((counter[a])/s) * ( -((counter[a]/denom) * math.log((counter[a]/denom),2))) 
                                    if self.type == 'Gini':
                                        gain[atrib] -= math.pow((counter[a]/s), 2)

                            if self.type == 'Gini':
                                gain[atrib] = gain[atrib] * (denom/s)
                            #special for majority error
                            if self.type == 'ME':
                                best = list(mecounter.keys())[0]
                                for me in mecounter.keys():
                                    if (mecounter[best]/s) < (mecounter[me]/s):
                                        best = me
                                gain[atrib] = (s- mecounter[best])/s
                            

                        
                    anum +=1
                #find best attribute to split
                #TODO select random attributes to chose from
                best = list(gain.keys())[0]
                for attribute in gain.keys():
                    if gain[attribute] < gain[best]:
                        best = attribute 
                
                #split on best
                nd = node(best)
                nd.set_label('split')
                find = list(self.attributes)
                for x in range(0, len(find)):
                    if find[x] == best:
                        find = x
                        break

                for val in self.attributes[best]:
                    newdata = []
                    for test in data:
                        if val in test[find]:
                            mod = []
                            for x in test:
                                mod.append(x)
                            mod[find] = best
                            newdata.append(mod)
                    #make leaf with majority label
                    if len(newdata) == 0:
                        cc = dict()
                        for a in self.labels:
                            cc[a] = 0
                        for ex in data:
                            label = ex[len(ex)-1]
                            cc[label] += 1
                        labellist = list(cc.keys())
                        mm = labellist[0]
                        for lab in labellist:
                            if cc[lab] > cc[mm]:
                                mm = lab
                        leaf = node('leaf')
                        leaf.is_leaf()
                        leaf.set_label(mm)
                        return leaf
                        
                    else:
                        nd.childs[val] = self.make_t(depth-1, newdata)
                return nd

    def make_s(self, depth, data):
        if depth == 0:
            #find majoriy label
            counter = dict()
            for ex in data:
                label = ex[len(ex)-1]
                if label not in counter.keys():
                    counter[label] = 1
                else:
                    counter[label] += 1
            #find highest
            most = list(counter.keys())[0]
            if len(most) == 0:
                leaf = node('leaf')
                leaf.is_leaf()
                leaf.set_label('error')
                return leaf

            for victim in list(counter.keys()):
                if counter[victim] > counter[most]:
                    most = victim
            #make leaf with most common label
            leaf = node('leaf')
            leaf.is_leaf()
            leaf.set_label(most)
            return leaf

        #depth is not zero
        else:
            #check if labels are the same
            prev = data[0][len(data[0])-1]
            same = True
            for victim in data:
                if prev != victim[len(victim)-1]:
                    same = False
                    break
            #if all same label then make leaf
            if same:
                leaf = node('leaf')
                leaf.is_leaf()
                leaf.set_label(prev)
                return leaf

            #not all same so calculate gain 
            else:
                temp = data
                #looking for lowest value in gain
                gain = dict()
                anum = 0
                for atrib in self.attributes.keys():
                    if temp[0][anum] != atrib:
                        gain[atrib] = 0

                        if self.type == 'Gini':
                            gain[atrib] = 1

                        mecounter = dict()
                        #if attribute has not been used to split
                        for val in self.attributes[atrib]:
                            counter = dict()
                            denom = 0
            
                            for ll in self.labels:
                                counter[ll] = 0
                                mecounter[ll] = 0 

                            #for each example atr in data 
                            for cc in range(0, len(temp)):
                                #if attribute value in this example
                                atr = temp[cc]
                                if val in atr[anum]:
                                    if self.stump:
                                        www =  self.weights[cc]
                                    else:
                                        www = 1
                                    #use weight instead of just 1 if stump
                                    counter[atr[len(atr)-1]] += www
                                    mecounter[atr[len(atr)-1]] += www
                                    denom += www
                                        
                            s = len(data)
                            for a in counter.keys():
                                if counter[a] != 0:
                                    #calculate the gain for different types 
                                    if self.type == 'ID3':
                                        gain[atrib] += ((counter[a])/s) * ( -((counter[a]/denom) * math.log((counter[a]/denom),2))) 
                                    if self.type == 'Gini':
                                        gain[atrib] -= math.pow((counter[a]/s), 2)

                            if self.type == 'Gini':
                                gain[atrib] = gain[atrib] * (denom/s)
                            #special for majority error
                            if self.type == 'ME':
                                best = list(mecounter.keys())[0]
                                for me in mecounter.keys():
                                    if (mecounter[best]/s) < (mecounter[me]/s):
                                        best = me
                                gain[atrib] = (s- mecounter[best])/s
                            

                        
                    anum +=1
                #find best attribute to split
                best = list(gain.keys())[0]
                for attribute in gain.keys():
                    if gain[attribute] < gain[best]:
                        best = attribute 
                
                #split on best
                nd = node(best)
                nd.set_label('split')
                find = list(self.attributes)
                for x in range(0, len(find)):
                    if find[x] == best:
                        find = x
                        break

                for val in self.attributes[best]:
                    newdata = []
                    for test in data:
                        if val in test[find]:
                            mod = []
                            for x in test:
                                mod.append(x)
                            mod[find] = best
                            newdata.append(mod)
                    #make leaf with majority label
                    if len(newdata) == 0:
                        cc = dict()
                        for a in self.labels:
                            cc[a] = 0
                        for ex in data:
                            label = ex[len(ex)-1]
                            cc[label] += 1
                        labellist = list(cc.keys())
                        mm = labellist[0]
                        for lab in labellist:
                            if cc[lab] > cc[mm]:
                                mm = lab
                        leaf = node('leaf')
                        leaf.is_leaf()
                        leaf.set_label(mm)
                        return leaf
                        
                    else:
                        nd.childs[val] = self.make_t(depth-1, newdata)
                return nd


    def make_tree(self, ty, dep):
        """ make the tree with the type of 'ID3', 'Gini', or 'ME',
            int max depth of the tree (< zero if no limit)
        """
        #compute information gain for each attribute
        self.depth = dep

        if ty != 'ID3' and ty != 'Gini' and ty != 'ME':
            print("use 'ID3', 'Gini', or 'ME' for type of tree in first argument")
        else:
            self.type = ty
            self.start = ''
            self.start = self.make_t(dep, self.training)


    def make_random(self, ty, dep):
        """ make a tree with the specified type and depth that
            splits on random attributes
        """
        self.depth = dep
        if ty != 'ID3' and ty != 'Gini' and ty != 'ME':
            print("use 'ID3', 'Gini', or 'ME' for type of tree in first argument")
        else:
            self.type = ty
            self.start = ''
            self.random = True
            self.start = self.make_t(dep, self.training)

    def make_stump(self, www):
        """ make a stump with depth 1
        """
        self.depth = 1
        self.type = 'ID3'
        self.stump = True
        self.weights = www
        self.start = self.make_s(1, self.training)