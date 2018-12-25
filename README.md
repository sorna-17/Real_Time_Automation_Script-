# Real_Time_Automation_Script-
This Repository contains Python Scripts which is based on automating the system without human interaction 
-Sornam Thiyagarajan 


'''Schedule this script in your system TASK MANAGER for every 5 min
START -> TASK SCHEDULER -> CREATE NEW TASK -> TRIGGER -> REGULATE TIME
It automatically starts running in the background'''




import psutil
from win10toast import ToastNotifier #supported packages

toaster = ToastNotifier()
battery = psutil.sensors_battery()
plugged = battery.power_plugged #retriving battery status
percent = str(battery.percent)
if plugged==False: plugged="Not Plugged In"
else: plugged="Plugged In"
print(percent+'% | '+plugged) #checking battery percent 
if percent == '100':
    toaster.show_toast(" 100% FULLY CHARGED","Unplug the charger") #POPS-UP if it is still PULUGGED IN after 100%
