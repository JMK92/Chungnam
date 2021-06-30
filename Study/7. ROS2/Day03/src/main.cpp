#include "TeleopTurtle.h"

int main(int argc, char **argv)
{
    rclcpp::init(argc, argv);
    rclcpp::spin(std::make_shared<TeleopTurtle>());
    rclcpp::shutdown();
    
    return 0;
}