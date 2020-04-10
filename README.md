# corona_avijan.O
This is the covid19 planning from us.
1. Drone based face tracking

ABSTRACT
The objective is to identify  and track criminal  and help police to capture criminal by sending a mail to the Police Station along with the information of that criminal.

FACE MATRIX PREPARATION
Face data of criminal is stored in the form of a  matrix. This face data is matches with the face data that is stored in the Criminal Database.

FACE TRACKING
The drone camera detects the midpoint of face and it tries to minimize the distance between Drone Camera Midpoint and Face Midpoint with the help of drone’s PID controller. Thus the drone tracks the criminal.

RESULT & DISCUSSION
e-mail to Nearest P.S.
As soon as drone detects the criminal, an EMAIL is sent to the nearest Police Station along with the previous Criminal Records.

CONCLUSION
 Criminals detected with 88% accuracy.
Drone follows to criminals
Send Picture, information and location
Some issues faced during the project :
Wi-Fi range
Short battery life
Face  Alignment problem

2. Groud robot based on RPLIDAR&SLAM and Deep Learning (ROS)
corona_fight robot
When we are give the goal poition then robot try to reach at desired
position with obstacle avoidance.
Step:-
        1.cd catkin_ws
        2.cd src/
        3. past the mowgli folder
        4. cd ..
        5. catkin_make
        6.source devel/setup.bash
        7. roslaunch mowgli mowgli.launch
        8.we shall move the robot with the help of teleop_twist_keyboard and map
        of the environment created.
        9.After creating the map we need to save the map. With the help of this
        command rosrun map_server map_saver -f test_map map will be saved.
        10. roslaunch mowgli mowgli_map.launch With the help of this command
        robot can move at goal point with obstacle avoid.

3. Face-attendance system and aadhar card scanning using Image processing
In this section We are going to propose you the aadhar card scanning and data storing and face attendence system. 
We have developed an innovative project using Advance Deep Learning by incorporating their insights from Machine Learning curriculum that facilitates direct uploading of government corona attendance through excel/csv files. 
