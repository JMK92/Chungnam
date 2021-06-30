#include "TeleopTurtle.h"

int main(int argc, char **argv)
{
    rclcpp::init(argc, argv);
    std::shared_ptr<TeleopTurtle> teleopTurtle = std::make_shared<TeleopTurtle>();
    //rclcpp::spin(teleopTurtle);
    
    for(;;){

        std::cout << "input(i,j,k,l)";
        char ch;
        std::cin >> ch;    

        switch(ch){
        case 'i': case 'I':
            teleopTurtle->foward();
            break;
        case 'm': case 'M':
            teleopTurtle->backward();
            break;
        case 'j': case 'J':
            teleopTurtle->rotateLeft();
            break;
        case 'k': case 'K':
            teleopTurtle->rotateRight();
            break;
        }
        
    }
    
    
    rclcpp::shutdown();

    return 0;
}