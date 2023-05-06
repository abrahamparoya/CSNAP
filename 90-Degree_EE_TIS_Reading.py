
#! /usr/bin/env python3


### Muli-Step Tactile Sensor Reading Test Script ###

###
# KINOVA (R) KORTEX (TM)
#
# Copyright (c) 2018 Kinova inc. All rights reserved.
#
# This software may be modified and distributed
# under the terms of the BSD 3-Clause license.
#
# Refer to the LICENSE file for details.
#
###

from sunau import AUDIO_UNKNOWN_SIZE
import sys
import os
import time
import threading
import numbers

from kortex_api.autogen.client_stubs.BaseClientRpc import BaseClient
from kortex_api.autogen.client_stubs.BaseCyclicClientRpc import BaseCyclicClient

from kortex_api.autogen.messages import Base_pb2, BaseCyclic_pb2, Common_pb2

# DEFINITIONS:

# Index Variables
# Initialize the varibales for the x,y and z slots of the soft and hard 
# list.
x = 0;
y = 1;
z = 2;

# Sensor Dimensions - Unit: cm
height = 11.5;
diameter = 6.5;
radius = diameter/2;


# Soft Inclusion Phantom Center Coordinates - Unit: cm
soft = [45, 5, -1.5];

# Subtracting the radius of the sample tube so the center of the
# sample tube sits above the center of the phantom.
softx = soft[x] - radius
softy = soft[y]

# Subtracting the height of the sample tube so the edge of the
# sample tube hovers above the phantom. 
softz = soft[z] + height
print(softx, softy, softz)

# Hard Inclusion Phantom Center Coordinates - Unit: cm
hard =  [45, -5, -0.5];
hardx = hard[x] - radius
hardy = hard[y]
hardz = hard[z] + height
print(hardx, hardy, hardz)

# End Effector Angle - Unit: degrees
# These angles are choosen to fix the end-effector of the Kinova arm at
# 90-degree angle.
adx = 90;
ady = 0;
adz = 90;

# Pyrex Coordinates - Unit: cm
P1 = [47, 10, -3.5]; #Top Left   
P2 = [47, 10, -3.5]; #Top Right
P3 = [30, -14, -3.5]; #Bottom Right
P4 = [30, 10, -3.5]; #Bottom Left

# Maximum allowed waiting time during actions (in seconds)
TIMEOUT_DURATION = 1000

# Create closure to set an event after an END or an ABORT
# Takes an input of "e" to see if the progam has finished or aborted.
# Returns the notification of the event that occured.

def check_for_end_or_abort(e):
    """Return a closure checking for END or ABORT notifications
    Arguments:
    e -- event to signal when the action is completed
        (will be set when an END or ABORT occurs)
    """
    def check(notification, e = e):
        print("EVENT : " + \
              Base_pb2.ActionEvent.Name(notification.action_event))
        if notification.action_event == Base_pb2.ACTION_END \
        or notification.action_event == Base_pb2.ACTION_ABORT:
            e.set()
    return check

def example_test_movement(base, base_cyclic):
    
    print("Starting Cartesian action movement ...")
    action = Base_pb2.Action()
    action.name = "Example Cartesian action movement"
    action.application_data = ""

    feedback = base_cyclic.RefreshFeedback()

    cartesian_pose = action.reach_pose.target_pose

    cartesian_pose.x = feedback.base.tool_pose_x          # (meters)
    cartesian_pose.y = feedback.base.tool_pose_y     # (meters)
    cartesian_pose.z = feedback.base.tool_pose_z     # (meters)
    cartesian_pose.theta_x = feedback.base.tool_pose_theta_x # (degrees)
    cartesian_pose.theta_y = feedback.base.tool_pose_theta_y # (degrees)
    cartesian_pose.theta_z = feedback.base.tool_pose_theta_z # (degrees)

    e = threading.Event()
    notification_handle = base.OnNotificationActionTopic(
        check_for_end_or_abort(e),
        Base_pb2.NotificationOptions()
    )

    print("Executing action")
    base.ExecuteAction(action)

    print("Waiting for movement to finish ...")
    finished = e.wait(TIMEOUT_DURATION)
    base.Unsubscribe(notification_handle)
    

    # Soft Movement 1
    print("Starting Cartesian action movement ...")
    action1 = Base_pb2.Action()
    action1.name = "Movement 1- Top Left"
    action1.application_data = ""

    feedback = base_cyclic.RefreshFeedback()

    cartesian_pose = action1.reach_pose.target_pose
    # These are loaded directly from Kinova Web app (the first three are divided by 100 since it gives them in mm)
    
    cartesian_pose.x = softx/100        # (meters)
    cartesian_pose.y = softy/100       # (meters)
    cartesian_pose.z = softz/100 + 15/100       # (meters)
    cartesian_pose.theta_x = adx   # (degrees)
    cartesian_pose.theta_y = ady     # (degrees)
    cartesian_pose.theta_z = adz     # (degrees)
	
    e = threading.Event()
    notification_handle = base.OnNotificationActionTopic(
        check_for_end_or_abort(e),
        Base_pb2.NotificationOptions()
    )

    print("Executing action")
    base.ExecuteAction(action1)

    print("Waiting for movement to finish ...")
    finished = e.wait(TIMEOUT_DURATION)
    base.Unsubscribe(notification_handle)

    # Soft Movement 2
    print("Starting Cartesian action movement ...")
    action1 = Base_pb2.Action()
    action1.name = "Movement 1- Top Left"
    action1.application_data = ""

    feedback = base_cyclic.RefreshFeedback()

    cartesian_pose = action1.reach_pose.target_pose
    # These are loaded directly from Kinova Web app (the first three are divided by 100 since it gives them in mm)
    
    cartesian_pose.x = softx/100        # (meters)
    cartesian_pose.y = softy/100       # (meters)
    cartesian_pose.z = softz/100         # (meters)
    cartesian_pose.theta_x = adx   # (degrees)
    cartesian_pose.theta_y = ady     # (degrees)
    cartesian_pose.theta_z = adz     # (degrees)
	
    e = threading.Event()
    notification_handle = base.OnNotificationActionTopic(
        check_for_end_or_abort(e),
        Base_pb2.NotificationOptions()
    )

    print("Executing action")
    base.ExecuteAction(action1)

    print("Waiting for movement to finish ...")
    finished = e.wait(TIMEOUT_DURATION)
    base.Unsubscribe(notification_handle)

# Soft Movement 3
    print("Starting Cartesian action movement ...")
    action1 = Base_pb2.Action()
    action1.name = "Movement 1- Top Left"
    action1.application_data = ""

    feedback = base_cyclic.RefreshFeedback()

    cartesian_pose = action1.reach_pose.target_pose
    # These are loaded directly from Kinova Web app (the first three are divided by 100 since it gives them in mm)
    
    cartesian_pose.x = softx/100       # (meters)
    cartesian_pose.y = softy/100             # (meters)
    cartesian_pose.z = softz/100 - 0.2/100       # (meters)
    cartesian_pose.theta_x = adx     # (degrees)
    cartesian_pose.theta_y = ady     # (degrees)
    cartesian_pose.theta_z = adz     # (degrees)

    e = threading.Event()
    notification_handle = base.OnNotificationActionTopic(
        check_for_end_or_abort(e),
        Base_pb2.NotificationOptions()
    )

    print("Executing action")
    base.ExecuteAction(action1)

    print("Waiting for movement to finish ...")
    finished = e.wait(TIMEOUT_DURATION)
    base.Unsubscribe(notification_handle)

# Soft Movement 4
    print("Starting Cartesian action movement ...")
    action1 = Base_pb2.Action()
    action1.name = "Movement 1- Top Left"
    action1.application_data = ""

    feedback = base_cyclic.RefreshFeedback()

    cartesian_pose = action1.reach_pose.target_pose
    # These are loaded directly from Kinova Web app (the first three are divided by 100 since it gives them in mm)
    
    cartesian_pose.x = softx/100        # (meters)
    cartesian_pose.y = softy/100       # (meters)
    cartesian_pose.z = softz/100 - 0.4/100       # (meters)
    cartesian_pose.theta_x = adx   # (degrees)
    cartesian_pose.theta_y = ady     # (degrees)
    cartesian_pose.theta_z = adz     # (degrees)

    e = threading.Event()
    notification_handle = base.OnNotificationActionTopic(
        check_for_end_or_abort(e),
        Base_pb2.NotificationOptions()
    )

    print("Executing action")
    base.ExecuteAction(action1)

    print("Waiting for movement to finish ...")
    finished = e.wait(TIMEOUT_DURATION)
    base.Unsubscribe(notification_handle)

# Soft Movement 5
    print("Starting Cartesian action movement ...")
    action1 = Base_pb2.Action()
    action1.name = "Movement 1- Top Left"
    action1.application_data = ""

    feedback = base_cyclic.RefreshFeedback()

    cartesian_pose = action1.reach_pose.target_pose
    # These are loaded directly from Kinova Web app (the first three are divided by 100 since it gives them in mm)
    
    cartesian_pose.x = softx/100        # (meters)
    cartesian_pose.y = softy/100       # (meters)
    cartesian_pose.z = softz/100 - 0.6/100       # (meters)
    cartesian_pose.theta_x = adx   # (degrees)
    cartesian_pose.theta_y = ady     # (degrees)
    cartesian_pose.theta_z = adz     # (degrees)

    e = threading.Event()
    notification_handle = base.OnNotificationActionTopic(
        check_for_end_or_abort(e),
        Base_pb2.NotificationOptions()
    )

    print("Executing action")
    base.ExecuteAction(action1)

    print("Waiting for movement to finish ...")
    finished = e.wait(TIMEOUT_DURATION)
    base.Unsubscribe(notification_handle)

# Soft Movement 6
    print("Starting Cartesian action movement ...")
    action1 = Base_pb2.Action()
    action1.name = "Movement 1- Top Left"
    action1.application_data = ""

    feedback = base_cyclic.RefreshFeedback()

    cartesian_pose = action1.reach_pose.target_pose
    # These are loaded directly from Kinova Web app (the first three are divided by 100 since it gives them in mm)
    
    cartesian_pose.x = softx/100        # (meters)
    cartesian_pose.y = softy/100       # (meters)
    cartesian_pose.z = softz/100 - 0.8/100       # (meters)
    cartesian_pose.theta_x = adx   # (degrees)
    cartesian_pose.theta_y = ady     # (degrees)
    cartesian_pose.theta_z = adz     # (degrees)

    e = threading.Event()
    notification_handle = base.OnNotificationActionTopic(
        check_for_end_or_abort(e),
        Base_pb2.NotificationOptions()
    )

    print("Executing action")
    base.ExecuteAction(action1)

    print("Waiting for movement to finish ...")
    finished = e.wait(TIMEOUT_DURATION)
    base.Unsubscribe(notification_handle)

# Soft Movement 7
    print("Starting Cartesian action movement ...")
    action1 = Base_pb2.Action()
    action1.name = "Movement 1- Top Left"
    action1.application_data = ""

    feedback = base_cyclic.RefreshFeedback()

    cartesian_pose = action1.reach_pose.target_pose
    # These are loaded directly from Kinova Web app (the first three are divided by 100 since it gives them in mm)
    
    cartesian_pose.x = softx/100        # (meters)
    cartesian_pose.y = softy/100       # (meters)
    cartesian_pose.z = softz/100 - 2/100       # (meters)
    cartesian_pose.theta_x = adx   # (degrees)
    cartesian_pose.theta_y = ady     # (degrees)
    cartesian_pose.theta_z = adz     # (degrees)

    e = threading.Event()
    notification_handle = base.OnNotificationActionTopic(
        check_for_end_or_abort(e),
        Base_pb2.NotificationOptions()
    )

    print("Executing action")
    base.ExecuteAction(action1)

    print("Waiting for movement to finish ...")
    finished = e.wait(TIMEOUT_DURATION)
    base.Unsubscribe(notification_handle)

# Retracting Arm
    print("Starting Cartesian action movement ...")
    action1 = Base_pb2.Action()
    action1.name = "Movement 1- Top Left"
    action1.application_data = ""

    feedback = base_cyclic.RefreshFeedback()

    cartesian_pose = action1.reach_pose.target_pose
    # These are loaded directly from Kinova Web app (the first three are divided by 100 since it gives them in mm)
    
    cartesian_pose.x = softx/100        # (meters)
    cartesian_pose.y = softy/100       # (meters)
    cartesian_pose.z = softz/100 + 15/100       # (meters)
    cartesian_pose.theta_x = adx   # (degrees)
    cartesian_pose.theta_y = ady     # (degrees)
    cartesian_pose.theta_z = adz     # (degrees)

    e = threading.Event()
    notification_handle = base.OnNotificationActionTopic(
        check_for_end_or_abort(e),
        Base_pb2.NotificationOptions()
    )

    print("Executing action")
    base.ExecuteAction(action1)

    print("Waiting for movement to finish ...")
    finished = e.wait(TIMEOUT_DURATION)
    base.Unsubscribe(notification_handle)

# Transition to Hard Inclusion
    print("Starting Cartesian action movement ...")
    action1 = Base_pb2.Action()
    action1.name = "Movement 1- Top Left"
    action1.application_data = ""

    feedback = base_cyclic.RefreshFeedback()

    cartesian_pose = action1.reach_pose.target_pose
    # These are loaded directly from Kinova Web app (the first three are divided by 100 since it gives them in mm)
    
    cartesian_pose.x = hardx/100        # (meters)
    cartesian_pose.y = hardy/100       # (meters)
    cartesian_pose.z = hardz/100 + 15/100       # (meters)
    cartesian_pose.theta_x = adx   # (degrees)
    cartesian_pose.theta_y = ady     # (degrees)
    cartesian_pose.theta_z = adz     # (degrees)

    e = threading.Event()
    notification_handle = base.OnNotificationActionTopic(
        check_for_end_or_abort(e),
        Base_pb2.NotificationOptions()
    )

    print("Executing action")
    base.ExecuteAction(action1)

    print("Waiting for movement to finish ...")
    finished = e.wait(TIMEOUT_DURATION)
    base.Unsubscribe(notification_handle)

# Hard Movement 1
    print("Starting Cartesian action movement ...")
    action1 = Base_pb2.Action()
    action1.name = "Movement 1- Top Left"
    action1.application_data = ""

    feedback = base_cyclic.RefreshFeedback()

    cartesian_pose = action1.reach_pose.target_pose
    # These are loaded directly from Kinova Web app (the first three are divided by 100 since it gives them in mm)
    
    cartesian_pose.x = hardx/100        # (meters)
    cartesian_pose.y = hardy/100       # (meters)
    cartesian_pose.z = hardz/100         # (meters)
    cartesian_pose.theta_x = adx   # (degrees)
    cartesian_pose.theta_y = ady     # (degrees)
    cartesian_pose.theta_z = adz     # (degrees)
	
    e = threading.Event()
    notification_handle = base.OnNotificationActionTopic(
        check_for_end_or_abort(e),
        Base_pb2.NotificationOptions()
    )

    print("Executing action")
    base.ExecuteAction(action1)

    print("Waiting for movement to finish ...")
    finished = e.wait(TIMEOUT_DURATION)
    base.Unsubscribe(notification_handle)

# Hard Movement 2
    print("Starting Cartesian action movement ...")
    action1 = Base_pb2.Action()
    action1.name = "Movement 1- Top Left"
    action1.application_data = ""

    feedback = base_cyclic.RefreshFeedback()

    cartesian_pose = action1.reach_pose.target_pose
    # These are loaded directly from Kinova Web app (the first three are divided by 100 since it gives them in mm)
    
    cartesian_pose.x = hardx/100       # (meters)
    cartesian_pose.y = hardy/100             # (meters)
    cartesian_pose.z = hardz/100 - 0.2/100       # (meters)
    cartesian_pose.theta_x = adx     # (degrees)
    cartesian_pose.theta_y = ady     # (degrees)
    cartesian_pose.theta_z = adz     # (degrees)

    e = threading.Event()
    notification_handle = base.OnNotificationActionTopic(
        check_for_end_or_abort(e),
        Base_pb2.NotificationOptions()
    )

    print("Executing action")
    base.ExecuteAction(action1)

    print("Waiting for movement to finish ...")
    finished = e.wait(TIMEOUT_DURATION)
    base.Unsubscribe(notification_handle)

# Soft Movement 3
    print("Starting Cartesian action movement ...")
    action1 = Base_pb2.Action()
    action1.name = "Movement 1- Top Left"
    action1.application_data = ""

    feedback = base_cyclic.RefreshFeedback()

    cartesian_pose = action1.reach_pose.target_pose
    # These are loaded directly from Kinova Web app (the first three are divided by 100 since it gives them in mm)
    
    cartesian_pose.x = hardx/100        # (meters)
    cartesian_pose.y = hardy/100       # (meters)
    cartesian_pose.z = hardz/100 - 0.4/100       # (meters)
    cartesian_pose.theta_x = adx   # (degrees)
    cartesian_pose.theta_y = ady     # (degrees)
    cartesian_pose.theta_z = adz     # (degrees)

    e = threading.Event()
    notification_handle = base.OnNotificationActionTopic(
        check_for_end_or_abort(e),
        Base_pb2.NotificationOptions()
    )

    print("Executing action")
    base.ExecuteAction(action1)

    print("Waiting for movement to finish ...")
    finished = e.wait(TIMEOUT_DURATION)
    base.Unsubscribe(notification_handle)

# Hard Movement 4
    print("Starting Cartesian action movement ...")
    action1 = Base_pb2.Action()
    action1.name = "Movement 1- Top Left"
    action1.application_data = ""

    feedback = base_cyclic.RefreshFeedback()

    cartesian_pose = action1.reach_pose.target_pose
    # These are loaded directly from Kinova Web app (the first three are divided by 100 since it gives them in mm)
    
    cartesian_pose.x = hardx/100        # (meters)
    cartesian_pose.y = hardy/100       # (meters)
    cartesian_pose.z = hardz/100 - 0.6/100       # (meters)
    cartesian_pose.theta_x = adx   # (degrees)
    cartesian_pose.theta_y = ady     # (degrees)
    cartesian_pose.theta_z = adz     # (degrees)

    e = threading.Event()
    notification_handle = base.OnNotificationActionTopic(
        check_for_end_or_abort(e),
        Base_pb2.NotificationOptions()
    )

    print("Executing action")
    base.ExecuteAction(action1)

    print("Waiting for movement to finish ...")
    finished = e.wait(TIMEOUT_DURATION)
    base.Unsubscribe(notification_handle)

# Hard Movement 5
    print("Starting Cartesian action movement ...")
    action1 = Base_pb2.Action()
    action1.name = "Movement 1- Top Left"
    action1.application_data = ""

    feedback = base_cyclic.RefreshFeedback()

    cartesian_pose = action1.reach_pose.target_pose
    # These are loaded directly from Kinova Web app (the first three are divided by 100 since it gives them in mm)
    
    cartesian_pose.x = hardx/100        # (meters)
    cartesian_pose.y = hardy/100       # (meters)
    cartesian_pose.z = hardz/100 - 0.8/100       # (meters)
    cartesian_pose.theta_x = adx   # (degrees)
    cartesian_pose.theta_y = ady     # (degrees)
    cartesian_pose.theta_z = adz     # (degrees)

    e = threading.Event()
    notification_handle = base.OnNotificationActionTopic(
        check_for_end_or_abort(e),
        Base_pb2.NotificationOptions()
    )

    print("Executing action")
    base.ExecuteAction(action1)

    print("Waiting for movement to finish ...")
    finished = e.wait(TIMEOUT_DURATION)
    base.Unsubscribe(notification_handle)

# hard Movement 6
    print("Starting Cartesian action movement ...")
    action1 = Base_pb2.Action()
    action1.name = "Movement 1- Top Left"
    action1.application_data = ""

    feedback = base_cyclic.RefreshFeedback()

    cartesian_pose = action1.reach_pose.target_pose
    # These are loaded directly from Kinova Web app (the first three are divided by 100 since it gives them in mm)
    
    cartesian_pose.x = hardx/100        # (meters)
    cartesian_pose.y = hardy/100       # (meters)
    cartesian_pose.z = hardz/100 -2/100       # (meters)
    cartesian_pose.theta_x = adx   # (degrees)
    cartesian_pose.theta_y = ady     # (degrees)
    cartesian_pose.theta_z = adz     # (degrees)

    e = threading.Event()
    notification_handle = base.OnNotificationActionTopic(
        check_for_end_or_abort(e),
        Base_pb2.NotificationOptions()
    )

    print("Executing action")
    base.ExecuteAction(action1)

    print("Waiting for movement to finish ...")
    finished = e.wait(TIMEOUT_DURATION)
    base.Unsubscribe(notification_handle)

# Retracting Arm
    print("Starting Cartesian action movement ...")
    action1 = Base_pb2.Action()
    action1.name = "Movement 1- Top Left"
    action1.application_data = ""

    feedback = base_cyclic.RefreshFeedback()

    cartesian_pose = action1.reach_pose.target_pose
    # These are loaded directly from Kinova Web app (the first three are divided by 100 since it gives them in mm)
    
    cartesian_pose.x = hardx/100        # (meters)
    cartesian_pose.y = hardy/100       # (meters)
    cartesian_pose.z = hardz/100 + 15/100       # (meters)
    cartesian_pose.theta_x = adx   # (degrees)
    cartesian_pose.theta_y = ady     # (degrees)
    cartesian_pose.theta_z = adz     # (degrees)

    e = threading.Event()
    notification_handle = base.OnNotificationActionTopic(
        check_for_end_or_abort(e),
        Base_pb2.NotificationOptions()
    )

    print("Executing action")
    base.ExecuteAction(action1)

    print("Waiting for movement to finish ...")
    finished = e.wait(TIMEOUT_DURATION)
    base.Unsubscribe(notification_handle)

    if finished:
        print("Cartesian movement completed")
    else:
        print("Timeout on action notification wait")
    return finished

def main():
    
    # Import the utilities helper module
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
    import utilities

    # Parse arguments
    args = utilities.parseConnectionArguments()
    
    # Create connection to the device and get the router
    with utilities.DeviceConnection.createTcpConnection(args) as router:

        # Create required services
        base = BaseClient(router)
        base_cyclic = BaseCyclicClient(router)

        # Example core
        success = True
        success &= example_test_movement(base, base_cyclic)
        #success &= example_test_movement(base, base_cyclic)

        return 0 if success else 1

if __name__ == "__main__":
    exit(main())
