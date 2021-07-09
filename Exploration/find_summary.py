import os
import re
import pandas as pd

summary={}
for i in range(0,500):
    for root, dirs, files in os.walk(f'{i}/'):
        print(f'rooots {root} dirs {dirs} files {files} \n')
        for file in files:
            if file.contains('failed')==True:
                print(f'{i} has failed events')
            elif file.contains('crashed')==True:
                print(f'{i} has crashed events')
            elif file.contains('success')==True:
                with open(file) as f:
                    lines = f.readlines()
                    if len(lines) == 10:
                        print(f'{i} design point has all {len(lines)} events')
                    else:
                        print(f'{i} design point is missing {10-len(lines)} events')
                        summary[i]=len(lines)
            else:
                print(f'{i} something terible happened')
                
        break;
summary_df= pd.DataFrame(list(summary.items(), columns = ['design','events'])
summary_df.to_csv('summary')