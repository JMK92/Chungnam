#include <memory>
#include<chrono>
#include<rclcpp/rclcpp.hpp>
#include<turtlebot3_msgs/srv/sound.hpp>

using namespace std::chrono_literals;

int main(int argc, char **argv)
{
    rclcpp::init(argc, argv);

    std::shared_ptr<rclcpp::Node> node = rclcpp::Node::make_shared("sound_srv");
    
    rclcpp::Client<turtlebot3_msgs::srv::Sound>::SharedPtr client = 
    node->create_client<turtlebot3_msgs::srv::Sound>("/sound");

    auto request = std::make_shared<turtlebot3_msgs::srv::Sound::Request>();
    request->value = 0; // 1, 2, 3

    while (!client->wait_for_service(1s)){
        RCLCPP_INFO(rclcpp::get_logger("rclcpp"), "waiting service");
    }

    auto result = client->async_send_request(request);
    if(rclcpp::spin_until_future_complete(node, result) == rclcpp::executor::FutureReturnCode::SUCCESS){

        RCLCPP_INFO(rclcpp::get_logger("rclcpp"), "sucess");        
    }else{
        RCLCPP_INFO(rclcpp::get_logger("rclcpp"), "fail");
    }

    rclcpp::shutdown();
    return 0;

}