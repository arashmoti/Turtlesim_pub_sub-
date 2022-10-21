#!/usr/bin/env python3
import sys
import rospy 
from first_pkg.srv import posecommand
rospy.init_node("client_node",anonymous=True)
if __name__=="__main__":
    x=int(sys.argv[1])
    y=int(sys.argv[2])
    rospy.wait_for_service("command")
    client=rospy.ServiceProxy("command",posecommand)
    client.call(x,y)
    
