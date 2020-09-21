import face_recognition
import cv2
import os

KNOWN_FACES = 'known_faces'
UNKNOWN_FACES = 'unknown_faces'
THRESHOLD = 0.6
frame_thick = 3
font = 2
model = 'cnn'

known_faces = []
known_name = []

if KNOWN_FACES not in os.listdir(os.getcwd()):
	os.mkdir(KNOWN_FACES)

if UNKNOWN_FACES not in os.listdir(os.getcwd()):
	os.mkdir(UNKNOWN_FACES)

print('processing known_faces')

for name in os.listdir(KNOWN_FACES):

	for filename in os.listdir(f"{KNOWN_FACES}/{name}"):

		image = face_recognition.load_image_file(f"{KNOWN_FACES}/{name}/{filename}")

		try:
			encoding = face_recognition.face_encodings(image)
			known_faces.append(encoding[0])
			known_name.append(name)

		except:
			pass


print('processing unknown_faces')

for filename in os.listdir(UNKNOWN_FACES):

	image = face_recognition.load_image_file(f"{UNKNOWN_FACES}/{filename}")
	locations = face_recognition.face_locations(image, model = model)
	encoding = face_recognition.face_encodings(image, locations)
	image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

	for face_encoding, face_location in zip(encoding, locations):
		results = face_recognition.compare_faces(known_faces, face_encoding, THRESHOLD)
		match = None
		if True in results:
			match = known_name[results.index(True)] ### This is only for the first match
			print(f"Match Found: {match}")

			top_left = (face_location[3]-5, face_location[0]-5)
			bottom_right = (face_location[1]+5, face_location[2]+5)
			color = [0, 255, 255]

			cv2.rectangle(image, top_left, bottom_right, color, frame_thick)

			top_left = (face_location[3], face_location[2])
			bottom_right = (face_location[1], face_location[2]+20)

			cv2.rectangle(image, top_left, bottom_right, [0,255,255], -1)
			cv2.putText(image, match, (face_location[3] + 10, face_location[2] + 15),
						cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0,0,200))

		cv2.imshow(filename, image)
		cv2.waitKey(0)
		cv2.destroyWindow(filename)



