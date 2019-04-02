import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

from scipy import stats


class ChartNode:

    def __init__(self, prior_weight=50, backend='Qt5Agg', **plot_opts):
        self.prior_weight = prior_weight
        self.backend = backend
        self.plot_opts = plot_opts
        self.sentiment = pd.Series()

        # Configure interactive plotting
        matplotlib.use(self.backend)
        plt.ion()

        self.plot_opts.setdefault('figsize', (16, 9))

    def __call__(self, data):
        time = data['time']
        value = data['sentiment']
        self.sentiment.loc[time] = value

        if self.sentiment.shape[0] <= 1:
            return

        tmp = self.sentiment.sort_index()
        a = self.prior_weight + tmp.map(lambda s: np.rint(5 * s)).map(lambda r: 0 if r < 0 else r).rolling(tmp.shape[0], min_periods=1).sum()
        b = self.prior_weight + tmp.map(lambda s: np.rint(5 * s)).map(lambda r: 0 if r > 0 else r).rolling(tmp.shape[0], min_periods=1).sum()

        mean = pd.Series(stats.beta.mean(a, b), tmp.index)
        p05 = pd.Series(stats.beta.ppf(0.05, a, b), tmp.index)
        p95 = pd.Series(stats.beta.ppf(0.95, a, b), tmp.index)

        # data = pd.DataFrame({p: stats.beta.pdf(p, a, b) for p in np.linspace(0, 1, 11)}, index=tmp.index).resample('10S').mean()

        # Plot the data
        plt.gca().cla()
        # sns.heatmap(data.T, cbar=False)

        ax = mean.plot(c='C0', **self.plot_opts)
        # ax = p05.plot(c='C0', **self.plot_opts)
        # p95.plot(ax=ax, c='C0', **self.plot_opts)
        ax.set(ylim=(0, 1))
        sns.despine()
        plt.pause(0.001)
