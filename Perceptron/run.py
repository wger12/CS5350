import perceptron

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

one = perceptron.perceptron(4)

for x in training:
    one.add_training(x)

#regular
one.make_regular(1, 10)

count = 0
error = 0
for test in testing:
    tt = [x.strip() for x in test.split(',')]
    ans = tt[len(tt)-1]
    ans = int(ans)

    guess = one.run(test)
    if ans != guess:
        error += 1
    count += 1

print('regular error: ' + str(float(error/count)))

#average
one.make_average(1, 10)

count = 0
error = 0
for test in testing:
    tt = [x.strip() for x in test.split(',')]
    ans = tt[len(tt)-1]
    ans = int(ans)

    guess = one.run(test)
    if ans != guess:
        error += 1
    count += 1

print('average error: ' + str(error/count))

#voting
one.make_vote(1, 10)

count = 0
error = 0
for test in testing:
    tt = [x.strip() for x in test.split(',')]
    ans = tt[len(tt)-1]
    ans = int(ans)

    guess = one.run(test)
    if ans != guess:
        error += 1
    count += 1

print('voting error: ' + str(error/count))