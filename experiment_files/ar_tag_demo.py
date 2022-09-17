#/usr/bin/env python3


import roslaunch
import rospy
from std_msgs.msg import Bool

def main():

    pub = rospy.Publisher("/finished", Bool, queue_size=10)
    msg = Bool()
    msg.data = False
    pub.publish(msg)

    uuid = roslaunch.rlutil.get_or_generate_uuid(None, False)
    roslaunch.configure_logging(uuid)
    launch = roslaunch.parent.ROSLaunchParent(uuid, ["/opt/ros/noetic/share/leo_example_follow_ar_tag/launch/follor_ar_tag.launch"])
    launch.start()
    rospy.loginfo("Launched")
    rospy.sleep(45)

    launch.shutdown()

    # publish finished message
    msg.data = True
    pub.publish(msg)


if __name__ == "__main__":
    main()
