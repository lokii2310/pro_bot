import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

def image_callback(msg):
    bridge = CvBridge()
    cv_image = bridge.imgmsg_to_cv2(msg, "bgr8")
    cv2.imshow("ROS Video Stream", cv_image)
    cv2.waitKey(1)

def main():
    rospy.init_node("video_stream_node")
    rospy.Subscriber("/camera/image_raw", Image, image_callback)
    rospy.spin()

if __name__ == "__main__":
    main()