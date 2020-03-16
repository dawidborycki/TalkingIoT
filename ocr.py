# Imports
import keras_ocr
import helpers

# Prepare OCR recognizer
recognizer = keras_ocr.recognition.Recognizer()

# Load images and their labels
dataset_folder = 'Dataset'
image_file_filter = '*.jpg'

images_with_labels = helpers.load_images_from_folder(
    dataset_folder, image_file_filter)

# Perform OCR recognition on the input images
predicted_labels = []
for image_with_label in images_with_labels:
    predicted_labels.append(recognizer.recognize(image_with_label[0]))

# Display results
rows = 4
cols = 2
font_size = 14
helpers.plot_results(images_with_labels, predicted_labels, rows, cols, font_size)