# diffusion eq
This program was created to simulate two deminsional heat diffusion phenomena.

## Overview
### outline of this program
This program was created to simulate two deminsional heat diffusion phenomena by compiling python(pandas DataFrame, numpy matplotlib) and Fortran90/95. Input, Output and visualization of data is executed by Python. Fortran subroutine undertakes simulation itself.  
### detail of simulation
Euler Explict method is adopted for this Numerical simulation. First of all, main.py reads csv-file which approximate initial conditon as pandas DataFrame. Then this DataFrame is converted to Numpy 2dimentional array and pass it to Fortran subroutine. Before passing array to subroutine, main.py will check sets of parametes meet convergence condition. This 

## Requirement
macOS Catalina 10.15.6
gfortran 10.1.10
python 3.8.5
