# virtualbox-CLI

This simple tool allows us to interact with VirtualBox and:

    Open an existing VM.
    Close an open VM.
    Create a VM (in progress)
    Delete a VM (in progress)

To run the project:

## Installation

1. Go to VirtualBox's downloads page (https://www.virtualbox.org/wiki/Downloads) and download the VirtualBox SDK. Within the extracted ZIP file there is a directory called "installer". Open a console within the installer directory and run python vboxapisetup.py install using your system Python. This installs vboxapi which is the interface that talks to VirtualBox via COM.

2. Next is to install this library; for that, our project brings a requirements.txt with the required dependencies to install.
   To execute it, type into your project folder console, pip install -r requirements.txt

3. type "python main.py" into your terminal and the will start.
   Then, our CLI will guide you to choose from different commands!

Cheers!
