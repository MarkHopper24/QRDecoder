<h3 align="center">12/29/2023 QRDecoder Retirement: </h3>

Hi all, I have decided to retire QRDecoder. For the last year, all of my barcode/QR code app development has been focused on barcodrod.io. barcodrod.io is an ad-free, open source Windows 10/11 app that offers the same functionality as QRDecoder, but with many more features and improvements. While Python was great for the limited feature scope of QRDecoder, barcodrod.io being written in C# and built on .NET comes with numerous development benefits for a native Windows application, allowing much more rapid feature development. Learn more here:

Website: https://barcodrod.io <br>
GitHub: https://github.com/MarkHopper24/barcodrod.io <br>
Download it from GitHub or the Microsoft Store: https://download.bardcodrod.io <br>

With that said, I will no longer update or support QRDecoder, including breaking and/or critical security fixes. The app and source code will remain available on GitHub for historical purposes and can be forked, referenced, and repurposed as needed under the MIT license but I recommend migrating to barcodrod.io for general usage as soon as possible. 

Thank you for your support! QRDecoder has been a really fun learning project, and I hope you have enjoyed using it or learning along with me. 🙂

<br><br>
<h1 align="center">
  <a href="https://apps.microsoft.com/store/detail/qrdecoder/9N6262B4T5CN?hl=en-us&gl=us"><img src="https://raw.githubusercontent.com/MarkHopper24/QRDecoder/main/Logo.png" alt="QRDecoder" width="150"></a><br>
  <br>
  QRDecoder

</h1>


<h4 align="center">A lightweight, on-screen QR code decoding tool for Windows. Built on top of Python leveraging the Windows Snipping Tool.</h4>

<p align="center">
  <a href="#overview">Overview</a> •
  <a href="#usage">Usage</a> •
  <a href="#credits">Credits</a> •
  <a href="#license">License</a>
</p>

<p align="center">
<img src = https://raw.githubusercontent.com/MarkHopper24/QRDecoder/main/Screenshot.png>
<br>
<br>
<img src = https://github.com/MarkHopper24/QRDecoder/blob/main/qrdecoder1.2.gif>
</p>


## Overview

QRDecoder is a lightweight, on-screen QR code decoding tool for Windows. It's built on top of Python and leverages the the Windows Snipping Tool/Snip & Sketch app for on-screen image selection. Simply install, launch, and crop to decode QR code images that are anywhere on your screen. 

This project is a work in progress. Pull-requests, suggestions, fixes, and feature requests are welcome.


## Usage

You can download and install the QRDecoder directly from GitHub [HERE](https://github.com/MarkHopper24/QRDecoder/blob/main/QRDecoderSetup.exe). Alternatively, you can install from the Microsoft Store [HERE](https://apps.microsoft.com/store/detail/qrdecoder/9N6262B4T5CN?hl=en-us&gl=us).

I've also included the following resources if you want to modify, compile, and package the application yourself:

* QRDecoder.py (standalone script)
* setup.py (for use with Cx_Freeze)

## Emailware

QRDecoder is an [emailware](https://en.wiktionary.org/wiki/emailware). Meaning, if you liked using this app or it has helped you in any way, I'd like you send me an email at <mark.hopper24@gmail.com> about anything you'd want to say about this software. I'd really appreciate it!

## Credits

This software would not have been possible without the use of the following tools, resources, and open source packages:

- [Python](https://www.python.org/)
- [Windows Snipping Tool](https://www.microsoft.com/store/productId/9MZ95KL8MR0L)
- [Pillow](https://github.com/python-pillow/Pillow/) (Image manipulation)
- [pyzbar](https://github.com/NaturalHistoryMuseum/pyzbar) (QR Decoding)
- [sv_ttk theme](https://github.com/rdbende/Sun-Valley-ttk-theme) (Theme)
- [@amitmerchant1990](https://github.com/amitmerchant1990/electron-markdownify#readme) (readme inspiration)
- [cx_Freeze](https://github.com/marcelotduarte/cx_Freeze) (compiling)
- [Inno Setup](https://jrsoftware.org/isinfo.php) (packaging)

## License

[MIT](https://github.com/MarkHopper24/QRDecoder/blob/main/LICENSE)

---

> GitHub [@MarkHopper24](https://github.com/MarkHopper24) &nbsp;&middot;&nbsp;
> Twitter [@Mark_Hopper24](https://twitter.com/Mark_Hopper24)

