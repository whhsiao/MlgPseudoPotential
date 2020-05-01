# BlgPseudoPotential
_This repository presents the Haldane pseudopotential code for bilayer graphene models._

In the studies of the quantum Hall effect, especially the fractional phases, physicists usually start with simple single-particle picture, in which we can solve the single-particle orbitals (wavefunctions) and the spectrum (eigenvalues) exactly. The interaction effect is then introduced to by evaluating the two-body interaction matrix element with the single-particle orbitals. 

Haldane realized the details owing to specific type of interaction may not be of great importance. Instead, we shall focus on the projection of the matrix element into different angular momentum channels. The "partial wave" of the interaction matrix element characterizes the interaction energy of a pair of particles rotating about each other in the angular momentum channel _L_, and is dubbed the Haldane pseudopotential. In the numerical studies of fractional quantum Hall effect the Haldane pseudopotentials are almost as important as the _realistic potentials_ as the starting points of research.

In this repository, we present the codes in both _Mathematica_ and _Python_ that is able to compute the Haldane pseudopotentials for the bilayer graphene models on a sphere. The detailed description of the background context can be found in the paper:

https://journals.aps.org/prb/abstract/10.1103/PhysRevB.101.155310

https://arxiv.org/abs/2001.01740

In the paper I merely computed the values for the bilayer graphene. Nonetheless, the codes can be applied to arbitrary layers with minor modification.
