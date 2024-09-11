#!/usr/bin/python3

def best_score(a_dictionary):

    best_score = a_dictionary[1]

    for key in a_dictionary[1:]:
        if a_dictionary[key] > best_score:
            best_score = key

    return best_score
