from asyncio.windows_events import NULL
from PIL import Image
from subprocess import Popen
from PIL import ImageGrab
from pyzbar.pyzbar import decode
import os
import time
import tkinter as tk
import sv_ttk
from tkinter import ttk
import requests

# Capturing script run timestamp
programStart = time.time()
# File for temp image captured by user with snipping tool
capturedQR = 'qr.png'
# Fake generated temp image if no image is detected in the user's clipboard when script starts running
fakeQR = 'placeholder.png'

decodedQRtxt = 'decodedQR.txt'
decodedQRpng = 'decodedQR.png'

# Function to cleanup temp files from last run
def tempFileCleanup():
    if (os.path.exists(capturedQR) == True):
        os.remove(capturedQR)
    if (os.path.exists(fakeQR) == True):
        os.remove(fakeQR)
    if (os.path.exists(decodedQRtxt) == True):
        os.remove(decodedQRtxt)
    if (os.path.exists(decodedQRpng) == True):
        os.remove(decodedQRpng)

# Function to decode QR code from from Snipping Tool selection
def captureAndDecodeQR():
    global QRContents
    #Clearing and renaming the text field so we can write to it
    field.configure(state="normal")
    field.delete(1.0, tk.END)
    # Making sure temp files were cleared out from last run
    tempFileCleanup()
    # Check user's clipboard for to see if there's already an existing image there, decode it, and set it to starting clipboard contents
    try:
        startingClipboard = ImageGrab.grabclipboard()
        startingContents = list(startingClipboard.getdata())
    # If no image detected, set decoded clipboard contents to the fake generated temp image
    except:
        fakeImage = Image.new("RGB", size=(10, 10), color='black')
        fakeImage.save(fakeQR)
        startingClipboard = Image.open(fakeQR)
        startingContents = list(startingClipboard.getdata())

    # Launch snipping tool
    Popen("start ms-screenclip:", shell=True)

    # Waiting for file creation which indicates clipboard change
    # In short, when the file exists, we know the user's clipboard is different than when we started and can exit the loop
    while os.path.exists(capturedQR) == False:
        # Checking for new clipboard contents
        try:
            newClipboards = ImageGrab.grabclipboard()
            newContents = list(newClipboards.getdata())
        # Passing exception if user still doesn't have a clipboard image
        except:
            pass
        # Checking if new clipboard contents have been detected
        if ('newContents' in locals()):
            # Same contents as when we started, sleep and loop again
            if (newContents == startingContents):
                time.sleep(.1)
            # Success! New clipboard image detected. Save to a file that will exit the loop
            else:
                newClipboards.save(capturedQR)

    # Decode new QR
    decodedQR = decode(Image.open(capturedQR))

    # Extract string from decoded QR
    try:
        QRContents = decodedQR[0][0]
        QRContents = QRContents.decode()
    except:
        QRContents = "QR code not read. Please try again."

    # Write decoded QR to text field
    field.insert(tk.INSERT, QRContents)
    field.configure(state="disabled")

#function to copy the contents of the field to the clipboard
def copyToClipboard():
    try:
        #Making sure we're not copying text thats not a decoded QR or the update URL
        if (QRContents != "QR code not read. Please try again.") and ("https://github.com/MarkHopper24/QRDecoder" not in QRContents) and QRContents != "You are running the latest version of QRDecoder.":
            root.clipboard_clear()
            root.clipboard_append(QRContents)
        if ("https://github.com/MarkHopper24/QRDecoder" in QRContents):
            root.clipboard_clear()
            root.clipboard_append("https://github.com/MarkHopper24/QRDecoder")
    except:
        pass

#function to save and open the contents of QRContents to a text file
def saveToTextFile():
    try:
        #Making sure we're not saving text thats not a decoded QR
        if (QRContents != "QR code not read. Please try again.") and ("https://github.com/MarkHopper24/QRDecoder" not in QRContents) and QRContents != "You are running the latest version of QRDecoder.":
            f = open(decodedQRtxt, "w")
            f.write(QRContents)
            f.close()
            #Opening the text file
            Popen("start " + decodedQRtxt, shell=True)
    except:
        pass

#function to open capturedQR in the default image viewer
def openImage():
    try:
        if (QRContents != "QR code not read. Please try again.") and ("https://github.com/MarkHopper24/QRDecoder" not in QRContents) and QRContents != "You are running the latest version of QRDecoder.":
            Popen("start " + capturedQR, shell=True)
    except:
        pass

#function check to see if new version is available on github
def checkForUpdate():
    global QRContents
    field.configure(state="normal")
    field.delete(1.0, tk.END)
    currentVersion = "1.2"
    try:
        response = requests.get(
            "https://api.github.com/repos/MarkHopper24/QRDecoder/releases/latest")
        releaseName = response.json()["name"]
        #remove "Version " from the release name
        releaseName = releaseName[8:]
        if (releaseName > currentVersion):
            QRContents = "Update available! \n \nPlease visit https://github.com/MarkHopper24/QRDecoder/releases to download the latest version of QRDecoder."
        else:
            QRContents = "You are running the latest version of QRDecoder."
    except:
        QRContents = "You are running the latest version of QRDecoder."
    field.insert(tk.INSERT, QRContents)
    field.configure(state="disabled")

# Create GUI + apply theme
root = tk.Tk()

root.title("QRDecoder")
root.attributes('-topmost', True)
root.iconphoto(False, tk.PhotoImage(file='Logo.png'))

sv_ttk.set_theme("dark")
sv_ttk.use_dark_theme()

buttonFrame = ttk.Frame(root, borderwidth=0)
buttonFrame.grid(row=0, column=0, sticky='nsew')


#create button to restart script
restartButton = ttk.Button(buttonFrame, text="Capture QR Code",
                           command=captureAndDecodeQR, style="Accent.TButton")
restartButton.pack(in_=buttonFrame, side='top', fill='both', expand=True)

#create button to copy decoded QR to clipboard
copyButton = ttk.Button(
    buttonFrame, text="Copy to Clipboard", command=copyToClipboard)
copyButton.pack(in_=buttonFrame, side='top', fill='both', expand=True)

#create button to save decoded QR to text file
saveButton = ttk.Button(
    buttonFrame, text="Open as Text File", command=saveToTextFile)
saveButton.pack(in_=buttonFrame, side='top', fill='both', expand=True)

#create button to open capturedQR in the default image viewer
openImageButton = ttk.Button(
    buttonFrame, text="Open as PNG File", command=openImage)
openImageButton.pack(in_=buttonFrame, side='top', fill='both', expand=True)

#create button to check for updates
updateButton = ttk.Button(
    buttonFrame, text="Check for Updates", command=checkForUpdate)
updateButton.pack(in_=buttonFrame, side='top', fill='both', expand=True)

#create button to close to gui
closeButton = ttk.Button(buttonFrame, text="Exit", command=root.destroy)
closeButton.pack(in_=buttonFrame, side='top', fill='both', expand=True)

buttonFrame.pack(side='left', fill='both')


# Field for all functions to put their text output
field = tk.Text(root)
field.configure(height=closeButton.winfo_height() + restartButton.winfo_height() + copyButton.winfo_height() +
                saveButton.winfo_height() + openImageButton.winfo_height() + updateButton.winfo_height())
field.pack(fill='both', expand=True, side='top')

# Configure field to read-only
field.configure(state="disabled", selectbackground="Yellow",
                selectforeground="Black")

# place GUI in center of screen
root.eval('tk::PlaceWindow . center')

#Set min size to the size of the buttons
root.minsize(buttonFrame.winfo_width() + 10,
             (restartButton.winfo_height() * 6))

# Launch GUI
root.mainloop()

# Cleanup files once GUI exits
tempFileCleanup()

# Destructing self to ensure we don't leave a process running after script ends
try:
    os.system('wmic process where name="QRDecoder.exe" delete', shell=True, stdout=NULL)
except:
    pass
