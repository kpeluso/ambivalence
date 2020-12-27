'''
Here, regimes are set and main loop is run
'''

import itertools
import numpy as np
from bokeh.models import Div
from bokeh.layouts import gridplot
from bokeh.plotting import figure, output_file, show
from bokeh.palettes import Oranges, Blues

from utils import createQuestions, createCommittee, cumulate, getNumOf1
from agent import getAgentAnswer
from dmi import dmi, kong
from constants import BUDGET, KONG, NUM_AGENTS, NUM_QUESTIONS_PER_ROUND, NUM_ROUNDS, REGIME_SEEDS

# constants to position visualizations
LINE = 1
BOX = 2
CORR = 2

def main():
  '''
  @notice Main loop to run monte carlo
    For each regime, loop:
    1. Regime is setup
    2. Agents answer questions
    3. DMI-Mechanism ran
    4. Increment scores per agent
    5. Record Box-n-Whisker plots of each type of agent
    - After intra-regime loop done, record box-whisker
      plot for each type of agent. Then, whiskers could
      be compared and overlap among them found.
    - For each regime, plot
      1. line graph cumulative earnings per timestep per agent
      2. box-whisker/bio-dot-gram of distribution of cumulative earnings per agent
      3. box-whisker/bio-dot-gram **to show magnitude of overlap in earnings
        between agent type in each round**
  '''
  output_file("stocks.html", title="stocks.py example")
  plots = [
    [
      Div(text='<h4>Regime Index</h4><p>'+str(idx)+'</p>'),
      figure(title="Cumulative Earnings Per Agent Per Round"),
      figure(title='Cumulative Earnings Per Agent')
      # None # will be replaced with: Div(text='<h4>% Avg Time Agent Type1 Earnings > Type2</h4><p>'+str(ANSWER)+'</p>')
    ] for idx in range(len(REGIME_SEEDS))
  ]
  for regimeIdx, seed in enumerate(REGIME_SEEDS):
    cumulativeEarnings = [] # NUM_ROUNDS x NUM_AGENTS matrix, for each regime
    committee = createCommittee(NUM_AGENTS, seed['lambda'], seed['delta1'], seed['delta2'])
    # viz setup for regime
    plots[regimeIdx][LINE].grid.grid_line_alpha=0.3
    plots[regimeIdx][LINE].xaxis.axis_label = 'Round'
    plots[regimeIdx][LINE].yaxis.axis_label = 'Accumulated Earnings'
    for round in range(NUM_ROUNDS):
      # create questions
      questions = createQuestions(NUM_QUESTIONS_PER_ROUND, seed['bias'])
      # print(questions, ':questions')
      # committee answer questions
      answersPerAgent = [[getAgentAnswer(agent, signal) for signal in questions] for agent in committee]
      # print(answersPerAgent, ':answersPerAgent')
      # dmi ran
      normalizedScores = dmi(answersPerAgent)
      # print(normalizedScores, ':normalizedScores')
      # map scores to budget-adjusted payments
      budgetAdjustedScores = kong(normalizedScores, BUDGET, NUM_AGENTS) if KONG else normalizedScores
      # print(budgetAdjustedScores, ':budgetAdjustedScores')
      # update cumulativeEarnings
      if len(cumulativeEarnings) == 0:
        cumulativeEarnings = [np.array(budgetAdjustedScores)]
      else:
        cumulativeEarnings = np.append(cumulativeEarnings, [np.array(budgetAdjustedScores)], axis=0)
      # quit()
    # visualize cumulative earnings over rounds line graphs
    rounds = list(range(NUM_ROUNDS))
    for agent in range(getNumOf1(NUM_AGENTS, seed['lambda'])):
      plots[regimeIdx][LINE].line(rounds, cumulate(cumulativeEarnings[:,agent]), color=Blues[8][np.random.randint(3,7)])
    for agent in range(NUM_AGENTS - getNumOf1(NUM_AGENTS, seed['lambda'])):
      plots[regimeIdx][LINE].line(rounds, cumulate(cumulativeEarnings[:,agent]), color=Oranges[8][np.random.randint(3,7)])
    # break # just 1st regime

  show(gridplot(plots, plot_width=400, plot_height=400))

if __name__ == '__main__':
  main()
