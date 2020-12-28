'''
Constants for visualizations
'''

import numpy as np

# positioning of each viz
INFO = 0
CORR = 1 # success calculation div
LINE = 2
BOX = 3

CORR_WIDTH = 150 # how wide success calculation div should be

# BOX property
DISP = 0.34 # dispersion, or range of horizontal placement of dot
DOT_SIZE = 8 # size of circles
TRANS = 0.5 # need to translate to the right to keep atop right x-values

disperse = lambda npArr: npArr + np.random.rand(len(npArr))*DISP - np.ones(len(npArr))*DISP/2 + TRANS

def dict2html(obj, indent=1):
  '''
  @dev Source: https://stackoverflow.com/questions/3930713/python-serialize-a-dictionary-into-a-simple-html-output
  '''
  if isinstance(obj, list):
    htmls = []
    for k in obj:
      htmls.append(dict2html(k,indent+1))
    return '[<div style="margin-left: %dem">%s</div>]' % (indent, ',<br>'.join(htmls))
  if isinstance(obj, dict):
    htmls = []
    for k,v in obj.items():
      htmls.append("<span style='font-style: italic; color: #888'>%s</span>: %s" % (k, dict2html(v,indent+1)))
    return '{<div style="margin-left: %dem">%s</div>}' % (indent, ',<br>'.join(htmls))
  return str(obj)
