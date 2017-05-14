# ############################ Examples how to use the cube solver #####################################################

cubestring = 'FFBLBRDLDUBRRFDDLRLUUUFB'  # cube definition string of cube we want to solve
# See module enums.py for the format of the cube definition string

# ######################### Method 1: directly call the solve routine# #################################################
# Advantage: No network layer needed. Disadvantage: For each solve, the tables have to be loaded which takes a few     #
# seconds for each new solve.                                                                                          #
########################################################################################################################

#  Uncomment this part if you want to use method 1
"""
import solver as sv
a = sv.solve(cubestring)  # solve with a maximum of 20 moves and a timeout of 2 seconds for example
print(a)
quit()
"""
########################################################################################################################


# ############################### Method 2 a/b: Start the cubesolving-server# ##########################################
# Advantage: Tables have to be loaded only once when the server starts. Disadvantage: Network layer must be present.   #
########################################################################################################################

#----------------------------------------------------------------------------------------------------------------------
# Method 2a: Start the server from inside a Python script:
import start_server
from threading import Thread
background_thread = Thread(target=start_server.start, args=(8080,))
background_thread.start()
# Server listens now on port 8080, maxlength 20 moves, timeout 2 seconds
# ----------------------------------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------------------------------
# Method 2b: Start the server from a terminal with parameter for port:
# python start_server.py 8080
# ----------------------------------------------------------------------------------------------------------------------


# Once the server is started you can transfer the cube definition string to the server with different methods:

# ----------------------------------------------------------------------------------------------------------------------
# 1. With a webbrowser, if the server runs on the same machine on port 8080
# http://localhost:8080/FFBLBRDLDUBRRFDDLRLUUUFB
# With a webbrowser, if the server runs on server myserver.com, port 8081
# http://myserver.com:8081/FFBLBRDLDUBRRFDDLRLUUUFB
# ----------------------------------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------------------------------
# 2. With netcat, if the server runs on the same machine on port 8080
# echo FFBLBRDLDUBRRFDDLRLUUUFB | nc localhost 8080
# ----------------------------------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------------------------------
# 3. With this little graphical interface.
# From within a Python script start the interface with

import client_gui

# From a terminal start the interface with
# python client_gui.py
# ----------------------------------------------------------------------------------------------------------------------

########################################################################################################################