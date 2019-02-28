How to use bagging and adaboost:
to add the attributes in the add_attrubute it must be a string that 
has the name of the sttribute first followed by the values it can hold.
everything must be separated by ','
the attributes mus be added in the same order as they will appear in
the training and testing

to add the lables the same thing applys just have all of the labels 
separated by ','

to add the training just have the attributes in the same order as they
were added and have the label last. everything separated by ','

the make_boost, make_full and make_random(doesn't work yet) will make
adaboost or the bagging trees.
make_boost only needs the amount of iterations you want to have.
make_full requires how many trees and how much random training data
goes to each tree.

can run the examples by either running the run.py or using the 
run.sh script
