import serial
import time
import sys, select, termios, tty

# read keyboard input continuously. Don't edit this function
def getKey():
	tty.setraw(sys.stdin.fileno())
	select.select([sys.stdin], [], [], 0)
	key = sys.stdin.read(1)
	termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
	return key
settings = termios.tcgetattr(sys.stdin)


# map input keys to servo angles. Modify this to work with your design
angleMap = {
		'1':b'000',
		'2':b'025',
		'3':b'050',
		'4':b'075'
	   }


ser = serial.Serial('/dev/ttyACM0')
print('Servo Control. Hit \'q\' to quit')


stay = True
while stay:
	n = getKey();
	if n == 'q':
		stay = False
	elif n in angleMap.keys():
		print(angleMap[n])
		ser.write(angleMap[n])
