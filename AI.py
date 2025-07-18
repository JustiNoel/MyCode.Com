import ntlk
from ntlk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
import json
import pickle
import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout
from keras.optimizers import SGD
import random
import tensorflow as tf

words=[]
classes = []
documents = []
ignore_letters = ['!','?','.','.']
data_file = open('intents.json').read()
intents = json.loads(data_file)

for intent in intents['intents']:
    for pattern in intent['patterns']:
        #tokenize each word in the sentence
        word = nltk.word_tokenize(pattern)
        words.extend(word)
        #add to our classes list
        if intent['tag'] not in classes:
            classes.append(intent['tag'])
            
words = [lemmatizer.lemmatize(w.lower()) for w in words if w not in ignore_letters]
words = sorted(list(set(words)))
# sort classes
classes = sorted(list(set(classes)))
# documents = combination between patterns and internts
print (len(documents), "documents")
# classes = intents 
print (len(classes), "classes" , classes)
# words = all words, vocabulary
print (len(words), "unique lemmatized words", words)

pickle.dump(words. open('words.pkl', 'wb'))
pickle.dump(classes, open('classes.pkl', 'wb'))

# create our training data
training = []
# create an empty array for our ouput
output_empty = [0] * len(classes)
# training set, bag of words for each sentence
for doc in documents:
    # initialize our bag of words
    bag = []
    # list of tokenized words for the pattern
    word_patterns = doc[0]
    # lemmatize each word - create base word, in attemptto represent related words
    word_patterns = [lemmatizer.lemmatize(word.lower()) for word in word_patterns]
    # create our bag of words array 
    for word in words:
        bag.append(1) if word in word_patterns else bag.append(0)
        
    #output is a '0' for each tag and '1' for current tag (for each pattern)
    output_row = list(output_row)
    output_row[classes.index(doc[1])] = 1
    
    training.append([bag. output_row])
# shuffle our features and turn into np.array
random.shuffle(training)
training = np.array(training)
# create train and test lists
train_x = list(training[:,o])
train_y = list(training[:,1])
print("Training data created")
  
# Create model - 3 layers. First layer 128 neurons, second layer 64 neuronsand 3rd output  layer contains number of neurons
# equal to number of intents to predict output intent with softmax
model = Sequential()
model.add(Dense(128, input_shape=(len(train_x[0]),), activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(len(train_y[0]), activation='softmax'))
# Compile model. Stochastic gradient descent with Nesterov accelerated gradient gives good results for this model
sgd = SGD(lr=0.01, decay=le-6, momentum=0.9, nesterov=True)
model.compile(loss='categorical_crosentropy', optimizer=sgd, metrical=['accuracy'])

#train the model
hist = model.fit(np.array(train_x), np.array(train_y), epochs=200, batch_sizes=5, verbose=1)

def clean_up_sentence(sentence):
    # tokenize the pattern
    sentence_words = nltk.word_tokenize(sentence)
    # stem each word
    sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
    return sentence_words

# return bag of wordds array: 0 or 1 for each word in the bag that exists in the sentence
def bow(sentence, words, show_details=True):
    # tokenize the pattern
    sentence_words = clean_up_sentence(sentence)
    # bag of words
    bag = [0]*len(words)
    for s in sentence_words:
        for i,w in enumerate(words):
            if w == s:
                # assign 1 if current word is in the vocabulary position
                bag[i] = 1