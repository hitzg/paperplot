paperplot
=========

Simple setup utility for publication-ready matplotlib figures

#### Installation

Simply run:
```bash
python setup.py install           # using sudo might be necessary
```

#### Usage

Use `\the\textwidth` (or `\the\columnwidth` in multi-column articles) in the tex file to get the width of the text in pt.
Then use `setup()` and `paper_fig(width, height)` to generate your plot.

```python
import paperplot
import matplotlib.pyplot as plt

# setup
paperplot.setup()

# create a figure with proper sizes (specify width and height in pt)
fig = paperplot.paper_figure(300,200)

# some plotting
plt.plot(1,1)

# save the result
plt.savefig('my_figure.pdf')
```
