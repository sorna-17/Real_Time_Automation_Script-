#Automatic Battery_Checker 
'''Schedule this script in your system TASK MANAGER for every 5 min
START -> TASK SCHEDULER -> CREATE NEW TASK -> TRIGGER -> REGULATE TIME
It automatically starts running in the background
-Sornam Thiyagarajan'''




import psutil
from win10toast import ToastNotifier #Supported packages




toaster = ToastNotifier()
battery = psutil.sensors_battery()#Retriving Battery Status
plugged = battery.power_plugged
percent = str(battery.percent)
if plugged==False: plugged="Not Plugged In"
else: plugged="Plugged In"
print(percent+'% | '+plugged)
if percent == '100':
    toaster.show_toast(" 100% FULLY CHARGED","Unplug the charger")#POP-UPS 
