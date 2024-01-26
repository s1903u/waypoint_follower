#!/usr/bin/env python
import rclpy
from nav2_simple_commander.robot_navigator import BasicNavigator
from geometry_msgs.msg import PoseStamped
import copy
import pprint

def main():
    rclpy.init()
    navigator = BasicNavigator()
    # Set our demo's initial pose
    inspection_route = [[0.006255, -0.594449, 0], [-1.57, 1.65201, 0],
    [-0.0231, 2.00202, 0], [-0.4861, -1.8063, 0], [999.9, 0.0, 0.0]]
    
    navigator.waitUntilNav2Active()
    i = 0
    while rclpy.ok():
        
        if(i>=len(inspection_route)):
            #ナビゲーション終わり
            print('ナビゲーション終了')
            break

        initial_pose = PoseStamped()
        navigator.setInitialPose(initial_pose)

        for point in inspection_route:
            i=i+1
            print("{}番目のウェイポイントへ行きます".format(i))
            inspection_pose = PoseStamped()
            inspection_pose.header.frame_id = 'map'
            inspection_pose.header.stamp = navigator.get_clock().now().to_msg()
            inspection_pose.pose.orientation.z = 1.0
            inspection_pose.pose.orientation.w = 0.0
            inspection_pose.pose.position.x = point[0]
            inspection_pose.pose.position.y = point[1]

            #start navigation
            nav_start = navigator.get_clock().now()
            navigator.goToPose(inspection_pose)
            
            while not navigator.isTaskComplete():
                #ナビゲーション中の処理
                feedback = navigator.getFeedback()
                
  
            #success or timeout 
            result = navigator.getResult()
            if result.name == 'SUCCEEDED':
                print('Goal succeeded!')
            elif result.name == 'CANCELED':
                print('Goal was canceled!')
            elif result.name == 'FAILED':
                print('Goal failed!')
            
        
    # Wait for navigation to fully activate
    
    

if __name__ == '__main__':
    main()
