import numpy as np

def createQuestions(n, bias=.5):
  '''
  @notice Creates binary questions
  @param n :: Z+ = number of questions to make
  @param bias :: [0,1] = bias towards choice 0 over 1
  @return number[] = for each question, id of signal (true answer)
  '''
  return np.random.binomial(1, bias, n)

def getNumOf1(size, lam):
  '''
  @return number - Number of agents of type 1
  '''
  return size - round(lam*size)

def createCommittee(size, lam, delta1, delta2):
  '''
  @notice Creates committee of agents given their characterization
  @param size :: Z+ = committee size
  @param lam :: [0,1] = Proportion of delta 2 agent
  @param delta1 :: [0,1] = Noise of agent type 1's reports given signal
  @param delta2 :: [0,1] = Noise of agent type 2's reports given signal
  @return number[]
  '''
  return [delta1 if agent < getNumOf1(size, lam) else delta2 for agent in range(size)]

def cumulate(ls):
  '''
  @param ls :: number[]
  @return number[] = List of numbers equalling [ls[0], ls[0]+ls[1], ...]
  '''
  return [sum(ls[0:i]) for i in range(1,1+len(ls))]
