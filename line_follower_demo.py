#/usr/bin/env python3


import roslaunch
import rospy


def main():

    
    uuid = roslaunch.rlutil.get_or_generate_uuid(None, False)
    roslaunch.configure_logging(uuid)
    launch = roslaunch.parent.ROSLaunchParent(uuid, ["line_follower.launch"])
    launch.start()
    rospy.loginfo("Launched")
    rospy.sleep(45)
    

    launch.shutdown()


if __name__ == "__main__":
    main()
