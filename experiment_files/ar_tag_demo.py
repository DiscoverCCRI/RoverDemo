#/usr/bin/env python3


import roslaunch
import rospy
from std_msgs.msg import Bool
from rover_api.discover_lidar import Lidar

def main():

    range_finder = Lidar()

    pub = rospy.Publisher("/finished", Bool, queue_size=10)
    msg = Bool()
    msg.data = False
    pub.publish(msg)

    uuid = roslaunch.rlutil.get_or_generate_uuid(None, False)
    roslaunch.configure_logging(uuid)
    launch = roslaunch.parent.ROSLaunchParent(uuid, ["/opt/ros/noetic/share/leo_example_follow_ar_tag/launch/follow_ar_tag.launch"])
    range_finder.start_recording()
    launch.start()

    rospy.loginfo("Launched")
    rospy.sleep(90)

    launch.shutdown()
    range_finder.stop_recording()

    # publish finished message
    msg.data = True
    pub.publish(msg)


if __name__ == "__main__":
    main()