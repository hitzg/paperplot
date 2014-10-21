paperplot
=========

Simple setup utility for publication-ready matplotlib figures

Use `\the\textwidth` (or `\the\columnwidth` in multi-column articles) in the tex file to get the width of the text in pt.
Then use `setup()` and `paper_fig(width, height)` to generate your plot.

```python
import paperplot
import matplotlib.pyplot as plt

paperplot.setup()

fig = paperplot.paper_figure(300,200)
plt.plot(1,1)
plt.savefig('my_figure.pdf')
```
