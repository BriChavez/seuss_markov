import re
import string
from numpy.random import choice
import random


def markov_dict():
    """create a dict of how what words follow which and how many times they did"""
    with open('./seuss_script.txt', 'r') as seuss_script:
        # open txt file and read to string, string to lower
        seussical = seuss_script.read()
        seussical = seussical.lower()
        word_freqs = {}
        # use regex to split text into words and punctuation
        global seuss_string
        seuss_string = re.sub(
            '['+string.punctuation+']', '', seussical).split()
        past_word = ""
        frequency = {}
        # for loop that runs over every word in test
        for word in seuss_string:
            # if past_word is in dict, assign it to 'frequency'
            if past_word in word_freqs:
                frequency = word_freqs[past_word]
            # if not, create empty dictionary with past_word as the key and frequency as the value
            else:
                word_freqs[past_word] = frequency

            if word in frequency:
                frequency[word] += 1
            else:
                frequency[word] = 1

            past_word = word

        return word_freqs


markov_dict()
# name our new dictionary of words and count of next possible words to a new variable
seuss_dict = markov_dict()
# print(seuss_dict)


import re
import string
from numpy.random import choice
import random

def markov_dict():
    """create a dict of how what words follow which and how many times they did"""
    with open('./seuss_script.txt', 'r') as seuss_script:
        # open txt file and read to string, string to lower
        seussical = seuss_script.read()
        seussical = seussical.lower()
        word_freqs = {}
        # use regex to split text into words and punctuation
        global seuss_string
        seuss_string = re.sub('['+string.punctuation+']', '', seussical).split()
        past_word = ""
        frequency = {}
        # for loop that runs over every word in test
        for word in seuss_string:
            # if past_word is in dict, assign it to 'frequency'
            if past_word in word_freqs:
                frequency = word_freqs[past_word]
            # if not, create empty dictionary with past_word as the key and frequency as the value
            else:
                word_freqs[past_word] = frequency

            if word in frequency:
                frequency[word] += 1
            else:
                frequency[word] = 1

            past_word = word

        return word_freqs

markov_dict()
# name our new dictionary of words and count of next possible words to a new variable
seuss_dict = markov_dict()
# print(seuss_dict)


"""start the story"""

# name variable with the first word in our list of words
first_word = random.choice(seuss_string)
print(first_word)
# name the first word of our story as
global story
story = []


def start_story(list):
    """function to start the story"""
    if story == []:
        # set story up with a first word
        story.append(first_word)
    else:
        # dont start the story if its already been started
        pass
    return story


start_story(seuss_string)
# call function on our list of words from the text
seuss_list = seuss_string


def whos_next():
    """function to get the next word using weighted probability"""

    for outer_word, inner_dict in seuss_dict.items():
        # pick out our nested dict for specific word
        word_self_total = inner_dict.items()
        # get the next words and instances
        total_occurances = inner_dict.values()
        # seperate the instances
        if outer_word == current_word:
            # pull the dictionary for the current word
            total = sum(total_occurances)
            # add the total times a word followed current word
            probs = []
            # set empty variable for the percent chance of each word occuring
            hopefuls = []
            # set a list of all words that came after current word
            likely = []
            # set an empty list to grab the count of each word
            for number in total_occurances:
                # pull every number of times each word came after current
                percent = number / total
                # factor the percent chance of a word being next
                probs.append(percent)
                # add each percent to our probs list

            for word, num in word_self_total:
                # pull words and their values from our inner dict
                hopefuls.append(word)
                # add each word to our hopefuls list
                likely.append(num)
                # add each number to our likely list
                global rng_says

            rng_says = choice(hopefuls, p=probs)
            # weighted rng based off the percent probability of word occuring
            return rng_says


"""add words to the story"""
next_word = str(rng_says)
# change rng output from numpy to string
story.append(next_word)
# add our next word string to the story
current_word = story[-1]
# set current word to be the last word of the story

print(story)
whos_next()


vals = [do() for _ in range(3)]
