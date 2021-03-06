import sys
import numpy as np
import scipy.stats as stats
import scipy
import matplotlib.pyplot as plt


def run_task(args):
    if args:
        if '2' in args[0]:
            filename = 'tasks/solutions/task2_costs.txt'
            fig = 'tasks/solutions/task2_cost_distribution.png'
            with open(filename) as f:
                costs = f.read()
            cost_list = [float(c) for c in costs.strip('][').split(',')]  # 1000 costs
            cost_list = np.array(cost_list)

            # remove the outliers
            cost_list = cost_list[cost_list > 3700000]  # ~998/1000 non-outliers
            bins = 60
            hist, edges = np.histogram(cost_list, bins)
            x = np.linspace(min(cost_list),max(cost_list),bins)

            y = [float(h) / np.size(cost_list) for h in hist]
            plt.scatter(x,y)  # create frequency plot

            a, loc, scale = scipy.stats.lognorm.fit(cost_list, loc=5345771.6318737976, scale=22690.626344507498)
            print(f"\nThe parameters for shape, loc and scale are {a}, {loc}, and {scale}.")
            fitted_data = scipy.stats.lognorm.pdf(x, a, loc, scale)
            scale_param = (max(cost_list) - min(cost_list)) / bins
            plt.plot(x, scale_param * fitted_data, color='red')
            plt.savefig(fig)

            # Calculate VAR
            print("\nThe VAR at 95 percent confidence is", stats.lognorm.ppf(0.95, a, loc, scale),"\n")

        elif '3' in args[0]:
            filename = 'tasks/solutions/task3_costs.txt'
            with open(filename) as f:
                costs = f.read()
            cost_list = [float(c) for c in costs.strip('][').split(',')]  # 1000 costs
            listed_cost = sorted(np.array(cost_list))
            listed_cost = sorted(cost_list)
            shape = len(cost_list)
            VAR = listed_cost[int(shape * 0.95)]

            # Calculate VAR
            print(f"\nThe VAR at 95 percent confidence is {VAR}\n")


run_task(sys.argv[1:])