'''
os module in Python provides a way of using operating system-dependent functionality like reading or writing to the file system, managing processes, and handling environment variables.
Here are some commonly used functions and features of the os module:
1. Importing the os module:
   ```python
   import os
   ```
2. File and Directory Operations:
    - `os.getcwd()`: Returns the current working directory.
    - `os.chdir(path)`: Changes the current working directory to the specified path.
    - `os.listdir(path)`: Returns a list of files and directories in the specified path.
    - `os.mkdir(path)`: Creates a new directory at the specified path.
    - `os.makedirs(path)`: Creates a new directory and any necessary parent directories.
    - `os.remove(path)`: Deletes the file at the specified path.
    - `os.rmdir(path)`: Deletes the empty directory at the specified path.
    - `os.rename(src, dst)`: Renames a file or directory from src to dst.
    - `os.path.join(path, *paths)`: Joins one or more path components intelligently.
3. Environment Variables:
    - `os.getenv(key, default=None)`: Returns the value of the environment variable key if it exists, otherwise returns default.
    - `os.environ`: A dictionary representing the string environment.
4. Process Management:
    - `os.system(command)`: Executes the command (a string) in a subshell
    - `os.getpid()`: Returns the current process ID.
    - `os.getppid()`: Returns the parent process ID.
5. File Permissions and Status:
    - `os.stat(path)`: Returns information about the specified path (like size, modification time, etc.).
    - `os.chmod(path, mode)`: Changes the mode (permissions) of the specified path.
6. Path Manipulations:
    - `os.path.exists(path)`: Returns True if the path exists, otherwise False.
    - `os.path.isfile(path)`: Returns True if the path is a file, otherwise False.
    - `os.path.isdir(path)`: Returns True if the path is a directory, otherwise False.
    - `os.path.abspath(path)`: Returns the absolute path of the specified path. 
These are just a few examples of what the os module can do. It is a powerful module that allows you to interact with the operating system in a platform-independent way.
'''
# from nt import environ
import os
import time

# File and Directory Operations:
print(os.getcwd())
# os.chdir(path)`: Changes the current working directory to the specified path.
# print(os.chdir('C:\\Users\\G SAIKUMAR')) # Change the path as per your system
# print(os.getcwd()) # Verify the change
print(os.listdir()) # List files and directories in the current directory
# os.mkdir('new_directory') # Create a new directory
# os.rename('new_directory', 'renamed_directory') # Rename the directory
# os.rmdir('renamed_directory') # Remove the directory
# print(os.path.join(os.getcwd(), 'example.txt')) # Join paths
# print(os.path.abspath('example.txt')) # Get absolute path
# os.remove('example.txt') # Remove a file
# Environment Variables:
# print(os.getenv('PATH')) # Get the PATH environment variable
# print(os.environ) # Print all environment variables

# Process Management:
# print(os.getpid()) # Get current process ID
# print(os.getppid()) # Get parent process ID
# a= os.system('echo Hello, World!') # Execute a command in the shell
# print(a)


# Path Manipulations:

# print(os.path.exists('test1.txt')) # Check if a path exists
# print(os.path.isfile('test1.txt')) # Check if it's a file
# print(os.path.isdir('test1.txt')) # Check if it's a directory
# print(os.path.isdir(os.getcwd())) # Check if current working directory is a directory
# # File Permissions and Status:
# print(os.stat('test1.txt')) # Get file status

# os module with time module
print("Current Time:", time.ctime(os.path.getctime('test1.txt'))) # Get creation time of a file
print("Last Modification Time:", time.ctime(os.path.getmtime('test1.txt'))) # Get last modification time of a file
print("Last Access Time:", time.ctime(os.path.getatime('test1.txt'))) # Get last access time of a file

os.chdir('renamed_directory') # Change the path as per your system
# os.mkdir('parent_directory') # Create a new directory
# os.makedirs('parent_directory/child_directory/grandchild_directory') # Create nested directories
# print(os.listdir('parent_directory')) # List files and directories in the specified path
# os.removedirs('parent_directory/child_directory/grandchild_directory') # Remove nested directories
# create a file inside the renamed_directory
with open('example.txt', 'w') as f:
    f.write('This is an example file.')
# remove the file inside the renamed_directory
# os.remove('example.txt')
os.chdir('..') # Go back to the previous directory
print(type(os.environ)) # Print the type of os.environ
print(environ.__class__)
print(dir(environ)) # Print the attributes and methods of os.environ
# print(os.environ) # Print all environment variables
