#date craeted 10.01.2020 Autthor: s.sivakumar
#centre for photonics and Nanotechnology
#Sona College of technology
#e.mail. sivakumar390@gmail.com
import math
import numpy as np
import os
Peak_postion = float(input(" Peak position (2 theta)"))
FWHM = float(input(" FWHM (2 theta)"))
Xray_wavelength = 1.54178
size = float (0.94*Xray_wavelength/(math.radians(FWHM)*math.cos(math.radians(Peak_postion/2)))/10)
print("crystal size is :" ,size, "nm" )
os.system("pause")
