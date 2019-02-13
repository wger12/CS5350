import decisionTree

atr1 = 'x1, 0, 1'
atr2 = 'x2, 0, 1'
atr3 = 'x3, 0, 1'
atr4 = 'x4, 0, 1'
attributes = 4
train1 = '0, 0, 1, 0, 0'
train2 = '0, 1, 0, 0, 0'
train3 = '0, 0, 1, 1, 1'
train4 = '1, 0, 0, 1, 1'
train5 = '0, 1, 1, 0, 0'
train6 = '1, 1, 0, 0, 0'
train7 = '0, 1, 0, 1, 0'
tree = decisionTree.decisionTree(attributes, True)
tree.add_attribute(atr1)
tree.add_attribute(atr2)
tree.add_attribute(atr3)
tree.add_attribute(atr4)
tree.add_training(train1)
tree.add_training(train2)
tree.add_training(train3)
tree.add_training(train4)
tree.add_training(train5)
tree.add_training(train6)
tree.add_training(train7)
tree.add_labels('0,1')
tree.make_tree('ID3', -1)
a = 2