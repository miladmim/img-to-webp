from PIL import Image
import os
import shutil

# Define the path of the folder containing images
input_folder = "photo"

# Define the path of the folder where you want to save the webp images
output_folder = "webp"

# Define the path of the folder for corrupted files
error_folder = "error"

# Ensure that the output folders exist, if not, create them
if not os.path.exists(output_folder):
    os.makedirs(output_folder)
if not os.path.exists(error_folder):
    os.makedirs(error_folder)

# List all files in the input folder
files = os.listdir(input_folder)

# Variable to count the number of successful files
successful_files = 0

# Variable to count the number of corrupted files
failed_files = 0

# Loop over each file
for file in files:
    # Ensure the file is an image
    if file.endswith((".jpg", ".jpeg", ".png")):
        # Define the input and output file paths
        input_path = os.path.join(input_folder, file)
        output_path = os.path.join(output_folder, os.path.splitext(file)[0] + ".webp")

        # Open the image
        try:
            image = Image.open(input_path)
        except Exception as e:
            print(f"Error opening file {file}: {e}")
            shutil.move(input_path, os.path.join(error_folder, file))
            failed_files += 1
            continue

        # Save the image in webp format
        try:
            image.save(output_path, "WEBP")
            successful_files += 1
        except Exception as e:
            print(f"Error saving file {file}: {e}")
            shutil.move(input_path, os.path.join(error_folder, file))
            failed_files += 1
            continue

        # Close the image
        image.close()

    # Move webp files to the corresponding folder
    elif file.endswith(".webp"):
        shutil.move(os.path.join(input_folder, file), os.path.join(output_folder, file))
        
# Display information at the end of execution
total_files = len(files)
print("Number of successful files: ", successful_files)
print("Number of corrupted files: ", failed_files)
print("Progress percentage: ", successful_files / total_files * 100 if total_files > 0 else 0)
