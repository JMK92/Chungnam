#include "TeleopPub.h"
#include <termios.h>

int getch(void)
{
    int ch;

    struct termios old;
    struct termios new1;

    tcgetattr(0, &old);

    new1 = old;
    new1.c_lflag &= ~(ICANON|ECHO);
    new1.c_cc[VMIN] = 1;
    new1.c_cc[VTIME] = 0;

    tcsetattr(0, TCSAFLUSH, &new1);
    ch = getchar();
    tcsetattr(0, TCSAFLUSH, &old);

    return ch;
}

int main(int argc, char **argv)
{
    rclcpp::init(argc, argv);
    std::shared_ptr<TeleopPub> teleopPub = std::make_shared<TeleopPub>(); // teleopPub 지역변수
    //rclcpp::spin(teleopTurtle);
    
    for(;;){

        std::cout << "input(i,j,k,m,s,q)";
        char ch;
        //std::cin >> ch; 
        ch = getch();   

        switch(ch){
        case 'i': case 'I':
            teleopPub->move(TeleopPub::DIRECTION_FORWARD);
            break;
        case 'm': case 'M':
            teleopPub->move(TeleopPub::DIRECTION_BACKWARD);
            break;
        case 'j': case 'J':
            teleopPub->move(TeleopPub::ROTATE_LEFT);
            break;
        case 'k': case 'K':
            teleopPub->move(TeleopPub::ROTATE_RIGHT);
            break;
        case 's': case 'S':
            teleopPub->move(TeleopPub::DIRECTION_STOP);
            break;
        case 'q': case 'Q':
            teleopPub->move(TeleopPub::DIRECTION_STOP);         
            goto out; // 중첩된 for문 빠져나걀때는 유용함 그외X
        }
        
    }
    out:
    
    // delete을 안써도 된다.
    rclcpp::shutdown();

    return 0;
}