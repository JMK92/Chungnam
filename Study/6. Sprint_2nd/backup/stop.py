from pop import LiDAR
from pop import Pilot

bot = Pilot.SerBot()
bot.stop()

lidar = LiDAR.Rplidar()
lidar.connect()
lidar.stopMotor()


