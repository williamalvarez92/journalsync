import os

# Determine the user's home directory based on the operating system
if os.name == 'posix':  # macOS and Linux
    user_home = os.path.expanduser("~")
elif os.name == 'nt':  # Windows
    user_home = os.path.expandvars("%USERPROFILE%")

# Define the relative paths from the home directory
relative_origin_folder = "OneDrive\\Documents\\Journals\\test"


# Construct the full paths
origin_folder = os.path.join(user_home, relative_origin_folder)
destination_folder = "G:\\My Drive\\Journals\\test"
