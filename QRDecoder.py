from PIL import Image
from subprocess import Popen
from PIL import ImageGrab
from pyzbar.pyzbar import decode
import os
import time
import tkinter as tk
import sv_ttk
import psutil

#Capturing script run timestamp
programStart = time.time()

#Function to close out other existing instances of the same process
def closeIfProcessRunning(processName):
    #Loop through all running processes
    for proc in psutil.process_iter():
        try:
            #If the process exists, was created before programStart, and has a different PID
            if (processName.lower() in proc.name().lower()) and (proc.create_time() < programStart) and (proc.pid != os.getpid()):
                #Terminate it
                proc.terminate()
            #If an exception is thrown, should be safe to assume there are no other instances and move on.
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess, psutil.TimeoutExpired, psutil.Error):
            pass

#Close other instances of QRDecoder.exe
closeIfProcessRunning('QRDecoder.exe')

#File for temp image captured by user with snipping tool
capturedQR = 'temp.png'
#Fake generated temp image if no image is detected in the user's clipboard when script starts running
fakeQR = 'placeholder.png'

#Making sure temp files were cleared out from last run
if(os.path.exists(capturedQR) == True):
    os.remove(capturedQR)
if(os.path.exists(fakeQR) == True):
    os.remove(fakeQR)

#Check user's clipboard for to see if there's already an existing image there, decode it, and set it to starting clipboard contents
try:
    startingClipboard = ImageGrab.grabclipboard()
    startingContents = list(startingClipboard.getdata())
#If no image detected, set decoded clipboard contents to the fake generated temp image
except:
    fakeImage = Image.new("RGB", size=(10, 10), color='black')
    fakeImage.save(fakeQR)
    startingClipboard = Image.open(fakeQR)
    startingContents = list(startingClipboard.getdata())

#Launch snipping tool
Popen("start ms-screenclip:", shell=True)

#Waiting for file creation which indicates clipboard change 
#In short, when the file exists, we know the user's clipboard is different than when we started and can exit the loop.
while os.path.exists(capturedQR) == False:
    #Checking for new clipboard contents
    try:
        newClipboards = ImageGrab.grabclipboard()
        newContents = list(newClipboards.getdata())
    #Passing exception if user still doesn't have a clipboard image
    except:
        pass
    #Checking if new clipboard contents have been detected
    if('newContents' in locals()):
        #Same contents as when we started, sleep and loop again
        if(newContents == startingContents):
            time.sleep(.1)
        #Success! New clipboard image detected. Save to a file that will exit the loop
        else:
            newClipboards.save(capturedQR)

#Decode new QR
decodedQR = decode(Image.open(capturedQR))

#Extract string from decoded QR
try:
    QRContents = decodedQR[0][0]
    QRContents = QRContents.decode()
except:
    QRContents = "QR code not read. Please try again."

#Create GUI + apply theme
root = tk.Tk()
sv_ttk.set_theme("dark")
sv_ttk.use_dark_theme()
root.title("QR Decoder")
root.geometry("500x500")
root.attributes('-topmost', True)

#Insert decoded text into text GUI text field
field = tk.Text(root)
field.insert(tk.INSERT, QRContents)
field.pack(fill='both', expand=True)

#Configure field to read-only
field.configure(state="disabled", selectbackground="Yellow",
                selectforeground="Black")

#Formatting GUI based on screen size
root.update()
root.minsize(root.winfo_width(), root.winfo_height())
x_cordinate = int((root.winfo_screenwidth() / 2) - (root.winfo_width() / 2))
y_cordinate = int((root.winfo_screenheight() / 2) - (root.winfo_height() / 2))
root.geometry("+{}+{}".format(x_cordinate, y_cordinate - 20))

#Launch GUI
root.mainloop()

#Cleanup files once GUI exits
if(os.path.exists(capturedQR) == True):
    os.remove(capturedQR)
if(os.path.exists(fakeQR) == True):
    os.remove(fakeQR)
