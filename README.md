Dropbox folder size
===================
Estimated time from setup to use: 5-10 mins. This code has been tested on Ubuntu 14.04 LTS with Python 2.7. Used technology: Dropbox Core API. Alternative is using a RESTful client, check out https://www.dropbox.com/developers/core/docs/python.

Prepare your local machine
--------------------------
1. Get Dropbox Core API for Python. Takes 1 min to download, unzip and install https://www.dropbox.com/developers/core/sdks/python

2. The unpacked folder was in my case dropbox-python-sdk-2.1.0. Find and open the file dropbox-python-sdk-2.1.0/example/cli_client.py with your favourite editor.

3. Insert my code before the do_ls() function.
Prepare your Dropbox
--------------------
Grant your Python app access to your Dropbox account:

1. Create a new Dropbox Platform app https://www.dropbox.com/developers/apps/create. Choose "Dropbox API app", "Files and datastores", "not limited to own folder", "access to all file types". Name the app something like "MyFolderSizeApp".

2. Copy-paste the provided App key and App secret into cli_client.py (variables near the top of the file).

3. Run the cli_client.py file, type login and press Enter. Go to the link provided, allow the app and copy-paste the provided authorization code into the console.
Run
---
Verify that you are logged in by typing ls. You will get the root folder contents.

1. Type folder_size and press Enter
