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

input_file1 = 'results/variance_age_80_90_vs_No_a_m.csv'
input_file2 = 'results/variance_gender_Female_vs_Male_a_m.csv'
input_file3 = 'results/variance_insulin_Steady_vs_No_a_m.csv'
input_file4 = 'results/variance_readmitted_NO_vs_Yes_a_m.csv'

output_plot = 'variance_a_m_0_missing'

# ===============================================================
# IDEAL VS STANDARD
percent = 0
percent_0 = 0


df = pd.read_csv(input_file1, names=['percentage','k','variance'])

#Jaccard
k5j = df[(df['k'] == 5) & (df['percentage'] == percent)]
k5j = k5j['variance']
k10j = df[(df['k'] == 10) & (df['percentage'] == percent)]
k10j = k10j['variance']

k5j = list(mean_confidence_interval(k5j))
k5j.insert(0,5)
#print(k5j)
#k5j.insert(1,'Jaccard')
k10j = list(mean_confidence_interval(k10j))
k10j.insert(0,10)
#k10j.insert(1,'Jaccard')

k5j0 = df[(df['k'] == 5) & (df['percentage'] ==percent_0)]
k5j0 = k5j0['variance']
k10j0 = df[(df['k'] == 10) & (df['percentage'] ==percent_0)]
k10j0 = k10j0['variance']

k5j0 = list(mean_confidence_interval(k5j0))
k5j0.insert(0,5)
#print(k5j)
#k5j.insert(1,'Jaccard')
k10j0 = list(mean_confidence_interval(k10j0))
k10j0.insert(0,10)
#k10j.insert(1,'Jaccard')

df = pd.DataFrame([k5j, k10j])
df.columns = ['k','mean','lb','ub']

mean0 = df['mean']
ub0 = df['ub']
lb0 = df['lb']
#print(ub0)

dfx = pd.DataFrame([k5j0, k10j0])
dfx.columns = ['k','mean','lb','ub']

mean00 = dfx['mean']
ub00 = dfx['ub']
lb00 = dfx['lb']
#print(ub0)







df1 = pd.read_csv(input_file2, names=['percentage','k','variance'])

k5r = df1[(df1['k'] == 5) & (df1['percentage'] == percent)]
k5r = k5r['variance']
k10r = df1[(df1['k'] == 10) & (df1['percentage'] == percent)]
k10r = k10r['variance']


k5r = list(mean_confidence_interval(k5r))
k5r.insert(0,5)
#k5r.insert(1,'RBO 0.95')
k10r = list(mean_confidence_interval(k10r))
k10r.insert(0,10)


k5r0 = df1[(df1['k'] == 5) & (df1['percentage'] ==percent_0)]
k5r0 = k5r0['variance']
k10r0 = df1[(df1['k'] == 10) & (df1['percentage'] ==percent_0)]
k10r0 = k10r0['variance']

k5r0 = list(mean_confidence_interval(k5r0))
k5r0.insert(0,5)
#k5r.insert(1,'RBO 0.95')
k10r0 = list(mean_confidence_interval(k10r0))
k10r0.insert(0,10)
#k10r.insert(1,'RBO 0.95')

df1 = pd.DataFrame([k5r, k10r])
df1.columns = ['k','mean','lb','ub']

mean1 = df1['mean']
ub1 = df1['ub']
lb1 = df1['lb']

df1x = pd.DataFrame([k5r0, k10r0])
df1x.columns = ['k','mean','lb','ub']

mean10 = df1x['mean']
ub10 = df1x['ub']
lb10 = df1x['lb']



df3 = pd.read_csv(input_file3, names=['percentage','k','variance'])

#Jaccard
k5jj = df3[(df3['k'] == 5) & (df3['percentage'] == percent)]
k5jj = k5jj['variance']
k10jj = df3[(df3['k'] == 10) & (df3['percentage'] == percent)]
k10jj = k10jj['variance']

k5jj = list(mean_confidence_interval(k5jj))
k5jj.insert(0,5)
#print(k5jj)
#k5jj.insert(1,'Jaccard')
k10jj = list(mean_confidence_interval(k10jj))
k10jj.insert(0,10)
#k10jj.insert(1,'Jaccard')

k5jj0 = df3[(df3['k'] == 5) & (df3['percentage'] ==percent_0)]
k5jj0 = k5jj0['variance']
k10jj0 = df3[(df3['k'] == 10) & (df3['percentage'] ==percent_0)]
k10jj0 = k10jj0['variance']

k5jj0 = list(mean_confidence_interval(k5jj0))
k5jj0.insert(0,5)
#print(k5jj)
#k5jj.insert(1,'Jaccard')
k10jj0 = list(mean_confidence_interval(k10jj0))
k10jj0.insert(0,10)
#k10jj.insert(1,'Jaccard')

df3 = pd.DataFrame([k5jj, k10jj])
df3.columns = ['k','mean','lb','ub']

mean3 = df3['mean']
ub3 = df3['ub']
lb3 = df3['lb']
#print(ub0)

df3x = pd.DataFrame([k5jj0, k10jj0])
df3x.columns = ['k','mean','lb','ub']

mean30 = df3x['mean']
ub30 = df3x['ub']
lb30 = df3x['lb']
#print(ub0)



df4 = pd.read_csv(input_file4, names=['percentage','k','variance'])

k5rr = df4[(df4['k'] == 5) & (df4['percentage'] == percent)]
k5rr = k5rr['variance']
k10rr = df4[(df4['k'] == 10) & (df4['percentage'] == percent)]
k10rr = k10rr['variance']


k5rr = list(mean_confidence_interval(k5rr))
k5rr.insert(0,5)
#k5rr.insert(1,'RBO 0.95')
k10rr = list(mean_confidence_interval(k10rr))
k10rr.insert(0,10)


k5rr0 = df4[(df4['k'] == 5) & (df4['percentage'] ==percent_0)]
k5rr0 = k5rr0['variance']
k10rr0 = df4[(df4['k'] == 10) & (df4['percentage'] ==percent_0)]
k10rr0 = k10rr0['variance']

k5rr0 = list(mean_confidence_interval(k5rr0))
k5rr0.insert(0,5)
#k5rr.insert(1,'RBO 0.95')
k10rr0 = list(mean_confidence_interval(k10rr0))
k10rr0.insert(0,10)
#k10rr.insert(1,'RBO 0.95')

df4 = pd.DataFrame([k5rr, k10rr])
df4.columns = ['k','mean','lb','ub']

mean4 = df4['mean']
ub4 = df4['ub']
lb4 = df4['lb']

df4x = pd.DataFrame([k5rr0, k10rr0])
df4x.columns = ['k','mean','lb','ub']

mean40 = df4x['mean']
ub40 = df4x['ub']
lb40 = df4x['lb']


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
ax.plot(mean00, lw = 1, color = '#539caf', alpha = 1, label = 'q1: age = (80-90) vs !(80-90)', marker='x', linestyle='-.', linewidth=2, markersize=12)
ax.plot(mean10, lw = 1, color = '#b65332', alpha = 1, label = 'q2: gender = Female vs Male', marker='<', linestyle='-', linewidth=2, markersize=12)
ax.plot(mean30, lw = 1, color = '#5be19a', alpha = 1, label = 'q3: insulin = Steady vs !Steady', marker='o', linestyle='-', linewidth=2, markersize=12)
ax.plot(mean40, lw = 1, color = '#ece554', alpha = 1, label = 'q4: readmitted = NO vs !NO', marker='s', linestyle='--', linewidth=2, markersize=12)

#ax.plot(mean00, lw = 1, color = '#5be19a', alpha = 1, label = 'q1: age = (80-90) vs !(80-90) 0 % missing', marker='o', linestyle='-', linewidth=2, markersize=12)
#ax.plot(mean10, lw = 1, color = '#ece554', alpha = 1, label = 'q2: gender = Female vs Male 0 % missing', marker='s', linestyle='--', linewidth=2, markersize=12)

# Shade the confidence interval
ax.fill_between(t, lb00, ub00, color = '#539caf', alpha = 0.4)
ax.fill_between(t, lb10, ub10, color = '#b65332', alpha = 0.4)
ax.fill_between(t, lb30, ub30, color = '#5be19a', alpha = 0.4)
ax.fill_between(t, lb40, ub40, color = '#e6a3ba', alpha = 0.4)

#ax.fill_between(t, lb00, ub00, color = '#5be19a', alpha = 0.4)
#ax.fill_between(t, lb10, ub10, color = '#e6a3ba', alpha = 0.4)

# Label the axes and provide a title
ax.set_title("Impact of k 0% missing, 95% CI")
ax.set_xlabel("k")
ax.set_ylabel("avg gap topk set")
x = [5, 10]
xi = list(range(len(x)))
plt.xticks(xi, x)
# Display legend
#ax.set_ylim(ymin=0.0)
#ax.set_ylim(ymax=0.1)

ax.legend(loc='best')

plt.savefig('plot/' + output_plot + '.svg', format="svg", dpi = 1000)
plt.savefig('plot/' + output_plot + '.png')
plt.show()



