import os

def rename_images(folder_path,new_name_prefix):
  # Get all files in the folder
  files = os.listdir(folder_path)

  # Iterate through each file
  for index, file in enumerate(files):
    if not file.endswith('.jpg'):
      continue

    # Generate the new file name
    file_name, file_extension = os.path.splitext(file)
    new_file_name = f'{new_name_prefix}{index+1}{file_extension}' 

    # Rename the file
    old_file_path = os.path.join(folder_path, file)
    new_file_path = os.path.join(folder_path, new_file_name)
    os.rename(old_file_path, new_file_path)

# Example usage
folder_path = ''
new_name_prefix = ''
rename_images(folder_path,new_name_prefix)
