import decisionTree

testfile = 'car_test.csv'
trainfile = 'car_train.csv'


#test 
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
tree.make_tree('ME', -1)

#cars
tree2 = decisionTree.decisionTree(4, True)
tree2.add_attribute('buying, vhigh, high, med, low')
tree2.add_attribute('maint, vhigh, high, med, low')
tree2.add_attribute('doors, 2, 3, 4, 5more')
tree2.add_attribute('persons, 2, 4, more')
tree2.add_attribute('lug_boot, small, med, big')
tree2.add_attribute('safety, low, med, high')
tree2.add_labels('unacc, acc, good, vgood')
#get data from training file
f = open(trainfile, 'r')
for line in f:
    tree2.add_training(line)
f.close()

#find training error
tests = ['ID3', 'Gini', 'ME']
for test in tests:
    for size in range(1, 7):
        count = 0
        correct = 0
        print('Tree type: ' + test + ' size: ' + str(size))
        tree2.make_tree(test, size)
        f = open(testfile, 'r')
        for trial in f:
            right = trial.split(',')
            right = right[len(right)-1].strip()
            answer = tree2.run(trial)
            if answer == right:
                correct += 1
            count += 1
        print('error' + str(1 - (correct/count)))
        
        f.close()
        f = open(trainfile, 'r')
        for trial in f:
            right = trial.split(',')
            right = right[len(right)-1].strip()
            answer = tree2.run(trial)
            if answer == right:
                correct += 1
            count += 1
        f.close()

        print('error' + str(1 - (correct/count)))
