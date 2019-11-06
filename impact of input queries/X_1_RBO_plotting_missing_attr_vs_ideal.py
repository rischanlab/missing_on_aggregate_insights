import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import scipy.stats
def mean_confidence_interval(data, confidence=0.95):
    a = 1.0 * np.array(data)
    n = len(a)
    m, se = np.mean(a), scipy.stats.sem(a)
    h = se * scipy.stats.t.ppf((1 + confidence) / 2., n-1)
    return m, m-h, m+h

input_file1 = 'results/age_missing_attributes_vs_ideal.csv'
input_file2 = 'results/gender_missing_attributes_vs_ideal.csv'
input_file3 = 'results/insulin_missing_attributes_vs_ideal.csv'
input_file4 = 'results/readmitted_missing_attributes_vs_ideal.csv'

output_plot = 'rbo_missing_attributes_vs_ideal'

# ===============================================================
# IDEAL VS STANDARD

df1 = pd.read_csv(input_file1, names=['percentage','k','RBO','Jaccard'])

percent = 10
#[5, 10, 15, 20, 100, 384]

k10j = df1[(df1['k'] == 5) & (df1['percentage'] == percent)]
k10j = k10j['RBO']

k20j = df1[(df1['k'] == 10) & (df1['percentage'] == percent)]
k20j = k20j['RBO']

k100j = df1[(df1['k'] == 12) & (df1['percentage'] == percent)]
k100j = k100j['RBO']



k10j = list(mean_confidence_interval(k10j))
k10j.insert(0,5)
k10j.insert(1,'Jaccard')

k20j = list(mean_confidence_interval(k20j))
k20j.insert(0,10)
k20j.insert(1,'Jaccard')

k100j = list(mean_confidence_interval(k100j))
k100j.insert(0,12)
k100j.insert(1,'Jaccard')


df1 = pd.DataFrame([k10j,k20j, k100j])
df1.columns = ['k','measurement','mean','lb','ub']

mean1 = df1[df1['measurement'] == 'Jaccard'].reset_index()
mean1 = mean1['mean']
ub1 = df1[df1['measurement'] == 'Jaccard'].reset_index()
ub1 = ub1['ub']
lb1 = df1[df1['measurement'] == 'Jaccard'].reset_index()
lb1 = lb1['lb']


df2 = pd.read_csv(input_file2, names=['percentage','k','RBO','Jaccard'])

percent = 10

k10j = df2[(df2['k'] == 5) & (df2['percentage'] == percent)]
k10j = k10j['RBO']

k20j = df2[(df2['k'] == 10) & (df2['percentage'] == percent)]
k20j = k20j['RBO']

k100j = df2[(df2['k'] == 12) & (df2['percentage'] == percent)]
k100j = k100j['RBO']



k10j = list(mean_confidence_interval(k10j))
k10j.insert(0,5)
k10j.insert(1,'Jaccard')

k20j = list(mean_confidence_interval(k20j))
k20j.insert(0,10)
k20j.insert(1,'Jaccard')

k100j = list(mean_confidence_interval(k100j))
k100j.insert(0,12)
k100j.insert(1,'Jaccard')


df2 = pd.DataFrame([k10j,k20j, k100j])
df2.columns = ['k','measurement','mean','lb','ub']

mean2 = df2[df2['measurement'] == 'Jaccard'].reset_index()
mean2 = mean2['mean']
ub2 = df2[df2['measurement'] == 'Jaccard'].reset_index()
ub2 = ub2['ub']
lb2 = df2[df2['measurement'] == 'Jaccard'].reset_index()
lb2 = lb2['lb']



df3 = pd.read_csv(input_file3, names=['percentage','k','RBO','Jaccard'])

percent = 10
#[5, 10, 15, 20, 100, 384]

k10j = df3[(df3['k'] == 5) & (df3['percentage'] == percent)]
k10j = k10j['RBO']

k20j = df3[(df3['k'] == 10) & (df3['percentage'] == percent)]
k20j = k20j['RBO']

k100j = df3[(df3['k'] == 12) & (df3['percentage'] == percent)]
k100j = k100j['RBO']


k10j = list(mean_confidence_interval(k10j))
k10j.insert(0,5)
k10j.insert(1,'Jaccard')

k20j = list(mean_confidence_interval(k20j))
k20j.insert(0,10)
k20j.insert(1,'Jaccard')

k100j = list(mean_confidence_interval(k100j))
k100j.insert(0,12)
k100j.insert(1,'Jaccard')


df3 = pd.DataFrame([k10j,k20j, k100j])
df3.columns = ['k','measurement','mean','lb','ub']

mean3 = df3[df3['measurement'] == 'Jaccard'].reset_index()
mean3 = mean3['mean']
ub3 = df3[df3['measurement'] == 'Jaccard'].reset_index()
ub3 = ub3['ub']
lb3 = df3[df3['measurement'] == 'Jaccard'].reset_index()
lb3 = lb3['lb']

df4 = pd.read_csv(input_file4, names=['percentage','k','RBO','Jaccard'])

percent = 10

k10j = df4[(df4['k'] == 5) & (df4['percentage'] == percent)]
k10j = k10j['RBO']

k20j = df4[(df4['k'] == 10) & (df4['percentage'] == percent)]
k20j = k20j['RBO']

k100j = df4[(df4['k'] == 12) & (df4['percentage'] == percent)]
k100j = k100j['RBO']



k10j = list(mean_confidence_interval(k10j))
k10j.insert(0,5)
k10j.insert(1,'Jaccard')

k20j = list(mean_confidence_interval(k20j))
k20j.insert(0,10)
k20j.insert(1,'Jaccard')

k100j = list(mean_confidence_interval(k100j))
k100j.insert(0,12)
k100j.insert(1,'Jaccard')


df4 = pd.DataFrame([k10j,k20j, k100j])
df4.columns = ['k','measurement','mean','lb','ub']

mean4 = df4[df4['measurement'] == 'Jaccard'].reset_index()
mean4 = mean4['mean']
ub4 = df4[df4['measurement'] == 'Jaccard'].reset_index()
ub4 = ub4['ub']
lb4 = df4[df4['measurement'] == 'Jaccard'].reset_index()
lb4 = lb4['lb']

# Set some parameters to apply to all plots. These can be overridden
# in each plot if desired
import matplotlib
# Plot size to 14" x 7"
matplotlib.rc('figure', figsize = (14, 14))
# Font size to 14
matplotlib.rc('font', size = 25)
# Do not display top and right frame lines
matplotlib.rc('axes.spines', top = False, right = False)
# Remove grid lines
matplotlib.rc('axes', grid = False)
# Set backgound color to white
matplotlib.rc('axes', facecolor = 'white')


t = np.arange(len(mean1))

_, ax = plt.subplots()
# Plot the data, set the linewidth, color and transparency of the
# line, provide a label for the legend
ax.plot(mean1, lw = 1, color = '#539caf', alpha = 1, label = 'q1: age = (80-90) vs !(80-90)', marker='x', linestyle='-.', linewidth=2, markersize=12)
ax.plot(mean2, lw = 1, color = '#b65332', alpha = 1, label = 'q2: gender = Female vs Male', marker='<', linestyle='-', linewidth=2, markersize=12)
ax.plot(mean3, lw = 1, color = '#5be19a', alpha = 1, label = 'q3: insulin = Steady vs !Steady', marker='o', linestyle='-', linewidth=2, markersize=12)
ax.plot(mean4, lw = 1, color = '#ece554', alpha = 1, label = 'q4: readmitted = NO vs !NO', marker='s', linestyle='--', linewidth=2, markersize=12)

# Shade the confidence interval
ax.fill_between(t, lb1, ub1, color = '#539caf', alpha = 0.4)
ax.fill_between(t, lb2, ub2, color = '#b65332', alpha = 0.4)
ax.fill_between(t, lb3, ub3, color = '#5be19a', alpha = 0.4)
ax.fill_between(t, lb4, ub4, color = '#e6a3ba', alpha = 0.4)
# Label the axes and provide a title
ax.set_title("Impact of k on Effectiveness, 95% CI, 10 % A missing")
ax.set_xlabel("k")
ax.set_ylabel("Effectiveness - Missing on Attributes to Ideal")
x = [5, 10, 12]
xi = list(range(len(x)))
plt.xticks(xi, x)
# Display legend
ax.set_ylim(ymin=0.0)
ax.set_ylim(ymax=1.1)

ax.legend(loc='best')

plt.savefig('plot/' + output_plot + '.svg', format="svg", dpi = 1000)
plt.savefig('plot/' + output_plot + '.png')
plt.show()
