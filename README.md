# CP8326---Final-Project
Optimizing Multi-Agent Food Delivery Using Heuristic Search 


**1. The Problem**

In the dynamic landscape of food delivery services, efficiently managing multiple delivery agents to fulfill orders from various restaurants is a significant challenge. This project aims to optimize delivery routes in a multi-agent context using heuristic search methods. The primary goal is to minimize overall delivery time through coordinated routing of multiple delivery personnel. We will focus on calculating optimal paths for each agent, considering the distance between delivery locations as the heuristic value. This approach aims to enhance the collective efficiency of the entire delivery fleet, addressing the complexities of real-world multi-agent delivery scenarios.


**2. Platform**

We are going to build a custom simulation platform using python to simulate the data. Also, we are searching for data that meets our case on several machine learning websites. Furthermore, we are also looking into understanding the parameters of the data so we can consider to mock it and generate large samples. We would like to try PathBench to see if this tool could help our work. 


**3. Objectives**

 - Analysis of the Multi-Agent Pathfinding (MAPF) Problem: Exploring the intricacies of MAPF as detailed in Sharon et al.​​[1].
 - Understanding Conflict-Based Search (CBS): Delving into CBS’s two-level structure – high-level Conflict Tree (CT) exploration and low-level individual agent searches that adhere to CT constraints​[1]
 - Implementation of CBS in Our Problem: Applying CBS to our specific multi-agent delivery problem, adapting the algorithm to fit the unique requirements and constraints of our scenario.
 - Comparative Analysis with A* Algorithm: Evaluating the performance of CBS in contrast to the A* algorithm, assessing efficiency, scalability, and practicality in real-world applications.

The project will employ an iterative approach, beginning with a study of existing literature and algorithms pertinent to heuristic searches in multi-agent systems. This will include analyzing peer-reviewed articles and prominent research papers in the field. The next phase will involve adapting the CBS algorithm to the food delivery use case, followed by a series of simulations on real-world and generated data to assess and refine its performance. This method is expected to examine fewer states than A* while maintaining optimality​​. CBS is suitable in bottleneck scenarios, where it outperforms traditional methods. This will be a focal point of our analysis​ when comparing with the A* and WA*. We will look at metrics such as time efficiency, route optimization, and resource utilization If time permits we would experiment with optimizing delivery times i.e. choosing an optimal path where we can visit nodes before a certain time respective to individual nodes. 

The estimated schedule to complete the implementation of multi-agent pathfinding is the first week (March 22nd). The following week will consist of additional work on comparing different algorithms and compiling the result. Given these objects are achieved by planned dates we will focus on the time based multi-agent optimization and expect it to be concluded by 5th April. The final 2 days will be dedicated to gathering everything in one place and preparing for presentation.

 
**4. References**

[1] G. Sharon, R. Stern, A. Felner, and N. R. Sturtevant, “Conflict-based search for optimal multi-agent pathfinding,” Artificial intelligence, vol. 219, pp. 40–66, 2015.

[2] A. Andreychuk, K. Yakovlev, P. Surynek, D. Atzmon, and R. Stern, “Multi-agent pathfinding with continuous time,” Artificial intelligence, vol. 305, p. 103662, 2022.
