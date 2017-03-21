#Used to calculate z score and p values

from scipy.stats import zscore
from scipy.stats import norm

accuracy1 = [0.172307692, 0.255384615, 0.178461538, 0.172307692, 0.138461538, 
             0.193846154, 0.147692308, 0.138461538, 0.24, 0.138461538]

zscore1 = zscore(accuracy1)
#print zscore1
p_values1 = norm.sf(abs(zscore1))
#print p_values1

accuracy3 = [0.895384615, 0.861538462, 0.892307692, 0.886153846, 0.889230769, 
             0.867692308, 0.76, 0.855384615, 0.572307692, 0.892307692]
zscore3 = zscore(accuracy3)
#print zscore3
p_values3 = norm.sf(abs(zscore3))
#print p_values3

accuracy2 = [0.875924404273, 0.907364961294, 0.776932058989, 0.899450763309,
             0.905072871167, 0.905332353068, 0.669679539852, 0.8593175626, 0.893136703715, 0.904424166414]
zscore2 = zscore(accuracy2)
# print zscore2
p_values2 = norm.sf(abs(zscore2))
#print p_values2

accuracy1_2 = [0.749125874, 0.859702797, 0.702797203, 0.85270979, 0.859702797, 
             0.856206294, 0.579982517, 0.798513986, 0.839160839, 0.857517483]
zscore1_2 = zscore(accuracy1_2)
#print zscore1_2

p_values1_2 = norm.sf(abs(zscore1_2))
#print p_values1_2

accuracy3_2 = [0.968531469, 0.946241259, 0.956293706, 0.972027972, 0.97027972, 
               0.964597902, 0.693181818, 0.958916084, 0.963286713, 0.968968531]
zscore3_2 = zscore(accuracy3_2)
print zscore3_2
p_values3_2 = norm.sf(abs(zscore3_2))
print p_values3_2

