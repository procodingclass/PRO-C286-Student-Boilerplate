from controller import Robot
from controller import Keyboard



robot=Robot()
keyboard = Keyboard()
timestep=64

autoMode= False


wheel1_left=robot.getDevice("wheel1_left")
wheel1_left.setPosition(float('inf'))
wheel1_left.setVelocity(0.0)

wheel1_right=robot.getDevice("wheel1_right")
wheel1_right.setPosition(float('inf'))
wheel1_right.setVelocity(0.0)

wheel2_left=robot.getDevice("wheel2_left")
wheel2_left.setPosition(float('inf'))
wheel2_left.setVelocity(0.0)

wheel2_right=robot.getDevice("wheel2_right")
wheel2_right.setPosition(float('inf'))
wheel2_right.setVelocity(0.0)



position=0
speed=4


keyboard.enable(timestep)


prev_key = 0
key_pressed = -1

while (robot.step(timestep) !=-1):
    

    prev_key=key_pressed
    key_pressed = keyboard.getKey()
   
    # 79 is "o" key
    if(prev_key == -1  and  key_pressed==79):
        autoMode= not autoMode

    
    if(autoMode):                  
        wheel1_left.setVelocity(speed)
        wheel1_right.setVelocity(speed)
        wheel2_left.setVelocity(speed)
        wheel2_right.setVelocity(speed)
       
    
    if(not autoMode):
       
        # 65 is "a" key
        if(key_pressed== 65):
            wheel1_left.setVelocity(-speed)
            wheel1_right.setVelocity(speed)
            wheel2_left.setVelocity(-speed)
            wheel2_right.setVelocity(speed)
            
        # 68 is "d" key    
        if(key_pressed== 68):
            wheel1_left.setVelocity(speed)
            wheel1_right.setVelocity(-speed)
            wheel2_left.setVelocity(speed)
            wheel2_right.setVelocity(-speed)
            
        # 87 is "w" key
        if(key_pressed== 87):
            wheel1_left.setVelocity(speed)
            wheel1_right.setVelocity(speed)
            wheel2_left.setVelocity(speed)
            wheel2_right.setVelocity(speed)
            
        # 83 is "s" key    
        if(key_pressed== 83):
            wheel1_left.setVelocity(-speed)
            wheel1_right.setVelocity(-speed)
            wheel2_left.setVelocity(-speed)
            wheel2_right.setVelocity(-speed)
            
        # if nothing is pressed    
        if(key_pressed== -1):
            wheel1_left.setVelocity(0)
            wheel1_right.setVelocity(0)
            wheel2_left.setVelocity(0)
            wheel2_right.setVelocity(0)
        
