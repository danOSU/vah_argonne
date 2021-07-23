import numpy as np
import os

def generate_input_file(parameter_values):

    print(parameter_values)
    # read in the model file
    with open('generate_module_input_files_MAP_adjust_N_w_VAH_PTMA.py',"r") as f:
        data_ar = f.readlines()
    data = np.array(data_ar)

    # line numbers for where the parametrs are
    key_to_line={"Pb_Pb":12,
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
    
    df_design_keys = ["Pb_Pb", "Mean", "Width", "Dist", "Flactutation", "Temp", "Kink", "eta_s", "Slope_low", "Slope_high", "Max", "Temp_peak", "Width_peak", "Asym_peak", "R"]
    no_p = 0
    for param in df_design_keys:
        print(param)
        pos= key_to_line[param]
        data_new = data.copy()
        old_line = data[pos].split()
        new_line = old_line
        new_line[2] = str(parameter_values[0][no_p])
        data_new[pos] = " ".join(new_line)
        print(data[pos])
        print(data_new[pos])
        no_p += 1

    with open(f'generate_module_input_files_VAH_PTMA.py','w+') as f:
        f.writelines(data_new)
    os.system(f'python generate_module_input_files_VAH_PTMA.py')
    
    
def sim_vah(H, persis_info, sim_specs, _):
    # underscore for internal/testing arguments
    
    # Generate std input file
    generate_input_file(H['x'])
    
    # Execute the code
 
    
    # Read the output files
    files = ['frescox_temp_input-std.xsum']
    outs = []
    for file in files:
        with open(file) as f:
            content = f.readlines()
            outs.append(content)
    
    # Get the corresponding outputs
    x, y = [], []
    for out in outs:
        for idline, line in enumerate(out):
            x.append(float(line.split()[0]))
            y.append(float(line.split()[1]))
 

    # Create an output array of length rho
    out = np.zeros(1, dtype=sim_specs['out'])

    # Assign cross section as an output
    out['crosssection'] = y
    out['angle'] = x

    # Send back our output and persis_info
    return out, persis_info


