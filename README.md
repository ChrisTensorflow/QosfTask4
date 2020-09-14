# QosfTask4

These are my attempts at task 4 of the quantum mentorship screening tasks. 

In the first version, I searched through different Rx rotation angles and found that pi gave the lowest expected value, which was -1. Therefore, I conclude that the lowest eignvalue of the matrix given in the question is -1.

In the second version, I use the circuit in figure 7 and the theory in section 7.2 of Ref [1] to improve my VQE implementation. Instead of having to run three different quantum circuits in order to get the final answer (as I did in version 1), I can arrive at the same result using only one circuit by processing the quantum measurement results more efficiently.

In the third version, I adapt the algorithm so that the output is the derivative of the lowest eigenvalue with respect to rotation angle. When the derivative is close to zero, this shows that one is close to finding the optimal angle for the VQE algorithm. I used Ref [4] for the main concept but this involved doing a controlled-X-rotation. To implement this, I used Ref [3].

[1] Minimizing State Preparations in Variational Quantum Eigensolverby Partitioning into Commuting Families
    Pranav Gokhale, Olivia Angiuli, Yongshan Ding, Kaiwen Gui, Teague Tomesh, Martin Suchara, Margaret Martonosi, and Frederic T. Chong
    arXiv:1907.13623v1
    
[3] https://www.asc.ohio-state.edu/perry.6/p5501_sp17/articles/quantum_gates.pdf

[4] Methodology for replacing indirect measurements with direct measurements
    Kosuke  Mitarai and  Keisuke  Fujii
    arXiv:1901.00015v2
