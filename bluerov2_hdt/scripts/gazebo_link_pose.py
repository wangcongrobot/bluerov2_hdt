#!/usr/bin/env python

import rospy
from gazebo_msgs.msg import LinkStates
from geometry_msgs.msg import Pose

class GazeboLinkPose(object):
    def __init__(self, link_name='bluerov2::bluerov2/base_link'):
        self.link_name = link_name
        self.link_pose = Pose()
        self.link_name_rectified = link_name.replace("::", "_")

        if not self.link_name and self.link_name:
            raise ValueError("'link_name' is an empty string")
        
        self.states_sub = rospy.Subscriber("/gazebo/link_states", LinkStates, self.callback)

        self.link_pose_pub = rospy.Publisher("/gazebo/" + self.link_name_rectified, Pose, queue_size=1)

    def callback(self, data):
        try:
            ind = data.name.index(self.link_name)
            self.link_pose = data.pose[ind]
        except ValueError:
            pass
    
    def run(self):
        rate = rospy.Rate(10)
        while not rospy.is_shutdown():
            self.link_pose_pub.publish(self.link_pose)
            print("rov base link pose: ", self.link_pose)
            rate.sleep()

if __name__ == '__main__':
    try:
        rospy.init_node('gazebo_link_pose', anonymous=True)
        gp = GazeboLinkPose()
        
        gp.run()

    except rospy.ROSInterruptException:
        pass