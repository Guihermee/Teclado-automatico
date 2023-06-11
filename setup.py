import sys
import os
from cx_Freeze import setup, Executable

python_dir = sys.base_prefix if hasattr(sys, 'base_prefix') else sys.prefix

build_exe_options = {
    "packages": ["os"],
    "includes": ["tkinter", "keyboard", "time"],
    "include_files": [
        (os.path.join(python_dir, "python3.dll"), "python3.dll"),
    ],
}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="Teclado_Automatico",
    version="0.5",
    description="Clicador automático de teclas",
    options={"build_exe": build_exe_options},
    executables=[Executable("clicar.py", base=base)]
)
