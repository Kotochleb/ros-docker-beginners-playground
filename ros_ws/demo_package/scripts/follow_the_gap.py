#!/usr/bin/env python3

import rospy
import numpy as np
import time

from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan


class LaserFollowGapNode:
    def __init__(self):
        ''' initialise DemoNode object '''
        # Register ROS node
        rospy.init_node('laser_follow_gap_node')
        
        # Predefine variables
        self._longest_beam_angle = None
        self._longest_beam_distance = None

        # Controller gains
        self._angular_gain = 0.5
        self._linear_gain = 0.1

        # If angle difference is bigger than heading angle (heading is rotation in place) only rotate
        self._heading_angle = np.pi/4 # +-45 degree
        
        # Define subscriber and publisher
        self._cmd_vel_publisher = rospy.Publisher('cmd_vel', Twist, queue_size=10)
        self._laser_subscriber = rospy.Subscriber('/laser/scan', LaserScan, self._laser_callback)

        # Create mesage object
        self._vel_msg = Twist()
        
        # Await messages to start being published
        while not rospy.wait_for_message('/laser/scan', LaserScan):
            rospy.logwarn(f'awaiting /laser/scan topic')
            time.sleep(1)

        # Run controll loop with 10Hz frequency calling _control_loop callback
        self._lights_controller_timer = rospy.Timer(rospy.Duration(0.05), self._control_loop)

        # Notify user that node started
        rospy.loginfo(f'{rospy.get_name()} started')


    def _control_loop(self, *args):
        '''executes main controll loop'''

        # Find smallest angle difference between current rotation and desired rotation
        smallest_angle = np.arctan2(np.sin(self._longest_beam_angle), np.cos(self._longest_beam_angle))
        self._vel_msg.angular.z = smallest_angle * self._angular_gain

        # If smallest angle is grater than heading rotate in place
        if np.abs(smallest_angle) > self._heading_angle:
            self._vel_msg.linear.x = 0.0
        else:
            # Scale velocity command with respect to maximal distance
            self._vel_msg.linear.x = self._longest_beam_distance * self._linear_gain

        # Publish velocity
        self._cmd_vel_publisher.publish(self._vel_msg)

        
    def _laser_callback(self, scan):
        '''laser topic callback'''
        # Remove all infinities
        ranges = np.array(scan.ranges)
        ranges[ranges >= scan.angle_max] = scan.range_min
        # Find reachable maximum
        idx = np.argmax(ranges, axis=0)
        beam_count = len(ranges)
        
        self._longest_beam_distance = ranges[idx]
        # Clip longest beam to max 10 meters
        self._longest_beam_distance = np.clip(self._longest_beam_distance, 0, 25)
        self._longest_beam_angle = (idx/beam_count) * np.abs(scan.angle_max-scan.angle_min) + scan.angle_min


def main():
    try:
        follow_the_gap = LaserFollowGapNode()
        rospy.spin()
    except Exception as e:
        rospy.logerr(f'laser_follow_gap_node error: {e}')
        exit(1)


if __name__ == '__main__':
    main()