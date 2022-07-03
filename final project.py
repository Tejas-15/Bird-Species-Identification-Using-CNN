from tkinter import *
from PIL import Image, ImageTk
import numpy as np
from keras.models import load_model
from keras.preprocessing import image
import tensorflow as tf 
from tkinter import filedialog


root = Tk()
root.geometry("450x300")
fileButton = Button(root, text='upload Bird image', command=lambda: [UploadAction()])
fileButton.pack()
birdname = Label(root, text = 'Bird name is :').pack()

def UploadAction(event=None):
	global filename
	filename = filedialog.askopenfilename()
	bird = Label(root, text = predict(filename)).pack()


def predict(filename):
	model = tf.keras.Sequential([
	tf.keras.layers.experimental.preprocessing.Rescaling(1./255),
	tf.keras.layers.Conv2D(32, 3, activation='relu'),
	tf.keras.layers.MaxPooling2D(),
	tf.keras.layers.Conv2D(32, 3, activation='relu'),
	tf.keras.layers.MaxPooling2D(),
	tf.keras.layers.Conv2D(32, 3, activation='relu'),
	tf.keras.layers.MaxPooling2D(),
	tf.keras.layers.Flatten(),
	tf.keras.layers.Dense(128, activation='relu'),
	tf.keras.layers.Dense(units=11 , activation='softmax')
	])

	model = load_model(r"bird_model.h5")
	validation_image = image.load_img(filename, target_size=(64,64))
	validation_image = image.img_to_array(validation_image)
	validation_image = np.expand_dims(validation_image,axis=0)
	result = model.predict(validation_image)
	print(result)

	y_predicted = model.predict(validation_image)
	y_predicted[0]

	global cn
	cn=np.argmax(y_predicted[0])
	print(cn)



	if cn==0 :
		return('ALEXANDRINE PARAKEET')
	elif cn==1 :
		return('BALD EAGLE')
	elif cn==2 :
		return('CHIPPING SPARROW')
	elif cn==3 :
		return('COCKATOO')
	elif cn==4 :
		return('CROW')
	elif cn==5 :
		return('FLAMINGO')
	elif cn==6 :
		return('IVORY GULL')
	elif cn==7 :
		return('OSTRICH')
	elif cn==8 :
		return('PEACOCK')
	elif cn==9 :
		return('PELICAN')
	elif cn==10 :
		return('STRIPED OWL')


root.mainloop()