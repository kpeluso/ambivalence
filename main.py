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
from vizConstants import INFO, CORR, CORR_WIDTH, LINE, BOX, DOT_SIZE, TRANS, disperse, dict2html

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
      3. success calculation: number showing % count of rounds where avg earnings of agents of type1 > those of type2
        Called "success" because this determines how well the truth-telling incentives actuall hold
  '''
  output_file('kong'+str(KONG)+'rounds'+str(NUM_ROUNDS)+'nqr'+str(NUM_QUESTIONS_PER_ROUND)+"dmi-sim.html", title="dmi-test")
  plots = [
    [
      None, # will be replaced with information
      None, # will be replaced with success calculation
      figure(title="Cumulative Earnings Per Agent Per Round"),
      figure(title='Cumulative Earnings Per Agent', x_range=np.arange(NUM_AGENTS).astype(str))
    ] for _ in range(len(REGIME_SEEDS))
  ]
  for regimeIdx, seed in enumerate(REGIME_SEEDS):
    plots[regimeIdx][INFO] = Div(text='<h4>Regime Info</h4><br></br>'+dict2html(seed), width=CORR_WIDTH)
    cumulativeEarnings = [] # NUM_ROUNDS x NUM_AGENTS matrix, for each regime
    committee = createCommittee(NUM_AGENTS, seed['lambda'], seed['delta1'], seed['delta2'])
    # viz setup for regime
    plots[regimeIdx][LINE].grid.grid_line_alpha=0.3
    plots[regimeIdx][LINE].xaxis.axis_label = 'Round'
    plots[regimeIdx][LINE].yaxis.axis_label = 'Accumulated Earnings'
    plots[regimeIdx][BOX].grid.grid_line_alpha=0.3
    plots[regimeIdx][BOX].xaxis.axis_label = 'Agent'
    plots[regimeIdx][BOX].yaxis.axis_label = 'Earnings Per Round'
    for _ in range(NUM_ROUNDS):
      # create questions
      questions = createQuestions(NUM_QUESTIONS_PER_ROUND, seed['bias'])
      # committee answer questions
      answersPerAgent = [[getAgentAnswer(agent, signal) for signal in questions] for agent in committee]
      # dmi ran
      normalizedScores = dmi(answersPerAgent)
      # map scores to budget-adjusted payments
      budgetAdjustedScores = kong(normalizedScores, BUDGET, NUM_AGENTS) if KONG else normalizedScores
      # update cumulativeEarnings
      if len(cumulativeEarnings) == 0:
        cumulativeEarnings = [np.array(budgetAdjustedScores)]
      else:
        cumulativeEarnings = np.append(cumulativeEarnings, [np.array(budgetAdjustedScores)], axis=0)
    # setup viz
    rounds = list(range(NUM_ROUNDS))
    numAgent1 = getNumOf1(NUM_AGENTS, seed['lambda'])
    # calculate success
    percentCount = 100*sum([1 if v > 0 else 0 for v in np.average(cumulativeEarnings[:,:numAgent1], axis=1) - np.average(cumulativeEarnings[:,numAgent1:], axis=1)])/NUM_ROUNDS
    plots[regimeIdx][CORR] = Div(width=CORR_WIDTH, text='<h4>% count of rounds where avg earnings of agents of type1 > those of type2</h4><p>'+str(percentCount)+'</p>')
    # visualize cumulative earnings over rounds line graphs
    for agent in range(numAgent1):
      plots[regimeIdx][LINE].line(rounds, cumulate(cumulativeEarnings[:,agent]), color=Blues[8][np.random.randint(3,7)])
    for agent in range(numAgent1, NUM_AGENTS):
      plots[regimeIdx][LINE].line(rounds, cumulate(cumulativeEarnings[:,agent]), color=Oranges[8][np.random.randint(3,7)])
    # vizualize distribution of each agent's earnings per round
    for agent in range(numAgent1):
      plots[regimeIdx][BOX].circle(disperse(np.ones(NUM_ROUNDS)*agent), cumulativeEarnings[:,agent], color=Blues[8][4], fill_alpha=0.2, size=DOT_SIZE)
    for agent in range(numAgent1, NUM_AGENTS):
      plots[regimeIdx][BOX].circle(disperse(np.ones(NUM_ROUNDS)*agent), cumulativeEarnings[:,agent], color=Oranges[8][4], fill_alpha=0.2, size=DOT_SIZE)

  show(gridplot(plots, plot_width=400, plot_height=400))

if __name__ == '__main__':
  main()
