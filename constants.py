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
  # 0 - all honest, fully-informed agents, no bias
  { 'lambda': Lambda['all'], 'delta1': Delta['none'], 'delta2': Delta['un'], 'bias': Bias['none'] },
  # 1 - all random agents, no bias
  { 'lambda': Lambda['none'], 'delta1': Delta['un'], 'delta2': Delta['all'], 'bias': Bias['none'] },
  # 2 - all honest, fully-informed agents, some bias
  { 'lambda': Lambda['all'], 'delta1': Delta['none'], 'delta2': Delta['un'], 'bias': Bias['slight'] },
  # 3 - all random agents, some bias
  { 'lambda': Lambda['none'], 'delta1': Delta['un'], 'delta2': Delta['all'], 'bias': Bias['slight'] },

  # more honest than random agents
  # 4 - no bias
  { 'lambda': Lambda['more'], 'delta1': Delta['all'], 'delta2': Delta['none'], 'bias': Bias['none'] },
  # 5 - some bias
  { 'lambda': Lambda['more'], 'delta1': Delta['all'], 'delta2': Delta['none'], 'bias': Bias['slight'] },
  # 6 - all bias
  { 'lambda': Lambda['more'], 'delta1': Delta['all'], 'delta2': Delta['none'], 'bias': Bias['all'] },

  # even honest, random agents
  # 7 - no bias
  { 'lambda': Lambda['even'], 'delta1': Delta['all'], 'delta2': Delta['none'], 'bias': Bias['none'] },
  # 8 - some bias
  { 'lambda': Lambda['even'], 'delta1': Delta['all'], 'delta2': Delta['none'], 'bias': Bias['slight'] },
  # 9 - all bias
  { 'lambda': Lambda['even'], 'delta1': Delta['all'], 'delta2': Delta['none'], 'bias': Bias['all'] },

  # more mostly honest than random agents
  # 10 - no bias
  { 'lambda': Lambda['even'], 'delta1': Delta['slight'], 'delta2': Delta['none'], 'bias': Bias['none'] },
  # 11 - some bias
  { 'lambda': Lambda['even'], 'delta1': Delta['slight'], 'delta2': Delta['none'], 'bias': Bias['slight'] },
  # 12 - all bias
  { 'lambda': Lambda['even'], 'delta1': Delta['slight'], 'delta2': Delta['none'], 'bias': Bias['all'] },

  # even slightly honest, random agents
  # 13 - no bias
  { 'lambda': Lambda['even'], 'delta1': Delta['slight'], 'delta2': Delta['none'], 'bias': Bias['none'] },
  # 14 - some bias
  { 'lambda': Lambda['even'], 'delta1': Delta['slight'], 'delta2': Delta['none'], 'bias': Bias['slight'] },
  # 15 - all bias
  { 'lambda': Lambda['even'], 'delta1': Delta['slight'], 'delta2': Delta['none'], 'bias': Bias['all'] },
]
