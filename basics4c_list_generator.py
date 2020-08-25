#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  2 20:16:44 2018

@author: rop
"""
import memory_profiler
import time
import random
import pandas as pd

n_samples = 100000

print('n_samples = {}'.format(n_samples))

print('list:')
print('memory (before): {}Mb'.format(memory_profiler.memory_usage()))
nums = [i for i in range(1, n_samples+1)]
randoms = random.sample(range(1, 10*n_samples+1), n_samples)

tic = time.process_time()
my_nums = [i*i for i in nums]
my_rand_sq = [i*i for i in randoms]
toc = time.process_time()
print('time (list): {}'.format(toc-tic))
print('memory (after): {}Mb'.format(memory_profiler.memory_usage()))

#def gen_sq(nums):
#    for i in nums:
#        yield (i*i)

print('*'*20)

print('generator:')
print('memory (before): {}Mb'.format(memory_profiler.memory_usage()))
tic = time.process_time()
my_nums = (i*i for i in nums)
my_rand_sq = (i*i for i in randoms)
toc = time.process_time()
print('time (generator): {}'.format(toc-tic))
print('memory (after): {}Mb'.format(memory_profiler.memory_usage()))


print('*'*50)
df = pd.read_csv('../data/nba_data/nba_players_teams_random.csv')

players = list(df['Players'])
teams = list(df['Teams'][pd.notnull(df['Teams'])])


def player_list(num_players):
    result = []
    for i in range(num_players):
        player = {
                    'id': i,
                    'name': random.choice(players),
                    'team': random.choice(teams)
                }
        result.append(player)
    return result


def player_generator(num_players):
    for i in range(num_players):
        player = {
                    'id': i,
                    'name': random.choice(players),
                    'team': random.choice(teams)
                }
        yield player


print('list:')
print('memory (before): {}Mb'.format(memory_profiler.memory_usage()))
tic = time.process_time()
list_player = player_list(n_samples)
toc = time.process_time()
print('time: {}'.format(toc-tic))
print('memory (after): {}Mb'.format(memory_profiler.memory_usage()))

print('*'*20)

print('generator:')
print('memory (before): {}Mb'.format(memory_profiler.memory_usage()))
tic = time.process_time()
gen_player = player_generator(n_samples)
toc = time.process_time()
print('time: {}'.format(toc-tic))
print('memory (after): {}Mb'.format(memory_profiler.memory_usage()))

print('*'*20)
for i in range(5):
    print(i, list_player[i])


