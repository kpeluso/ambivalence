# Ambivalance Test for DMI-Mechanism

*How well does this mechanism incentivize action over ambivalence?*

# Setup

`conda activate pricing`

`python main.py`

# Overview

Q = question

- Only consider binary (e.g. "yes/no") questions in this version
- Some agents sample from strategy I - the honest-strategy - for each Q
- Other agents sample from R strategy - the random/no strategy - for each Q
- We see what happens under different regimes, where...
  1. agents siloed (I with Is, R with Rs)
  2. agents mixed (lambda\*100% are I, (1-lambda)\*100% are R)
  3. I agents sample from delta-I - the noisy-honest strategy - for each Q

So, actually there are a few different regimes,
|Delta|\*|Lambda|\*|Bias| regimes where
  Delta = the set of delta (noise) values used
  Lambda = the set of lambda (mixture) values used
  Bias = the set of bias (of yes over no Qs) values used

### Hypotheses

- Overall goal #1 is to compare cumulative earnings of each type of agent in each regime
  - Hypothesis #1 is: difference between ambivalent/honest agents is not significant
  - This would imply that *ambivalence* is a "good-enough" strategy

- Overall goal #2 is to study the variance of times honest strategy beats rest
  - Hypothesis #2 is: variance of agents' earnings is significant
  - This would imply that DMI-Mechanism's truth-telling properties are not sufficiently robust

# Objects

<!-- ```Question :: { id: number, ans: number }``` -->
```Question :: number```
  - number is true answer to Q in [0, domainCardinality - 1]

<!-- ```Agent :: { id: number, delta: number }``` -->
```Agent :: number```
  - number = delta = noise of agent's reports given signal
  - in [0,1]

```RegimeSeed :: { lambda: number, delta1: number | None, delta2: number, bias: number }```
  - this is what's needed to create a regime
  - lambda = % of agents with delta2; 1-lambda = % agents with delta1
  - delta1, delta2 = agent characterization
  - bias = yes over no Qs (.5 => no bias)
  - all regime seed parameters in `[0,1]`

```Regime :: { numAgents: number, numQuestions: number, seed: RegimeSeed }```
  - joint distribution of agents and questions
  - `numQuestions` = number of questions, must be integer divisible by 2C
  - `numAgents` = number of agents
  - numAgents, numQuestions are set globally and just determine how clear results are
    - as a consequence, each regime loops through same number of Qs

# Helpful Links for Dev

1. [line graph](https://docs.bokeh.org/en/latest/docs/gallery/stocks.html)
2. [boxplot](https://docs.bokeh.org/en/latest/docs/gallery/boxplot.html)
3. [palettes](https://docs.bokeh.org/en/latest/docs/reference/palettes.html)
4. [to edit div](https://docs.bokeh.org/en/latest/docs/reference/models/widgets.markups.html?highlight=div#bokeh.models.widgets.markups.Div)
5. [categorical data](https://docs.bokeh.org/en/latest/docs/user_guide/categorical.html)
6. [examples, Bokeh homepage](https://docs.bokeh.org/en/latest/)

# License

MIT
