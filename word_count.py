# author: Jake Schlaerth
# date: 07/01/2020
#
# word_count.py
# ===================================================
# Implement a word counter that counts the number of
# occurrences of all the words in a file. The word
# counter will return the top X words, as indicated
# by the user.
# ===================================================

import re
from hash_map import HashMap

"""
This is the regular expression used to capture words. It could probably be endlessly
tweaked to catch more words, but this provides a standard.
"""
rgx = re.compile("(\w[\w']*\w|\w)")

def hash_function_2(key):
    """
    This is a hash function that can be used for the hash map.
    """

    hash = 0
    index = 0
    for i in key:
        hash = hash + (index + 1) * ord(i)
        index = index + 1
    return hash

def top_words(source, number):
    """
    Takes a plain text file and counts the number of occurrences of case insensitive words.
    Returns the top `number` of words in a list of tuples of the form (word, count).

    Args:
        source: the file name containing the text
        number: the number of top results to return (e.g. 5 would return the 5 most common words)
    Returns:
        A list of tuples of the form (word, count), sorted by most common word. (e.g. [("a", 23), ("the", 20), ("it", 10)])
    """

    # keys = set()

    ht = HashMap(25,hash_function_2)

    tuple_list = []

    # This block of code will read a file one word as a time and
    # put the word in `w`.
    with open(source) as f:
        for line in f:
            words = rgx.findall(line)
            for w in words:
                w = w.lower()
                if ht.contains_key(w):
                    # inc count
                    ht.put(w, ht.get(w) +1)

                else:
                    # start count
                    ht.put(w, 1)

        for bucket in ht._buckets:
            current = bucket.head
            while current is not None:
                tuple_list.append((current.key, current.value))
                current = current.next
        sort_tuples(tuple_list)
        return tuple_list[:number]


def second_item(tup):
    """
    returns the second item of a tuple
    :param tup: tuple
    :return: second item in tuple
    """
    return tup[1]


def sort_tuples(tuple_list):
    """
    :param tuple_list: list of tuples
    :return: list of tuples in sorted order according to second element of each tuple
    """
    tuple_list.sort(key=second_item, reverse=True)


if __name__ == "__main__":
    # when run as a python3 script, this line will search the local directory for a file called "alice.txt"
    # and return the 10 most common words in that file utilizing a hash map. Here, the text file is the
    # entirety of Lewis Carrol's Alice's Adventures in Wonderland
    print(top_words("alice.txt", 10))