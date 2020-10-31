#!/usr/bin/python
import csv
from csv import reader
import glob, os

user = input("insert username:") #count individual user


paths = ['./monday/ras', './monday/wie', './monday/embs', './monday/cs', './monday/mesa',
	'./thursday/industria', './thursday/objetos', './thursday/oportunidades', 
	'./thursday/redes', './thursday/visionartificial', './thursday/computadora',
	'./wednesday/espacio', './wednesday/ingenuidad', './wednesday/musculos', './wednesday/ortesis', 
	'./wednesday/protesis', './tuesday/drone', './tuesday/iamastonta', './tuesday/nlp', './tuesday/racismo',
	'./tuesday/rostros', './tuesday/thomas', './friday/arte', './friday/cats', './friday/pimentel',
	'./friday/sati', './friday/taller']


minutes = 0

for path in paths:
	for filename in glob.glob(os.path.join(path, '*.json')):
		current_file = open(filename, "r")
		print("checking in: " + str(filename))		
		if user in str(current_file.read()):
			minutes += 5
			print("OK")
		current_file.close()

print(user + " time in coference: " + str(minutes) + " minutes "+ str(minutes/60) + " hours")

