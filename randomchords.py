# import the necessary packages
import argparse
import random
import time
# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-d", "--delay", required=True, help="tiempo de espera")
args = vars(ap.parse_args())

delay = float(args['delay'])
roots = ["A", "B", "C", "D", "E", "F", "G"]
altered = ["", "b", "#"]
quality = ["m7", "maj7", "7", "dim"]

def generate_chord(roots, altered, quality):
	aux = ""
	return aux + random.choice(roots) + random.choice(altered) + " " + random.choice(quality)

count = 0
while count < 50:
	chord = generate_chord(roots, altered, quality)
	print(chord)
	count += 1
	time.sleep(delay)
