# AppleBananaClassifier

 This is a basic approach to handle inception net and implemented transfer learning to train the net to classify user specific object
 
 
 put your train data in the train_photo folder like in this hirerarcy :-
 
    .
    |
    train_photo
    |
    -> apple
        |
        -> apple01.jpg
        -> apple02.jpg # at least 30 photos
    -> banana
        |
        -> banana01.jpg
        -> banana02.jpg # at least 30 photos
    -> orange
        |
        -> orange01.jpg
        -> orange02.jpg # at least 30 photos
    ........... like so add as many fruite type as you like to train the neural net
    
NOTE : this repo already has two fruite's image in train_photo folder apple and banana

So at first you need to retrain the neural net after immediate download of this repository.

# Requirements
* You need Python 3.5
* Tensorflow version 1.4

NOTE: If you already have Python 3.5 and pipenv installed in your system then just open cmd or terminal and type `pipenv install` and pipenv will autometiaclly install and setup the environment for this program to run. After that type `pipenv shell` to activate that environment

# How to run
* First run the retrain.py file with `python3.5 retrain.py` in cmd/terminal and wait for this program to finishes it's execution
* Then run ValidationWithRandomImage.py file with `python3.5 ValidationWithRandomImage.py abc2.jpg`

NOTE: abc2.jpg is an image of banana which is already present in this repo. If you don't provide any argument while running the 2nd python script then by default abc.jpg an image of apple will be taken as input to classify.
