# Dynamic_Systems_Fingerprint_Model
"Final Project",UNAM (https://www.unam.mx/) -TICs-Dynamic Systems 2022-1 class,taught by Dr. Victor de la Luz 


____
## Table of Contents
* [Team_Members](#Team_Members)
* [License](#License)
* [Project Overview](#Project_Overview)
* [Introduction](#Introduction)
* [Justification](#Justification)
* [Goals](#Goals)
* [Hypothesis](#Hypothesis)
* [Metodology](#Metodology)
* [Libreries](#Libreries)
* [Packages](#Packages)
* [Results](#Results)
* [Conclusions](#Conclusions)
* [Executing_Software_Intructions](#Executing_Software_Intructions)
* [References](#References)

____
# Team_Members

* Luis Aarón Nieto Cruz. ([LuisAaronNietoCruz](https://github.com/LuisAaronNietoCruz))
* Jadiel Zúñiga Rodriguez. ([JZRodriguez](https://github.com/JZRodriguez))
* Miguel Ángel Zamorano Presa. ([miguelzpresa](https://github.com/miguelzpresa))

____
# License
Copyright © 2022 <mikezpresa@gmail.com, zujadiel@gmail.com, aaronnicruz@gmail.com>

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

____
# Project_Overview
This project aims to develop a model for fingerprint formation. 

![Alt text](https://github.com/JZRodriguez/fingerprints_project/blob/main/Fingerprints%20patterns%202.jpg 'Fingerprints')

Freepik Company. (2010-2022). Detailed fingerprint icons. Retrieved from [Link page](https://www.freepik.es/vector-premium/iconos-detallados-huellas-dactilares-escaner-policia-pulgar-simbolos-vectoriales-identidad-persona-seguridad-id-pictogramos-dedo-identidad-tecnologia-biometric_4866225.htm)


# Introduction
Fingerprints Growth formation pattern is dictated by highly complex interactions of multiple initial conditions, listed  below. The main goal is to generate fongerprints based of the paper " fingerprint formation model published in the scientific journal EUROPHYSICS LETTERS, "DOI: 10.1209/epl/i2004-10161-2""
 
## What are fingerprints?
Fingerprints are skin patterns with friction ridges. Our fingers, palms and soles are characterized by ridges (hills) and valleys (furrows). Their formation occurs during fetal development, beginning at approximately the 10th week of gestation, being completed by the 17th week, and remaining throughout life.

## What are the patterns of fingerprints? 
There are three basic patterns of fingerprints: 
* Whorls (a): Most complex, and contain central pocket, double loop, and accidental 
* Loops (b): Radial or  ulnar, depending on whether direction of slope of pattern is towards inner arm bone (radius) or outer arm bone (ulna) 
* Arches (c): Can be plain or tented

![Alt text](https://github.com/JZRodriguez/fingerprints_project/blob/main/Fingerprints%20pattern.jpg 'Types of patterns')

M. Kücken, A.C. Newell / Journal of Theoretical Biology 235 (2005) 71–83. Retrieved from page 80 Fig.11. [Link to the article](https://www.math.arizona.edu/~anewell/publications/Fingerprint_Formation.pdf)
______
# Justification

The biggest inspiration for this project comes from the work of Alan Turing's Patterns in Nature. Zebra stripes, cat coats, leopards and cheetahs are surprisingly unique, making stripes a tool to identify one animal from the rest, fingerprints are like our stripes.   


Turing’s theory was elegant and simple: any repeating natural pattern could be created by the interaction of two things — molecules, cells, whatever — with particular characteristics. Through a mathematical principle he called ‘reaction–diffusion’, these two components would spontaneously self-organise into spots, stripes, rings, swirls or dappled blobs.
"https://ideas.ted.com/how-the-zebra-got-its-stripes-with-alan-turing/"

# Constraints
Physics and mathematical theory of embryology deals with highly complex dynamics systems ,some of them non-linear,its important to mention that we do not pretend to model the actual physical process of ridges formation(fingerprints),However ,the paper that we are analyzing gives an alternative approach,it takes the principal properties ,that we will list below ,to replicate the fingerprint formation during embryological process through ,multivariable calculus tools ,vectors spaces,and numerical methods.

#  Goals
* Get a better understanding of embryological process of epidermial ridge formation
* Understand the problem domain 
* Implement the 3 Principal Patterns :Whorls,Loops.Archs
* Analize the different dynamics output from different initial conditions
* Simulate the closest thing to a fingerprint 


____
# Hipothesis
* Anisotropic laws are true (locally)(inplace stress distribution)
* Stability in the solutions of the ecuations
Given that no person has the same attributes than another person, the expected result is that no two fingerprints analyzed will be the same.
* The stress field anticipates the direction of the ridge system and also predicts in what  areas buckling will take place first
* Wavevectors Ecuations will perform as planned to calculate the buckling patterns



![Alt text](https://github.com/JZRodriguez/fingerprints_project/blob/main/Fingerprints%20examples.jpg 'Fingerprint models')

M. Kücken, A.C. Newell / Journal of Theoretical Biology 235 (2005) 71–83. Retrieved from page 79 Fig.10. [Link to the article](https://www.math.arizona.edu/~anewell/publications/Fingerprint_Formation.pdf)

______
# Methodology

The surface will be defined as a map of a rectangular region Omega where (u,v) will belong to Omega and the surface S will be defined as the image of the map r: Omega --> S

The map is defined by:

![Alt text](https://github.com/JZRodriguez/fingerprints_project/blob/main/F2.jpg 'F2')


M. Kücken, A.C. Newell / Journal of Theoretical Biology 235 (2005) 71–83. Retrieved from page 82. [Link to the article](https://www.math.arizona.edu/~anewell/publications/Fingerprint_Formation.pdf)


r0 is a parameter to be chosen close to the average radius of curvature of the pad. In addition we have a function r(u, v) denoting the surface distance. This construction guarantees a smooth surface (at least once differentiable) for all smooth r(u, v). The geometry of the pad can now be specified by choosing a certain function r(u, v). It is given by
the following expression: 
<img src="https://github.com/JZRodriguez/fingerprints_project/blob/main/F3.jpg" width="50%"/>  

 
                                                                                                                                             
![Alt text](https://github.com/JZRodriguez/fingerprints_project/blob/main/F3.jpg  'F3')

M. Kücken, A.C. Newell / Journal of Theoretical Biology 235 (2005) 71–83. Retrieved from page 82. [Link to the article](https://www.math.arizona.edu/~anewell/publications/Fingerprint_Formation.pdf)
# For the 3 Pattern Models
Surface Domain Solution is equally defined for  The 3 Prototypes.
as 
phi,theta = [ 0 ,2*pi]
and radious =1 thats why 3d axis ticks are aligned in ranges from -[1 ,1]
Once the Generation of points in the program is completed ,the next step is to create the grid for the future 3dimentional plot  
* 2nd.Step.Yield the surface of a sphere taking as input the previous points created each to the ecuations ,the output are the points of our grid

* 3rd .In order to recreate a reallistic vector field that simulates the flow dynamics of the Elastic Shield Plate that is our Sphere Surface ,the values that  we use were the same of our Thesis that we are following,  this values were the input of the direction of the fields.
![image](https://user-images.githubusercontent.com/49998408/174407919-cf1e8961-b9e4-4115-b445-e95b069a9103.png)
M. Kücken, A.C. Newell / Journal of Theoretical Biology 235 (2005) 71–83. Retrieved from page 79 Fig.10. [Link to the article](https://www.math.arizona.edu/~anewell/publications/Fingerprint_Formation.pdf)






___
# Libreries

* [Python 3](https://www.python.org/)
* Linux Ubuntu    64-bit
* Linux Arch      64-bit
* [Github](https://www.github.com)
* Windows 10      64-bit
* Jupyter lab     3.2.9
* [Blender](https://www.blender.org/)
* 

___
# Packages<br>
* [Pandas    version 1.4.1](https://pandas.pydata.org/)
* [Matplotlib version 3.2.2](https://matplotlib.org/)
* [Numpy      version 1.21.5](https://numpy.org/)  
* Linux console
* https://github.com/nortikin/sverchok/
* https://github.com/inca/blender-differential-growth/blob/main/op_grow.py

___
# Results
For Purposes of Simulation the Metrics Ssystem presented on Simulations was decimal base:  
Surface Domain Solution is equally defined for  The 3 Prototypes.
as 
phi,theta = [ 0 ,2*pi]  
and radious =1  
thats why 3d axis ticks are aligned in ranges from -[1 ,1]


![image](https://user-images.githubusercontent.com/49998408/174307759-a60ce64b-147d-40d2-b2b0-32afe17d3b85.png)

<img src="https://github.com/JZRodriguez/fingerprints_project/blob/main/Prueba3.jpg" width="50%"/> 


<img src="https://github.com/JZRodriguez/fingerprints_project/blob/main/Crecimiento-diferencial.jpg" width="50%"/> 


____
# Conclusions
The way we achieve to find the 3 different Fingerprints  Patterns was by playing with our initial wavevector values,not really by changing the original value but from changing the signs or moving the value of x to y position and viceversa,because changes minimal changes were not to visible and the bigger ones break with our intentions of finding the shape of a buckling flow pattern .The relevance in this proyect abut Blender Animation was that it allow us to compute in a fast and realistic way the fingerprints growth ,and generates buckling all around the surface of the finger,not only that but to skip natural process such as time ,because what the simulation achieves in seconds in nature is the process of weeks of formation, and in a micro scale.  
Matplotlib Simulations does not provide shell physical properties that in the thesis are specified,what blender allow us from in build tools was to tunne properties such as ,Anisotroic Elasticity,Young Modulus,Blending Modulus,Airy Stress Function ,and stiffness Matrix of the surface,Potential Engergy of Surface,tensil and Tensor forces around whole surface of our shells,forfurther works,it is planned to implement those parameters in the laws of Matplotlib simulations.  
Another interesting conclusión was founded in the process of research phase of an interesting Article called "Can a Fingerprint be Modelled by a Differential Equation??" by From: Fouad Zinoun 
https://doi.org/10.48550/arXiv.1802.05671 where mathematically Foad arrives to the conclusion that is not possible to model a fingerprint by differential ecuations because ideally the model should be starting from a finite set of initial conditions and more important,he also explains that trying to assign an explicit written differential ecuation to an observed system of curves is most often illusory.



_____
# Executing_Software_Intructions

To run the software, open a terminal:  
To see 3 Models:  
initialize jupyter notebook Navegate where the file is located (Downloads ) and clic to the file name called Fingerprints_Models.ipynb
For Python Script:
type ./more_practice.py
For Blender Animation
Download finger_print.blend,download Sverchock zip "https://github.com/nortikin/sverchok/"open your blender program,open the file inside blender,open menu of upper left section,select preferences,then clic on  Add ons  
,clic on install package,select sverchock zip ,install it ,clic on the sverchock activate botton,save configuration,open menu of upper left section,select sverchok ,once it opens a new dark window,go to right side of the window select toggle to open ,select shervock,open available progrmas clic in node tree,the  the Info_wrapper node will be in the right side at the botton(color green)you will see a botton of the simbol of play to start the  animation.  
One final step.  
Go to  https://github.com/inca/blender-differential-growth/blob/main/op_grow.py copy the code ,open a python terminal in blender and paste it,clic run 
With the Code running you can know start the infowrapper button and enjoy the animation.

___
# References
Europhys. Lett., 68 (1), pp. 141–146 (2004)
DOI: 10.1209/epl/i2004-10161-2

Dubey, Deepika. Fingerprints; 30 May 2018.

Michael Kucken and Alan C. Newell. Fingerprint formation. Journal of Theoretical Biology, 235(13):71–83, 2005

https://github.com/asahidari/differentialgrowthsnliteb3d4  

https://github.com/nortikin/sverchok/  
https://github.com/inca/blender-differential-growth/blob/main/op_grow.pyv
