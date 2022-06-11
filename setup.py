import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
# "packages": ["os"] is used as example only
build_exe_options = {'replace_paths': [("*", "")],
"include_msvcr": True 
}

#base="Win32GUI" should be used only for Windows GUI app
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="QR Decoder",
    version="1.1",
    options={"build_exe": build_exe_options},
    
    executables=[Executable(script='QRDecoder.py', base = base, icon='Logo.ico')]
)