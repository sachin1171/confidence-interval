###################basic statstics part 1#######
############probelm 2########
#Check whether the data follows normal distribution 
#a) Check whether the MPG of Cars follows Normal Distribution Dataset: Cars.csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
cars=pd.read_csv('C:/Users/usach/Desktop/confidence/Cars.csv')
cars

sns.distplot(cars.MPG, label='Cars-MPG')
plt.xlabel('MPG')
plt.ylabel('Density')
plt.legend();

cars.MPG.mean()

cars.MPG.median()
#Inference: MPG of Cars does follow normal distribution approximately
#(as mean and median are approx. same)

#b)Check Whether the Adipose Tissue (AT) and Waist Circumference(Waist)
#from wc-at data set follows Normal Distribution Dataset: wc-at.csv
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

wcat=pd.read_csv('C:/Users/usach/Desktop/confidence/wc-at.csv')
wcat

# plotting distribution for Waist Circumference (Waist) 
sns.distplot(wcat.Waist)
plt.ylabel('density');

# plotting distribution for Adipose Tissue (AT) 
sns.distplot(wcat.AT)
plt.ylabel('density');

# WC
wcat.Waist.mean() , wcat.Waist.median()
# AT
wcat.AT.mean() , wcat.AT.median()
#Inference: Both the Adipose Tissue (AT) and Waist Circumference(Waist) data set 
#do follow the normal distribution approximately 
#(as mean and median of both the data are approximately same)

####################problem 3 ######################
#Calculate the Z scores of 90% confidence interval,94% confidence interval, 
#60% confidence interval.
from scipy import stats
from scipy.stats import norm
#Z-score of 90% confidence interval 
stats.norm.ppf(0.95)

# Z-score of 94% confidence interval
stats.norm.ppf(0.97)

# Z-score of 60% confidence interval
stats.norm.ppf(0.8)

#######################problem 4########################
#Calculate the t scores of 95% confidence interval, 96% confidence interval,
# 99% confidence interval for sample size of 25
from scipy import stats
from scipy.stats import norm
# t scores of 95% confidence interval for sample size of 25
stats.t.ppf(0.975,24)  # df = n-1 = 24

# t scores of 96% confidence interval for sample size of 25
stats.t.ppf(0.98,24)

# t scores of 99% confidence interval for sample size of 25
stats.t.ppf(0.995,24)

