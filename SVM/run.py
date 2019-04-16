import svm

testfile = 'test.csv'
trainfile = 'train.csv'

training = []
testing = []

f = open(trainfile, 'r')
#get all training examples from file
for line in f:
    training.append(line)
f.close()

f = open(testfile, 'r')
#get all testing examples from file
for line in f:
    testing.append(line)
f.close()

one = svm.svm()

for x in training:
    one.add_training(x)

one.make_primal(100, 0.5, (100/873), 1)


count = 0
error = 0
for test in testing:
    tt = [x.strip() for x in test.split(',')]
    ans = tt[len(tt)-1]
    ans = int(ans)

    guess = one.run(test)
    if ans == guess:
        error += 1
    count += 1

print('teting error:' + str(error/count))

count = 0
error = 0
for test in training:
    tt = [x.strip() for x in test.split(',')]
    ans = tt[len(tt)-1]
    ans = int(ans)

    guess = one.run(test)
    if ans == guess:
        error += 1
    count += 1


print('training error:' + str(error/count))