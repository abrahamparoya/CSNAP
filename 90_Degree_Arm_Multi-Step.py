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

import sys
import os
import time
import threading

from kortex_api.autogen.client_stubs.BaseClientRpc import BaseClient
from kortex_api.autogen.client_stubs.BaseCyclicClientRpc import BaseCyclicClient

from kortex_api.autogen.messages import Base_pb2, BaseCyclic_pb2, Common_pb2


# Maximum allowed waiting time during actions (in seconds)
TIMEOUT_DURATION = 360

# Create closure to set an event after an END or an ABORT
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

def example_angular_action_movement(base):
    
    print("Starting angular action movement ...")
    action = Base_pb2.Action()
    action.name = "Example angular action movement"
    action.application_data = ""

    actuator_count = base.GetActuatorCount()

    # Place arm straight up
    for joint_id in range(actuator_count.count):
        joint_angle = action.reach_joint_angles.joint_angles.joint_angles.add()
        joint_angle.joint_identifier = joint_id
        joint_angle.value = 0

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

    if finished:
        print("Angular movement completed")
    else:
        print("Timeout on action notification wait")
    return finished

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
    
    # Movement 1
    print("Starting Cartesian action movement ...")
    action1 = Base_pb2.Action()
    action1.name = "Movement 1- Top Left"
    action1.application_data = ""

    feedback = base_cyclic.RefreshFeedback()

    cartesian_pose = action1.reach_pose.target_pose
    # These are loaded directly from Kinova Web app (the first three are divided by 100 since it gives them in mm)
    
    cartesian_pose.x = 40/100        # (meters)
    cartesian_pose.y = 0/100        # (meters)
    cartesian_pose.z = 20/100        # (meters)
    cartesian_pose.theta_x = 90   # (degrees)
    cartesian_pose.theta_y = 0      # (degrees)
    cartesian_pose.theta_z = 90     # (degrees)

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

        # Movement 2
    print("Starting Cartesian action movement ...")
    action2 = Base_pb2.Action()
    action2.name = "Movement 2- Top Right"
    action2.application_data = ""

    feedback = base_cyclic.RefreshFeedback()

    cartesian_pose = action2.reach_pose.target_pose
    # These are loaded directly from Kinova Web app (the first three are divided by 100 since it gives them in mm)
    
    cartesian_pose.x = 40/100      # (meters)
    cartesian_pose.y = 6/100     # (meters)
    cartesian_pose.z = 20/100      # (meters)
    cartesian_pose.theta_x = 90 # (degrees)
    cartesian_pose.theta_y = 0 # (degrees)
    cartesian_pose.theta_z = 90 # (degrees)

    e = threading.Event()
    notification_handle = base.OnNotificationActionTopic(
        check_for_end_or_abort(e),
        Base_pb2.NotificationOptions()
    )

    print("Executing action")
    base.ExecuteAction(action2)

    print("Waiting for movement to finish ...")
    finished = e.wait(TIMEOUT_DURATION)
    base.Unsubscribe(notification_handle)
    
    
    # Movement 3
    print("Starting Cartesian action movement ...")
    action3 = Base_pb2.Action()
    action3.name = "Movement 3- Bottom Right"
    action3.application_data = ""

    feedback = base_cyclic.RefreshFeedback()

    cartesian_pose = action3.reach_pose.target_pose
    # These are loaded directly from Kinova Web app (the first three are divided by 100 since it gives them in mm)
    
    cartesian_pose.x = 40/100      # (meters)
    cartesian_pose.y = 6/100     # (meters)
    cartesian_pose.z = 15/100      # (meters)
    cartesian_pose.theta_x = 90 # (degrees)
    cartesian_pose.theta_y = 0 # (degrees)
    cartesian_pose.theta_z = 90 # (degrees)

    e = threading.Event()
    notification_handle = base.OnNotificationActionTopic(
        check_for_end_or_abort(e),
        Base_pb2.NotificationOptions()
    )

    print("Executing action")
    base.ExecuteAction(action3)

    print("Waiting for movement to finish ...")
    finished = e.wait(TIMEOUT_DURATION)
    base.Unsubscribe(notification_handle)

 # Movement 4
    print("Starting Cartesian action movement ...")
    action3 = Base_pb2.Action()
    action3.name = "Movement 3- Bottom Right"
    action3.application_data = ""

    feedback = base_cyclic.RefreshFeedback()

    cartesian_pose = action3.reach_pose.target_pose
    # These are loaded directly from Kinova Web app (the first three are divided by 100 since it gives them in mm)
    
    cartesian_pose.x = 40/100      # (meters)
    cartesian_pose.y = 6/100     # (meters)
    cartesian_pose.z = 13/100      # (meters)
    cartesian_pose.theta_x = 90 # (degrees)
    cartesian_pose.theta_y = 0  # (degrees)
    cartesian_pose.theta_z = 90  # (degrees)

    e = threading.Event()
    notification_handle = base.OnNotificationActionTopic(
        check_for_end_or_abort(e),
        Base_pb2.NotificationOptions()
    )

    print("Executing action")
    base.ExecuteAction(action3)

    print("Waiting for movement to finish ...")
    finished = e.wait(TIMEOUT_DURATION)
    base.Unsubscribe(notification_handle)

# Movement 5
    print("Starting Cartesian action movement ...")
    action3 = Base_pb2.Action()
    action3.name = "Movement 3- Bottom Right"
    action3.application_data = ""

    feedback = base_cyclic.RefreshFeedback()

    cartesian_pose = action3.reach_pose.target_pose
    # These are loaded directly from Kinova Web app (the first three are divided by 100 since it gives them in mm)
    
    cartesian_pose.x = 40/100      # (meters)
    cartesian_pose.y = 6/100     # (meters)
    cartesian_pose.z = 12.9/100      # (meters)
    cartesian_pose.theta_x = 90  # (degrees)
    cartesian_pose.theta_y = 0 # (degrees)
    cartesian_pose.theta_z = 90  # (degrees)

    e = threading.Event()
    notification_handle = base.OnNotificationActionTopic(
        check_for_end_or_abort(e),
        Base_pb2.NotificationOptions()
    )

    print("Executing action")
    base.ExecuteAction(action3)

    print("Waiting for movement to finish ...")
    finished = e.wait(TIMEOUT_DURATION)
    base.Unsubscribe(notification_handle)

# Movement 6
    print("Starting Cartesian action movement ...")
    action3 = Base_pb2.Action()
    action3.name = "Movement 3- Bottom Right"
    action3.application_data = ""

    feedback = base_cyclic.RefreshFeedback()

    cartesian_pose = action3.reach_pose.target_pose
    # These are loaded directly from Kinova Web app (the first three are divided by 100 since it gives them in mm)
    
    cartesian_pose.x = 40/100      # (meters)
    cartesian_pose.y = 6/100     # (meters)
    cartesian_pose.z = 12.8/100      # (meters)
    cartesian_pose.theta_x = 90 # (degrees)
    cartesian_pose.theta_y = 0 # (degrees)
    cartesian_pose.theta_z = 90  # (degrees)

    e = threading.Event()
    notification_handle = base.OnNotificationActionTopic(
        check_for_end_or_abort(e),
        Base_pb2.NotificationOptions()
    )

    print("Executing action")
    base.ExecuteAction(action3)

    print("Waiting for movement to finish ...")
    finished = e.wait(TIMEOUT_DURATION)
    base.Unsubscribe(notification_handle)

# Movement 7
    print("Starting Cartesian action movement ...")
    action3 = Base_pb2.Action()
    action3.name = "Movement 3- Bottom Right"
    action3.application_data = ""

    feedback = base_cyclic.RefreshFeedback()

    cartesian_pose = action3.reach_pose.target_pose
    # These are loaded directly from Kinova Web app (the first three are divided by 100 since it gives them in mm)
    
    cartesian_pose.x = 40/100      # (meters)
    cartesian_pose.y = 6/100     # (meters)
    cartesian_pose.z = 12.7/100      # (meters)
    cartesian_pose.theta_x = 90  # (degrees)
    cartesian_pose.theta_y = 0  # (degrees)
    cartesian_pose.theta_z = 90  # (degrees)

    e = threading.Event()
    notification_handle = base.OnNotificationActionTopic(
        check_for_end_or_abort(e),
        Base_pb2.NotificationOptions()
    )

    print("Executing action")
    base.ExecuteAction(action3)

    print("Waiting for movement to finish ...")
    finished = e.wait(TIMEOUT_DURATION)
    base.Unsubscribe(notification_handle)

    # Movement 8
    print("Starting Cartesian action movement ...")
    action3 = Base_pb2.Action()
    action3.name = "Movement 3- Bottom Right"
    action3.application_data = ""

    feedback = base_cyclic.RefreshFeedback()

    cartesian_pose = action3.reach_pose.target_pose
    # These are loaded directly from Kinova Web app (the first three are divided by 100 since it gives them in mm)
    
    cartesian_pose.x = 40/100      # (meters)
    cartesian_pose.y = 6/100     # (meters)
    cartesian_pose.z = 12.6/100      # (meters)
    cartesian_pose.theta_x = 90  # (degrees)
    cartesian_pose.theta_y = 0  # (degrees)
    cartesian_pose.theta_z = 90  # (degrees)

    e = threading.Event()
    notification_handle = base.OnNotificationActionTopic(
        check_for_end_or_abort(e),
        Base_pb2.NotificationOptions()
    )

    print("Executing action")
    base.ExecuteAction(action3)

    print("Waiting for movement to finish ...")
    finished = e.wait(TIMEOUT_DURATION)
    base.Unsubscribe(notification_handle)

# Movement 8
    print("Starting Cartesian action movement ...")
    action3 = Base_pb2.Action()
    action3.name = "Movement 3- Bottom Right"
    action3.application_data = ""

    feedback = base_cyclic.RefreshFeedback()

    cartesian_pose = action3.reach_pose.target_pose
    # These are loaded directly from Kinova Web app (the first three are divided by 100 since it gives them in mm)
    
    cartesian_pose.x = 40/100      # (meters)
    cartesian_pose.y = 6/100     # (meters)
    cartesian_pose.z = 12.5/100      # (meters)
    cartesian_pose.theta_x = 90  # (degrees)
    cartesian_pose.theta_y = 0  # (degrees)
    cartesian_pose.theta_z = 90  # (degrees)

    e = threading.Event()
    notification_handle = base.OnNotificationActionTopic(
        check_for_end_or_abort(e),
        Base_pb2.NotificationOptions()
    )
    print("Executing action")
    base.ExecuteAction(action3)

    print("Waiting for movement to finish ...")
    finished = e.wait(TIMEOUT_DURATION)
    base.Unsubscribe(notification_handle)
    
    # Movement 9
    print("Starting Cartesian action movement ...")
    action3 = Base_pb2.Action()
    action3.name = "Movement 3- Bottom Right"
    action3.application_data = ""

    feedback = base_cyclic.RefreshFeedback()

    cartesian_pose = action3.reach_pose.target_pose
    # These are loaded directly from Kinova Web app (the first three are divided by 100 since it gives them in mm)
    
    cartesian_pose.x = 40/100      # (meters)
    cartesian_pose.y = 6/100     # (meters)
    cartesian_pose.z = 12.4/100      # (meters)
    cartesian_pose.theta_x = 90  # (degrees)
    cartesian_pose.theta_y = 0  # (degrees)
    cartesian_pose.theta_z = 90  # (degrees)

    e = threading.Event()
    notification_handle = base.OnNotificationActionTopic(
        check_for_end_or_abort(e),
        Base_pb2.NotificationOptions()
    )
    print("Executing action")
    base.ExecuteAction(action3)

    print("Waiting for movement to finish ...")
    finished = e.wait(TIMEOUT_DURATION)
    base.Unsubscribe(notification_handle)

    # Movement 10
    print("Starting Cartesian action movement ...")
    action3 = Base_pb2.Action()
    action3.name = "Movement 3- Bottom Right"
    action3.application_data = ""

    feedback = base_cyclic.RefreshFeedback()

    cartesian_pose = action3.reach_pose.target_pose
    # These are loaded directly from Kinova Web app (the first three are divided by 100 since it gives them in mm)
    
    cartesian_pose.x = 40/100      # (meters)
    cartesian_pose.y = 6/100     # (meters)
    cartesian_pose.z = 12.3/100      # (meters)
    cartesian_pose.theta_x = 90  # (degrees)
    cartesian_pose.theta_y = 0  # (degrees)
    cartesian_pose.theta_z = 90  # (degrees)

    e = threading.Event()
    notification_handle = base.OnNotificationActionTopic(
        check_for_end_or_abort(e),
        Base_pb2.NotificationOptions()
    )
    print("Executing action")
    base.ExecuteAction(action3)

    print("Waiting for movement to finish ...")
    finished = e.wait(TIMEOUT_DURATION)
    base.Unsubscribe(notification_handle)

# Movement 11
    print("Starting Cartesian action movement ...")
    action3 = Base_pb2.Action()
    action3.name = "Movement 3- Bottom Right"
    action3.application_data = ""

    feedback = base_cyclic.RefreshFeedback()

    cartesian_pose = action3.reach_pose.target_pose
    # These are loaded directly from Kinova Web app (the first three are divided by 100 since it gives them in mm)
    
    cartesian_pose.x = 40/100      # (meters)
    cartesian_pose.y = 6/100     # (meters)
    cartesian_pose.z = 12.2/100      # (meters)
    cartesian_pose.theta_x = 90  # (degrees)
    cartesian_pose.theta_y = 0  # (degrees)
    cartesian_pose.theta_z = 90  # (degrees)

    e = threading.Event()
    notification_handle = base.OnNotificationActionTopic(
        check_for_end_or_abort(e),
        Base_pb2.NotificationOptions()
    )
    print("Executing action")
    base.ExecuteAction(action3)

    print("Waiting for movement to finish ...")
    finished = e.wait(TIMEOUT_DURATION)
    base.Unsubscribe(notification_handle)

# Movement 12
    print("Starting Cartesian action movement ...")
    action3 = Base_pb2.Action()
    action3.name = "Movement 3- Bottom Right"
    action3.application_data = ""

    feedback = base_cyclic.RefreshFeedback()

    cartesian_pose = action3.reach_pose.target_pose
    # These are loaded directly from Kinova Web app (the first three are divided by 100 since it gives them in mm)
    
    cartesian_pose.x = 40/100      # (meters)
    cartesian_pose.y = 6/100     # (meters)
    cartesian_pose.z = 12.1/100      # (meters)
    cartesian_pose.theta_x = 90  # (degrees)
    cartesian_pose.theta_y = 0  # (degrees)
    cartesian_pose.theta_z = 90  # (degrees)

    e = threading.Event()
    notification_handle = base.OnNotificationActionTopic(
        check_for_end_or_abort(e),
        Base_pb2.NotificationOptions()
    )
    print("Executing action")
    base.ExecuteAction(action3)

    print("Waiting for movement to finish ...")
    finished = e.wait(TIMEOUT_DURATION)
    base.Unsubscribe(notification_handle)


# Movement 12
    print("Starting Cartesian action movement ...")
    action3 = Base_pb2.Action()
    action3.name = "Movement 3- Bottom Right"
    action3.application_data = ""

    feedback = base_cyclic.RefreshFeedback()

    cartesian_pose = action3.reach_pose.target_pose
    # These are loaded directly from Kinova Web app (the first three are divided by 100 since it gives them in mm)
    
    cartesian_pose.x = 40/100      # (meters)
    cartesian_pose.y = 6/100     # (meters)
    cartesian_pose.z = 20/100      # (meters)
    cartesian_pose.theta_x = 90  # (degrees)
    cartesian_pose.theta_y = 0  # (degrees)
    cartesian_pose.theta_z = 90  # (degrees)

    e = threading.Event()
    notification_handle = base.OnNotificationActionTopic(
        check_for_end_or_abort(e),
        Base_pb2.NotificationOptions()
    )
    print("Executing action")
    base.ExecuteAction(action3)

    print("Waiting for movement to finish ...")
    finished = e.wait(TIMEOUT_DURATION)
    base.Unsubscribe(notification_handle)


    if finished:
        print("Cartesian movement completed")
    else:
        print("Timeout on action notification wait")
    return finished

def example_angular_trajectory_movement(base):
    
    constrained_joint_angles = Base_pb2.ConstrainedJointAngles()

    actuator_count = base.GetActuatorCount()

    # Place arm straight up
    for joint_id in range(actuator_count.count):
        joint_angle = constrained_joint_angles.joint_angles.joint_angles.add()
        joint_angle.joint_identifier = joint_id
        joint_angle.value = 0

    e = threading.Event()
    notification_handle = base.OnNotificationActionTopic(
        check_for_end_or_abort(e),
        Base_pb2.NotificationOptions()
    )

    print("Reaching joint angles...")
    base.PlayJointTrajectory(constrained_joint_angles)


    print("Waiting for movement to finish ...")
    finished = e.wait(TIMEOUT_DURATION)
    base.Unsubscribe(notification_handle)

    if finished:
        print("Joint angles reached")
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

        #success &= example_cartesian_action_movement(base, base_cyclic)
        #success &= example_angular_action_movement(base)
        success &= example_test_movement(base, base_cyclic)
        #success &= example_angular_trajectory_movement(base)
        
        #success &= example_move_to_pack_position(base)

        return 0 if success else 1

if __name__ == "__main__":
    exit(main())
