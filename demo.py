#/usr/bin/env python3


import roslaunch
import rospy
from rover_api.discover_lidar import Lidar


def main():

    range_finder = Lidar()
    uuid = roslaunch.rlutil.get_or_generate_uuid(None, False)
    roslaunch.configure_logging(uuid)
    launch = roslaunch.parent.ROSLaunchParent(uuid, ["/~/catkin_ws/src/leo_examples/leo_example_follow_ar_tag/launch/follor_ar_tag.launch"])
    range_finder.start_recording()
    launch.start()
    rospy.loginfo("Launched")
    rospy.sleep(45)
    range_finder.stop_recording()

    launch.shutdown()


if __name__ == "__main__":
    main()
