'''
Define, parameterize regimes
This file serves as the control center / parameter tuning room for rest of the simulation
'''

# There is *no reason* to vary these parameters:

DOMAIN = 2 # only consider binary (eg yes/no) question setting
BUDGET = 10
NUM_ROUNDS = 100 # grow as we're more sure simulation's efficacy

# These parameters *could* be varied:

# True => use kong map to get budget-adjusted scores vs
# False => use normalized scores directly from dmi
KONG = True
# agents in each committee
NUM_AGENTS = 5 # try with 3, 5, 10, 20
# how large dmi task batch is in each round
NUM_QUESTIONS_PER_ROUND = 50 # try low and high

# These parameters *will* be varied:

Lambda = {
  'all': 0, # all agent 1, no agent 2
  'more': 0.25, # more of agent 1 than agent 2
  'even': 0.5, # even agent 1, 2
  'none': 1 # all agent 2
}

Delta = {
  'none': 0, # no noise
  'slight': 0.1, # some noise
  'all': 0.5, # all noise = random strategy
  'un': None # unused
}

Bias = {
  'none': 0.5, # no bias, even yes, no Qs
  'slight': 0.1, # more of yes Qs than no
  'all': 0, # all yes Qs, all bias
}

# Regimes are built by varying the parameters above:

REGIME_SEEDS = [
  # controls
  { 'id': 0, 'lambda': Lambda['all'], 'delta1': Delta['none'], 'delta2': Delta['un'], 'bias': Bias['none'], 'description': 'all honest, fully-informed agents, no bias'},
  { 'id': 1, 'lambda': Lambda['none'], 'delta1': Delta['un'], 'delta2': Delta['all'], 'bias': Bias['none'], 'description': 'all random agents, no bias'},
  { 'id': 2, 'lambda': Lambda['all'], 'delta1': Delta['none'], 'delta2': Delta['un'], 'bias': Bias['slight'], 'description': 'all honest, fully-informed agents, some bias'},
  { 'id': 3, 'lambda': Lambda['none'], 'delta1': Delta['un'], 'delta2': Delta['all'], 'bias': Bias['slight'], 'description': 'all random agents, some bias'},

  { 'id': 4, 'lambda': Lambda['more'], 'delta1': Delta['none'], 'delta2': Delta['all'], 'bias': Bias['none'], 'description': 'more honest than random agents, no bias'},
  { 'id': 5, 'lambda': Lambda['more'], 'delta1': Delta['none'], 'delta2': Delta['all'], 'bias': Bias['slight'], 'description': 'more honest than random agents, some bias'},
  { 'id': 6, 'lambda': Lambda['more'], 'delta1': Delta['none'], 'delta2': Delta['all'], 'bias': Bias['all'], 'description': 'more honest than random agents, all bias'},

  { 'id': 7, 'lambda': Lambda['even'], 'delta1': Delta['none'], 'delta2': Delta['all'], 'bias': Bias['none'], 'description': 'even honest & random agents, no bias'},
  { 'id': 8, 'lambda': Lambda['even'], 'delta1': Delta['none'], 'delta2': Delta['all'], 'bias': Bias['slight'], 'description': 'even honest & random agents, some bias'},
  { 'id': 9, 'lambda': Lambda['even'], 'delta1': Delta['none'], 'delta2': Delta['all'], 'bias': Bias['all'], 'description': 'even honest & random agents, all bias'},

  { 'id': 10, 'lambda': Lambda['even'], 'delta1': Delta['slight'], 'delta2': Delta['all'], 'bias': Bias['none'], 'description': 'more mostly honest than random agents, no bias'},
  { 'id': 11, 'lambda': Lambda['even'], 'delta1': Delta['slight'], 'delta2': Delta['all'], 'bias': Bias['slight'], 'description': 'more mostly honest than random agents, some bias'},
  { 'id': 12, 'lambda': Lambda['even'], 'delta1': Delta['slight'], 'delta2': Delta['all'], 'bias': Bias['all'], 'description': 'more mostly honest than random agents, all bias'},

  { 'id': 13, 'lambda': Lambda['even'], 'delta1': Delta['slight'], 'delta2': Delta['all'], 'bias': Bias['none'], 'description': 'even slightly honest & random agents, no bias'},
  { 'id': 14, 'lambda': Lambda['even'], 'delta1': Delta['slight'], 'delta2': Delta['all'], 'bias': Bias['slight'], 'description': 'even slightly honest & random agents, some bias'},
  { 'id': 15, 'lambda': Lambda['even'], 'delta1': Delta['slight'], 'delta2': Delta['all'], 'bias': Bias['all'], 'description': 'even slightly honest & random agents, all bias'},
]
