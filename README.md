# diffusion eq
This program was created to simulate two deminsional heat diffusion phenomena.

## Overview
### outline of this program
This program was created to simulate two deminsional heat diffusion phenomena by compiling python(pandas DataFrame, numpy matplotlib) and Fortran90/95. Input, Output and visualization of data is executed by Python. Fortran subroutine undertakes simulation itself.  
### detail of simulation 
Euler Explict method is adopted for this Numerical simulation. First of all, main.py reads csv-file which approximate initial conditon as pandas DataFrame. Second, this DataFrame is converted to Numpy 2dimentional array and pass it to Fortran subroutine(hereinafter, this is called "heat_Euler"). Before passing array to subroutine, main.py will check whether sets of parametes meet convergence condition or not. After that, heat_Euler do calculation designated time which is decided by varuable itrnum. Finally, Python functions, Conter and SurFace visualize result of simulation. Please always check numerical answer which is computed by heat_Euler because heat_Euler won't check convergence of numerical answer.

## Requirement
macOS Catalina 10.15.6
gfortran 10.1.10
python 3.8.5
Environments under Windows 10 pro is tested.

## contact
My twitter account : @dnJJ_tensor
I long to get feedback from anyone because I am a not professional engineer. I'm a university student, so There are a lot of things I must learn.