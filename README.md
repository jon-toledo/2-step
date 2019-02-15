# 2-step: A solver for the prime-paths TSP

This project is based on the Kaggle competition https://www.kaggle.com/c/traveling-santa-2018-prime-paths.  It is a modified Traveling Salesman Problem where there is a global constraint on the path.  The statement of the problem is as follows.  You are given a list of cities each with a CityId number and (x,y) coordinates.  The CityId numbers range from 0 to the number of cities.   You want to find the shortest path through all the cities that starts and ends at city 0 subject to the constraint that every 10th step is 10% more lengthy unless coming from a prime CityId.  The number of cities is of the order of 10^{5}.  

My goal was not to re-invent any method of approximating solutions to this type of problem (there are already well established methods based on k-opt).   My goal was to practice optimization over large networks where developing efficient algorithms is completely essential.  For this I develop a simple procedure for improving an approximate solution of the TSP in order to account for the global constraint.  The code is highly optimized and vectorized in order to deal with the size of the network (~ 10^{5} nodes).  
