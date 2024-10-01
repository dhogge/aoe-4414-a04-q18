# eci_to_ecef.py
#
# Usage: python3 script_name.py arg1 arg2 ...
#  Text explaining script usage
# Parameters:
#  arg1: description of argument 1
#  arg2: description of argument 2
#  ...
# Output:
#  A description of the script output
#
# Written by Brad Denby
# Other contributors: Dylan Hogge
#
# Optional license statement, e.g., See the LICENSE file for the license.

# import Python modules
# e.g., import math # math module
import sys # argv
import math

# "constants"
R_E_KM = 6378.137
E_E=0.081819221456
w= 0.00007292115

# helper functions

## function description
def calc_denom(ecc, lat_rad):
  return math.sqrt(1.0-(ecc**2)*(math.sin(lat_rad)**2))


# initialize script arguments
year=float('nan')
month=float('nan')
day=float('nan')
hour=float('nan')
minute=float('nan')
second=float('nan')
eci_x_km=float('nan')
eci_y_km=float('nan')
eci_z_km=float('nan')


# parse script arguments
if len(sys.argv)==10:
   year = float(sys.argv[1])
   month = float(sys.argv[2])
   day = float(sys.argv[3])
   hour = float(sys.argv[4])
   minute = float(sys.argv[5])
   second = float(sys.argv[6])
   eci_x_km = float(sys.argv[7])
   eci_y_km = float(sys.argv[8])
   eci_z_km = float(sys.argv[9])
   ...
else:
   print(\
      'Usage: '\
        'python3 year month day hour minute second eci_x_km eci_y_km eci_z_km ...'\
        )
   exit()

# write script below this line
JD = day - 32075+1461*(year+4800-(14-month)//12)//4+367*(month-2+(14-month)//12*12)//12-3*((year+4900-(14-month)//12)//100)//4
JD_MN = JD-0.5
D_fract = (second+60*(minute+60*hour))/86400
JD_fract = JD_MN+D_fract

T_UT1 = (JD_fract - 2451545.0) / 36525

theta_gmst_sec = 67310.54841 + (876600 * 60 * 60 + 8640184.812866) * T_UT1 + 0.093104 * (T_UT1**2) + (-6.2 * 10**(-6)) * T_UT1**3

GMST = w * math.fmod(theta_gmst_sec, 86400)


ecef_x_km = eci_x_km*math.cos(GMST)+eci_y_km*math.sin(GMST)
ecef_y_km = eci_y_km*math.cos(GMST)-eci_x_km*math.sin(GMST)
ecef_z_km = eci_z_km

print(ecef_x_km)
print(ecef_y_km)
print(ecef_z_km)
