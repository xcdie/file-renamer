import os


def bulk_rename(directory_path, prefix):
  if not os.path.exists(directory_path):
    print(f'Error: The directory {directory_path} does not exist.')
    return

  files = sorted(os.listdir(directory_path))

  counter = 1
  for filename in files:
    full_path = os.path.join(directory_path, filename)

  
    if os.path.isfile(full_path):
      file_ext = os.path.splitext(filename)[1]
      new_name = f'{prefix}_{counter}{file_ext}'
      new_path = os.path.join(directory_path, new_name)

      os.rename(full_path, new_path)
      print(f'Renamed: {filename} -> {new_name}')
      counter += 1

