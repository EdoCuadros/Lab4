import rospy
from std_msgs.msg import String
from sensor_msgs.msg import JointState
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint

def joint_publisher():
    pub = rospy.Publisher('/joint_trajectory', JointTrajectory, queue_size=0)
    rospy.init_node('joint_publisher', anonymous=False)
    
    while not rospy.is_shutdown():
        state = JointTrajectory()
        state.header.stamp = rospy.Time.now()
        state.joint_names = ["joint_1","joint_2","joint_3","joint_4","joint_5",]
        point = JointTrajectoryPoint()
        point.positions = [0, 0, 0, 0, 0]    
        point.time_from_start = rospy.Duration(0.5)
        state.points.append(point)
        pub.publish(state)
        print('published command')
        rospy.sleep(1)
        state = JointTrajectory()
        state.header.stamp = rospy.Time.now()
        state.joint_names = ["joint_1","joint_2","joint_3","joint_4","joint_5",]
        point = JointTrajectoryPoint()
        point.positions = [0.4363, 0.4363, 0.3490,-0.3490, 0]    
        point.time_from_start = rospy.Duration(0.5)
        state.points.append(point)
        pub.publish(state)
        print('published command')
        rospy.sleep(1)
        state = JointTrajectory()
        state.header.stamp = rospy.Time.now()
        state.joint_names = ["joint_1","joint_2","joint_3","joint_4","joint_5",]
        point = JointTrajectoryPoint()
        point.positions = [-0.6108, 0.6108, -0.5235, 0.5235, 0]    
        point.time_from_start = rospy.Duration(0.5)
        state.points.append(point)
        pub.publish(state)
        print('published command')
        rospy.sleep(1)
        state = JointTrajectory()
        state.header.stamp = rospy.Time.now()
        state.joint_names = ["joint_1","joint_2","joint_3","joint_4","joint_5",]
        point = JointTrajectoryPoint()
        point.positions = [1.4835, -0.3490, 0.9599, 0.4363, 0]    
        point.time_from_start = rospy.Duration(0.5)
        state.points.append(point)
        pub.publish(state)
        print('published command')
        rospy.sleep(1)
        state = JointTrajectory()
        state.header.stamp = rospy.Time.now()
        state.joint_names = ["joint_1","joint_2","joint_3","joint_4","joint_5",]
        point = JointTrajectoryPoint()
        point.positions = [1.3962, -0.6108, 0.9599, -0.7853, 0]    
        point.time_from_start = rospy.Duration(0.5)
        state.points.append(point)
        pub.publish(state)
        print('published command')
        rospy.sleep(1)

if __name__ == '__main__':
    try:
        joint_publisher()
    except rospy.ROSInterruptException:
        pass

