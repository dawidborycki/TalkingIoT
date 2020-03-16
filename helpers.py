#Imports
import os
import fnmatch
import matplotlib.pyplot as plt
from tensorflow import keras

def load_images_from_folder(folder, filter):       
    # Get files in the folder
    files = fnmatch.filter(os.listdir(folder), filter)

    # Load all files
    result = []    
    for file in files:
        # Get full file path
        file_path = os.path.join(folder, file)    
                
        # Load image and convert to unit8 array
        img = keras.preprocessing.image.load_img(file_path)    
        img = keras.preprocessing.image.img_to_array(img)

        # Get expected label
        label = file.split('_')[1]

        # Append image with the label
        result.append((img, label))       
        
    return result

def plot_results(images_with_labels, predicted_labels, row_count, col_count, font_size):
    # Prepare plot
    plt.figure()

    # Iterate over rows and cols
    for i in range(row_count * col_count):
        
        plt.subplot(row_count, col_count, i+1)                    

        # Disable ticks
        plt.xticks([])
        plt.yticks([])
        plt.grid(False)

        # Display image
        plt.imshow(images_with_labels[i][0] / 255)

        # Prepare and display actual and predicted labels
        label = predicted_labels[i] + ' (actual: ' + images_with_labels[i][1] + ')'
        plt.xlabel(label, fontsize=font_size)

    
    # Add padding
    plt.tight_layout(pad=1.0)

    # Show plot
    plt.show()

def sayText(text):
    os.system('echo ' + text + ' | festival --tts')
