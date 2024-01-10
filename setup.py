from cx_Freeze import setup, Executable

base = None    

executables = [Executable("constellations\main.py", base=base)]

packages = ["idna","pygame","math","random"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "jimmy saville",
    options = options,
    version = "1.0",
    description = 'something goes here',
    executables = executables
)