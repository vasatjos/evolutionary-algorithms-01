# use and edit this file to make all the plots you need - it is generally easier
# than plotting directly after the run of the algorithm

import utils

import matplotlib.pyplot as plt

plt.figure(figsize=(12, 8))
utils.plot_experiments(
    directory="hw02/partition",
    exp_ids=[
        "default",
        "tournament-elitism",
        # "tournament",
        # "elitism",
        # "swap-tournament-elitism",
        "greedy-tournament-elitism",
        "multi_mutation04-02-tournament-elitism",
        # "greedy03-tournament-elitism",
        # "greedy03-02-tournament-elitism",
        # "tournament-multi_cross-elitism",
        # "swap-uniform_cross-elitism",
        # "tournament-elitism-swap",
        # "tournament-uniform_cross-elitism",
        # "uniform_cross-elitism",
    ],
)
plt.show()
