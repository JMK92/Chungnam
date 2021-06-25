from pop import LiDAR

lidar = LiDAR.Rplidar()
lidar.connect()
lidar.startMotor()

vectors = lidar.getVectors() 

for i in range(5):
    
    for v in vectors:
        print("angle: ", v[0], "distance: ", v[1])


lidar.stopMotor()