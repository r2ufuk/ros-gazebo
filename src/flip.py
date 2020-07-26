#!/usr/bin/env python
"""Habitat: coke.world"""

import rospy
from gazebo_msgs.srv import ApplyBodyWrench
from geometry_msgs.msg import Wrench

rospy.init_node("coke_flip")


def flip():
    try:
        apply_force = rospy.ServiceProxy("/gazebo/apply_body_wrench", ApplyBodyWrench)

        coke_can = "coke_can::link"

        wrench = Wrench()
        wrench.force.x = 3
        wrench.force.z = 9
        wrench.torque.y = -0.03999

        duration = rospy.Duration(0.25)

        apply_force(body_name=coke_can, reference_frame=coke_can, wrench=wrench, duration=duration)

    except rospy.ServiceException as e:
        print(e)


if __name__ == "__main__":
    flip()
