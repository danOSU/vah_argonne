import pandas as pd
import os
import numpy as np
#import Exploration/initial_design.py
df_design = pd.read_csv('design_20210829.txt', delimiter = ' ')
df_design = df_design.drop(columns='tau_initial')
print(df_design.keys())
#sh /home/ac.liyanage/vah_run_events/find_events_did_not_run $job /home/ac.liyanage/vah_run_events/$1 
#read in the model file
with open('generate_module_input_files_MAP_adjust_N_w_VAH_PTMA.py',"r") as f:
    data_ar = f.readlines()
data = np.array(data_ar)


#The line numbers for where the parametrs are
key_to_line={"Pb_Pb":13,
             "Mean":16,
             "Width":19,
             "Dist":20,
             "Flactutation":17,
             "Temp":33,
             "Kink":25,
             "eta_s":28,
             "Slope_low":26,
             "Slope_high":27,
             "Max":29,
             "Temp_peak":30,
             "Width_peak":31,
             "Asym_peak":32,
             "R":35
}

#This make a new lines array with the new design point keeping everything else as in the model input files geerating script.

def make_new_script(design_point):
    data_new=[]
    for param in df_design.keys():
        print(param)
        pos= key_to_line[param]
        data_new = data
        old_line = data[pos].split()
        new_line = old_line
        new_line[2] = str(df_design[param][design_point])
        data_new[pos] = " ".join(new_line)+'\n'
        #print(data[pos])
        #print(data_new[pos])
    print(data_new)
    return data_new

#Make a folder for each design point with corresponding input file

for i in range(0,500):
    new_file = make_new_script(i)
    os.makedirs(f"design/{i}/parameters", exist_ok=True)
    os.chdir(f"design/{i}")
    #os.makedirs(f"design/{i}/param", exist_ok=True)
    with open(f'generate_module_input_files_VAH_PTMA_{i}.py','w+') as f:
        f.writelines(new_file)
        #print(new_file)
    os.system(f'python generate_module_input_files_VAH_PTMA_{i}.py')
    os.chdir("../../")
