# bluerov2_hdt

BlueROV2 with HDT arm in UUVSimulator. This repository is in development. 


## Install

```
cd ~/catkin_ws/src
git clone -b realistic-sonar-sim-48 https://github.com/NickSadjoli/uuv_simulator.git 
git clone https://github.com/wangcongrobot/uuv_hdt_manpulator.git
git clone https://github.com/wangcongrobot/bluerov2.git
git clone https://github.com/YanielCarreno/orcawp1_integration.git
git clone https://github.com/wangcongrobot/bluerov2_hdt.git
cd ..
catkin_make
source devel/setup.bash
```

```
roslaunch bluerov2_hdt integration_scenario_bluerov2.launch
rosrun bluerov2_hdt move_arm.py
roslaunch uuv_control_utils send_waypoints_file.launch uuv_name:=bluerov2
```
Move BlueROV2 and HDT arm:
![bluerov2_hdt_ocrasim](images/bluerov2_arm_ocrasimx2.gif)

ArUco marker detection:
![aruco_detection](image/../images/bluerov2_arm_aruco_detectionx2.gif)

You can use keyboard to control the bluerov2:
![keyboard](images/keyboard.png)