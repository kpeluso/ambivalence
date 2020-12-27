'''
This file determines answers agents give to questions
'''

import numpy as np

from constants import DOMAIN

def getAgentStrategy(delta):
  '''
  @dev Strategy row = signal from env. Strategy column = agent report
  @param delta :: [0,1] = noise of agent's informative strategy
  @return Strategy agent uses to answer questions
  '''
  return [
    [1-delta, delta],
    [delta, 1-delta]
  ]

def getAgentAnswer(delta, answer):
  '''
  @param delta :: [0,1] = noise of agent's informative strategy
  @param answer :: {0,1} = true answer of question
  @return Answer agent provides to question
  '''
  strategy = getAgentStrategy(delta)
  return np.random.choice(DOMAIN, p=strategy[answer])
