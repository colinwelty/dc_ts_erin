# Purpose: Vertically interpolate your WRF datasets!

# Input:
    # input_file: The stitched WRFout file path
    # variable_name: A list of variables that you are interested in calculating
        # U == Zonal wind [m/s]
    # output_dir: The path to a directory where you'd like the new .nc files to be located
    # vertical_levels: An np.array() of pressure level(s) (in hPa) to interpolat
# Output:
    # .nc files for specific variables
# Process:
    # Open the stitched wrfout file
    # Figure out if the user wants 1 level or multiple levels, then loop through the variables
    # Create the new .nc file, copy global attributes over, and edit certain dims
    # Create the home where the variable will live then loop through each timestep
        # and fill it with the interpolated variable. This loop is necessary for 
        # variables that are too big to load into one variable.
# Tip:
    # You'd want to run this function for each domain file you have because input_file currently takes one path.
## EXAMPLE ##
# i.e. if I want to interpolate zonal winds on pressure coordinates on 50hPa , I would run this: 
# parent_dir = '/this/is/where/my/data/lives'
# input_file_d01 = parent_dir + '/raw/d01'  # Path to the raw input netCDF file
# input_file_d02 = parent_dir + '/raw/d02'  # Path to the raw input netCDF file
# output_dir = parent_dir + '/L2/'  # Path to the directory with interpolated files
# variable_name = ['U']             # Declare the variables you want to interpolate
# vertical_levels = np.arange(1000,0,-50)   # Pressure heights you want to interpolate at
# Call the function:
# interp_variable(input_file_d01, variable_name, output_dir, vertical_levels)

import netCDF4 as nc
import numpy as np
import wrf
import sys

def interp_variable(input_file, variable_name, output_dir, vertical_levels, first_letter):
    # Open the input netCDF file
    dataset = nc.Dataset(input_file, 'r')   # 'r' is just to read the dataset, we do NOT want write privledges

    if vertical_levels.shape == (): levels = 1
    else: levels = len(vertical_levels)

    for i in variable_name:
        if i == 'U':
            # Create new .nc file we can write to and name it appropriately
            if levels == 1:
                output_dataset = nc.Dataset(output_dir + first_letter+ '_aglinterp_' + 'U' + str(vertical_levels), 'w', clobber=True)
            else:
                output_dataset = nc.Dataset(output_dir + first_letter+ '_aglinterp_U', 'w', clobber=True)
                output_dataset.setncatts(dataset.__dict__)
                vertical_interval = vertical_levels[1] - vertical_levels[0]
                output_dataset.comment = f"Vertical levels range from {vertical_levels[0]} to {vertical_levels[-1]} meters with an interval of {vertical_interval} meters"
            # Create the dimensions based on global dimensions, with exception to bottom_top
            for dim_name, dim in dataset.dimensions.items():
                if dim_name == 'bottom_top':    output_dataset.createDimension(dim_name, levels)
                else:   output_dataset.createDimension(dim_name, len(dim))
            # wrf.getvar() will destagger, therefore dim 'west_east_stag' should be 'west_east'
            temp = list(dataset.variables['U'].dimensions)
           # print("Initial: ")
            #print(temp)
            temp[-1] = 'west_east'
            #print("Post Initial: ")
            #print(temp)
            temp = tuple(temp)
            # Create the variable, set attributes, and start filling the variable into the new nc file
            output_variable = output_dataset.createVariable(i, 'f4', temp)  # 'f4' == float32
            temp_atts = dataset.variables['U'].__dict__
            temp_atts.update({'stagger': ''})
            output_variable.setncatts(temp_atts)
            
            for t in range(dataset.dimensions['Time'].size):
                variable = wrf.getvar(dataset, 'ua', timeidx=t, meta=False)
                variable.set_fill_value(wrf.default_fill(np.float64))
                #pressure_heights = wrf.getvar(dataset, 'pressure', timeidx=t, meta=False)
                agl_heights = wrf.getvar(dataset, 'height_agl', timeidx=t, meta=False)
                interp_variable = wrf.interplevel(variable,agl_heights,vertical_levels,meta=False, missing = wrf.default_fill(np.float64))
                #print(np.shape(interp_variable))
                #print(np.shape(output_variable[t,...]))
                output_variable[t,:,:,:] = interp_variable[:,:,:]
                print("Confirmation this is working")
                #sys.exit()
            # Make sure you close the input and output files at the end
            output_dataset.close()
        if i == 'V':
            # Create new .nc file we can write to and name it appropriately
            if levels == 1:
                output_dataset = nc.Dataset(output_dir + first_letter+ '_aglinterp_' + 'V' + str(vertical_levels), 'w', clobber=True)
            else:
                output_dataset = nc.Dataset(output_dir + first_letter+ 'aglinterp_V', 'w', clobber=True)
            output_dataset.setncatts(dataset.__dict__)
            # Create the dimensions based on global dimensions, with exception to bottom_top
            for dim_name, dim in dataset.dimensions.items():
                if dim_name == 'bottom_top':    output_dataset.createDimension(dim_name, levels)
                else:   output_dataset.createDimension(dim_name, len(dim))
            # wrf.getvar() will destagger, therefore dim 'west_east_stag' should be 'west_east'
            temp = list(dataset.variables['V'].dimensions)
            #print("New Initial: ")
            #print(temp)
            temp[-2] = 'south_north'
            print("New Post Initial: ")
            print(temp)
            temp = tuple(temp)
            # Create the variable, set attributes, and start filling the variable into the new nc file
            output_variable = output_dataset.createVariable(i, 'f4', temp)  # 'f4' == float32
            temp_atts = dataset.variables['V'].__dict__
            temp_atts.update({'stagger': ''})
            output_variable.setncatts(temp_atts)
            vertical_interval = vertical_levels[1] - vertical_levels[0]
            output_dataset.comment = f"Vertical levels range from {vertical_levels[0]} to {vertical_levels[-1]} meters with an interval of {vertical_interval} meters"
            for t in range(dataset.dimensions['Time'].size):
                variable = wrf.getvar(dataset, 'va', timeidx=t, meta=False)
                variable.set_fill_value(wrf.default_fill(np.float64))
                agl_heights = wrf.getvar(dataset, 'height_agl', timeidx=t, meta=False)
                interp_variable = wrf.interplevel(variable,agl_heights,vertical_levels,meta=False, missing = wrf.default_fill(np.float64))
                #interp_variable = wrf.interplevel(variable,pressure_heights,vertical_levels,meta=False)
                output_variable[t,:,:,:] = interp_variable[:,:,:]
                #output_variable[t, ...] = np.expand_dims(interp_variable, axis=0)
            # Make sure you close the input and output files at the end
            output_dataset.close()
    dataset.close()
    return

#interp_file = "/ourdisk/hpc/radclouds/auto_archive_notyet/tape_2copies/tc_erin/analysis"
c_input_file = "/ourdisk/hpc/radclouds/auto_archive_notyet/tape_2copies/tc_erin/stitchd02_wrfout.nc"
d_input_file = "/ourdisk/hpc/radclouds/auto_archive_notyet/tape_2copies/tc_erin/stitchd02_wrfoutdiurnal.nc"
nocrf_input_file = "/ourdisk/hpc/radclouds/auto_archive_notyet/tape_2copies/tc_erin/crf/output/stitchd02_wrfoutcrf.nc"
ctrl2_input_file = "/ourdisk/hpc/radclouds/auto_archive_notyet/tape_2copies/tc_erin/ctrl/output/stitchd02_wrfoutctrl2.nc"
noflux_input_file = "/ourdisk/hpc/radclouds/auto_archive_notyet/tape_2copies/tc_erin/ctrl_imp/output/stitchd02_wrfoutnoflux.nc"
cimp_input_file = "/ourdisk/hpc/radclouds/auto_archive_notyet/tape_2copies/tc_erin/ctrl_imp/output/stitchd02_wrfoutimp.nc"
cimp2_input_file = "/ourdisk/hpc/radclouds/auto_archive_notyet/tape_2copies/tc_erin/ctrl_imp/outputnewimp/stitchd02_wrfoutctrlimp2.nc"
dimp_input_file = "/ourdisk/hpc/radclouds/auto_archive_notyet/tape_2copies/tc_erin/diurnal_imp/output/stitchd02_wrfoutimp_d.nc"
nocrfimp_input_file = "/ourdisk/hpc/radclouds/auto_archive_notyet/tape_2copies/tc_erin/crf_imp/output/stitchd02_wrfoutcrfimp.nc"
dimp2_input_file = '/ourdisk/hpc/radclouds/auto_archive_notyet/tape_2copies/tc_erin/diurnal_imp/outputnewimp/stitchd02_wrfoutdimp2.nc'
nocrfimp2_input_file = '/ourdisk/hpc/radclouds/auto_archive_notyet/tape_2copies/tc_erin/diurnal_imp/outputnewimp/stitchd02_wrfoutdimp2.nc'
variable_name = 'U'
variable_name2 = 'V'
#vertical_levels = np.arange(1000,450,-50)
vertical_levels = np.arange(0,5250,250)
output_dir = "/ourdisk/hpc/radclouds/auto_archive_notyet/tape_2copies/tc_erin/analysis/"
print("Levels: ", vertical_levels)
# interp_variable(c_input_file, variable_name, output_dir, vertical_levels, 'c_5000_250')
# interp_variable(c_input_file, variable_name2, output_dir, vertical_levels, 'c_5000_250')
# interp_variable(d_input_file, variable_name, output_dir, vertical_levels, 'd_5000_250')
# interp_variable(d_input_file, variable_name2, output_dir, vertical_levels, 'd_5000_250')
# interp_variable(nocrf_input_file, variable_name, output_dir, vertical_levels, 'nocrf_5000_250')
# interp_variable(nocrf_input_file, variable_name2, output_dir, vertical_levels, 'nocrf_5000_250')
# interp_variable(noflux_input_file, variable_name, output_dir, vertical_levels, 'nf_5000_250')
# interp_variable(noflux_input_file, variable_name2, output_dir, vertical_levels, 'nf_5000_250')
# interp_variable(cimp2_input_file, variable_name, output_dir, vertical_levels, 'cimp2_5000_250')
# interp_variable(cimp2_input_file, variable_name2, output_dir, vertical_levels, 'cimp2_5000_250')
# interp_variable(dimp_input_file, variable_name, output_dir, vertical_levels, 'dimp_5000_250')
# interp_variable(dimp_input_file, variable_name2, output_dir, vertical_levels, 'dimp_5000_250')
# interp_variable(nocrf_input_file, variable_name, output_dir, vertical_levels, 'nocrfimp_5000_250')
# interp_variable(nocrf_input_file, variable_name2, output_dir, vertical_levels, 'nocrfimp_5000_250')
interp_variable(dimp2_input_file, variable_name, output_dir, vertical_levels, 'dimp2_5000_250')
interp_variable(dimp2_input_file, variable_name2, output_dir, vertical_levels, 'dimp2_5000_250')
interp_variable(nocrfimp2_input_file, variable_name, output_dir, vertical_levels, 'nocrfimp2_5000_250')
interp_variable(nocrfimp2_input_file, variable_name2, output_dir, vertical_levels, 'nocrfimp2_5000_250')

