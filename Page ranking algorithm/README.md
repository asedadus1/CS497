This is a group in-class project aimed at implementing Google's PageRank algorithm. The project is designed for 1-2 students in a team. Please sign up in the People section's Page Rank Algorithm page before submission. Detailed project instructions are provided during class and can also be found in our slides covering Google's PageRank algorithm.

1. Find out sinks and add outgoing links.
2. Set damping factor (e.g., 𝑑 = 0.85 and 𝜀 = 0.01).
3. Initialize all ranks to be 1/𝑁. Stop converging at whichever comes first: 100 iterations or margin of error < 𝜀.
4. Calculate PageRank of each page repetitively based on the following structure: B -> D -> A -> C.
