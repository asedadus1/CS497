README.md
This repository contains the implementation of the PageRank Algorithm for an in-class project. The project was assigned to teams consisting of 1-2 students, and detailed instructions were provided during class sessions. The project instructions can also be found in the slides provided for Google's PageRank algorithm.

1. Find out sinks and add outgoing links.
2. Set damping factor (e.g., 𝑑 = 0.85 and 𝜀 = 0.01).
3. Initialize all ranks to be 1/𝑁. Stop converging at whichever comes first: 100 iterations or margin of error < 𝜀.
4. Calculate PageRank of each page repetitively based on the following structure: B -> D -> A -> C.
