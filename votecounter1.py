# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 13:53:18 2020

@author: Gamer
"""

from collections import Counter
import math


def raw_majority(labels):
    votes = Counter(labels)
    winner, _ = votes.most_common(1)[0]
    return winner

labels = [ 'G', 'G', 'PG', 'PG', 'R']

print raw_majority(labels)

def majority_vote(labels):
    vote_counts = Counter(labels)
    winner, winner_count = vote_counts.most_common(1)[0]
    num_winners = len([count
                       for count in vote_counts.values()
                       if count == winner_count])
    
    if num_winners == 1:
        return winner
    else:
        return majority_vote(labels[:-1])
    
print majority_vote(labels)

def vector_subtract(v, w):
    return[v_i - w_i 
           for v_i, w_i in zip(v, w)]
def dot(v, w):
    return sum(v_i * w_i
               for v_i, w_i in zip(v, w))

def sum_of_squares(v):
    return dot(v, v)

def squared_distance(v, w):
    return sum_of_squares(vector_subtract(v,w))


def distance(v, w):
    return math.sqrt(squared_distance(v, w))





def knn_classify(k, labeled_points, new_point):
    by_distance = sorted(labeled_points,
                         key = lambda(point, _): distance(point, new_point))
    k_nearest_labels = [label for _, label in by_distance[:k]]
    return majority_vote(k_nearest_labels)





cities = [([-122.3, 47.53], "Python"),
          ([-96.85, 32.85], "Java"),
          ([-89.33, 43.13], "R"),
          ]

for k in [1,3, 5,7]:
    num_correct = 0
    
    for city in cities:
        location, actual_language = city
        other_cities = [other_city
                        for other_city in cities
                        if other_city != city]
        predicted_language = knn_classify(k, other_cities, location)
        
        if predicted_language == actual_language:
            num_correct +=1
    print k, "neighbor[s]:", num_correct, "correct out of", len(cities)