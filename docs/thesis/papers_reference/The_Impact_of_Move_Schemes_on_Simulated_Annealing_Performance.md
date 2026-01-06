The Impact of Move Schemes on Simulated
Annealing Performance

arXiv:2504.17949v1 [math.OC] 24 Apr 2025

Ruichen Xua , Haochun Wanga , Yuefan Denga,∗
a

Department of Applied Mathematics and Statistics, Stony Brook University, 100 Nicolls
Road, Stony Brook, 11794, NY, USA

Abstract
Designing an effective move-generation function for Simulated Annealing
(SA) in complex models remains a significant challenge. In this work, we
present a combination of theoretical analysis and numerical experiments to
examine the impact of various move-generation parameters—such as how
many particles are moved and by what distance at each iteration—under different temperature schedules and system sizes. Our numerical studies, carried
out on both the Lennard-Jones problem and an additional benchmark, reveal that moving exactly one randomly chosen particle per iteration offers the
most efficient performance. We analyze acceptance rates, exploration properties, and convergence behavior, providing evidence that partial-coordinate
updates can outperform full-coordinate moves in certain high-dimensional
settings. These findings offer practical guidelines for optimizing SA methods
in a broad range of complex optimization tasks.
Keywords: Simulated Annealing, Move Generation, Partial Update,
Metropolis-Hastings
Note: This manuscript is a preprint (ongoing work). We may update or revise it significantly before official publication.
∗

Corresponding author.
Email addresses: ruichen.xu@stonybrook.edu (Ruichen Xu),
haochun.wang@stonybrook.edu (Haochun Wang), yuefan.deng@stonybrook.edu
(Yuefan Deng)

1. Introduction
We address a fundamental challenge in Simulated Annealing, SA, namely
designing effective proposal mechanisms under a fixed total variance for proposed moves. We study how allocating this variance across a smaller subset
of coordinates at each iteration, rather than across all coordinates at once,
can significantly improve acceptance rates and accelerate chain mixing in
Metropolis-Hastings-based implementations.
Simulated Annealing, SA, has been extensively investigated since its inception, largely because of its remarkable ability to escape local minima when
tackling complex non-convex optimization problems [1, 2, 3]. A key factor
influencing performance and convergence is the move-generation strategy,
also referred to as the neighborhood or perturbation mechanism. Early theoretical research showed that convergence to the global optimum requires
an ergodic move set in combination with a sufficiently slow cooling schedule [3, 4, 5]. As a result, numerous studies have investigated how neighborhood size and structure influence the ability to traverse the state space,
overcome energy barriers, and achieve an effective balance between local and
global exploration [6, 7, 8]. Larger or more diverse neighborhoods can extend
the search to far-reaching regions and escape deeper local minima, yet they
may raise the computational burden per iteration [9, 10]. Various adaptive,
multi-scale, and temperature-dependent move-generation methods have been
proposed to further enhance convergence without compromising theoretical
guarantees [11, 12, 13, 14]. In summary, theoretical and empirical results
consistently highlight the critical role of the move-generation strategy in determining both the efficiency and reliability of SA for a wide spectrum of
optimization tasks.
Partial-coordinate or blockwise move-generation strategies in SA involve
modifying only a subset of variables at each iteration rather than updating the entire solution state. From a theoretical viewpoint, such localized
moves preserve the essential convergence properties of SA. In seminal work,
Geman employed a coordinate-wise Gibbs sampler with annealing for image
restoration and established that this single-site update scheme converges to
a global optimum under appropriate cooling schedules [15]. In more general
settings, SA Markov chains with partial updates remain ergodic and converge globally given suitably slow cooling rates [16, 17]. Fully synchronous
updates that attempt to change all coordinates simultaneously may break
certain convergence conditions, while randomized partial updates tend to
2

avoid these pitfalls.
From a practical standpoint, partial-coordinate proposals often yield higher
acceptance rates and more efficient exploration in high-dimensional optimization. Restricting proposed moves to a small number of coordinates at a time
mitigates the detrimental effects of large collective perturbations, which can
turn the process into a low-performing random walk. Many successful applications illustrate the advantages of blockwise SA. In molecular modeling
and materials science, SA is often implemented by displacing a single atom or
rotating a single bond at a time, which allows the search to navigate complex
energy landscapes efficiently [18]. Wille’s study of atomic clusters demonstrates that single-atom moves discover minimum-energy configurations effectively. In machine learning, coordinate-wise moves manifest as techniques
such as Gibbs sampling, used in training Boltzmann machines and other
high-dimensional models [15]. Similarly, in large-scale logistics problems, for
example routing or scheduling, SA-based heuristics commonly adjust only a
small portion of the solution to explore the search space efficiently [19]. As
one illustration, Osman proposed a vehicle-routing SA that used localized
route modifications and tabu search to strike a balance between diversification and intensification in a complex high-dimensional landscape.
We present a fresh theoretical perspective by recasting SA as a Markov
Chain Monte Carlo, MCMC, process operating at different temperatures,
revealing how acceptance behavior and chain efficiency are governed by how
proposal variance is allocated across coordinates. This perspective clarifies
the connection observed in adaptive-proposal methods [12, 9]: when fewer
coordinates are updated, the resulting moves are more moderate, leading to
higher acceptance rates and faster mixing. We demonstrate these principles
on the Lennard-Jones potential, showing that limiting the dimensionality
of proposed moves, while maintaining a fixed total variance, dramatically
enhances convergence in high-dimensional settings. Finally, we offer practical
recommendations suggesting that updating smaller subsets of coordinates can
surpass the performance of full-dimensional updates in a range of real-world
scenarios, highlighting an important yet under-explored design parameter in
SA.
2. MCMC and SA for Optimization
We consider the global optimization problem minx∈X f (x), where X ⊂ Rd
is non-empty and compact, and f ∈ C 1 (X; R).
3

This optimization problem (2) thus consists of identifying a point x ∈ X
that minimizes f . In the stochastic search paradigm, the Metropolis-Hastings
(MH) algorithm [20] underpins MCMC methods for sampling from complex
distributions. SA [1] extends these ideas by introducing a temperature schedule that decreases over time, concentrating the MCMC sampling near global
minimizers of f [2, 3]. Ensuring a sufficient number of MCMC iterations
at each temperature, along with an appropriate cooling scheme, can significantly increase the probability of discovering the global optimum.
2.1. MCMC
Markov chain Monte Carlo (MCMC) techniques are designed to generate
samples from a target probability distribution π defined on a state space X .
The goal is to construct a Markov chain {Xt } that leaves π invariant and
converges to π over time. Under irreducibility and aperiodicity, Chib and
Greenberg demonstrated that long-run sample averages computed from such
a chain almost surely approximate expectations taken with respect to π [20].
A standard procedure for constructing such a chain is the Metropolis–
Hastings (MH) algorithm, described in Algorithm 1. The method begins at
an initial state x0 ∼ µ0 . At each iteration, a candidate point yk is drawn
from a proposal distribution Qd (xk , ·) with density qd (xk , yk ). An acceptance
probability is then computed as
p(xk , yk ) = 1 ∧

π(yk ) qd (yk , xk )
,
π(xk ) qd (xk , yk )

and a uniform random variable uk ∼ Uniform(0, 1) determines whether to
accept or reject the proposal. If uk ≤ p(xk , yk ), the next state is set to yk ,
otherwise the chain remains at xk .
The induced transition kernel Pd for the chain can be written as
h Z
i
Pd (x, dy) = p(x, y) Qd (x, dy) + 1 − p(x, z) Qd (x, dz) δx (dy),
X

where δx denotes the Dirac measure at x. One verifies that
π(x) p(x, y) qd (x, y) = π(y) p(y, x) qd (y, x),
which ensures π is invariant under Pd . When the chain is irreducible and
aperiodic (for instance, by ensuring qd (x, y) > 0 on the support of π and
allowing self-transitions through rejection), it converges in distribution to π.
4

Algorithm 1 Metropolis–Hastings Algorithm
1: Initialization: draw x0 ∼ µ0 .
2: for k = 1, 2, . . . do
3:
Propose yk ∼ Qd (xk , ·).
4:
Compute the acceptance probability
p(xk , yk ) = 1 ∧

π(yk ) qd (yk , xk )
.
π(xk ) qd (xk , yk )

5:
Draw uk ∼ Uniform(0, 1).
6:
if uk ≤ p(xk , yk ) then
7:
xk+1 ← yk (accept)
8:
else
9:
xk+1 ← xk (reject)
10:
end if
11: end for

By the ergodic argument from Ref. [20], sample averages taken along the
chain approximate integrals with respect to π:
n

1X
g(Xt ) −−−→
n→∞
n t=1

Z
g(x) π(dx) almost surely.
X

Thus, the Metropolis–Hastings sampler provides a flexible and general-purpose
method for generating approximate samples from π, allowing the evaluation
of expectations via empirical means.
2.2. SA
Simulated Annealing [1] is a stochastic optimization technique that applies MCMC at a decreasing sequence of temperature levels {Tk }. At temperature T , the target distribution is the Boltzmann distribution
i
h
f (x)
πT (x) ∝ exp − T .
As T → 0, this distribution concentrates on the global minimizer set S :=
{ x : f (x) = f ∗ }, where f ∗ is the global minimum value of f .
Under suitable cooling schedules {Tk } and sufficiently many MCMC steps
{Nk } at each stage, classical results [16] show that xk → S in probability,
5

Algorithm 2 Simulated Annealing (SA)
1: Initialization:

choose x0 , a temperature T0 > 0, and schedules

{Tk }, {Nk }.
2: for k = 1, 2, 3, . . . do
3:
Run Metropolis–Hastings (Algorithm 1) for Nk iterations targeting:


f (x)
.
πTk (x) ∝ exp −
Tk
4:
Let xk+1 be the final state of these MH updates.
5:
Decrease Tk .
6: end for

i.e.,
lim P xk ∈ Sϵ



k→∞

= 1 for all ϵ > 0,

where Sϵ = { x : f (x) ≤ f ∗ + ϵ}. Hence,
lim P xk ∈ S

k→∞



= 1.

Thus, the algorithm converges to a global minimizer of f with high probability if the temperature decreases slowly enough and each MCMC run at
temperature Tk is sufficiently long.
3. Performance Analysis of SA
3.1. Theoretical Analysis
This section builds on the preliminaries in Section 2 to analyze how
MCMC performance metrics—such as acceptance rate and autocorrelation
times—impact SA in high dimensions. We focus on partial-coordinate MH
proposals, which selectively update a subset of coordinates at each iteration. We then formalize these proposals and discuss why they help avoid
severe acceptance-rate decay. We then present theoretical results showing
how partial-coordinate moves can significantly improve mixing and maintain
viable acceptance probabilities
during SA.

Let π(x) ∝ exp − f (x)
be
a
strictly
positive target distribution defined on
T
N
R . To alleviate the difficulties of high-dimensional sampling, we consider
a partial-coordinate update that perturbs only d components of x at each
6

iteration. A subset Sd ⊂ {1, . .. , N } of size d is chosen with some probability
mass function P (Sd ) on all Nd possible subsets. Then, for i ∈ Sd , a proposal
increment δi is drawn from a user-specified distribution Qi (δi ) with finite
mean and variance, while for i ∈
/ Sd , the coordinate remains unchanged.
Hence the candidate x′ ∈ RN is given by

xi + δi , i ∈ Sd ,
x′i =
x ,
i∈
/ Sd .
i
A standard M-H acceptance rule [21] is used:
p(x, x′ ) = 1 ∧

e ′ → x)
π(x′ ) Q(x
,
e → x′ )
π(x) Q(x

e → x′ ) denotes the probability density of proposing x′ when at x;
where Q(x
e ′ → x) = Q(x
e → x′ ) and p(x, x′ ) reduces
if each Qi is symmetric, then Q(x
′
)
.
to 1 ∧ π(x
π(x)
Under the setup, suppose each proposal distribution Qi (·) is non-degenerate
and P (Sd ) > 0 for all valid subsets Sd . Then the partial-coordinate M–H kernel K(x, dx′ ) admits π(x) as a stationary distribution. If K is also irreducible
and aperiodic on the support of π, then π is the unique invariant measure.
In practice, this approach can mitigate high-dimensional sampling challenges
by controlling the variance of each update and maintaining an acceptable
Metropolis–Hastings acceptance ratio. By breaking the parameter space into
lower-dimensional subsets and tuning the proposal distributions Qi (·) accordingly, one can avoid making excessively large moves in high dimensions while
also preventing overly small moves that cause slow exploration. As a result, the Markov chain can achieve a balance between adequately exploring
the space and maintaining a reasonable acceptance rate, thereby improving
mixing and overall efficiency in high-dimensional sampling problems.
2
Consider the Markov chain Xtσ ,d generated by partial-coordinate M-H
with proposal variance σ 2 and subset size d. The lag-ℓ autocorrelation of
(σ,d)
{f (Xt )} is


E (f (Xt ) − f¯)(f (Xt+ℓ ) − f¯)
(σ,d)


ρf (ℓ) =
,
E (f (Xt ) − f¯)2
where f¯ is the stationary mean of f (Xt ). Suppose the acceptance probability
remains bounded away from zero as σ 2 increases. Under these conditions,
7

two main observations
hold:
first, if acceptance remains non-negligible for


σ,d
2
large σ , then E |∆ft | grows with σ 2 ; second, for each ℓ ≥ 1, ρσ,d
f [ℓ]
tends to decrease as σ 2 grows, though strict monotonicity may fail unless
strong conditions on the target distribution and proposal mechanism are
satisfied. Moreover, reducing the subset size d helps maintain a nonvanishing
acceptance rate in high-dimensional settings, thereby enabling larger effective
moves and faster mixing.
Let p denote the acceptance probability of the partial-coordinate MH
update, which by hypothesis is bounded below by some positive constant
p0 > 0 as σ 2 grows. Because the proposal variance in the chosen d coordinates
scales with σ 2 , the typical size of a proposed move in those coordinates is
on the order of σ. Whenever a move is accepted, the resulting difference
(σ,d)
∆ft
can be approximated using a local Taylor expansion in the selected
coordinates. Larger steps in parameter space tend to produce larger changes
(σ,d)
in f , so the expected absolute increment, E[|∆ft |], is nondecreasing as σ 2
grows. Formally,


(σ,d)
(σ,d)
E[|∆ft |] ≥ p0 E |∆ft | move accepted ,
and the conditional expectation on the right increases in σ. By standard
(σ,d)
monotonicity arguments, E[|∆ft |] thus grows with σ 2 .
Because the acceptance probability p is bounded away from zero, increasing σ 2 allows the chain to traverse the state space more broadly with each
accepted move, thereby accelerating mixing and reducing successive correlations. A coupling argument formalizes this: consider two copies of the
Markov chain initiated at different points. When σ 2 is larger, these two
copies converge more rapidly to the same state with high probability, implying lower correlation over finite lags. In particular, as σ 2 grows, successive
(σ,d)
states are less likely to remain close to each other, thus driving ρf (ℓ) down(σ,d)

ward. Hence ρf

(ℓ) decreases monotonically in σ 2 for each ℓ ≥ 1.

When N is large, raising σ 2 for all coordinates simultaneously typically forces
the acceptance probability p to become unacceptably small. In contrast,
updating only a subset of d coordinates avoids collapsing p and still benefits
from broader proposals in the chosen coordinates. This partial-coordinate
strategy thus enables faster mixing in high-dimensional settings, balancing a
reasonable acceptance rate and an effective move size.
8

(σ,d)

Let {Xt } be the Markov chain generated by the MH kernel Pσ,d , under
which d distinct coordinates are perturbed by i.i.d. Gaussian increments of
(σ,d)
variance σ 2 . By stationarity and reversibility, each Xt
follows the same
2
distribution π, and for any function g ∈ L (π),
h
i


(σ,d) 
(σ,d) 
E g Xt+1 g Xt
= Eπ g(X) Pσ,d g (X) .
In particular, if we set g(X) = f (X) − Eπ [f (X)], then Eπ [g(X)] = 0. The
(σ,d) 
lag-t autocorrelation in f Xt
is
h
i
(σ,d) 
(σ,d) 
E g X0
g Xt
(σ,d)


ρf (t) =
.
Eπ g(X)2
Let {λi (σ, d)} be the real eigenvalues of the Markov operator P
Pσ,d acting
on L2 (π), with 1 = λ1 (σ, d) ≥ |λ2 (σ, d)| ≥ . . . . We can write g = i βi ϕi in
the eigenbasis of Pσ,d . Then
h
i
X 



t
t
E g(X0 ) g(Xt ) = Eπ g(X) Pσ,d
g (X) =
βi2 λi (σ, d) .
i

Hence,

t
2
β
λ
(σ,
d)
i
i i
P 2
.
=
i βi

t
(σ,d)
For large t, the dominant term is λ2 (σ, d) , so ρf (t) is tied closely to
|λ2 (σ, d)|.
(σ,d)
ρf (t)

P

Increasing σ 2 augments the size of proposals in the selected coordinates.
Attempting to update all N coordinates with large σ 2 often drives p to nearzero in high dimensions. By restricting updates to d coordinates, one keeps
p at a moderate level yet still obtains meaningful shifts in Xt , which disrupts
(σ,d)
the chain’s tendency to remain near its previous state, reducing ρf (t). A
more formal argument leverages diffusion approximations for Metropolis-like
samplers [22] or bounds on local conductance [23].
In summary, enlarging the proposal amplitude in only d coordinates helps
maintain a sensible acceptance probability p while enabling substantial motion in parameter space, thereby boosting the chain’s mixing. Mathematically, this appears as a reduction in |λ2 (σ, d)| and a monotonic drop in
9

(σ,d)

ρf (t). Adjusting d adds an additional tuning mechanism for proposal design, and hence completes the argument regarding improved mixing through
partial-coordinate updates.
We now analyze how varying the number of updated coordinates d influences both the acceptance rate p and the autocorrelation of the Metropolis–
Hastings sampler. Suppose the proposal y ∈ RN is generated by perturbing
d randomly selected components of the current state x ∈ RN :
(
xi + δi , i ∈ Sd ,
yi =
(3.4)
xi ,
i∈
/ Sd ,
where Sd ⊂ {1, 2, . . . , N } has |Sd | = d, and each δi ∼ N (0, σ 2 ) is drawn
independently. The Metropolis–Hastings acceptance probability is
h
 i
p(x, y) = 1 ∧ exp − f (y) − f (x) /T ,
(3.5)
where f is the objective function, and T > 0 is an effective temperature.
To evaluate the average acceptance probability, note that
i
h
(x)
.
R(y | x) = exp − f (y)−f
T
Define
Z = log R(y | x) = −

f (y) − f (x)
∆f
= −
.
T
T

Z ∞

Z 0

Then




E 1∧R = E 1∧eZ =

z

1∧e



Z ∞

e fZ (z) dz +

fZ (z) dz =

−∞

z

−∞

fZ (z) dz.
0

In order to approximate Z for large N and partial-coordinate updates, we
apply a second-order Taylor expansion of f (y) around x in the d perturbed
coordinates.
Let y = x + ξ, where ξ ∈ RN has exactly d nonzero components (indexed
by Sd ) and each active entry δi ∼ N (0, σ 2 ). Then
f (y) ≈ f (x) + ∇f (x)⊤ ξ + 21 ξ ⊤ ∇2 f (x) ξ.
Hence
∆f = f (y) − f (x) ≈ ∇f (x)⊤ ξ + 12 ξ ⊤ ∇2 f (x) ξ.
10

Thus

1
1 ⊤ 2
∆f
≈ − ∇f (x)⊤ ξ −
ξ ∇ f (x) ξ.
T
T
2T
We now compute the first three cumulants (central moments) of Z:
We consider a fixed subset Sd ⊂ {1, 2, . . . , N } of size d. Let g = ∇f (x) ∈
N
R with components gi , and let H = ∇2 f (x) = (hij )1≤i,j≤N . At each update,
we perturb only the coordinates i ∈ Sd by δi ∼ N (0, σ 2 ) independently, while
for i ∈
/ Sd , δi = 0. Define
(
Gaussian(0, σ 2 ), i ∈ Sd ,
ξ = (δ1 , δ2 , . . . , δN )⊤ with δi =
0,
i∈
/ Sd ,
Z = −

and

∆f
.
T
A second-order Taylor expansion of f (x + ξ) around x in the active coordinates yields
X
X
hij δi δj + (higher-order terms),
f (x + ξ) = f (x) +
gi δi + 12
∆f = f (x + ξ) − f (x),

Z = −

i,j∈Sd

i∈Sd

where gi = ∂f (x)/∂xi and hij = ∂ 2 f (x)/∂xi ∂xj . Neglecting higher-order
terms (to focus on the exact second-order contributions in the expansion),
we set
X
X
hij δi δj ,
∆f =
gi δi + 12
i,j∈Sd

i∈Sd

thus
Z = −

1 X
1 X
gi δi −
hij δi δj .
T i∈S
2 T i,j∈S
d

d

We now compute κ1 = E[Z], κ2 = Var[Z], and κ3 = E[(Z − κ1 )3 ] line by line,
treating ξ as a strictly d-dimensional Gaussian perturbation in the selected
coordinates.
Computation of κ1 = E[Z].
Z = −

1 X
1 X
gi δi −
hij δi δj .
T i∈S
2 T i,j∈S
d

d

11

We split Z into a linear term and a quadratic term:
1 X
1 X
gi δi ,
Zquad = −
hij δi δj .
Zlinear = −
T i∈S
2 T i,j∈S
d

d

Since δi ∼ N (0, σ 2 ) with mean zero, E[δi ] = 0. Hence
E[Zlinear ] = −

1 X
gi E[δi ] = 0.
T i∈S
d

Next, we examine the quadratic contribution:
1 X
E[Zquad ] = −
hij E[δi δj ].
2 T i,j∈S
d

For independent zero-mean Gaussians, E[δi δj ] = 0 if i ̸= j and equals σ 2 if
i = j. Thus
E[Zquad ] = −

σ2 X
1 X
hii σ 2 = −
hii .
2 T i∈S
2 T i∈S
d

d

Therefore,
κ1 = E[Z] = E[Zlinear ] + E[Zquad ] = −

σ2 X
hii .
2 T i∈S
d

If one subsequently averages over all possible subsets Sd of size d, the result
becomes
d σ2
µhess ,
κ1 = −
2T
hP
i
where µhess = d1 E
i∈Sd hii in a setting where the Hessian varies slowly
over coordinates or subsets.
Computation of κ2 = Var[Z]. By definition,
2
κ2 = Var[Z] = E[Z 2 ] − E[Z] .
We already have E[Z] from above. Hence we need E[Z 2 ]. Write
Z = Zlinear + Zquad = −

1 X
1 X
g i δi −
hij δi δj .
T i∈S
2 T i,j∈S
d

12

d

Thus
2
2
Z 2 = Zlinear
+ 2 Zlinear Zquad + Zquad
.

We will compute E[Z 2 ] by examining each piece:
2
1. E[Zlinear
]. Since

Zlinear = −

1 X
gi δi ,
T i∈S
d

we have
2
Zlinear
=

2
1 X
g
δ
.
i i
T 2 i∈S
d

Taking expectation,
1 X 2
g E[δi2 ],
T 2 i∈S i

2
E[Zlinear
] =

d

because δi are independent and each has variance σ 2 . Hence
2
E[Zlinear
] =

σ2 X 2
g .
T 2 i∈S i
d

2
2. E[Zquad
]. Here,

Zquad = −

1 X
hij δi δj .
2 T i,j∈S
d

Then
2
Zquad
=

2
1 X
h
δ
δ
.
ij i j
4 T 2 i,j∈S
d

Expanding the square,
X
2
hij δi δj
=
i,j∈Sd

X

hij hkℓ δi δj δk δℓ .

i,j,k,ℓ∈Sd

By Isserlis’ theorem (also known as Wick’s theorem for Gaussian moments),


E δi δj δk δℓ = E[δi δj ] E[δk δℓ ] + E[δi δk ] E[δj δℓ ] + E[δi δℓ ] E[δj δk ].

13

Since E[δi δj ] = σ 2 δij , the only nonzero contributions come when the
indices match up in pairs. Hence
h X
i
X
h2ij
E
hij hkℓ δi δj δk δℓ = σ 4
i,j∈Sd

i,j,k,ℓ∈Sd

+ σ4

X

hij hji + (terms with repeated indices).

i̸=j∈Sd

Because H is symmetric (the Hessian), hij = hji . A more careful
count of diagonal versus off-diagonal elements leads to a sum of squared
entries
P of H2Sd ,Sd . Thus one obtains an exact1 expression in terms of
4
σ
i,j∈Sd hij . Multiplying by the prefactor 4 T 2 yields
2
E[Zquad
] =

σ4 X 2
h .
4 T 2 i,j∈S ij
d

3. E[Zlinear Zquad ].

 X

1 X
Zlinear Zquad =
gi δi
hjk δj δk × (sign factor),
2 T 2 i∈S
j,k∈S
d

d

where the sign factor is (−1) · (−1) = +1. However, because δi are
zero-mean Gaussians, any triple product δi δj δk with distinct indices
has mean zero. Terms vanish unless two of the indices match, in which
case the third is left unpaired, giving zero mean. Therefore,
E[Zlinear Zquad ] = 0.
Collecting these,
2
2
E[Z 2 ] = E[Zlinear
]+E[Zquad
]+2 E[Zlinear Zquad ] =

σ4 X 2
σ2 X 2
+
g
h .
T 2 i∈S i
4 T 2 i,j∈S ij
d

d

Meanwhile,
E[Z]

2

=

σ 4  X 2
hii .
4 T 2 i∈S
d

Hence
 X 2 
2
σ2 X 2
σ4  X 2
κ2 = Var[Z] = E[Z 2 ]− E[Z] = 2
gi +
h
−
hii
.
T i∈S
4 T 2 i,j∈S ij
i∈S
d

14

d

d

Rewriting the squared-sum difference in terms of diagonal versus off-diagonal
2
2
parts leads to the standard expression involving σhess
and τhoff
if one averages
over all subsets Sd .
Computation of κ3 = E[(Z − κ1 )3 ]. The third central moment is


κ3 = E (Z − κ1 )3 .
We write
Z − κ1 =



Zlinear + Zquad



− κ1 = Zlinear +

Denote
U = Zlinear = −





Zquad − E[Zquad ] .

1 X
gi δi
T i∈S
d

V = Zquad − E[Zquad ] = −

1 X
σ2 X
hij δi δj +
hii .
2 T i,j∈S
2 T i∈S
d

d

Hence
(Z − κ1 )3 = (U + V )3 = U 3 + V 3 + 3 U 2 V + 3 U V 2 .
We use Isserlis’ theorem again to compute each expectation term-by-term.
Because U is linear in the δi and V is at most quadratic (minus its mean),
any odd product of unpaired δi has mean zero. After carefully accounting for
all index matchings, one obtains an exact sum of terms involving up to δi3 δj
or δi4 . If H is not constant in x or if one includes higher-order expansions of
f , additional contributions arise. In practice, an explicit summation reveals
that κ3 is proportional to σ 6 times a combination of Hessian elements and
possible third derivatives. We can write:


κ3 = E (Z − κ1 )3 = (finite sum of terms in gi , hij , δi ).
When averaged over subsets Sd , this yields a factor of d σ 6 times a constant
that depends on third-order derivatives. Often one denotes that constant by
µh3 or a similar notation:
κ3 = −

d σ6
µh3
T3

(if sign conventions follow a typical local expansion).

15

Thus we obtain the exact line-by-line Gaussian moment sums for κ1 , κ2 , κ3
under a second-order expansion of f and partial-coordinate perturbations in
the d selected coordinates.
Once κ1 , κ2 , κ3 have been identified for Z, one may approximate E[ 1 ∧ R ]
by assuming a specific form for the distribution of Z. A straightforward
approach is to treat Z as Gaussian with mean κ1 and variance κ2 . In this
approximation, we write

Z ∼ N κ1 , κ2 ,
and then


E 1∧eZ ≈

Z ∞
h
i
h
i
2
1
1
(z−κ1 )2
1)
√
exp − 2κ2
dz +
exp − (z−κ
dz.
e √
2κ2
2π κ2
2π κ2
0
−∞

Z 0

z

These integrals reduce to closed-form expressions in terms of the error function or the standard normal cumulative distribution function.
One can further refine the approximation by accounting for skewness
through an Edgeworth expansion. In that case, the density fZ (z) around
κ1 , κ2 is modified as

i
κ3
1  z−κ1 h
z−κ
1
H3 √κ2 ,
fZ (z) ≈ √ ϕ √κ2 1 +
κ2
6 (κ2 )3/2
where ϕ is the standard normal probability density function, and H3 (w) =
w3 − 3w. Substituting this into
Z 0
Z ∞
z
e fZ (z) dz +
fZ (z) dz
−∞

0

R

introduces additional terms involving H3 (w) eαw ϕ(w) dw, yielding an O(κ3 )
skewness correction beyond the Gaussian approximation.
Since d influences both the linear and quadratic terms in κ1 , κ2 , κ3 , raising
d generally amplifies these cumulants and lowers the acceptance probability
p. Consequently, careful selection of d and σ 2 helps maintain a nontrivial
acceptance rate while still proposing sufficiently large moves, thereby striking
a desirable balance between exploration and efficiency in high-dimensional
SA.
3.2. Experiments
We test the performance of our SA approach on the classical benchmark
problem: the Lennard-Jones (L-J) potential (3.2.1), Rosenbrock Problem
16

(3.2.2) and Hyper-Elliptic problem (3.2.3). These three examples span a
wide spectrum of continuous optimization difficulties, ranging from nearly
independent coordinates to highly coupled ones.
3.2.1. Lennard-Jones potential
The L-J potential [24] is a fundamental model in molecular physics, commonly used to describe the interaction between a pair of neutral atoms or
molecules. For N particles in a 3-dimensional space, let x1 , x2 , . . . , xN denote
their coordinates. The total LJ potential is
 
 σ 6 
X
σ 12
−
,
E(x1 , . . . , xN ) =
4ϵ
rij
rij
1≤i<j≤N
where rij = ∥xi − xj ∥ is the distance between particles i and j, while ϵ and
σ are parameters controlling the depth of the potential well and the finite
distance at which the inter-particle potential is zero, respectively. In optimization terms, finding low-energy configurations translates to minimizing
E(x1 , . . . , xN ) over R3N . This problem exemplifies a highly coupled system
where local moves can drastically alter the global structure. It serves as an
excellent stress test for simulated annealing (SA), given the abundance of
local minima.
In the Lennard-Jones setting, we examine the final energy attained by
SA under a specified cooling schedule. We set the initial and final temperatures to T0 = 2.0 and Tfinal = 0.2, respectively, and use a cooling coefficient
of α = 0.9999. Each temperature is held for Nequ = 100 steps, and the
schedule continues for Ncooling = 200 temperature reductions, yielding an
overall sequence of 20,000 SA iterations. We study problem instances of
sizes N ∈ {6, 39, 69} and, after the schedule completes, we record the minimized energy of the system. Our primary interest lies in how this final energy
depends on the number of updated coordinates at each iteration, as well as
on the manner in which total proposal variance is distributed among those
coordinates.
We measure the final energy of the LJ system at different MCMC steps,
under varying numbers of updated coordinates d and total proposal vari2
ance σtotal
. Below are illustrative tables presenting the mean and standard
deviation of final energies, each row labeling a particular d and sub-rows for
2
different σtotal
. The columns correspond to the MCMC step indices at which
final energies were recorded.
17

In this experiment, we record the final energy of theLJ system at different
MCMC steps , under varying numbers of updated coordinates d and total
2
proposal variance σtotal
. The following tables present the mean and standard
deviation of the final energies over multiple runs for three LJ problem sizes:
6, 39 and 69. Each table’s rows correspond to a particular d, with sub-rows
2
. The columns correspond to the MCMC step
for different values of σtotal
index at which the final energies were recorded.
Table 1: Relative errors (in %) for various Lennard-Jones systems (N ), number of updated
−2
coordinates (d), and σtotal
∈ {200, 100, 10}.

N

d

1
2
6 4
6
1
2
4
39 8
16
32
39
1
2
4
8
89 16
32
64
89

200
0.85 ± 0.20
0.89 ± 0.20
0.92 ± 0.20
0.99 ± 0.20
5.56 ± 0.60
5.66 ± 0.60
5.70 ± 0.60
5.80 ± 0.70
6.11 ± 0.70
6.14 ± 0.70
6.04 ± 0.60
8.21 ± 1.00
8.33 ± 1.00
8.64 ± 1.00
9.09 ± 1.10
9.50 ± 1.20
9.75 ± 1.40
9.85 ± 1.30
9.96 ± 1.40

2
1/σtotal
100
0.96 ± 0.30
1.07 ± 0.20
1.22 ± 0.30
1.32 ± 0.30
5.74 ± 0.50
5.82 ± 0.70
6.23 ± 0.60
6.58 ± 0.70
7.07 ± 0.80
7.41 ± 0.80
7.31 ± 0.80
8.51 ± 0.90
8.92 ± 1.00
9.61 ± 1.10
10.50 ± 1.20
11.53 ± 1.50
12.25 ± 1.70
12.75 ± 1.70
12.94 ± 1.90

10
2.16 ± 1.00
3.65 ± 1.20
5.81 ± 1.40
6.76 ± 1.50
7.90 ± 1.10
10.60 ± 1.30
15.38 ± 1.30
21.20 ± 1.50
26.19 ± 1.80
29.70 ± 2.10
30.88 ± 2.30
12.08 ± 1.40
15.70 ± 1.50
21.94 ± 1.80
29.82 ± 2.50
37.54 ± 2.60
42.49 ± 2.80
46.06 ± 2.60
46.30 ± 2.70

In Table 1, we report the relative errors with respect to the true minimum energies for Lennard-Jones systems of sizes N ∈ {6, 39, 89}. Each row
corresponds to a specific (N, d) pair, where d is the number of coordinates up−2
∈
dated per Metropolis-Hastings proposal, and each column indicates(σtotal
{200, 100, 10}. The entries list the mean relative error multiplied by 100,
along with its standard deviation.
−2
We observe that, at fixed σtotal
, increasing d generally increases the relative error, indicating that spreading the same proposal variance over more
18

coordinates tends to produce larger, less frequently accepted moves. More−2
over, when σtotal
is smaller, this effect becomes especially pronounced for
large d. Finally, smaller problems achieve consistently lower relative errors
2
are high. These results
than larger systems, especially when both d and σtotal
underscore the importance of tuning both the number of updated coordinates
and the overall proposal variance to achieve accurate solutions in LennardJones simulations.

Figure 1: Violin plots of the relative errors, (Best−BestMin)/|BestMin|, for Lennard-Jones
systems of sizes N = 6, 39, 89 at Step = 100,000. Each subplot has a custom width ratio
of 4:7:8, and the horizontal axis shows d (the number of coordinates moved). Colors (red,
−2
green, blue) indicate three inverse-variance settings σtotal
= 200, 100, 10. The vertical
range is restricted to [0, 0.6], with labels N = 6, 39, 89 placed in the upper region of each
subplot. A single figure-level legend at the bottom summarizes the three variance cases.

3.2.2. Rosenbrock Problem
We also tested the partial-coordinate Simulated Annealing (SA) schemes
on the Rosenbrock function [25], a classic benchmark in nonlinear optimization. Recall that the Rosenbrock function in N dimensions is given by
f (x) =

N
−1h
X

i
100 (xi+1 − x2i )2 + (1 − xi )2 ,

x = (x1 , . . . , xN ) ∈ RN ,

i=1

with a global minimum of f (x) = 0 at x1 = x2 = · · · = xN = 1. This problem
features a narrow “banana-shaped” valley, which is notoriously difficult for
local methods.
19

Figure 2: Heatmap (left) and contour plot (right) for the 2D Rosenbrock function f (x, y) =
2
(1 − x)2 + 100 y − x2 with logarithmic color scale. The heatmap covers the domain
[−1.5, 1.5] × [−1.5, 1.5], and a red rectangle indicates the smaller region [0.5, 1.5] × [0.5, 1.5]
for the contour plot.
−2
Table 2 shows the final absolute errors across combinations of σtotal
∈
{6000, 9000, 12000}, partial-update size d, and problem dimension N =
−2
30, 72, 200. When σtotal
is lower, errors remain small for N = 30 and 72, but
−2
can grow for N = 200. As σtotal
increases , the mean errors for N = 200 can
spike further, since more aggressive proposals are accepted less frequently
later in the annealing schedule. Smaller update sizes generally show moder−2
ate errors in lower-dimensional problems; however, when dimension and σtotal
both grow, the errors can escalate. In contrast, moderate partial updates
strike a balance between acceptance rate and step size, but with increasing
variability for higher N . Overall, the data highlight that both the parameter
−2
p and the inverse variance σtotal
strongly influence the convergence pace and
final accuracy on this classically ill-conditioned problem.

3.2.3. Hyper-Elliptic proble
In this section, we examine a hyperelliptic-like function to illustrate how
partial-coordinate simulated annealing (SA) performs in high-dimensional
settings. Figure 4 offers a two-dimensional visualization of the function
f (x, y) = 2x2 +y 2 , highlighting both its global structure (via a heatmap) and
20

Figure 3: Comparison across three problem sizes (N=30, 72, and 200). The legend at the
top shows different d values for acceptance rate (solid lines) and best value (dashed lines).

21

Table 2: Absolute errors for Rosen dataset across settings
N
2
1/σtotal

d

30

72

200

6000

1
2
3
6

(5.64 ± 8.01) × 10−4
(1.97 ± 2.21) × 10−3
(5.35 ± 5.48) × 10−3
(1.35 ± 0.64) × 10−2

(8.62 ± 10.14) × 10−4
(3.96 ± 3.70) × 10−3
(9.04 ± 5.78) × 10−3
(3.19 ± 0.77) × 10−2

(9.58 ± 17.99) × 10−2
(3.21 ± 5.94) × 10−1
(5.52 ± 10.60) × 10−1
(1.74 ± 2.67) × 100

9000

1
3
9

(1.26 ± 1.73) × 10−3
(8.42 ± 7.21) × 10−3
(3.72 ± 1.16) × 10−2

(1.88 ± 2.10) × 10−3
(2.10 ± 1.30) × 10−2
(1.00 ± 0.22) × 10−1

(4.08 ± 3.48) × 10−1
(1.49 ± 2.31) × 100
(2.53 ± 4.92) × 100

12000

1
2
3
4
6

(1.69 ± 2.08) × 10−3
(8.63 ± 10.49) × 10−3
(1.62 ± 1.27) × 10−2
(2.64 ± 1.43) × 10−2
(5.44 ± 2.67) × 10−2

(1.89 ± 2.22) × 10−3
(1.64 ± 1.76) × 10−2
(3.99 ± 2.94) × 10−2
(6.10 ± 2.45) × 10−2
(1.29 ± 0.37) × 10−1

(7.36 ± 4.55) × 10−1
(2.36 ± 1.97) × 100
(3.24 ± 3.89) × 100
(4.52 ± 5.58) × 100
(4.51 ± 7.39) × 100

finer local contours (via a smaller zoomed-in region). By extending this idea
to higher dimensions, we replicate the core challenge of navigating elongated
valleys and “flat” directions that can slow convergence. We vary the partial2
), and the dimension N
update size d, the total proposal variance (1/σtotal
to assess how robustly partial-coordinate SA handles this hyperelliptic-like
landscape. As shown in Table 3, tuning the combination of these parameters
plays a crucial role in maintaining a balance between adequate exploration
and sufficient acceptance rates, particularly when N becomes large.
In our problem setting, the initial temperature was set to T0 = 2.0. We
then cooled the system to T = 0.2 using a cooling factor of α = 0.9999. An
equilibration phase of Nequ = 100 iterations was carried out before initiating
a further cooling phase of Ncooling = 200 steps. Throughout these simulations,
the system size was varied in N ∈ {6, 39, 69}.
2
Table 3 reports the final absolute errors for each combination of 1/σtotal
∈
{600, 900, 1200}, partial-update size d, and problem dimension N ∈ {30, 72, 200}.
−2
As σtotal
increases, the proposals become bolder, which can help in escaping local traps but also risks diminishing acceptance rates at later stages.
For lower dimensions, even relatively large d values maintain small errors,
−2
whereas high N exhibits more variation, especially when d grows and σtotal
is large. In short, these results confirm that partial-coordinate SA can effectively handle the hyperelliptic-like constraints, though the interplay between
partial-update size and proposal variance must be tuned to balance acceptance rates with sufficiently rapid exploration.

22

Figure 4: Heatmap (left) and contour plot (right) for the hyperelliptic-like function
f (x, y) = 2x2 + y 2 in 2D. The heatmap spans the domain [−2, 2] × [−2, 2], and a red
rectangle highlights the smaller region [−0.2, 0.2] × [−0.2, 0.2] on which the contour plot
is drawn.

4. Conclusions
We have investigated the role of partial-coordinate moves in Metropolis–
Hastings-based Simulated Annealing and demonstrated that selectively updating smaller subsets of coordinates can significantly improve performance
in high-dimensional settings. Our theoretical analysis showed that partialcoordinate proposals help sustain a nontrivial acceptance rate when scaling
the overall proposal variance, thereby maintaining larger effective step sizes
and enhancing the chain’s mixing properties. In particular, we quantified how
the acceptance probability and autocorrelation depend on the dimensionality
of the proposal and derived approximate expressions for key MCMC metrics,
including acceptance probabilities and third-order corrections via Edgeworth
expansions.
Extensive numerical experiments further confirmed that adjusting the
number of coordinates d and distributing the total proposal variance judiciously can yield substantial gains in optimization accuracy. On LennardJones clusters and high-dimensional benchmark problems such as Rosenbrock functions, partial-coordinate SA outperformed full-coordinate updates
23

Figure 5: Comparison across three problem sizes (N=30, 72, and 200). The legend at the
top shows different d values for acceptance rate (solid lines) and best value (dashed lines).

24

Table 3: Absolute error for Hyper dataset across settings
N
2
1/σtotal

d

30

72

200

600

1
2
3
6

(4.00 ± 1.00) × 10−6
(1.42 ± 0.32) × 10−4
(7.39 ± 1.72) × 10−4
(3.20 ± 0.51) × 10−3

(3.20 ± 0.60) × 10−5
(7.85 ± 1.22) × 10−4
(3.19 ± 0.46) × 10−3
(1.06 ± 0.13) × 10−2

(2.00 ± 1.00) × 10−6
(7.20 ± 0.76) × 10−4
(4.52 ± 0.43) × 10−3
(2.12 ± 0.15) × 10−2

900

1
3
9

(6.00 ± 2.00) × 10−6
(1.55 ± 0.32) × 10−3
(9.77 ± 1.49) × 10−3

(4.60 ± 0.80) × 10−5
(6.62 ± 0.84) × 10−3
(2.84 ± 0.29) × 10−2

(5.00 ± 1.00) × 10−6
(1.00 ± 0.09) × 10−2
(6.20 ± 0.39) × 10−2

1200

1
2
3
4
6

(8.00 ± 2.00) × 10−6
(4.50 ± 1.04) × 10−4
(2.67 ± 0.56) × 10−3
(5.97 ± 1.15) × 10−3
(1.23 ± 0.20) × 10−2

(5.90 ± 1.20) × 10−5
(2.48 ± 0.43) × 10−3
(1.14 ± 0.17) × 10−2
(2.18 ± 0.30) × 10−2
(4.00 ± 0.50) × 10−2

(8.00 ± 1.00) × 10−6
(2.69 ± 0.28) × 10−3
(1.75 ± 0.15) × 10−2
(4.09 ± 0.33) × 10−2
(8.24 ± 0.56) × 10−2

by achieving lower energies and faster convergence to near-optimal solutions,
especially for larger problem dimensions.
These results emphasize the importance of designing proposal mechanisms that carefully balance acceptance probability and exploration in highdimensional Simulated Annealing. While we focused on Gaussian increments
and isotropic proposals, the same principles can be extended to non-Gaussian
or adaptive strategies. Future research directions include refining the subset
selection procedure (for instance, using adaptive or problem-specific heuristics), incorporating multiple scales of step sizes within partial-coordinate
updates, and applying these methods to more complex molecular or machinelearning models. Our findings suggest that partial-coordinate move strategies offer a flexible and efficient avenue for tackling large-scale optimization
challenges via Simulated Annealing.
References
[1] S. Kirkpatrick, C. D. Gelatt, and M. P. Vecchi. Optimization by simulated annealing. Science, 220(4598):671–680, 1983.
[2] V. Černý. Thermodynamical approach to the travelling salesman problem: An efficient simulation algorithm. Journal of Optimization Theory
and Applications, 45(1):41–51, 1985.

25

[3] S. Geman and D. Geman. Stochastic relaxation, gibbs distributions,
and the bayesian restoration of images. IEEE Transactions on Pattern
Analysis and Machine Intelligence, 6(6):721–741, 1984.
[4] Peter J. M. Van Laarhoven and Emile H. L. Aarts. Simulated Annealing:
Theory and Applications, volume 37. Springer, Dordrecht, 1987.
[5] B Hajek. Cooling schedules for optimal annealing. Mathematics of
Operations Research, 13(2):311–329, 1988.
[6] L Goldstein and MS Waterman. Neighborhood size in the simulated annealing algorithm. In American Journal of Mathematical and
Management Sciences, volume 8, pages 409–423, 1988.
[7] John N Tsitsiklis. Markov chains with rare transitions and simulated
annealing. Mathematics of Operations Research, 14(1):70–90, 1989.
[8] V. Granville, M. Krivanek, and J. P. Rasson. Simulated annealing:
A proof of convergence. IEEE Transactions on Pattern Analysis and
Machine Intelligence, 16(6):652–656, 1994.
[9] M. Locatelli. Simulated annealing algorithms for continuous global optimization: Convergence conditions. Journal of Optimization Theory and
Applications, 104:121–133, 2000.
[10] Marc C. Robini. Theoretically grounded acceleration techniques for simulated annealing. In Ivan Zelinka, J.I. Hidalgo, and V. Snášel, editors,
Handbook of Optimization, pages 311–335. Springer, 2012.
[11] C. G. E. Boender, A. H. G. Rinnooy Kan, G. T. Timmer, and L. Stougie.
A novel simulated annealing approach to continuous global optimization.
Global Optimization, pages 249–259, 1989.
[12] L. Ingber. Very fast simulated re-annealing.
Computer Modelling, 12(8):967–973, 1993.

Mathematical and

[13] D Mitra, F Romeo, and A Sangiovanni-Vincentelli. Convergence and
finite-time behavior of simulated annealing. Advances in Applied
Probability, 18(3):747–771, 1986.
[14] R Holley and D Stroock. Simulated annealing via sobolev inequalities.
Communications in Mathematical Physics, 115(4):553–569, 1988.
26

[15] Stuart Geman and Donald Geman. Stochastic relaxation, gibbs distributions, and the bayesian restoration of images. IEEE Transactions on
Pattern Analysis and Machine Intelligence, PAMI-6(6):721–741, 1984.
[16] Bruce Hajek. Cooling schedules for optimal annealing. Mathematics of
Operations Research, 13(2):311–329, 1988.
[17] Pablo A. Ferrari, Arnoldo Frigessi, and Roberto H. Schonmann. Convergence of some partially parallel gibbs samplers with annealing. Annals
of Applied Probability, 3(1):137–153, 1993.
[18] Luc T. Wille. Minimum-energy configurations of atomic clusters: New
results obtained by simulated annealing. Chemical Physics Letters,
133(5):405–410, 1987.
[19] Ibrahim H. Osman. Metastrategy simulated annealing and tabu search
algorithms for the vehicle routing problem. Annals of Operations
Research, 41:421–451, 1993.
[20] Siddhartha Chib and Edward Greenberg. Understanding the metropolishastings algorithm. The American Statistician, 49(4):327–335, 1995.
[21] W Keith Hastings. Monte carlo sampling methods using markov chains
and their applications. 1970.
[22] Gareth O. Roberts, Andrew Gelman, and Walter R. Gilks. Weak convergence and optimal scaling of random walk metropolis algorithms. The
Annals of Applied Probability, 7(1):110–120, 1997.
[23] P. H. Peskun. Optimum monte carlo sampling using markov chains.
Biometrika, 60(3):607–612, 1973.
[24] John E. Lennard-Jones. On the determination of molecular fields. — ii.
from the equation of state of a gas. Proceedings of the Royal Society of
London. Series A, 106(738):463–477, 1924.
[25] Howard H. Rosenbrock. An automatic method for finding the greatest
or least value of a function. The Computer Journal, 3(3):175–184, 1960.

27

