'''
Peer prediction utilities
'''

from functools import reduce
from itertools import combinations as combs
import operator as op
import numpy as np

def ncr(n,r):
  '''@dev Source: https://stackoverflow.com/a/4941932'''
  r = min(r, n-r)
  numer = reduce(op.mul, range(n, n-r, -1), 1)
  denom = reduce(op.mul, range(1, r+1), 1)
  return numer // denom

fact = lambda n: reduce(op.mul, range(2, n+1), 1)

norm = lambda n,C,T1,T2: int((n-1)*fact(C)*ncr(T1,C)*ncr(T2,C))

def kong(scores, B, n):
  '''
  @notice Kong's transform of scores into payments that are:
          1. Linear in scores
          2. Sum to given budget
          3. Nonnegative
  @dev Floor division used to make in-line with Solidity code
       Similarly, it is assumed fixed-point base already multiplied
       Taken from older version of scoring service
  @param scores :: number[] = agent scores
  @param B :: Int = Budget
  @param n :: Int = num agents
  '''
  sbar = np.average(scores)
  bma = np.max(scores) - np.min(scores) + 1
  return list(map(lambda si: int((si-sbar+bma)*B//bma//n), scores))

def dmi(answers):
  '''
  @dev Taken from older version of scoring service
  @param answers :: List(N)<List<Int>>
  @return scores :: List<Float> = scores for committee members plus lower bound
  '''
  domain = 2
  N = len(answers)
  scores = np.zeros(N)
  numQs = len(answers[0])
  firstHalfQs = numQs//2
  for indxs in combs(range(N), 2):
    mat1 = np.zeros([domain, domain])
    for i in range(firstHalfQs):
      mat1[answers[indxs[0]][i]][answers[indxs[1]][i]] += 1
    mat2 = np.zeros([domain, domain])
    for i in range(firstHalfQs, numQs):
      mat2[answers[indxs[0]][i]][answers[indxs[1]][i]] += 1
    # print(mat1, mat2)
    prod = np.linalg.det(mat1) * np.linalg.det(mat2)
    # print(prod)
    scores[indxs[0]] += prod
    scores[indxs[1]] += prod
  Z = norm(N, domain, firstHalfQs, numQs-firstHalfQs)
  return list(map(lambda score: score/Z, scores))
