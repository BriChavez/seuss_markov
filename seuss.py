import re
import string
from numpy.random import choice
import random

"""READ FILE IN TO PLAY"""

with open('extra_text.txt', 'r') as seuss_script:
    # open txt file and read to string, string to lower
    seussical = seuss_script.read()
    seussical = seussical.lower()

# use regex to split text into words and punctuation, including contracted words
seuss_string = re.findall(r"[.,]|[a-z]+[']?[a-z]+", seussical)

"""CREATE OUR NESTED DICT TO SAVE HOW OFTEN ONE WORD FOLLOWS ANOTHER"""

seuss_dict = {}
# for loop that runs over every word in our string, but stating to stop at the last word
for i, word in enumerate(seuss_string[:-1]):
    # setting this word to be the word right after the one we were on
    this_word = seuss_string[i - 1]
    # if this_word isn't in our dictionary already...
    if this_word not in seuss_dict:
        # start our counter dict
        next_count = {}
        # add our new word to be a key in our seuss dict and the count dict to be its value
        seuss_dict[this_word] = next_count
    # if it is already in there....
    else:
        # create empty dictionary with this_word as the key and next_count as the value
        next_count = seuss_dict[this_word]
    # if the next word(word) is in our nested dict already...
    if word in next_count:
        # add one to its count
        next_count[word] += 1
    # if its not already in there
    else:
        # lets add it and set its count to 1
        next_count[word] = 1

"""START THE STORY"""

# starting out story off blank
story = []
# Pick the first word at random from our initial string
first_word = random.choice(seuss_string)
# while loop to make sure we dont start on punctuation
while first_word in string.punctuation:
    # if it was punctuation, choose again
    first_word = random.choice(seuss_string)
# if story is blank...
if story == []:
    # set story up with our first word
    story.append(first_word)

"""CREATE THE WEIGHTED PROB ALGORITHM TO DETERMINE THE NEXT WORD"""


# function to get the next word using weighted probability

def whos_next():
    # set the current word to the last line of the story
    current_word = story[-1]
    # pull the main words and the words following them from our nested dict
    for outer_word, inner_dict in seuss_dict.items():
        # set a variable to be equal to following words and their frequency counts
        word_self_total = inner_dict.items()
        # get the frequency counts from our following words
        total_occurrences = inner_dict.values()
        # enter the outer dictionary of the word we are on
        if outer_word == current_word:
            # add the total times a word followed current word
            total = sum(total_occurrences)
            # set empty variable for the percent chance of each word occurring
            probs = []
            # set a list of all words that came after current word
            hopefuls = []
            # set an empty list to grab the count of each word
            likely = []
            # pull every number of times each word came after current
            for number in total_occurrences:
                # factor the percent chance of a word being next
                percent = number / total
                # add each percent to our probs list
                probs.append(percent)
            # pull words and their values from our current word's inner dict
            for word, num in word_self_total:
                # add each word to our hopefuls list
                hopefuls.append(word)
                # add each number to our likely list
                likely.append(num)
            # weighted rng based off the percent probability of word occurring
            rng_says = choice(hopefuls, p=probs)
            # change rng output from numpy to string
            next_word = str(rng_says)
            # add our next word string to the story
            story.append(next_word)


"""ADD WORDS TO OUR STORY, DROP WHITE SPACE, CAPITALIZE, AND NEWLINE"""

# while our story is less than this long
while len(story) < 200:
    # call our function
    whos_next()
# set our full story to be 
whole_story = ' '.join(story)

# replace white space preceding punctuation
# Matches the contents of the group of the same number. Groups are numbered starting from 1
whole_story = re.sub(r'\s([?.,!](?:\s|$))', r'\1', whole_story)

# re-split the story, this time on sentences
sentences = re.split('[?.]', whole_story)
# set a new clean variable
cap_sent = []
# run each sentence of our story through this for loop


def cut_down(sentence):
    """function to make our sentences have to be less than 13 words long"""
    # if they aren't...
    if len(sentence.split(' ')) > 12:
        # prefer to split on a comma, so lets do that first
        if ',' in sentence:
            # count the commas and pick the middle one to split it into two lines
            *a, b = sentence.split(', ', sentence.count(',') // 2 + 1)
            # the first half (a) is a list, so lets fix that, drop the leading white space, and capitalize the first word
            a = ', '.join(a).lstrip().capitalize()
            # capitalize the second half (b) and strip the leading white space
            b = b.lstrip().capitalize()
            # if the first half of the sentence is still too long,
            if a.count(' ') > 12:
                # we send it through this function
                a = cut_down(a)
            # same with b
            if b.count(' ') > 12:
                # cut it back if it is too long
                b = cut_down(b)
            # bring our new shorter sentences back together with a comma and a new line
            sentence = ''.join(a) + ',\n' + b

        # split the sentence if it has no commas
        else:
            # count the spaces and split in the middle
            *a, b = sentence.split(' ', len(sentence.split(' ')) // 2 + 1)
            # the first half (a) is a list, so lets fix that, drop the leading white space, and capitalize the first word
            a = ' '.join(a).lstrip().capitalize()
            # capitalize the second half (b) and strip the leading white space
            b = b.lstrip().capitalize()
            # if the first half of the sentence is still too long,
            if a.count(' ') > 12:
                # we send it through this function
                a = cut_down(a)
            # same with b
            if b.count(' ') > 12:
                # cut it back if it is too long
                b = cut_down(b)
            # bring our new shorter sentences back together with a comma and a new line
            sentence = ''.join(a) + ',\n' + b

        # now, lets get our sentence back
        return sentence

    # if the sentence isn't too long...
    else:
        # give it back to us
        return sentence


# lets clean up our story so the output looks prettier
for sentence in sentences:
    # lets drop the leading white space and capitalize each sentence
    sentence = sentence.lstrip().capitalize() + '.' + "\n"
    # now, lets send each one through our function to make sure our sentences aren't crazy long
    sentence = cut_down(sentence)
    # now that they look better, lets add it to a clean list
    cap_sent.append(sentence)
# join the list so it is a string
cap_sent = ''.join(cap_sent)

"""NOW LET'S SAVE AND READ OUR NEW TALE"""

# open a file of whatever name we want to save it as
text_file = open('seuss_story5.txt', 'w')
# write our newly made and beautifully laid out dr seuss story to the file
text_file.write(cap_sent)
# shut it down and share your fun story with a friend
text_file.close()

"""THE END"""
