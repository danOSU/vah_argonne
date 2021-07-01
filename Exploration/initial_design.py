import numpy as np
import pandas as pd
from smt.sampling_methods import LHS
import seaborn as sns
from datetime import datetime

# read the design
def read_design(filename='design_20210627.txt'):
    # read from txt
    df_design = pd.read_csv(filename, delimiter = ' ')
    return df_design

df_design = read_design()

# observe pair-plot
sns.pairplot(df_design)

# code to create a new design
# define limits
xlimits = np.array([[10, 30],
                    [-0.7, 0.7],
                    [0.5, 1.5],
                    [0, 1.7**3],
                    [0.3, 2],
                    [0.135, 0.165],
                    [0.13, 0.3],
                    [0.01, 0.2],
                    [-2, 1],
                    [-1, 2],
                    [0.01, 0.25],
                    [0.12, 0.3],
                    [0.025, 0.15],
                    [-0.8, 0.8],
                    [0.3, 1],
                    [0.05, 0.5]])

# obtain sampling object
sampling = LHS(xlimits=xlimits)
num = 500
x = sampling(num)
print(x.shape)

# convert data into data frame
df = pd.DataFrame(x, columns = ['Pb_Pb',
                                'Mean',
                                'Width',
                                'Dist',
                                'Flactutation',
                                'Temp',
                                'Kink',
                                'eta_s',
                                'Slope_low',
                                'Slope_high',
                                'Max',
                                'Temp_peak',
                                'Width_peak',
                                'Asym_peak',
                                'R',
                                'tau_initial'])

# observe pair-plot
sns.pairplot(df)

# write design points into a file
date = datetime.now().strftime('%Y%m%d') 
filename = f"design_{date}" + '.txt'
df.to_csv(filename, header=True, index=None, sep=' ', mode='a')

