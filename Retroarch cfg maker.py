import os

# Set the directory containing the PNG files
directory = os.path.dirname(os.path.abspath(__file__))

# Iterate through all the files in the directory
for filename in os.listdir(directory):
    # Check if the file is a PNG
    if filename.endswith(".png"):
        # Get the file name without extension
        name_without_ext = os.path.splitext(filename)[0]
        
        # Create the content for the .cfg file
        cfg_content = f"""overlays = 1

overlay0_overlay = {filename}

overlay0_full_screen = true

overlay0_descs = 0:"""
        
        # Write the content to a .cfg file with the same base name as the PNG
        cfg_filename = os.path.join(directory, f"{name_without_ext}.cfg")
        with open(cfg_filename, 'w') as cfg_file:
            cfg_file.write(cfg_content)

print("CFG files created successfully.")