## ML_mini_project
# Vision-based inspection system for PMR Yoke

# Considerations:
▪ Development of algorithm to detect the defects on both the larger and smaller surface of the Yoke
▪ Algorithm shall be suitable to detect the defects on the surface as well as the edges of the surface
▪ Algorithm shall be suitable to identify each specific defects. If no defect is identified then the part
can be classified as a OK part.
▪ Testing and implementation of algorithm on live production and ensuring near to 100% accuracy
of inspection as compared to the existing manual inspection methodology
▪ The algorithm shall be capable of inspecting parts at the rate of ~10 parts per minute.
▪ The samples will be stationary while the images is being captured.

# Interface and Communication:
▪ The algorithm shall be later developed into an application software which is easy to handle for a
production scenario.
▪ The software shall have relevant interface to interact and maintain.
▪ The software developed shall communicate with the vision system to capture the image and be
able to read the image.
▪ The software shall have a feature to communicate and enable connection with an industrial PLC.


▪ The algorithm shall be triggered by an external input (24VDC) and shall provide multiple output
based on the identified error.
▪ The error name definition shall be dynamic and configurable.
* Needs discussion before consideration

# Requirements from L&T: General Scope
# Compliance
▪ The algorithm shall be developed in an authorized software or platform which can later be
transferred to L&T and shall comply with all statuary requirements.
▪ The hardware for capturing the images and processing the above developed algorithm shall be in
scope of L&T.
▪ The hardware specifications suitable for the computational requirements of the developed
algorithm shall be used by L&T. The required hardware specifications shall be conveyed after the
successful trials of the algorithm.
▪ L&T shall provide the raw images required as the input for the development and implementation
of the vision inspection algorithm.
▪ Other points as mentioned further in the document shall be part of the deliverable.


![image](https://user-images.githubusercontent.com/46946896/103620993-81e74380-4f5a-11eb-8335-1bb8086e5971.png)

# part description:
PMR Yoke
Material: FeNi Alloy
Surface finish: Grounded
Appearance: Steel Finish

# Camera used for capturing images:
Camera: Lens: Tamron make M23FM50 
Light: VL -EXC 5050 R Red colour

# Overview of the Project
Design a vision-based solution towards automated inspection of PMR yoke. 
The objective of the project is: 
▪ To develop a vision-based solution towards inspection of Yoke, and towards this, 
o Develop an algorithm to classify the yoke into accepted (satisfying the benchmark) and rejected samples based on captured visual information. 
o Develop an algorithm to identify the type of defect in the rejected yoke sample (i.e, samples with scratches, dents, burr, white/black spots, grinding lines, and uneven ground surfaces) and label the rejected yokes as workable and non-workable rejected samples based on type of defect. 
▪ To develop a interface for communication with the physical system, and towards this,
o Develop an application software which is easy to handle for a production scenario. o Develop an interface that can communicate and enable connection with an industrial PLC. 

# Considered Defects in PMR Yoke 

List of possible defects:  
1. Dent  
2. Scratch  
3. Grinding lines 
4. White spot/Black spot  
5. Surface not ground evenly 
6. Burr 
7. Defect on the edges




Accepted/OK

Dent

Scratch

Grinding Lines

Black Spot

Surface Not Ground Evenly

Burr

Defect on the Edge

