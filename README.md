# Interactive-model-operon
# Author 
- Maria Rybak
# Description of the project 
The project presents an operon - a construct in biology responsible for occurance of specific features in microorganisms like bacteria. The operon consists of several genes (4 in this project) which are expressed when the activator binds to the promoter after being activated by the inducer. Genes expression is shown by the color of the LEDs. When they are red - expression is not taking place, and when they turn green - the expression is activated. The model may be used as a tool to better understand the mechanism of gene expression in the operon.
# Science and tech used 
Whole construction is hidden in the box printed by Prusa printer (files in the branch "3d-printing"). The elements were designed in Tinkercad and then sliced by the modelling slicing software Slicer 4.0. Mechanism is very simple. The inducer is the element compatible with activator. When they connect, they may bind to the promoter. Then red lights which present lack of gene expression are turning off and green lights (genes are expressed) are turning on. 
Elements of the model:
- Raspberry Pi Zero (https://www.raspberrypi.com/products/raspberry-pi-zero/)
- Contact reed switch 20 mm
- 8 resistors 330 Ohm
- 4 red and 4 green LEDs
- magnet
- elements printed by 3D Prusa printer (box, 4 genes, promoter, activator and inducer)
- Breadboard justPi
- connecting cables
# State of the art 
Circuit was created basing on the scheme found in "Raspberry Pi Beginner's Guide" and the software is the modified version of the one found on the website https://kostrzewinki.pl/podlaczenia-kontaktronu-raspberry-pi-systemie-domoticz/. 
# What next?
This model may be used during for example biochemistry courses to demonstrate the positive control of the operon. With this technology we may create more interactive models which can be very helpful in learning. Moreover, it's not hard to change the model to also present the negative control of the operon.
As it was mentioned the project is quite simple. However, we may easily develop it to be more complex and to present more complicated mechanisms. 
# Sources 
- [Writing on GitHub] ( https://docs.github.com/en/get-started/writing-on-github )
- Raspberry Pi Beginner's Guide
- Web app for 3D designs TINKERCAD (https://www.tinkercad.com)
- modelling slicing software Slicer 4.0. (https://3dgence.com/pl/oprogramowanie-dla-druku-3d/slicer-4-0/)
- https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2776167/
- https://ryansouthgate.com/raspberry-pi-door-sensor/
