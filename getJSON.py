#!/usr/bin/python3
from datetime import datetime
import urllib.request, json 
import time
from apscheduler.schedulers.blocking import BlockingScheduler

stream_url = "https://tmi.twitch.tv/group/user/ieeeramaestudiantil_itm/chatters"
conference = "taller"


mint = 5

print("Auto IEEE CREW 2020 viewers check started: " + datetime.now().strftime("%H:%M:%S"))
print("Will run every "+ str(mint) +" minutes :)")
print("Stream URL: " + stream_url)
print("Current Conference: "+ conference)
sched = BlockingScheduler()

@sched.scheduled_job('interval', minutes=mint)
def timed_job():
	print("Saved viewers at:", end=" ")
	print(datetime.now())


	now = datetime.now()
	current_time = now.strftime("%H:%M:%S")


	with urllib.request.urlopen(stream_url) as url:
		data = json.loads(url.read())

		fileObj  = open("friday/"+conference +"-"+ current_time+".json", "w+") 

		fileObj.write(str(data))

		fileObj.close()

timed_job()
sched.start()
