#ifndef SOUND_SRV_H
#define SOUND_SRV_H

#include<rclcpp/rclcpp.hpp>
#include<turtlebot3_msgs/srv/sound.hpp>

class SoundSrv : public rclcpp::Node{
public:

private:
    std::shared_ptr::Client<turtlebot3_msgs::srv::Sound> client;

};

#endif