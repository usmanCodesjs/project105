import os
import cv2

# Set the path to the "Images" folder
image_folder = "C:\Users\usman\OneDrive\Desktop\project105\PRO-C105-Project-Images-main"

# Create a list to store the image file names
images = []

# Loop through the files in the folder
for filename in os.listdir(image_folder):
    # Split the file name and extension
    name, extension = os.path.splitext(filename)
    
    # Check if the file has a valid image extension (e.g., .jpg, .png)
    if extension in ['.jpg', '.jpeg', '.png', '.gif']:
        # Create the full file path
        file_name = os.path.join(image_folder, filename)
        
        # Add the file to the list
        images.append(file_name)
        
# Get the total number of images
count = len(images)

# Read the first image to get its dimensions
frame = cv2.imread(images[0])
height, width, channels = frame.shape

# Create a tuple for the video size
size = (width, height)

# Print the size for verification
print(size)

# Create a VideoWriter object to save the video
out = cv2.VideoWriter('Project.avi', cv2.VideoWriter_fourcc(*'DIVX'), 0.8, size)

# Loop through the images and add them to the video
for i in range(count):
    # Read the current image
    img = cv2.imread(images[i])
    
    # Add the image to the video
    out.write(img)

# Release the video writer
out.release()

# Print a completion message
print("Done")
