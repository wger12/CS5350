import adaboost
import bagging
import statistics
import math

testfile = 'test.csv'
trainfile = 'train.csv'

training = []
testing = []
mod_train = []
mod_test = []
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

age = []
job = 'job, admin.,unknown,unemployed,management,housemaid,entrepreneur,student,blue-collar,self-employed,retired,technician,services'
marital = 'marital, married, divorced, single'
education = 'education, unknown, secondary, primary, tertiary'
default = 'default, yes, no'
balance = []
housing = 'housing, yes, no'
loan = 'loan, yes, no'
contact = 'contact, unknown, telephone, cellular'
day = []
month = 'month, jan, feb, mar, apr, may, jun, jul, aug, sep, oct, nov, dec'
duration = []
campaign = []
pdays = []
previous = []
poutcome = 'poutcome, unknown, other, failure, success'
label = 'yes, no'

#calculate the mean of numerical values
for train in training:
    parts = [x.strip() for x in train.split(',')]
    age.append(int(parts[0]))
    balance.append(int(parts[5]))
    day.append(int(parts[9]))
    duration.append(int(parts[11]))
    campaign.append(int(parts[12]))
    pdays.append(int(parts[13]))
    previous.append(int(parts[14]))

zero = statistics.median(age)
five = statistics.median(balance)
nine = statistics.median(day)
elev = statistics.median(duration)
twel = statistics.median(campaign)
thir = statistics.median(pdays)
fotn = statistics.median(previous)

#now with threshold I make these numeric values yes if above median and no if below or equal
#also feed to adaboost label and attributes
boost = adaboost.adaboost()
boost.add_labels(label)
boost.add_attribute('age, yes, no')
boost.add_attribute(job)
boost.add_attribute(marital)
boost.add_attribute(education)
boost.add_attribute(default)
boost.add_attribute('balance, yes, no')
boost.add_attribute(housing)
boost.add_attribute(loan)
boost.add_attribute(contact)
boost.add_attribute('day, yes, no')
boost.add_attribute(month)
boost.add_attribute('duration, yes, no')
boost.add_attribute('campaign, yes, no')
boost.add_attribute('pdays, yes, no')
boost.add_attribute('previous, yes, no')
boost.add_attribute(poutcome)
bag = bagging.bagging()
bag.add_labels(label)
bag.add_attribute('age, yes, no')
bag.add_attribute(job)
bag.add_attribute(marital)
bag.add_attribute(education)
bag.add_attribute(default)
bag.add_attribute('balance, yes, no')
bag.add_attribute(housing)
bag.add_attribute(loan)
bag.add_attribute(contact)
bag.add_attribute('day, yes, no')
bag.add_attribute(month)
bag.add_attribute('duration, yes, no')
bag.add_attribute('campaign, yes, no')
bag.add_attribute('pdays, yes, no')
bag.add_attribute('previous, yes, no')
bag.add_attribute(poutcome)


#now add training
#change tests and training to have the yes and no
meds = [zero,five,nine,elev,twel,thir,fotn]
checks = [0,5,9,11,12,13,14]
for train in training:
    parts = [x.strip() for x in train.split(',')]
    for x in range(0, len(checks)):
        if int(parts[checks[x]]) > meds[x]:
            parts[checks[x]] = 'yes'
        else:
            parts[checks[x]] = 'no'

    modded = ''
    for p in range(0, len(parts)-1):
        modded = modded + parts[p] + ','
    modded += parts[len(parts)-1]

    boost.add_training(modded)
    bag.add_training(modded)
    mod_train.append(modded)

for t in testing:
    parts = [x.strip() for x in t.split(',')]
    for x in range(0, len(checks)):
        if int(parts[checks[x]]) > meds[x]:
            parts[checks[x]] = 'yes'
        else:
            parts[checks[x]] = 'no'

    modded = ''
    for p in range(0, len(parts)-1):
        modded = modded + parts[p] + ','
    modded += parts[len(parts)-1]

    mod_test.append(modded)


#boost.make_boost(10)
#a = boost.run(mod_train[0])
#a += ''

for T in range(1,1001,50):
    a = (len(mod_train)/8)
    a = math.floor(a)
    bag.make_full(T, a)
    #find training error
    total = 0
    nope = 0
    for tt in mod_train:
        correct = tt.split(',')
        correct = correct[len(correct)-1].strip()
        ans = bag.run(tt)
        if correct != ans:
            nope += 1
        total += 1
    training_error = nope/total
    #find testing error
    total = 0
    nope = 0     
    for tt in mod_test:
        correct = tt.split(',')
        correct = correct[len(correct)-1].strip()
        ans = bag.run(tt)
        if correct != ans:
            nope += 1
        total += 1
    testing_error = nope/total

    print('T = ' + str(T) + ' training error = ' + str(training_error) + ' testing error = ' + str(testing_error))



#find the training and testing error for boosting
for T in range(1,1001,50):
    boost.make_boost(T)
    #find training error
    total = 0
    nope = 0
    for tt in mod_train:
        correct = tt.split(',')
        correct = correct[len(correct)-1].strip()
        ans = boost.run(tt)
        if correct != ans:
            nope += 1
        total += 1
    training_error = nope/total
    #find testing error
    total = 0
    nope = 0     
    for tt in mod_test:
        correct = tt.split(',')
        correct = correct[len(correct)-1].strip()
        ans = boost.run(tt)
        if correct != ans:
            nope += 1
        total += 1
    testing_error = nope/total

    print('T = ' + str(T) + ' training error = ' + str(training_error) + ' testing error = ' + str(testing_error))
