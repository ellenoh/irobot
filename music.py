import robot
import time

r = robot.Robot()

jingle_bells = [64, 12, 64, 12, 64, 24, 64, 12,
                64, 12, 64, 24, 64, 12, 67, 12,
                60, 12, 62, 12, 64, 24]

r.defineSong(3, jingle_bells)

william_tell = [60, 12, 60, 12, 60, 24,
                60, 12, 60, 12, 60, 24,
                60, 12, 60, 12, 65, 24, 67, 24, 69, 24]

r.defineSong(15, william_tell)

print ("Press 1 to play Jingle Bells")
print ("Press 2 to play William Tell")
print ("Press 'q' to quit")

while True:
    choice = input()
    if choice == '1':
        r.playSong(3)
    elif choice == '2':
        r.playSong(15)
    elif choice == 'q':
        break
    else:
        print ("That is not a choice.")
