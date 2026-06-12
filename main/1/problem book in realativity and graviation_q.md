PROBLEM BOOK IN RELATIVITY AND GRAVITATION

# PROBLEM BOOK IN RELATIVITY AND GRAVITATION

ALAN P. LIGHTMAN

WILLIAM H. PRESS

RICHARD H. PRICE

SAUL A. TEUKOLSKY

PRINCETON UNIVERSITY PRESS

PRINCETON, NEW JERSEY

Copyright © 1975 by Princeton University Press

Published by Princeton University Press, Princeton, New Jersey

In the United Kingdom, by Princeton University Press, Chichester, West Sussex

# ALL RIGHTS RESERVED

Library of Congress Cataloging in Publication Data will be found on the last printed page of this book

This book has been composed in VariTyper Bookman

Princeton University Press books are printed on acid-free paper and meet the guidelines for permanence and durability of the

Committee on Production Guidelines for Book Longevity of the Council on Library Resources

Printed in the United States of America

Second printing, with corrections, 1979

# CONTENTS

PREFACE vii

NOTATION xi

<table><tr><td></td><td>PROBLEMS</td><td>SOLUTIONS</td></tr><tr><td>1. Special-Relativistic Kinematics</td><td>3</td><td>133</td></tr><tr><td>2. Special-Relativistic Dynamics</td><td>11</td><td>159</td></tr><tr><td>3. Special-Relativistic Coordinate Transforma-tions, Invariants and Tensors</td><td>15</td><td>173</td></tr><tr><td>4. Electromagnetism</td><td>23</td><td>192</td></tr><tr><td>5. Matter and Radiation</td><td>28</td><td>205</td></tr><tr><td>6. Metrics</td><td>37</td><td>233</td></tr><tr><td>7. Covariant Differentiation and Geodesic Curves</td><td>40</td><td>243</td></tr><tr><td>8. Differential Geometry: Further Concepts</td><td>47</td><td>263</td></tr><tr><td>9. Curvature</td><td>55</td><td>284</td></tr><tr><td>10. Killing Vectors and Symmetries</td><td>64</td><td>315</td></tr><tr><td>11. Angular Momentum</td><td>67</td><td>327</td></tr><tr><td>12. Gravitation Generally</td><td>71</td><td>346</td></tr><tr><td>13. Gravitational Field Equations and Linearized Theory</td><td>76</td><td>364</td></tr><tr><td>14. Physics in Curved Spacetime</td><td>82</td><td>386</td></tr><tr><td>15. The Schwarzschild Geometry</td><td>87</td><td>404</td></tr><tr><td>16. Spherical Symmetry and Relativistic Stellar Structure</td><td>92</td><td>432</td></tr><tr><td>17. Black Holes</td><td>100</td><td>466</td></tr><tr><td>18. Gravitational Radiation</td><td>106</td><td>490</td></tr><tr><td>19. Cosmology</td><td>112</td><td>520</td></tr><tr><td>20. Experimental Tests</td><td>122</td><td>560</td></tr><tr><td>21. Miscellaneous</td><td>125</td><td>575</td></tr><tr><td>INDEX</td><td colspan="2">593</td></tr></table>

# PREFACE

This book contains almost 500 problems and solutions in the fields of special relativity, general relativity, gravitation, relativistic astrophysics and cosmology. The collection is motivated by a simple premise: that the most important content of this field does not lie in its rigorous axiomatic development, nor, necessarily, in its intrinsic aesthetic beauty, but rather does lie in computable results, predictions, and models for phenomena in the real universe. Accordingly, we have aimed for problems whose statement is broadly understandable in physical terms and have tried to make their statement independent of notational conventions. We hope to awaken the reader's curiosity. ("Now how would one show that...?") We have steered clear of purely technical problems, found in texts, of the form "prove equation 17.4.38." In our solutions we also try to show the reader "good" ways to compute things, methods and tricks which can vastly reduce the labor of a plug-in and grind-away approach, but we also try to avoid the opposite pitfall of introducing too much confusing but powerful formalism for an easy problem. There is often a lot of leeway in this balance, and the reader should not be surprised if his solutions use a rather smaller (or larger) set of calculational tools.

The first five chapters of this book deal only with special relativity, and are designed for advanced undergraduates and graduate students in any course in modern physics, classical mechanics or electromagnetism. They are arranged roughly in order of increasing sophistication, beginning at about the easy level of Spacetime Physics by E. F. Taylor and J. A. Wheeler (Freeman, 1963); there are, however, both easy and difficult problems in each chapter.

The remainder of the book is aimed at the student in a course in general relativity and/or cosmology. The chapters cover aspects of metric geometry, the equations of Einstein's gravitation theory (and some competing theories), the effect of gravitation on other physical phenomena, and applications to a variety of experimental and astrophysical situations. A final chapter deals with some more formal topics whose applications are less direct.

Each chapter begins with an introductory note whose purpose is largely to define the notation used. These by no means constitute a complete or orderly presentation of the material covered in the chapter, but are intended to aid the student familiar with a notation different from ours. We assume that the reader has the benefit of one or more of the following texts (which we have used heavily):

C. W. Misner, K. S. Thorne, and J. A. Wheeler, Gravitation (Freeman, 1973) [cited in this book as “MTW’].   
S. Weinberg, Gravitation and Cosmology (Wiley, 1972) [cited in this book as "Weinberg)].   
R. Adler, M. Bazin, and M. Schiffer, Introduction to General Relativity 2nd ed. (McGraw-Hill, 1975).   
We have also been influenced by the following texts or monographs:   
Anderson, J. L., Principles of Relativity Physics (Academic Press, 1967).   
Batygin, V. V., and Toptygin, I. N., Problems in Electrodynamics (Academic Press - Infosearch, 1964).   
Hawking, S. W., and Ellis, G. F. R., The Large-Scale Structure of Space-Time (Cambridge University Press, 1973).   
Landau, L. D., and Lifschitz, E. M., The Classical Theory of Fields, 3rd ed., (Addison-Wesley, 1971).   
Peebles, P. J. E., Physical Cosmology (Princeton University Press, 1971).   
Robertson, H. P., and Noonan, T. W., Relativity and Cosmology (Saunders, 1968).   
Sexl, R. U., and Urbantke, H. K., Gravitation and Kosmologie, (Wiener Berichte über Gravitationsstheorie, 1973).

We have cited the primary literature where appropriate.

We are pleased to express our appreciation to colleagues who have contributed original problems to this collection: Douglas Eardley, Charles W. Misner, Don Page, Bernard F. Schutz, and our friend and teacher, Kip S. Thorne.

We are also grateful to C. R. Alcock, B. C. Barrois, J. Conwell, H. B. French, K. S. Jancaitis, C. Jayaprakash, S. J. Kovacs and W. A. Russell for valuable help in improving the problems and solutions. Our thanks go to Steve Wilson for preparing most of the illustrations in this book. We acknowledge support from the Department of Physics at the California Institute of Technology while we were there. Of course, we are responsible for the errors which inevitably must be present in a book of this sort. We have tried particularly hard for problems and solutions which are conceptually free from error, but we also apologize in advance for the algebraic slips that the diligent reader will certainly find; we invite his corrections.

A. P. LIGHTMAN

W. H. PRESS

R. H. PRICE

S.A. TEUKOLSKY

PASADENA, MAY 1974

# NOTATION

It is intended that this book be compatible with several different textbooks, each with its own system of notational conventions. Thus, no single notational system will be used exclusively in this book. In almost all instances, meanings will be clear from the context. The following is a list of the usual meanings of some frequently used symbols and conventions.

$\alpha, \beta, \mu, \nu \cdots$ Greek indices range over $0, 1, 2, 3$ and represent spacetime coordinates, components, etc.

i,j,k… Latin indices range over 1,2,3 and represent coordinates etc. in 3-dimensional space

$\mathbf{e}_{\alpha}, \mathbf{e}_{\mathrm{j}} \cdots$ Basis vectors

A (Any boldface symbol) a spacetime vector, tensor, or form

A A 3-dimensional vector

$\mathbf{A}^{\mu}, \mathbf{B}_{\beta}^{\alpha} \cdots$ Tensor components

$(\mathbf{A}^0,\mathbf{A}^1,\mathbf{A}^2,\mathbf{A}^3)$ A vector represented by its components

$(\mathbf{A}^0,\underline{\mathbf{A}})$ A vector represented by its time component and spatial part

(Caret) indicates unit vector, components in orthonormal basis

d/dλ Occasionally used to represent a vector (see Introduction to Chapter 7)

A(f) A vector operating on a function $= \mathbf{A}^{a}\mathbf{f}_{,a}$

A one-form   
$\otimes$ Outer product, tensor product e.g. $\mathbf{A} \otimes \mathbf{B}$ has components $\mathbf{A}^{\mu} \mathbf{B}^{\nu}$   
$\wedge$ Wedge product (see Introduction to Chapter 8)   
$\nabla$ Covariant derivative operator (see Introduction to Chapter 7). Also used as in ordinary physics $\nabla \times = \operatorname{curl}$ , $\nabla^2 = \operatorname{Laplacian}$ , etc.   
$\nabla_{\mathbf{A}}$ Directional derivative (see Introduction to Chapter 7)   
D/dλ Covariant derivative along a curve (see Introduction to Chapter 7)   
d Gradient operator as in e.g. the one-form $\widetilde{\mathrm{df}}$ (see introduction to Chapter 8)   
Lie derivative (see Problem 8.13)   
$\Gamma_{\beta \gamma}^{\alpha}$ Christoffel symbol (see Introduction to Chapter 7)   
□ d'Alembertian operator $\equiv \nabla^2 -\partial^2 /\partial t^2$ in Special Relativity, Partial derivative   
; Covariant derivative (see Introduction to Chapter 7)   
$\mathbf{R}_{\alpha \beta \gamma \delta}$ Riemann tensor (see Introduction to Chapter 9)   
Rαβ Ricci tensor $\equiv$ Rγayβ   
R Ricci scalar $\equiv \mathbb{R}^{\alpha}$ . Also scale factor in Robertson-Walker metric.   
$\mathbf{G}_{\alpha \beta}$ Einstein tensor (see Introduction to Chapter 9)   
$C_{\alpha \beta \gamma \delta}$ Weyl (conformal) tensor (see Introduction to Chapter 9)   
$\mathbf{K}_{ij}$ Extrinsic curvature tensor (see Introduction to Chapter 9)   
Proper time   
c Speed of light (usually taken as unity in the problems)   
G Gravitational constant (usually taken as unity in the problems)   
u 4-velocity   
a 4-acceleration $\equiv$ du/dr   
p or P 4-momentum

p or P Pressure

$\mathbf{T}^{\mu \nu}$ Stress-energy tensor (see Introduction to Chapter 5)

$\mathbf{F}^{\mu \nu}$ Electromagnetic field tensor (see Introduction to Chapter 4)

$\mathbf{J}^{\mu}$ Current density (see Introduction to Chapter 4)

J\* Angular momentum tensor (see Problems 11.1, 11.2)

$\eta_{\mu \nu}$ Minkowski metric (see Introduction to Chapter 1)

$\mathbf{h}_{\mu \nu}$ Metric perturbations (see Introduction to Chapter 13)

C.M. Center of momentum frame, center of mass

$\nu ,\omega$ Frequency in cycles per unit time, radians per unit time

$\gamma$ Lorentz factor $\equiv (1 - v^2 /c^2)^{-\frac{1}{2}}$ , or photon symbol

$\Lambda_{\beta}^{\alpha}$ Lorentz transformation matrix

det Determinant

Tr Trace

< > Average (as in $< \mathbf{E} > =$ average energy)

$<,>$ Scalar combination of vector and one-form, as in $<\tilde{\omega}, \mathbf{A}>$ (see Introduction to Chapter 8)

[ ] Antisymmetrization (see Problem 3.17) or commutator (see Introduction to Chapter 8) or discontinuity (as in Problem 21.9)

（） Symmetrization (see Problem 3.17)

$\varepsilon^{\alpha}\beta \gamma \delta$ The totally antisymmetric tensor (see Problem 3.20)

\* Duality symbol (see Problem 3.25)

Re Real part

$\Omega$ Solid angle (as in $\int \mathrm{d}\Omega$ ), angular velocity

$\mathbf{P}^{\alpha \beta}$ Projection tensor (see Problems 5.18, 6.6)

$\theta$ Expansion (see Problem 5.18)

$\sigma_{\alpha \beta}$ Shear (see Problem 5.18)

$\omega_{a\beta}$ Rotation (see Problem 5.18)

xiv

# NOTATION

$\mathbf{I}_{jk}$ Reduced quadrupole tensor (see Introduction to Chapter 18)

$\mathbf{H}_0$ Hubble constant

$\mathbf{q}_0$ Deceleration parameter

$\mathbf{M}_{\odot}, \mathbf{R}_{\odot}, \dots$ Mass, radius, of sun

z Redshift factor (see Problem 8.28, Introduction to Chapter 19)

Order of magnitude

Proportional to (e.g., $\mathbf{r}^3\propto \mathbf{t}^2$ ) or parallel vector to (e.g., $\mathbf{A}\propto \mathbf{B}$

PROBLEMS

# CHAPTER 1 SPECIAL-RELATIVISTIC KINEMATICS

The path of an observer through spacetime is called the worldline of that observer. The time measured by the observer's own clocks, called his proper time $\tau$ , is given by

$$
- \mathrm {d} r ^ {2} \equiv \mathrm {d s} ^ {2} = - \mathrm {d t} ^ {2} + \mathrm {d x} ^ {2} + \mathrm {d y} ^ {2} + \mathrm {d z} ^ {2},
$$

where $t, x, y, z$ are the observer's (Minkowski) coordinates along his path. Here, and unless noted otherwise throughout this book, we use units in which $c$ , the speed of light, is unity.

The 4-velocity $\mathbf{u}$ , with components $(\mathrm{dt} / \mathrm{d}\tau, \mathrm{dx} / \mathrm{d}\tau, \mathrm{dy} / \mathrm{d}\tau, \mathrm{dz} / \mathrm{d}\tau)$ , and 4-acceleration $\mathbf{a} \equiv \mathbf{du} / \mathrm{d}\tau$ , components $(\mathrm{d}^2\mathrm{t} / \mathrm{d}\tau^2, \mathrm{d}^2\mathbf{x} / \mathrm{d}\tau^2, \mathrm{d}^2\mathbf{y} / \mathrm{d}\tau^2, \mathrm{d}^2\mathbf{z} / \mathrm{d}\tau^2)$ , are defined on the worldline. The (contravariant) components of these or other 4-vectors are denoted $\mathbf{u}^{\alpha}, \mathbf{a}^{\beta}, \mathbf{A}^{\gamma}, \mathbf{B}^{\delta}$ , etc., where a Greek index indicates any of the 4 components $t, x, y, z \equiv 0, 1, 2, 3$ . Latin indices i, j, k... are used to indicate only the spatial components $x, y, z \equiv 1, 2, 3$ .

The Einstein summation convention is used, that is, any repeated literal index is assumed to be summed over its range. For example,

$$
\mathbf {V} = \mathbf {V} ^ {\mu} \mathbf {e} _ {\mu}
$$

expresses a vector as a sum of contravariant components multiplied by basis vectors, $\mathbf{e}_0 \equiv (1, 0, 0, 0)$ , $\mathbf{e}_1 \equiv (0, 1, 0, 0)$ , etc.

The invariant dot product of two 4-vectors is, in Minkowski coordinates,

$$
\mathbf {A} \cdot \mathbf {B} = - \mathbf {A} ^ {0} \mathbf {B} ^ {0} + \mathbf {A} ^ {1} \mathbf {B} ^ {1} + \mathbf {A} ^ {2} \mathbf {B} ^ {2} + \mathbf {A} ^ {3} \mathbf {B} ^ {3}.
$$

This can be written as $\mathbf{A} \cdot \mathbf{B} = \mathbf{A}_{\mu} \mathbf{B}^{\mu}$ , where the numbers $\mathbf{A}_{\mu}$ , called covariant components of $\mathbf{A}$ , are defined by $\mathbf{A}_{\mu} \equiv \eta_{\mu \nu} \mathbf{A}^{\nu}$ , or $\mathbf{A}^{\mu} = \eta^{\mu \nu} \mathbf{A}_{\nu}$

$$
\eta_ {\mu \nu} \equiv \left[ \begin{array}{c c c c} - 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \end{array} \right] \qquad (\mathrm {a l s o} \equiv \eta^ {\mu \nu}) .
$$

Vectors are called spacelike, timelike, or null, according to whether their square $\mathbf{v} \cdot \mathbf{v}$ is positive, negative, or zero. 4-velocities are always timelike.

Two Lorentz frames may differ by a relative 3-velocity $\underline{\mathbf{v}}$ or by a spatial rotation, or by a combination of relative velocity and rotation. If $t$ , $x$ , $y$ , $z$ are the coordinates of one frame, then the coordinates in a different frame are usually written $t'$ , $x'$ , $y'$ , $z'$ . Similarly, vector components in the primed frame are written $A^{\mu'}$ , $B_{\nu'}$ , etc., and its basis vectors are $e_{\mu'}$ . The basis vectors and the components of vectors in Lorentz frames are related by

$$
\mathbf {e} _ {\mu^ {\prime}} = \Lambda_ {\mu^ {\prime}} ^ {\alpha} \mathbf {e} _ {\alpha}, \quad \mathbf {V} _ {\mu^ {\prime}} = \Lambda_ {\mu^ {\prime}} ^ {\alpha} \mathbf {V} _ {\alpha}
$$

$$
\mathbf {V} ^ {\mu^ {\prime}} = \Lambda_ {a} ^ {\mu^ {\prime}} \mathbf {V} ^ {a} \quad (\Lambda_ {a} ^ {\mu^ {\prime}} \equiv \text {m a t r i x i n v e r s e o f} \Lambda_ {\mu^ {\prime}} ^ {a})
$$

where the $\Lambda$ 's are Lorentz transformation matrices. Of special interest are the "boost" transformations involving changes in velocity with no rotation. For a primed frame with velocity $\beta$ in the $x$ -direction,

$$
\Lambda_ {\nu} ^ {\mu^ {\prime}} = \left[ \begin{array}{c c c c} \gamma & - \gamma \beta & 0 & 0 \\ - \gamma \beta & \gamma & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \end{array} \right], \qquad \gamma \equiv (1 - \beta^ {2}) ^ {- \frac {1}{2}}.
$$

The velocity between two frames is sometimes parameterized by $\theta \equiv \tanh^{-1}\beta$ ("the rapidity parameter").

A particle of rest mass $m$ and 4-velocity $u$ has 4-momentum $p \equiv mu$ . If $m = 0$ (photons), $p$ is defined by its components in the frame of any observer $p^0 \equiv \text{photon energy}$ , $p^i \equiv p = \text{photon 3-momentum}$ .

Problem 1.1. The 4-velocity $\mathbf{u}$ corresponds to 3-velocity $\mathbf{v}$ . Express:

(a) $\mathbf{u}^0$ in terms of $|\underline{\mathbf{v}}|$   
(b) $\mathfrak{u}^{\mathrm{j}}(\mathrm{j} = 1,2,3)$ in terms of $\underline{\mathbf{v}}$   
(c) $\mathbf{u}^0$ in terms of $\mathbf{u}^j$   
(d) $\mathrm{d} / \mathrm{d}\tau$ in terms of $\mathrm{d} / \mathrm{d}t$ and $\underline{\mathbf{y}}$   
(e) $\mathbf{v}^{\mathrm{j}}$ in terms of $\mathbf{u}^{\mathrm{j}}$   
(f) $|\mathbf{v}|$ in terms of $\mathbf{u}^0$

Problem 1.2. Find the matrix for the Lorentz transformation consisting of a boost $\mathbf{v}_{\mathbf{x}}$ in the $\mathbf{x}$ -direction followed by a boost $\mathbf{v}_{\mathbf{y}}$ in the $\mathbf{y}$ -direction. Show that the boosts performed in the reverse order would give a different transformation.

Problem 1.3. If two frames move with 3-velocities $\underline{\mathbf{v}}_1$ and $\underline{\mathbf{v}}_2$ , show that their relative velocity is given by

$$
v ^ {2} = \frac {\left(v _ {1} - v _ {2}\right) ^ {2} - \left(v _ {1} \times v _ {2}\right) ^ {2}}{\left(1 - v _ {1} \cdot v _ {2}\right) ^ {2}}.
$$

Problem 1.4. A cart rolls on a long table with velocity $\beta$ . A smaller cart rolls on the first cart in the same direction with velocity $\beta$ relative to the first cart. A third cart rolls on the second cart in the same direction with relative velocity $\beta$ , and so on up to $n$ carts. What is the velocity $v_{n}$ of the $n$ th cart in the frame of the table? What does $v_{n}$ tend to as $n \to \infty$ ?

Problem 1.5. A distant camera snaps a photograph of a speeding bullet (velocity v) with length b in its rest frame. Behind the bullet and parallel to its path is a meter stick, at rest with respect to the camera. The direction to the camera is an angle $\alpha$ from the direction of the bullet's velocity. What will be the apparent length of the bullet as seen in the photo? (i.e. How much of the meter stick is hidden?).

Problem 1.6. Tachyons are hypothetical particles whose velocity is faster than light. Suppose that a tachyon transmitter emits particles of a constant

velocity $u > c$ in its rest frame. If a tachyonic message is sent to an observer at rest at a distance $L$ , how much time will elapse before a tachyonic reply can be received? How much time will elapse if the distant observer is moving directly away at velocity $v$ , and is at a distance $L$ at the instant he receives the message and replies? (Show that for $u > [1 + (1 - v^2)^{\frac{1}{2}}] / v$ the reply can be received before the signal is sent!)

Problem 1.7. Frame $S'$ moves with velocity $\underline{v}$ relative to frame $S$ . A rod in frame $S'$ makes an angle $\theta'$ with respect to the forward direction of motion. What is this angle $\theta$ as measured in $S$ ?

Problem 1.8. Frame $S'$ moves with velocity $\underline{\beta}$ relative to frame $S$ . A bullet in frame $S'$ is fired with velocity $\underline{v'}$ at an angle $\theta'$ with respect to the forward direction of motion. What is this angle $\theta$ as measured in $S$ ? What if the bullet is a photon?

Problem 1.9. Suppose that an observer at rest with respect to the fixed distant stars sees an isotropic distribution of stars. That is, in any solid angle $\mathrm{d}\Omega$ he sees $\mathrm{dN} = \mathrm{N}(\mathrm{d}\Omega /4\pi)$ stars, where $\mathbf{N}$ is the total number of stars he can see.

Suppose now that another observer (whose rest frame is $S'$ ) is moving at a relativistic velocity $\beta$ in the $e_x$ direction. What is the distribution of stars seen by this observer? Specifically, what is the distribution function $P(\theta', \phi')$ such that the number of stars seen by this observer in his solid angle $d\Omega'$ is $P(\theta', \phi') d\Omega'$ ? Check to see that $\int_{\text{sphere}} P(\theta', \phi') d\Omega' = N$ , and check that $P(\theta', \phi') \to \frac{N}{4\pi}$ as $\beta \to 0$ . Where will the observer see the stars "bunch up"?

Problem 1.10. Show that $\mathbf{A} = 3^{\frac{1}{2}}\mathbf{e}_{t} + 2^{\frac{1}{2}}\mathbf{e}_{x}$ is a unit timelike vector in special relativity. Show that the angle between $\mathbf{A}$ and $\mathbf{e}_{t}$ is not real.

Problem 1.11. Two rings rotate with equal and opposite angular velocity $\omega$ about a common center. Suppose Adam rides on one ring and Eve on the other, and that at some moment they pass each other and their clocks agree. At the moment they pass, Eve sees Adam's clock running more

slowly, so she expects to be ahead the next time they meet. But Adam expects just the reverse. What really happens? Can you reconcile this with Adam's (or Eve's) observations?

Problem 1.12. Define an imaginary coordinate $\mathbf{w} = \mathbf{i} \mathbf{t}$ . Show that a rotation of angle $\theta$ in the $\mathbf{x_i}, \mathbf{w}$ plane $(\mathrm{i} = 1,2,3)$ , where $\theta$ is a pure imaginary number, corresponds to a pure Lorentz boost in $t$ , $\mathbf{x}$ , $\mathbf{y}$ , $\mathbf{z}$ coordinates. How is the boost velocity $\mathbf{v}$ related to the angle $\theta$ ?

Problem 1.13. Show that the curve

$$
\begin{array}{l} \mathbf {x} = \int \mathbf {r} \cos \theta \cos \phi d \lambda \\ \mathbf {y} = \int \mathbf {r} \cos \theta \sin \phi d \lambda \\ z = \int r \sin \theta d \lambda \\ \mathrm {t} = \int r d \lambda , \\ \end{array}
$$

where $\mathbf{r}$ , $\theta$ and $\phi$ are arbitrary functions of $\lambda$ , is a null curve in special relativity. Under what conditions is it a null geodesic?

Problem 1.14. Show that an observer's 4-acceleration $\mathrm{du}^{\alpha} / \mathrm{d}\tau$ has only 3 independent components, and give the relation of these to the 3 components of ordinary acceleration that he would measure with a Newtonian accelerometer in his local frame.

Problem 1.15. Write the magnitude of the acceleration measured in the observer's frame as an invariant.

Problem 1.16. A particle moves with 3-velocity $\underline{\mathbf{u}}$ and 3-acceleration $\underline{\mathbf{a}}$ as seen by an inertial observer $\mathcal{O}$ . Another inertial observer $\mathcal{O}'$ has 3-velocity $\underline{\mathbf{v}}$ relative to $\mathcal{O}$ . Show that the components of acceleration of the particle parallel and perpendicular to $\underline{\mathbf{v}}$ as measured by $\mathcal{O}'$ are

$$
\begin{array}{l} \underline {{\mathsf {a}}} ^ {\prime} \| = \frac {\left(1 - \mathrm {v} ^ {2}\right) ^ {3 / 2}}{\left(1 - \underline {{\mathrm {v}}} \cdot \underline {{\mathrm {u}}}\right) ^ {3}} \underline {{\mathsf {a}}} \| \\ \underline {{{\mathsf {a}}}} _ {\perp} ^ {\prime} = \frac {(1 - \mathsf {v} ^ {2})}{(1 - \underline {{{\mathsf {v}}}} \cdot \underline {{{\mathsf {u}}}}) ^ {3}} \left[ \underline {{{\mathsf {a}}}} _ {\perp} - \underline {{{\mathsf {v}}}} \times (\underline {{{\mathsf {a}}}} \times \underline {{{\mathsf {u}}}}) \right]. \\ \end{array}
$$

Problem 1.17. An observer experiences a uniform acceleration in the $x$ direction, of magnitude $g$ . Define a coordinate system $(\overline{t}, \overline{x}, \overline{y}, \overline{z})$ for him in the following way: (i) Let the observer be at $\overline{x} = \overline{y} = \overline{z} = 0$ and let $\overline{t}$ be his proper time. (ii) Let his hyperplanes of simultaneity agree with the hyperplanes of simultaneity of an instantaneously comoving inertial frame. (iii) Let the other "coordinate stationary observers" (for whom $\overline{x}, \overline{y}, \overline{z}$ are constant) move in such a way that they are always at rest with respect to the observer on the hyperplanes of simultaneity. At $t = 0$ label all spatial points with the same labels as the momentarily comoving inertial system $t = 0, x, y, z$ .

Give the coordinate transformation between $t, x, y, z$ and $\overline{t}, \overline{x}, \overline{y}, \overline{z}$ . Show that coordinate stationary clocks cannot remain synchronized.

Problem 1.18. A mirror moves perpendicular to its plane with a velocity $\mathbf{v}$ . With what angle to the normal is a ray of light reflected, if it is incident at an angle $\theta$ ? What is the change in the frequency of the light?

Problem 1.19. A mirror is moving parallel to its plane. Show that the angle of incidence of a photon equals the angle of reflection.

Problem 1.20. A particle of rest mass $m$ and 4-momentum $p$ is examined by an observer with 4-velocity $u$ . Show that:

(a) the energy he measures is $\mathbf{E} = -\mathbf{p}\cdot \mathbf{u}$   
(b) the rest mass he attributes to the particle is $\mathbf{m}^2 = -\mathbf{p}\cdot \mathbf{p}$   
(c) the momentum he measures has magnitude $|\mathbf{p}| = [(\mathbf{p}\cdot \mathbf{u})^2 +\mathbf{p}\cdot \mathbf{p}]^{\frac{1}{2}};$   
(d) the ordinary velocity $\mathbf{v}$ he measures has magnitude

$$
| \underline {{\mathbf {v}}} | = \left[ 1 + \frac {\mathbf {p} \cdot \mathbf {p}}{(\mathbf {p} \cdot \mathbf {u}) ^ {2}} \right] ^ {\frac {1}{2}}
$$

(e) the 4-vector $\mathbf{v}$ , whose components in the observer's Lorentz frame are

$$
\mathbf {v} ^ {0} = 0, \mathbf {v} ^ {\mathrm {j}} = (\mathrm {d x} ^ {\mathrm {j}} / \mathrm {d t}) _ {\text {p a r t i c l e}} = \text {o r d i n a r y v e l o c i t y},
$$

is given by $\mathbf{v} = -\mathbf{u} - \frac{\mathbf{p}}{\mathbf{p}\cdot\mathbf{u}}$

Problem 1.21. An iron nucleus emits a Mössbauer gamma ray with frequency $\nu_{0}$ as measured in its own rest frame. The nucleus is traveling with velocity $\underline{\beta}$ with respect to some inertial observer. What frequency does the observer measure when the gamma ray reaches him? Express the answer in terms of $\underline{\beta}$ , $\nu_{0}$ , and the unit vector $\underline{\mathbf{n}}$ pointing towards the nucleus at the time it emitted the $\gamma$ -ray, as measured by the observer.

Problem 1.22. An observer receives light from a source of light which is moving with a velocity $\mathbf{v}$ ; the angle between $\mathbf{v}$ and the line between observer and source is $\theta$ at the time the light is emitted. If the observer sees no net redshift or blueshift, what is $\theta$ in terms of $|\mathbf{v}|$ ?

Problem 1.23. Suppose in some inertial frame S a photon has 4-momentum components

$$
\mathbf {p} ^ {0} = \mathbf {p} ^ {\mathbf {x}} = \mathbf {E}, \quad \mathbf {p} ^ {\mathbf {y}} = \mathbf {p} ^ {\mathbf {z}} = 0.
$$

There is a special class of Lorentz transformations - called the "little group of $\mathbf{p}$ " - which leave the components of $\mathbf{p}$ unchanged, e.g. a pure rotation through an angle $\alpha$ in the $y-z$ plane

$$
\left[ \begin{array}{c c c c} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & \cos \alpha & - \sin \alpha \\ 0 & 0 & \sin \alpha & \cos \alpha \end{array} \right] \left[ \begin{array}{c} E \\ E \\ 0 \\ 0 \end{array} \right] = \left[ \begin{array}{c} E \\ E \\ 0 \\ 0 \end{array} \right]
$$

is such a transformation. Find a sequence of pure boosts and pure rotations whose product is not a pure rotation in the $y-z$ plane, but is in the little group of $p$ .

Problem 1.24. Two giant frogs are captured, imprisoned in a large metal cylinder, and placed on an airplane. While in flight, the storage doors accidentally open and the cylinder containing the frogs falls out. Sensing something amiss, the frogs decide to try to break out. Centering themselves in the cylinder, they push off from each other and slam simultaneously into the ends of the cylinder. They instantly push off from the ends and shoot across the cylinder past each other into the opposite ends. This

continues until the cylinder hits the ground. Consider how this looks from some other inertial frame, falling at another speed. In this frame, the frogs do not hit the ends of the cylinder simultaneously, so the cylinder jerks back and forth about its mean speed $\beta$ . The cylinder, however, was at rest in one inertial frame. Does this mean that one inertial frame can jerk back and forth with respect to another?

Problem 1.25. Let $\mathbf{J}_{\mathbf{x}}, \mathbf{J}_{\mathbf{y}}, \mathbf{J}_{\mathbf{z}}$ be infinitesimal rotation operators defined so that $1 + \mathrm{i}\mathbf{J}_{\mathbf{j}}\theta / 2$ is a rotation by a small angle $\theta$ around the j-axis. Let $\mathbf{K}_{\mathbf{x}}, \mathbf{K}_{\mathbf{y}}, \mathbf{K}_{\mathbf{z}}$ be infinitesimal boost operators defined so that $1 + \mathrm{i}\mathbf{K}_{\mathbf{j}}\mathbf{v} / 2$ is a boost by a small velocity $\mathbf{v}$ in the j-direction. Show that the following relationships, and all their cyclic permutations, are true:

$$
\begin{array}{l} [ J _ {x}, J _ {y} ] = 2 i J _ {z} \\ [ J _ {x}, K _ {y} ] = 2 i K _ {z} \\ \left[ \mathrm {K} _ {\mathbf {x}}, \mathrm {K} _ {\mathbf {y}} \right] = - 2 \mathrm {i} \mathrm {J} _ {z}. \\ \end{array}
$$

Find a representation of the Lorentz group in terms of Pauli spin matrices $\sigma_{\mathbf{x}}$ , $\sigma_{\mathbf{y}}$ , $\sigma_{\mathbf{z}}$ , and the unit matrix.

Problem 1.26. Two successive, arbitrary pure Lorentz boosts $\underline{\mathbf{v}}_1$ and $\underline{\mathbf{v}}_2$ are equivalent to a pure boost $\underline{\mathbf{v}}_3$ followed by a pure rotation $\theta \underline{\mathbf{n}}$ , where $\mathbf{n}$ is a unit vector. Find the magnitude of $\theta$ in terms of $\underline{\mathbf{v}}_1$ and $\underline{\mathbf{v}}_2$ and show that $\underline{\mathbf{n}} \cdot \underline{\mathbf{v}}_3 = 0$ .

Problem 1.27. Show that any proper (non time-reversing, non parity-reversing) homogeneous Lorentz transformation leaves fixed at least one null direction.

Problem 1.28. What is the least number of pure boosts which generate an arbitrary Lorentz transformation? Note: This is a difficult problem!

# CHAPTER 2

# SPECIAL-RELATIVISTIC DYNAMICS

In our laboratory frame, a particle with 4-momentum $\mathbf{p}$ has total energy $\mathbf{E} = \mathbf{p}^{0}$ and 3-momentum $\underline{\mathbf{p}} = \mathbf{p}^{\dot{\mathbf{i}}}$ . If the particle has a nonzero rest mass $\mathfrak{m}$ , the 4-momentum, 4-velocity $\mathbf{u}$ and 3-velocity $\underline{\mathbf{v}}$ are related by

$$
\mathbf {p} = \operatorname {m u} = \operatorname {m} (\gamma , \gamma_ {\mathbf {v}}), \quad \gamma \equiv (1 - \mathbf {v} ^ {2}) ^ {- \frac {1}{2}},
$$

so $\mathbf{E} = \gamma \mathbf{m}$ , $\underline{\mathfrak{p}} = \gamma \underline{\mathfrak{m}}$ . The square of a particle's 4-momentum, an invariant in all frames, is

$$
\mathbf {p} \cdot \mathbf {p} = - \mathrm {E} ^ {2} + \underset {\sim} {\mathrm {p}} ^ {2} = - \mathrm {m} ^ {2}.
$$

The kinetic energy of a particle is $\mathbf{T} \equiv \mathbf{E} - \mathfrak{m}$ .

The fundamental dynamical law for particle interactions is that in any frame the vector sum of the 4-momenta of all particles is a conserved constant in time.

00000000

Problem 2.1. (Compton scattering.) A photon of wavelength $\lambda$ hits a stationary electron (mass $m_{e}$ ) and comes off with wavelength $\lambda'$ at an angle $\theta$ . Derive the expression

$$
\lambda^ {\prime} - \lambda = \left(\mathrm {h} / \mathrm {m} _ {\mathrm {e}}\right) (1 - \cos \theta).
$$

# Problem 2.2.

(a) When a photon scatters off a charged particle which is moving with a speed very nearly that of light, the photon is said to have undergone an inverse Compton scattering. Consider an inverse Compton scattering in which a charged particle of rest mass $m$ and total mass-energy (as seen

in the lab frame) $\mathbf{E} \gg \mathfrak{m}$ , collides head-on with a photon of frequency $\nu (\mathrm{h}\nu \ll \mathrm{m})$ . What is the maximum energy the particle can transfer to the photon?

(b) If space is filled with black-body radiation of temperature $3^{0} \mathrm{~K}$ and contains cosmic ray protons of energies up to $10^{20} \mathrm{eV}$ , how much energy can a proton of energy $10^{20} \mathrm{eV}$ transfer to a $3^{0} \mathrm{~K}$ photon?

Problem 2.3. Show that it is impossible for an isolated free electron to absorb or emit a photon.

Problem 2.4. A particle of rest mass $\mathfrak{m}_1$ and velocity $\underline{\mathbf{v}}_1$ collides with a stationary particle of rest mass $\mathfrak{m}_2$ and is absorbed by it. Find the rest mass $\mathfrak{m}$ and velocity $\underline{\mathbf{v}}$ of the resultant compound system.

Problem 2.5. The beta-decay of a neutron is isotropic in the rest frame of the neutron, with the velocity of the emitted electron $\mathbf{v}_{\mathbf{e}} = 0.77$ . If the neutron is moving with velocity $\beta$ through the laboratory, what values of the electron's laboratory momentum vector $\underline{\mathbf{P}}$ are possible?

Problem 2.6. Evaluate the "available energy" of two different proton-proton scattering experiments. The first is of the conventional type, where a beam of protons is accelerated to $30\mathrm{GeV}$ and allowed to strike a target (liquid hydrogen, for example). In the second, two separate beams of protons are accelerated to $15\mathrm{GeV}$ each, then directed toward each other and allowed to collide. Evaluate the total energy of two colliding protons in the center of momentum frame for each experiment. To what energy would a beam in the first type of experiment have to be accelerated to match the CM energy of the $15\mathrm{GeV}$ protons in the second experiment?

Problem 2.7. A particle of rest mass $m$ collides elastically with a stationary particle of equal mass. The incident particle has kinetic energy $T_0$ . What is its kinetic energy after the collision, if the scattering angle is $\theta$ ?

Problem 2.8. Calculate the threshold energy of a nucleon $\mathbf{N}$ for it to undergo the reaction

$$
\gamma + \mathbf {N} \rightarrow \mathbf {N} + \pi
$$

where $\gamma$ represents a photon of temperature $3^0\mathrm{K}$ . Assume the collision is head-on; take the photon energy to be $\sim \mathrm{kT}$ ; $\mathfrak{m}_{\mathbf{N}} = 940\mathrm{MeV}$ ; $\mathfrak{m}_{\pi} = 140\mathrm{MeV}$ . (This effect probably produces a cut-off in the cosmic-ray spectrum at this threshold energy.)

Problem 2.9. Consider the reaction $\pi^{+} + n \rightarrow K^{+} + \Lambda^{0}$ . The rest masses of the particles are $m_{\pi} = 140 \, \text{MeV}$ , $m_{n} = 940 \, \text{MeV}$ , $m_{K} = 494 \, \text{MeV}$ , $m_{\Lambda} = 1115 \, \text{MeV}$ . What is the threshold kinetic energy of the $\pi$ to create a $K$ at an angle of $90^{\circ}$ in the lab in which the $n$ is at rest?

Problem 2.10. Consider the reaction $\mathbf{A} \rightarrow \mathbf{B} + \mathbf{C}$ (with particle masses $\mathfrak{m}_{\mathbf{A}}, \mathfrak{m}_{\mathbf{B}}, \mathfrak{m}_{\mathbf{C}}$ ).

(a) If $\mathbf{A}$ is at rest in the lab frame, show that in the lab frame particle B has energy $\mathbf{E}_{\mathbf{B}} = (\mathfrak{m}_{\mathbf{A}}^{2} + \mathfrak{m}_{\mathbf{B}}^{2} - \mathfrak{m}_{\mathbf{C}}^{2}) / 2\mathfrak{m}_{\mathbf{A}}$ .   
(b) An atom of mass M at rest decays to a state of rest energy M-δ by emitting a photon of energy hν. Show that hν < δ. In the Mössbauer effect, why is hν = δ?   
(c) If A decays while moving in the lab frame, find the relation between the angle at which B comes off, and the energies of A and B.

Problem 2.11. Consider the reaction $1 + 2 \rightarrow 3 + 4$ . The lab frame is defined to be the one in which $\underline{\mathbf{P}}_2 = 0$ . The C.M. frame is defined to be the one in which $\underline{\mathbf{P}}_1^{\mathbf{C.M.}} + \underline{\mathbf{P}}_2^{\mathbf{C.M.}} = 0$ . Show that:

(a) $\mathbf{E}_{\mathrm{total}}^{\mathbf{C.M.}} = \left(\mathfrak{m}_1^2 +\mathfrak{m}_2^2 +2\mathfrak{m}_2\mathbf{E}_1\right)^{\frac{1}{2}}$   
(b) $\mathbf{E}_1^{\mathbf{C.M.}} = \left[\left(\mathbf{E}_{\mathrm{total}}^{\mathbf{C.M.}}\right)^2 +\mathbf{m}_1^2 -\mathbf{m}_2^2\right] / 2\mathbf{E}_{\mathrm{total}}^{\mathbf{C.M.}}$   
(c) $\mathbf{P}_1^{\mathbf{C},\mathbf{M}.} = \mathfrak{m}_2\mathbf{P}_1 / \mathbf{E}_{\mathrm{total}}^{\mathbf{C},\mathbf{M}}.$   
(d) $\gamma_{\mathbf{C.M.}} = (\mathrm{E_1 + m_2}) / \mathrm{E}_{\mathrm{total}}^{\mathbf{C.M.}}$ (v.C.M. $\equiv$ velocity of C.M. in lab frame, and $\gamma_{\mathbf{C.M.}}\equiv (1 - \mathrm{v}^{2}_{\mathbf{C.M.}})^{-\frac{1}{2}}.$ )   
(e) $\mathbf{v}_{\mathbf{C},\mathbf{M}.} = \mathbf{P}_1 / (\mathbf{E}_1 + \mathbf{m}_2)$ .

Problem 2.12. Consider the elastic collision of a particle of mass $m_1$ with a stationary particle of mass $m_2 < m_1$ . Let $\theta_{\max}$ be the maximum scattering angle of $m_1$ . In nonrelativistic calculations, $\sin \theta_{\max} = m_2 / m_1$ . Prove that this result also holds relativistically.

# Problem 2.13.

(a) If a rocket has engines that give it a constant acceleration of $1 \, \text{g}$ (relative to its instantaneous inertial frame, of course), and the rocket starts from rest near the earth, how far from the earth (as measured in the earth's frame) will the rocket be in 40 years as measured on the earth? How far after 40 years as measured in the rocket?   
(b) Compute the proper time for the occupants of a rocket ship to travel the 30,000 light years from the Earth to the center of the galaxy. Assume they maintain an acceleration of $1\mathrm{g}$ for half the trip and decelerate at $1\mathrm{g}$ for the remaining half.   
(c) What fraction of the initial mass of the rocket can be payload in part (b)? Assume an ideal rocket that converts rest mass into radiation and ejects all of the radiation out of the back with $100\%$ efficiency and perfect collimation.

Problem 2.14. What is the maximum energy one could get out of a fixed frequency electron cyclotron with accelerating potential $V$ .

Problem 2.15. A new force field $\mathbf{F}^{\mu}(\mathbf{x}^{\nu})$ is discovered which induces a 4-acceleration $a^\mu \equiv \mathrm{du}^\mu /\mathrm{d}\tau = \mathfrak{m}^{-1}\mathrm{F}^\mu (\mathbf{x}^\nu)$ on a particle of mass m, at position $\mathbf{x}^{\nu}$ . Notice that $\mathbf{F}^{\mu}$ does not depend on $\mathbf{u}^{\nu}$ . Show that this force is not consistent with special relativity.

# CHAPTER 3

# SPECIAL-RELATIVISTIC COORDINATE TRANSFORMATIONS, INVARIANTS AND TENSORS

Spacetime in special relativity can be described by more general (curvilinear) coordinates than "inertial" or Minkowski coordinates, e.g. coordinates $v^{\mu'}$ .

$$
\mathbf {x} ^ {\mu^ {\prime}} = \mathbf {f} ^ {\mu} (\mathbf {x} ^ {\nu})
$$

where $\mathbf{x}^{\nu}$ are Minkowski coordinates, and $\mathbf{f}^{\mu}$ four arbitrary functions. One then shows that the basis vectors and components of vectors in the new coordinates are related to the old by

$$
\begin{array}{l} \mathbf {e} _ {\alpha^ {\prime}} = \frac {\partial \mathbf {x} ^ {\mu}}{\partial \mathbf {x} ^ {\alpha}}, \mathbf {e} _ {\mu}, \quad \mathbf {e} _ {\mu} = \frac {\partial \mathbf {x} ^ {\alpha^ {\prime}}}{\partial \mathbf {x} ^ {\mu}} \mathbf {e} _ {\alpha^ {\prime}} \\ V ^ {\alpha^ {\prime}} = \frac {\partial_ {X} ^ {\alpha^ {\prime}}}{\partial_ {X} ^ {\mu}} V ^ {\mu}, \quad V ^ {\mu} = \frac {\partial_ {X} ^ {\mu}}{\partial_ {X} ^ {\alpha}}, V ^ {\alpha^ {\prime}} \\ V _ {\alpha^ {\prime}} = \frac {\partial_ {X} ^ {\mu}}{\partial_ {X} ^ {\alpha}}, V _ {\mu}, \quad V _ {\mu} = \frac {\partial_ {X} ^ {\alpha^ {\prime}}}{\partial_ {X} ^ {\mu}} V _ {\alpha^ {\prime}}. \\ \end{array}
$$

In other words, the transformation matrix $\Lambda_{a}^{\mu^{'}}\equiv \partial_{\mathbf{x}}\mu^{'} / \partial_{\mathbf{x}}^{a}$ replaces the less general Lorentz matrices (which are applicable only for transformations between two systems of Minkowski coordinates).

In general coordinates, the relation $\mathbf{A} \cdot \mathbf{B} = \mathbf{A}_{\mu}\mathbf{B}^{\mu}$ still holds, but we no longer have $\mathbf{A}_{\mu} = \eta_{\mu \nu}\mathbf{A}^{\mu}$ . Rather, corresponding to every coordinate system there is a metric tensor with components $\mathbf{g}_{\alpha \beta}$ , such that $\mathrm{ds}^2 = \mathbf{g}_{\alpha \beta}\mathrm{dx}^\alpha \mathrm{dx}^\beta$ , which leads to $\mathbf{A}_{\mu} = \mathbf{g}_{\mu \nu}\mathbf{A}^\nu$ and therefore $\mathbf{A} \cdot \mathbf{B} = \mathbf{g}_{\mu \nu}\mathbf{A}^\mu \mathbf{B}^\nu$ . Note also $\mathbf{A}^\mu = \mathbf{g}^{\mu \nu}\mathbf{A}_\nu$ where $\mathbf{g}^{\mu \nu}$ is the matrix inverse of $\mathbf{g}_{\mu \nu}$ .

Various formal definitions of a tensor are possible. Here, it suffices to say that it is a geometrical object which, like a vector, has components

whose numerical values are different in different coordinate systems. A tensor has $4^{\mathbf{n}}$ components, where $\mathfrak{n}$ is its rank (number of "slots" or indices for components). Slots may be contravariant or covariant; examples: $\mathrm{T}^{\mu \nu}$ , $\mathbf{F}_{\mu \nu}$ , $\mathbb{R}^{\alpha}$ , $\beta \gamma \delta$ , $\mathbf{G}_{\mu}^{\nu}$ . Tensors transform with one matrix for each slot, e.g.

$$
\mathbf {G} _ {\mu} ^ {\nu^ {\prime}} = \Lambda_ {\mu^ {\prime}} ^ {a} \Lambda_ {\beta} ^ {\nu^ {\prime}} \mathbf {G} _ {a} ^ {\beta}.
$$

Tensors may be "contracted" (a covariant and a contravariant index summed) or multiplied as a "direct product" with other tensors or with themselves to form new tensors, e.g.

$$
\mathrm {Q} _ {\mu \nu} = \mathsf {R} _ {\mu a \nu} ^ {a}, \quad \mathrm {A} ^ {\mu} = \mathsf {G} _ {\nu} ^ {\mu} \mathsf {B} ^ {\nu}, \quad \mathrm {F} _ {\mu \nu} = \mathsf {A} _ {\mu} \mathsf {B} _ {\nu}.
$$

A special case is contraction with the metric tensor, where the same symbol is usually used for the result as in the relation of covariant and contravariant vectors, $\mathbf{F}^{\mu}_{\nu} = \mathbf{g}_{\nu \alpha}\mathbf{F}^{\mu \alpha}$ . A tensor expression with no free indices, e.g. $\mathbf{F}_{\mu \nu}\mathbf{A}^{\mu}\mathbf{A}^{\nu}$ or $\mathbf{R}_{\beta \gamma}\mathbf{F}^{\beta \gamma}$ or $\mathbf{A}^{\alpha}\mathbf{B}^{\beta}\mathbf{g}_{\alpha \beta}$ , is a scalar and is an invariant number in all frames. The analog of the index free notation $\mathbf{A}$ for a vector $\mathbf{A}^{\mu}$ is to write, e.g. $\mathbf{T}$ for a tensor $\mathbf{T}^{\mu \nu}$ . In both cases the existence of covariant or contravariant slots must be deduced from the context.

In index free notation, $\otimes$ represents the direct product, e.g. $\mathbf{F}^{\mu \nu}\mathbf{A}^{\rho}$ is written $\mathbf{F} \otimes \mathbf{A}$ ; the contracted product is written with a dot, e.g. $\mathbf{F} \cdot \mathbf{A}$ for $\mathbf{F}^{\mu \alpha}\mathbf{A}_{\alpha}$ .

We denote partial derivatives by a comma, e.g. $\mathbf{f}_{,\alpha} \equiv \partial \mathbf{f} / \partial \mathbf{x}^{\alpha}$ .

000000000

# Problem 3.1.

(I) If 2 events are separated by a spacelike interval, show that

(a) there exists a Lorentz frame in which they are simultaneous, and   
(b) in no Lorentz frame do they occur at the same point.

(II) If 2 events are separated by a timelike interval, show that

(a) there exists a frame in which they happen at the same point, and   
(b) in no Lorentz frame are they simultaneous.

Problem 3.2. Find 4 linearly independent null vectors in Minkowski space. Can you find 4 which are orthogonal?

Problem 3.3. Show that the only non-spacelike vectors orthogonal to a given nonzero null vector are multiples of it.

Problem 3.4. Show that the sum of two vectors can be spacelike, null, or timelike, independently of whether the two vectors are spacelike, null, or timelike.

Problem 3.5. Show that the cross-sectional area of a parallel beam of light is invariant under Lorentz transformations.

Problem 3.6. Show that $\sum_{\mu} \mathrm{D}^{\mu \mu}$ and $\sum_{\mu} \mathrm{D}_{\mu \mu}$ are not invariant under coordinate transformations, but that $\sum_{\mu} \mathrm{D}_{\mu}^{\mu}$ is invariant. (Take $\mathbf{D}$ to be a tensor defined by its components $\mathrm{D}^{\mu \nu}$ .)

Problem 3.7. $\mathbf{F}^{\alpha \beta}$ is antisymmetric on its two indices. Show that

$$
\mathrm {F} _ {\mu} ^ {\alpha}, \nu \mathrm {F} _ {\alpha} ^ {\nu} = - \mathrm {F} _ {\mu \alpha , \beta} \mathrm {F} ^ {\alpha \beta}.
$$

Problem 3.8. In a coordinate system with coordinates $\mathbf{x}^{\mu}$ , the invariant line element is $\mathrm{ds}^2 = \eta_{\alpha \beta} \mathrm{dx}^\alpha \mathrm{dx}^\beta$ . If the coordinates are transformed $\mathbf{x}^{\mu} \rightarrow \overline{\mathbf{x}}^{\mu}$ , show that the line element is $\mathrm{ds}^2 = \mathbf{g}_{\overline{\mu} \overline{\nu}} \mathrm{d}\overline{\mathbf{x}}^\mu \mathrm{d}\overline{\mathbf{x}}^\nu$ , and express $\mathbf{g}_{\overline{\mu} \overline{\nu}}$ in terms of the partial derivatives $\partial \mathbf{x}^{\mu} / \partial \overline{\mathbf{x}}^{\nu}$ . For two arbitrary 4-vectors $\mathbf{U}$ and $\mathbf{V}$ , show that

$$
\mathbf {U} \cdot \mathbf {V} = \mathbf {U} ^ {\alpha} \mathbf {V} ^ {\beta} \eta_ {\alpha \beta} = \mathbf {U} ^ {\overline {{\alpha}}} \mathbf {V} ^ {\overline {{\beta}}} \mathbf {g} _ {\overline {{\alpha}}} \overline {{\beta}}.
$$

Problem 3.9. Show that the determinant of the metric tensor $\mathbf{g} \equiv \det(\mathbf{g}_{\mu \nu})$ is not a scalar.

Problem 3.10. If $\Lambda_{\beta}^{a}$ and $\tilde{\Lambda}_{\beta}^{a}$ are two matrices which transform the components of a tensor from one coordinate basis to another, show that the matrix $\Lambda_{\gamma}^{a}\tilde{\Lambda}_{\beta}^{\gamma}$ is also a coordinate transformation.

Problem 3.11. You are given a tensor $\mathbf{K}^{\alpha \beta}$ . How can you test whether it is a direct product of two vectors $\mathbf{K}^{\alpha \beta} = \mathbf{A}^{\alpha} \mathbf{B}^{\beta}$ ? Can you express the test in coordinate-free language?

Problem 3.12. Prove that the general second-rank tensor in $n$ -dimensions cannot be represented as a simple direct product of two vectors, but can be expressed as a sum over many such products.

Problem 3.13. A two index "object" $\mathbf{X}^{\mu \nu}$ is defined by the "direct sum" of two vectors $\mathbf{X}^{\mu \nu} = \mathbf{A}^{\mu} + \mathbf{B}^{\nu}$ . Is $\mathbf{X}^{\mu \nu}$ a tensor? Is there a transformation law to take $\mathbf{X}$ to a new coordinate system, i.e. to obtain $\mathbf{X}^{\hat{\mu}\hat{\nu}}$ from $\mathbf{X}^{\mu \nu}$ ?

Problem 3.14. Show that a second rank tensor $\mathbf{F}$ which is antisymmetric in one coordinate frame $(\mathbf{F}_{\mu \nu} = -\mathbf{F}_{\nu \mu})$ is antisymmetric in all frames. Show that the contravariant components are also antisymmetric $(\mathbf{F}^{\mu \nu} = -\mathbf{F}^{\nu \mu})$ . Show that symmetry is also coordinate invariant.

Problem 3.15. Let $\mathbf{A}_{\mu \nu}$ be an antisymmetric tensor so that $\mathbf{A}_{\mu \nu} = -\mathbf{A}_{\nu \mu}$ ; and let $\mathbf{S}^{\mu \nu}$ be a symmetric tensor so that $\mathbf{S}^{\mu \nu} = \mathbf{S}^{\nu \mu}$ . Show that $\mathbf{A}_{\mu \nu} \mathbf{S}^{\mu \nu} = 0$ . Establish the following two identities for any arbitrary tensor $\mathbf{V}_{\mu \nu}$ :

$$
\mathrm {V} ^ {\mu \nu} \mathrm {A} _ {\mu \nu} = \frac {1}{2} \left(\mathrm {V} ^ {\mu \nu} - \mathrm {V} ^ {\nu \mu}\right) \mathrm {A} _ {\mu \nu}, \qquad \mathrm {V} ^ {\mu \nu} \mathrm {S} _ {\mu \nu} = \frac {1}{2} \left(\mathrm {V} ^ {\mu \nu} + \mathrm {V} ^ {\nu \mu}\right) \mathrm {S} _ {\mu \nu}.
$$

# Problem 3.16.

(a) In an $n$ -dimensional metric space, how many independent components are there for an $r$ -rank tensor $T^{\alpha \beta \cdots}$ with no symmetries?   
(b) If the tensor is symmetric on $s$ of its indices, how many independent components are there?   
(c) If the tensor is antisymmetric on a of its indices, how many independent components are there?

Problem 3.17. We define the meaning of square and round brackets enclosing a set of indices as follows:

$$
\mathrm {V} _ {(a _ {1}, \dots , a _ {p})} \equiv \frac {1}{p !} \Sigma \mathrm {V} _ {a _ {\pi_ {1}} \dots a _ {\pi_ {p}}}; \qquad \mathrm {V} _ {[ a _ {1}, \dots a _ {p} ]} \equiv \frac {1}{p !} \Sigma (- 1) ^ {\pi} \mathrm {V} _ {a _ {\pi_ {1}} \dots a _ {\pi_ {p}}} .
$$

Here the sum is taken over all permutations $\pi$ of the numbers $1,2,\dots ,\mathfrak{p}$ and $(-1)^{\pi}$ is $+1$ or $-1$ depending on whether the permutation is even or odd. The quantity $\mathbf{V}$ may have other indices, not shown here, besides the set of $\mathfrak{p}$ indices $a_1,a_2,\dots ,a_{\mathfrak{p}}$ , but only this set of indices is affected by the operations described here. The numbers $\pi_1,\pi_2,\dots ,\pi_{\mathfrak{p}}$ are the numbers $1,2,\dots ,\mathfrak{p}$ rearranged according to the permutation $\pi$ . Thus for example $\mathrm{V}_{(a_1a_2)}\equiv \frac{1}{2} (\mathrm{V}_{a_1a_2} + \mathrm{V}_{a_2a_1})$ or equivalently $\mathrm{V}_{(\mu \nu)} = \frac{1}{2} (\mathrm{V}_{\mu \nu} + \mathrm{V}_{\nu \mu})$ .

(a) If $\mathbf{F}$ is antisymmetric and $\mathbf{T}$ is symmetric, apply these definitions to give explicit formulas for the following: $\mathrm{V}_{[\mu \nu ]}$ , $\mathrm{F}_{[\mu \nu ]}$ , $\mathrm{F}_{(\mu \nu)}$ , $\mathrm{T}_{[\mu \nu ]}$ , $\mathrm{T}_{(\mu \nu)}$ , $\mathrm{V}_{[a\beta \gamma ]}$ , $\mathrm{T}_{(a\beta ,\gamma)}$ , $\mathrm{F}_{[a\beta ,\gamma ]}$ .   
(b) Establish the following formulae: $\mathbf{V}((a_1 \cdots a_p)) = \mathbf{V}(a_1 \cdots a_p)$ ; $\mathbf{V}[[a_1 \cdots a_p]] = \mathbf{V}[a_1 \cdots a_p]$ ; $\mathbf{V}(a_1 \cdots [a_\ell a_m] \cdots a_p) = 0$ ; $\mathbf{V}[a_1 \cdots [a_\ell a_m] \cdots a_p] = \mathbf{V}[a_1 \cdots a_\ell a_m \cdots a_p]$ .   
(c) Use these notations to show that $\mathbf{F}_{\mu \nu} = \mathbf{A}_{\nu, \mu} - \mathbf{A}_{\mu, \nu}$ implies $\mathbf{F}_{a\beta, \nu} + \mathbf{F}_{\beta\nu, a} + \mathbf{F}_{\nu a, \beta} = 0$ . (Half of Maxwell's equations!)

Problem 3.18. Show for any two-index tensor $\mathbf{X}$ , that $\mathbf{X}_{\alpha \beta} = \mathbf{X}_{(\alpha \beta)} + \mathbf{X}_{[\alpha \beta]}$ where ( ) and [ ] denote symmetrization and antisymmetrization, respectively. Show that in general

$$
\mathbf {Y} _ {\alpha \beta \gamma} \neq \mathbf {Y} _ {(a \beta \gamma)} + \mathbf {Y} _ {[ a \beta \gamma ]}.
$$

Problem 3.19. Prove that the Kronecker delta, $\delta_{\nu}^{\mu}$ , is a tensor.

Problem 3.20. Prove that, except for scaling by a constant, there is a unique tensor $\varepsilon_{\alpha \beta \gamma \delta}$ which is totally antisymmetric on all its 4 indices. The usual choice is to take $\varepsilon_{0123} = 1$ in Minkowski coordinates. What are the components of $\varepsilon$ in a general coordinate frame, with metric $g_{\mu \nu}$ ?

Problem 3.21. In an orthonormal frame, show that

$$
\varepsilon_ {\alpha \beta \gamma \delta} = - \varepsilon^ {\alpha \beta \gamma \delta}.
$$

What is the analogous relation in a general coordinate frame with metric $\mathbf{g}_{\mu \nu}$ ?

Problem 3.22. Evaluate $\varepsilon_{\mu \nu \rho \sigma} \varepsilon^{\mu \nu \rho \sigma}$ .

Problem 3.23. Show that for any tensor $\mathbf{A}^{\alpha}\beta$

$$
\varepsilon_ {\alpha \beta \gamma \delta} \mathbf {A} _ {\mu} ^ {\alpha} \mathbf {A} _ {\nu} ^ {\beta} \mathbf {A} _ {\lambda} ^ {\gamma} \mathbf {A} _ {\sigma} ^ {\delta} = \varepsilon_ {\mu \nu \lambda \sigma} \det  \| \mathbf {A} _ {\beta} ^ {\alpha} \|
$$

where $\| \mathbf{A}^{\alpha}\boldsymbol {\beta}\|$ is the matrix of the components $\mathbf{A}^{\alpha}\boldsymbol{\beta}$ .

Problem 3.24. Show that four vectors $\mathbf{u}, \mathbf{v}, \mathbf{w}, \mathbf{x}$ , are linearly independent if and only if $\mathbf{u} \wedge \mathbf{v} \wedge \mathbf{w} \wedge \mathbf{x} \neq 0$ . Show that in this case $\mathbf{u} \wedge \mathbf{v} \wedge \mathbf{w} \wedge \mathbf{x}$ is proportional to the totally antisymmetric tensor $\varepsilon$ . (The “wedge” product is defined as the antisymmetrized direct product, e.g. $\mathbf{u} \wedge \mathbf{v} = \mathbf{u} \otimes \mathbf{v} - \mathbf{v} \otimes \mathbf{u}$ .)

Problem 3.25. Let $\mathbf{F}$ be an antisymmetric second-rank tensor with components $\mathbf{F}^{\mu \nu}$ . From $\mathbf{F}$ construct another second-rank, anti-symmetric tensor, $*\mathbf{F}$ , called the dual of $\mathbf{F}$ , as follows

$$
* \mathbf {F} = \frac {1}{2} \varepsilon^ {\mu \nu \alpha \beta} \mathbf {F} _ {\alpha \beta} \mathbf {e} _ {\mu} \otimes \mathbf {e} _ {\nu}.
$$

Show that $\mathbf{\Phi}(*\mathbf{F}) = -\mathbf{F}$

Problem 3.26. Show that

$$
\mathbf {V} _ {\sigma} \mathbf {V} ^ {\sigma} = - \frac {1}{3 !} \left(* \mathbf {V}\right) _ {a \beta \gamma} \left(* \mathbf {V}\right) ^ {a \beta \gamma} .
$$

Problem 3.27. The tensor $\delta_{\rho \dots \sigma}^{\mu \dots \lambda}$ is defined by

$$
\delta_ {\rho \dots \sigma} ^ {\mu \dots \lambda} \equiv \det  \left[ \begin{array}{c} \delta_ {\rho} ^ {\mu} \dots \delta_ {\rho} ^ {\lambda} \\ \vdots & \vdots \\ \delta_ {\sigma} ^ {\mu} \dots \delta_ {\sigma} ^ {\lambda} \end{array} \right].
$$

Show that if there are more than 4 upper (or lower) indices, the tensor identically vanishes.

Problem 3.28. Show that $\delta_{\lambda \kappa}^{\mu \nu} = -\frac{1}{2}\varepsilon^{\mu \nu \rho \sigma}\varepsilon_{\lambda \kappa \rho \sigma},$ and generalize to $\delta_{\lambda \dots \kappa}^{\mu \dots \nu}$ of other ranks.

Problem 3.29. Show that if the antisymmetric tensor $\mathfrak{p}^{\alpha \beta}$ is a bivector (i.e. $\mathfrak{p}^{\alpha \beta} = \mathbf{A}^{[\alpha \mathbf{B}^{\beta}]}.$ ) then

$$
\mathsf {p} ^ {\alpha \beta} \mathsf {p} ^ {\gamma \delta} + \mathsf {p} ^ {\alpha \gamma} \mathsf {p} ^ {\delta \beta} + \mathsf {p} ^ {\alpha \delta} \mathsf {p} ^ {\beta \gamma} = 0
$$

(the Plücker relations).

Problem 3.30. In 4-space define the 3-dimensional volume element in a hypersurface $\mathbf{x}^{\alpha} = \mathbf{x}^{\alpha}(\mathbf{a},\mathbf{b},\mathbf{c})$ by $\mathrm{d}^3\Sigma_\mu = (1 / 3!) \varepsilon_{\mu \alpha \beta \gamma} \mathrm{da} \mathrm{db} \mathrm{dc} [\partial (\mathbf{x}^\alpha ,\mathbf{x}^\beta ,\mathbf{x}^\gamma) / \partial (\mathbf{a},\mathbf{b},\mathbf{c})]$ , where the last factor is a $3\times 3$ Jacobian determinant. Compute the components of $\mathrm{d}^3\Sigma_\mu$ for a space-like hypersurface $\mathbf{x}^0 =$ constant, parameterized by $\mathbf{x}^1 = \mathbf{a}$ , $\mathbf{x}^2 = \mathbf{b}$ , $\mathbf{x}^3 = \mathbf{c}$ .

Problem 3.31. Show that the invariant proper volume element in 4-dimensional space is given by

$$
\mathrm {d V} = (- \mathbf {g}) ^ {\frac {1}{2}} \mathrm {d} ^ {4} \mathbf {x}
$$

where $\mathrm{d}^4\mathbf{x} = \mathrm{dxdydzdt}$ in the coordinate system of the metric $\mathbf{g}_{\mu \nu}$ .

Problem 3.32. Show that the proper 3-volume element of an observer with 4-velocity $\mathbf{u}$ is $\mathrm{d}^3\mathbf{V} = (-\mathbf{g})^{\frac{1}{2}}\mathbf{u}^0\mathrm{d}^3\mathbf{x}$ , and show that this is a scalar invariant.

Problem 3.33. What is the invariant volume element of contravariant momentum $\mathsf{d}^4\mathbf{P}$ for 4-dimensional momentum space? What is the invariant 3-volume "on the mass shell", i.e. when the constraint $(-\mathbf{P}\cdot \mathbf{P})^{\frac{1}{2}} = \mathfrak{m}$ is imposed?

Problem 3.34. A group of $\mathbf{N}$ particles is seen to occupy a volume $\mathrm{d}x \, \mathrm{d}y \, \mathrm{d}z \, \mathrm{d}\mathbf{P}^{\mathbf{x}} \, \mathrm{d}\mathbf{P}^{\mathbf{y}} \, \mathrm{d}\mathbf{P}^{\mathbf{z}}$ in 6-dimensional phase space, so that the number

density of particles in phase space $\mathfrak{N}$ is given by

$$
\mathbf {N} = \mathcal {N} d \mathbf {x} d \mathbf {y} d z d P ^ {\mathbf {x}} d P ^ {\mathbf {y}} d P ^ {\mathbf {z}}.
$$

Show that $\mathfrak{N}$ is a Lorentz invariant, i.e. that all observers will compute the same numerical value for $\mathfrak{N}$ .

Problem 3.35. A vector field $\mathbf{J}^{\alpha}(\mathbf{x}^{\mu})$ satisfies $\mathbf{J}_{,\alpha}^{\alpha} = 0$ and $\mathbf{J}^{\alpha}$ falls off faster than $\mathbf{r}^{-2}$ at large distances from the origin. (a) Show that $\int \mathbf{J}^{0}\mathrm{d}^{3}\mathbf{x}$ is constant in time. (b) Show that the integral is a scalar, i.e. $\int \mathbf{J}^{0}\mathrm{d}^{3}\mathbf{x} = \int \mathbf{J}^{0}\mathrm{d}^{3}\mathbf{x}^{\prime}$ .

# CHAPTER 4 ELECTROMAGNETISM

The electromagnetic field is described relativistically by the antisymmetric electromagnetic field tensor (Maxwell tensor) $\mathbf{F}^{\mu \nu}$ . In any Lorentz frame the components of $\mathbf{F}^{\mu \nu}$ are related to the electric and magnetic field strengths, $\underline{\mathbf{E}}$ and $\underline{\mathbf{B}}$ , in that frame by

$$
\mathbf {F} ^ {\mu \nu} = \left[ \begin{array}{c c c c} 0 & \mathbf {E} ^ {\mathbf {x}} & \mathbf {E} ^ {\mathbf {y}} & \mathbf {E} ^ {\mathbf {z}} \\ - \mathbf {E} ^ {\mathbf {x}} & 0 & \mathbf {B} ^ {\mathbf {z}} & - \mathbf {B} ^ {\mathbf {y}} \\ - \mathbf {E} ^ {\mathbf {y}} & - \mathbf {B} ^ {\mathbf {z}} & 0 & \mathbf {B} ^ {\mathbf {x}} \\ - \mathbf {E} ^ {\mathbf {z}} & \mathbf {B} ^ {\mathbf {y}} & - \mathbf {B} ^ {\mathbf {x}} & 0 \end{array} \right].
$$

Here $\mu$ is the row index and $\nu$ the column index. Maxwell's equations can be written

$$
\mathrm {F} ^ {\mu \nu} _ {, \nu} = 4 \pi \mathrm {J} ^ {\mu}
$$

$$
\mathbf {F} _ {a} \beta , \gamma + \mathbf {F} _ {\gamma a}, \beta + \mathbf {F} _ {\beta \gamma , a} = 0,
$$

where $\mathbf{J}^{\mu} = (\rho, \mathbf{J})$ is the 4-current density. The Lorentz force law is

$$
\mathrm {d p} ^ {\mu} / \mathrm {d} r = e F ^ {\mu \nu} u _ {\nu}
$$

for a particle of charge e, 4-momentum p and 4-velocity u.

The energy density $\mathfrak{S} = (\mathbf{E}^2 +\mathbf{B}^2) / 8\pi$ , the Poynting energy flux $\underline{\mathbf{S}} = (\underline{\mathbf{E}}\times \underline{\mathbf{B}}) / 4\pi$ , and the 3-dimensional stress-tensor

$$
\mathbf {T} ^ {\mathbf {i j}} = [ - (\mathbf {E} ^ {\mathbf {i}} \mathbf {E} ^ {\mathbf {j}} + \mathbf {B} ^ {\mathbf {i}} \mathbf {B} ^ {\mathbf {j}}) + \frac {1}{2} \delta^ {\mathbf {i j}} (\mathbf {E} ^ {\mathbf {2}} + \mathbf {B} ^ {\mathbf {2}}) ] / 4 \pi
$$

are combined to form the electromagnetic stress-energy tensor

$$
\mathbf {T} ^ {\mu \nu} = (\mathbf {F} _ {\alpha} ^ {\mu \alpha} \mathbf {F} _ {\beta} ^ {\nu} - \frac {1}{4} \eta^ {\mu \nu} \mathbf {F} _ {\alpha} ^ {\alpha \beta} \mathbf {F} _ {\beta}) / 4 \pi .
$$

Problem 4.1. Find the magnetic field $\underline{\mathsf{B}}$ from a current I in an infinitely long straight wire, by appropriate Lorentz transformations and superpositions of the electric field of an infinitely long straight charge distribution.

Problem 4.2. For electric and magnetic fields, show that $\mathbf{B}^2 -\mathbf{E}^2$ and $\underline{\mathbf{E}}\cdot \underline{\mathbf{B}}$ are invariant under changes of coordinates and Lorentz transformations. Are there any invariants which are not merely algebraic combinations of these two?

Problem 4.3. A particular electromagnetic field has its E field at an angle $\theta_0$ to its B field, and $\theta_0$ is invariant to all observers. What is the value of $\theta_0$ ?

Problem 4.4. Show that $\mathfrak{S}^2 - |\underline{\mathbf{S}}|^2$ is a Lorentz invariant of the electromagnetic field, where $\mathfrak{S}$ is the energy density and $\underline{\mathbf{S}}$ the Poynting flux.

Problem 4.5. Prove that except when $(\underline{\mathbf{B}}\cdot \underline{\mathbf{E}})^2 +(\mathbf{B}^2 -\mathbf{E}^2)^2 = 0$ , there is a Lorentz transformation which will make E and B parallel $(\underline{\mathbf{E}}^{\prime}\times \underline{\mathbf{B}}^{\prime} = 0)$ [Hint: Try $\underline{\mathbf{v}} = a(\underline{\mathbf{E}}\times \underline{\mathbf{B}})$ for some $\alpha .]$

Problem 4.6. Suppose that $\underline{\mathbf{E}}\cdot \underline{\mathbf{B}} = 0$ . Show that there is a Lorentz transformation which makes $\underline{\mathbf{E}} = 0$ if $\mathbf{B}^2 -\mathbf{E}^2 >0$ , or one that makes $\underline{\mathbf{B}} = 0$ if $\mathbf{B}^2 -\mathbf{E}^2 < 0$ . What if $\mathbf{B}^2 -\mathbf{E}^2 = 0$ in addition to $\underline{\mathbf{E}}\cdot \underline{\mathbf{B}} = 0$ ?

Problem 4.7. A collection of charged particles of charges $\mathbf{e}_{\mathrm{i}}$ has 3-velocities $\underline{\mathbf{v}}_{\mathrm{i}}$ and trajectories $\underline{\mathbf{x}} = \underline{\mathbf{z}}_{\mathrm{i}}(\mathbf{t})$ . The 4-current has components $\mathbf{J}^{0} = \sum_{\mathrm{i}} \mathbf{e}_{\mathrm{i}} \delta^{3}[\underline{\mathbf{x}} - \underline{\mathbf{z}}_{\mathrm{i}}(\mathbf{t})]$ ; $\mathbf{J}^{\mathrm{i}} = \sum_{\mathrm{k}} \mathbf{e}_{\mathrm{k}} \mathbf{v}^{\mathrm{i}} \delta^{3}[\underline{\mathbf{x}} - \underline{\mathbf{z}}_{\mathrm{k}}(\mathbf{t})]$ . Show that this can be written $\mathbf{J}^{\mu} = \sum_{\mathrm{k}} \int \mathbf{e}_{\mathrm{k}} \delta^{4}[\mathbf{x}^{\alpha} - \mathbf{z}^{\alpha}_{\mathrm{k}}(\tau)] \mathbf{u}_{\mathrm{k}}^{\mu} \, \mathrm{d}\tau$ where $\mathbf{u}_{\mathrm{k}}^{\mu}$ is the 4-velocity of particle $\mathbf{k}$ .

Problem 4.8. Show by explicit examination of components that the

equations

$$
\mathbf {F} _ {\alpha \beta , \gamma} + \mathbf {F} _ {\beta \gamma , \alpha} + \mathbf {F} _ {\gamma \alpha , \beta} = 0 \qquad \mathbf {F} _ {, \beta} ^ {\alpha \beta} = 4 \pi \mathbf {J} ^ {\alpha}
$$

reduce to Maxwell's equations:

$$
\begin{array}{l} \underline {{\nabla}} \cdot \underline {{\mathbf {B}}} = 0, \quad \dot {\underline {{\mathbf {E}}}} + \underline {{\nabla}} \times \underline {{\mathbf {E}}} = 0, \quad \underline {{\nabla}} \cdot \underline {{\mathbf {E}}} = 4 \pi \rho , \\ \underline {{\dot {E}}} - \underline {{\nabla}} \times \underline {{B}} = - 4 \pi \underline {{J}}. \\ \end{array}
$$

Problem 4.9. If $\mathbf{F}^{\mu \nu}$ is the electromagnetic tensor, show that Maxwell's equations in vacuum can be written as $\mathbf{F}_{,\nu}^{\mu \nu} = 0$ and ${\bf *F}^{\mu \nu}_{,\nu} = 0$ . [Here, ${\bf *F}^{\mu \nu}$ is the dual of $\mathbf{F}^{\mu \nu}$ ; see Problem 3.25.]

Problem 4.10. Write out the $\mu = 0$ component of the Lorentz force equation $\mathrm{du}^{\mu} / \mathrm{d}\tau = (\mathrm{e} / \mathrm{m})\mathrm{F}^{\mu \beta}\mathrm{u}_{\beta}$ expressing $\mathbf{F}^{\mu \nu}$ in terms of $\mathbf{E}_i$ and $\mathbf{B}_i$ , to obtain

$$
\mathrm {d P} ^ {0} / \mathrm {d t} = \underset {\sim} {\mathrm {e}} \underset {\sim} {\mathrm {v}} \cdot \underset {\sim} {\mathrm {E}}.
$$

Problem 4.11. From the spatial components of the Lorentz 4-force equation, find an equation for $\underline{\mathrm{dP}}/\mathrm{dt}$ in terms of $\underline{\mathbf{E}}$ and $\underline{\mathbf{B}}$ . (Here $\underline{\mathbf{P}}$ is the spatial part of $\mathbf{P}$ ).

Problem 4.12. A particle of charge $\mathbf{q}$ and mass $m$ is coasting through the lab with velocity $v_{\underline{\mathbf{x}}}$ when it encounters a constant $\underline{\mathbf{E}}$ field in the $y$ -direction. Find $y(x)$ , the shape of the particle's subsequent motion.

Problem 4.13. A particle of charge $q$ , mass $m$ , moves in a circular orbit of radius $R$ in a uniform B field $\mathbf{B}_{\underline{\mathbf{e}}_z}$ . (a) Find B in terms of R, q, m and $\omega$ , the angular frequency. (b) The speed of the particle is constant since the B field can do no work on the particle. An observer moving at velocity $\beta_{\underline{\mathbf{e}}_{\mathbf{x}}}$ , however, does not see the speed as constant. What is $\mathfrak{u}^{0^{'}}$ measured by this observer? (c) Calculate $\mathrm{du}^{0^{'}} / \mathrm{dr}$ and thus $\mathrm{dP}^{0^{'}} / \mathrm{d}\tau$ . Explain how the energy of the particle can change since the B field does no work on it.

Problem 4.14. A small test particle (mass $m$ , positive charge $q$ ) makes circular orbits around a "fixed" (i.e. very massive) body of positive charge $Q$ . A uniform magnetic field $\underline{B}$ perpendicular to the orbital plane serves to keep the particle in orbit. In the inertial frame in which the central body is at rest, the test charge is seen to circle in the plane perpendicular to the $B$ field with an angular frequency $\omega$ . What is the charge to mass ratio of the test particle in terms of $\omega$ , $R$ , $B$ , $Q$ ?

Problem 4.15. Show that the stress-energy tensor for the electromagnetic field is divergenceless (i.e. $\mathbf{T}^{\mu \nu}_{,\nu} = 0$ ) in the absence of charge sources.

Problem 4.16. Show that the stress-energy tensor for the electromagnetic field has zero trace.

Problem 4.17. If $\mathbf{T}^{\mu \nu}$ is the stress-energy tensor of the electromagnetic field, show that

$$
\mathbf {T} _ {\alpha} ^ {\mu} \mathbf {T} _ {\nu} ^ {a} = \delta_ {\nu} ^ {\mu} \left[ \left(\mathbf {E} ^ {2} - \mathbf {B} ^ {2}\right) ^ {2} + \left(2 \underline {{\mathbf {E}}} \cdot \underline {{\mathbf {B}}}\right) ^ {2} \right] / (8 \pi) ^ {2}.
$$

Problem 4.18. Write Ohm's law $\underline{\mathbf{J}} = \sigma \underline{\mathbf{E}}$ invariantly in terms of $\mathbf{J}^{\mu}$ , $\mathbf{F}^{\mu \nu}$ , $\sigma$ and $\mathfrak{u}^{\mu}$ (the 4-velocity of the conducting element).

Problem 4.19. Derive the Lorentz force law for a charged particle from the action $\int \mathrm{J}^{\mu}\mathrm{A}_{\mu}\mathrm{d}^{4}\mathbf{x} - \mathfrak{m}\int \mathrm{d}\tau$ , where $\mathrm{J}^{\mu}$ is the 4-current, $\mathrm{A}_{\mu}$ the vector potential, and $\mathrm{d}\tau^{2} \equiv -\eta_{\alpha \beta}\mathrm{d}\mathbf{x}^{\alpha}\mathrm{d}\mathbf{x}^{\beta}$ .

Problem 4.20.

(a) Show that $\underline{\mathbf{E}}\rightarrow -\underline{\mathbf{B}}$ and $\underline{\mathbf{B}}\rightarrow \underline{\mathbf{E}}$ under the "duality transformation" $\mathbf{F}\to *\mathbf{F}$   
(b) Show that if $\mathbf{F}$ is a solution of the free-space Maxwell equations, so is $*\mathbf{F}$ and also $\mathbf{e}^{*a}\mathbf{F} \equiv \mathbf{F} \cos \alpha + * \mathbf{F} \sin \alpha$ for arbitrary $a$ . ( $\mathbf{F} \rightarrow \mathbf{e}^{*a}\mathbf{F}$ is called a “duality rotation”).

Problem 4.21. If one believes that esthetics should be an important consideration in physical laws, then by symmetry Maxwell's laws should read

$$
\begin{array}{l} \mathbf {F} _ {, \nu} ^ {\mu \nu} = 4 \pi \mathrm {J} ^ {\mu} \\ * \mathrm {F} _ {, \nu} ^ {\mu \nu} = 4 \pi \mathrm {K} ^ {\mu}. \\ \end{array}
$$

What would the significance of $\mathbf{K}$ be?

Problem 4.22. In Minkowski spacetime, there is an electromagnetic current $\mathbf{J}^{\mu}(\mathbf{x}^{\nu})$ . Show that the solution to Maxwell's equation is

$$
\mathrm {F} ^ {\mu \nu} (\mathrm {x} ^ {\alpha}) = \frac {4}{\pi \mathrm {i}} \int \frac {\mathrm {r} ^ {[ \mu ]} \mathrm {J} ^ {\nu ]} \mathrm {d} ^ {4} \tilde {\mathrm {x}}}{(\mathrm {r} _ {\sigma} \mathrm {r} ^ {\sigma}) ^ {2}}
$$

where $\mathbf{r}^{\beta} \equiv \tilde{\mathbf{x}}^{\beta} - \mathbf{x}^{\beta}$ . (Start by finding a Green's function of $\square \mathbf{A}^{\mu} = -4\pi \mathbf{J}^{\mu}$ .) How are the retarded boundary conditions specified?

Problem 4.23. Find the equation for the convective time rate of change of a magnetic field which is "frozen in" a perfectly conducting fluid, in terms of the expansion, shear, and rotation of the fluid. (See Problem 5.18 for definitions of these quantities.)

# CHAPTER 5 MATTER AND RADIATION

A proper description of the energy, momentum and stress of a relativistic fluid or field uses the symmetric tensor $\mathbf{T}$ , the stress-energy tensor (also called the energy-momentum tensor). The components of this tensor in the Lorentz frame of an observer are related to the measurements made by that observer in the following way:

$\mathbf{T}^{00} \equiv$ density of mass-energy (often denoted $\rho$ ).

$\mathbf{T}^{0j} = \mathbf{T}^{j0} \equiv j$ -component of momentum-density   
= j-component of energy-flux

$\mathbf{T}^{\mathrm{ij}} \equiv$ components of the ordinary stress tensor (e.g. $\mathbf{T}^{\mathbf{x}\mathbf{x}} = \mathbf{x}$ -component of pressure).

If $\mathbf{T}^{\mu \nu}$ describes all fields, fluids, particles etc. present in a system, the interrelation of momentum flow and energy change is summarized by the equations of motion:

$$
\mathrm {T} _ {, \nu} ^ {\mu \nu} = 0.
$$

The basic concepts of relativistic thermodynamics and hydrodynamics which follow from this are developed in the problems.

With a view to developments later in the book, several problems in this chapter use covariant differentiation, denoted by a semicolon. The reader not yet familiar with this may replace all semicolons by commas (partial differentiation in Minkowski coordinates). Also, the $\nabla$ notation is introduced; e.g. $\nabla \mathbf{S}$ for $\mathbf{S}_{; \beta}^{a}, \nabla \mathbf{f}$ for $\mathbf{f}_{, a}, \nabla \cdot \mathbf{T}$ for $\mathbf{T}_{; \nu}^{\mu \nu}$ , etc.

Problem 5.1. Calculate the nonzero components in an inertial frame S of the stress-energy tensor for the following systems:

(a) A group of particles all moving with the same velocity $\underline{\beta} = \beta \underline{e}_{\mathbf{x}}$ as seen in S. Let the rest-mass density of these particles be $\rho_0$ as measured in their comoving frame. Assume a high density of particles and treat them in the continuum approximation.

(b) A ring of $\mathbf{N}$ similar particles of mass $m$ rotating counterclockwise in the $x-y$ plane about some point fixed in $S$ at a radius $a$ and angular velocity $\omega$ . (The width of the ring is much less than $a$ .) Do not include the stress-energy of whatever forces keep them in orbit. Assume $\mathbf{N}$ is large enough that one can treat the particles as being continuously distributed.

(c) Two such rings of particles, one rotating clockwise, the other counter-clockwise, at the same radius a. The particles do not collide or interact with each other in any way.

Problem 5.2. What is the stress energy of a gas with a proper number density (i.e. number density as measured in the local rest frame of the gas) $\mathbf{N}$ of noninteracting particles of mass $m$ , if the particles all have the same speed $v$ but move isotropically? (Do not assume $v << c$ .)

Problem 5.3. In the rest frame of a perfect fluid its stress energy tensor, in terms of mass-energy density $\rho$ and pressure $\mathfrak{p}$ , is the diagonal tensor

$$
\mathbf {T} ^ {\mu \nu} = \left[ \begin{array}{c c c c} \rho & & & 0 \\ & \text {p} & & \\ & & \text {p} & \\ 0 & & & \text {p} \end{array} \right].
$$

If a fluid element of proper density and pressure, $\rho$ and $\mathfrak{p}$ is moving with 4-velocity $\mathbf{u}$ , what is its stress-energy?

Problem 5.4. Find the stress-energy tensor for a uniform magnetic field. What is the average stress-energy if the B field is static but "chaotic" i.e. the direction of the B field varies, and is isotropic on the average?

Problem 5.5. A rod has cross sectional area A and mass per unit length $\mu$ . Write down the stress-energy tensor inside the rod when the rod is under a tension F. (Assume that the tension is uniformly distributed over the cross section.)

Problem 5.6. A rope of mass per unit length $\mu$ has a static breaking strength $F$ . What is the maximum $F$ can be without violating the "weak" energy condition that $T^{00}$ should be positive to all observers? How close is steel cable to this theoretical maximum strength?

Problem 5.7. An infinitesimally thin rod of length $2a$ has a point mass $m$ at each of its ends. The center of the rod is fixed in the laboratory and the rod rotates about this point with a relativistic angular velocity $\omega$ . (i.e. $\omega \ell$ is comparable with $c$ ). Assume the rod is massless. What is $\mathbf{T}^{\mu \nu}$ for the rod and particle system?

Problem 5.8. A parallel plate capacitor consists of two large plates of area A, perpendicular to the x-direction, separated by a small distance d. The capacitor is charged so that a uniform electric field of magnitude E is present between the plates; fringe effects at the edge of the plate can be neglected. The "electrostatic mass" of this capacitor is $\mathrm{E}^2\mathrm{Ad} / 8\pi$ in the rest frame of the capacitor. Show that the electrostatic energy is smaller if the capacitor is moving in the x-direction! Consider now that the plates must be held apart. Let the plates be held apart by an ideal gas of proper density $\rho_0$ . Show that the total energy (electrostatic + gas) of the capacitor increases with velocity in the x-direction in precisely the same manner that the energy of a point mass does.

Problem 5.9. Consider a system of discrete particles of charge $\mathbf{q}_{\mathbf{i}}$ and mass $\mathfrak{m}_{\mathbf{i}}$ interacting through electromagnetic forces. From the explicit expression for $\mathrm{T}^{\mu \nu}$ of the particles show that the total $\mathrm{T}^{\mu \nu}$ (particles plus field) is conserved, i.e. that $\mathrm{T}^{\mu \nu}_{,\nu} = 0$ .

Problem 5.10. The specific intensity $\mathbf{I}_{\nu}$ of radiation measures the intensity of radiation at a particular frequency $\nu$ in a particular direction. It is defined as the flux per unit frequency interval, per unit solid angle. Show that $\mathbf{I}_{\nu} / \nu^{3}$ is a Lorentz invariant.

Problem 5.11. A star emits radiation isotropically in its own rest frame, with luminosity $\mathbf{L}$ (energy per unit time). At a particular instant, as measured from the earth, the star is at a distance $\mathbf{R}$ , and is moving with a velocity $\mathbf{v}$ which makes an angle $\theta$ with respect to the direction from the earth to the star. What is the flux of radiation (energy per unit time per unit area) seen by an observer on the earth in terms of $\mathbf{R}$ , $\mathbf{v}$ and $\theta$ evaluated at the instant the radiation was emitted?

Problem 5.12. Consider a spherical particle of mass $m$ which scatters all electromagnetic radiation incident on it, isotropically in its rest frame. Let $A$ be the effective cross sectional area of the particle. Find the equation of motion of the particle in a constant radiation field of intensity $S$ (energy per time per area), and solve it for the case of a particle initially at rest. (Poynting-Robertson effect).

Problem 5.13. A thermally-conducting black sphere with a thermometer attached moves with velocity $\mathbf{v}$ through a black body radiation field of temperature $\mathbf{T}_0$ . What does the thermometer read?

Problem 5.14. In an electron gas of temperature $\mathrm{T} < \mathrm{m_e c^2 / k}$ a photon of energy $\mathbf{E} < \mathbf{m_e c^2}$ undergoes collisions and is Compton scattered. Show that, to lowest order in $\mathbf{E}$ and $\mathbf{T}$ the average energy lost by a photon in a collision is

$$
<   \Delta E > = (E / m _ {e} c ^ {2}) (E - 4 k T).
$$

Problem 5.15. Show that in special relativity the stress-energy of an isolated physical system of finite extent obeys the tensor virial theorem

$$
\int \mathrm {T} ^ {\mathrm {i j}} \mathrm {d} ^ {3} \mathbf {x} = \frac {1}{2} \frac {\mathrm {d} ^ {2}}{\mathrm {d t} ^ {2}} \int \mathrm {T} ^ {0 0} \mathbf {x} ^ {\mathrm {i}} \mathbf {x} ^ {\mathrm {j}} \mathrm {d} ^ {3} \mathbf {x}.
$$

Problem 5.16. Show that the stress-energy tensor $\mathbf{T}^{\mu \nu}$ has a timelike eigenvector if and only if there is a physical observer who sees no net energy flux in any direction. What is the significance of the eigenvalue?

# Problem 5.17.

(a) Consider a stressed medium which moves through a particular inertial frame with velocity $|\underline{\mathbf{v}}| << 1$ . Show that to first order in the velocity, the spatial components of the momentum density are

$$
\mathbf {g} ^ {\mathbf {j}} = \mathbf {m} ^ {\mathbf {j k}} \mathbf {v} ^ {\mathbf {k}},
$$

where $\mathfrak{m}^{\mathrm{jk}}$ , the "inertial mass per unit volume" is

$$
\mathbf {m} ^ {\mathrm {j k}} = \mathbf {T} ^ {0 ^ {\prime} 0 ^ {\prime}} \delta^ {\mathrm {j k}} + \mathbf {T} ^ {\mathrm {j ^ {'} k ^ {'}}}
$$

in terms of $\mathbf{T}^{\mu^{\prime}\nu^{\prime}}$ , the components of the stress-energy in the rest frame of the medium. What is $\mathbf{m}^{\mathrm{jk}}$ for a perfect fluid?

(b) Consider an isolated, stressed body at rest and in equilibrium $(\mathbf{T}^{\alpha \beta},_0 = 0)$ in the laboratory frame. Show that its total inertial mass,

defined by

$$
\mathbf {M} ^ {\mathrm {i j}} \equiv \int_ {\substack {\text {stressed} \\ \text {body}}} \mathbf {m} ^ {\mathrm {i j}} \mathrm {d x} \mathrm {d y} \mathrm {d z}
$$

is isotropic and equals the rest mass of the body, i.e. show that

$$
\mathbf {M} ^ {\mathrm {i j}} = \delta^ {\mathrm {i j}} \int \mathbf {T} ^ {0 0} d x d y d z.
$$

Problem 5.18. If $\mathbf{u}$ is the 4-velocity of a fluid show that $\nabla \mathbf{u}$ can be decomposed as

$$
\mathsf {u} _ {\alpha ; \beta} = \omega_ {\alpha \beta} + \sigma_ {\alpha \beta} + \frac {1}{3} \theta \mathsf {P} _ {\alpha \beta} - \mathsf {a} _ {\alpha} \mathsf {u} _ {\beta},
$$

where $\mathbf{a}$ is the "4-acceleration" of the fluid

$$
\mathbf {a} _ {\alpha} \equiv \mathbf {u} _ {\alpha ; \beta} \mathbf {u} ^ {\beta} ,
$$

$\theta$ is the "expansion" of the fluid world lines

$$
\theta \equiv \nabla \cdot \mathbf {u} = \mathrm {u} _ {; \alpha} ^ {\alpha},
$$

$\omega_{\alpha \beta}$ is the “rotation 2-form” of the fluid, and $\sigma_{\alpha \beta}$ is the “shear tensor”

$$
\omega_ {\alpha \beta} \equiv \frac {1}{2} \left(\mathrm {u} _ {\alpha ; \mu} \mathrm {P} ^ {\mu} _ {\beta} - \mathrm {u} _ {\beta ; \mu} \mathrm {P} ^ {\mu} _ {\alpha}\right),
$$

$$
\sigma_ {\alpha} \beta \equiv \frac {1}{2} \left(\mathrm {u} _ {\alpha ; \mu} \mathrm {P} ^ {\mu} _ {\beta} + \mathrm {u} _ {\beta ; \mu} \mathrm {P} ^ {\mu} _ {\alpha}\right) - \frac {1}{3} \theta \mathrm {P} _ {\alpha} \beta .
$$

Here $\mathbf{P}$ is the projection tensor

$$
\mathbf {P} _ {\alpha \beta} \equiv \mathbf {g} _ {\alpha \beta} + \mathbf {u} _ {\alpha} \mathbf {u} _ {\beta}
$$

which projects a vector onto the 3-surface perpendicular to $\mathbf{u}$ .

Problem 5.19. Write the first law of thermodynamics for a relativistic fluid. (i.e. Write the law of conservation of mass-energy for a fluid element.)

Problem 5.20. Use the equations of motion $(\mathbf{T}^{\mu \nu}; \nu = 0)$ to show that the flow of a perfect fluid is isentropic.

Problem 5.21. For a perfect fluid with equation of state $\rho = \rho (\mathfrak{n})$ (where $\mathfrak{n} =$ baryon density) show that $\mathbf{T}_{\mu}^{\mu}$ , the trace of the stress-energy tensor is negative if and only if

$$
d \log \rho / d \log n <   4 / 3.
$$

Problem 5.22. Show that the velocity of sound $\mathbf{v}_{\mathbf{s}}$ in a relativistic perfect fluid is given by

$$
v _ {s} ^ {2} = \left. \partial p / \partial \rho \right| _ {s = c o n s t a n t}.
$$

For a high temperature relativistic gas with an equation of state $\rho \approx 3\mathrm{P}$ (essentially that for a photon gas) show that $\mathbf{v}_{\mathrm{s}} \approx 1 / \sqrt{3}$ .

Problem 5.23. The velocity of sound in a fluid is $\left.\mathbf{v}_{\mathbf{s}}^{2} = \frac{\partial \mathbf{p}}{\partial \rho}\right|_{\mathbf{s}} = \text{constant}$ . Show that $\mathbf{v}_{\mathbf{s}}^{2} = \Gamma_{1} \mathbf{p} / (\rho + \mathbf{p})$ where $\Gamma_{1}$ is the adiabatic index

$$
\Gamma_ {1} = \partial \log p / \partial \log n | _ {s = c o n s t a n t}.
$$

Problem 5.24. What is the speed of sound in an ideal Fermi gas at zero temperature?

Problem 5.25. A relativistic wind tunnel is to be fed from a tank of perfect adiabatic compressed gas. Suppose the gas has an equation of state $p \propto n^{\gamma}$ with $\gamma$ constant, and the speed of sound in the tank is $a$ . What is the largest wind velocity $v_{\max}$ which can be obtained? (No gravitational forces; isentropic flow.)

Problem 5.26. An idealized description of heat flow in a fluid uses the heat flux 4-vector $\mathbf{q}$ with components in the fluid rest frame $\mathbf{q}^0 = 0$ , $\mathbf{q}^j = (\text{energy per unit time crossing a unit surface perpendicular to } \mathbf{e}_j, \text{ in the positive } j$ direction). What is the stress-energy tensor associated with the heat flow?

Problem 5.27. Let $s$ , $n$ and $q$ be respectively entropy per baryon, number density of baryons, and heat flux, all measured in the proper frame of the fluid. In this proper frame $q$ is purely spatial. Let $S$ be the entropy density-flux 4-vector. Show that

$$
\mathbf {S} = \mathbf {n s u} + \mathbf {q} / \mathbf {T},
$$

where $\mathbf{u}$ is the 4-velocity of the fluid rest frame.

Problem 5.28. A fluid is "perfect" except for admitting some heat conduction, described by a heat flow 4-vector $\mathbf{q}$ . Calculate the local rate of entropy generation $\nabla \cdot \mathbf{S}$ .

Problem 5.29. In a uniformly accelerating system, show that the condition for thermal equilibrium is not $\mathbf{T} = \text{constant} = \mathbf{T}_0$ but rather is

$$
\mathrm {T} = \mathrm {T} _ {0} \exp (- \underline {{\mathbf {a}}} \cdot \underline {{\mathbf {x}}})
$$

where $\underline{\mathbf{x}}$ is coordinate position in the accelerating frame.

Problem 5.30. The stress energy tensor of a viscous fluid is

$$
\mathbf {T} ^ {\alpha \beta} = \rho \mathbf {u} ^ {\alpha} \mathbf {u} ^ {\beta} + \mathrm {p P} ^ {\alpha \beta} - 2 \eta \sigma^ {\alpha \beta} - \zeta \theta \mathbf {P} ^ {\alpha \beta}.
$$

Here $\eta$ and $\zeta$ are respectively the coefficients of shear and bulk viscosity. The definitions of $\sigma^{\alpha\beta}$ , $\theta$ , $\mathbb{P}^{\alpha\beta}$ are those of Problem 5.18. The pressure and density are $p$ and $\rho$ . Show that the viscous terms lead to the production of entropy at a rate

$$
\mathrm {S} _ {; \alpha} ^ {\alpha} = (\zeta \theta^ {2} + 2 \eta \sigma_ {\alpha \beta} \sigma^ {\alpha \beta}) / \mathrm {T}
$$

where $\mathbf{T}$ is the temperature of the fluid. (Hint: First show that $\mathbf{S}_{;a}^{a} = [\mathrm{d}\rho /\mathrm{d}\tau +\theta (\rho +\mathfrak{p})] / \mathbf{T}$ for a fluid without heat flow, then differentiate $\rho \mathbf{u}^{\beta} = -\mathbf{T}^{a\beta}\mathbf{u}_a$ to get $\mathrm{d}\rho /\mathrm{d}\tau .)$

Problem 5.31. From the stress-energy

$$
\mathbf {T} ^ {\alpha \beta} = \rho \mathbf {u} ^ {\alpha} \mathbf {u} ^ {\beta} + \mathrm {p P} ^ {\alpha \beta} - 2 \eta \sigma^ {\alpha \beta} - \zeta \theta \mathbf {P} ^ {\alpha \beta},
$$

show that the equations of motion derived from $\mathbf{T}^{\alpha \beta},\beta = 0$ reduce to the Navier-Stokes equations in the nonrelativistic limit.

Problem 5.32. As in non-relativistic thermodynamics, one defines the specific heat of a gas at constant volume and constant pressure by

$$
\mathbf {c _ {v}} = \mathrm {T} \left. \frac {\mathrm {d s}}{\mathrm {d T}} \right| _ {\mathbf {n}} \qquad \mathbf {c _ {p}} = \mathrm {T} \left. \frac {\mathrm {d s}}{\mathrm {d T}} \right| _ {\mathbf {p}} .
$$

For a perfect Maxwell-Boltzmann gas, show that $c_{\mathbf{p}} = c_{\mathbf{v}} + \mathbf{k}$ . (Here $\mathbf{k} =$ Boltzmann's constant.) Show that the adiabatic index

$$
\Gamma_ {1} \equiv \frac {\partial \log p}{\partial \log n} | _ {s}
$$

is equal to the ratio of specific heats,

$$
\gamma \equiv c _ {\mathbf {p}} / c _ {\mathbf {v}}.
$$

Problem 5.33. For a perfect Maxwell-Boltzmann gas, show that if $\gamma$ is approximately constant in some regime of interest, then $p = Kn^{\gamma}$ and $\rho = mn + Kn^{\gamma} / (\gamma - 1)$ under adiabatic conditions. (K = constant, m = mass of particles.)

Problem 5.34. The invariant equilibrium distribution function of a relativistic gas is (25-1) $\frac{1}{4}$ .

$$
\mathcal {N} \left(\mathrm {p} ^ {\alpha}, \mathrm {x} ^ {\alpha}\right) \equiv \frac {\mathrm {d N}}{\mathrm {d} ^ {3} \mathrm {x d} ^ {3} \mathrm {P}} = \frac {(2 \mathrm {J} + 1) / \mathrm {h} ^ {3}}{\exp \left[ - \frac {\mathrm {P} \cdot \mathrm {u}}{\mathrm {k T}} - \theta \right] - \varepsilon}.
$$

Here $\mathbf{J} =$ spin of particles, $\mathbf{h} =$ Planck's constant, $\mathbf{u} =$ mean 4-velocity of gas, $\varepsilon = 1,0$ or $-1$ for Bose-Einstein, Maxwell-Boltzmann or Fermi-Dirac statistics respectively. The parameter $\theta$ is independent of $\mathbf{P}$ . The first two moments of $\mathfrak{N}$ are

$$
\mathrm {J} ^ {\mu} \equiv \int \mathcal {N} \mathrm {P} ^ {\mu} \frac {\mathrm {d} ^ {3} \mathrm {P}}{(- \mathrm {P} \cdot \mathrm {u})}, \qquad \mathrm {T} ^ {\mu \nu} \equiv \int \mathcal {N} \mathrm {P} ^ {\mu} \mathrm {P} ^ {\nu} \frac {\mathrm {d} ^ {3} \mathrm {P}}{(- \mathrm {P} \cdot \mathrm {u})}.
$$

Since $\mathbf{u}$ is the only free vector, these integrals must have the form

$$
J ^ {\mu} = n u ^ {\mu}, \quad T ^ {\mu \nu} = (\rho + p) u ^ {\mu} u ^ {\nu} + p g ^ {\mu \nu}.
$$

(This is the kinetic-theory definition of $\mathfrak{n},\rho ,\mathfrak{p}$ .)

(a) Obtain 1-dimensional integrals for $n$ , $\rho$ and $p$ .   
(b) Show that $\mathrm{dp} = (\rho +\mathfrak{p}) / \mathrm{T}\mathrm{d}\mathrm{T} + \mathrm{nkT}\mathrm{d}\theta .$   
(c) Use the first law of thermodynamics to identify $\mathrm{kT}\theta$ as the chemical potential $\mu = (\rho +\mathfrak{p}) / \mathfrak{n} - \mathfrak{T}\mathfrak{s}$ .   
(d) Show that for a Maxwell-Boltzmann gas, $p = nkT$ for all $T$ .   
(e) Show that for a Maxwell-Boltzmann gas, $\rho = n(m + \frac{3}{2} kT)$ is an approximation valid only for $kT << m$ . Find the exact expression for $\rho / n$ . What is $\rho / n$ for $kT >> m$ ? (Here $m$ is the mass of a gas particle.)

Problem 5.35. For a perfect Maxwell-Boltzmann gas, find $\gamma(T)$ , the ratio of specific heats, as a function of temperature.

# CHAPTER 6

# METRICS

Metric geometry, geometry specified by a distance formula $\mathrm{ds}^2 = \mathbf{g}_{a\beta}\mathrm{dx}^a\mathrm{dx}^\beta$ , is the foundation for general relativity and for most of the remaining chapters in this book. The most important metric is of course a spacetime metric, formally a metric which can locally be transformed to the Minkowski metric, i.e. for every point $\mathbf{P}$ in the spacetime, there is some coordinate transformation which makes $\mathbf{g}_{a\beta} = \eta_{a\beta}$ at $\mathbf{P}$ .

0 0 0 0 0 0 0 0

Problem 6.1.

(a) Prove that the 2-dimensional metric space described by

$$
\mathrm {d s} ^ {2} = \mathrm {d v} ^ {2} - \mathrm {v} ^ {2} \mathrm {d u} ^ {2} \tag {1}
$$

is just the flat 2-dimensional Minkowski space usually described by

$$
\mathrm {d s} ^ {2} = \mathrm {d x} ^ {2} - \mathrm {d t} ^ {2}. \tag {2}
$$

Do this by finding the coordinate transformations $\mathbf{x}(\mathbf{v},\mathbf{u})$ and $\mathbf{t}(\mathbf{v},\mathbf{u})$ which take the metric (2) into the form (1).

(b) For an unaccelerated particle, show that the component of the 4-momentum $\mathbf{P_u}$ is constant, but that $\mathbf{P_v}$ is not.

Problem 6.2. Show that the line element

$$
\mathrm {d s} ^ {2} = \mathsf {R} ^ {2} [ \mathrm {d} a ^ {2} + \sin^ {2} \alpha (\mathrm {d} \dot {\theta} ^ {2} + \sin^ {2} \theta \mathrm {d} \phi^ {2}) ]
$$

represents a hypersphere of radius $\mathbf{R}$ in Euclidean 4-space, i.e. a locus of points a distance $\mathbf{R}$ from a given point.

Problem 6.3. The metric for the surface of a globe of the Earth is

$$
\mathrm {d s} ^ {2} = \mathrm {a} ^ {2} (\mathrm {d} \lambda^ {2} + \cos^ {2} \lambda \mathrm {d} \phi^ {2})
$$

where $\lambda$ is the latitude and $\phi$ is the longitude. The metric of a flat map of the world, with Cartesian coordinates $x$ and $y$ is $\mathrm{ds}^2 = \mathrm{dx}^2 + \mathrm{dy}^2$ ; however we are not interested in this geometry, but in that of the globe it represents. What is the metric of the globe expressed in $x$ and $y$ coordinates for (a) a cylindrical projection, and (b) a stereographic projection map of the world?

Problem 6.4. Mercator's projection is defined as follows: The map coordinates are rectangular Cartesian coordinates $(x, y)$ such that a straight line on the map is a line of constant compass bearing on the globe.

(a) Show that the map is defined by $\mathbf{x} = \phi$ , $\mathbf{y} = \log \cot \frac{1}{2}\theta$ , where $(\theta, \phi)$ are the polar coordinates of a point on the globe.

(b) What is the metric of the globe in $(\mathbf{x},\mathbf{y})$ coordinates?

(c) Show that the great circles are given by $\sinh y = a\sin (x + \beta)$ (except for the special cases $y = 0$ or $x =$ constant).

Problem 6.5. A space purports to be 3-dimensional, with coordinates $x, y, z$ and the metric

$$
\mathrm {d s} ^ {2} = \mathrm {d x} ^ {2} + \mathrm {d y} ^ {2} + \mathrm {d z} ^ {2} - \left(\frac {3}{1 3} \mathrm {d x} + \frac {4}{1 3} \mathrm {d y} + \frac {1 2}{1 3} \mathrm {d z}\right) ^ {2}.
$$

Show that it is really a two-dimensional space, and find two new coordinates $\zeta$ and $\eta$ for which the line element takes the form

$$
\mathrm {d s} ^ {2} = \mathrm {d} \zeta^ {2} + \mathrm {d} \eta^ {2}.
$$

Problem 6.6. Show that a contraction of a vector $\mathbf{V}$ with the “projection tensor” $\mathbf{P} \equiv \mathbf{g} + \mathbf{u} \otimes \mathbf{u}$ projects $\mathbf{V}$ into the 3-surface orthogonal to the 4-velocity vector $\mathbf{u}$ . If $\mathbf{n}$ is a unit spacelike vector show that

$$
\mathbf {P} \equiv \mathbf {g} - \mathbf {n} \otimes \mathbf {n}
$$

is the corresponding projection operator. Show that there is no unique projection operator orthogonal to a null vector.

Problem 6.7. Show that a conformal transformation of a metric, i.e. $\mathbf{g}_{\alpha}\beta \rightarrow \mathbf{f}(\mathbf{x}^{\mu})\mathbf{g}_{\alpha}\beta$ for an arbitrary function $f$ , preserves all angles. (Figure out how to define angles!) Show that all null curves remain null curves.

Problem 6.8. One can put a metric on the velocity space of a particle by defining the distance between two nearby velocities as their relative velocity. Show that the metric can be written in the form

$$
\mathrm {d s} ^ {2} = \mathrm {d} \chi^ {2} + \sinh^ {2} \chi (\mathrm {d} \theta^ {2} + \sin^ {2} \theta \mathrm {d} \phi^ {2}).
$$

where the magnitude of the velocity is $\mathbf{v} = \tanh \chi$ .

Problem 6.9. A manifold which has the topology of a 2-sphere has - in a neighborhood of $\theta = \frac{1}{2}$ , $\chi = 0$ - the metric

$$
\mathrm {d s} ^ {2} = \mathrm {d} \theta^ {2} + (\theta - \theta^ {3}) ^ {2} \mathrm {d} \chi^ {2}.
$$

The manifold has precisely one point which is not locally flat, and that point is a “conical” singularity. Show that there are two different maximal analytic extensions of the metric, i.e. that there are two different ways of extending the metric, and satisfying the condition that there is only one conical singularity. Note that this shows that a metric in a local coordinate patch does not always pin down the global nature of the manifold. (Hint: consider the periodicity of the $\chi$ coordinate.)

Problem 6.10. Find the most general form for a spacetime metric that is (spatially) spherically symmetric.

# CHAPTER 7

# COVARIANT DIFFERENTIATION AND GEODESIC CURVES

The partial derivatives of a vector or tensor with respect to the coordinates of a space (e.g. $\mathbf{A}_{,\nu}^{\mu}$ or $\mathbf{Q}^{\alpha \beta \dots}{}_{\gamma \delta \dots ,\nu}$ ) are not themselves components of a tensor. Rather, the curvilinearity of the coordinates (optional in flat space, but inevitable in a curved space) must be taken into account, leading to the idea of covariant differentiation.

The tensor formed by differentiating a tensor $\mathbf{Q}$ with components $\mathbf{Q}^{\alpha \beta \dots} \gamma \delta \dots$ is denoted $\nabla \mathbf{Q}$ and has components denoted

$$
\begin{array}{l} \mathrm {Q} ^ {\alpha \beta \dots} _ {\gamma \delta \dots ; \sigma} \equiv \mathrm {Q} ^ {\alpha \beta \dots} _ {\gamma \delta \dots , \sigma} + \Gamma^ {\alpha} _ {\nu \sigma} \mathrm {Q} ^ {\nu \beta \dots} _ {\gamma \delta \dots} \\ + \Gamma^ {\beta} _ {\nu \sigma} Q ^ {a \nu \dots} _ {\gamma \delta \dots} + \dots - \Gamma^ {\nu} _ {\gamma \sigma} Q ^ {a \beta \dots} _ {\nu \delta \dots} \\ - \Gamma^ {\nu} _ {\delta \sigma} \mathrm {Q} ^ {\alpha \beta \dots} _ {\gamma \nu \dots} \\ \end{array}
$$

where there is one “correction” term for every index of $\mathbf{Q}$ . The $\Gamma$ 's are called Christoffel symbols or [affine] connection coefficients. In a basis they are related to the partial derivatives of the metric by

$$
\Gamma_ {\beta \gamma} ^ {a} = \mathbf {g} ^ {a \mu} \Gamma_ {\mu \beta \gamma} = \frac {1}{2} \mathbf {g} ^ {a \mu} (\mathbf {g} _ {\mu \beta , \gamma} + \mathbf {g} _ {\mu \gamma , \beta} - \mathbf {g} _ {\beta \gamma , \mu})
$$

(the first equality defines $\Gamma_{\mu \beta \gamma}$ ). The $\Gamma$ 's are sets of numbers, but they are not components of a tensor. (They do not transform like a tensor.)

A covariant derivative which is dotted into a vector is called a directional derivative:

$$
(\nabla \mathbf {Q}) \cdot \mathbf {u} \equiv \nabla_ {\mathbf {u}} \mathbf {Q} \equiv Q ^ {\alpha \beta \dots} _ {\gamma \delta \dots ; \nu} \mathbf {u} ^ {\nu}  .
$$

If the vector $\mathbf{u}$ is tangent to a curve parameterized by $\lambda$ , one sometimes writes $\mathbf{u} = \mathrm{d} / \mathrm{d}\lambda$ for $\mathbf{u}^{\alpha} = \mathrm{d}\mathbf{x}^{\alpha} / \mathrm{d}\lambda$ and

$$
\nabla_ {\mathbf {u}} \mathbf {Q} \equiv \frac {\mathrm {D} \mathbf {Q}}{\mathrm {d} \lambda}.
$$

If the vector happens to be a basis vector, one writes

$$
\nabla_ {\mathbf {e} _ {a}} \mathbf {Q} \equiv \nabla_ {a} \mathbf {Q}.
$$

In terms of the basis vectors, the connection coefficients can be written

$$
\nabla_ {\beta} \mathbf {e} _ {\alpha} = \Gamma_ {\alpha \beta} ^ {\mu} \mathbf {e} _ {\mu} \quad \text {o r} \quad \Gamma_ {\mu a \beta} = \mathbf {e} _ {\mu} \cdot \nabla_ {\beta} \mathbf {e} _ {\alpha}.
$$

The covariant derivative operator $\nabla$ obeys all of the nice rules expected of a derivative operator, except that in curved space $\nabla_{\mathbf{u}}\nabla_{\mathbf{v}} \neq \nabla_{\mathbf{v}}\nabla_{\mathbf{u}}$ (see Chapter 9).

If $\mathbf{u}$ is the tangent vector to a curve, a tensor $\mathbf{Q}$ is said to be parallel propagated along the curve if

$$
\nabla_ {\mathbf {u}} \mathbf {Q} = 0.
$$

If the tangent vector is itself parallel propagated,

$$
\nabla_ {\mathbf {u}} \mathbf {u} = 0
$$

(tangent vector "covariantly constant") the curve is a geodesic, the generalization of a straight line in flat space. If $\mathbf{x}^{\alpha}(\lambda)$ is the geodesic (with $\mathbf{u}^{\alpha} = \mathrm{d}\mathbf{x}^{\alpha} / \mathrm{d}\lambda$ ) then the components of this geodesic equation are

$$
0 = (\nabla_ {\mathbf {u}} \mathbf {u}) ^ {\mu} = \frac {\mathrm {d} \mathbf {u} ^ {\mu}}{\mathrm {d} \lambda} + \mathbf {u} ^ {\alpha} \mathbf {u} ^ {\beta} \Gamma_ {\alpha \beta} ^ {\mu}.
$$

Here $\lambda$ must be an affine parameter along the curve; for non-null curves this means $\lambda$ must be proportional to proper length.

If a curve is timelike, $\mathbf{u}$ is its tangent vector, and $\mathbf{a} \equiv \nabla_{\mathbf{u}} \mathbf{u} = \mathrm{D} \mathbf{u} / \mathrm{d} \tau$ , then a vector $\mathbf{V}$ is said to be Fermi-Walker transported along $\mathbf{u}$ if

$$
\nabla_ {\mathbf {u}} \mathbf {V} = (\mathbf {u} \otimes \mathbf {a} - \mathbf {a} \otimes \mathbf {u}) \cdot \mathbf {V}.
$$

Problem 7.1. Show that the connection coefficients $\Gamma_{\beta \gamma}^{\alpha}$ do not obey the tensor transformation law.

Problem 7.2. For a 2-dimensional flat, Euclidean space described by polar coordinates $\mathbf{r}$ , $\theta$ , assume that the geodesics are the usual straight lines.

(a) Find the connection coefficients $\Gamma_{\beta \gamma}^{\alpha}$ , using your knowledge of these geodesics, and the geodesic equation

$$
\frac {\mathrm {d} ^ {2} \mathbf {x} ^ {\mu}}{\mathrm {d s} ^ {2}} + \frac {\mathrm {d} \mathbf {x} ^ {\alpha}}{\mathrm {d s}} \frac {\mathrm {d} \mathbf {x} ^ {\beta}}{\mathrm {d s}} \Gamma_ {\alpha \beta} ^ {\mu} = 0 .
$$

(b) Next, in the coordinates $\mathbf{x}, \mathbf{y}$ which are related to $\mathbf{r}, \theta$ in the usual way, take the covariant structure to be given by $\Gamma_{\mathbf{x}\mathbf{x}}^{\mathbf{x}} = \Gamma_{\mathbf{x}\mathbf{y}}^{\mathbf{x}} = \dots = 0$ . Using the transformation law for connection coefficients find the connection coefficients in the $\mathbf{r}, \theta$ coordinates.

(c) Finally, from the line element $\mathrm{ds}^2 = \mathrm{dr}^2 +\mathrm{r}^2\mathrm{d}\theta^2$ find the Christoffel symbols, in the usual way, as derivatives of the metric coefficients $\mathbf{g}_{\mu \nu}$ . (All three methods, of course, must give the same Christoffel symbols.)

Problem 7.3. Consider the familiar metric space

$$
\mathrm {d s} ^ {2} = \mathrm {d r} ^ {2} + \mathrm {r} ^ {2} \mathrm {d} \theta^ {2}.
$$

(a) Write the 2 equations that result from the geodesic equation, and show that the following are first integrals of these equations:

$$
r ^ {2} \frac {d \theta}{d s} = R _ {0} = c o n s t a n t
$$

$$
\left(\frac {\mathrm {d} \mathbf {r}}{\mathrm {d} s}\right) ^ {2} + \mathrm {r} ^ {2} \left(\frac {\mathrm {d} \theta}{\mathrm {d} s}\right) ^ {2} = 1.
$$

(b) Use the results in (a) to get a first-order differential equation for $\mathbf{r}(\theta)$ . [That is: Eliminate $s$ as a parameter and replace by $\theta$ ].

(c) Using the fact that the metric space is just flat 2-dimensional!

Euclidean space, write down the general equation for a straight line in $\mathbf{r}$ , $\theta$ coordinates, and show that the straight line satisfies the equation in (b).

Problem 7.4. For the 2-dimensional metric $\mathrm{ds}^2 = (\mathrm{dx}^2 -\mathrm{dt}^2) / \mathrm{t}^2$ , find all connection coefficients $\Gamma_{\alpha \beta \gamma}$ , and find all timelike geodesic curves.

Problem 7.5. Show that the metric tensor is covariantly constant.

Problem 7.6. For a diagonal metric, prove that (in a coordinate frame) the Christoffel symbols are given by

$$
\begin{array}{l} \Gamma_ {\nu \lambda} ^ {\mu} = 0, \qquad \Gamma_ {\lambda \lambda} ^ {\mu} = - \frac {1}{2 \mathrm {g} _ {\mu \mu}} \frac {\partial \mathrm {g} _ {\lambda \lambda}}{\partial \mathbf {x} ^ {\mu}} \\ \Gamma_ {\mu \lambda} ^ {\mu} = \frac {\partial}{\partial \mathbf {x} ^ {\lambda}} \left(\log \left(| \mathbf {g} _ {\mu \mu} |\right) ^ {\frac {1}{2}}\right), \quad \Gamma_ {\mu \mu} ^ {\mu} = \frac {\partial}{\partial \mathbf {x} ^ {\mu}} \left(\log \left(| \mathbf {g} _ {\mu \mu} |\right) ^ {\frac {1}{2}}\right). \\ \end{array}
$$

Here $\mu \neq \nu \neq \lambda$ and there is no summation over repeated indices.

Problem 7.7. Prove the following identities:

(a) $\mathbf{g}_{\alpha \beta ,\gamma} = \Gamma_{\alpha}\beta \gamma +\Gamma_{\beta \alpha \gamma}$   
(b) $\mathbf{g}_{\alpha \mu} \mathbf{g}^{\mu \beta}, \gamma = -\mathbf{g}^{\mu \beta} \mathbf{g}_{\alpha \mu, \gamma}$ .   
(c) $\mathbf{g}^{\alpha \beta}_{,\gamma} = -\Gamma_{\mu \gamma}^{\alpha}\mathbf{g}^{\mu \beta} - \Gamma_{\mu \gamma}^{\beta}\mathbf{g}^{\mu \alpha}.$   
(d) $\mathbf{g}_{,a} = -\mathbf{gg}_{\beta \gamma}\mathbf{g}_{,a}^{\beta \gamma} = \mathbf{gg}_{\beta \gamma}\mathbf{g}_{\beta \gamma ,a}$ .   
(e) $\Gamma_{\alpha \beta}^{\alpha} = (\log |\mathbf{g}|^{\frac{1}{2}}),\beta$ in a coordinate frame.   
(f) $\mathbf{g}^{\mu \nu}\Gamma_{\mu \nu}^{\alpha} = -\frac{1}{|\mathbf{g}|^{\frac{1}{2}}} (\mathbf{g}^{\alpha \nu}|\mathbf{g}|^{\frac{1}{2}}),\nu$ in a coordinate frame.   
(g) $\mathbf{A}_{;a}^{\alpha} = \frac{1}{|\mathbf{g}|^{\frac{1}{2}}} (|\mathbf{g}|^{\frac{1}{2}}\mathbf{A}^{\alpha})_{,a}$ in a coordinate frame.   
(h) $\mathbf{A}_{\alpha}^{\beta}; \beta = \frac{1}{|\mathbf{g}|^{\frac{1}{2}}} (|\mathbf{g}|^{\frac{1}{2}} \mathbf{A}_{\alpha}^{\beta}), \beta - \Gamma_{\alpha \mu}^{\lambda} \mathbf{A}_{\lambda}^{\mu}$ in a coordinate frame.   
(i) $\mathbf{A}^{\alpha \beta}$ ; $\beta = \frac{1}{|\mathbf{g}|^{\frac{1}{2}}}(|\mathbf{g}|^{\frac{1}{2}}\mathbf{A}^{\alpha \beta})$ , $\beta$ in a coordinate frame, if $\mathbf{A}^{\alpha \beta}$ is antisymmetric.   
(j) $\square S = S_{,a}^{;a} = \frac{1}{|g|^{\frac{1}{2}}} (|g|^{\frac{1}{2}} g^{\alpha \beta} S, \beta), a$ in a coordinate frame.

Problem 7.8. Let $\mathbf{A} \equiv \det(\mathbf{A}_{\mu\nu})$ where $\mathbf{A}_{\mu\nu}$ is a second rank tensor. Show that $\mathbf{A}$ is not a scalar. (i.e., Show that its value changes under coordinate transformations.) Since $\mathbf{A}$ is not a scalar one cannot define $\mathbf{A}_{;a} = \mathbf{A}_{,a}$ . How should $\mathbf{A}_{;a}$ be defined (in terms of $\mathbf{A}_{,a}$ and $\mathbf{A}$ )?

Problem 7.9. If a geodesic is timelike at a given point $\mathbf{P}$ , show that it is timelike everywhere along its length, and similarly for spacelike or null, geodesics.

Problem 7.10. Derive the geodesic equation from the definition of a geodesic as a curve of extremal length.

Problem 7.11. An affine parameter $\lambda$ is one for which the equation of geodesic motion has the form

$$
\frac {\mathrm {d} \mathbf {x} ^ {\alpha}}{\mathrm {d} \lambda^ {2}} + \Gamma_ {\beta \gamma} ^ {\alpha} \frac {\mathrm {d} \mathbf {x} ^ {\beta}}{\mathrm {d} \lambda} \frac {\mathrm {d} \mathbf {x} ^ {\gamma}}{\mathrm {d} \lambda} = 0.
$$

Show that all affine parameters are related by linear transformations with constant coefficients.

Problem 7.12. Show that in flat spacetime, the conservation law for the 4-momentum of a freely moving particle can be written $\nabla_{\mathbf{p}} \mathbf{p} = 0$ . Show that particles with nonzero rest mass move along timelike geodesics.

Problem 7.13. Suppose the coordinate $\mathbf{x}^1$ is a cyclic coordinate, i.e. the metric functions $\mathbf{g}_{\alpha \beta}$ are independent of $\mathbf{x}^1$ . If $\mathbf{p}$ is the momentum of an unaccelerated particle, show that the component $\mathbf{p}_1$ is constant along the particle world line.

Problem 7.14. Prove the general relativity version of Fermat's principle: In any static metric $(\mathbf{g}_{0j} = \mathbf{g}_{\alpha \beta,0} = 0)$ , consider all null curves between two points in space, $\mathbf{x}^j = \mathbf{a}^j$ and $\mathbf{x}^j = \mathbf{b}^j$ . Each such null curve $\mathbf{x}^j(t)$ requires a particular coordinate time $\Delta t$ to get from $\mathbf{a}^j$ to $\mathbf{b}^j$ . Show that the curves of extremal time $\Delta t$ are null geodesics of the spacetime.

# Problem 7.15.

(a) Show that the geodesics of the velocity space metric defined in Problem 6.8 are paths of minimum fuel use for a rocket ship changing its velocity.   
(b) A rocket ship in interstellar space with velocity $\underline{\mathbf{v}}_1$ (with respect to the earth) changes its velocity to a new velocity $\underline{\mathbf{v}}_2$ , in a manner that uses up the least fuel. What is the ship's smallest velocity relative to earth during the change?

Problem 7.16. On the surface of a two-sphere, $\mathrm{ds}^2 = \mathrm{d}\theta^2 + \sin^2\theta \mathrm{d}\phi^2$ , the vector $\mathbf{A}$ is equal to $\mathbf{e}_{\theta}$ at $\theta = \theta_0$ , $\phi = 0$ . What is $\mathbf{A}$ after it is parallel transported around the circle $\theta = \theta_0$ ? What is the magnitude of $\mathbf{A}$ ?

Problem 7.17. Consider an observer with 4-velocity $\mathbf{u}$ who transports his four basis vectors $\mathbf{e}_{\alpha}$ along with him according to the transport law $\nabla_{\mathbf{u}}\mathbf{e}_{\alpha} = \mathbf{A}_{\alpha}^{\beta}\mathbf{e}_{\beta}$ . What is the most general form of $\mathbf{A}_{\alpha}^{\beta}$ if:

(i) the basis vectors are to be orthonormal?   
(ii) in addition $\mathbf{e}_{\hat{\mathbf{o}}} = \mathbf{u}$ ? (i.e. the frame is his rest-frame).   
(iii) in addition the spatial vectors are to be nonrotating? (i.e. He sees a freely-falling particle move with no Coriolis forces.)

Problem 7.18. Show that the scalar product of two vectors is not altered as they are both Fermi-Walker transported along a curve $\mathcal{C}$ .

Problem 7.19. Show that Fermi-Walker transport along a geodesic curve is the same as parallel transport.

Problem 7.20. Write the following expressions in index-free notation:

(a) $\mathrm{U}_{\alpha ;\beta}\mathrm{U}^{\beta}\mathrm{U}^{a}$

(b) $\mathbf{V}_{; \beta}^{\alpha} \mathbf{U}^{\beta} - \mathbf{U}_{; \beta}^{\alpha} \mathbf{V}^{\beta}$

(c) $\mathrm{T}_{\alpha \beta ;\gamma}\mathrm{V}^{\alpha}\mathbb{W}^{\beta}\mathrm{U}^{\gamma}$

(d) $\mathsf{W}^{\alpha ;\beta}\mathsf{V}_{\beta ;\gamma}\mathsf{U}^{\gamma}$

(e) $\mathsf{W}^{\alpha}_{;\gamma \beta}\mathsf{U}^{\gamma}\mathsf{U}^{\beta} + \mathsf{W}^{\alpha}_{;\gamma}\mathsf{U}^{\gamma}_{;\beta}\mathsf{U}^{\beta} - \mathsf{U}^{\alpha}_{;\beta}\mathsf{W}^{\beta}_{;\gamma}\mathsf{U}^{\gamma}$ .

Problem 7.21. Show that the paths of light rays in a static, isotropic spacetime can be described by taking the space to have a certain spatially

varying “index of refraction” $\mathfrak{n}(\mathbf{x}^{\mathrm{j}})$ . What is $\mathfrak{n}$ in terms of $\mathfrak{g}_{\alpha \beta}$ ? Assume $\mathfrak{g}_{\alpha \beta}$ has the form $\mathrm{ds}^2 = g_{\alpha \beta} \mathrm{dt}^2 - f(\mathrm{dx}^2 + \mathrm{dx}^2 + \mathrm{dx}^2)$ .

Problem 7.22. An inebriated astronaut pulses his rocket, firing in a random direction for each pulse. As measured in a momentarily comoving frame, each pulse corresponds to a velocity boost of $\Delta v << c$ . Find the probability distribution of his resultant velocity after $n$ boosts, where $n$ is a very large number. Show that the drunk astronaut achieves highly relativistic velocities less efficiently than a sober astronaut (who fires his rocket always in the same direction), and takes on the average $3c / \Delta v$ times as many pulses to achieve the same velocity.

# Problem 7.23.

(a) Suppose a vector field $\mathbf{k}$ is orthogonal to a family of hypersurfaces ("hypersurface-orthogonal"). Show that this implies $\mathbf{k}_{[\mu ;\nu}\mathbf{k}_{\lambda ]} = 0$

(b) What is the geometric interpretation if $\mathbf{k}_{[\mu ;\nu ]}$ also vanishes?

Problem 7.24. Prove that any congruence of null curves that is hypersurface-orthogonal consists of null geodesics.

Problem 7.25. Show that the variational principle

$$
\delta \int \left(\mathrm {g} _ {\alpha \beta} \dot {\mathrm {x}} ^ {\alpha} \dot {\mathrm {x}} ^ {\beta}\right) \mathrm {d s} = 0
$$

givesthe same geodesics as the defining property for geodesics

$$
\delta \int \left(\mathrm {g} _ {\alpha \beta} \dot {\mathrm {x}} ^ {\alpha} \dot {\mathrm {x}} ^ {\beta}\right) ^ {\frac {1}{2}} \mathrm {d s} = 0
$$

when s is proper length (not an arbitrary parameterization) and $\dot{\mathbf{x}}\equiv$ $\mathrm{dx}^a /\mathrm{ds}$ . If $\mathbf{y}\equiv (\mathbf{g}_{\alpha \beta}\dot{\mathbf{x}}^{\alpha}\dot{\mathbf{x}}^{\beta})^{\frac{1}{2}}$ , show that

$$
\delta \int F (y) d s = 0
$$

givesthe same geodesicsforanymonotonicfunction $\mathbf{F}(\mathbf{y})$

# CHAPTER 8

# DIFFERENTIAL GEOMETRY: FURTHER CONCEPTS

A vector $\mathbf{B}$ is related to its contravariant components $\mathbf{B}^{\mu}$ by

$$
\mathbf {B} = \mathbf {B} ^ {\mu} \mathbf {e} _ {\mu},
$$

where the $\mathbf{e}_{\mu}$ are basis vectors. The covariant components $\mathbf{B}_{\mu}$ represent the same vector, but represent it as a different type of "vector", called a one-form. (Loosely, one-forms are often called "covariant vectors".) For one-forms the analog of the above equation is

$$
\tilde {\textbf {B}} = \textbf {B} _ {\mu} \tilde {\boldsymbol {\omega}} ^ {\mu},
$$

where $\sim$ indicates a one-form and $\tilde{\omega}^{\mu}$ are basis one-forms with covariant components $(1,0,0,0)$ , $(0,1,0,0)$ , etc. For an arbitrary tensor $\mathbf{T}$ , with components $\mathbf{T}_{\alpha \beta} \ldots^{\gamma \delta \cdots}$ ,

$$
\mathbf {T} = \mathbf {\Delta T} _ {\alpha \beta} \dots^ {\gamma \delta \dots} \tilde {\pmb {\omega}} ^ {\alpha} \otimes \tilde {\pmb {\omega}} ^ {\beta} \otimes \dots \otimes \mathbf {e} _ {\gamma} \otimes \mathbf {e} _ {\delta} \otimes \dots .
$$

The scalar product of two vectors, or of two one-forms, involves the metric tensor, and is denoted by a “dot”:

$$
\mathbf {A} \cdot \mathbf {B} = \mathrm {g} _ {\mu \nu} \mathrm {A} ^ {\mu} \mathrm {B} ^ {\nu}
$$

$$
\tilde {\mathbf {A}} \cdot \tilde {\mathbf {B}} = \mathrm {g} ^ {\mu \nu} \mathrm {A} _ {\mu} \mathrm {B} _ {\nu}.
$$

(Here $\mathbf{g}^{\mu \nu}$ is the matrix inverse of $\mathbf{g}_{\mu \nu}$ .) The scalar product of a vector with a one-form does not involve the metric, only a summation over an index. This is sometimes distinguished notationally as

$$
\mathbf {\tilde {B}} \cdot \mathbf {A} \equiv <   \mathbf {\tilde {B}}, \mathbf {A} > \equiv \mathbf {B} _ {\mu} \mathbf {A} ^ {\mu}
$$

Since $\langle \tilde{\omega}^{\mu},\mathbf{e}_{\nu}\rangle = \delta_{\nu}^{\mu}$ , the basis $\tilde{\omega}^{\mu}$ is said to be "dual" to the basis $\mathbf{e}_{\mu}$ . If $\tilde{\mathbf{B}}$ and $\tilde{\mathbf{A}}$ are one-forms corresponding to vectors $\mathbf{B}$ and $\mathbf{A}$ we have, of course, $\mathbf{A}\cdot \mathbf{B} = \tilde{\mathbf{A}}\cdot \tilde{\mathbf{B}} = <  \tilde{\mathbf{B}},\mathbf{A}> = <  \tilde{\mathbf{A}},\mathbf{B}>$ .

A one-form of particular usefulness is $\widetilde{\mathrm{df}}$ , the gradient of any scalar function $f$ . When combined with a vector $v$ , it gives the directional derivative of $f$ along $v$ .

$$
<   \widetilde {\mathrm {d f}}, \mathbf {v} > = \nabla_ {\mathbf {v}} \mathbf {f} = \mathbf {f} _ {, a} \mathbf {v} ^ {a}.
$$

The basis vectors $\mathbf{e}_{\alpha}$ corresponding to a coordinate system are tangent to the coordinate lines. This motivates the notation for a coordinate basis vector

$$
\mathbf {e} _ {\alpha} = \frac {\partial}{\partial \mathbf {x} ^ {\alpha}}.
$$

Similarly, the coordinate basis one-forms are gradients of the coordinate surfaces,

$$
\tilde {\boldsymbol {\omega}} ^ {\alpha} \equiv \widetilde {\mathbf {d x}} ^ {\alpha}.
$$

Alternatively, since a spacetime metric can locally be transformed to the Minkowski metric, it is always possible to find a set of orthonormal basis vectors and one-forms at every point. These are not necessarily tangents to or gradients of the coordinates; they are denoted by $\mathbf{e}_{\hat{\mu}}, \tilde{\boldsymbol{\omega}}^{\hat{\mu}}$ , where $\hat{\boldsymbol{\omega}}$ indicates orthonormality. Note that the relations $<\tilde{\boldsymbol{\omega}}^{\alpha}, \mathbf{e}_{\beta}> = \delta^{\alpha}{}_{\beta}$ , $\mathbf{e}_{\alpha} \cdot \mathbf{e}_{\beta} = \mathbf{g}_{\alpha \beta}$ , and $\tilde{\boldsymbol{\omega}}^{\alpha} \cdot \tilde{\boldsymbol{\omega}}^{\beta} = \mathbf{g}^{\alpha \beta}$ always hold. When the basis is orthonormal, then in addition $\mathbf{g}_{\alpha \beta} = \eta_{\alpha \beta}$ and $\mathbf{g}^{\alpha \beta} = \eta^{\alpha \beta}$ . If a local orthonormal frame in spacetime is freely falling (i.e. the basis is that of a freely falling observer), then all the $\Gamma^{\alpha}{}_{\beta \gamma}$ vanish at the center of the frame.

The commutator of two basis-vector fields

$$
\nabla_ {\mathbf {e} _ {\alpha}} \mathbf {e} _ {\beta} - \nabla_ {\mathbf {e} _ {\beta}} \mathbf {e} _ {\alpha} = [ \mathbf {e} _ {\alpha}, \mathbf {e} _ {\beta} ] \equiv \mathbf {c} _ {\alpha \beta} ^ {\gamma} \mathbf {e} _ {\gamma}
$$

vanishes identically, $\mathbf{c}_{\alpha} \beta^{\gamma} = 0$ , if and only if $\mathbf{e}_{\alpha}$ and $\mathbf{e}_{\beta}$ are the tangent vectors to come coordinate system (a coordinate basis). In a

general (not necessarily a coordinate) basis,

$$
\Gamma_ {\mu \beta \gamma} \equiv \mathbf {e} _ {\mu} \cdot (\nabla_ {\gamma} \mathbf {e} _ {\beta}) = \frac {1}{2} \left(\mathbf {g} _ {\mu \beta , \gamma} + \mathbf {g} _ {\mu \gamma , \beta} - \mathbf {g} _ {\beta \gamma , \mu} + \mathbf {c} _ {\mu \beta \gamma} + \mathbf {c} _ {\mu \gamma \beta} - \mathbf {c} _ {\beta \gamma \mu}\right).
$$

A tensor of rank $p$ with all of its indices covariant, and which is totally antisymmetric on all indices, is called a $p$ -form. A totally antisymmetrized direct product of forms is denoted by a wedge “ $\wedge$ ”.

The concepts of Lie differentiation, Lie transport, and exterior differentiation of forms are developed in problems.

![](images/85052b23b4f038bbc9f4c7e10a14f64e6971fd4a8b9436bd4457c2c34b439071.jpg)

# Problem 8.1.

(a) A spacetime has coordinates $\mathbf{x}^a$ with basis vectors $\partial/\partial \mathbf{x}^a$ and basis one-forms $\widetilde{\mathrm{dx}}^a$ . What are the values of:

$$
<   \widetilde {\mathbf {d x}} ^ {0}, \partial / \partial \mathbf {x} ^ {0} >, <   \widetilde {\mathbf {d x}} ^ {2}, \partial / \partial \mathbf {x} ^ {3} >, (\partial / \partial \mathbf {x} ^ {0}) \cdot (\partial / \partial \mathbf {x} ^ {1}), \widetilde {\mathbf {d x}} ^ {0} \cdot \widetilde {\mathbf {d x}} ^ {1}, \widetilde {\mathbf {d x}} ^ {0} \cdot \widetilde {\mathbf {d x}} ^ {0}?
$$

(b) To what vector does the one-form $\widetilde{\mathbf{dx}}^1$ correspond?

Problem 8.2. The usual basis for polar coordinates, $\mathbf{e}_{\hat{\mathbf{r}}} = \mathbf{e}_{\mathbf{r}}$ , $\mathbf{e}_{\hat{\boldsymbol{\theta}}} = \mathbf{r}^{-1}\mathbf{e}_{\boldsymbol{\theta}}$ is not a coordinate basis. Consider the one-form basis $\tilde{\pmb{\omega}}^{\hat{\mathbf{i}}}$ dual to this basis

$$
<   \tilde {\boldsymbol {\omega}} ^ {\hat {\mathbf {i}}}, \mathbf {e} _ {\hat {\mathbf {j}}} > = \delta_ {\mathbf {j}} ^ {\mathbf {i}}.
$$

Find the function $f$ such that $\tilde{\omega}^{\hat{\mathbf{r}}} = \widetilde{\mathbf{df}}$ and prove that there does not exist a function $g$ such that $\tilde{\omega}^{\hat{\boldsymbol{\theta}}} = \widetilde{\mathbf{dg}}$ . Do this without imposing any metric on the polar coordinates.

Problem 8.3. In 3-dimensional Euclidean space, what is a necessary and sufficient condition on a field of one-forms $\tilde{\sigma}$ for there to exist a function $f$ such that $\tilde{\sigma} = \widetilde{\mathrm{df}}$ ?

Problem 8.4. If $\Omega_1$ is a p-form and $\Omega_2$ a q-form, show that

$$
\Omega_ {1} \wedge \Omega_ {2} = (- 1) ^ {\mathrm {p q}} \Omega_ {2} \wedge \Omega_ {1}.
$$

Problem 8.5. The exterior derivative of a differential form $\Omega$ can be defined axiomatically by the following properties:

(i) If $\Omega$ is a p-form, $d\Omega$ is a $(p + 1)$ -form;   
(ii) $\mathrm{d}(\Omega_1 + \Omega_2) = \mathrm{d}\Omega_1 + \mathrm{d}\Omega_2;$   
(iii) For a zero form $f$ (scalar), $\widetilde{df}$ is defined by $<\widetilde{df}, v> = \nabla_v f$ for any $v$ ;   
(iv) $\mathbf{d}(\Omega_1\wedge \Omega_2) = \mathbf{d}\Omega_1\wedge \Omega_2 + (-1)^{\mathrm{p}}\Omega_1\wedge \mathbf{d}\Omega_2$ where $\Omega_{1}$ is a p-form;

[Note: If $\mathbf{p} = 0$ (i.e. f a scalar) this reads: $\widetilde{\mathbf{d}}(\mathbf{f}\Omega) = \widetilde{\mathbf{d}}\mathbf{f} \wedge \Omega + \mathbf{f}\widetilde{\mathbf{d}}\Omega$ .]

(v) $\mathrm{dd}\Omega = 0$ for any $\Omega$ .

An alternative definition notes that a p-form is a completely antisymmetric covariant tensor of rank $p$ , and defines the exterior derivative as the completely antisymmetrized covariant derivative. Show that these definitions are equivalent.

Problem 8.6. Consider a 2-form in $n$ -dimensional space:

$$
\alpha = f \left(x ^ {1}, x ^ {2}, \dots , x ^ {n}\right) \widetilde {\mathrm {d} x ^ {1}} \wedge \widetilde {\mathrm {d} x ^ {2}}.
$$

Suppose for some region of space including $\mathbf{x}^1 = 0$ , that

$$
\mathrm {d} \alpha = 0.
$$

Construct the 1-form

$$
\widetilde {\boldsymbol {\beta}} = \left[ \mathrm {x} ^ {1} \int_ {0} ^ {1} \mathrm {f} (\xi \mathrm {x} ^ {1}, \mathrm {x} ^ {2}, \dots , \mathrm {x} ^ {\mathrm {n}}) \mathrm {d} \xi \right] \widetilde {\mathrm {d x}} ^ {2}
$$

and show that $\alpha = \mathrm{d}\tilde{\beta}$

Problem 8.7. The components of the Maxwell tensor $\mathbf{F}_{\alpha \beta}$ can be regarded as the components of a 2-form $\mathbf{F}$ . Show that Maxwell's equations in vacuum can be written $\mathrm{d}\mathbf{F} = \mathbf{0}$ , $\mathrm{d}*\mathbf{F} = \mathbf{0}$ .

Problem 8.8. A 3-surface in spacetime is spacelike, timelike, or null, if its normal vector is timelike, spacelike, or null respectively. It is desired to find three orthogonal linearly independent vectors in a 3-surface. Show that for a spacelike surface, these are all spacelike; for a timelike surface,

two spacelike and one timelike; for a null surface, one null and two spacelike.

Problem 8.9. Show that the integral $\int_{\mathbf{S}} \mathbf{F}^{\mu} \mathrm{d}^{3}\Sigma_{\mu}$ , where $\mathbf{F}^{\mu}$ is some vector field and $\mathbf{S}$ is some oriented 3-dimensional hypersurface in spacetime, is independent of the parametrization $\mathbf{x}^{\mu} = \mathbf{x}^{\mu}(\mathbf{a}, \mathbf{b}, \mathbf{c})$ used to describe $\mathbf{S}$ . [See Problem 3.30 for the definition of $\mathrm{d}^{3}\Sigma_{\mu}$ .]

Problem 8.10. [Note: This problem assumes a familiarity with the Cartan calculus, beyond the scope of most relativity texts. Succeeding problems do not depend on it.] In the language of differential forms the generalized

Stokes' theorem is

$$
\int_ {\Omega} \mathrm {d} \boldsymbol {\theta} = \int_ {\partial \Omega} \boldsymbol {\theta}.
$$

To what does this theorem reduce, in the following cases

(a) $\Omega$ is 3-dimensional, $\pmb{\theta} = \mathbf{f}^{\mathrm{k}}\mathbf{d}^{2}\mathbf{S}_{\mathbf{k}}$   
(b) $\Omega$ is 4-dimensional, $\pmb{\theta} = \mathbf{f}^{\mu}\mathbf{d}^{3}\pmb{\Sigma}_{\mu}$ .   
(c) $\Omega$ is 3-dimensional, $\pmb{\theta} = \mathbf{F}^{\mu \nu}\mathbf{d}^{2}\pmb{\Sigma}_{\mu \nu}$ where $\mathbf{F}^{\mu \nu}$ is antisymmetric.   
(d) Use the generalized Stokes theorem to derive the familiar relation

$$
\int_ {\underset {\sim} {\mathbf {A}}} \cdot \underline {{\mathrm {d} l}} = \int (\underset {\sim} {\nabla} \times \underline {{\mathbf {A}}}) \cdot \underline {{\mathrm {d} S}}.
$$

Problem 8.11. Show that there exists no tensor with components constructed from the 10 metric coefficients $\mathbf{g}_{\alpha \beta}$ and their 40 first derivatives $\mathbf{g}_{\alpha \beta, \mu}$ - except $\mathbf{g}$ itself and products of it with itself, e.g. $\mathbf{g} \otimes \mathbf{g}$ .

# Problem 8.12.

(a) Show that, in a coordinate frame, $\Gamma_{\alpha \beta \gamma}$ is symmetric on the last two indices.   
(b) Show that in an orthonormal frame, $\Gamma_{\alpha \beta \gamma}$ is antisymmetric on the first two indices.

Problem 8.13. The Lie derivative of a scalar function is defined to be the directional derivative: $\mathcal{L}_{\mathbf{x}}\mathbf{f} = \nabla_{\mathbf{x}}\mathbf{f}$ . For a vector field $\mathbf{y}$ , we define

Lie differentiation as $\mathcal{L}_{\mathbf{x}}\mathbf{y} \equiv [\mathbf{x},\mathbf{y}] = \nabla_{\mathbf{x}}\mathbf{y} - \nabla_{\mathbf{y}}\mathbf{x}$ . The Lie derivative obeys all the usual rules for a derivative operator and always gives a tensor of the same rank as the tensor differentiated.

(a) What is the Lie derivative of a 1-form?   
(b) What is the Lie derivative of a tensor whose components are $\mathbf{T}^{\alpha}\beta$ ?

Problem 8.14. Suppose $\mathbf{A} = \mathrm{d} / \mathrm{d}\lambda$ is the tangent vector field to a congruence (set of curves) $\mathbf{x}^{\alpha} = \mathbf{x}^{\alpha}(\lambda)$ and $\mathbf{B}$ is a vector field. Show that the geometrical interpretation of the transport law $\mathfrak{L}_{\mathbf{A}}\mathbf{B} = \mathbf{0}$ is that $\mathbf{B}$ connects points of equal $\lambda$ on neighboring curves of the congruence.

Problem 8.15. Show that Lie differentiation commutes with the operation of contraction.

Problem 8.16. Show that

$$
\mathcal {L} _ {\bf u} \mathcal {L} _ {\bf v} - \mathcal {L} _ {\bf v} \mathcal {L} _ {\bf u} = \mathcal {L} _ {[ \bf u, v ]}.
$$

Problem 8.17. Another definition of the Lie derivative of a geometric object $\Phi^{\mathbf{A}}[\mathbf{x}^{\mu}(\mathbf{P})]$ (A represents all the tensor indices, $\mathbf{x}^{\mu}(\mathbf{P})$ are the coordinates of a point $\mathbf{P}$ ) is as follows: Make an infinitesimal point transformation $\mathbf{P}_0 \to \mathbf{P_N}$ by $\mathbf{x}^{\mu}(\mathbf{P}_0) = \mathbf{x}^{\mu}(\mathbf{P_N}) + \xi^{\mu}(\mathbf{P_N})$ . (Since $\xi^{\mu}$ is infinitesimal, it can in fact be evaluated at either $\mathbf{P}_0$ or $\mathbf{P_N}$ .) Also make an infinitesimal coordinate transformation that makes the numerical values of the coordinates of $\mathbf{P_N}$ the same as those of $\mathbf{P}_0$ in the original coordinates:

$$
\overline {{\mathbf {x}}} ^ {\mu} (\mathbf {P _ {N}}) = \mathbf {x} ^ {\mu} (\mathbf {P _ {0}}).
$$

Then define

$$
\mathcal {L} _ {\boldsymbol {\xi}} \Phi^ {\mathbf {A}} (\mathrm {P} _ {0}) = \underset {\boldsymbol {\xi} \to 0} {\text {L I M}} \left[ \Phi^ {\mathbf {A}} (\mathrm {P} _ {0}) - \overline {{\Phi}} ^ {\mathbf {A}} (\mathrm {P} _ {\mathrm {N}}) \right]  .
$$

Show that this definition is equivalent to that of Problem 8.13 by examining the cases (i) $\Phi^{\mathbf{A}} = \mathbf{a}$ scalar field (ii) $\Phi^{\mathbf{A}} = \mathbf{A}_{\mu}$ (iii) $\Phi^{\mathbf{A}} = \mathbf{T}_{\mu}^{\nu}$ .

Problem 8.18. It is desired to transport a vector $\mathbf{v}$ along a curve with tangent vector $\mathbf{u}$ . Which of the following are necessary for parallel transport? - for Fermi-Walker transport? - for Lie transport?: metric; affine connection; $\mathbf{u}(\mathbf{x})$ defined off the curve.

Problem 8.19. You are given a vector field $\mathbf{v}^{\mathrm{i}} = (-\mathbf{y},\mathbf{x},\mathbf{z}^{\alpha}),\alpha = \text{constant}$ , in a 3-space with metric $\mathrm{ds}^2 = \mathrm{dx}^2 +\mathrm{dy}^2 +\mathrm{dz}^2$ . A certain vector $\underline{\mathbf{u}}$ is Lie transported along $\underline{\mathbf{v}}$ from a point $\mathbf{A}$ to a point $\mathbf{B}$ and is then parallel transported back to $\mathbf{A}$ by the reverse route. For what value of $\alpha$ is there a $\underline{\mathbf{u}}$ which is always left unchanged by this process?

Problem 8.20. Find the most general vector field which is everywhere parallel-propagated along itself. Fermi-Walker transported along itself. Lie transported along itself.

Problem 8.21. If $\Omega$ is a p-form, show that $\mathcal{L}_{\mathbf{X}}(\mathrm{d}\Omega) = \mathrm{d}(\mathcal{L}_{\mathbf{X}}\Omega)$ .

Problem 8.22. Vector analysis in 3-dimensional orthogonal curvilinear coordinates is a special case of tensor analysis where $\mathbf{g}_{ij} = \mathbf{h}_i^2\delta_{ij}$ (not summed). The $\mathbf{h}_i$ 's are functions of the coordinates called "scale factors". Vector components are often referred to the ("physical") orthonormal basis $\tilde{\pmb{\omega}}^{\hat{\mathbf{i}}} = \mathbf{h}_i\widetilde{\mathbf{dx}}^{\hat{\mathbf{i}}}$ (not summed). Derive expressions for (i) $\nabla S$ , (ii) $\nabla \times \underline{\mathbf{V}}$ , (iii) $\nabla \cdot \underline{\mathbf{V}}$ and (iv) $\nabla^2 S$ , where $S$ is a scalar field and $\underline{\mathbf{V}}$ a vector field.

Problem 8.23. Derive expressions for $\underline{\nabla} \cdot \underline{\mathbf{A}}$ and $\underline{\nabla} \times \underline{\mathbf{A}}$ in spherical polar coordinates.

Problem 8.24. If $\mathbf{F}_{\mu \nu} = \mathbf{A}_{\nu ;\mu} - \mathbf{A}_{\mu ;\nu},$ prove that $\mathbf{F}_{[\mu \nu ;\lambda]} = 0$

Problem 8.25. In an arbitrary spacetime manifold (not necessarily homogeneous or isotropic), pick an initial spacelike hypersurface $S_{\mathbf{I}}$ , place an arbitrary coordinate grid $(\mathbf{x}^1, \mathbf{x}^2, \mathbf{x}^3)$ on it, eject geodesic world lines orthogonal to it, and give these world lines the coordinates $(\mathbf{x}^1, \mathbf{x}^2, \mathbf{x}^3) = \text{constant}, \mathbf{x}^0 \equiv t = t_{\mathbf{I}} + \tau$ where $\tau$ is proper time along the world line,

beginning with $\tau = 0$ on $\mathbf{S}_{\mathbf{I}}$ . Show that in this coordinate system ("Gaussian normal coordinates") the metric takes on the synchronous form

$$
d s ^ {2} = - d t ^ {2} + g _ {i j} d x ^ {i} d x ^ {j}.
$$

Problem 8.26.

(a) If $\mathbf{g}_{\mu \nu}$ and $\overline{\mathbf{g}}_{\mu \nu}$ are the components of two symmetric tensors, show that $\mathbf{S}_{\mu \nu}^{\lambda} = \overline{\Gamma}_{\mu \nu}^{\lambda} - \Gamma_{\mu \nu}^{\lambda}$

are the components of a tensor. Here the $\Gamma$ 's and $\overline{\Gamma}$ 's are Christoffel symbols formed from the tensors $\mathbf{g}$ and $\overline{\mathbf{g}}$ in the usual way.

(b) Suppose $\mathbf{g}_{\mu \nu}$ and $\overline{\mathbf{g}}_{\mu \nu}$ have the same geodesics. Then show that

$$
\mathsf {S} _ {\mu \nu} ^ {\lambda} = \delta_ {\mu} ^ {\lambda} \Psi_ {\nu} + \delta_ {\nu} ^ {\lambda} \Psi_ {\mu}
$$

where $\Psi_{\mu}$ are the components of a vector.

Problem 8.27. Compute the connection coefficients of the following metric in an orthonormal frame

$$
\begin{array}{l} \mathrm {d s} ^ {2} = - \mathrm {e} ^ {2 \alpha} \mathrm {d t} ^ {2} + \mathrm {e} ^ {2 \beta} \mathrm {d r} ^ {2} + \mathrm {e} ^ {2 \gamma} (\mathrm {d} \theta^ {2} + \sin^ {2} \theta \mathrm {d} \phi^ {2}) \\ a, \beta , \gamma = f u n c t i o n s o f r a n d t. \\ \end{array}
$$

Problem 8.28. The redshift between two observers (with 4-velocities $\mathbf{u}_{\mathbf{A}}$ and $\mathbf{u}_{\mathbf{B}}$ ) can be defined in two ways: (i) by the energies of a photon (4-momentum $\mathbf{p}$ ) travelling along a null geodesic between them: $1 + z \equiv \mathbf{u}_{\mathbf{A}} \cdot \mathbf{p} / \mathbf{u}_{\mathbf{B}} \cdot \mathbf{p}$ , or (ii) by the proper time between two null geodesics, emitted $\Delta \tau_{\mathbf{A}}$ apart and received $\Delta \tau_{\mathbf{B}}$ apart, $1 + z \equiv \Delta \tau_{\mathbf{A}} / \Delta \tau_{\mathbf{B}}$ . Show that these definitions are equivalent.

# CHAPTER 9 CURVATURE

The study of curvature is based on the Riemann curvature tensor:

$$
\mathsf {R} _ {\nu \alpha \beta} ^ {\mu} \equiv \frac {\partial \Gamma_ {\nu \beta} ^ {\mu}}{\partial \mathbf {x} ^ {\alpha}} - \frac {\partial \Gamma_ {\nu \alpha} ^ {\mu}}{\partial \mathbf {x} ^ {\beta}} + \Gamma_ {\rho \alpha} ^ {\mu} \Gamma_ {\nu \beta} ^ {\rho} - \Gamma_ {\rho \beta} ^ {\mu} \Gamma_ {\nu \alpha} ^ {\rho}
$$

in a coordinate frame. The covariant components of the Riemann tensor are connected by several symmetries

$$
\mathrm {R} _ {\alpha \beta \gamma \delta} = \mathrm {R} _ {\gamma \delta \alpha \beta}, \quad \mathrm {R} _ {\alpha \beta \gamma \delta} = - \mathrm {R} _ {\beta \alpha \gamma \delta},
$$

$$
\mathrm {R} _ {\alpha \beta \gamma \delta} = - \mathrm {R} _ {\alpha \beta \delta \gamma}, \quad \mathrm {R} _ {\alpha [ \beta \gamma \delta ]} = 0.
$$

The (symmetric) Ricci tensor and the Ricci scalar are formed from the Riemann tensor:

$$
\mathrm {R} _ {\alpha \beta} \equiv \mathrm {R} _ {\alpha \mu \beta} ^ {\mu}
$$

$$
\mathbf {R} \equiv \mathbf {R} _ {\alpha} ^ {\alpha}.
$$

The Weyl tensor,

$$
\begin{array}{l} \mathrm {C} _ {\lambda \mu \nu \kappa} \equiv \mathrm {R} _ {\lambda \mu \nu \kappa} - \frac {1}{2} \left(\mathrm {g} _ {\lambda \nu} \mathrm {R} _ {\mu \kappa} - \mathrm {g} _ {\lambda \kappa} \mathrm {R} _ {\mu \nu} - \mathrm {g} _ {\mu \nu} \mathrm {R} _ {\lambda \kappa} + \mathrm {g} _ {\mu \kappa} \mathrm {R} _ {\lambda \nu}\right) \\ + \frac {1}{6} \left(\mathrm {g} _ {\lambda \nu} \mathrm {g} _ {\mu \kappa} - \mathrm {g} _ {\lambda \kappa} \mathrm {g} _ {\mu \nu}\right) \mathrm {R} \\ \end{array}
$$

is also called the conformal tensor due to its invariance under conformal transformations. It vanishes if and only if the metric is conformally flat (i.e. reducible to Minkowski space by a conformal transformation).

The extrinsic curvature tensor of a hypersurface which has unit normal $\mathbf{n}$ and which is spanned by basis vectors $\mathbf{e}_i, \mathbf{e}_j \cdots$ is denoted $\mathbf{K}$ , with

components

$$
\mathbf {K} _ {\mathrm {i j}} = - \mathbf {e} _ {\mathrm {j}} \cdot \nabla_ {\mathrm {i}} \mathbf {n}.
$$

Problem 9.1. On a sphere of radius $a$ try to construct a local Cartesian system in two ways (a) from geodesics and (b) from the (orthogonal) lines of longitude and latitude. Either way there will be deviations from a good Cartesian system (e.g. the sum of the angles in a coordinate box will differ from $2\pi$ , or the fractional difference in length between "parallel" sides of a coordinate box will not vanish). Show that such deviations are of order [Area of coordinate patch/a²].

Problem 9.2. How many independent components does the Riemann tensor have in $\mathbf{n}$ dimensions?

Problem 9.3. Mathematical manipulations with the Riemann tensor are often done with computers. Rather than calculate and store the $4^4 = 256$ components of the tensor as $\mathbf{R}(\mathbf{I},\mathbf{J},\mathbf{K},\mathbf{L})$ with $\mathbf{I},\mathbf{J},\mathbf{K},\mathbf{L} = 0,1,2,3$ , the symmetries of the Riemann tensor can be used to reduce the size of the stored array. Design a subprogram which stores or recalls all components of $\mathbf{R}(\mathbf{I},\mathbf{J},\mathbf{K},\mathbf{L})$ in a linear array of dimensions $\leq 21$ .

Problem 9.4. Compute all the nonvanishing components of the Riemann tensor $\mathbf{R}_{\mathrm{ijk1}}(\mathrm{i},\mathrm{j},\mathrm{k},\mathrm{l} = \theta ,\phi)$ for the 2-sphere metric

$$
\mathrm {d s} ^ {2} = \mathrm {r} ^ {2} (\mathrm {d} \theta^ {2} + \sin^ {2} \theta \mathrm {d} \phi^ {2}).
$$

Problem 9.5. Find the Christoffel symbols and Riemann curvature components for the two dimensional spacetime:

$$
\mathrm {d s} ^ {2} = \mathrm {d v} ^ {2} - \mathrm {v} ^ {2} \mathrm {d u} ^ {2}.
$$

Problem 9.6. Set up a coordinate system on a torus (the 2-dimensional surface of a doughnut in Euclidean 3-space). Calculate all components of $\mathbf{g}_{\mu \nu}$ , $\Gamma_{\alpha \beta}^{\mu}$ and $\mathbb{R}_{\alpha \beta \gamma \delta}$ .

Problem 9.7. In a space of fewer than 4 dimensions simple expressions can be given for the Riemann tensor.

(a) What is the Riemann tensor in a 1-dimensional space?

(b) Express the Riemann tensor for a 2-dimensional space in terms of the metric and the Ricci scalar.   
(c) Express the Riemann tensor for a 3-dimensional space in terms of the metric and the Ricci tensor.

Problem 9.8. Prove the relation

$$
2 \mathrm {V} _ {a; [ \nu \kappa ]} \equiv \mathrm {V} _ {a; \nu \kappa} - \mathrm {V} _ {a; \kappa \nu} = \mathrm {V} _ {\sigma} \mathrm {R} _ {a \nu \kappa} ^ {\sigma}
$$

and find its generalization to the commutator of second derivatives for a tensor of arbitrary rank $\mathbf{T}_{\alpha \ldots}^{\beta \ldots}$ .

Problem 9.9. Show that the second derivatives of a scalar field commute (i.e. show that $\mathbf{S}_{;a\beta} = \mathbf{S}_{;b\alpha}$ ). For third derivatives $\mathbf{S}_{;a\beta\gamma}$ , compute $\mathbf{S}_{;(a\beta)\gamma}$ and $\mathbf{S}_{;a[\beta\gamma]}$ .

Problem 9.10. Prove that for any second rank tensor

$$
\mathrm {A} _ {; \mu \nu} ^ {\mu \nu} = \mathrm {A} _ {; \nu \mu} ^ {\mu \nu}.
$$

Problem 9.11. An infinitesimal circuit in the shape of a parallelogram can be specified by the differential displacements $\mathbf{u}$ , $\mathbf{v}$ representing the sides of the parallelogram. Let a vector $\mathbf{A}$ be parallel transported around this circuit. (i.e. Displace it successively by $\mathbf{u}$ , $\mathbf{v}$ , $-\mathbf{u}$ , $-\mathbf{v}$ .) Show that the change in $\mathbf{A}$ due to the transport around this circuit is

$$
\delta \mathbf {A} ^ {\alpha} = - \mathbf {R} _ {\beta \gamma \delta} ^ {\alpha} \mathbf {A} ^ {\beta} \mathbf {u} ^ {\gamma} \mathbf {v} ^ {\delta}.
$$

Problem 9.12. Riemann curvature can also be computed with the Riemann operator $\mathbf{R}$

$$
\mathbf {R} (\mathbf {A}, \mathbf {B}) \mathbf {C} = (\nabla_ {\mathbf {A}} \nabla_ {\mathbf {B}} - \nabla_ {\mathbf {B}} \nabla_ {\mathbf {A}} - \nabla_ {[ \mathbf {A}, \mathbf {B} ]}) \mathbf {C}
$$

(a) Show that the value of $\mathbf{R}$ at a point $\mathbf{P}$ is linear in the arguments $\mathbf{A}, \mathbf{B}, \mathbf{C}$ and depends only on their values at $\mathbf{P}$ and not on the way in which they vary around $\mathbf{P}$ .

(b) Show that

$$
(\mathbf {R} (\mathbf {A}, \mathbf {B}) \mathbf {C}) ^ {\alpha} = \mathbf {R} _ {\mu \lambda \sigma} ^ {\alpha} \mathbf {C} ^ {\mu} \mathbf {A} ^ {\lambda} \mathbf {B} ^ {\sigma}.
$$

Problem 9.13. Two nearby geodesics have affine parameters such that nearby points on the two geodesics have very close values of affine parameter $\lambda$ . Let $u^{\alpha} \equiv dx^{\alpha} / d\lambda$ be the tangent to one of the geodesics, and let $\mathbf{n}$ be the differential vector connecting points of equal affine parameter on the two geodesics. Prove the equation of geodesic deviation

$$
\frac {\mathrm {D} ^ {2} \mathrm {n} ^ {\alpha}}{\mathrm {d} \lambda^ {2}} + \mathrm {R} ^ {\alpha} _ {\beta \gamma \delta} \mathrm {u} ^ {\beta} \mathrm {n} ^ {\gamma} \mathrm {u} ^ {\delta} = 0.
$$

Problem 9.14. In a suitable coordinate system the gravitational field of the Earth is approximately (to lowest nontrivial order in $\mathbf{M} / \mathbf{r}$ )

$$
\begin{array}{l} \mathrm {d s} ^ {2} = - (1 - 2 \mathrm {M} / \mathrm {r}) \mathrm {d t} ^ {2} + (1 + 2 \mathrm {M} / \mathrm {r}) (\mathrm {d x} ^ {2} + \mathrm {d y} ^ {2} + \mathrm {d z} ^ {2}) \\ r \equiv (x ^ {2} + y ^ {2} + z ^ {2}) ^ {\frac {1}{2}} \\ \mathbf {M} = \text {m a s s o f E a r t h} (\mathbf {c} = \mathbf {G} = 1). \\ \end{array}
$$

Suppose a Skylab satellite orbits the Earth in a circular equatorial orbit. What is the orbital period? An astronaut jettisons a bag of garbage into a nearby orbit and watches it move relative to the satellite. At a given time the separation of the Skylab and its garbage is described by the vector

$$
\xi^ {\mathrm {i}} \equiv \mathrm {x} ^ {\mathrm {i}} (\text {g a r b a g e}) - \mathrm {x} ^ {\mathrm {i}} (\text {s k y l a b}).
$$

Using the equation of geodesic deviation, find the components of the relative motion $\xi^{\mathbf{i}}$ as a function of time.

Problem 9.15. Prove the cyclic identity

$$
\mathrm {R} _ {a \beta \gamma \delta} + \mathrm {R} _ {a \delta \beta \gamma} + \mathrm {R} _ {a \gamma \delta \beta} = 0
$$

and the Bianchi identities

$$
\mathrm {R} _ {a \delta \beta \gamma ; \nu} + \mathrm {R} _ {a \delta \nu \beta ; \gamma} + \mathrm {R} _ {a \delta \gamma \nu ; \beta} = 0.
$$

Problem 9.16. Show that Bianchi identities imply that the Einstein tensor

$$
\mathsf {G} _ {\mu \nu} \equiv \mathsf {R} _ {\mu \nu} - \frac {1}{2} \mathsf {g} _ {\mu \nu} \mathsf {R}
$$

has vanishing divergence (i.e. $\mathbf{G}_{\nu ;\mu}^{\mu} = 0$ ).

Problem 9.17. Show that the vanishing of the Riemann tensor is a sufficient condition for a spacetime to be Minkowskiian, i.e., a coordinate transformation will bring $\mathbf{g}_{\mu \nu}$ into the form $\eta_{\mu \nu}$ .

Problem 9.18. A beam of light has a circular cross section at some point along its path. Show that the beam experiences no shear (i.e. the cross-section is not deformed into an ellipse) when the Weyl tensor is zero.

Problem 9.19. Compute the Riemann tensor, Ricci tensor, and scalar curvature of the conformally-flat metric $\mathbf{g}_{\mu \nu} = \mathrm{e}^{2\phi}\eta_{\mu \nu}$ where $\phi = \phi (\mathbf{x}^{\mu})$ is an arbitrary function.

Problem 9.20. Compute the Riemann tensor of the following metric in an orthonormal frame:

$$
\begin{array}{l} \mathrm {d s} ^ {2} = - \mathrm {e} ^ {2 \alpha} \mathrm {d t} ^ {2} + \mathrm {e} ^ {2 \beta} \mathrm {d r} ^ {2} + \mathrm {e} ^ {2 \gamma} (\mathrm {d} \theta^ {2} + \sin^ {2} \theta \mathrm {d} \phi^ {2}) \\ \alpha , \beta , \gamma = \text {f u n c t i o n s} \mathrm {r}, \mathrm {t}. \\ \end{array}
$$

What is the Ricci tensor for this metric? The scalar curvature? The Einstein tensor?

Problem 9.21. Consider a Riemann tensor representing a plane gravitational wave, i.e. $\mathbf{R}_{\alpha \beta \gamma \delta} = \mathbf{R}_{\alpha \beta \gamma \delta}(\mathfrak{u})$ , where $\mathfrak{u}$ is "retarded time" ( $\nabla \mathbf{u} \cdot \nabla \mathbf{u} = 0$ ). Find the number of independent components of such a Riemann tensor. Do not assume that $\mathbf{R}_{\alpha \beta \gamma \delta}$ satisfies the Einstein field equations.

Problem 9.22. At a given instant, the coordinate accelerations of $n$ nearby test particles are measured. What is the smallest $n$ required to measure all components of $\mathbf{F}^{\mu \nu}$ ? of $\mathbf{R}_{\nu \rho \sigma}^{\mu}$ ?

Problem 9.23. Let $\mathbf{A}$ and $\mathbf{B}$ be two linearly independent vectors tangent at a point to a two-dimensional surface, in a space of dimension $\geq 2$ . The Riemannian curvature of the 2-surface at that point is defined as

$$
K = \frac {R _ {\alpha \gamma \beta \delta} A ^ {\alpha} A ^ {\beta} B ^ {\gamma} B ^ {\delta}}{\left(g _ {\alpha \beta} g _ {\gamma \delta} - g _ {\alpha \delta} g _ {\beta \gamma}\right) A ^ {\alpha} A ^ {\beta} B ^ {\gamma} B ^ {\delta}}.
$$

Show that $\mathbf{K}$ is unchanged if $\mathbf{A}$ and $\mathbf{B}$ are replaced by linear combinations of $\mathbf{A}$ and $\mathbf{B}$ .

Problem 9.24. Suppose $\mathbf{K}$ is the curvature at a point in a 2-dimensional surface, as defined in Problem 9.23. If $\mathbf{A}$ and $\mathbf{B}$ are two vectors tangent at a point to the two surface, and $\mathbf{A}$ is parallel transported around a small circuit lying in the 2-surface, show that the change in the angle between

A and B is of magnitude

$$
\Delta \theta = | K \Delta \Sigma |
$$

where $\Delta \Sigma$ is the area enclosed by the circuit.

Problem 9.25. Suppose that the curvature $\mathbf{K}$ at a point $\mathbf{P}$ , as defined in Problem 9.23, does not depend on the 2-surface which is chosen through that point. Show then that

$$
\mathrm {R} _ {a \beta \gamma \delta} = \mathrm {K} (\mathrm {g} _ {a \gamma} \mathrm {g} _ {\beta \delta} - \mathrm {g} _ {a \delta} \mathrm {g} _ {\beta \gamma}) .
$$

Problem 9.26. If the Riemann curvature is isotropic, the Riemann curvature tensor can be written as

$$
\mathrm {R} _ {a \beta \gamma \delta} = \mathrm {K} (\mathrm {g} _ {a \gamma} \mathrm {g} _ {\beta \delta} - \mathrm {g} _ {a \delta} \mathrm {g} _ {\beta \gamma}).
$$

Use the Bianchi identities to show (Schur's theorem) that $\mathbf{K}$ must be a constant.

Problem 9.27. Show that a space is conformally flat if the Riemann tensor can be written as

$$
\mathrm {R} _ {\lambda \mu \nu \kappa} = \mathrm {K} (\mathbf {g} _ {\lambda \nu} \mathbf {g} _ {\mu \kappa} - \mathbf {g} _ {\lambda \kappa} \mathbf {g} _ {\mu \nu}) .
$$

![](images/fc1d86d54c5745eaf9dbdb82e3cf2f949dc00c121b17f48296920fd93a672fc2.jpg)

Problem 9.28. Suppose at a point $\mathbf{q}$ in a 3-surface $\Sigma$ two curves are tangent (i) $C_{\Sigma}$ a curve in the 3-surface and (ii) $C$ a geodesic of the 4-dimensional space in which $\Sigma$ is embedded. Let $\mathbf{n}$ be the unit normal to $\Sigma$ . The vector $\xi^{\alpha} = \frac{1}{2}\mathbf{u}^{\alpha};\beta \mathbf{u}^{\beta}$ (where $\mathbf{u}$ is the tangent vector to $C_{\Sigma}$ ) measures the rate at which $C$ and $C_{\Sigma}$ separate. Show that the rate of separation $\mathbf{n} \cdot \boldsymbol{\xi}$ is

$$
\mathbf {n} \cdot \boldsymbol {\xi} = \frac {1}{2} K _ {\alpha \beta} u ^ {\alpha} u ^ {\beta}
$$

where $\mathbf{K}_{\alpha \beta}$ is the extrinsic curvature tensor for $\pmb{\Sigma}$ .

Problem 9.29. What is the extrinsic curvature of the $\tau =$ constant slice of the metric, $\mathrm{ds}^2 = -\mathrm{d}\tau^2 + \mathrm{a}^2(\tau) [\gamma_{ij}(\mathbf{x}^k) \mathrm{dx}^i \mathrm{dx}^j]$ ?

Problem 9.30. Prove that the extrinsic curvature of a timelike hypersurface with unit normal vector $\mathbf{n}$ is $-\frac{1}{2} \mathcal{L}_{\mathbf{n}} \mathbf{P}_{\alpha \beta}$ , where $\mathbf{P}_{\alpha \beta} = \mathbf{g}_{\alpha \beta} - \mathbf{n}_{\alpha} \mathbf{n}_{\beta}$ is the projection tensor into the hypersurface.

Problem 9.31. If we neglect gravity, the potential energy due to surface tension of a soap film is proportional to its area. Thus in equilibrium a

soap film spanning a fixed closed wire loop will assume a shape of minimum area. Show that this implies that the surface is one whose “mean curvature” $\mathbf{K} \equiv \mathbf{K}_{\mathbf{i}}^{\mathbf{i}}$ is zero.

Problem 9.32. Let $\mathbf{n}$ be the unit normal to a hypersurface $\Sigma$ , with $\mathbf{n} \cdot \mathbf{n} \equiv \varepsilon = +1$ or $-1$ if $\Sigma$ is timelike or spacelike respectively. In Gaussian normal coordinates (see Problem 8.25) based on $\Sigma$ , the metric is

$$
d s ^ {2} = \varepsilon d n ^ {2} + ^ {(3)} g _ {i j} d x ^ {i} d x ^ {j}.
$$

Derive the Gauss-Codazzi equations

$$
\begin{array}{l} { } ^ { ( 4 ) } \mathrm { R } _ { i j k } ^ { m } = { } ^ { ( 3 ) } \mathrm { R } _ { i j k } ^ { m } + \varepsilon \left( \mathrm { K } _ { i j } \mathrm { K } _ { k } ^ { m } - \mathrm { K } _ { i k } \mathrm { K } _ { j } ^ { m } \right) \\ \left(^ {(4)} \mathrm {R} _ {\mathrm {i j k}} ^ {\mathrm {n}} = \varepsilon \left(\mathrm {K} _ {\mathrm {i k} | \mathrm {j}} - \mathrm {K} _ {\mathrm {i j} | \mathrm {k}}\right) \right.. \\ \end{array}
$$

Here 4 and 3 refer respectively to the spacetime geometry and to the geometry of $\Sigma$ ; a slash denotes covariant differentiation with respect to ${}^{(3)}\mathbf{g}_{ij}$ ; the $\mathbf{n}$ index denotes the component on the $\mathbf{n}$ basis vector. Also derive the equation for the remaining component of the Riemann tensor:

$$
{ } ^ { ( 4 ) } \mathbf { R } _ { \text { i n k } } ^ { \mathbf { n } } = \varepsilon \left( \mathrm { K } _ { \mathrm { i k } , \mathrm { n } } + \mathrm { K } _ { \mathrm { i m } } \mathrm { K } _ { \mathrm { k } } ^ { \mathbf { m } } \right) .
$$

Problem 9.33. Using the results of Problem 9.32, derive expressions for ${}^{(4)}\mathbf{G}_{\beta}^{\alpha}$ , the components of the Einstein tensor, in Gaussian normal coordinates.

Problem 9.34. The eigenvalues and eigenvectors of the extrinsic curvature tensor are called the principal curvatures and principal directions. Find the principal curvatures and directions for the following surfaces embedded in a 3-dimensional Euclidean space.

(i) sphere: $\mathbf{x}^2 + \mathbf{y}^2 + \mathbf{z}^2 = \mathbf{a}^2$ .   
(ii) cylinder: $x^2 + y^2 = a^2$ .   
(iii) quadratic surface (compute at origin only): $z = \frac{1}{2} (\mathrm{ax}^2 + 2\mathrm{bxy} + \mathrm{cy}^2)$ .

Problem 9.35. Show that if $\Sigma$ is a 2-dimensional surface in a flat 3-space, then the scalar curvature of $\Sigma$ is

$$
{ } ^ { ( 2 ) } \mathbf { R } = \frac { 2 } { \rho _ { 1 } \rho _ { 2 } }
$$

where $\rho_{1}$ and $\rho_{2}$ are the principal radii of curvature of $\Sigma$ . What is the analogous formula for a 3-surface embedded in a flat 4-space?

# CHAPTER 10

# KILLING VECTORS AND SYMMETRIES

Suppose that a geometry has a symmetry such that a vector field $\xi$ exists with the following property: If any set of points is displaced by $\xi d\lambda$ (d $\lambda$ a small number) then all distance relationships are unchanged. The vector field is then called a Killing vector for the geometry, and it satisfies Killing's equation

$$
\xi_ {(\alpha ; \beta)} \equiv \frac {1}{2} \left[ \xi_ {\alpha ; \beta} + \xi_ {\beta ; \alpha} \right] = 0.
$$

0000000000

Problem 10.1. Solve Killing's equations to find the Killing vector fields of the 2-sphere:

$$
\mathrm {d s} ^ {2} = \mathrm {d} \theta^ {2} + \sin^ {2} \theta \mathrm {d} \phi^ {2}.
$$

Problem 10.2. Show that Killing's equation $\xi_{\alpha;\beta} + \xi_{\beta;\alpha} = 0$ is equivalent to $\mathcal{L}_{\pmb{\xi}}\mathbf{g} = 0$ , where $\mathbf{g}$ is the metric tensor. Interpret this result geometrically.

# Problem 10.3.

(a) Show that the commutator of two Killing vector fields is a Killing vector field.   
(b) Show that a linear combination of Killing vectors with constant coefficients is a Killing vector.

Problem 10.4. In Euclidean 3-space show that the 3 Killing vectors describing rotations around the $x, y$ , and $z$ axes are linearly dependent at any given point but that no constant coefficient combination of them is zero. Show that the generators of the rotation group $O(3)$ are thus 2-surface forming, even though the group is 3-dimensional. Explain.

Problem 10.5. The metric for an axially symmetric rotating star admits two Killing vectors, $\pmb{\xi}_{(t)}$ and $\pmb{\xi}_{(\phi)}$ . Assume there are no other independent Killing vectors. Prove that $\pmb{\xi}_{(t)}$ and $\pmb{\xi}_{(\phi)}$ commute.

Problem 10.6. Show that any Killing vector is a solution of the equation

$$
\xi_ {; \lambda} ^ {\nu ; \lambda} + \mathrm {R} _ {\sigma} ^ {\nu} \xi^ {\sigma} = 0.
$$

Find a Lagrangian-type variational principle from which this equation can be derived.

Problem 10.7. If $\pmb{\xi}$ is a Killing vector, prove that

$$
\xi_ {\mu ; \alpha \beta} = \mathsf {R} _ {\gamma \beta \alpha \mu} \xi^ {\gamma}.
$$

Problem 10.8. A metric is "stationary" if and only if it has a Killing vector field $\xi$ which is timelike at infinity (the "time" direction is $\partial/\partial t$ ). There are two ways to define a "static" metric:

(i) stationary and invariant under time reversal, $\partial/\partial t \to -\partial/\partial t$ , or   
(ii) stationary and $\partial/\partial t$ is hypersurface orthogonal (see Problem 7.23). Show that the two definitions are equivalent.

Problem 10.9. In flat Minkowski spacetime find ten Killing vectors that are linearly independent.

Problem 10.10. If $\pmb{\xi}(\mathbf{x}^{\mu})$ is a Killing vector field and $\mathbf{u}$ is the tangent vector to a geodesic, show that $\pmb{\xi} \cdot \mathbf{u}$ is constant along the geodesic.

Problem 10.11. If $\xi$ is a Killing vector and $\mathbf{T}$ is the stress-energy tensor, show that $\mathrm{J}^{\mu} \equiv \mathrm{T}^{\mu \nu} \xi_{\nu}$ is a conserved quantity i.e. $\mathrm{J}_{; \mu}^{\mu} = 0$ . Interpret $\mathbf{J}$ when $\xi$ is a timelike Killing vector.

Problem 10.12. If $\mathbf{T}$ is the energy-momentum tensor, and $\pmb{\xi}$ is a time Killing vector, show that the integral over a whole spacelike hypersurface

$$
\int_ {\mathbf {F}} \mathbf {T} _ {\beta} ^ {\alpha} \xi^ {\beta} \mathrm {d} ^ {3} \Sigma_ {\alpha}
$$

is independent of the choice of spacelike hypersurface F.

Problem 10.13. Given a divergenceless stress energy tensor in flat spacetime, i.e.

$$
\mathrm {T} _ {; \nu} ^ {\mu \nu} = 0 \quad \mathrm {R} _ {\alpha \beta \gamma \delta} = 0
$$

show that one may construct ten global conservation laws and hence ten conserved quantities.

Problem 10.14. If $\pmb{\xi}$ is a timelike Killing vector and $\mathbf{u} = \pmb{\xi} / |\pmb{\xi} \cdot \pmb{\xi}|^{\frac{1}{2}}$ is a 4-velocity, prove that $\mathbf{a} \equiv \nabla_{\mathbf{u}} \mathbf{u} = \frac{1}{2} \nabla \log |\pmb{\xi} \cdot \pmb{\xi}|$ .

Problem 10.15. In a stationary metric with time Killing vector $\xi$ the "energy at infinity" $\mathbf{E} = -\mathbf{p} \cdot \boldsymbol{\xi}$ of a test particle with 4-momentum $\mathbf{p}$ is conserved. Find the minimum value of $\mathbf{E} / \mu$ (where $\mu =$ particle mass) that the particle can have at a given point in the spacetime, in terms of the norm of $\boldsymbol{\xi}$ .

Problem 10.16. Show that a Killing vector is an admissible solution for the vector potential of Maxwell's equations for a test field in a vacuum spacetime. What electromagnetic field corresponds to the Killing vector $\partial/\partial\phi$ in Minkowski space?

# CHAPTER 11 ANGULAR MOMENTUM

This chapter contains problems dealing with rotation, angular momentum, spin, etc. in general relativity. Definitions are developed in the problems.

Problem 11.1. In special relativity, when a particle is at an event B and has 4-momentum p, its angular momentum about event A is

$$
\mathbf {J} = \Delta \mathbf {x} \otimes \mathbf {p} - \mathbf {p} \otimes \Delta \mathbf {x}
$$

where $\pmb{\Delta}\mathbf{x}$ is the 4-vector from event A to event B

(i) Show that for a freely moving (i.e. unaccelerated) particle $\mathbf{J}$ is conserved - i.e. $\mathrm{d}\mathbf{J} / \mathrm{d}\tau = 0$   
(ii), Suppose that several particles

![](images/400037e0d3c3af84478eeed57d9d0f4fa4399a0b44a3715dbd2d8fd2346873c4.jpg)

collide at an event B, thereby producing several other particles. Show that the sum of the angular momenta of the particles about an event A is the same after the collision as before:

$$
\sum_ {(\mathbf {k})} \left. \mathbf {J} _ {(\mathbf {k})} \right| _ {\text {a f t e r}} = \sum_ {(\mathbf {k})} \left. \mathbf {J} _ {(\mathbf {k})} \right| _ {\text {b e f o r e}}.
$$

Problem 11.2. Show

(a) that the total angular momentum of an isolated system in flat

space

is a conserved tensor (when $\mathbf{T}^{\alpha \beta},\beta = 0)$ , but

(b) that it is not invariant under the coordinate translation $\mathbf{x}^{\alpha} \rightarrow \mathbf{x}^{\alpha} + \mathbf{a}^{\alpha}$ . Show also that

(c) the spin 4-vector defined by

$$
\mathbf {S} _ {\alpha} \equiv - \frac {1}{2} \varepsilon_ {\alpha \beta \gamma \delta} \mathbf {J} ^ {\beta \gamma} \mathbf {u} ^ {\delta}
$$

is both conserved and

(d) invariant under translations. Here $\mathfrak{u}^{\alpha}$ is the "center of mass 4-velocity" $\mathfrak{u}^{\alpha} \equiv \mathbb{P}^{\alpha} / (-\mathbb{P}^{\beta} \mathbb{P}_{\beta})^{\frac{1}{2}}$ and $\mathbb{P}^{\alpha}$ is the total momentum $\mathbb{P}^{\alpha} \equiv \int \mathrm{d}^{3} \mathbf{x} \mathbf{T}^{\alpha 0}$ .

Problem 11.3. Show that a system's intrinsic spin 4-vector $\mathbf{S}_{\alpha}$ is orthogonal to its 4-velocity $\mathbf{u}^{\alpha}$ .

Problem 11.4. Show that a gyroscope with no applied torques Fermi-Walker transports its spin vector.

Problem 11.5.

(a) If angular momentum is computed about the center of mass of a system show that $\mathbf{J}^{\alpha \beta}\mathbf{u}_{\beta} = 0$   
(b) In this case show that the angular momentum ("intrinsic angular momentum") can be found from the spin vector as

$$
\mathbf {J} _ {\mathbf {(C . M .)}} ^ {\alpha \beta} \equiv \mathsf {S} ^ {\alpha \beta} = - \varepsilon^ {\alpha \beta \gamma \delta} \mathsf {S} _ {\gamma} \mathsf {u} _ {\delta} \mathrm {.}
$$

Problem 11.6. Two bodies A and B have momenta $\mathbf{P}_{\mathbf{A}}$ and $\mathbf{P}_{\mathbf{B}}$ and spin $\mathbf{S}_{\mathbf{A}}$ and $\mathbf{S}_{\mathbf{B}}$ ; their centers of mass are on a collision course. After

colliding they stick together to form a composite body C (spin $\mathbf{S}_{\mathbf{C}}$ ). Calculate $\mathbf{S}_{\mathbf{C}}$ in terms of $\mathbf{P}_{\mathbf{A}}, \mathbf{P}_{\mathbf{B}}, \mathbf{S}_{\mathbf{A}}$ and $\mathbf{S}_{\mathbf{B}}$ .

Problem 11.7. Thomas Precession: Consider a ("classical") spinning electron which Fermi-Walker transports its spin angular momentum, S, as it moves in a circular orbit around an atomic nucleus. As seen in the laboratory frame, the electron moves in a circular orbit of radius r in the x-y plane with constant angular velocity, $\omega$ . Calculate S(t), the spin as a function of laboratory time.

Problem 11.8. A nonspherical spinning body in an inhomogeneous gravitational field experiences a torque which causes its intrinsic spin 4-vector S to change with time. If $\mathbf{u}$ is the 4-velocity of the center of mass of the object, freely moving along a geodesic, show that

$$
\frac {\mathrm {D S} ^ {\kappa}}{\mathrm {d} \tau} = \varepsilon^ {\kappa \beta \alpha \mu} u _ {\mu} u ^ {\sigma} u ^ {\lambda} t _ {\beta \eta} R ^ {\eta} _ {\sigma \alpha \lambda}.
$$

Here $\mathfrak{t}\beta \eta$ is the "reduced quadrupole moment tensor" $\mathfrak{t}^{\mathrm{ij}} = \int \rho (\mathbf{x}^{\mathrm{i}}\mathbf{x}^{\mathrm{j}} - \frac{1}{3}\mathbf{r}^{2}\delta^{\mathrm{ij}})\mathbf{d}^{3}\mathbf{x}$ in the rest frame of the center of mass, $\mathfrak{t}^{\alpha \beta}\mathfrak{u}_{\alpha} = 0$ and the Riemann tensor is generated externally to the body in question and is assumed to be approximately constant over the body.

Problem 11.9. Calculate the period of precession of the Earth's axis due to the coupling of tidal forces from the sun and moon with the quadrupole moment of the (slightly nonspherical) Earth.

Problem 11.10. Consider a family of stationary observers in a stationary spacetime, i.e. their 4-velocity is proportional to the time Killing vector $\pmb{\xi}$ . Each observer arranges his spatial basis vectors so that they connect to the same neighboring observers for all time $t$ , where $\pmb{\xi} = \frac{\partial}{\partial t}$ .

(1) Show that $\mathcal{L}_{\pmb{\xi}} \mathbf{e}_{\widehat{\alpha}} = 0$ , where $\mathbf{e}_{\alpha}$ is a basis vector of the stationary observer.   
(2) Show that the rate of change of the components of any tensor quantity $Q$ as measured by the stationary observer in units of $t$ , is

$$
\frac {\mathrm {d} Q}{\mathrm {d} t} ^ {\hat {\alpha} \dots \hat {\beta}} = (\mathcal {Q} _ {\boldsymbol {\xi}} Q) ^ {\hat {\alpha} \dots \hat {\beta}}. \text {W h a t i s} \frac {\mathrm {d} Q}{\mathrm {d} \hat {t}} ^ {\hat {\alpha} \dots \hat {\beta}}?
$$

(3) The stationary observer carries a gyroscope with him applying no torques to it. Show that the gyroscope's spin vector precesses (Lens-Thirring effect) with an angular velocity relative to the stationary observer, as measured in units of proper time,

$$
\omega^ {a} = \frac {\varepsilon^ {a \nu \sigma \lambda} \xi_ {\nu} \xi_ {\sigma ; \lambda}}{2 \xi^ {\gamma} \xi_ {\gamma}}.
$$

(4) Show that $\omega = 0$ if the spacetime is static, and not merely stationary.

Problem 11.11. A gyroscope is placed in a circular orbit about the Earth and no torques are applied to it. What is the angular velocity of precession for its spin vector relative to a reference frame fixed with respect to the distant stars? ("geodetic precession" and "Lens-Thirring effect").

# CHAPTER 12 GRAVITATION GERELY

This chapter contains problems dealing with the physical consequences of gravitational interactions. Most of the problems use the Newtonian limit, in which gravity is represented by a scalar potential $\mathbf{U}$ satisfying

$$
\nabla^ {2} \mathbf {U} = - 4 \pi \rho
$$

and generating a gravitational acceleration

$$
\underline {{\mathbf {g}}} = \nabla \mathbf {U} .
$$

(Alternatively, one sometimes uses a potential $\Phi \equiv -\mathbf{U}$ .) Tidal forces depend on $\partial^2\Phi/\partial x^i\partial x^k$ in Newtonian theory; these forces appear as the $R_{j0k0}$ terms of the Riemann tensor in the appropriate limit of the equation of geodesic deviation in general relativity. Some of the problems explore consequences of gravity's spin-2 nature, and of its weakness in comparison to other fields.

00000000

Problem 12.1. A small satellite has a circular frequency $\omega$ in an orbit of radius $r$ about a central object of mass $m$ . From the known value of $\omega$ show that it is possible to determine neither $r$ nor $m$ individually, but only the effective "Kepler density" $3m / 4\pi r^3$ of the object as averaged over a sphere of the same radius as the orbit. Give the formula for $\omega^2$ in terms of this Kepler density.

Problem 12.2. Estimate the height of spring tides and neap tides.

Problem 12.3. If the amplitude of solid-earth tides as a function of time is fourier transformed, there are peaks at certain frequencies. What are the frequencies (or periods) of the 10 strongest peaks?

Problem 12.4. The position of the sun in the sky can in principle be measured by a sensitive tidal gravimeter. What is the angular difference between this position and its position as measured optically? If the actual position of the sun were at its optical position, there would be a force in the direction of the earth's motion. (Why?) If this were the case find the radius of the earth's orbit as a function of time.

Problem 12.5. The "Eddington limit" for the luminosity of a star of mass $M$ is defined as the luminosity at which outward light pressure just balances inward gravitational force everywhere within the star. Calculate the luminosity. (You may assume that all matter is fully ionized hydrogen.)

Problem 12.6. Show that an electron does not fall down when released in the center of an evacuated perfectly conducting closed container in a uniform gravitational field. ("Perfect conductor") $\equiv$ perfectly rigid positive lattice with perfectly mobile conduction electrons.)

Problem 12.7. A tall, cylindrical, insulated bottle of height $h$ is filled with air at $300^0\mathrm{K}$ . It is then sealed and set on a scale at sea level. The scale reads a weight $W$ . For what range of $h$ does the weight $W$ decrease as the contents of the bottle are slowly heated.

Problem 12.8. Define a stress tensor for the Newtonian gravitational potential $\mathbf{U}$ as follows:

$$
\mathbf {T} _ {\mathrm {j k}} \equiv \frac {1}{4 \pi} \left(\mathbf {U} _ {, \mathrm {j}} \mathbf {U} _ {, \mathrm {k}} - \frac {1}{2} \delta_ {\mathrm {j k}} \mathbf {U} _ {, \mathrm {n}} \mathbf {U} ^ {, \mathrm {n}}\right) .
$$

Show that the Newtonian equations of motion for stressed matter with proper density $\rho_0$ and velocity $\underline{\mathbf{v}}$ can be written in the form

$$
\rho_ {0} \frac {\mathrm {d} \mathbf {v} _ {\mathrm {j}}}{\mathrm {d} t} = - \frac {\partial}{\partial \mathbf {x} ^ {\mathrm {k}}} \left(\mathbf {T} _ {\mathbf {j k}} + \mathbf {t} _ {\mathbf {j k}}\right)
$$

$$
\left(\rho_ {0} \mathrm {v} _ {\mathrm {j}}\right), \mathrm {t} + \left(\mathrm {T} _ {\mathrm {j k}} + \mathrm {t} _ {\mathrm {j k}} + \rho_ {0} \mathrm {v} _ {\mathrm {j}} \mathrm {v} _ {\mathrm {k}}\right), \mathrm {k} = 0,
$$

where $t_{jk}$ is the ordinary 3-dimensional stress tensor.

Problem 12.9. Consider an extended body of mass $\mathbf{M}$ with several forces $\underline{\mathbf{F}}_{i}$ acting on it. Using the equivalence of gravitational mass and energy show that the condition for equilibrium of the body is

$$
\sum \underline {{F}} _ {i} \left(1 - \underline {{g}} \cdot \underline {{x}} _ {i} / c ^ {2}\right) = - M g
$$

where $\underline{\mathbf{g}}$ is the acceleration of gravity and $\underline{\mathbf{x}}_i$ denotes the point of application of each of the forces, measured in a local Lorentz frame.

Problem 12.10. From the result of Problem 12.9 show that the equation of hydrostatic equilibrium in a star is

$$
\frac {\mathrm {d p}}{\mathrm {d r}} = - \frac {\mathrm {G M} (\mathrm {r})}{\mathrm {r} ^ {2}} \left(\rho + \mathrm {p} / \mathrm {c} ^ {2}\right)
$$

where $\mathbf{M}(\mathbf{r})$ is defined as the "active" mass interior to the fluid shell at radius $r$ . This shows that in a fluid the "effective inertial mass" density is $\rho + p/c^2$ . Notice that this result does not depend on the field equations of general relativity.

Problem 12.11. Show that the Newtonian equation of motion of a test particle in a Newtonian gravitational potential $\Phi$ can be written as a geodesic equation in 4-dimensional spacetime. Compute the Christoffel symbols and the Riemann tensor, and show that they are not derivable from a metric.

Problem 12.12. By examining the relative acceleration of a family of test-particle trajectories in Newtonian gravity and comparing with the Newtonian limit of the equation of geodesic deviation, derive the correspondence

$$
R _ {j 0 k 0} = \frac {\partial^ {2} \Phi}{\partial x ^ {j} \partial x ^ {k}}
$$

between the Newtonian potential and the Riemann tensor. (A Newtonian test particle is acted on only by gravity; a test particle in a relativistic theory of gravity follows a geodesic.)

Problem 12.13. Write a Newtonian gravitational force law in covariant 4-dimensional language, using a scalar field as the universal Newtonian time function. Show that the resulting theory is consistent with special relativity. Show that signals can be sent faster than the speed of light. Is the theory acausal, i.e. can an observer send signals into his own past?

Problem 12.14. Consider two particles of equal mass in a freely falling elevator. One carries a charge $q$ and the other is neutral. There is a vertical electrical field $E$ in the elevator. Write an equation for the separation of the particles as a function of time, including tidal and electrical effects. Reconcile the existence of both terms with the equivalence principle.

Problem 12.15. New particles of mass $\mathfrak{m}_0$ are created which carry a new kind of charge, evidenced by a classical inverse-square force law. A container holds a perfect monatomic gas of these particles in thermal equilibrium. The total charge $Q$ in the container is measured by the average force on test particles outside, and it is observed to vary with temperature as $Q \propto Q_0(1 + 6kT / m_0)$ . What is the spin of the new force field?

Problem 12.16. Show (nonrigorously) that gravity is the only classical, infinite range (massless quanta) pure spin-2 field; i.e. that any other field would couple identically to bulk matter and would thus be indistinguishable from gravity.

Problem 12.17. In “geometrized units of length” (units in which the gravitational constant $G$ , the speed of light $c$ and the Boltzmann constant $k$ are all taken to be unity) give the values of the following, expressed in terms of centimeters: $h$ ; the charge of an electron; $e/m$ for an electron; the mass of the sun; the luminosity of the sun; $300^0\mathrm{K}$ ; one year; one volt.

Problem 12.18. Form "natural" units of mass, length, and time out of the physical constants $\pi$ , $G$ , and $c$ .

Problem 12.19. Estimate the Bohr radius of a "gravitational atom", e.g. two neutrons bound by their gravitational attraction in their lowest energy state.

# CHAPTER 13

# GRAVITATIONAL FIELD EQUATIONS AND LINEARIZED THEORY

The gravitational field, described by the metric of spacetime $\mathbf{g}_{\mu \nu}$ , is generated by the stress-energy $\mathbf{T}^{\mu \nu}$ of matter. Various field equations relating $\mathbf{g}_{\mu \nu}$ to $\mathbf{T}^{\mu \nu}$ have been proposed. The most successful to date are the Einstein equations which are the foundation of general relativity:

$$
\mathrm {G} _ {\mu \nu} \equiv \mathrm {R} _ {\mu \nu} - \frac {1}{2} \mathrm {g} _ {\mu \nu} \mathrm {R} = 8 \pi \mathrm {T} _ {\mu \nu} \tag {1}
$$

where $\mathbf{R}_{\mu \nu}$ and $\mathbf{R}$ are the Ricci tensor and scalar curvature derived from the metric $\mathbf{g}_{\mu \nu}$ , and $\mathbf{G}_{\mu \nu}$ is the Einstein tensor. The equations are nonlinear, since the left hand side is not a linear function of the metric.

Some other (less successful) field equations are discussed in the problems, but unless specifically stated, the Einstein field equations are to be assumed.

The equations of motion $\mathrm{T}^{\mu \nu}$ ; $\nu = 0$ are a consequence of Equation (1). Other desirable properties of $\mathrm{T}^{\mu \nu}$ , called "energy conditions", must be independently postulated on physical grounds.

When the gravitational field is weak, the geometry of spacetime is nearly flat and one writes

$$
\mathbf {g} _ {\mu \nu} = \eta_ {\mu \nu} + \mathrm {h} _ {\mu \nu}
$$

where all $|\mathfrak{h}_{\mu \nu}|$ are $<< 1$ . In this case Equation (1) can be solved approximately, by keeping only first-order terms in $\mathfrak{h}_{\mu \nu}$ . A number of problems make use of this "linearized theory."

![](images/ae8bda5ba00a9097f54794ba6c56535277e5cc98850970d546fd526628213713.jpg)

Problem 13.1. A somewhat generalized form of the Einstein field equations is

$$
R _ {\mu \nu} - a g _ {\mu \nu} R = 8 \pi T _ {\mu \nu}
$$

where $\alpha$ is some dimensionless constant. Show that if $\alpha$ is not $\frac{1}{2}$ the field equations disagree with experiment, even in the Newtonian limit.

Problem 13.2. A metric theory (devised by Nordström in 1913) relates $\mathbf{g}_{\mu \nu}$ to $\mathbf{T}_{\mu \nu}$ by the equations

$$
\mathrm {C} _ {\mu \nu \rho \sigma} = 0
$$

$$
\mathrm {R} = \kappa \mathrm {g} _ {\mu \nu} \mathrm {T} ^ {\mu \nu},
$$

where $\mathbf{C}$ is the Weyl tensor. Show that this theory, in the Newtonian limit and with the proper choice of $\kappa$ , agrees with Newtonian gravitation theory, but that this theory predicts no deflection of starlight passing near the Sun. Does this theory agree with the Pound-Rebka experiments, i.e. are photons redshifted as they rise against the gravitational pull near the surface of the Earth?

Problem 13.3. In the Brans-Dicke theory of gravity (see MTW p. 1070 or Weinberg p. 160 for field equations), the locally measured Newtonian gravitational constant $G$ varies with position and time. Its value at infinity is $G_{\infty}$ . Show that $G$ is a constant inside a self-gravitating spherical shell of mass $M$ and circumference $2\pi R$ . If $R >> G_{\infty}M / c^2$ , express $G$ inside the shell in terms of $G_{\infty}$ , $M$ , and $R$ , to lowest order in $(G_{\infty}M / Rc^2)$ .

Problem 13.4. In relativistic quantum mechanics empty space contains virtual particles. It is speculated that the vacuum therefore, has a nonzero stress-energy.

(1) What form must the vacuum stress-energy tensor take, if there is to be no preferred vacuum frame? Show that there is a resulting term in the field equations which can be interpreted as an effective cosmological constant.

(2) Suppose that the vacuum energy is due to the rest mass of virtual

protons or electrons, produced with an average spacing of their Comp- ton wavelength. Is such vacuum stress-energy ruled out by observa- tions?

(3) Ya. B. Zel'dovich has suggested that the mass-energy density should be associated only with the gravitational interaction energy of nearby virtual particles (separated by their Compton wavelength). What is the predicted magnitude of the vacuum stress energy here? Is it ruled out by observation?

Problem 13.5. In a local region of spacetime, an observer finds that the Ricci curvature scalar is nearly constant, $\mathbf{R} \approx +1 / a^2$ . Why will the sign to be “+?”? If the region of spacetime is filled only with electromagnetic energy what is R?

Problem 13.6. Normally it is assumed that a physically possible $\mathbf{T}^{\mu \nu}$ must satisfy the (weak) energy condition, $\mathbf{T}^{00} \geq 0$ for all physical observers. Assume that $\mathbf{T}^{\mu \nu}$ has a timelike eigenvector; how can a given single observer determine whether the $\mathbf{T}^{\mu \nu}$ he measures satisfies the condition?

Problem 13.7. The "dominant energy condition" on $\mathbf{T}^{\mu \nu}$ requires that the weak energy condition be satisfied (all observers see a nonnegative energy density) and furthermore, that all observers see energy density greater or equal to the magnitude of the energy-flux 3-vector. Show that the statement

$$
\mathbf {u} \cdot (- \mathbf {T}) ^ {\mathbf {n}} \cdot \mathbf {u} \leq 0
$$

for all nonspacelike vectors $\mathbf{u}$ reduces to the weak energy condition for $\mathfrak{n} = 1$ and to the dominant energy condition for $\mathfrak{n} = 2$ . What about $\mathfrak{n} > 2$ ? [Here $(\mathbf{T}^2)_{\mu \nu} \equiv \mathbf{T}_\mu^\sigma \mathbf{T}_{\sigma \nu}$ and so forth.]

Problem 13.8. Is it possible to have a solution of the Einstein field equations in which space is empty to the past of some surface of constant time $t = 0$ , but in which there is a nonvanishing $T_{\mu \nu}$ to the future of this surface?

Problem 13.9. A static metric is generated by a perfect fluid. Show that the fluid 4-velocity is parallel to the time Killing vector.

Problem 13.10. At each point on an initial Cauchy hypersurface how many numbers must be specified, to determine uniquely the evolution of the metric field above that hypersurface. [Hint: First show that only spatial components of the Einstein tensor contain second time derivatives of the metric.]

Problem 13.11. For the "nearly Newtonian" metric

$$
\mathrm {d s} ^ {2} = - (1 + 2 \Phi) \mathrm {d t} ^ {2} + (1 - 2 \Phi) \delta_ {\mathrm {j k}} \mathrm {d x} ^ {\mathrm {j}} \mathrm {d x} ^ {\mathrm {k}}
$$

calculate, to lowest nonvanishing order in $\Phi$ , the components of the Landau-Lifschitz stress-energy pseudotensor $t_{\mathbf{L}\cdot \mathbf{L}}^{\alpha \beta}$ (Landau and Lifschitz p. 306). Assume that the field is changing so slowly in time that time derivatives of $\Phi$ can be neglected compared to spatial derivatives.

Problem 13.12. A gauge transformation is an infinitesimal coordinate transformation which relabels the coordinates of a point $\mathbf{P}$ according to

$$
\mathbf {x} _ {\mathrm {n e w}} ^ {\mu} (\mathbf {P}) = \mathbf {x} _ {\mathrm {o l d}} ^ {\mu} (\mathbf {P}) + \xi^ {\mu} (\mathbf {P}).
$$

Such transformations induce changes, to first order in $\pmb{\xi}$ , of the functional forms of tensors. Find the gauge transformation laws for scalars, and components of vectors and second rank tensors. For the linearized metric perturbations $\mathbf{g}_{\mu \nu} = \eta_{\mu \nu} + \mathrm{h}_{\mu \nu}$ show in particular that

$$
\mathrm {h} _ {\mu \nu} ^ {\mathrm {n e w}} (\mathbf {x}) = \mathrm {h} _ {\mu \nu} ^ {\mathrm {o l d}} (\mathbf {x}) - 2 \xi_ {(\mu , \nu)} .
$$

Problem 13.13. Show that in linearized theory the components of the Riemann tensor are

$$
\mathsf {R} _ {\alpha \mu \beta \nu} = \frac {1}{2} \left(\mathsf {h} _ {\alpha \nu , \mu \beta} + \mathsf {h} _ {\mu \beta , \nu \alpha} - \mathsf {h} _ {\mu \nu , \alpha \beta} - \mathsf {h} _ {\alpha \beta , \mu \nu}\right) .
$$

Also show explicitly that this Riemann tensor is invariant under a gauge transformation.

Problem 13.14. In linearized theory one often uses the "trace reversed" form of the metric perturbations $\overline{\mathbf{h}}_{\alpha}\beta \equiv \mathbf{h}_{\alpha}\beta -\frac{1}{2}\eta_{\alpha \beta}\mathbf{h}_{\sigma}^{\sigma}$ . Show that there always exists a gauge transformation to the "Lorentz gauge", in which the divergence of $\overline{\mathbf{h}}_{\alpha}\beta$ vanishes. Is this gauge transformation unique?

Problem 13.15. Show that in the Lorentz gauge (see Problem 13.14) the linearized field equations reduce to

$$
\square \overline {{{\mathrm {h}}}} _ {\mu \nu} \equiv \overline {{{\mathrm {h}}}} _ {\mu \nu , a}, ^ {\alpha} = - 1 6 \pi \mathrm {T} _ {\mu \nu} ,
$$

where $\overline{\mathbf{h}}_{\mu \nu}$ is trace-reversed $\mathbf{h}_{\mu \nu}$ .

Problem 13.16. In linearized theory a plane gravitational wave propagating in empty spacetime can be represented as the real part of a complex ex

pression

$$
\overline {{\mathrm {h}}} _ {\mu \nu} = \operatorname {R e} \left[ \mathrm {A} _ {\mu \nu} \mathrm {e} ^ {\mathrm {i k} _ {\alpha} \mathrm {x} ^ {\alpha}} \right]
$$

where $\mathbf{A}_{\mu \nu}$ is a constant tensor. Show that $\mathbf{k}$ must be a null vector, and that $\mathbf{A}$ is orthogonal to $\mathbf{k}$ .

For a particular observer with 4-velocity $\mathbf{u}$ the "transverse-traceless" gauge (a further specialization of the Lorentz gauge) is defined in the observer's unperturbed rest frame ( $u^0 = 1$ , $u^i = 0$ ) such that

$$
\overline {{{\mathbf {h}}}} _ {\mu 0} = 0, \qquad \overline {{{\mathbf {h}}}} _ {\mu} ^ {\mu} = 0.
$$

Find the gauge transformation which accomplishes this. Does A remain orthogonal to k?

Problem 13.17. Show that in linearized theory there is no attractive gravitational force between two thin parallel beams of light.

Problem 13.18. A rigid spherical shell of radius $\mathbb{R}$ and total mass $M$ (distributed uniformly on the shell), with negligible thickness, rotates slowly with constant angular velocity $\Omega$ with respect to inertial frames far away. Use the linearized equations of gravity to determine $\omega$ , the

angular velocity of dragging of inertial frames inside the shell, to first order in $\Omega R << 1$ . Show that

$$
\omega \equiv - \frac {\mathbf {g} _ {0} \phi}{\mathbf {g} _ {\phi} \phi} = \frac {4}{3} \frac {\mathbf {M} \Omega}{\mathbf {R}} + \mathcal {O} (\Omega^ {2} \mathbf {R} ^ {2}),
$$

which is constant everywhere inside the shell. [The constancy of $\omega$ in the cavity has been interpreted by some to mean that Einstein's equations satisfy Mach's principle to some degree.]

Problem 13.19. In the linearized gravitational theory, show that the equations of motion for matter $\mathbf{T}^{\mu \nu}_{;\nu} = 0$ are inconsistent with the field equations for the metric perturbation. Show that this inconsistency is of second order in the metric perturbation, hence negligible to first order.

Problem 13.20. A hypothetical particle of negative gravitational mass $-\mathbf{M}$ is released from rest at a distance $\ell >> \mathbf{M}$ from another fixed particle of equal positive mass $+\mathbf{M}$ . As seen by a static observer, what is the magnitude and direction of the acceleration of each particle? Calculate the motion of the particles after they are released, making any reasonable approximations necessary.

# CHAPTER 14 PHYSICS IN CURVED SPACETIME

This chapter deals with the generalization of the laws of special-relativistic physics (e.g. hydrodynamics, electrodynamics) to curved spacetime. Often this generalization involves only the replacement of partial differentiation by covariant differentiation (''comma-goes-to-semicolon rule'); for example the generalization of the equations of motion is from $\mathbf{T}^{\mu \nu}_{,\nu} = 0$ to $\mathbf{T}^{\mu \nu}_{;\nu} = 0$ ; this latter equation, with semicolons, includes the effects of gravity.

00000000

Problem 14.1. Write the stress-energy tensor for a single free particle, and show that the equation of geodesic motion follows from $\mathbf{T}^{\mu \nu}_{;\nu} = 0$ .

Problem 14.2. Show that the condition for thermal equilibrium of a static system in general relativity is

$$
\mathrm {T} \left(- \mathrm {g} _ {0 0}\right) ^ {\frac {1}{2}} = \text {c o n s t a n t}
$$

(where $\mathbf{T}$ is the temperature measured by a local static observer) rather than the Newtonian relation $\mathbf{T} = \mathbf{constant}$ .

Problem 14.3. Derive the Euler equation $(\rho + p)\nabla_{\mathbf{u}}\mathbf{u} = -[\nabla p + (\nabla_{\mathbf{u}}p)\mathbf{u}]$ from $\mathbf{T}^{\mu \nu}_{;\nu} = 0$ , and show that this equation has the correct Newtonian limit.

Problem 14.4. Derive the general relativistic equation of hydrostatic

equilibrium,

$$
\frac {- \partial \mathbf {p}}{\partial \mathbf {x} ^ {\nu}} = (\rho + \mathbf {p}) \frac {\partial}{\partial \mathbf {x} ^ {\nu}} \log (- \mathbf {g} _ {0 0}) ^ {\frac {1}{2}}
$$

and compare it to the Newtonian equation.

Problem 14.5. Show that a highly relativistic fluid $(\mathfrak{p} = \frac{1}{3}\rho)$ in hydrostatic equilibrium in a gravitational field can never have a free surface (i.e. a surface where $\rho \rightarrow 0$ ).

Problem 14.6. Two identical containers in a static uniform gravitational field contain different substances. The containers and contents have identical time-independent densities of mass-energy, but different (and possibly anisotropic) stresses. Do the containers weigh the same if weighed on the same scale?

Problem 14.7. If $\mathbf{u}$ is the 4-velocity of a perfect gas undergoing adiabatic stationary flow in a stationary gravitational field, prove (the relativistic Bernoulli equation) that along the flow lines

$$
u _ {0} = \text {c o n s t a n t} \times n / (\rho + p),
$$

where $\mathfrak{n} =$ baryon number density.

Problem 14.8. Show that the relativistic Bernoulli equation of Problem 14.7 reduces to the correct Newtonian limit for slow velocities and weak gravitational fields.

Problem 14.9. Consider a moving medium with four-velocity $\mathbf{u}(\mathbf{x})$ . Choose two arbitrary neighboring particles A and B. At each event along the world line of A define the four-vector separation of B from A, $\xi$ , as follows: (i) $\xi$ is an infinitesimal vector from a given event on A's world line to B's world line; (ii) $\xi$ has vanishing time component, $\xi^{\hat{0}} = 0$ , relative to the orthonormal tetrad carried by A.

(a) Define the motion of the medium to be a rigid-body motion if and only if the distance, $(\pmb{\xi} \cdot \pmb{\xi})^{\frac{1}{2}}$ , between any two neighboring particles - e.g., A and B above - is constant for all time. Show that a medium undergoes rigid body motion if and only if $\sigma_{\alpha \beta} = 0$ and $\theta = 0$ , where $\sigma_{\alpha \beta}$ and $\theta$ are the quantities defined in Problem 5.18.

(b) How many independent equations do these conditions constitute? How many degrees of freedom are there in relativistic rigid-body motion?

Problem 14.10. If $\theta$ is the expansion of a fluid, derive the Raychaudhuri equation

$$
\frac {\mathrm {d} \theta}{\mathrm {d} r} = a _ {; a} ^ {\alpha} + 2 \omega^ {2} - 2 \sigma^ {2} - \frac {1}{3} \theta^ {2} - R _ {\alpha \beta} u ^ {\alpha} u ^ {\beta}
$$

where $\omega^2 = \frac{1}{2}\omega_\alpha\beta\omega^\alpha\beta$ , $\sigma^2 = \frac{1}{2}\sigma_\alpha\beta\sigma^\alpha\beta$ , and the notation is the same as in Problem 5.18.

Problem 14.11. In a certain spacetime fluid flows along geodesics with zero shear and expansion. (See Problem 5.18 for the definitions of shear $\sigma_{\alpha \beta}$ and expansion $\theta$ .) Show that the spacetime has a timelike Killing vector.

Problem 14.12. An observer in a closed box (not necessarily in free fall) measures positions and times inside his box with rulers and a clock. Show that the equation of motion for a particle, correct to first order in its measured velocity $v << 1$ and position $x^j$ is

$$
\begin{array}{l} \mathrm {d} \mathbf {v} ^ {\mathrm {j}} / \mathrm {d} t = 2 (\underline {{\mathbf {v}}} \times \underline {{\omega}}) ^ {\mathrm {j}} - [ (\underline {{\mathbf {x}}} \times \underline {{\omega}}) \times \underline {{\omega}} ] ^ {\mathrm {j}} + (\underline {{\mathbf {x}}} \times \underline {{\mathrm {d}}} \underline {{\omega}} / \mathrm {d} t) ^ {\mathrm {j}} \\ - \mathrm {a} ^ {\mathrm {j}} (1 + \underline {{\underline {{\mathrm {a}}}}} \cdot \underline {{\underline {{\mathrm {x}}}}}) - \mathrm {R} _ {0 \mathrm {k 0}} ^ {\mathrm {j}} \mathrm {x} ^ {\mathrm {k}}. \\ \end{array}
$$

Here $\underline{\omega}$ is the angular velocity of the box, $\underline{\mathbf{a}}$ its acceleration, and $\mathbb{R}^j_{0k0}$ the Riemann tensor evaluated at the origin.

Problem 14.13. The stress-energy tensor of a massless scalar field is

taken to be

$$
\mathbf {T} _ {\mu \nu} = (4 \pi) ^ {- 1} (\boldsymbol {\Phi} _ {, \mu} \boldsymbol {\Phi} _ {, \nu} - \frac {1}{2} \mathbf {g} _ {\mu \nu} \boldsymbol {\Phi} _ {, \alpha} \boldsymbol {\Phi} ^ {, \alpha}) .
$$

Derive the equation of motion of this scalar field from $\mathbf{T}^{\mu \nu}_{;\nu} = 0$

Problem 14.14. The equation for a scalar field, in flat spacetime, is $\Phi_{,\nu}^{\nu} = \rho_{\mathrm{s}}$ where $\rho_{\mathrm{s}}$ is the density of "scalar charge." We are tempted to conclude that in curved spacetime the equation should be

$$
\Phi_ {; \nu} ^ {; \nu} = \rho_ {\mathbf {s}} \tag {1}
$$

but another possible generalization is

$$
\Phi_ {; \nu} ^ {; \nu} - \frac {1}{6} R \Phi = \rho_ {\mathrm {s}} \tag {2}
$$

where $\mathbf{R}$ is the Ricci scalar. (Equation (2) is “conformally invariant” while (1) is not.) Does Equation (2), in principle, violate the strong equivalence principle? Find the influence of the $\mathbf{R}$ term on the force $(\sim \nabla \Phi)$ between two “scalar charged” particles, assuming that $\mathbf{R} = 1 / a^2$ varies very slowly on a laboratory scale. In a practical laboratory experiment what would be the magnitude of such anomalous $\mathbf{R}$ -term forces compared to the ordinary scalar forces?

Problem 14.15. Show that Maxwell's equations $\mathbf{F}_{; \nu}^{\mu \nu} = 4\pi \mathbf{J}^{\mu}$ , imply $\mathbf{J}_{; \mu}^{\mu} = 0$ .

Problem 14.16. The generalization of Maxwell's equations to curved spacetime by the "comma-goes-to-semicolon" rule (or principle of equivalence) is not completely unambiguous. Show that the use of this rule with the vector potential $\mathbf{A}^{\mu}$ can lead to two different results for a relativistic equation.

Problem 14.17. Estimate the fractional error introduced into Maxwell's equations (applied to some earthbound process of characteristic frequency $\nu$ and size $\ell$ ) by our ignorance of what curvature coupling terms there may be.

Problem 14.18. Show that except in the case $\underline{\mathbf{E}}\cdot \underline{\mathbf{B}} = 0$ , the sourceless Maxwell equations $\mathbf{F}^{\beta \nu}_{;\nu} = 0$ follow from the requirements $\nabla \cdot \mathbf{T} = 0$ , where $\mathbf{T}$ is the electromagnetic stress-energy tensor, and from the fact that $\mathbf{F}^{\mu \nu}$ is derived from a vector potential.

Problem 14.19. Show that $\mathrm{H} = \frac{1}{2}\mathrm{g}^{\mu \nu}(\pi_{\mu} - \mathrm{eA}_{\mu})(\pi_{\nu} - \mathrm{eA}_{\nu})$ is a Hamiltonian giving the equations of motion of a test particle of charge e. Here $\pi_{\mu}$ is the canonical momentum. (The canonical momentum $\pi^{\mu}$ is not equal to $\mathfrak{p}^{\mu}$ , the particles 4-momentum unless the 4-potential $\mathbf{A}^{\mu}$ is zero.)

Problem 14.20. Suppose $\pmb{\xi}$ is a Killing vector for a solution of the Einstein-Maxwell equations. Write down an integral of the motion for charged test particles. (Assume $\mathfrak{L}_{\pmb{\xi}}\mathbf{A} = 0$ where $\mathbf{A}$ is the 4-potential.)

Problem 14.21. Show that Maxwell's equations are invariant under the "conformal transformation"

$$
\begin{array}{l} \mathrm {g} _ {\alpha \beta} \rightarrow \tilde {\mathrm {g}} _ {\alpha \beta} = \mathrm {f g} _ {\alpha \beta} \\ \mathbf {F} _ {\alpha \beta} \rightarrow \tilde {\mathbf {F}} _ {\alpha \beta} = \mathbf {F} _ {\alpha \beta} \\ \mathrm {J} _ {\mu} \rightarrow \tilde {\mathrm {J}} _ {\mu} = \mathrm {f} ^ {- 2} \mathrm {J} _ {\mu}, \\ \end{array}
$$

where $f$ is an arbitrary function of position.

# CHAPTER 15

# THE SCHWARZSCHILD GEOMETRY

The vacuum $(\mathbf{T}^{\mu \nu} = 0)$ solution to the Einstein field equations which is spherically symmetric and static is called the Schwarzschild geometry. In "curvature coordinates" (where $2\pi r$ measures the proper circumference of 2-spheres) the Schwarzschild metric has the form

$$
d s ^ {2} = - \left(1 - \frac {2 M}{r}\right) d t ^ {2} + \left(1 - \frac {2 M}{r}\right) ^ {- 1} d r ^ {2} + r ^ {2} \left(d \theta^ {2} + \sin^ {2} \theta d \phi^ {2}\right).
$$

(One sometimes abbreviates $\mathsf{d}\Omega^2\equiv \mathsf{d}\theta^2 +\sin^2\theta \mathsf{d}\phi^2.$ ) The constant M is the mass of the source of the field. If the metric is generated by a spherical star, the Schwarzschild metric holds outside the star and matches smoothly to the star's interior metric at its surface.

0000000000

Problem 15.1. Prove that the total angular momentum squared

$$
\mathbf {L} ^ {2} = \mathbf {p} _ {\theta} ^ {2} + \sin^ {- 2} \theta \mathbf {p} _ {\phi} ^ {2}
$$

is a constant of motion along any Schwarzschild geodesic.

# Problem 15.2.

(a) Prove that all orbits in the Schwarzschild geometry are planar.   
(b) Prove that all orbits are stably planar.

Problem 15.3. A particle falls radially into a Schwarzschild metric. As measured by proper time at infinity, what is its inward coordinate velocity (dr/dt) at a (curvature-) radius $r$ ? What is the locally-measured velocity relative to a stationary observer at the same radius?

Problem 15.4. Derive the equations of motion (equations relating $t$ , $r$ and $\tau$ ) for a particle falling radially in the Schwarzschild geometry. Consider the three cases (i) particle released from rest at $r = R$ (ii) particle released from rest at infinity (iii) particle projected inward from infinity with velocity $v_{\infty}$ .

Problem 15.5. Derive a first-order differential equation for the trajectory (r as a function of $\phi$ ) for equatorial orbits in the Schwarzschild geometry.

Problem 15.6. Show that the trajectory of light rays in the Schwarzschild

metric obeys

$$
\frac {\mathrm {d} ^ {2} \mathbf {u}}{\mathrm {d} \phi^ {2}} + \mathbf {u} = 3 \mathbf {u} ^ {2}
$$

where $\mathbf{u} \equiv \mathbf{M} / \mathbf{r}$ , and $\mathbf{r}$ is the Schwarzschild radial coordinate. Denote the minimum value of $\mathbf{r}$ along the trajectory by $\mathbf{b}$ , the "impact parameter." In the case $\mathbf{M} / \mathbf{b} < 1$ what is the deflection of a photon as it passes a spherical gravitating body? Give a formula for the deflection angle to lowest nonvanishing order in $(\mathbf{M} / \mathbf{b})$ .

# Problem 15.7.

(a) For a nearly Newtonian planetary orbit (i.e. $\mathbf{M} / \mathbf{r} < 1$ ) calculate to lowest order in $\mathbf{M} / \mathbf{r}$ the advance of the periastron, per orbit, predicted by general relativity.   
(b) Suppose that the central star is somewhat oblate or prolate, so that the form of the classical Newtonian potential is $\Phi (\mathbf{r}) = -\mathbf{M} / \mathbf{r} - \mathbf{A}\mathbf{M} / \mathbf{r}^3$ where A is related to the magnitude of the oblateness or prolateness. Calculate the advance (if oblate) of the periastron, to lowest order in $\mathbf{A} / \mathbf{r}^2$ , per orbit. (This is a purely Newtonian calculation.)   
(c) Assume that the oblateness of the sun is so large that the rate of advance of the perihelion due to oblateness and the rate of advance due to general relativity are equal for the orbit of Mercury. Compute the rate of advance of the perihelion (in seconds of arc per century) for the four planets closest to the sun, due to each of the effects. Note: to simplify

the calculations assume, throughout the problem, that the orbits are nearly circular - i.e. they all have negligible eccentricity.

Problem 15.8. A rocket ship in a circular orbit of circumference $2\pi r$ around a star of mass M fires a laser gun (rest frequency $\nu_0$ ). The gun is aimed in the orbital plane, and at an angle $\alpha$ (in the ship's frame) outward from the tangential direction of motion. What is the frequency of the laser as seen by a stationary observer at infinity?

Problem 15.9. A test particle of relativistic velocity $\mathbf{v}$ flies past a mass $M$ at an impact parameter $b$ so great that the deflection $\theta_{\mathrm{grav}}$ is small. Calculate $\theta_{\mathrm{grav}}$ . In flat space, a test charge $e$ flies with velocity $v$ past a nucleus of charge $Ze$ at an impact parameter $b$ so great that the deflection $\theta_{\mathrm{EM}}$ is small. Calculate $\theta_{\mathrm{EM}}$ . Why is the formula for $\theta_{\mathrm{grav}}$ different from that for $\theta_{\mathrm{EM}}$ ?

Problem 15.10. A radio commentator is describing his radial fall into a Schwarzschild black hole. Just before he crosses the Schwarzschild radius his broadcast frequency starts becoming redshifted enormously with a time dependence exp $(-t / \text{constant})$ , where $t$ measures proper time at infinity. From the constant deduce the mass of the hole.

Problem 15.11. Calculate the cross section for capture of particles by a Schwarzschild black hole of mass $M$ , in the limits of very high velocity particles ( $v \rightarrow c$ ) and very low velocity particles ( $v << c$ ).

Problem 15.12. Suppose that Paul is orbiting a neutron star in a circular orbit at radial coordinate $r = 4M$ . Peter, his colleague, has been fired radially from a cannon on the neutron star with less than escape velocity; he flies outward just meeting Paul as he crosses his orbit, reaches a maximum radius and falls back down just happening to meet Paul again. Between their two meetings Paul has completed 10 orbits of the neutron star. Peter and Paul have an obsession about comparing their clocks whenever they meet. They set their clocks to agree on their first meeting

as Peter flies outward. When they again compare their clocks, by how much do they disagree?

Problem 15.13. Give the coordinate transformation from Schwarzschild coordinates, in which $\mathrm{ds}^2 = -\mathrm{e}^{2\phi}\mathrm{dt}^2 + \mathrm{e}^{2\Lambda}\mathrm{dr}^2 + \mathrm{r}^2\mathrm{d}\Omega^2$ to "isotropic coordinates", in which $\mathrm{ds}^2 = -\mathrm{e}^{2\phi}\mathrm{dt}^2 + \mathrm{e}^{2\mu}(\mathrm{d}\overline{\mathbf{r}}^2 + \overline{\mathbf{r}}^2\mathrm{d}\Omega^2)$ . Specialize to the vacuum Schwarzschild solution and construct coordinate diagrams showing the relation between $(\mathfrak{t}, \mathfrak{r})$ and $(\mathfrak{t}, \overline{\mathbf{r}})$ coordinates. Is the area $A$ of the surface $\overline{\mathbf{r}} =$ constant, $\mathfrak{t} =$ constant given by $A = 4\pi \overline{\mathbf{r}}^2$ ? Construct an embedding diagram (see MTW p. 613) for the spacelike hypersurface $t = 0$ , for $0 < \overline{\mathbf{r}} < \infty$ .

# Problem 15.14.

(a) Show that in general a boost in the spatial direction $\mathbf{e}_{\hat{\mathbf{j}}}$ leaves invariant the physical components of the Riemann tensor $\mathbb{R}_{\hat{\mathbf{t}}\hat{\mathbf{j}}\hat{\mathbf{t}}\hat{\mathbf{j}}}$ which are "parallel" to the boost. This is analogous to the invariance of $\mathbf{E}_{\hat{\mathbf{j}}}$ and $\mathbf{B}_{\hat{\mathbf{j}}}$ for a boost in the $\mathbf{e}_{\hat{\mathbf{j}}}$ direction.

(b) In the Schwarzschild geometry show that all the physical components of the Riemann tensor are invariant for a boost in the $\mathbf{r}$ -direction, but that all physical components are not invariant for a boost in the $\theta$ or $\phi$ direction.

Problem 15.15. Show that the spacelike slice $\mathbf{v} = \text{constant}(|\mathbf{v}| > 1)$ of the Schwarzschild geometry in Kruskal coordinates $\mathbf{u}, \mathbf{v}$ cannot be embedded in a Euclidean 3-space. What is the general condition on the slope $\mathrm{dv} / \mathrm{du}$ of a spacelike slice of the Schwarzschild geometry that allows it to be embedded in a Euclidean 3-space?

Problem 15.16. Prove that the metric,

$$
\mathrm {d s} ^ {2} = - \mathrm {d t} ^ {2} + \frac {4}{9} \left[ \frac {9 \mathrm {M}}{2 (\mathrm {r} - \mathrm {t})} \right] ^ {2 / 3} \mathrm {d r} ^ {2} + \left[ \frac {9 \mathrm {M}}{2} (\mathrm {r} - \mathrm {t}) ^ {2} \right] ^ {2 / 3} \mathrm {d} \Omega^ {2}
$$

(which looks dynamical because the metric coefficients depend on $t$ ) is actually static. Show that it is in fact the Schwarzschild geometry.

Problem 15.17. In the preceding problem (15.16) show that the set of coordinate-stationary observers are all in free fall and have zero energy (i.e. they fell in from infinity with zero initial velocity).

Problem 15.18. A perfectly adiabatic gas with equation of state $p = \mathrm{Kn}^{\gamma}$ , $4/3 \leq \gamma \leq 5/3$ , $\gamma$ constant, accretes spherically onto a Schwarzschild black hole of mass $M$ . The speed of sound in the gas at radial infinity is $a_{\infty}$ . At what radius does the inward flow become supersonic? (Give answer only to leading term in $a_{\infty}/c$ .)

Problem 15.19. A scalar field satisfies $\square \Phi = 0$ . Show that in the Schwarzschild geometry $\Phi$ can be decomposed into spherical harmonic components $(Y_{\ell_m} = \text{spherical harmonic})$ as

$$
\Phi = \mathbf {\boldsymbol {r}} ^ {- 1} \psi (\mathbf {\boldsymbol {r}}, t) \mathbf {\boldsymbol {Y}} _ {\ell_ {\mathrm {m}}} (\theta , \phi)
$$

where $\psi$ satisfies

$$
\begin{array}{l} \psi_ {, \mathrm {t t}} - (1 - 2 \mathrm {M} / \mathrm {r}) [ (1 - 2 \mathrm {M} / \mathrm {r}) \psi_ {, \mathrm {r}} ], _ {\mathrm {r}} + \mathrm {V} _ {\varrho} (\mathrm {r}) \psi = 0 \\ \mathrm {V} _ {\ell} (\mathrm {r}) \equiv (1 - 2 \mathrm {M} / \mathrm {r}) \left[ \frac {2 \mathrm {M}}{\mathrm {r} ^ {3}} + \frac {\ell (\ell + 1)}{\mathrm {r} ^ {2}} \right]. \\ \end{array}
$$

Problem 15.20. Show that the Schwarzschild metric is also a solution of the Brans-Dicke theory of gravity. (For the Brans-Dicke field equations, see e.g. MTW p. 1070.)

# CHAPTER 16

# SPHERICAL SYMMETRY AND RELATIVISTIC STELLAR STRUCTURE

The geometry generated by a nonrotating, perfect fluid star is spherically symmetric. Exterior to the star it is the Schwarzschild geometry, even if the star is nonstatic (radially pulsating or collapsing). If the star is static, the interior metric can be written

$$
\mathrm {d s} ^ {2} = - \mathrm {e} ^ {2 \Phi} \mathrm {d t} ^ {2} + (1 - 2 \mathrm {m} / \mathrm {r}) ^ {- 1} \mathrm {d r} ^ {2} + \mathrm {r} ^ {2} \mathrm {d} \Omega^ {2}
$$

where $\mathfrak{m} = \int_{0}^{\mathbf{r}} 4\pi \mathbf{r}^{2}\rho \, \mathrm{d}\mathbf{r}$ . The pressure gradient inside the star is given by the OV (Oppenheimer-Volkoff) equation of hydrostatic equilibrium

$$
\frac {\mathrm {d} \mathbf {p}}{\mathrm {d} \mathbf {r}} = - \frac {(\rho + \mathbf {p}) (\mathbf {m} + 4 \pi \mathbf {r} ^ {3} \mathbf {p})}{\mathbf {r} (\mathbf {r} - 2 \mathbf {m})}.
$$

Here $p$ and $\rho$ are the pressure and mass-energy density of the fluid, satisfying the equations of state

$$
\begin{array}{l} \mathrm {p} = \mathrm {p} (\mathrm {n}, \mathrm {T}) \\ \rho = \rho (\mathrm {n}, \mathrm {T}). \\ \end{array}
$$

If the entropy per baryon $s$ is constant in the star, then $p$ depends only on $\rho$ : $p = p(\rho)$ . The metric function $\Phi$ is determined by the Einstein field equations:

$$
\frac {\mathrm {d} \Phi}{\mathrm {d} r} = \frac {\mathrm {m} + 4 \pi \mathrm {r} ^ {3} \mathrm {p}}{\mathrm {r} (\mathrm {r} - 2 \mathrm {m})} \quad \text {a n d} \quad \mathrm {e} ^ {2 \Phi} = 1 - 2 \mathrm {M} / \mathrm {R}, \quad \text {a t} \quad \mathrm {r} = \mathrm {R}
$$

where $\mathbf{R}$ is the radius of the star and $\mathbf{M} = \mathbf{m}(\mathbf{R})$ is its total mass (mass of the exterior Schwarzschild metric).

Equilibrium stellar models may be unstable against gravitational collapse. In this situation the relevant dynamical equations derive from the Einstein field equations and/or from $\mathrm{T}_{;\nu}^{\mu \nu} = 0$ .

A stationary rotating star is not spherically symmetric, but rather is only axisymmetric. The structural equations for axisymmetric stars are quite complicated. However, certain general properties can be deduced (i) from the symmetries or (ii) when the star is assumed to be rigidly rotating.

000000000

Problem 16.1. Find basis vectors (and a dual basis of 1-forms) for orthonormal tetrads in a spherical geometry. Take the legs of the tetrad to be in the $\mathbf{t}$ , $\mathbf{r}$ , $\theta$ , and $\phi$ directions of the isotropic coordinate system whose metric is

$$
d s ^ {2} = - e ^ {2 \Phi} d t ^ {2} + e ^ {2 \mu} (d r ^ {2} + r ^ {2} d \Omega^ {2}).
$$

Problem 16.2. Suppose that an observer, at rest at some point inside a spherical relativistic star, measures the radial pressure-buoyant force, $\mathbf{F}_{\mathrm{buoy}}$ , on a small element of volume V, using the usual laboratory techniques. What value will he find for $\mathbf{F}_{\mathrm{buoy}}$ , in terms of $\rho$ , p, m, V, and dp/dr? If he equates this buoyant force to an equal and opposite gravitational force, $\mathbf{F}_{\mathrm{grav}}$ , what will $\mathbf{F}_{\mathrm{grav}}$ be in terms of $\rho$ , p, m, V, and r? How do these results differ from the corresponding Newtonian results?

Problem 16.3. Prove Birkhoff's Theorem: a spherically symmetric vacuum gravitational field is always static, and is always the Schwarzschild solution.

Problem 16.4. Show that test particles experience no gravitational forces inside a self-gravitating hollow sphere.

Problem 16.5. In the Brans-Dicke theory of gravity (see MTW p. 1070 or Weinberg p. 160 for field equations), show that the only static spherically

vacuum solution which is regular at the origin is the flat-space metric $\pmb{\eta}$ and constant scalar field $\Phi$ .

Problem 16.6. How many algebraically independent components of $\mathbf{T}^{\mu \nu}$ are there in a spherically symmetric configuration?

Problem 16.7. Evaluate the 4 components of the equation $\mathbf{T}^{\alpha \beta}$ ; $\beta = 0$ for the stress energy tensor describing a static, spherically-symmetric perfect fluid star.

Problem 16.8. Polytropic stars (stars with fluids described by $\mathfrak{p} = \mathbf{K}\rho^{\gamma}$ ) are unstable in Newtonian theory if $\gamma < 4/3$ . Consider the influence of small relativistic effects on this stability criterion. Show that the effect is to increase the unstable range of $\gamma$ to $\gamma < 4/3 + \varepsilon$ where $\varepsilon$ may depend on the mass, radius, and structure of the star.

Problem 16.9. Express the Chandrasekhar and Oppenheimer-Volkoff upper mass limits (for white dwarfs and neutron stars, respectively) as dimensional combinations of fundamental constants and the mass of the nucleon and electron. Similarly express the limiting radii corresponding to these mass limits.

Problem 16.10. The mass $\mathfrak{m}(\mathfrak{r})$ inside radius $\mathbf{r}$ for a spherical star appears in the $\mathbf{g}_{\mathbf{rr}}$ term of the line element

$$
\mathrm {d s} ^ {2} = - \mathrm {e} ^ {2 \Phi} \mathrm {d t} ^ {2} + (1 - 2 \mathrm {m} (\mathrm {r}) / \mathrm {r}) ^ {- 1} \mathrm {d r} ^ {2} + \mathrm {r} ^ {2} \mathrm {d} \Omega^ {2}.
$$

Express $\mathfrak{m}(\mathbf{r})$ in a coordinate-independent manner in terms of the surface area and radial separation of spherical surfaces.

Problem 16.11.

(a) What is the form of the Schwarzschild metric in “outgoing Eddington-Finkelstein coordinates”, obtained from curvature coordinates by the

transformation

$$
\mathrm {d t} = \mathrm {d u} + (1 - 2 \mathrm {M} / \mathrm {r}) ^ {- 1} \mathrm {d r}.
$$

(b) Now let $\mathbf{M}$ be a function of the null coordinate $\mathfrak{u}$ in part (a). Show that the space-time is not vacuum, and find the corresponding $T^{\alpha \beta}$ . Give a physical interpretation. (This is the "Vaidya" metric.)

Problem 16.12. Solve the relativistic equations of stellar structure for a static, spherically symmetric star of uniform density. Show that the mass and radius of the star satisfy $\mathbf{R} / 2\mathbf{M} > 9 / 8$ . What is the smallest $\mathbf{R} / 2\mathbf{M}$ can be if the dominant energy condition (see Problem 13.7) holds?

Problem 16.13. A static, spherically symmetric star is made out of a zero-temperature Fermi gas with Fermi energies much larger than the particle rest masses. Show that the equations of stellar structure have a solution $\mathbf{m}(\mathbf{r}) = 3\mathbf{r} / 14$ . Find $\rho(\mathbf{r})$ , $\mathbf{p}(\mathbf{r})$ , and $\mathbf{n}(\mathbf{r})$ . Although $\mathbf{n}$ is infinite at $\mathbf{r} = 0$ , show that the number of particles out to any radius is finite. Make an embedding diagram of the 3-surface, $\mathbf{t} =$ constant. What kind of singularity is at $\mathbf{r} = 0$ ?

Problem 16.14. Calculate the surface stresses in a static self-gravitating shell of mass M and circumference $2\pi R$ . What is the proper surface mass density? Compare the stresses to the Newtonian limit when $\mathbf{R} >> \mathbf{M}$ .

Problem 16.15. What is the smallest possible proper circumference of a self-supporting spherical shell of mass $M$ , if its matter satisfies the dominant energy condition (as do all known forms of matter)?

Problem 16.16. What is the redshift to radial infinity from a thin spherical shell in static equilibrium, in terms of its proper surface density $\Lambda_{\hat{\theta}}^{\hat{0}}$ and proper surface stresses $\Lambda_{\hat{\theta}}^{\hat{\theta}}$ ? What is the largest possible redshift if it satisfies the dominant energy condition?

Problem 16.17. Show that for a rigidly rotating, self-gravitating, perfect fluid star

$$
\nabla \mathbf {p} = (\rho + \mathbf {p}) \nabla \log \mathbf {u} ^ {\mathrm {t}}.
$$

Here $\mathbf{u}^{\dagger}$ is a component of the 4-velocity of the fluid in the canonical coordinate system adapted to the Killing vectors (i.e. $\pmb{\xi}_{(t)} = \partial/\partial t, \pmb{\xi}_{(\phi)} = \partial/\partial \phi$ ).

Problem 16.18. Show that in a rigidly rotating, self-gravitating, perfect fluid star, the surfaces of constant $\mathfrak{p}$ and $\rho$ coincide.

Problem 16.19. Show that the surface of a rigidly rotating star, with angular velocity of rotation $\Omega$ as seen at $\infty$ , is given by

$$
\mathbf {g} _ {\mathrm {t t}} + 2 \mathbf {g} _ {\mathrm {t} \phi} \Omega + \mathbf {g} _ {\phi \phi} \Omega^ {2} = \text {c o n s t a n t}.
$$

Problem 16.20. Find the Doppler broadening for a spectral line from a rigidly rotating star observed by an astronomer who is infinitely far away along the axis of rotation. (The Doppler broadening is the variation across the star in the Doppler shift:

$$
z = \frac {\nu_ {\text {e m i t t e d}}}{\nu_ {\text {o b s e r v e d}}} - 1.)
$$

Problem 16.21. Derive the general relativistic criterion for convective stability in a static equilibrium configuration of perfect fluid.

Problem 16.22. Prove the equivalence of isentropy and constant injection energy $\left[(\rho + p) / (nu^0)\right]$ for a rigidly rotating configuration.

Problem 16.23. Consider a stationary, axisymmetric star. There are two Killing vectors, $\pmb{\xi}_{(t)}$ and $\pmb{\xi}_{(\phi)}$ . Show that

$$
\mathsf {M} = - \int (2 \mathrm {T} _ {\nu} ^ {\mu} - \delta_ {\nu} ^ {\mu} \mathrm {T}) \boldsymbol {\xi} _ {\mathrm {(t)}} ^ {\nu} \mathrm {d} ^ {3} \Sigma_ {\mu}
$$

is the mass of the star as measured from infinity. Here $\mathrm{d}^3\Sigma_\mu$ is the volume element of the star at some instant of time $t$ (the time coordinate $t$ is chosen such that $\xi_{(t)} = \partial/\partial t$ ). Similarly, show that

$$
\mathrm {J} = \int \mathrm {T} _ {\nu} ^ {\mu} \xi_ {(\phi)} ^ {\nu} \mathrm {d} ^ {3} \Sigma_ {\mu}
$$

is the angular momentum as measured from infinity.

Problem 16.24. Show that the integral for M given in Problem 16.23, in the case of a static spherical star made of perfect fluid, is

$$
\mathrm {M} = \int_ {0} ^ {\mathrm {R}} (\rho + 3 \mathrm {p}) \mathrm {e} ^ {\Phi + \lambda} 4 \pi \mathrm {r} ^ {2} \mathrm {d r}
$$

in curvature coordinates $(\mathbf{g}_{00} = \mathrm{e}^{2\Phi}, \mathbf{g}_{\mathrm{rr}} = \mathrm{e}^{2\lambda})$ . Show that this is the same as the expression derived from the equation of stellar structure,

$$
\mathbf {M} = \int_ {0} ^ {\mathbf {R}} \rho 4 \pi \mathrm {r} ^ {2} \mathrm {d r}.
$$

Problem 16.25. For collapsing spherical stars we can't simultaneously have the three nice properties: (i) radial coordinate is comoving with a fluid shell; (ii) time coordinate is proper time for the fluid; (iii) the metric is diagonal. Prove that we can have all three properties if and only if the pressure vanishes.

Problem 16.26. If $\mathbf{R}$ is a comoving coordinate, the metric for a spherically symmetric collapsing star (see Problem 16.25) can be written as

$$
\mathrm {d s} ^ {2} = - \mathrm {e} ^ {2 \Phi} \mathrm {d t} ^ {2} + \mathrm {e} ^ {2 \Lambda} \mathrm {d R} ^ {2} + \mathrm {r} ^ {2} (\mathrm {t}, \mathrm {R}) \mathrm {d} \Omega^ {2}
$$

where $\Phi$ and $\Lambda$ are functions of $\mathbb{R}$ , t. If the star is made of a perfect fluid it is often useful to define the following functions:

$$
\begin{array}{l} m \equiv \int_ {0} ^ {R} 4 \pi r ^ {2} \rho r ^ {\prime} d R \\ \mathrm {U} \equiv \mathrm {e} ^ {- \Phi} \mathrm {i} \\ \Gamma^ {2} \equiv e ^ {- 2 \Lambda} (r ^ {\prime}) ^ {2}. \\ \end{array}
$$

Here primes denote partial differentiation with respect to $\mathbf{R}$ , and dots with respect to $t$ . The function $m$ is interpreted as the mass interior to the shell at $\mathbf{R}$ , and $U$ is the rate at which a shell is moving with respect to the proper time of a comoving observer.

Prove the following relations:

$$
\dot {\mathrm {m}} = - 4 \pi \mathrm {p r} ^ {2} \dot {\mathrm {r}}. \tag {a}
$$

[Hint: Use the first law of thermodynamics (Problem 5.19), baryon conservation, the equations of motion, and $\mathbf{G}_{\mathbf{R}}^{\mathbf{t}} = 0$ (Problem 9.20).]

$$
\Gamma^ {2} = 1 + U ^ {2} - 2 m / r. \tag {b}
$$

[Hint: Use $\mathbf{G}_{\mathfrak{t}}^{\mathfrak{t}} = -8\pi \rho$ and $\mathbf{G}_{\mathbf{R}}^{\mathbf{t}} = 0$ (Problem 9.20).]

Problem 16.27. In a collapsing star made of perfect fluid show that once a mass shell at comoving radius $\mathbf{R}$ has collapsed far enough so that $2\mathfrak{m}(\mathbf{R},\mathfrak{t}) / \mathfrak{r}(\mathbf{R},\mathfrak{t}) > 1$ , the mass shell will collapse to $\mathbf{r} = 0$ in a finite proper time.

Problem 16.28. For spherically symmetric pressure free collapse show that the fall of a shell is governed by the mass interior to that shell in the same manner as the radial fall of a particle in the Schwarzschild geometry is governed by the Schwarzschild mass:

$$
\mathrm {d} ^ {2} \mathrm {r} / \mathrm {d} \tau^ {2} = - \mathrm {M} / \mathrm {r} ^ {2}.
$$

Problem 16.29. For pressure free spherically symmetric collapse (see Problem 16.26), show that both $m$ and $\Gamma$ are independent of time. Solve the resulting dynamical equation

$$
\left(\frac {\mathrm {d} \mathbf {r}}{\mathrm {d} \tau}\right) ^ {2} - \frac {2 \mathbf {m} (\mathbf {R})}{\mathbf {\dot {r}}} = \Gamma^ {2} (\mathbf {R}) - 1
$$

in the three physically distinct cases $\Gamma^2 - 1$ greater than, less than, and equal to, zero.

Problem 16.30. Consider the gravitational collapse of a spherically symmetric, perfect fluid star of zero pressure and uniform density (i.e. uniform throughout the star as seen by observers comoving with the fluid).

(i) Show that the metric inside the star is locally the Friedmann solution with $\mathbf{k} = +1$ if the star collapses from rest at some finite radius, $\mathbf{k} = 0$ if the star is at rest at infinity, or $\mathbf{k} = -1$ if the star is projected with finite velocity from infinity.

(ii) By Birkhoff's theorem (Problem 16.3), the exterior metric is the Schwarzschild metric. Show that each point on the surface of the star moves along a radial geodesic of the Schwarzschild metric.   
(iii) Show that the Friedmann and Schwarzschild metrics match together smoothly at the surface of the star. (It is necessary and sufficient to show that the intrinsic 3-geometry of the surface and the extrinsic curvature of the surface are the same whether measured in the exterior or the interior.)

# CHAPTER 17

# BLACK HOLES

The Kerr-Newman black hole is an exact solution of the Einstein field equations possessing mass, angular momentum, and (in principle but not in astrophysical cases) charge.

The metric describing this solution is (in “Boyer-Lindquist coordinates’):

$$
\begin{array}{l} d s ^ {2} = - \left(1 - \frac {2 M r - Q ^ {2}}{\Sigma}\right) d t ^ {2} - \frac {(2 M r - Q ^ {2}) 2 a \sin^ {2} \theta}{\Sigma} d t d \phi \\ + \frac {\sum}{\Delta} d r ^ {2} + \Sigma d \theta^ {2} + \left(r ^ {2} + a ^ {2} + \frac {(2 M r - Q ^ {2}) a ^ {2} \sin^ {2} \theta}{\Sigma}\right) \sin^ {2} \theta d \phi^ {2} \\ \end{array}
$$

where

$$
a ^ {2} + Q ^ {2} \leq M ^ {2},
$$

$$
\begin{array}{l} M \equiv m a s s, Q \equiv c h a r g e \\ a = \text {a n g u l a r m o m e n t u m p e r u n i t m a s s} \\ \Delta \equiv r ^ {2} - 2 M r + a ^ {2} + Q ^ {2} \\ \Sigma \equiv r ^ {2} + a ^ {2} \cos^ {2} \theta . \\ \end{array}
$$

The metric coefficients are independent of $t$ and $\phi$ , so $\pmb{\xi}_{(t)} = \partial/\partial t$ and $\pmb{\xi}_{(\phi)} = \partial/\partial \phi$ are Killing vectors. Among the properties of this solution which follow from the metric are the orbital equations for test

particles:

$$
\begin{array}{l} \Sigma \dot {\mathbf {r}} = \pm \left(\mathbf {V} _ {\mathbf {r}}\right) ^ {\frac {1}{2}} \\ \Sigma \dot {\theta} = \pm (\mathrm {V} _ {\theta}) ^ {\frac {1}{2}} \\ \Sigma \dot {\phi} = - \left(a E - L _ {z} / \sin^ {2} \theta\right) + \frac {a}{\Lambda} P \\ \Sigma \dot {t} = - a (a E \sin^ {2} \theta - L _ {z}) + \frac {r ^ {2} + a ^ {2}}{\Delta} P. \\ \end{array}
$$

Here “dot” indicates derivative with respect to proper time or affine parameter, and

$$
\mathrm {P} \equiv \mathrm {E} (\mathrm {r} ^ {2} + \mathrm {a} ^ {2}) - \mathrm {L} _ {z} \mathrm {a} - \mathrm {e Q r}
$$

$$
\mathrm {V} _ {\mathrm {r}} \equiv \mathrm {P} ^ {2} - \Delta [ \mu^ {2} \mathrm {r} ^ {2} + (\mathrm {L} _ {z} - \mathrm {a E}) ^ {2} + \mathcal {Z} ]
$$

$$
\mathbf {V} _ {\theta} \equiv \boldsymbol {\mathcal {Q}} - \cos^ {2} \theta [ \mathsf {a} ^ {2} (\mu^ {2} - \mathsf {E} ^ {2}) + \mathsf {L} _ {z} ^ {2} / \sin^ {2} \theta ],
$$

E $\equiv$ conserved total energy

$\mathbf{L}_{z} \equiv$ conserved $z$ component of angular momentum

$\mathfrak{Q}\equiv$ conserved quantity related to total angular momentum

$\mu \equiv$ rest mass of particle

e $\equiv$ charge of particle.

A Schwarzschild black hole is the special case for which $\mathbf{a} = \mathbf{Q} = 0$ . A Reissner-Nordström black hole is the special case $\mathbf{a} = 0$ , $\mathbf{Q} \neq 0$ ; it is spherically symmetric. A Kerr black hole is the case $\mathbf{a} \neq 0$ , $\mathbf{Q} = 0$ . The defining property of a black hole is that it has a horizon, a surface through which matter can fall, but from which no matter or information can escape to infinity. For a Kerr hole, it is located at $\mathbf{r}_+$ , the larger root of the equation $\Delta = 0$ . The stationary limit of a rotating hole is the surface within which all observers are dragged around the hole. For Kerr, the stationary limit is at $\mathbf{r}_0$ , the larger root of $\mathbf{g}_{\mathrm{tt}} = 0$ . The region between the horizon and stationary limit is called the ergosphere.

00000000

Problem 17.1. Show that the constant M which occurs in the Kerr metric is the mass of the system, and that the constant a is the angular momentum per mass.

Problem 17.2. A suggested use of small $(\ll \mathbb{M}_{\oplus})$ black holes is to crush junked automobiles into neat spherical balls by allowing them to partially collapse around a black hole. Estimate what mass hole, in orbit around

the Earth, would be appropriate for this application. How many wrecks per hour could be processed?

Problem 17.3. Show that once a rocket ship crosses the gravitational radius (horizon) of a Schwarzschild black hole, it will reach $r = 0$ in a proper time $r \leq \pi M$ , no matter how the engines are fired.

Problem 17.4. Show that Kepler's law

$$
\Omega^ {2} = \mathrm {M} / \mathrm {r} ^ {3}
$$

holds exactly for circular orbits around a Schwarzschild black hole, if $r$ is the curvature coordinate radius, and $\Omega$ is the angular frequency as measured from infinity. Derive an analogous law for equatorial orbits around a Kerr black hole of specific angular momentum $a$ .

Problem 17.5. An observer in a circular orbit of circumference $2\pi r$ around a charged, spherical, black hole (a Reissner-Nordstrom black hole) of mass M and charge Q measures local electric and magnetic fields. What are their strengths and orientations?

Problem 17.6. By considering the mass, charge, and angular momentum of a "classical" electron, show that it cannot be a Kerr-Newman black hole.

Problem 17.7. For circular orbits in the equatorial plane of a Kerr black hole, prove that the marginally stable orbit has minimum energy E and minimum angular momentum L.

Problem 17.8. An observer (not necessarily freely-falling) orbits a Kerr black hole in the equatorial $(\theta = \pi /2)$ plane.

(a) Let his orbit be at constant $\mathbf{r}$ . Define $\Omega = \frac{\mathrm{d}\phi}{\mathrm{d}t}$ to be his "angular velocity relative to a distant stationary observer." In terms of $\Omega$ , $\mathbf{r}$ , $\mathbf{M}$ , and $\mathbf{a}$ , find $\mathbf{u}^0$ , $\mathbf{u}^\phi$ , $\mathbf{u}_0$ , $\mathbf{u}_\phi$ .   
(b) Suppose that the circular orbit lies in the ergosphere (the orbital radius is outside the horizon at $\mathbf{r}_{+}$ but inside the stationary limit at $\mathbf{r}_0$ ).

Show that the observer cannot remain at rest with respect to a distant observer. That is, show that $\Omega$ for the observer must be nonzero.

(c) If the observer is in the region $\mathbf{r}_{-} < \mathbf{r} < \mathbf{r}_{+}$ , show that he cannot remain at constant radius.

Problem 17.9. Show that there are negative energy particle trajectories inside the ergosphere of a Kerr black hole (and outside the horizon!). Show that it is possible for a rocket ship to increase its total energy by firing a bullet into the hole during an orbital passage through the ergosphere.

Problem 17.10. Show that as a test particle approaches $\mathbf{r} = \mathbf{r}_{+}$ , the horizon of a Kerr black hole, it has "angular velocity as seen from infinity" equal to

$$
\Omega \equiv \frac {\mathrm {d} \phi}{\mathrm {d} t} = \frac {\mathrm {a}}{2 \mathrm {M r} _ {+}}.
$$

Problem 17.11. Prove that there exist "quasi-circular, polar" orbits in the Kerr geometry, i.e. orbits which pass alternately over the north and south poles at a fixed radial coordinate distance. What is the smallest possible polar radius of these orbits?

Problem 17.12. A Killing horizon is a null hypersurface generated by a Killing vector. An ergosurface ("stationary limit") is an infinite red-shift surface for static observers. Show that for a static black hole the ergosurface is a Killing horizon.

Problem 17.13. Show that the surface area of the horizon of a Kerr-Newman black hole (area of surface $\mathbf{r} = \mathbf{r}_{+}$ , $t = \text{constant}$ , in Boyer-Lindquist coordinates) is $4\pi \left[\left[\mathbf{M} + (\mathbf{M}^{2} - \mathbf{Q}^{2} - \mathbf{a}^{2})^{\frac{1}{2}}\right]^{2} + \mathbf{a}^{2}\right]$ .

Problem 17.14. According to Hawking's theorem (that in a collision of two black holes the total surface area must not decrease), what is the minimum mass $\mathbf{M}_2$ of a Schwarzschild black hole that results from the collision of two Kerr black holes of equal mass $\mathbf{M}_1$ and opposite angular

momentum parameter, a? Suppose $|a| \approx M_1$ ; what fraction of the original mass can be radiated away? Are there any other uncharged black-hole collisions that can get this much energy out?

Problem 17.15. Use the theorem that the area of a black hole is nondecreasing (cf. Problem 17.14) to prove that a Kerr black hole amplifies (rather than absorbs) certain modes of an incident radiation field.

Problem 17.16.

(a) Write down the scalar wave equation $\square \Phi = 0$ in the Kerr geometry in Boyer-Lindquist coordinates.   
(b) Show that the equation can be reduced to ordinary differential equations by separation of variables.   
(c) Find the asymptotic form of $\Phi$ for $\mathbf{r} \to \infty$ .   
(d) Find the asymptotic form of $\Phi$ for $\mathbf{r} \to \mathbf{r}_{+}$ .   
(e) What boundary condition on $\Phi$ corresponds to ingoing waves as seen by a physical observer on the horizon?   
(f) Show that, for a wave of the form $\Phi = \exp(-\mathrm{i}\omega t + \mathrm{i}\mathrm{m}\phi)\mathrm{f}(\mathbf{r},\theta)$ , energy flows out of the hole if $0 < \omega / \mathfrak{m} < \mathfrak{a} / (2\mathbf{M}\mathbf{r}_{+})$ . Compare to Problem 17.15.

Problem 17.17. Charged particles are dropped radially into a Reissner-Nordström black hole with $Q^2 < M^2$ . Show that it is never possible to drop in enough charge to make $Q^2 > M^2$ (a solution which would be a naked singularity, not a black hole).

Problem 17.18. The “Zero Angular Momentum Observers” (ZAMO's) in the Kerr geometry have basis 1-forms

$$
\begin{array}{l} \tilde {\omega} ^ {\hat {t}} = \left| g _ {t t} - \omega^ {2} g _ {\phi \phi} \right| ^ {\frac {1}{2}} \widetilde {d t} \\ \tilde {\omega} ^ {\hat {\phi}} = \left(\mathrm {g} _ {\phi \phi}\right) ^ {\frac {1}{2}} \left(\widetilde {\mathrm {d} \phi} - \omega \widetilde {\mathrm {d t}}\right) \\ \tilde {\boldsymbol {\omega}} ^ {\hat {\mathbf {r}}} = \left(\boldsymbol {\Sigma} / \Delta\right) ^ {\frac {1}{2}} \overline {{\mathrm {d} \mathbf {r}}} \\ \tilde {\boldsymbol {\omega}} ^ {\hat {\theta}} = \Sigma^ {\frac {1}{2}} \widetilde {\mathbf {d} \theta} \\ \end{array}
$$

where $\omega \equiv -\mathbf{g}_{t\phi} / \mathbf{g}_{\phi \phi}$

(a) Show that these basis 1-forms are orthonormal.   
(b) Find the dual basis vectors.   
(c) The 4-velocity of the ZAMO is $\mathbf{u} = \mathbf{e}_{\hat{\mathbf{t}}}$ ; show that $\mathbf{u}$ has zero rotation.   
(d) The ZAMO is not an inertial observer; show that the acceleration is $\mathbf{a} = \frac{1}{2}\nabla \log |\mathbf{g}_{\mathrm{tt}} - \omega^2\mathbf{g}_{\phi \phi}|$ .

Problem 17.19. Calculate the Gaussian curvature of the horizon of a Kerr black hole and show that it becomes negative for $a > 3^{\frac{1}{2}}\mathbf{M} / 2$ . (This shows that the horizon cannot be globally embedded in a Euclidean 3-space if $a > 3^{\frac{1}{2}}\mathbf{M} / 2$ .) Use the Gauss-Bonnet theorem to check that the horizon is topologically a 2-sphere.

Problem 17.20. Show that a primordial, rotating, black hole $(\sim 10^{10}$ years old), of mass $\lesssim 10^{15}\mathrm{gm}$ . will have already lost most of its angular momentum to spontaneous quantum emission of photons or gravitons. What fraction of the angular momentum of a $1\mathbf{M}_{\odot}(\sim 10^{33}\mathrm{gm})$ rotating hole would be lost in the same time?

Problem 17.21. Consider the vacuum metric

$$
\mathrm {d s} ^ {2} = - \frac {\left(1 - \frac {1}{2} \mathrm {m} / \rho\right) ^ {2}}{\left(1 + \frac {1}{2} \mathrm {m} / \rho\right) ^ {2}} \mathrm {d t} ^ {2} + \frac {\left(1 - \frac {1}{2} \mathrm {m} / \rho\right) ^ {2}}{\left(1 - \frac {3}{2} \mathrm {m} / \rho\right) ^ {2}} (\mathrm {d} \rho^ {2} + \rho^ {2} \mathrm {d} \theta^ {2} + \rho^ {2} \sin^ {2} \theta \mathrm {d} \phi^ {2})
$$

(which is a particular solution to the static, spherically symmetric problem in the Lightman-Lee theory of gravity). Does the above metric describe a black hole; and, if so, how do the hole's properties differ from those of the corresponding hole in general relativity?

# CHAPTER 18

# GRAVITATIONAL RADIATION

Weak gravitational waves are described by linearized theory (see Chapter 13). The basic equations for waves propagating in vacuum are

$$
\begin{array}{l} \mathrm {g} _ {\mu \nu} = \eta_ {\mu \nu} + \mathrm {h} _ {\mu \nu} \left(\left| \mathrm {h} _ {\mu \nu} \right| \ll 1\right) \\ \overline {{\mathrm {h}}} _ {\mu \nu} \equiv \mathrm {h} _ {\mu \nu} - \frac {1}{2} \mathrm {h} _ {a} ^ {a} \eta_ {\mu \nu} \\ \square \overline {{\mathrm {h}}} _ {\mu \nu} \equiv \overline {{\mathrm {h}}} _ {\mu \nu} ^ {; a} _ {a} = 0 \\ \overline {{h}} _ {; \alpha} ^ {\mu} = 0 \quad \left(" \text {L o r e n t z g a u g e} ^ {\prime \prime}\right) \\ \end{array}
$$

$$
h _ {\mu 0} = 0, h _ {a} ^ {\alpha} = 0 \quad \left(^ {\prime \prime} T T ^ {\prime \prime} \text {o r} ^ {\prime \prime} \text {T r a n s v e r s e - T r a c e l e s s} ^ {\prime \prime} \text {g a u g e}\right).
$$

The effective stress-energy tensor for gravitational waves is

$$
\mathrm {T} _ {\mu \nu} ^ {\mathrm {(G W)}} = \frac {1}{3 2 \pi} <   \mathrm {h} _ {\mathrm {j k}, \mu} \mathrm {h} _ {, \nu} ^ {\mathrm {j k}} >
$$

where $<$ denotes an average over several wavelengths and $h_{jk}$ is in the TT gauge (see e.g. MTW Section 36.7).

The gravitational wave power $\mathbf{L}_{\mathbf{GW}}$ , emitted by a nearly-Newtonian, slow-motion (v << c) gravitating source is

$$
\mathrm {L} _ {\mathrm {G W}} = \frac {1}{5} \frac {\mathrm {G}}{\mathrm {c} 5} <   \ddot {\mathrm {x}} _ {\mathrm {j k}} \ddot {\mathrm {x}} _ {\mathrm {j k}} >,
$$

where $\mathfrak{I}_{jk}$ is the "reduced quadrupole moment tensor" of the source,

given by

$$
\mathbf {x} _ {\mathrm {j k}} \equiv \int \rho \left(\mathbf {x} _ {\mathrm {j}} \mathbf {x} _ {\mathrm {k}} - \frac {1}{3} \delta_ {\mathrm {j k}} \mathrm {r} ^ {2}\right) \mathrm {d} ^ {3} \mathbf {x},
$$

and $<  >$ denotes averaging over several characteristics periods of the source. 106

Problem 18.1. A Massachusetts motorist shakes his fist angrily at another motorist. What fraction of his expended energy goes into gravitational radiation?

Problem 18.2. A gravitationally bound dynamical system (e.g. a binary star) has, in order of magnitude, mass M and size R. Estimate the time for radiation reaction forces to affect the system substantially, and compare this time-scale with the dynamical time-scale for the system.

Problem 18.3. For an electric dipole, and its radiation pattern, there are three independent orientations, corresponding to the three directions in which the dipole may point. How many independent orientations are there for a traceless quadrupole tensor?

Problem 18.4. Calculate the gravitational radiation luminosity of a spinning thin metal rod of mass M and length $\ell$ , spinning at frequency $\omega$ around a symmetrical perpendicular axis. Estimate the electromagnetic luminosity which would arise from the slight excess of electrons pushed toward the ends by centrifugal force. If the rod has a reasonable density $(10\mathrm{gm} / \mathrm{cm}^3)$ and is rotating at a reasonable frequency (1 kHz) will electromagnetic or gravitational radiation be more important in slowing the rotation?

Problem 18.5. The radiation reaction forces on a slow-motion, weak field source can be derived from an addition to the Newtonian potential

$$
\Phi^ {\text {r e a c t .}} = \frac {1}{5} X _ {j k} ^ {(5)} x ^ {j} x ^ {k}.
$$

(Cf. W. Burke, J. Math. Phys. 12, 402 (1971); MTW pp. 993.) Here $\mathfrak{X}_{\mathbf{jk}}$ is the reduced quadrupole moment of the source $\mathbf{x}_{\mathbf{jk}} \equiv \int \rho (\mathbf{x}_{\mathbf{j}}\mathbf{x}_{\mathbf{k}} - \frac{1}{3}\delta_{\mathbf{jk}}\mathbf{r}^{2})\mathrm{d}^{3}\mathbf{x}$ at a given time. The superscript (5) indicates the fifth time derivative. From this potential derive expressions for the time-averaged rates at which the source loses energy and angular-momentum, in terms of derivatives of $\mathfrak{X}_{\mathbf{jk}}$ .

Problem 18.6. Two stars of mass $\mathbf{M}_1$ and $\mathbf{M}_2$ separated by a distance $\mathbf{R}$ revolve about each other in a nonrelativistic circular orbit. Due to gravitational radiation reaction, $\mathbf{R}$ changes with time. Find $\mathbf{R}(t)$ .

Problem 18.7. Two point masses $\mathfrak{m}_1$ and $\mathfrak{m}_2$ are in a Newtonian elliptical orbit with semimajor axis $a$ and eccentricity $e$ . Compute $da/dt$ and $de/dt$ due to gravitational radiation reaction. Show that the elliptical orbit tends to be circularized.

Problem 18.8. A plane gravitational wave propagates through nearly flat empty spacetime, in the $x^1$ direction (i.e. the metric perturbations $h_{\alpha \beta}$ are functions only of $u = t - x$ ). Give an explicit coordinate transformation which makes all the $h_{\alpha \beta}$ zero except $h_{23} = h_{32}$ and $h_{22} = -h_{33}$ . Show that the same resulting components could have been obtained directly by projection into the transverse traceless gauge.

Problem 18.9. Show that gravitational radiation generated by an axisymmetric system carries no net angular momentum. (Do not assume that the sources have weak internal gravitational fields.)

Problem 18.10. Define Stokes parameters for a plane gravitational wave and show how to calculate the fraction of circular polarization, linear polarization and the orientation of maximum linear polarization from the three Stokes parameters.

Problem 18.11. An initially static source undergoes violent motion which generates gravitational radiation and then, after a finite time, becomes again static. A distant observer detects the gravitational waves by watching the motion of two free particles which are initially at rest with respect to each other. Show that after the passage of the waves the observer sees the particles back in their original positions and at rest with respect to each other, to linear order in the wave amplitude.

Problem 18.12. An elastic rod can be used to detect gravitational waves not only at its lowest normal mode frequency $\omega_0$ , but also at harmonics

$\omega_{n} \equiv n \omega_{0}$ . What is the sensitivity of the $n^{\text{th}}$ mode relative to the zeroth, i.e. how does the ratio of maximum squared amplitude of the displacement to energy flux of wave vary with $n$ ? (Assume the rod has the same mechanical damping time for all modes.)

Problem 18.13. A (weak) plane gravitational wave travelling in the $x$ -direction is normally incident on a slab of cement. The cement absorbs energy $E$ from the plane wave. Show (e.g. as a result of $T^{\mu \nu}$ ; $\nu = 0$ ) that the slab must absorb $x$ -momentum $E$ also, and find the relationship between the rate at which energy and $x$ -momentum are absorbed.

Problem 18.14. In the previous problem it was shown that materials must be able to absorb momentum in the direction of wave propagation. This seems incompatible with the description of gravitational waves as transverse! To investigate this point idealize the cement molecules of the previous problem as being harmonically bound to their equilibrium positions, and having a damping force due to internal friction of the cement. Assume the gravitational wave is monochromatic and linearly polarized. Using the equation of geodesic deviation find the time average force, and hence the rate of momentum absorption, in the direction of wave propagation. Show that this rate of momentum absorption is equal to the rate at which the molecule absorbs energy.

Problem 18.15. A weak, plane gravitational wave of frequency $\omega$ and dimensionless amplitude $h$ passes through a "hard-sphere" gas of temperature $T$ . The mean free path of atoms in the gas is $\ell$ , and the gas is dilute enough so that $\ell >> c / \omega$ . Show that in a finite amount of time the particles in the gas will be heated to relativistic temperatures. Estimate this time. Estimate the distance over which the wave is damped by a factor of $e$ in amplitude.

Problem 18.16. Estimate the number of gravitons emitted in an asymmetric explosion of energy E.

Problem 18.17. Roughly how many thermal gravitons does a 100 watt lightbulb emit in its rated lifetime of 1000 hours? What is the approximate wavelength and number of gravitons emitted when the lightbulb is dropped and broken on a cement floor?

Problem 18.18. Calculate in detail the lifetime of a hydrogen atom in the 3d state against decaying to the 1s state by gravitational radiation.

Problem 18.19. By symmetry, the thermal graviton flux from a spherically symmetric star is evidently isotropic; reconcile this fact with Birkhoff's theorem. Approximately what is the multipolarity $2^{\ell}$ of the flux $(\ell = 1 \equiv$ dipole, etc.) for a typical star, such as our sun.

Problem 18.20. Consider the following "gravitational wave modes" representing a gravitational wave travelling in the $z$ direction

$$
\begin{array}{l} \Psi_ {2} = - \frac {1}{6} R _ {z 0 z 0} \quad \Psi_ {4} = R _ {y 0 y 0} - R _ {x 0 x 0} + 2 i R _ {x 0 y 0} \\ \Psi_ {3} = \frac {1}{2} (- R _ {x 0 z 0} + i R _ {y 0 z 0}) \quad \overline {{\Psi}} _ {4} = R _ {y 0 y 0} - R _ {x 0 x 0} - 2 i R _ {x 0 y 0} \\ \bar {\Psi} _ {3} = \frac {1}{2} \left(- R _ {x 0 z 0} - i R _ {y 0 z 0}\right) \quad \Phi_ {2 2} = - \left(R _ {x 0 x 0} + R _ {y 0 y 0}\right). \\ \end{array}
$$

Which of these waves are transverse?

The spin of a wave indicates (among other things) the relation of the orientation of polarization states. For a spin 0 (scalar) wave the manifestations of the wave are symmetric about the direction of propagation. For a spin 1 (vector) wave (e.g. an electromagnetic wave) the independent polarization states are oriented at $90^{\circ}$ to each other; a rotation of $180^{\circ}$ returns to the original polarization state, with only a sign change. In general for a spin s wave a rotation of $\pi /s$ brings back the original polarization state. Which of the waves above are spin 0? Spin 1? Spin 2? Which are possible in general relativity?

Problem 18.21. Draw the force field of each of the modes in the preceding problem.

Problem 18.22. Consider the metric $\mathrm{ds}^2 = \mathrm{dx}^2 + \mathrm{dy}^2 - \mathrm{dudv} + 2\mathrm{H}(\mathbf{x}, \mathbf{y}, \mathbf{u})\mathrm{du}^2$ . What form must the function $\mathbf{H}$ have for this to represent a (strong) plane gravitational wave propagating in vacuum?

# CHAPTER 19

# COSMOLOGY

If the universe is homogeneous and everywhere isotropic, its geometry is that of the Robertson-Walker metric

$$
\mathrm {d s} ^ {2} = - \mathrm {d t} ^ {2} + \mathrm {R} ^ {2} (\mathrm {t}) \left[ \frac {\mathrm {d r} ^ {2}}{1 - \mathrm {k r} ^ {2}} + \mathrm {r} ^ {2} \mathrm {d} \Omega^ {2} \right],
$$

where $\mathbf{k} = +1, 0, -1$ for a closed, marginally open, or open universe.

When the Einstein equations are used to determine the time development of $\mathbf{R}(t)$ and the value of $k$ , the resulting spacetime is called a Friedmann model (sometimes called a Lemaitre model, especially for nonzero cosmological constant). The first two derivatives of $\mathbf{R}(t)$ at the present epoch (denoted by subscript 0) are parameterized by the Hubble constant

$$
\mathrm {H} _ {0} \equiv (\mathrm {d R} / \mathrm {d t}) / \mathrm {R} \quad \text {a t} \quad \mathrm {R} = \mathrm {R} _ {0}
$$

and the "deceleration parameter"

$$
\mathsf {q} _ {0} \equiv - \left[ (\mathrm {d} ^ {2} \mathsf {R} / \mathrm {d t} ^ {2}) \mathsf {R} \right] / (\mathrm {d R} / \mathrm {d t}) ^ {2} \quad \mathrm {a t} \mathsf {R} = \mathsf {R} _ {0} .
$$

The matter in a cosmology is generally in a state of expansion or contraction, so that light received by an observer is generally red- or blueshifted relative to its source by an amount $z$ ,

$$
1 + z \equiv \frac {\nu_ {\text {e m i t t e d}}}{\nu_ {\text {o b s e r v e d}}} = \frac {\lambda_ {\text {o b s e r v e d}}}{\lambda_ {\text {e m i t t e d}}}.
$$

Often the magnitude of $\mathbf{z}$ varies monotonically with distance from an observer so one speaks of "an object at redshift $\mathbf{z}$ ."

If $\rho$ and $p$ are the density and pressure of the smoothed-out mass-energy content of the universe, the universe is said to be "matter dominated" when $\rho >> p$ , and "radiation dominated" when $p \approx \frac{1}{3} \rho$ .

The 3.0K black-body "cosmic microwave background," when extrapolated back in time, implies high temperatures at early times in the Friedmann model, a "hot big bang." However it is also possible that the large "entropy per baryon" implied by this radiation was generated by some dissipative process during the evolution of our universe.

00000000

Problem 19.1. Show that the equations of Newtonian gravity and hydrodynamics do not admit a cosmology which is isotropic, homogeneous, and static (i.e. an unchanging universe filled with a uniform perfect fluid).

Problem 19.2. A spacetime contains no matter and is everywhere isotropic. Prove that it is flat Minkowski space.

Problem 19.3. An object emits black body radiation of temperature $T$ in its own rest frame; we see it at a redshift $z$ and subtending a solid angle $\Omega$ . What flux do we measure? What if the redshift is due to doppler motion of a local object instead of a cosmological redshift?

Problem 19.4. Homogeneous, isotropic spatial hypersurfaces must (by spherical symmetry) have a line element of the form

$$
\mathrm {d} \sigma^ {2} = a ^ {2} \left[ f ^ {2} (r) d r ^ {2} + r ^ {2} d \Omega^ {2} \right], \quad a = c o n s t a n t.
$$

Show that $f^2(r)$ must have the form $(1 - \mathrm{kr}^2)^{-1}$ , where $k = 0, \pm 1$ .

Problem 19.5. Show that the Robertson-Walker metric

$$
\mathrm {d s} ^ {2} = - \mathrm {d t} ^ {2} + \mathrm {R} ^ {2} (\mathrm {t}) \left[ \frac {\mathrm {d r} ^ {2}}{1 - \mathrm {k r} ^ {2}} + \mathrm {r} ^ {2} \left(\mathrm {d} \theta^ {2} + \sin^ {2} \theta \mathrm {d} \phi^ {2}\right) \right]
$$

can also be written as

$$
\mathrm {d s} ^ {2} = - \mathrm {d t} ^ {2} + R ^ {2} (\mathrm {t}) [ \mathrm {d} \chi^ {2} + \Sigma^ {2} (\chi) (\mathrm {d} \theta^ {2} + \sin^ {2} \theta \mathrm {d} \phi^ {2}) ]
$$

or as

$$
\mathrm {d s} ^ {2} = \mathsf {R} ^ {2} (\eta) \left[ - \mathrm {d} \eta^ {2} + \mathrm {d} \chi^ {2} + \Sigma^ {2} (\chi) (\mathrm {d} \theta^ {2} + \sin^ {2} \theta \mathrm {d} \phi^ {2}) \right]
$$

where $\Sigma^2 (\chi) = \sin^2\chi$ or $\chi^2$ or $\sinh^2\chi$ $(k = 1,0, - 1)$

Problem 19.6. Show that the spacelike 3-surfaces of a closed, isotropic, homogeneous universe possess a translation symmetry which leaves no points fixed. (Notice that this is not true in 2 dimensions; a 2 sphere cannot be combed smooth!)

Problem 19.7. A bullet is shot out into an expanding Robertson-Walker universe with a velocity $\mathbf{V}_1$ (relative to cosmological observers). Later, when the universe has expanded by a scale factor $(1 + z)^{-1}$ , it has a different velocity $\mathbf{V}_2$ with respect to cosmological observers. Find $\mathbf{V}_2$ in terms of $z$ and $\mathbf{V}_1$ . Show that in the limit $\mathbf{V}_1 \rightarrow \mathbf{c}$ , the formula for the redshift of photons is obtained.

Problem 19.8. Show by an explicit coordinate transformation that the Robertson-Walker metric is conformally flat. Write $\mathbf{R}_{\mu \nu a\beta}$ in terms of $\mathbf{g}_{\mu \nu}$ and $\rho, p$ and the 4-velocity $\mathfrak{u}^{\mu}$ of the matter.

Problem 19.9. In a Robertson-Walker metric show that angular diameter distance $(\mathbf{d}_{\mathbf{A}})$ , luminosity distance $(\mathbf{d}_{\mathbf{L}})$ and proper motion distance $(\mathbf{d}_{\mathbf{M}})$ are related by

$$
(1 + z) ^ {2} \mathrm {d} _ {\mathbf {A}} = (1 + z) \mathrm {d} _ {\mathbf {M}} = \mathrm {d} _ {\mathbf {L}}.
$$

Problem 19.10. Suppose astronomers are able to find a family of objects whose absolute luminosities $L$ are known. Suppose their apparent luminosities $\ell$ (or equivalently their luminosity distance $d_{L}$ ) and their redshift $z$ are measured. Using the Robertson-Walker line element, find an expression for $\ell$ (or $d_{L}$ ) as a function of $L$ , $z$ , $H_{0}$ and $q_{0}$ for small $z$ .

Problem 19.11. Let $\mathfrak{n}(\mathfrak{t}_0)$ be the number density at the present epoch of a (mythical) family of identical light or radio sources distributed uniformly throughout the universe.

(a) Show that the number of such sources with redshifts less than $z$ as observed from the Earth today is

$$
\mathrm {N} (z) = \frac {4 \pi}{3} \frac {\mathrm {n} (\mathrm {t} _ {0})}{\mathrm {H} _ {0} ^ {3}} z ^ {3} \left(1 - \frac {3}{2} z (1 + \mathrm {q} _ {0}) + \dots\right).
$$

Ignore evolutionary effects, i.e. the number of sources in a unit comoving volume remains constant.

(b) If the sources all have intrinsic luminosity $\mathbf{L}$ , show that the number with fluxes (ergs $\sec^{-1}\mathrm{cm}^{-2}$ ) greater than $\mathbf{S}$ as observed from the earth today is

$$
\mathrm {N} (\mathrm {S}) = \frac {4 \pi}{3} \left. \mathrm {n} (\mathrm {t} _ {0}) \left(\frac {\mathrm {L}}{4 \pi \mathrm {S}}\right) ^ {3 / 2} \left[ 1 - 3 \mathrm {H} _ {0} \left(\frac {\mathrm {L}}{4 \pi \mathrm {S}}\right) ^ {1 / 2} + \dots \right] \right..
$$

Problem 19.12. A ray of light travels along a radial line in the Robertson-

Walker metric

$$
\mathrm {d s} ^ {2} = - \mathrm {d t} ^ {2} + \mathrm {R} ^ {2} (\mathrm {t}) \left[ \frac {\mathrm {d r} ^ {2}}{1 - \mathrm {k r} ^ {2}} + \mathrm {r} ^ {2} \mathrm {d} \Omega^ {2} \right].
$$

How is the coordinate $\mathbf{r}$ related to the affine parameter $\lambda$ along the ray, namely what is $\mathrm{dr} / \mathrm{d}\lambda$ ?

Problem 19.13. By requiring that the Robertson-Walker metric satisfy the Einstein field equations, derive the dynamical equations for a perfect fluid Friedmann cosmology:

$$
3 \ddot {\mathbf {R}} + 4 \pi \mathbf {G} (\rho + 3 \mathrm {p}) \mathbf {R} = 0 \tag {1}
$$

$$
\ddot {\mathbf {R}} \ddot {\mathbf {R}} + 2 \dot {\mathbf {R}} ^ {2} + 2 \mathbf {k} - 4 \pi \mathrm {G} (\rho - \mathrm {p}) \mathbf {R} ^ {2} = 0. \tag {2}
$$

Problem 19.14. Show that the two second-order equations of Problem 19.13 are equivalent to the first order equations

$$
\dot {\mathbf {R}} ^ {2} + \mathbf {k} = \frac {8 \pi G}{3} \rho \mathbf {R} ^ {2} \tag {1}
$$

$$
\frac {\mathrm {d}}{\mathrm {d} \mathrm {R}} (\rho \mathrm {R} ^ {3}) = - 3 \mathrm {p R} ^ {2}. \tag {2}
$$

Problem 19.15. For a Friedmann cosmology derive the relations

$$
\frac {8 \pi G \rho}{3} = \left(\frac {\mathrm {k}}{\mathrm {R} ^ {2}} + \mathrm {H} ^ {2}\right) \tag {1}
$$

$$
- 8 \pi G p = \frac {k}{R ^ {2}} + H ^ {2} (1 - 2 q). \tag {2}
$$

If the cosmology is matter-dominated $(\rho >> p)$ show that

$$
\frac {\mathrm {k}}{\mathrm {R} ^ {2}} = (2 \mathrm {q} - 1) \mathrm {H} ^ {2} \tag {3}
$$

$$
\frac {8 \pi G \rho}{3} = 2 q H ^ {2}. \tag {4}
$$

If it is radiation dominated $(\mathfrak{p} \approx 1/3 \rho)$ show that

$$
\frac {k}{R ^ {2}} = (q - 1) H ^ {2} \tag {5}
$$

$$
\frac {8 \pi G \rho}{3} = q H ^ {2}. \tag {6}
$$

Problem 19.16. For a Friedmann cosmology what equations relating $\mathfrak{p}$ , $\rho$ , and $\mathbf{R}(t)$ result from the equation of energy conservation, $\mathbf{T}_{\mu ;\nu}^{\nu} = 0$ ?

Problem 19.17. For a $\mathbf{k} = -1$ Friedmann cosmology with $\mathfrak{p} = \rho = 0$ show that the line element becomes

$$
\mathrm {d s} ^ {2} = - \mathrm {d t} ^ {2} + \mathrm {t} ^ {2} \left[ \mathrm {d} \chi^ {2} + \sinh^ {2} \chi \left(\mathrm {d} \theta^ {2} + \sin^ {2} \theta \mathrm {d} \phi^ {2}\right) \right].
$$

Exhibit an explicit coordinate transformation to show that this metric describes Minkowski space.

Problem 19.18. Solve the first-order Friedmann equation

$$
\left(\frac {\dot {\mathrm {R}}}{\bar {\mathrm {R}}}\right) ^ {2} = \frac {8 \pi \mathrm {G}}{3} \rho - \frac {\mathrm {k}}{\mathrm {R} ^ {2}}
$$

for $\mathbf{R}(t)$ when the density $\rho$ is dominated by a) matter and b) radiation. Express any parameters of the present epoch in terms of $\mathbf{H}_0$ and $\mathbf{q}_0$ .

Problem 19.19. A bullet is shot out into an expanding Friedmann universe. When $\mathbf{k} = -1$ , show that it approaches the same velocity as some cosmological observer, but a position which is a constant proper distance away from him. When $\mathbf{k} = 0$ , show that the bullet again approaches the velocity of some cosmological observer but that the proper distance between the bullet and that observer becomes arbitrarily large as $t \to \infty$ .

Problem 19.20. For a closed $(k = 1)$ Friedmann universe in which radiation dominates for only a negligibly short fraction of the life of the universe, how many times can a photon encircle the universe from the moment of the creation of the universe to the moment of its death?

Problem 19.21. If an idealized $\mathbf{k} = 0$ matter dominated Friedmann cosmology with Hubble constant $\mathrm{H}_0$ contains homogeneously distributed sources of constant luminosity $\mathrm{L}$ , and if the local number density of such sources in space is now $\mathfrak{n}$ , what is the brightness $\mathbf{B}$ of the night sky (energy per steradian of sky per collection area per time)? (If the universe were static and infinitely old the brightness would be infinite; this is called Olbers' Paradox.)

Problem 19.22. Suppose that at the time of hydrogen recombination (which, say, occurred at a redshift of $z = 1500$ ) the deceleration parameter was $q = 0.5002$ . What would $q_0$ be today? Repeat for $q = 0.4998$ at $z = 1500$ . (Assume a matter-dominated universe.)

Problem 19.23. A closed $(\mathbf{k} = 1)$ Friedmann universe has Hubble constant $H_0$ and deceleration parameter $q_0$ . Assume that the universe has always been matter dominated.

(a) What is the total proper volume of the universe at the present epoch?   
(b) What is the total proper volume that we see, looking out into the sky?   
(c) What is the total proper volume now occupied by the matter which we see, looking out into the sky?

Problem 19.24. What is the apparent angular size of an object of proper diameter $\ell$ seen at redshift $z$ in a matter dominated Friedmann cosmology with present parameters $\mathbf{H}_0$ and $\mathbf{q}_0$ ? (Analogous results for apparent proper motion and apparent luminosity follow from Problem 19.9.)

Problem 19.25. In a "hot" Friedmann cosmology, two unrelated important epochs are when matter first begins to dominate radiation ( $\rho_{\text{matter}} \approx \rho_{\text{radiation}}$ ), and when protons and electrons recombine to form hydrogen. Given that these epochs happen to be nearly the same in our universe, deduce a numerical value for the conserved entropy per baryon $\sigma \equiv 4aT^3 / 3n$ (where $T =$ temperature, $a =$ radiation constant, $n =$ number density of baryons).

Problem 19.26. In terms of the conserved entropy per baryon $\sigma$ of a hot big bang model, find the temperature at which hydrogen characteristically recombined, i.e. had an equilibrium ionization fraction of 0.5. Evaluate your answer for $\sigma = 10^{8}$ , $10^{9}$ .

Problem 19.27. In a radiation dominated Friedmann cosmology at times near the big bang singularity, calculate the temperature $T$ as a function of (proper cosmological) time $t$ . Assume that only photons, electrons and positrons contribute to the energy density $\rho$ . How is the answer changed if neutrinos and antineutrinos are also allowed?

Problem 19.28. A Friedmann cosmology has temperature $\mathbf{T}_1$ at expansion scale $\mathbf{R}_1$ , and is dominated by relativistic electrons, positrons, muons, photons, and neutrinos in thermal equilibrium. Later, at expansion scale $\mathbf{R}_2$ , the muon pairs have annihilated, but the other particles are still relativistic and in equilibrium. Find the temperature $\mathbf{T}_2$ in terms of $\mathbf{T}_1$ , $\mathbf{R}_1$ , and $\mathbf{R}_2$ .

Problem 19.29. Under which of the following suppositions would the hot big bang have produced less $\mathbf{He}^4$ than predicted by the "standard" model? Less $\mathbf{H}^2$ (deuterium)?

(i) Suppose the baryon density in the universe today is larger than we now think.   
(ii) Suppose the weak interaction constant is smaller than we now think.   
(iii) Suppose there are many more neutrinos than antineutrinos or photons in the cosmic background today.   
(iv) Suppose there are many more antineutrinos than neutrinos or photons in the cosmic background today.   
(v) Suppose that the gravitational constant $G$ varies with cosmological time and was slightly larger in the past.

Problem 19.30. Suppose that a universe is isotropic, homogeneous, and empty except for a “vacuum polarization” stress energy of the form $8\pi \mathrm{T}_{\mu \nu} = \Lambda \mathbf{g}_{\mu \nu}$ . (In old language: there is a non-zero cosmological constant $\Lambda$ .) Find a $\mathbf{k} = 0$ cosmological solution. Find a coordinate system in which it is static. (This is the “de Sitter universe”).

Problem 19.31. A universe is isotropic, homogeneous, and contains only pressureless dust and "vacuum polarization" stress energy, so that $\mathbf{T}_{\mu \nu} = \rho_0 \mathfrak{u}_\mu \mathfrak{u}_\nu - \frac{\Lambda}{8\pi} \mathfrak{g}_{\mu \nu}$ where $\mathfrak{u}^\mu$ is the 4-velocity field of the matter. Show that there is a static solution for the metric, but that it is unstable. (This cosmology is called the "Einstein universe".)

Problem 19.32. What is the proper volume of the "Einstein universe" of Problem 19.31, in terms of $\rho_0$ , the density of its dust.

Problem 19.33. At one time observations seemed to suggest that there was an unusual clustering of quasar redshifts around $z = 2$ . One proposal to explain this is that our universe is a $k = +1$ dust cosmology, with nonzero cosmological constant $\Lambda$ only slightly greater than the value for a static "Einstein Universe" (Problem 19.31). Show that for this model the universe will expand at a decreasing rate to a certain radius $R_{\mathrm{m}}$ , at which radius it will remain for a long time while expanding very slowly, before expanding again at a rate which asymptotically approaches $H = (\Lambda / 3)^{\frac{1}{2}}$ .

Suppose quasar formation occurred at the time of nearly constant radius. What does this model predict for $\rho_{\text{matter}}$ today? [Use $\mathbf{H}_0 = 10^{-28} \, \mathrm{cm}^{-1}$ ].

Problem 19.34. What is the order of magnitude of the influence of the cosmological constant on the celestial mechanics of the solar system if $\Lambda \sim 10^{-57} \mathrm{~cm}^{-2}$ ?

Problem 19.35. Prove that for a physically possible perfect fluid no solution of the Einstein equations is homogeneous, everywhere isotropic, and static. (Before Hubble's discovery, Einstein considered this a failing of the theory and introduced the "cosmological constant" term as a remedy.)

Problem 19.36: Prove that no solution of the Einstein equations for a pressureless fluid is static. Do not assume isotropy or homogeneity. (The difficulty of this problem depends on the definition of "static.") Easy case: Take static to mean time invariant and time reversible, the first definition of "static" in Problem 10.8. Harder case: Use the second definition in Problem 10.8.)

Problem 19.37. Prove that no solution of the Einstein equations for a perfect fluid is static and homogeneous. Do not assume isotropy. (Again as in Problem 19.36 there are easy and harder cases depending on the definition of "static" that is used.)

Problem 19.38. In cosmology one usually uses coordinates comoving with the galaxies. Let $(r, x^i)$ be such a system, and let the metric take the

general form

$$
\mathrm {d s} ^ {2} = - \mathrm {d} \tau^ {2} + 2 \mathrm {g} _ {0 \mathrm {i}} \mathrm {d} \tau \mathrm {d x} ^ {\mathrm {i}} + \mathrm {g} _ {\mathrm {i j}} \mathrm {d x} ^ {\mathrm {i}} \mathrm {d x} ^ {\mathrm {j}}
$$

where $\mathbf{g}_{0\mathrm{i}}$ and $\mathbf{g}_{\mathrm{ij}}$ can be functions of $\pmb{\tau}$ and $\mathbf{x}^{\mathrm{i}}$ . Show

(a) that $\tau$ is the proper time measured by a galaxy;   
(b) that $\mathbf{g}_{\cdot \cdot}$ governs proper distances in the hypersurface of constant $\tau$ ;   
(c) that if $\mathbf{g}_{0\mathrm{i}}$ and $\mathbf{g}_{ij}$ are independent of all $\mathbf{x}^{\mathrm{i}}$ , then the universe is homogeneous but that the converse is false;

(d) that if $\mathbf{g}_{0\mathrm{i}}$ and $\mathbf{g}_{\mathrm{ij}}$ are independent of $\pmb{\tau}$ , then $\sigma_{\alpha \beta} = 0$ , $\theta = 0$ (but $\omega_{\alpha \beta} \neq 0$ in general);   
(e) that if $\mathbf{g}_{0\mathbf{i}} = 0$ and $\mathbf{g}_{ij} = \mathbf{f}(\tau)\overline{\mathbf{g}}_{ij}(\mathbf{x}^{\mathbf{k}})$ , then $\sigma_{ij} = 0$ ;   
(f) that $\mathbf{g}_{0\mathbf{i},0} = 0$ if and only if galaxies fall on geodesics;   
(g) that if $\omega_{\alpha \beta} \neq 0$ , no choice of $\tau$ and $\mathbf{x}^{\mathrm{i}}$ can make $\mathbf{g}_{0\mathrm{i}} = 0$ everywhere and that this means that $\omega_{\alpha \beta, 0} \neq 0$ implies nongeodesic motion of the galaxies.

Problem 19.39. The distance between two neighboring galaxies is $\delta \mathbf{x}^a = \mathbf{Rn}^a$ where $\mathbf{n}$ is a unit, purely spatial vector in one galaxy's rest frame. Show that

$$
\frac {\dot {R}}{R} = \sigma_ {\alpha \beta} n ^ {\alpha} n ^ {\beta} + \frac {1}{3} \theta
$$

(where $\sigma$ is the shear tensor and $\theta$ is the scalar expansion) and that averaging over all directions $\mathfrak{n}^{\alpha}$ gives

$$
<   \frac {\dot {\mathbf {R}}}{\mathbf {R}} > = \frac {1}{3} \theta .
$$

Problem 19.40. For the congruence of galaxy world lines in a Robertson-Walker cosmology find $\theta, \omega_{\alpha \beta}$ and $\sigma_{\alpha \beta}$ . (See Problem 5.18 for definitions.) Do the same for the anisotropic metric

$$
\mathrm {d s} ^ {2} = - \mathrm {d t} ^ {2} + \mathrm {e} ^ {2 a} \mathrm {d x} ^ {2} + \mathrm {e} ^ {2 b} \mathrm {d y} ^ {2} + \mathrm {e} ^ {2 c} \mathrm {d z} ^ {2}
$$

where a, b, and c are functions of t and where x, y and z are coordinates comoving with the galaxies.

Problem 19.41. Consider the homogeneous, anisotropic cosmological model with metric

$$
d s ^ {2} = - d t ^ {2} + g _ {i j} (t) d x ^ {i} d x ^ {j}.
$$

where the space slices $t =$ constant have a flat geometry. Find the evolution of the $g_{ij}$ when the universe is "gravitation dominated," i.e. set $T^{\mu \nu}$ to zero in the field equations. Show that the volume of the universe goes to zero linearly with $t$ as $t \to 0$ (in contrast to the $t^{3/2}$ or $t^2$ behavior for radiation- or matter-dominated Friedmann models).

# CHAPTER 20 EXPERIMENTAL TESTS

This chapter explores concepts relevant to experimental tests of gravitation theory (light deflection, perihelion shift, etc.). A number of problems elsewhere in this book are similarly relevant: 11.9, 11.11, 12.2-12.4, 12.6, 12.7, 13.2-13.4, 14.12, 15.6, 15.7.

000000000

Problem 20.1. Gravitational bending of light: An evacuated tube of length $\ell$ is set up horizontally in a uniform gravitational field - e.g., in the field of the earth at sea level with $\ell \ll r_{\text{earth}}$ so that gravitational inhomogeneities (tidal forces) are negligible. A laser beam passing through the tube is deflected from the horizontal by the uniform gravitational field. Calculate the angle of light deflection measured relative to the axis of the tube. Express the answer in terms of the length of the tube, $\ell$ , and the acceleration of gravity, g. Discuss the feasibility of performing such an experiment in an earth-based laboratory.

Problem 20.2. Calculate the gravitational light deflection of a ray passing near the sun using Newtonian gravity and the fact that light moves along straight lines in the local frame of a freely falling observer. Since the light is always in a weak gravitational field, the Newtonian approximation seems justifiable. Why doesn't this answer agree with the general relativistic answer?

Problem 20.3. Derive the general expression for the angular deflection of light by the sun's gravitational field, if the light comes from a star which is at an angle $\alpha$ from the sun as seen from earth. Take the earth-sun distance to be R. Do not assume that $\alpha$ is small, but show that in the

limit of small $\alpha$ the answer reduces to the conventional result (Problem 15.6) $\delta \alpha = 4\mathsf{M} / \mathsf{b}$ .

Problem 20.4. Show that the sun's angular momentum $\underline{\mathbf{J}}$ modifies the light deflection formula (Problem 20.3) from $\delta \phi = 4\mathsf{M} / \mathsf{b}$ to

$$
\delta \phi = \frac {4 \mathrm {M}}{\mathrm {b}} \left(1 - \frac {\mathrm {J} \cdot \mathrm {n}}{\mathrm {M b}}\right)
$$

where $\underline{\mathfrak{n}}\equiv$ unit vector in direction of angular momentum of the photons about the center of sun.

Problem 20.5. In addition to the general relativistic deflection of electromagnetic waves by the sun, there is a frequency-dependent deflection caused by the solar corona, which must be taken into account in the interpretation of measurements. Estimate the impact parameter at which the general relativistic and coronal deflections of an electromagnetic wave of frequency $\nu$ make approximately equal contributions. Take an approximate coronal electron density of

$$
\log_ {1 0} \left(\frac {\mathrm {n} _ {\mathrm {e}}}{1 \mathrm {c m} ^ {- 3}}\right) = 8. 4 - 6. 5 \log_ {1 0} \left(\frac {\mathrm {r}}{\mathrm {R} _ {\odot}}\right)
$$

for $\mathbf{r} \leq 4\mathbf{R}_{\odot}$ . Evaluate your answer, in solar radii, for $\nu = 1000\mathrm{MHz}$ .

Problem 20.6. The deflection angle of light passing near the sun is given by $\delta = 1.75^{\prime \prime} / b$ , where $b$ is the impact parameter in solar radii. Design a thin lens (i.e. give thickness as a function of radius) which models this focal behavior. Take the solar disc to be a black mask of $8\mathrm{mm}$ diameter in the center of the lens, so that you can simulate the light deflection experiment by holding the lens at arm's length. Assume an index of refraction appropriate to ordinary crown glass, $n = 1.52$ .

Problem 20.7. Calculate the expected perihelion shift of the planet Mercury in terms of the semimajor axis of its orbit $\mathbf{a}$ , the eccentricity $\mathbf{e}$ , and the mass $\mathbf{M}$ of the sun.

Problem 20.8. Newtonian gravitation theory can be modified and made covariant if the force equation on a point particle is written as

$$
\mathrm {d p} ^ {\mu} = - \eta^ {\mu \nu} \Phi_ {, \nu} \mathrm {p} _ {\beta} \mathrm {d x} ^ {\beta} + \mathrm {p} ^ {\alpha} \Phi_ {, \alpha} \mathrm {d x} ^ {\mu}
$$

where $\Phi$ is a scalar potential which is related to stress energy by

$$
\Phi_ {; \mu} ^ {; \mu} = 4 \pi   T _ {\mu} ^ {\mu}    .
$$

Investigate whether this theory agrees with experiment and observation:

(a) Is this theory in agreement with the experiments of Eotvos and Dicke showing the equivalence of inertial and passive gravitational mass?   
(b) Is this theory in agreement with the Pound-Rebka experiment on the gravitational redshift of a photon on the earth's surface?   
(c) Does this theory predict the bending of starlight near the sun?

Problem 20.9. A physicist wishes to take advantage of the tremendous precision of current atomic clocks by using them to test both special and general relativity. He places various clocks at different locations on the earth (assumed to be rigidly rotating) and measures their ticking rates with respect to some standard clock. Both the doppler shift, due to the earth's rotation, and the redshift effect, due to the earth's gravitational field, make contributions to deviations in ticking rates. Calculate the measured ticking rate of a clock located at $(\mathbf{r},\theta)$ relative to a standard clock of your choice. Take into account the rotational deformation of the earth's surface, assuming the earth is a rigidly rotating perfect fluid.

# CHAPTER 21   MISCELLANEOUS

Problems in this chapter deal mostly with variational techniques, thin shells of matter, and spinors.

![](images/38d4485c1efee3c404771dd57d01422348244127c087ac740071e28791e90a5d.jpg)

Problem 21.1. Show that

(i) $\delta (-\mathbf{g})^{\frac{1}{2}} = \frac{1}{2} (-\mathbf{g})^{\frac{1}{2}}\mathbf{g}^{\mu \nu}\delta \mathbf{g}_{\mu \nu}$   
(ii) $\delta \mathbf{g}^{\mu \nu} = -\mathbf{g}^{\rho \mu}\mathbf{g}^{\sigma \nu}\delta \mathbf{g}_{\rho \sigma}$

Problem 21.2. Let $\mathbf{L} = \mathbf{L}(\Phi^{\mathbf{A}},\mathbf{g}_{\mu \nu})$ be the Lagrangian density for some field or matter distribution. The field is described by the variables $\Phi^{\mathbf{A}}$ , where $\mathbf{A}$ represents any tensor indices. The action is

$$
S = \int L (- g) ^ {\frac {1}{2}} d ^ {4} x.
$$

The functional derivative $\delta L / \delta \Phi^{\mathbf{A}}$ is defined by making a variation $\Phi^{\mathbf{A}}\rightarrow$ $\Phi^{\mathbf{A}} + \delta \Phi^{\mathbf{A}}$ and taking the change in S to be

$$
\delta \mathbf {S} = \int \frac {\delta \mathbf {L}}{\delta \Phi^ {\mathbf {A}}} \delta \Phi^ {\mathbf {A}} (- \mathbf {g}) ^ {\frac {1}{2}} \mathbf {d} ^ {4} \mathbf {x} .
$$

Show that $\delta \mathbf{L} / \delta \Phi^{\mathbf{A}} = 0$ is the usual Euler-Lagrange equation when $\mathbf{L}$ depends on $\Phi^{\mathbf{A}}$ and its partial derivatives $\Phi_{,a}^{\mathbf{A}}$ .

Problem 21.3. If $\mathbf{L}$ is a Lagrangian density as in Problem 21.2, the stress-energy tensor can be defined by a variation of $\mathbf{g}_{\mu \nu}$ in $S$ :

$$
\delta S = \intop \frac {\delta (\mathrm {L} (- \mathrm {g}) ^ {\frac {1}{2}})}{\delta \mathbf {g} _ {\mu \nu}} \delta \mathbf {g} _ {\mu \nu} \mathrm {d} ^ {4} \mathbf {x} \equiv \frac {1}{2} \intop \mathrm {T} ^ {\mu \nu} \delta \mathbf {g} _ {\mu \nu} (- \mathbf {g}) ^ {\frac {1}{2}} \mathrm {d} ^ {4} \mathbf {x} .
$$

Show that $\mathbf{T}^{\mu \nu}_{;\nu} = 0$ follows from the equation of motion of the field and the fact that S is a scalar.

Problem 21.4. Consider the action

$$
\mathbf {S} = (1 6 \pi) ^ {- 1} \int (- \mathbf {g}) ^ {\frac {1}{2}} \mathsf {R d} ^ {4} \mathbf {x} + \int \mathsf {L} _ {\mathrm {m a t t e r}} (- \mathbf {g}) ^ {\frac {1}{2}} \mathsf {d} ^ {4} \mathbf {x} ,
$$

where $\mathbf{R}$ is the Ricci scalar and $\mathbf{L}_{\mathrm{matter}}$ contains g's but no $\Gamma$ 's (so that $\Gamma$ 's are present only in $\mathbf{R}$ ).

(a) Treat the g's and the $\Gamma$ 's as independent field variables ("Palatini method"), and show that $\delta S = 0$ leads to the Einstein field equations and the usual formula for the $\Gamma$ 's in terms of the g's. (Assume $\Gamma_{\beta \nu}^{\alpha} = \Gamma_{\nu \beta}^{\alpha}$ .)   
(b) Now assume $\Gamma$ 's are Christoffel symbols used to define covariant derivatives in the usual way. Show that $\delta S = 0$ (where now $\delta \Gamma^{\alpha}{}_{\beta \nu}$ is not independent of $\delta g^{\alpha \beta}$ ) leads to the Einstein field equations.

Problem 21.5. The Lagrangian density for a scalar field is

$\mathbf{L} = -(8\pi)^{-1}(\Phi_{;a}\Phi^{;a} + \mathfrak{m}^{2}\Phi^{2})$ . Find the equations of motion and the stress-energy tensor. Verify explicitly that the stress-energy tensor has vanishing divergence.

Problem 21.6. The electromagnetic Lagrangian density is

$\mathbf{L} = -(16\pi)^{-1}\mathbf{F}^{\mu \nu}\mathbf{F}_{\mu \nu}$ where $\mathbf{F}_{\mu \nu} = \mathbf{A}_{\nu ;\mu} - \mathbf{A}_{\mu ;\nu}$ . Show that the Maxwell equations $\mathbf{F}^{\alpha \beta}$ ; $\beta = 0$ follow from setting to zero the variation of $\int \mathbf{L}(-\mathbf{g})^{\frac{1}{2}}\mathrm{d}^{4}\mathbf{x}$ with respect to $\mathbf{A}_{\mu}$ . Find the stress-energy from the prescription

$$
\mathrm {T} _ {\mu \nu} = - 2 \frac {\delta \mathrm {L}}{\delta \mathrm {g} ^ {\mu \nu}} + \mathrm {g} _ {\mu \nu} \mathrm {L}.
$$

Show that an equivalent Lagrangian density is

$$
\mathbf {L} = - \frac {1}{1 6 \pi} \mathbf {F} _ {\mu \nu} \mathbf {F} ^ {\mu \nu} - \frac {1}{4 \pi} \mathbf {F} ^ {\mu \nu} \mathbf {A} _ {\mu ; \nu}
$$

where $\mathbf{F}^{\mu \nu}$ is antisymmetric and $\mathbf{F}^{\mu \nu}$ and $\mathbf{A}_{\mu}$ must be varied independently.

Problem 21.7. A Lagrangian for the Brans-Dicke theory is

$$
L = \left(\Phi R - \omega \Phi_ {, a} \Phi^ {, a} \Phi^ {- 1} + 1 6 \pi L _ {\text {m a t t e r}}\right)
$$

where $\Phi =$ scalar field, $\mathbf{R} =$ curvature scalar, $\omega =$ coupling constant.

Derive the field equations from $\delta \int \mathbf{L}(-\mathbf{g})^{\frac{1}{2}}\mathrm{d}^{4}\mathbf{x} = 0$ by varying $\mathbf{g}_{\alpha \beta}$ and $\Phi$ .

Problem 21.8. A surface layer is a timelike 3-surface separating two regions of spacetime. In general relativity the intrinsic geometry of such a 3-surface is well defined, but the extrinsic curvature may be discontinuous. That is, we may get a different extrinsic curvature tensor $\mathbf{K}$ if we evaluate it with respect to the 4-geometry on one side or the other. The surface stress-energy $S^{\alpha}_{\beta}$ contained in such a surface layer is defined as

$$
S ^ {\alpha} \beta = \lim  _ {\varepsilon \rightarrow 0} \int_ {- \varepsilon} ^ {+ \varepsilon} T ^ {\alpha} \beta d n
$$

where $\mathbf{n}$ is proper distance perpendicular to the 3-surface. Use the initial value equations to find the discontinuity in $\mathbf{K}$ in terms of $S^{\alpha}\beta$ .

Problem 21.9. For a surface layer described with Gaussian normal coordinates $\mathbf{n}$ and $\mathbf{x}^i$ ( $i = 1, 2, 3$ ) (see solution to Problem 21.8) derive the equation of motion of the surface layer

$$
\mathbf {S} _ {j \mid i} ^ {i} + \left[ \mathbf {T} _ {j} ^ {n} \right] = 0
$$

where the square brackets denote a discontinuity across the surface and the slash denotes covariant differentiation with respect to the intrinsic geometry of the 3-surface.

Problem 21.10. A thin shell of dust in vacuum has surface density of mass $\sigma$ as measured by an observer comoving with the dust. If $\mathbf{u}$ is the 4-velocity of the dust, show that

$$
\begin{array}{l} \left[ \mathrm {K} _ {\mathrm {i j}} \right] = 8 \pi \sigma \left(\mathrm {u} _ {\mathrm {i}} \mathrm {u} _ {\mathrm {j}} + \frac {1}{2} ^ {(3)} \mathrm {g} _ {\mathrm {i j}}\right) \\ \frac {\mathrm {d} \sigma}{\mathrm {d} \tau} = - \sigma \mathbf {u} ^ {\mathbf {i}} | _ {\mathbf {i}} \\ \mathbf {a} ^ {+} - \mathbf {a} ^ {-} = 4 \pi \sigma \mathbf {n} \\ \mathbf {a} ^ {+} + \mathbf {a} ^ {-} = 0. \\ \end{array}
$$

Here $\mathbf{a}^{+}$ and $\mathbf{a}^{-}$ are the 4-accelerations measured on the outside and inside of the shell, respectively.

Problem 21.11. The vacuum geometries exterior to and interior to a collapsing spherical shell of dust are the Schwarzschild geometry

$$
\mathrm {d s} ^ {2} = - \left(1 - \frac {2 \mathrm {M}}{\mathrm {r}}\right) \mathrm {d t} ^ {2} + \left(1 - \frac {2 \mathrm {M}}{\mathrm {r}}\right) ^ {- 1} \mathrm {d r} ^ {2} + \mathrm {r} ^ {2} \mathrm {d} \Omega^ {2}
$$

for the exterior, and the flat geometry

$$
\mathbf {d s} ^ {2} = - \mathbf {\nabla d T} ^ {2} + \mathbf {\nabla d r} ^ {2} + \mathbf {\nabla r} ^ {2} \mathbf {\nabla d} \Omega^ {2}
$$

for the interior. [The radial coordinates in these metrics both, clearly, have the property that $4\pi r^2$ is the proper surface area of the spherical surfaces $r = \text{constant}$ , and $t$ or $T = \text{constant}$ .]

Show that for the collapsing spherical shell of dust the "rest mass of the shell" $\mu \equiv 4\pi R^2 (\tau)\sigma$ is constant. Here $\sigma$ is the surface mass density of the shell and the area of the shell as a function of proper shell time is $4\pi R^{2}(\tau)$ . Derive the equation of motion of the shell

$$
\mathbf {M} = \mu \left[ 1 + \left(\frac {\mathrm {d} \mathbf {R}}{\mathrm {d} \tau}\right) ^ {2} \right] ^ {\frac {1}{2}} - \frac {\mu^ {2}}{2 \mathbf {R}}
$$

and integrate the equation to find (in implicit form) $\mathbf{R}(\tau)$ in the case $\mathrm{d}\mathbf{R} / \mathrm{d}\tau = 0$ at $\mathbf{R} = \infty$ .

Problem 21.12. Find an instantaneous spatial metric which represents $N$ point masses at arbitrary positions at an instant of time symmetry.

Problem 21.13. Suppose one identifies four-vectors $\mathbf{U}^{\alpha}$ with 2-index spinors $\mathbf{U}^{\mathbf{A}\mathbf{A}'}$ by

$$
(\mathrm {U} ^ {0}, \mathrm {U} ^ {1}, \mathrm {U} ^ {2}, \mathrm {U} ^ {3}) \rightarrow 2 ^ {- \frac {1}{2}} \left[\begin{array}{l l}\mathrm {U} ^ {0} + \mathrm {U} ^ {1}&\mathrm {U} ^ {2} + \mathrm {i U} ^ {3}\\\mathrm {U} ^ {2} - \mathrm {i U} ^ {3}&\mathrm {U} ^ {0} - \mathrm {\Delta U} ^ {1}\end{array}\right].
$$

What is the analog of the Minkowski metric in spinor language? i.e. Find an $\mathbf{L}_{\mathbf{A}\mathbf{A}^{\prime}\mathbf{B}\mathbf{B}^{\prime}}$ such that $\mathbf{U}\cdot \mathbf{V} = \eta_{\alpha \beta}\mathbf{U}^{\alpha}\mathbf{V}^{\beta} = \mathbf{L}_{\mathbf{A}\mathbf{A}^{\prime}\mathbf{B}\mathbf{B}^{\prime}}\mathbf{U}^{\mathbf{A}\mathbf{A}^{\prime}}\mathbf{V}^{\mathbf{B}\mathbf{B}^{\prime}}$ . (Hint: use the spinor $(\varepsilon_{\mathbf{AB}}) = (\varepsilon^{\mathbf{AB}}) = (-1\frac{1}{0})$ .) What is the analog of a Lorentz transformation?

[Note: The spinor notation used here and in the following problems is that of e.g. F. A. E. Pirani in A. Trautman, F. A. E. Pirani, and H. Bondi, Lectures on General Relativity, Brandeis 1964 Summer Institute on Theoretical Physics (Prentice-Hall, 1965).]

Problem 21.14. Show that

(a) $\varepsilon_{\mathbf{A}[\mathbf{B}\varepsilon_{\mathbf{CD}}]} = 0$   
(b) $\xi_{\mathbf{AB}} = \xi_{(\mathbf{AB})} + \frac{1}{2}\varepsilon_{\mathbf{AB}}\xi_{\mathbf{C}}^{\mathrm{C}}$

where $\xi_{\mathbf{AB}}$ is an arbitrary 2-spinor. [Note: This problem and the two following were suggested by T. Sejnowski.]

Problem 21.15. Let $\mathbf{T_{ab}} = \mathbf{T_{AA'B'B'}}$ . Show that if $\mathbf{T_{ab}}$ is antisymmetric then its dual in a spinor representation is $*\mathbf{T_{ab}} = \frac{1}{2}\mathbf{i}(\mathbf{T_{ABB'A'}} - \mathbf{T_{BAA'B'}})$ .

Problem 21.16. Let $\mathbf{T_{ab}} = \mathbf{T_{AA'B'B'}}$ in a spinor representation. What tensor corresponds to $\mathbf{T_{BA'AB'}}$ ?

![](images/f404a62563f9fc89d13d35d8131eb87beff805cff737bd5890e6a21522d33245.jpg)

SOLUTIONS

![](images/55c13e25e78cdb65a61175bd522a92895df4d8273d4b58baf338e58e186f30b4.jpg)
