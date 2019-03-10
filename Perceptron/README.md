Perceptron implementation
This wil only support binary labels

How to use:
create the new perceptron object with the parameter of how many attributes.
once created add the strining one at a time with the add_training method.
to make the perceptron use the make_regular, make_vote or make_average to choose one of the different versions. 
once this is made you can use the run method that takes the test string and returns 0 or 1.
you can use the create more than once to create different types with the same training and it overwrite the previous.