#!/usr/bin/env python

# Parameter files for TRENTo + VH2 + iS3D2 + SMASH (PTMA = modified anisotropic distribution)

import math

js_seed = 0                                                                           # SMASH seed (0 = clock time seed)

# TRENTo parameters
projectile = 'Pb'
target = 'Pb'
sqrts = 2760                                                                          # Pb+Pb sqrt(s) = 2.76 TeV
cross_section = 6.4                                                                   # partonic cross section for sqrt(s) = 2.76 TeV
normalization = 20.0																  # normalization (adjusted to increase particle yield in VAH)
cent_low = 0
cent_high = 100                                                                       # does this cover multiple centrality bins?
reduced_thickness = 0.063                                                             # p
fluct_sigma = 1.05                                                                     # sigma_k
fluct_k = 1. / (fluct_sigma**2.)                                                      # k = 1 / sigma_k^2
nucleon_width = 0.98                                                                  # w (adjusted to increase <pT>, v_n{2} in VAH)
nucleon_min_dist = 1.44                                                               # d_min (for trento, not cpu vah)


# VAH parameters
kinetic_theory_model = 0                                                              # idle parameter since running anisotropic hydro
eta_over_s_T_kink_in_GeV = 0.223                                                      # shear viscosity parameterization
eta_over_s_low_T_slope_in_GeV = -0.776
eta_over_s_high_T_slope_in_GeV = 0.37
eta_over_s_at_kink = 0.096
zeta_over_s_max = 0.133                                                                # bulk viscosity parameterization
zeta_over_s_T_peak_in_GeV = 0.12
zeta_over_s_width_in_GeV = 0.072
zeta_over_s_lambda_asymm = -0.122
T_c = 0.136                                                                            # switching temperature
freezeout_finder_period = 2															  # coarse-grains temporal resolution of freezeout surface
R = 0.03

# iS3D2 parameters
delta_f_mode = 5                                                                      # modified anisotropic distribution (PTMA)
rap_max = 2.0                                                                         # y_cut for 2+1d
min_num_hadrons = 100000                                                              # oversampling parameters
max_num_samples = 1000


# SMASH parameters
max_time_smash = 1000.0                                                               # max run time in smash [fm/c]


# Grid parameters
dx = round(0.15 * nucleon_width, 3)                                                   # lattice spacing to resolve nucleon
dy = round(0.15 * nucleon_width, 3)

L_x = 15.0                                                                            # default half grid length (should set resolve_nucleons = 0)
L_y = 15.0

nx = 1.  +  (2. * L_x) / dx                                                           # default grid points
ny = 1.  +  (2. * L_y) / dy

nx = int(math.ceil(nx))                                                               # round up integer
ny = int(math.ceil(ny))

if((nx % 2) == 0):                                                                    # adjust grid points to odd number
    nx += 1
if((ny % 2) == 0):
    ny += 1

L_x = ((nx - 1) / 2.) * dx                                                            # adjust grid length
L_y = ((nx - 1) / 2.) * dx

max_x = L_x  + 0.5 * dx                                                               # TRENTo needs a slightly larger grid
max_y = L_y  + 0.5 * dy


# make VAH directory parameters/                                                      # need to adjust Macro parameters in cpu_vah prior to compiling
hydro_file = open('parameters/hydro.properties','w')
hydro_file.write("run_hydro                  = 2"     + "\n")                         # hard coded values are fixed
hydro_file.write("tau_initial                = 0.05"  + "\n")
hydro_file.write("plpt_ratio_initial         = " + str(R)   
                 + "\n")
hydro_file.write("kinetic_theory_model       = "      + str(kinetic_theory_model)           + "\n")
hydro_file.write("temperature_etas           = 1"     + "\n")
hydro_file.write("constant_etas              = 0.2"   + "\n")
hydro_file.write("etas_min                   = 0.01"  + "\n")
hydro_file.write("etas_aL                    = "      + str(eta_over_s_low_T_slope_in_GeV)  + "\n")
hydro_file.write("etas_aH                    = "      + str(eta_over_s_high_T_slope_in_GeV) + "\n")
hydro_file.write("etas_Tk_GeV                = "      + str(eta_over_s_T_kink_in_GeV)       + "\n")
hydro_file.write("etas_etask                 = "      + str(eta_over_s_at_kink)             + "\n")
hydro_file.write("zetas_normalization_factor = "      + str(zeta_over_s_max)                + "\n")
hydro_file.write("zetas_peak_temperature_GeV = "      + str(zeta_over_s_T_peak_in_GeV)      + "\n")
hydro_file.write("zetas_width_GeV            = "      + str(zeta_over_s_width_in_GeV)       + "\n")
hydro_file.write("zetas_skew                 = "      + str(zeta_over_s_lambda_asymm)       + "\n")
hydro_file.write("freezeout_temperature_GeV  = "      + str(T_c)                            + "\n")
hydro_file.write("freezeout_finder_period    = "      + str(freezeout_finder_period)        + "\n")
hydro_file.write("flux_limiter               = 1.8"   + "\n")
hydro_file.write("energy_min                 = 1.e-1" + "\n")
hydro_file.write("pressure_min               = 1.e-3" + "\n")
hydro_file.write("regulation_scheme          = 1"     + "\n")
hydro_file.write("rho_max                    = 10.0"  + "\n")
hydro_file.close()

initial_file = open('parameters/initial.properties','w')
initial_file.write("initial_condition_type          = 5"     + "\n")                  # initial_condition_type = 5 reads in energy density from TRENTo.
initial_file.write("nucleus_A                       = 208"   + "\n")                  # won't be generating initial energy density profile
initial_file.write("nucleus_B                       = 208"   + "\n")                  # with cpu_vah so remaining parameters are idle.
initial_file.write("initial_central_temperature_GeV = 0.718" + "\n")
initial_file.write("impact_parameter                = 0.0"   + "\n")
initial_file.write("rapidity_variance               = 3.24"  + "\n")
initial_file.write("rapidity_flat                   = 4.0"   + "\n")
initial_file.write("q_gubser                        = 1.0"   + "\n")
initial_file.write("trento_normalization_GeV        = "      + str(normalization)     + "\n")
initial_file.write("trento_nucleon_width            = "      + str(nucleon_width)     + "\n")
initial_file.write("trento_min_nucleon_distance     = "      + str(nucleon_min_dist)  + "\n")
initial_file.write("trento_geometric_parameter      = "      + str(reduced_thickness) + "\n")
initial_file.write("trento_gamma_standard_deviation = "      + str(fluct_sigma)       + "\n")
initial_file.write("trento_average_over_events      = 1"     + "\n")
initial_file.write("trento_number_of_average_events = 2000"  + "\n")
initial_file.write("trento_fixed_seed               = 1000"  + "\n")
initial_file.close()

lattice_file = open('parameters/lattice.properties','w')
lattice_file.write("lattice_points_x     = "      + str(nx) + "\n")
lattice_file.write("lattice_points_y     = "      + str(ny) + "\n")
lattice_file.write("lattice_points_eta   = 1"     + "\n")
lattice_file.write("lattice_spacing_x    = "      + str(dx) + "\n")
lattice_file.write("lattice_spacing_y    = "      + str(dy) + "\n")
lattice_file.write("lattice_spacing_eta  = 0.2"   + "\n")
lattice_file.write("resolve_nucleons     = 0"     + "\n")                             # turned off resolve_nucleons b/c grid parameters already taken care of above
lattice_file.write("fit_rapidity_plateau = 0"     + "\n")
lattice_file.write("training_grid        = 0"     + "\n")
lattice_file.write("train_coarse_factor  = 1"     + "\n")
lattice_file.write("auto_grid            = 0"     + "\n")                             # not using auto grid at this time
lattice_file.write("sigma_factor         = 0.0"   + "\n")
lattice_file.write("buffer               = 2.5"   + "\n")
lattice_file.write("max_time_steps       = 2000"  + "\n")
lattice_file.write("output_interval      = 0.5"   + "\n")
lattice_file.write("fixed_time_step      = 0.01" + "\n")
lattice_file.write("adaptive_time_step   = 1"     + "\n")
lattice_file.write("delta_0              = 0.004" + "\n")
lattice_file.write("alpha                = 0.5"   + "\n")
lattice_file.close()


# make iS3D parameter file (for iS3D2, not iS3D master version)

iS3D_file = open('iS3D_parameters.dat','w')
iS3D_file.write("operation                 = 2"     + "\n")                           # run particle sampler
iS3D_file.write("mode                      = 1"     + "\n")                           # cpu_vah surface format (for iS3D2 only)
iS3D_file.write("hrg_eos                   = 3"     + "\n")                           # can be overwritten by the MAP script
iS3D_file.write("dimension                 = 2"     + "\n")
iS3D_file.write("df_mode                   = "      + str(delta_f_mode) + "\n")       # can be overwritten by the MAP script
iS3D_file.write("include_baryon            = 0"     + "\n")
iS3D_file.write("include_bulk_deltaf       = 1"     + "\n")
iS3D_file.write("include_shear_deltaf      = 1"     + "\n")                           # shear + bulk corrections turned on (muB = nB = Vmu = 0)
iS3D_file.write("include_baryondiff_deltaf = 0"     + "\n")
iS3D_file.write("regulate_deltaf           = 1"     + "\n")
iS3D_file.write("outflow                   = 1"     + "\n")
iS3D_file.write("deta_min                  = 1.e-5" + "\n")
iS3D_file.write("group_particles           = 0"     + "\n")
iS3D_file.write("particle_diff_tolerance   = 0.01"  + "\n")
iS3D_file.write("mass_pion0                = 0.138" + "\n")
iS3D_file.write("do_resonance_decays       = 0"     + "\n")
iS3D_file.write("lightest_particle         = 111"   + "\n")
iS3D_file.write("oversample                = 1"     + "\n")                           # do oversampling
iS3D_file.write("min_num_hadrons           = "      + str(min_num_hadrons) + "\n")
iS3D_file.write("max_num_samples           = "      + str(max_num_samples) + "\n")
iS3D_file.write("fast                      = 1"     + "\n")                           # using fast mode (sample surface with T_avg to speed up calculation)
iS3D_file.write("y_cut                     = "      + str(rap_max) + "\n")
iS3D_file.write("sampler_seed              = -1"    + "\n")                           # seed set to clock time
iS3D_file.write("test_sampler              = 0"     + "\n")                           # not testing sampler so remaining parameters are idle
iS3D_file.write("pT_min                    = 0.0"   + "\n")
iS3D_file.write("pT_max                    = 3.0"   + "\n")
iS3D_file.write("pT_bins                   = 100"   + "\n")
iS3D_file.write("y_bins                    = 50"    + "\n")
iS3D_file.write("phip_bins                 = 100"   + "\n")
iS3D_file.write("eta_cut                   = 7"     + "\n")
iS3D_file.write("eta_bins                  = 70"    + "\n")
iS3D_file.write("tau_min                   = 0.0"   + "\n")
iS3D_file.write("tau_max                   = 12.0"  + "\n")
iS3D_file.write("tau_bins                  = 120"   + "\n")
iS3D_file.write("r_min                     = 0.0"   + "\n")
iS3D_file.write("r_max                     = 10.0"  + "\n")
iS3D_file.write("r_bins                    = 50"    + "\n")
iS3D_file.close()





# JETSCAPE init xml file (for TRENTo, MUSIC, SMASH)

js_file = open('jetscape_init.xml', 'w')                                              # mike: did not modify this file

js_file.write("<?xml version=\"1.0\"?>\n")
js_file.write(" <jetscape>\n")
js_file.write("  <debug> on </debug>\n")
js_file.write("  <remark> off </remark>\n")
js_file.write("  <vlevel> 0 </vlevel>\n")
js_file.write("  <Random>\n")
js_file.write("    <seed>" + str(js_seed) + "</seed>\n")
js_file.write("  </Random>\n")

# parameters common to TRENTo and MUSIC
js_file.write("  <IS>\n")
js_file.write("    <grid_max_x> " + str(max_x) + " </grid_max_x>\n")
js_file.write("    <grid_max_y> " + str(max_y) + " </grid_max_y>\n")
js_file.write("    <grid_max_z> 0 </grid_max_z>\n")
js_file.write("    <grid_step_x> " + str(dx) + " </grid_step_x>\n")
js_file.write("    <grid_step_y> " + str(dy) + " </grid_step_y>\n")
js_file.write("    <grid_step_z> 0.5 </grid_step_z>\n")

# TRENTo parameters
js_file.write("    <Trento>\n")
js_file.write("		<PhysicsInputs	projectile=\'" + str(projectile) + "\'\n")
js_file.write("						target=\'" + str(target) + "\'\n")
js_file.write("						sqrts=\'" + str(sqrts) + "\'\n")
js_file.write("						cross-section=\'" + str(cross_section) + "\'\n")
js_file.write("						normalization=\'" + str(normalization) + "\'>\n")
js_file.write("		</PhysicsInputs>\n")
js_file.write("		<CutInputs	centrality-low=\'" + str(cent_low) + "\'\n")
js_file.write("					centrality-high=\'" + str(cent_high) + "\'>\n")
js_file.write("		</CutInputs>\n")
js_file.write("		<TransInputs	reduced-thickness=\'" + str(reduced_thickness) + "\'\n")
js_file.write("						fluctuation=\'" + str( round(fluct_k, 4) ) + "\'\n")
js_file.write("						nucleon-width=\'" + str(nucleon_width) + "\'\n")
js_file.write("						nucleon-min-dist=\'" + str(nucleon_min_dist) + "\'>\n")
js_file.write("		</TransInputs>\n")
js_file.write("		<LongiInputs	mean-coeff=\'1.0\'\n")
js_file.write("						std-coeff=\'3.0\'\n")
js_file.write("						skew-coeff=\'0.0\'\n")
js_file.write("						skew-type=\'1\'\n")
js_file.write("						jacobian=\'0.8\'>\n")
js_file.write("		</LongiInputs>\n")
js_file.write("    </Trento>\n")
js_file.write("    <initial_profile_path>../examples/test_hydro_files</initial_profile_path>\n")
js_file.write("  </IS>\n")

# these are dummies, not actually read by freestream-milne
js_file.write("  <Preequilibrium>\n")
js_file.write("    <tau0>0.0</tau0>\n")
js_file.write("    <taus>0.5</taus>\n")
js_file.write("    <FreestreamMilne>\n")
js_file.write("      <name>FreestreamMilne</name>\n")
js_file.write("      <freestream_input_file>freestream_input</freestream_input_file>\n")
js_file.write("    </FreestreamMilne>\n")
js_file.write("  </Preequilibrium>\n")

# fixed parameters for MUSIC
js_file.write("  <Hydro>\n")
js_file.write("    <MUSIC>\n")
js_file.write("      <name>MUSIC</name>\n")
js_file.write("      <MUSIC_input_file>music_input</MUSIC_input_file>\n")
js_file.write("      <Perform_CooperFrye_Feezeout>0</Perform_CooperFrye_Feezeout>\n")
js_file.write("    </MUSIC>\n")
js_file.write("  </Hydro>\n")

# parameters for SMASH
js_file.write("  <Afterburner>\n")
js_file.write("    <SMASH>\n")
js_file.write("      <name>SMASH</name>\n")
js_file.write("      <SMASH_config_file>smash_input/config.yaml</SMASH_config_file>\n")
js_file.write("      <SMASH_particles_file>smash_input/box/particles.txt</SMASH_particles_file>\n")
js_file.write("      <SMASH_decaymodes_file>smash_input/box/decaymodes.txt</SMASH_decaymodes_file>\n")
js_file.write("      <end_time>" + str(max_time_smash) + "</end_time>\n")
js_file.write("      <only_decays>0</only_decays>\n")
js_file.write("    </SMASH>\n")
js_file.write("  </Afterburner>\n")

js_file.write("</jetscape>\n")

js_file.close()




