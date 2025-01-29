# OneDrive (using rclone)

All tough `rclone` is a command line tool (https://rclone.org/), to configure a OneDrive connection a graphical environment is needed to authorize the connection to Microsoft OneDrive. Configuration of the connection only needs to be done once.

## Start an interactive Desktop Session

Login to [The Umbrella Cluster](https://hpc.tue.nl) and request an Interactive Desktop (Scroll Down to the bottom of the list of Tiles), 1 hour, 1 CPU and 4 GB of memory should be sufficient to finish the configuration.

## Setting up a connection to Microsoft OneDrive

Once the Interactive Desktop session is ready, open a terminal. In the terminal, run the command `rclone config`.

It prompts you with a bunch of questions:

- It shows "No remotes found -- make a new one" or list available remotes you made before
    - Answer "n" for "New remote"
- "name>" (the name for the new remote)
    - Type "OneDrive" (or whatever else you want to call this remote)
- "Storage>" (the storage type of the new remote)
    - This should display a list to choose from. Enter the number corresponding to the "Microsoft OneDrive" storage type, which is "35".
- "client_id>"
    - Leave this blank (just press enter).
- "client_secret>"
    - Leave this blank (just press enter).
- "Choose national cloud region for OneDrive."
    - This should display a list to choose from. Enter the number corresponding to the "Microsoft Cloud Global" region, which is "1".
- "Edit advanced config?"
    - Type "n" for no
- "Use auto config?"
    - Answer "y" for yes
- A web browser window should pop up allowing you to log into box. It is a good idea at this point to verify that the url is actually OneDrive before entering any credentials
    - Enter your TU/e email, Password and MFA
    - This should take you to the OSU login page. Login with your OSU credentials
    - Go back to the terminal once "Success" is displayed.
- "Your choice>"
    - Locate the drive you wish to use.
    - Type "1" to use your personal or business OneDrive
- "Choose drive to use"
    - Locate the option: OneDrive (business)
    - Type the number of the option
- "Is this Okay? y/n>"
    - Type "y" to confirm the drive you wish to use is correct.
- "y/e/d>"
    - Type "y" to confirm you wish to add this remote to rclone.
- "Current remotes:"
    - An remote of type "onedrive" should be avaiable.
    - Type "q" to Quit

Close the terminal (type `exit` of close the window) and end the Interactive Desktop (Left Click on your name in the upper right corner en choose "logout" the press "logout" button).

## Testing the OneDrive Connection (Command Line)

Either use SSH to login into the Umbrella cluster (ssh username@hpc.tue.nl) or use https://hpc.tue.nl to open a terminal.

Create an empty hello.txt file and upload it to OneDrive using 'rclone copy' as below in a terminal:

``` shell
touch hello.txt
rclone copy hello.txt OneDrive:/test
```

This creates a toplevel directory in OneDrive called 'test' if it does not already exist, and uploads the file hello.txt to it.

To verify the uploading is successful, you can either login to OneDrive in a web browser to check the file, or use rclone ls command in the terminal as:

``` shell
rclone ls OneDrive:/test
```

Copy the contents of a source directory from a configured OneDrive remote, OneDrive:/src/dir/path, into a destination directory in your OSC session, /dest/dir/path, using the code below:

``` shell
rclone copy OneDrive:/src/dir/path /dest/dir/path
```
Identical files on the source and destination directories are not transferred. Only the contents of the provided source directory are copied, not the directory name and contents.

copy does not delete files from the destination. To delete files from the destination directory in order to match the source directory, use the sync command instead.

If only one file is being transferred, use the copyto command instead:

``` shell
rclone copyto OneDrive:/test/hello.txt test-onedrive.txt
```

## Testing the OneDrive Connection (Webacces https://hpc.tue.nl)

Login, check the "File" top menu bar option, besides a "Homedrive" there now is a "onedrive" which was configured. Uisng the files browser can be copie from and to the "Homedrive".
