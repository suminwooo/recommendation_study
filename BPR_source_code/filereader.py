#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 12:44:43 2020

@author: shah
"""
from BPR_source_code.classes import user
from BPR_source_code.classes import movie
from numpy import random
from BPR_source_code.util import min_rating, random_vector, num_users
from random import seed
import pandas as pd
import numpy as np
def read_ratings(filename):
    seed(42)
    np.random.seed(42)
    ratings = pd.read_csv(filename,  sep=',', encoding='latin-1')
    ratings.columns = ['userId', 'movieId', 'rating', 'timestamp']
    ratings['userId'] = ratings['userId'].astype(int)
    ratings['movieId'] = ratings['movieId'].astype(int)
    ratings['rating'] = ratings['rating'].astype(float)

    numusers = num_users()

    msks = ratings['userId'] < numusers
    ratings = ratings[msks]
    users = dict()
    testcount = 0
    traincount = 0
    trainuserdict = dict()

    for index, row in ratings.iterrows():
        userid = int(row['userId'])
        movieid = int(row['movieId'])
        rating1 = float(row['rating'])
        minmovierating = min_rating()
        if rating1 >= minmovierating:
            if random.random() < 0.7:
                traincount = traincount + 1
                if userid in users.keys():
                    user1 = users[userid]
                    user1.movies_train[movieid] = rating1
                else:
                    user1 = user(userid)
                    user1.factor = random_vector()
                    user1.movies_train[movieid] = rating1
                    users[userid] = user1
                    trainuserdict[userid] = 1
            else:
                testcount = testcount + 1
                if userid in users.keys():
                    user1 = users[userid]
                    user1.movies_test[movieid] = rating1
                else:
                    user1 = user(userid)
                    user1.factor = random_vector()
                    user1.movies_test[movieid] = rating1
                    users[userid] = user1

    for index, row in ratings.iterrows():
        userid = int(row['userId'])
        movieid = int(row['movieId'])
        rating1 = float(row['rating'])
        if userid in users.keys():
            user1 = users[userid]
            user1.movies_all[movieid] = rating1

    return users

def read_movies(filename):
    df = pd.read_csv(filename, sep=",", encoding='latin-1')
    df.columns = ['movieId', 'title', 'genres']
    movies = dict()
    for index, row in df.iterrows():
        movieid = row['movieId']
        movie1 = movie(movieid, 0)
        movie1.factor = random_vector()
        movies[movieid] = movie1

    return movies
