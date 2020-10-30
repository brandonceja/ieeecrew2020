#!/usr/bin/python
import csv
from csv import reader
import glob, os


paths = ['./monday/ras', './monday/wie', './monday/embs', './monday/cs', './monday/mesa',
	'./thursday/industria', './thursday/objetos', './thursday/oportunidades', 
	'./thursday/redes', './thursday/visionartificial', './thursday/computadora',
	'./wednesday/espacio', './wednesday/ingenuidad', './wednesday/musculos', './wednesday/ortesis', 
	'./wednesday/protesis', './tuesday/drone', './tuesday/iamastonta', './tuesday/nlp', './tuesday/racismo',
	'./tuesday/rostros', './tuesday/thomas', './friday/arte', './friday/cats', './friday/pimentel',
	'./friday/sati', './friday/taller']

creditos = 0

with open('control_numbers.csv', 'r') as read_obj:
	with open('asistencia.csv', 'w',  newline='') as write_obj:
		
		csv_reader = reader(read_obj)
		writer = csv.writer(write_obj)
		writer.writerow(["Número de Control", "Tiempo Total en Minutos", "Tiempo Total en Horas"])
		
		for row in csv_reader:
			minutes = 0

			if len(row) > 0:
				for path in paths:
					for filename in glob.glob(os.path.join(path, '*.json')):
						current_file = open(filename, "r")
			
						if row[0] in str(current_file.read()):
							minutes += 5
						current_file.close()
				print(str(row) + " time in coference: " + str(minutes) + " minutes "+ str(minutes/60) + " hours")
				writer.writerow([str(row)[2:-2], str(minutes), str(minutes/60)])

				if minutes/60 >= 18:
					creditos +=1


print("Total de créditos: " + str(creditos))
