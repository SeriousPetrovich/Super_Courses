import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats

# ���������� ������
titanic_data = pd.read_csv('train.csv')
titanic_data = titanic_data[titanic_data.Age.isnull() == False]
ages = titanic_data.Age

n = ages.shape[0] # ������ �������

N_int = 8 # ���������� ���������� + 1
n_j = np.zeros(N_int - 1) # ���������� ���������� � j-� ��������� 

intervals = np.linspace(0,80, N_int) # ���������� �� ���������

# ������� n_j

for i in range(N_int - 1):
    n_j[i] = len(ages[(ages > intervals[i]) & (ages <= intervals[i + 1])])

# �������� �������� ���������� ����������
    
if np.prod(n_j >= 5):
    print('��������� ����� ��������� �� ������ 5')
    flag = 1
else:
    print('��������� ����� ��������� ������ 5')
    flag = 0
    
# ���� �������� ������ �������, ��:    

mean = ages.mean()
var  = ages.var()
std  = np.sqrt(var)

if flag:
    
    # ������� ����������� ��������� ���������� � j-�� ��������
    
    p_j_skew_norm = np.zeros(N_int - 1)
    p_j_norm      = np.zeros(N_int - 1)
    p_j_chi2      = np.zeros(N_int - 1)
            
    for i in range(N_int - 1):
        p_j_skew_norm[i] = stats.skewnorm.cdf(intervals[i + 1], *stats.skewnorm.fit(ages)) - stats.skewnorm.cdf(intervals[i], *stats.skewnorm.fit(ages))
        p_j_norm[i]      = stats.norm.cdf(intervals[i + 1], *stats.norm.fit(ages)) - stats.norm.cdf(intervals[i], *stats.norm.fit(ages))
        p_j_chi2[i]      = stats.chi2.cdf(intervals[i + 1], *stats.chi2.fit(ages)) - stats.chi2.cdf(intervals[i], *stats.chi2.fit(ages))

    # ������� ������������ �������� �������� ��-�������

    chi2_skew_norm, chi2_norm, chi2_chi2 = 0, 0, 0

    for i in range(N_int - 1):
        chi2_skew_norm += ((n_j[i] - n*p_j_skew_norm[i])**2)/(n*p_j_skew_norm[i])
        chi2_norm      += ((n_j[i] - n*p_j_norm[i])**2)/(n*p_j_norm[i])
        chi2_chi2      += ((n_j[i] - n*p_j_chi2[i])**2)/(n*p_j_chi2[i])
    print('chi2:')
    chi2_dict = {'skew_norm' : chi2_skew_norm,
                 'norm'      : chi2_norm,
                 'chi2'      : chi2_chi2}

    print(chi2_dict)


# ������������

x = range(81)

# ������ ������� ������������

chi2_dots = stats.chi2.rvs(*stats.chi2.fit(ages), size=1000000)
norm_dots = stats.norm.rvs(*stats.norm.fit(ages), size=1000000)
skewnorm_dots = stats.skewnorm.rvs(*stats.skewnorm.fit(ages), size=1000000)

sns.distplot(ages, hist=False, kde=True, kde_kws={'shade': True, 'linewidth': 5}, label = 'Ages (�������)')
sns.distplot(norm_dots, hist=False, kde=True, kde_kws={'shade': False}, color='C1', label='Norm')
sns.distplot(skewnorm_dots, hist=False, kde=True, kde_kws={'shade': False}, color='C2', label='Skew Norm')
sns.distplot(chi2_dots, hist=False, kde=True, kde_kws={'shade': False}, color='C3', label='chi2')
# Means
plt.axvline(x=skewnorm_dots.mean(), color='C2', linestyle='-')
plt.axvline(x=norm_dots.mean(), color='C1', linestyle='-')
plt.axvline(x=chi2_dots.mean(), color='C3', linestyle='-')


# ������ ������� ������������

# y_skew_pdf = stats.skewnorm.pdf(x, *stats.skewnorm.fit(ages))
# y_pdf      = stats.norm.pdf(x, *stats.norm.fit(ages))
# y_chi2     = stats.chi2.pdf(x, *stats.chi2.fit(ages))

# sns.distplot(ages, hist=True, kde=True, kde_kws={'shade': True, 'linewidth': 5}, label = 'Ages (�������)')
# plt.plot(x, y_pdf, color='C1', label='Norm')
# plt.plot(x, y_skew_pdf, color='C2', label='Skew Norm')
# plt.plot(x, y_chi2, color='C3', label='chi2')

# 

# Mean
plt.axvline(x=mean, color='b', linestyle='-')
# Intervals
for i in intervals:
    plt.axvline(x=i, color='#1fa7ff', linestyle='--')

plt.gca().set_xlim([0, 80])
plt.legend()
plt.show()