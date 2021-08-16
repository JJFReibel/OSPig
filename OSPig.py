# By JJ Reibel, using Python 3
import platform

# Get Computer Name
print("Computer Name:"+ " "*19 + str(platform.node()))

# Get OS
print(str("Operating System:" + " "*16 + platform.system()))

# Get OS Release
print(str("Operating System Release:" + " "*8 + platform.release()))

# Get OS Version
print(str("Operating System Version:" + " "*8 + platform.platform()))
