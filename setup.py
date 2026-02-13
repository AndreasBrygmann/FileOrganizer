from setuptools import setup, find_packages

setup(
    name='fileOrganizer',  # The package name
    version="0.3",
    #packages=find_packages('fileOrganizer'),  # Automatically find all packages in your project
    #packages=['src/fileHandling.py', 'src/logg.py', 'src/main.py', 'src/navigation.py', 'src/sorting.py'],
    #package_dir = {"": "src"},
    include_package_data=True,  # Include non-Python files specified in MANIFEST.in (if any)
    description='Sort files based on file type',
    author='Jon Andreas Brygmann',
    author_email='jobry7545@oslomet.no',
    url='https://github.com/AndreasBrygmann/FileOrganizer',
    #install_requires=['setuptools'],
    entry_points={
        'console_scripts': [
            'fileOrganizer = src.main:main'
        ],
    },

)