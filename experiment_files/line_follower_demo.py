# /usr/bin/env python3


import roslaunch
import rospy
from std_msgs.msg import Bool
from rover_api.discover_camera import Camera


def main():

    cam = Camera()
    uuid = roslaunch.rlutil.get_or_generate_uuid(None, False)

    pub = rospy.Publisher("/finished", Bool, queue_size=10)
    msg = Bool()
    msg.data = False
    pub.publish(msg)

    roslaunch.configure_logging(uuid)
    launch = roslaunch.parent.ROSLaunchParent(uuid, ["line_follower.launch"])
    launch.start()
    cam.start_recording()
    rospy.loginfo("Launched")
    rospy.sleep(45)
    cam.stop_recording()

    launch.shutdown()

    # publish finished message
    msg.data = True
    pub.publish(msg)


if __name__ == "__main__":
    main()
