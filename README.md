# Array-clicker
Small app for visualization and manual marking of various data stored in numpy arrays.
![alt text](https://github.com/vachaj11/array-clicker/blob/master/doc/prev.png?raw=true)
## Installation
This app is written in Python so you have to have a [Python interpreter](https://www.python.org/downloads/) installed on your machine in order to run it.

The files you need to download are  [main.py](https://github.com/vachaj11/array-clicker/blob/master/main.py), [form.py](https://github.com/vachaj11/array-clicker/blob/master/form.py),  [bind.py](https://github.com/vachaj11/array-clicker/blob/master/bind.py) and [colormaps.py](https://github.com/vachaj11/array-clicker/blob/master/colormaps.py)
the dependencies apart from the standard python libraries are PySide6 and NumPy. Install them using:
```
pip install PySide6 Numpy
```
## Running
Run the program with (in location where you stored all of the 4 files):
```
python3 main.py
```
## Usage
Function of any button/widget is described in its tooltip.
### Input
The inputed data are expected to be 2D NumPy arrays (stored in ```.npy``` files) containing scalar quantities (specifically real numbers, that is without infinity). I haven't tried displaying anything larger than 2000x2000 array with this, so I can't guarentee that it will work.
### Output
Marking information are saved as a NumPy array of the input array indicies in the chosen output directory with the same name as was the name of the input file only with \_out appended at the end.
## License
This program is available as open source under the terms of the GPL-3.0 License.

Most of this program is based on Python Qt libraries developed by the Qt Company and published under GPL and LGPL licences.
