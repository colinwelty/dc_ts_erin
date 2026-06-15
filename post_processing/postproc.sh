echo "Sourcing bashrc_wrf"
source /home/colinwelty/wrf-stuff/bashrc_wrf
echo "Loading Neccesary Modules"
module load iimpi/2018a
module load NCO
echo "Moving raw files to raw folder"
mv /ourdisk/hpc/radclouds/auto_archive_notyet/tape_2copies/tc_erin/diurnal_imp/WRF/run/wrfout_d* /ourdisk/hpc/radclouds/auto_archive_notyet/tape_2copies/tc_erin/diurnal_imp/outputnewimp
echo "Creating stitched files in current directory"
ncrcat /ourdisk/hpc/radclouds/auto_archive_notyet/tape_2copies/tc_erin/diurnal_imp/outputnewimp/wrfout_d01* -o stitchd01_wrfoutdimp2.nc -O
ncrcat /ourdisk/hpc/radclouds/auto_archive_notyet/tape_2copies/tc_erin/diurnal_imp/outputnewimp/wrfout_d02* -o stitchd02_wrfoutdimp2.nc -O
echo "Moving files to postprocessing folder"
mv stitchd01_wrfoutdimp2.nc /ourdisk/hpc/radclouds/auto_archive_notyet/tape_2copies/tc_erin/diurnal_imp/outputnewimp/
mv stitchd02_wrfoutdimp2.nc /ourdisk/hpc/radclouds/auto_archive_notyet/tape_2copies/tc_erin/diurnal_imp/outputnewimp/
echo "Resourcing bashrc_wrf"
source /home/colinwelty/wrf-stuff/bashrc_wrf