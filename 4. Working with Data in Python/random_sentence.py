import random

adjectives = ['timid', 'mad', 'scary', 'suspicous', 'scheming', 'wise old', 'foolish', 'handsome','spooky', 
              'friendly', 'splendid', 'obscene', 'overrated', 'ill-informed', 'industrious', 'drunk', 'spiteful', 
              'potty-mouthed', 'furious', 'humble', 'kindly', 'well-dressed', 'chatty', 'obnoxious', 'rude', 
              'cool', 'huaghty', 'arrogant', 'calculating', 'loquacious', 'ridiculous', 'brave', 'outragous', 
              'witty', 'hedonistic', 'brainy']

animals = ['snake', 'horse', 'sloth', 'crocodile', 'lizard', 'chicken', 'ottor', 'newt', 'whale', 'goat', 'panda', 
           'rabbit', 'bat', 'goose', 'moose', 'koala', 'dophin', 'badger', 'hamster', 'pig', 'snail', 'hippo', 
           'bee', 'kangaroo', 'elephant', 'giraffe', 'duck', 'fox', 'spider', 'slug', 'pug', 'eagle']

verbs = ['conspired against', 'mis-sold ppi to', 'played squash with', 'sent a postcard to', 'got married to', 
         'had their heart broken by', 'tried to eat', 'was beaten at chess by', 'prank called', 'sent bitcoin to', 
         'took a train with', 'went into the cheese business with', 'had a mild dispute with', 'fell in love with',
         'cheated at monopoly against', 'went to a rave with', 'thought little of', 'liked the style of', 
         'was suspicious of', 'stole the shoes of', 'directed a hit musical with', 'went rollerbrlading with', 
         'discussed Marxism with', 'travelled the world with', 'disapproved of the politics of', 
         'went bowling with', 'had an affair with', "couldn't get enough of", 'hurt the feelings of', 
         'lost at connect 4 against', 'doubted the integrity of', 'had a duel with', 'started an underground gambling ring with', 
         'was taught karate by', 'listened to the conspiracy theories of', 'fell in love with', 
         'just wanted to be appreciated by', 'questioned the motives of', 'founded a tech company with', 
         'did a charity fun-run with', 'exposed the hypocracy of', 'was arrested by', 'went to art school with', 
         'was caught fiddling his expenses by', 'started a ponzi scheme with', 
         'was convinced to enter into a pyramid scheme with', 'regretted agreeing to go fishing with', 'really loved', 
         'set up an off-shore shell corporation with', 'saved the world from', 'won strictly come dancing with',
         'took out the bins for', 'had a rap battle with', 'went on a yoga retreat with', 'was thrown in a Thai prison with']

def generate_random_sentence():
    return ' '.join([random.choice(word) for word in [['The'], adjectives, animals, verbs, ['the'], adjectives, animals]])