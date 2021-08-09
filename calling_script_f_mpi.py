import os
import numpy as np
from generator_f import gen_random_sample
from simulator_f import sim_vah

# Import libEnsemble modules
from libensemble.libE import libE
from libensemble.manager import ManagerException
from libensemble.tools import parse_args, save_libE_output, add_unique_random_streams
from libensemble import libE_logger

USE_BALSAM = False
PERSIS_GEN = False

if PERSIS_GEN:
    from libensemble.gen_funcs.persistent_uniform_sampling import persistent_uniform as gen_f
    from libensemble.alloc_funcs.start_only_persistent import only_persistent_gens as alloc_f
else:
    from libensemble.gen_funcs.sampling import uniform_random_sample as gen_f
    from libensemble.alloc_funcs.give_sim_work_first import give_sim_work_first as alloc_f


libE_logger.set_level('INFO')  # INFO is now default

# nworkers, is_manager, libE_specs, _ = parse_args()
#if is_manager:
#    print('\nRunning with {} workers\n'.format(nworkers))

nworkers = 4
libE_specs = {'nworkers': nworkers, 'comms': 'local'}

# Create executor and register sim to it.
if USE_BALSAM:
    from libensemble.executors.balsam_executor import BalsamMPIExecutor
    exctr = BalsamMPIExecutor()  # Use allow_oversubscribe=False to prevent oversubscription
else:
    from libensemble.executors.mpi_executor import MPIExecutor
    exctr = MPIExecutor()  # Use allow_oversubscribe=False to prevent oversubscription
#exctr.register_calc(full_path=sim_app, calc_type='sim')

# Note: Attributes such as kill_rate are to control forces tests, this would not be a typical parameter.

# State the objective function, its arguments, output, and necessary parameters (and their sizes)
gen_specs = {'gen_f': gen_random_sample,   # Our generator function
             'out': [('x', float, (15,))],  # gen_f output (name, type, size)
             'user': {
                 'lower': np.array([10, -0.7, 0.5, 0, 0.3, 0.135, 0.13, 0.01, -2, -1, 0.01, 0.12, 0.025, -0.8, 0.3]),  # lower boundary for random sampling
                 'upper': np.array([30, 0.7, 1.5, 1.7**3, 2, 0.165, 0.3, 0.2, 1, 2, 0.25, 0.3, 0.15, 0.8, 1]),  # upper boundary for random sampling
                 'gen_batch_size': 6        # number of x's gen_f generates per call
                 }
             }

sim_specs = {'sim_f': sim_vah,       # Our simulator function
             'in': ['x'],                  # Input field names. 'x' from gen_f output
             'out': [('rho', float, (401,)),
                     ('xrho', float, (401,))]}  # sim_f output. Executes the fortran code

if PERSIS_GEN:
    alloc_specs = {'alloc_f': alloc_f, 'out': [('given_back', bool)]}
else:
    alloc_specs = {'alloc_f': alloc_f,
                   'out': [('allocated', bool)],
                   'user': {'batch_mode': True,    # If true wait for all sims to process before generate more
                            'num_active_gens': 1}  # Only one active generator at a time
                   }

libE_specs['sim_dirs_make'] = True     # Separate each sim into a separate directory
libE_specs['gen_dirs_make'] = True     # Separate each gen into a separate directory
libE_specs['profile'] = False    # Whether to have libE profile on (default False)
libE_specs['sim_dir_copy_files'] = [os.path.join(os.getcwd(), 'generate_module_input_files_MAP_adjust_N_w_VAH_PTMA.py')]

# Maximum number of simulations
sim_max = 6
exit_criteria = {'sim_max': sim_max}

# Create a different random number stream for each worker and the manager
persis_info = {}
persis_info = add_unique_random_streams(persis_info, nworkers + 1)

H, persis_info, flag = libE(sim_specs, gen_specs, exit_criteria,
                                persis_info=persis_info,
                                alloc_specs=alloc_specs,
                                libE_specs=libE_specs)


