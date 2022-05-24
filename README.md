<h1 align="center">
  <br>
  QRDecoder
  <br>
</h1>

<h4 align="center">A lightweight, on-screen QR decoding tool for Windows. Built on top of Python leveraging the Windows Snipping Tool.</h4>

<p align="center">
  <a href="#overview">Overview</a> •
  <a href="#usage">Usage</a> •
  <a href="#credits">Credits</a> •
  <a href="#license">License</a>
</p>

![screenshot](GIF URL)

## Overview

QRDecoder is a lightweight, on-screen QR code decoding tool for Windows. It's built on top of Python and leverages the the Windows Snipping Tool/Snip & Sketch app for on-screen image selection. Simply install, launch, and crop to decode QR code images that are anywhere on your screen. 

This project is a work in process. Pull-requests, suggestions, fixes, and feature requests are welcome.


## Usage

You can [download](downloadURL) the latest installable version of QRDecoder for Windows. I've also included the following resources if you want to modify, compile, and package the application yourself:

* QRDecoder.py (standalone script)
* setup.py (for use with Cx_Freeze)

If using the managed installer, all dependencies are included. If running manually, you'll need to install/import the following Python modules:

 ```python
from PIL import Image
from subprocess import Popen
from PIL import ImageGrab
from pyzbar.pyzbar import decode
import os
import time
import tkinter as tk
import sv_ttk
import psutil
 ```

## Emailware

QRDecoder is an [emailware](https://en.wiktionary.org/wiki/emailware). Meaning, if you liked using this app or it has helped you in any way, I'd like you send me an email at <mark.hopper24@gmail.com> about anything you'd want to say about this software. I'd really appreciate it!

## Credits

This software would not have been possible without the use of the following tools, resources, and open source packages:

- [Python](https://www.python.org/)
- [Windows Snipping Tool](https://www.microsoft.com/store/productId/9MZ95KL8MR0L)
- [Pillow](https://github.com/python-pillow/Pillow/) (Image manipulation)
- [pyzbar](https://github.com/NaturalHistoryMuseum/pyzbar)) (QR Decoding)
- [sv_ttk theme](https://github.com/rdbende/Sun-Valley-ttk-theme) (Theme)
- [@amitmerchant1990](https://github.com/amitmerchant1990/electron-markdownify#readme) (readme insperation)
- [cx_Freeze](https://github.com/marcelotduarte/cx_Freeze) (compling)
- [Inno Setup](https://jrsoftware.org/isinfo.php) (packaging)

## License

MIT

---

> GitHub [@MarkHopper24](https://github.com/MarkHopper24) &nbsp;&middot;&nbsp;
> Twitter [@Mark_Hopper24](https://twitter.com/Mark_Hopper24)

