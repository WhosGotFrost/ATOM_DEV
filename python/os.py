#gives out simple obv information about your system
#linux!
import os

print("Logged in as: " + os.getlogin());
print("OS: " + os.uname()[0]);
print("MACHINE: " + os.uname()[4]);
print("Current Directory: " + os.getcwd())
