## Table of Contents

1. [Project Overview](#project-overview)  
   - [Brief](#brief)  
   - [Aim](#aim)  
   - [Scope](#scope)  
2. [Features](#features)  
   - [Crane Optimization](#crane-optimization)  
   - [Machine Learning](#machine-learning)  
3. [Problem Design](#problem-design)  
   - [Scenario](#scenario)  
4. [Logical Representation](#logical-representation)  
5. [Transitional Model](#transitional-model)  
6. [Search Algorithm](#search-algorithm)  
   - [Algorithm](#algorithm)  
7. [Machine Learning Model](#machine-learning-model)  
   - [Features](#features)  



## Project Overview
### Brief 
This project model solves a complex crane optimization problem and trains a machine learning model to predict container priority when placing.
### Aim 
To explore AI solutions for automation combining optimized algorithms and supervised learning
### Scope
Includes problem design, logical modeeling, search algorithms, machine learning and ethical reflections which is the priority

# Features
### Crane Optimization
- Logical relations to represent crane environments
- Transition models for crane actions
- Search algorithm implementation for finding an optimal crane plan

### Machine Learning
- Predicting container priorities using supervised learning
- Training and evaluation with real-world data

# Problem Design
### Scenario
- 6 Containers, 4-8 loading bays
- At least 10 crane actions to solve the problem
**Goal:** Define and Achieve an optimal crane configuration through logical planning

# Logical Representation
Relationed Defined: 
__**SOON**__

**Goals:** Ensure coverage of the environment and actions

# Transitional Model 
- Preconditions and effects for each action
- Documented in a transition table

# Search Algorithm
### Algorithm
Breadth-first search (BFS) A*
- Does it find a solution
- Does it guarantee the best solution?

# Machine Learning Model
- **Dataset:** ```ContainerData.csv```
- **Features:** Height, Width, Movement Frequency, Dock time
- **Goal:** Train a model to predict container priority (high/low).

# Appendix
State 1
![image](https://github.com/user-attachments/assets/a7810b02-8bb2-4d4d-bdec-2abe8d8efec0)

State 2
![image](https://github.com/user-attachments/assets/fbcbb7b1-ed82-43df-9bc6-02783b099a80)

State 3
![image](https://github.com/user-attachments/assets/c935f247-275f-4a2f-8fcd-7d3e68a262bd)

State 4
![image](https://github.com/user-attachments/assets/a7292c24-73c3-4a9d-95e3-490cec3f7e29)

State 5
![image](https://github.com/user-attachments/assets/5b08a21b-7473-4cbc-8eee-850446dc0967)


