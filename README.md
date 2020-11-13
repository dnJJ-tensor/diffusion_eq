# diffusion eq
This program was created to simulate two dimensional heat diffusion phenomena which is governed by equation below. 

<image src="https://latex.codecogs.com/gif.latex?\frac{\partial&space;T}{\partial&space;t}&space;=&space;\kappa\left(\frac{\partial^{2}T}{\partial&space;x^2}&plus;\frac{\partial^{2}T}{\partial&space;y^2}\right)">

## Overview
### Outline
This program was created to simulate two dimensional heat diffusion phenomena by compiling python(pandas DataFrame, numpy, matplotlib) and Fortran90/95 with f2py. Input, output and visualization of data is executed by Python program (main.py). Fortran subroutine  undertakes simulation itself.  
### Methodology of simulation 
#### discretization and variables
comming soon.
#### whole process
Euler Explict method is adopted for this Numerical simulation. First of all, main.py reads csv-file which approximate initial conditon as pandas DataFrame. Second, this DataFrame is converted to Numpy 2dimentional array and main.py passes it to Fortran subroutine (hereinafter, this is called "heat_Euler"). Before passing array to subroutine, main.py will check whether sets of parameter valuables meet convergence condition or not. After that, main.py repeat calling heat_Euler for specific times which is designated by itrnum and heat_Euler conducts calculation. Finally, Python functions, Conter and SurFace visualize result of simulation. Please always check numerical solution which is computed by heat_Euler because heat_Euler won't check convergence of numerical solution.

## Requirement
gfortran 10.1.10

python 3.8.5
