import speech_recognition
import pyttsx3
from datetime import date, datetime


while True:
	robot_mouth = pyttsx3.init()
	robot_ear = speech_recognition.Recognizer()
	robot_brain=""
	with speech_recognition.Microphone() as mic:
		print("AI: I'm Listening")
		audio = robot_ear.listen(mic)
		print("Processing .....")
	try:
		you = robot_ear.recognize_google(audio)
	except:
		you=""

	print("You " +you)

	if you=="":
		robot_brain="I can't hear you, try again"
	elif "name" in you:
		robot_brain="You are fuck boy"
	elif "hello" in you:
		robot_brain ="Hello coin card"
	elif "today" in you:
		today = date.today()
		robot_brain = today.strftime("%B %d, %Y")
	elif "time" in you:
		now=datetime.now()
		robot_brain=now.strftime("%H hours %M minutes %S seconds")
	elif "Daddy " in you:
		robot_brain="You are daddy"	
	elif "bye" in you:
		robot_brain="Bye bye"
		print("AI :"+robot_brain)
		break
	else:
		robot_brain="Daddy, I can't hear you"


	print("AI :"+robot_brain)
	robot_mouth.say(robot_brain)
	robot_mouth.runAndWait()