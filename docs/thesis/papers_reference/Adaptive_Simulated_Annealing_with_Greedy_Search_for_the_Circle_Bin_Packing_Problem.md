Highlights
Adaptive Simulated Annealing with Greedy Search for the Circle Bin Packing Problem
Yong Yuan,Kevin Tole,Fei Ni,Kun He,Zhengda Xiong,Jinfa Liu
• First paper to introduce the circle bin packing problem with circular items (CBPP-CI).
• Define a tangent occupying action and propose a greedy constructive algorithm for CBPP-CI.
• Design two new operations, circle perturbation and sector perturbation, to generate neighbor solutions.

arXiv:2108.03203v1 [cs.CG] 6 Aug 2021

• Propose an adaptive simulated annealing algorithm with greedy search that obtains competitive results.
• Build two sets with a total of 52 new benchmark instances with 20 to 100 circular items.

Adaptive Simulated Annealing with Greedy Search for the Circle Bin
Packing Problem
Yong Yuana,1 , Kevin Tolea,b,1 , Fei Nia , Kun Hea,∗ , Zhengda Xionga and Jinfa Liuc
a School of Computer Science, Huazhong University of Science and Technology, Wuhan 430074, China.
b Institute of Computing and Informatics, Technical University of Mombasa, Mombasa 90420 - 80100, Kenya.
c Guangzhou Key Laboratory of Multilingual Intelligent Processing, Guangdong University of Foreign Studies, Guangzhou 510006, China

ARTICLE INFO

ABSTRACT

Keywords:
Packing
Heuristics
Tangent occupying action
Adaptive simulated annealing
Greedy search

We introduce a new bin packing problem, termed the circle bin packing problem with circular items
(CBPP-CI). The problem involves packing all the circular items into multiple identical circle bins as
compact as possible with the objective of minimizing the number of used bins. We first define the
tangent occupying action (TOA) and propose a constructive greedy algorithm that sequentially packs
the items into places tangent to the packed items or the bin boundaries. Moreover, to avoid falling
into a local minimum trap and efficiently judge whether an optimal solution has been established, we
continue to present the adaptive simulated annealing with greedy search (ASA-GS) algorithm that
explores and exploits the search space efficiently. Specifically, we offer two novel local perturbation
strategies to jump out of the local optimum and incorporate the greedy search to achieve faster
convergence. The parameters of ASA-GS are adaptive according to the number of items so that they
can be size-agnostic across the problem scale. We design two sets of new benchmark instances, and
the empirical results show that ASA-GS completely outperforms the constructive greedy algorithm.
Moreover, the packing density of ASA-GS on the top few dense bins is much higher than that of
the state-of-the-art algorithm for the single circle packing problem, inferring the high quality of the
packing solutions for CBPP-CI.

1. Introduction
As a classic combinatorial optimization problem, the
packing problems aim to pack a certain number of items
into one or multiple containers without overlapping. Most
researches are for single container packing. The shape of
the container can be rectangular, square, or circular, and
the items can be rectangles or circles. As an important
branch of operational research, the packing problems have a
wide variety of applications in the logistic industry, circular
cutting, container loading, cylinder packing, etc. Meanwhile,
it has been proved to be NP-hard by (Demaine, Fekete and
Lang, 2010). Hence there is no deterministic algorithm to
find the exact solutions in polynomial time unless P = NP.
The bin packing problem (BPP) has been well studied
for multiple container packing since the 1970s (Johnson,
1973). There exist mainly two variants: the two-dimensional
rectangular bin packing problem (2D-RBPP) and the twodimensional square bin packing problem with circular items
(SBPP-CI). The 2D-RBPP aims to pack a set of rectangular
items into a minimum number of identical rectangular bins
without overlapping (Chung, Garey and Johnson, 1982).
The impact of these techniques on the practical solution of
2D-RBPP has been quite impressive (Christensen, Khan,
Pokutta and Tetali, 2017). For example, Kang and Park
(2003) propose two greedy algorithms: IFFD and IBFD.
IFFD assigns the items sequentially by the first-fit decreasing
manner, and a new bin will be initialized when there is
∗ Corresponding author

brooklet60@hust.edu.cn (K. He)

ORCID (s):

1 The first two authors contribute equally.

no more room for the packing; IBFD is a modification of
IFFD, which assigns each item to the bin with the smallest
remaining capacity. Other representative approaches include
the tabu search (Lodi, Martello and Vigo, 1999), the guided
local search (Faroe, Pisinger and Zachariasen, 2003), the
hybrid GPASP/VND approach (Parreño, Alvarez-Valdés,
Oliveira and Tamarit, 2010), and various heuristics based on
greedy method (Lodi, Martello and Monaci, 2002; Monaci
and Toth, 2006; Wei, Oon, Zhu and Lim, 2011). The SBPPCI allocates all the circular items to a minimum number of
square bins without overlap, which is first presented by He
and Dosh (2017). They further propose a greedy algorithm
with corner occupying action to improve the packing quality
by introducing the adaptive large neighborhood search (He,
Tole, Ni, Yuan and Liao, 2021).
To our knowledge, many studies have focused on multiple square or rectangular containers, while no significant
published research addresses the problem of packing with
multiple circular bins. Therefore, in this paper, we address
a new variant termed the circle bin packing problem with
circular items (CBPP-CI), which places a series of circular
items inside multiple circular bins to minimize the number of bins used. It is an important extension of the twodimensional circle packing problem (CPP), which is to pack
all circular items into a single container of the circular or
square shape to minimize the size of the container. Generally
speaking, the approaches of CPP can be classified into two
categories: constructive strategies and global optimization
strategies.
Constructive strategies sequentially pack the items into
the bin based on some rules, such as the best-local position (BLP) (Hifi and M’Hallah, 2002; Mhand and Rym,

Y. Yuan, K. Tole, F. Ni, K. He et al.: Preprint submitted to Elsevier

Page 1 of 14

ASA-GS for Solving the CBPP-CI

2004) and the maximal hole degree (MHD) (Huang, Li, Li
and Xu, 2006), which are defined to evaluate the benefit
of a partial solution. Representative heuristics include the
prune-enriched Rosenbluth method (PERM) (Lü and Huang,
2008), the augment beam search (Akeb, Hifi and M’Hallah,
2009; Akeb, Hifi and Negre, 2011), the best-fit algorithm
(BFA) (He, Huang and Jin, 2012), etc.
As the second category of approaches, global optimization strategies improve the solution iteratively based on
the initial solution. It could be further subdivided into two
categories: quasi-physical methods and meta-heuristic optimizations. The quasi-physical methods are based on a
physical gradient or human-intuitive behavior to enhance the
solutions obtained by problem-oriented heuristics (Wang,
Huang, Zhang and Xu, 2002; Lubachevsky and Graham,
1997), while meta-heuristic optimizations usually have an
evaluation function devised to employ a trade-off between
randomization and local search, with the goal of directing
and remodeling basic heuristics to generate feasible solutions. Typical algorithms include a simulated annealing
approach (SA) (Hifi, Paschos and Zissimopoulos, 2004),
monotonic basin hopping approach (MBH) (Grosso, Jamali,
Locatelli and Schoen, 2010), iterated tabu search(ITS) (Fu,
Huang and Lü, 2013), action-space-based global optimization algorithm (ASGO) (He, Huang and Yang, 2015), formulation space search (FSS) (López and Beasley, 2016),
adaptive tabu search and variable neighborhood descent
(ATS-VND) (Zhizhong, Xinguo, Kun and Zhanghua, 2018),
etc.
Most of the constructive solutions focus on the traditional CPP and are designed on the specific characteristics
of the problem. These methods are no longer applicable for
CBPP-CI because of the characteristic gap between CPP and
CBPP-CI. Moreover, although the global optimization technique can be used on CBPP-CI as a general search framework, it lacks adaptive adjustments, including the search
strategy and evaluation function. Otherwise, the search efficiency is poor, and it is hard to find an iterative optimization
method to make further improvements based on the current
solution.
As the CBPP-CI is a new problem, there are no available
benchmark instances. Following our previous works on the
square bin packing problem with circular items (SBPP-CI)
in (He et al., 2021; He and Dosh, 2017), we choose two categories of benchmarks for the single circle packing problem
(SCPP) on the packomonia website 2 and build two sets of
new benchmark instances based on them for the CBPP-CI.
For the solving method, we first propose a greedy heuristic
based on the designed tangent occupying action (TOA),
which can quickly obtain a competitive packing result. TOA
always places the current circular item tangent to any two
packed items or the bin boundary. At the same time, we also
need the packing item to have a minimum distance to the
bin boundary. In this way, items are packed as compact as
possible, and the remaining space can all gather in the center
area of a bin. To judge whether an optimal solution has been
2 www.packomonia.com

found, we continue to design adaptive simulated annealing
with greedy search (ASA-GS) method inspired by related
works (He et al., 2021; Hifi et al., 2004; Geng, Chen, Yang,
Shi and Zhao, 2011). In contrast to the TOA algorithm, we
apply a globalization approach that improves the packing
pattern iteratively. We first present an energy function to be
minimized and offer an initial packing solution. Then we try
to seek more adaptive parameter control to improve the solution quality on large-scale instances. Besides, we utilize the
greedy search strategy to achieve faster convergence. Finally,
to avoid falling into local optimal solutions, we propose
two novel perturbation strategies, and the experiments have
verified their effectiveness. Moreover, the packing density
of ASA-GS on the top few bins is much higher than the
best results for the single circle packing problem on the
packomonia website, which indicates the high quality of our
solution.
The main contributions of this work are summarized as
follows:
• We address a new and important variant of BPP
termed CBPP-CI, which comprises packing circular
items into multiple circle bins as compactly as possible to minimize the number of used bins. Moreover,
we build two sets of new benchmark instances for
CBPP-CI.
• We propose a constructive greedy algorithm based on
the devised tangent occupying action that can quickly
generate a competitive solution.
• We define an energy function for simulated annealing
and present two novel perturbation methods (sector perturbation and circle perturbation) to generate
neighbor solutions. Besides, we incorporate a greedy
search to achieve faster convergence.
• The parameters are adaptive along with the number
of items such that our algorithm can obtain the better
solution for the CBPP-CI with a broad scale.
The rest of this paper is organized as follows: Section 2
presents a formal definition of the CBPP-CI and our alternate
optimization function, which could help find denser packing
so as to minimize the objective. Section 3 gives some definitions and proposes the constructive algorithm. Section 4
presents two perturbation operators and describes the ASAGS algorithm in detail. Section 5 shows and analyzes the
experimental results. Section 6 concludes the work with
future work recommendations.

2. Preliminary
In the proposed circle bin packing problem with circular
items (CBPP-CI), we are given 𝑛(𝑛 ∈ 𝑁 + ) circular items
𝐶1 , 𝐶2 , . . . , 𝐶𝑛 with radius 𝑟1 , 𝑟2 , . . . , 𝑟𝑛 , and a set of 𝑛
identical circular bins with radius 𝑅 (w.l.g. for any circular
item 𝐶𝑖 , 𝑟𝑖 ≤ 𝑅), we aim to determine the center coordinates
of each item 𝐶𝑖 in a bin such that all items are packed

Y. Yuan, K. Tole, F. Ni, K. He et al.: Preprint submitted to Elsevier

Page 2 of 14

ASA-GS for Solving the CBPP-CI
Table 1
Variable definition.
Variable

Description

𝑛
𝐶𝑖
(𝑟𝑖
)
𝑥𝑖 , 𝑦𝑖
𝐵𝑘
𝑅
𝐼𝑖𝑘
𝑌𝑘
𝑑𝑖𝑗

Number of circular items
The 𝑖-th circular item
Radius of 𝐶𝑖
Center coordinates of 𝐶𝑖
The 𝑘-th bin
Radius of the circular bins
Indicator of whether 𝐶𝑖 is in the 𝑘-th bin
Indicator of whether the 𝑘-th bin is used
Distance between points (𝑥𝑖 , 𝑦𝑖 ) and (𝑥𝑗 , 𝑦𝑗 )

feasibly, i.e. with all circular items fitting completely inside
the bins and no overlapping exists between any pair-wise
items (i.e.(𝐶𝑖 ∩𝐶𝑗 = ∅)). The goal is to minimize the number
of used bins, denoted as 𝐾 (1 ≤ 𝐾 ≤ 𝑛).

2.1. Problem Formulation
Assume that the center of each circular bin 𝐵𝑘 is located
at (𝑅, 𝑅) in two-dimensional Cartesian coordinate system
and denote the center of each circular item 𝐶𝑖 as (𝑥𝑖 , 𝑦𝑖 ). We
can define a packing solution as 𝑋 = {< 𝑥1 , 𝑦1 , 𝑏1 >, <
𝑥2 , 𝑦2 , 𝑏2 >, … , < 𝑥𝑛 , 𝑦𝑛 , 𝑏𝑛 >}, where 𝑏𝑖 is the indicator
that the placement of item 𝐶𝑖 in the 𝑏𝑖 -th bin 𝐵𝑏𝑖 (𝑏𝑖 ∈
{1, … , 𝐾}). In order to formulate the problem, a summary
of necessary variables is listed in Table 1.
The CBPP-CI problem can be formalized as minimizing
𝐾 while satisfying the following constraints:
𝑛
∑

(1)

𝐼𝑖𝑘 = 1,

𝑘=1

where 𝐼𝑖𝑘 ∈ {0, 1} and 𝑖, 𝑘 ∈ {1, … , 𝑛}, implying that each
circular item is packed exactly once. CBPP-CI also requires
that any pair-wise items in the same bin (i.e. 𝐼𝑖𝑘 = 𝐼𝑗𝑘 = 1,
∀𝑖, 𝑗, 𝑘 ∈ {1, … , 𝑛}) must not overlap:
√
𝑑𝑖𝑗 = (𝑥𝑖 − 𝑥𝑗 )2 + (𝑦𝑖 − 𝑦𝑗 )2 ≥ (𝑟𝑖 + 𝑟𝑗 )𝐼𝑖𝑘 𝐼𝑗𝑘 . (2)
Third, to ensure that every circular item is placed entirely
inside a bin, CBPP-CI requires:
√
(𝑥𝑖 − 𝑅)2 + (𝑦𝑖 − 𝑅)2 + 𝑟𝑖 ≤ 𝑅.
(3)
Finally, we use 𝑌𝑘 to indicate whether there exist circular
items packed into a bin 𝐵𝑘 :
{
∑
1, if 𝑛𝑖=1 𝐼𝑖𝑘 > 0, 𝑖, 𝑘 ∈ {1, … , 𝑛},
𝑌𝑘 =
(4)
0, otherwise.

min 𝐾 =

𝑌𝑘 ,

𝑘=1

and clearly 1 ≤ 𝐾 ≤ 𝑛.

2.2. Optimization Function
The overall goal of the CBPP-CI is to use as few bins as
possible to pack the 𝑛 circular items 𝐶𝑖 , as shown in Eq. (5).
However, to attain the global optimum, it is necessary to
consider a more local objective function that focuses on
packing as tightly as possible. In this regard, suppose that
a packing solution 𝑋 corresponds to a partition 𝑆 = 𝑆1 ∪
𝑆2 ∪ … ∪ 𝑆𝐾 such that 𝑆𝑘 is the set of circular items that are
packed in bin 𝐵𝑘 , and 𝑘 ∈ {1, … , 𝐾}. Let 𝐴 be the area of a
bin (all bins are identical). Then, the density of packing 𝑆𝑘
into a bin 𝐵𝑘 is given by:
1 ∑
where 𝐴 = 𝜋𝑅2 .
(6)
𝜋𝑟2𝑖 ,
𝑑𝐵𝑘 (𝑋) =
𝐴 𝐶 ∈𝑆
𝑖

𝑘

Given a packing solution 𝑋 and 𝑘 ∈ {1, … , 𝑛}, let
𝑑min = min{𝑑𝐵𝑘 (𝑋)|1 ≤ 𝑘 ≤ 𝐾} and 𝑑max = max{𝑑𝐵𝑘 (𝑋)|1 ≤
𝑘 ≤ 𝐾}. A useful local optimization function is defined as
follows:
(7)

𝑣(𝑋) = 𝑑𝑚𝑎𝑥 − 𝑑𝑚𝑖𝑛 .

The greater the value of 𝑣(⋅), the higher the quality of a
feasible solution 𝑋. Since an increment in 𝑣(⋅) corresponds
to a tighter packing as some items move from sparser bins to
the denser bins.
Further, we need to minimize the value of 𝐾, i.e., to
maximize the value of −𝐾. So we define our optimization
function as:
max 𝐹 (𝑋) = −𝐾 + 𝑑𝑚𝑎𝑥 − 𝑑𝑚𝑖𝑛 .

(8)

The greater the value of 𝐹 (⋅) is, the better and tighter the
packing is.
Note that 0 ≤ 𝑑𝑚𝑎𝑥 − 𝑑𝑚𝑖𝑛 ≤ 1, this term is used
for regularization. It implies that the optimization function
is more inclined to use fewer bins, and the difference in
the number of bins is enough to weigh different solutions.
When two feasible packings use the same number of bins,
we will focus on each candidate solution’s densest bin and
the sparsest bin. The denser the densest bin is, the less the
wasted space is. The more sparse the sparsest bin is, the
more concentrated and complete the remaining still-reserved
space is, making it easier to pack the following circular
items. Therefore, we assume such a difference in density
could determine the quality of candidate solutions.

3. Tangent Occupying Action Algorithm

And the goal is to minimize the summation of 𝑌𝑘 :
𝑛
∑

We could associate the items in bin 𝐵𝑘 as an item
set, denoted as 𝑆𝑘 . So a solution can be obtained by two
steps: we first partition the items into different sets  =
⟨𝑆1 , 𝑆2 , … , 𝑆𝐾 ⟩ for the bins; then we try to pack the items
of 𝑆𝑘 into bin 𝐵𝑘 without overlapping. An optimal packing is
that the number of bins used can not be reduced any further.

(5)

This section introduces the concept of tangent occupying
action and then proposes a constructive greedy algorithm
based on this action. We want to pack circular items into the
bins as compact as possible through the tangent occupying
action to reduce the number of bins used.

Y. Yuan, K. Tole, F. Ni, K. He et al.: Preprint submitted to Elsevier

Page 3 of 14

ASA-GS for Solving the CBPP-CI

3.1. Definitions
We first provide several essential definitions, especially
the tangent occupying action.
Definition 1. (Tangent occupying action). A tangent
occupying action (TOA) is a packing action that chooses an
outside circular item to place to a position inside a bin such
that the item is tangent to any two or more packed items (the
circular bin can be regarded as a special hollow item).
Definition 2. (Quality of a feasible packing position).
For an item, the quality of a feasible packing position is
determined by the distance between the center of the packing
item and the circular bin’s boundary:
√
(9)
𝑑 (𝑥, 𝑦) = 𝑅 − (𝑥 − 𝑅)2 + (𝑦 − 𝑅)2 − 𝑟,
where (𝑥, 𝑦) is the center of the circular item. The smaller
the interval, the better the packing position.
All feasible positions are sorted in the ascending order
of 𝑑(𝑥, 𝑦) for a circular item in the current bin. A smaller
𝑑(𝑥, 𝑦) is better, which allows more concentrated free space
in favor of placing the remaining circular items. The idea is
to pack circular items nearer to the bin’s boundary.

3.2. TOA Algorithm
Algorithm 1: TOA Algorithm
Input: A vector of unassigned circle’s ID:
circle_ids, a vector of bin’s ID: bin_ids,
bin’s radius: 𝑅;
Result: For each circle 𝐶𝑖 , (find a )bin 𝐵𝑘 , and place
the circle center at 𝑥𝑖 , 𝑦𝑖 ;
1 for 𝑖 ∈ 𝑐𝑖𝑟𝑐𝑙𝑒_𝑖𝑑𝑠 do
2
𝑣𝑒𝑐𝑡𝑜𝑟 < 𝑇 𝑂𝐴 > 𝑠 = ∅ ;
3
𝑏𝑖𝑛_𝑖𝑑_𝑖𝑑𝑥 = 0;
4
while true do
5
if 𝑏𝑖𝑛_𝑖𝑑_𝑖𝑑𝑥 == 𝑏𝑖𝑛_𝑖𝑑𝑠.𝑠𝑖𝑧𝑒() then
6
return false;
7
end
8
𝑠 ← Compute feasible packing positions for
𝐶𝑖 ;
9
if 𝑠 ≠ ∅ then
10
break;
11
end
12
𝑏𝑖𝑛_𝑖𝑑_𝑖𝑑𝑥 ← 𝑏𝑖𝑛_𝑖𝑑_𝑖𝑑𝑥 + 1; // Turn to
the next bin

end
14
TOA 𝑏𝑒𝑠𝑡_𝑡𝑜𝑎 = Select the best packing
position from 𝑠 with 𝑑(𝑥, 𝑦);
15
𝑐𝑖𝑟𝑐𝑙𝑒𝑠[𝑖].𝑥 = 𝑏𝑒𝑠𝑡_𝑡𝑜𝑎.𝑝.𝑥;
16
𝑐𝑖𝑟𝑐𝑙𝑒𝑠[𝑖].𝑦 = 𝑏𝑒𝑠𝑡_𝑡𝑜𝑎.𝑝.𝑦;
17
Place the circles[i] into the bin_ids[ bin_id_idx]
bin;
18 end
13

current item, we first locate all the TOAs of the first bin
that satisfies the problem constraints. If there is no available
TOA, we seek the next bin to continue searching feasible
TOAs until at least one available TOA occurs. Among all
possible TOAs, we select the placement with the minimal
distance 𝑑(𝑥, 𝑦) and place the item at (𝑥, 𝑦) in the current
bin. The TOA algorithm iterates the above procedure until
all circular items have been loaded into the bins without
overlapping. With this process, TOA prefers positions closer
to the bin’s boundary. Hence, it packs the circular items as
compact as possible and utilizes the bin space greedily to
minimize the number of bins used.
TOA is very fast in constructing a solution, but it could
not obtain a solution with excellent quality. Therefore, we
present two novel mutations and introduce a meta-heuristic
global optimization approach called ASA-GS to improve the
solution quality.

4. Adaptive Simulated Annealing with Greedy
Search
Simulated annealing (SA) algorithm (Kirkpatrick, Gelatt
and Vecchi, 1983) has been extensively developed and
widely used in many optimization problems. It can avoid
getting trapped in the local optimum and attain better solutions by accepting worse solutions with a certain probability.
To strengthen the packing solution, we propose a boosted
algorithm called the adaptive simulated annealing with
greedy search (ASA-GS) for the CBPP-CI. Our method is
inspired by the works (He et al., 2021; Hifi et al., 2004; Geng
et al., 2011) that can guide the algorithm quickly converging
to optimal solutions.
The ASA-GS algorithm (Geng et al., 2011) is described
in Alg. 2. In ASA-GS, there are several decisions to be
made: how to define the energy function 𝑓 (⋅); how to attain
an initial solution; how to generate a neighbor solution;
how to determine the assignments of parameters such as
the probability of accepting a new solution, and the current
temperature.
In what follows, we show how one can use the principle
of the ASA-GS algorithm to solve the CBPP-CI.

4.1. Energy Function
According to our defined optimization function of the
packing problem, we define the energy function 𝑓 (⋅) as
−𝐹 (⋅) for the simulated annealing algorithm:
𝑓 (𝑋) = −𝐹 (𝑋) = 𝐾 − 𝑑𝑚𝑎𝑥 + 𝑑𝑚𝑖𝑛 .

(10)

It can be seen from Eq. (10) that minimizing the energy
function 𝑓 (⋅) is equivalent to maximizing the optimization
function 𝐹 (⋅). Therefore, the smaller the value of 𝑓 (⋅), the
better a packing solution.

4.2. Initial Packing Solution
Details of the TOA algorithm are presented in Alg. 1. It
works by packing circular items sequentially in a particular
order of their radii (e.g., from large to small). To load the

We can easily obtain an initial packing solution using 𝑛
circular bins and assigning each circular item 𝐶𝑖 in bin 𝐵𝑖 as

Y. Yuan, K. Tole, F. Ni, K. He et al.: Preprint submitted to Elsevier

Page 4 of 14

ASA-GS for Solving the CBPP-CI

4.3.1. Circle perturbation
As Alg. 3 shows, the circle perturbation strategy selects a
circular item randomly in a circular bin 𝐵𝑘 , then generates a
circular area with the item’s center as its center, the radius of
the circular area is a random number in [0, 𝑅2 ]. It guarantees
that at least one item will intersect the generated circular
area. In most cases, more than one item will cross this area
and be reassigned at each iteration.

Algorithm 2: ASA-GS Algorithm
Input : Bin radius 𝑅, a set of 𝑛 circular items
{𝐶𝑖 |1 ≤ 𝑖 ≤ 𝑛} with radii
𝑟1 , … , 𝑟𝑛 (𝑟𝑖 ≥ 𝑟𝑖+1 )
Output: A dense packing solution 𝐗 for CBPP-CI.
1 Initialize the annealing parameters 𝑡𝑠𝑡𝑎𝑟𝑡 , 𝑡𝑐𝑜𝑜𝑙 , 𝑁,
𝑡𝑔𝑟𝑒𝑒𝑑𝑦 , and set 𝑡𝑐𝑢𝑟𝑟𝑒𝑛𝑡 = 𝑡𝑠𝑡𝑎𝑟𝑡 , 𝐺 = 0 ;
2 Initialize a packing solution 𝐗𝟎 and let 𝐗 = 𝐗𝟎 ;
3 for 𝑖 ← 1 to 𝑁 do
4
Select one perturbation method between sector
perturbation and circle perturbation;
′
5
Compute 𝑑𝐸 = 𝑓 (𝑋 ) − 𝑓 (𝑋);

Algorithm 3: Pseudo-code of sampling a circle
Input : Bin 𝐵𝑘 , bin radius 𝑅
Output: A circular area with < 𝑥, 𝑦, 𝑟 >
// Each circle is represented as < 𝑥, 𝑦, 𝑟 >
1 𝑟 ← random_real(𝑅∕2); // The circle radius is r
// Randomly select a circular item from 𝐵𝑘
2 if (!𝐵𝑘 .𝑒𝑚𝑝𝑡𝑦()) then
{
}
3
𝑖 ← random_ints(1, 𝑖 ||𝐶𝑖 ∈ 𝐁𝐤 );
4 end
5 𝑥 ← 𝐶𝑖 .𝑥;
6 𝑦 ← 𝐶𝑖 .𝑦;
7 𝑐𝑖𝑟𝑐𝑙𝑒 = 𝐶𝑖𝑟𝑐𝑙𝑒(𝑥, 𝑦, 𝑟);// Generate a circle area

// See Subsection 4.3.3 and Algorithm 6 for
details
6
7
8
9
10
11
12

′

𝐗 ← Generate a new packing solution(𝑋, 𝑅);
if 𝑑𝐸 ≤ 0 then
′
𝑋 = 𝑋 ;// Accept the new solution
else
′
𝐺 = 𝐺 + 1 and compute 𝑓 (𝑋𝐺 );
if 𝐺 ≥ 𝑡𝑔𝑟𝑒𝑒𝑑𝑦 then
′
′
Select 𝑋𝑏𝑒𝑠𝑡 with condition 𝑓 (𝑋𝑏𝑒𝑠𝑡 ) =
′
′
′
𝑚𝑖𝑛(𝑓 (𝑋1 ), 𝑓 (𝑋2 ), ..., 𝑓 (𝑋𝑡
)) ;
𝑔𝑟𝑒𝑒𝑑𝑦

Algorithm 4: Pseudo-code of sampling a sector
Input : Size of the central angle Δ𝜃, is_fixed
Output: A sector with (𝛼, 𝛽)
// Each sector is represented as (𝛼, 𝛽)
1 𝛼 ← randInt(0, 360);
2 if !𝑖𝑠_𝑓 𝑖𝑥𝑒𝑑 then
3
Δ𝜃 ← 𝑟𝑎𝑛𝑑𝐼𝑛𝑡(20, 60);
4 end
5 𝛽 ← (𝛼 + Δ𝜃)%360;
6 sector = Sector(𝛼,𝛽);// Generate a sector area

// Accept the best solution with
probability 𝑝

if 𝑒(−𝑑𝐸∕𝑡𝑐𝑢𝑟𝑟𝑒𝑛𝑡 )×𝑙𝑜𝑔(𝑛∕2) >= 𝑟𝑎𝑛𝑑(0, 1)
then
′
14
𝑋 = 𝑋𝑏𝑒𝑠𝑡 ;
15
end
16
else
17
Continue to generate next neighbor
solution;
18
end
19
end
20
𝑡𝑐𝑢𝑟𝑟𝑒𝑛𝑡 = 𝑡𝑐𝑢𝑟𝑟𝑒𝑛𝑡 × 𝑡𝑐𝑜𝑜𝑙 and let 𝐺 = 0;
21
if 𝑡𝑐𝑢𝑟𝑟𝑒𝑛𝑡 ≤ 𝑡𝑒𝑛𝑑 then
22
break;
23
end
24 end
13

shown in Fig. 1.
Initialize_packing_solution (𝑃 ) =
{
}
⟨𝑅, 𝑟𝑖 , 𝐵𝑖 ⟩ |𝑖 ∈ {1, … , 𝑛}

(11)

4.3. Generate Neighbor Solutions
Generally, a new neighbor solution is obtained by conducting a local disturbance to the current solution. Here
an effective perturbation strategy plays a significant role
in heuristic algorithms in the local search process to solve
the optimization problem. Besides, different perturbation
methods usually have different impacts on the specific problem. To void falling into local optimum, we design two
new perturbation strategies for the CBPP-CI, termed circle
perturbation and sector perturbation.

4.3.2. Sector perturbation
As Alg. 4 shows, the sector perturbation strategy randomly generates a sector area (𝛼, 𝛽) in a circular bin. The
larger the central angle, the larger the sector area. Therefore,
the larger the disturbance, the more circular items intersecting the area will be reassigned at each iteration. Especially
the circular items are taken out and unassigned from the
border to the center of the circular bin.
Alg. 5 can determine whether a circular item 𝐶𝑖 intersects the selected circular (or sector) area. If a circular item
𝐶𝑖 intersects the chosen area, that is, the item with a red
dotted border in Fig. 2 or Fig. 3, which will be taken out from
the bin and added to the unassigned circular set 𝑐𝑖𝑟𝑐𝑙𝑒_𝑖𝑑𝑠
in Alg. 6 (line 5). However, as the sector area is not easy to
express with mathematical formulas like the circle area, it is
not intuitive to judge whether a circular item intersects with
the sector area. Due to the sector is surrounded by two radii
and the arc opposite the central angle. We turn it into two
small subproblems: 1) whether the center of a circular item
is in the sector area; 2) whether the circular item intersects
the radii 𝑟𝛼 or 𝑟𝛽 of the central angle. The former is judged

Y. Yuan, K. Tole, F. Ni, K. He et al.: Preprint submitted to Elsevier

Page 5 of 14

ASA-GS for Solving the CBPP-CI

R
ri
B1

B2

Bi

Bn

Fig. 1: Initialize a packing solution.

Algorithm 5: Pseudo-code of intersecting with the
sector or circle
Input : Circle 𝐶𝑖 , sector 𝑆 (or circle 𝐶), bin radius
𝑅
Output: True or false
// Returns if 𝐶𝑖 intersects the perturbation area
𝑆 (or 𝐶 )
1 if adopt the sector perturbation then
2
𝛼 = 𝑆.𝛼;
3
𝛽 = 𝑆.𝛽;
4
if the center of 𝐶𝑖 is in sector area 𝑆 then
5
return true;// Intersects with the sector
area 𝑆
6
end
7
if 𝐶𝑖 intersects with radii 𝑟𝛼 or 𝑟𝛽 of 𝑆 then
8
return true;// Intersects with the sector
area 𝑆
9
end
10
return false;// No intersects with the sector
area 𝑆
11 else

Fig. 2: An illustration of circle perturbation.

// adopt the circle perturbation

if (𝐶𝑖 .𝑥 − 𝐶.𝑥)2 + (𝐶𝑖 .𝑦 − 𝐶.𝑦)2 ≤ 𝐶𝑖 .𝑟 + 𝐶.𝑟
then
13
return true; // Intersects with circle area
𝐶
14
else
15
return false;// No intersects with circle
area 𝐶
16
end
17 end
12

Fig. 3: An illustration of sector perturbation.

by line 4, Alg. 5, and the latter is implemented by line 7,
Alg. 5.

4.3.3. Generate Neighbor Solution
′
As Alg. 6 shows, a new packing solution 𝑋 is generated
from the old packing solution 𝑋 by selecting two bins
𝐵𝑘1 , 𝐵𝑘2 randomly and performing sector perturbation or
circle perturbation. We randomly choose a sector area with
equal angle size in each bin, and all items that intersect the

sector area will be taken out, and their IDs will be added
to set 𝑐𝑖𝑟𝑐𝑙𝑒𝑠_𝑖𝑑𝑠. 𝑘1 , 𝑘2 will be added to set 𝑏𝑖𝑛_𝑖𝑑𝑠. The
unassigned circular items will be reassigned with algorithm
′
TOA. Then we will get a new neighbor packing solution 𝑋 .
At each iteration, two (or more) bins will be selected
so that the unassigned circular items have more free space
to be assigned. Even in the worst case, the algorithm will
attempt to exchange the circular items in the two (or more)
areas, ensuring that there will be some disturbance at each
operation.

Y. Yuan, K. Tole, F. Ni, K. He et al.: Preprint submitted to Elsevier

Page 6 of 14

ASA-GS for Solving the CBPP-CI

Algorithm 6: Pseudo-code of generating a new
solution
Input : The old packing solution: 𝑋, bin radius: 𝑅
′
Output: A new neighbor packing solution: 𝑋
1 𝐾 ← 𝑋.𝑏𝑖𝑛𝑠.𝑠𝑖𝑧𝑒();
// Select two bins randomly
2

(

)
𝑘1 , 𝑘2 ← random_ints(2, {1, … , 𝐾)}) ;

// Select a sector or circle area in the first
bin using Algorithm 4 or Algorithm 3
3 𝐴1 ← Sample a sector(𝜃, 𝑖𝑠_𝑓 𝑖𝑥𝑒𝑑); // or Sample a
circle(𝐵𝑘 , 𝑅);
// Select an area in the second bin
4 𝐴2 ← Sample a sector(𝜃, 𝑖𝑠_𝑓 𝑖𝑥𝑒𝑑); // or Sample a
circle(𝐵𝑘 , 𝑅);

⟨
⟩
⋃
𝑐𝑖𝑟𝑐𝑙𝑒_𝑖𝑑𝑠 ← 𝑗∈{1,2} {𝑖| 𝑥𝑖 , 𝑦𝑖 , 𝑘𝑗 ∈
⋀
⋀
𝑋
𝐼𝑖𝑘𝑗 = 1
intersects(𝐶𝑖 , 𝐴𝑗 , 𝑅) ==
𝑇 𝑟𝑢𝑒}; // See Algorithm 5
6 𝑏𝑖𝑛_𝑖𝑑𝑠 ← {𝑘1 , 𝑘2 };
′
7 𝑋 ← 𝑇 𝑂𝐴(𝑐𝑖𝑟𝑐𝑙𝑒_𝑖𝑑𝑠, 𝑏𝑖𝑛_𝑖𝑑𝑠, 𝑅);// Generate a
5

new solution

Besides, at the early stage, the sector area (i.e., Δ𝜃) can
be set larger so that the new neighbor solution can be located
far away from the current solution to speed up the search
process and to avoid getting trapped at a local minimum
solution. Once the temperature 𝑓 (𝑋) gets low, the sector
area will become smaller. The new solution will be generated
nearby with the minor disturbance and focus on the local
area.

4.5. The Overall ASA-GS Algorithm
The workflow of ASA-GS is provided in Alg. 2. Firstly, it
is necessary to initialize the annealing parameters and attain
a feasible packing pattern with the initial solution as shown
in subsection 4.2. Then, it will select one of the perturbation
methods between sector perturbation and circle perturbation
as well as generate a new neighbor packing solution by
Alg. 6. After that, it will compute the energy function and
utilize the greedy search technique based on the simulated
annealing to decide whether accept the new solution. Finally,
it updates the parameters such as the cooling coefficient
of the temperature with 𝑡𝑐𝑢𝑟𝑟𝑒𝑛𝑡 = 𝑡𝑐𝑢𝑟𝑟𝑒𝑛𝑡 × 𝑡𝑐𝑜𝑜𝑙 , and the
acceptance probability by Eq. (14). The process will execute
until the terminal criterion such as the current temperature
𝑡𝑐𝑢𝑟𝑟𝑒𝑛𝑡 is below the threshold 𝑡𝑒𝑛𝑑 , or the number of iterations
𝑖 exceeds the given value 𝑁.
The key concept of greedy search can be described as
′
′
follows: take a new neighbor packing 𝑋 (𝑖.𝑒.𝑋1 ) as the
′
best packing 𝑋 when 𝑑𝐸 ≤ 0(𝑖.𝑒.𝑓 (𝑋 ) ≤ 𝑓 (𝑋)), and
go to the next step. Otherwise the algorithm continues to
′
generate the next new neighbor packing 𝑋2 , and takes it
′
as the best packing 𝑋 when 𝑓 (𝑋2 ) ≤ 𝑓 (𝑋), then goes
to the next step. Otherwise this step will continue to be
executed until attaining a better packing solution or has
′
generated 𝑡𝑔𝑟𝑒𝑒𝑑𝑦 − 𝑡ℎ new neighbor packing 𝑋𝑡
. The
𝑔𝑟𝑒𝑒𝑑𝑦

′

latter will generate 𝑡𝑔𝑟𝑒𝑒𝑑𝑦 neighbor packing solutions 𝑋1 ,
′
′
𝑋2 . . . , 𝑋𝑡
while they are all worse than the original
𝑔𝑟𝑒𝑒𝑑𝑦
packing solution 𝑋. In such case, it will accept the best new
′
packing 𝑋𝑏𝑒𝑠𝑡 among the 𝑡𝑔𝑟𝑒𝑒𝑑𝑦 neighbor packing solutions
generated with probability 𝑝.

4.4. The Assignments of Parameters
In the experiments, we find that different assignments of
parameters are suitable for different problem scales. Therefore, to obtain a better solution in solving the packing problem in a broad scale, the parameter values should change
along with the number of items, which can make the assignments of parameters dynamic and adaptive, such as the times
of greedy search 𝑡𝑔𝑟𝑒𝑒𝑑𝑦 :
𝑡𝑔𝑟𝑒𝑒𝑑𝑦 ← 𝛽 × 𝑛,
and the cool coefficient of the temperature 𝑡𝑐𝑜𝑜𝑙 :
√
𝛼× 𝑛−1
𝑡𝑐𝑜𝑜𝑙 ←
√ .
𝛼× 𝑛

′

(14)

𝑝 ← 𝑒−(𝑓 (𝑋 )−𝑓 (𝑋))∕𝑡𝑐𝑢𝑟𝑟𝑒𝑛𝑡 ×𝑙𝑜𝑔(𝑛∕2) .

′

Obviously, the quality of the best neighbor solution 𝑋𝑏𝑒𝑠𝑡
will vary from low to high with the times of greedy search
increases so that the new solution can jump to a better
′
solution space with high probability. 𝑓 (𝑋𝑏𝑒𝑠𝑡 ) is defined by
Eq. (15):

(12)

′

′

′

′

′

𝑓 (𝑋𝑏𝑒𝑠𝑡 ) = 𝑚𝑖𝑛(𝑓 (𝑋1 ), 𝑓 (𝑋2 ), ..., 𝑓 (𝑋𝐺 ), ..., 𝑓 (𝑋𝑡

𝑔𝑟𝑒𝑒𝑑𝑦

)).

(15)
(13)

In this way, our algorithm is adaptive for the number of
items, and the parameter space can be sampled much more
efficiently. For example, if 𝑛 is small, we will get a quick
cooling coefficient. As the number of items increases, the
times of greedy search will become larger and get a slower
cooling coefficient fit for big-scale packing instances. The
difficulty of the problem becomes higher as the number of
items becomes larger, indicating more solution space to be
explored.

The ASA-GS algorithm can achieve faster convergence
and improve the quality-time trade-off by utilizing the
greedy search technique. As the experimental results show,
the solutions produced by the ASA-GS algorithm are very
competitive.

5. Experiments
For experiments, we evaluate and analyze the competency and performance of the proposed algorithms, TOA
and ASA-GS. We implemented the algorithms using Visual
C++ programming language. All results were generated by
setting parameters as 𝑁 = 2 × 106 , 𝛼 = 0.9, 𝛽 = 0.08,

Y. Yuan, K. Tole, F. Ni, K. He et al.: Preprint submitted to Elsevier

Page 7 of 14

ASA-GS for Solving the CBPP-CI
Table 2
Experimental results on the fixed benchmarks with circular bins for 𝑟𝑖 = 𝑖.
𝑛0

𝑛

𝐴𝑙𝑔.

𝐵𝑖𝑛0

bin 1

bin 2

bin 3

bin 4

bin 5

bin 6

𝐹

𝐹𝐴 − 𝐹𝑇

8

40

0.78

45

10

50

11

55

12

60

13

65

14

70

15

75

16

80

17

85

18

90

19

95

20

100

0.84
0.81
0.83
0.81
0.84
0.81
0.84
0.83
0.85
0.82
0.84
0.84
0.85
0.86
0.85
0.84
0.85
0.86
0.86
0.86
0.86
0.86
0.86
0.86
0.87
0.86

0.80
0.74
0.80
0.75
0.79
0.79
0.81
0.74
0.80
0.79
0.82
0.81
0.80
0.80
0.82
0.79
0.82
0.82
0.83
0.84
0.83
0.83
0.83
0.82
0.83
0.83

0.74
0.72
0.77
0.74
0.79
0.74
0.81
0.72
0.79
0.77
0.81
0.75
0.79
0.77
0.81
0.75
0.82
0.77
0.81
0.75
0.80
0.76
0.80
0.77
0.80
0.77

0.74
0.72
0.76
0.71
0.79
0.74
0.77
0.71
0.77
0.73
0.78
0.75
0.79
0.74
0.79
0.74
0.78
0.74
0.79
0.74
0.79
0.75
0.79
0.75
0.80
0.76

0.71
0.69
0.70
0.69
0.79
0.70
0.77
0.70
0.76
0.68
0.76
0.72
0.78
0.72
0.77
0.72
0.78
0.70
0.76
0.74
0.78
0.75
0.77
0.73
0.77
0.75

0.03
0.19
0.15
0.21
0.07
0.35
0.06
0.24
0.10
0.26
0.12
0.24
0.08
0.26
0.11
0.25
0.11
0.23
0.14
0.25
0.15
0.27
0.13
0.24

−5.19
−5.38
-4.87
-5.34
-4.95
-5.40
-5.23
-5.52
-5.21
-5.42
-5.26
-5.42
-5.27
-5.38
-5.23
-5.42
-5.26
-5.39
-5.25
-5.37
-5.28
-5.39
-5.29
-5.41
-5.26
-5.38

0.19

9

ASA-GS
TOA
ASA-GS
TOA
ASA-GS
TOA
ASA-GS
TOA
ASA-GS
TOA
ASA-GS
TOA
ASA-GS
TOA
ASA-GS
TOA
ASA-GS
TOA
ASA-GS
TOA
ASA-GS
TOA
ASA-GS
TOA
ASA-GS
TOA

0.79
0.80
0.80
0.80
0.81
0.81
0.82
0.83
0.83
0.83
0.84
0.84

𝑡𝑠𝑡𝑎𝑟𝑡 = 0.1, 𝑡𝑒𝑛𝑑 = 10−4 , and obtained using a computer
equipped with an Intel(R) Core(TM) i7-10710U CPU @
1.10GHz 1.61Hz.
As the CBPP-CI is a new problem, there are no available
benchmark instances. Referring to the pioneering work of
square bin packing problem with circular items (SBPPCI) (He et al., 2021). We choose two categories of benchmarks for the single circle packing problem (SCPP) on the
packomonia website and build two sets of new benchmark
instances based on them for the CBPP-CI.
The generated instances consist of strong heterogeneous
√
𝑟𝑖 = 𝑖 (i.e., the circle radii vary widely), and 𝑟𝑖 =
𝑖
for weakly heterogeneous instances. For each category, we
produce fixed and random instances. We first choose instances from the packomonia website for SCPP to generate
our instances. Each circular bin’s best-known solution found
in Eckardi (2018) ranges from 8 to 20 from the circular bin
benchmarks. The fixed set of benchmarks contains exactly
five copies of each circle instance, and for the random benchmarks instances, it contains a random copy of each circular
item that ranges from 2 − 10 from the same benchmarks. We
fix the circular bin size from the best solution found on the
packomonia website.
In the computational tables, we list 52 generated instances from the two categories of benchmarks (fixed and
rand). For each instance in the Tables ( 2, 3, 4 and 5), we have
results for two algorithms: ASA-GS and TOA. Column 𝑛0

0.47
0.45
0.29
0.21
0.16
0.11
0.19
0.13
0.12
0.11
0.12
0.12

represents the original index number of the circle set for each
instance, column 𝑛 represents the actual number of replicated circles in the CBPP-CI instance. The third column (i.e.,
Alg.) represents the two algorithms. Column 𝐵𝑖𝑛0 is only
for the fixed benchmarks representing the reference value
indexed from Eckardi (2018) for the state-of-the-art results.
Columns 5𝑡ℎ to 10𝑡ℎ denote the density (bin occupancy rate)
for each bin. Lastly, the 𝐹 and 𝐹𝐴 − 𝐹𝑇 columns represent
the actual measure value achieved for each algorithm and
relative improvement of ASA-GS over TOA.

5.1. Comparison on 𝑟 = 𝑖
Here 𝑟 = 𝑖 is a benchmark instance that has a wide
variation of circle sizes. In this set of benchmarks, we
execute ASA-GS and TOA algorithms for comparison. We
select instances that range from 8 to 20 for both fixed and
random setup from the benchmark. Table 2 displays the
computational results of fixed benchmarks while Table 3
displays for random benchmarks.
In Table 2 we can notice that the objective value of
ASA-GS is better than TOA on all the instances, and in
addition, we can also observe one lesser bin occupancy rate.
for instance, 𝑛0 = 9 & 𝑛 = 45 and 𝑛0 = 10 & 𝑛 = 45, i.e.,
ASA-GS uses five bins to pack 45 circles while TOA uses six
bins to load the same set of circular items, for a diagrammatic
representation of the packing layout when 𝑛0 = 9 & 𝑛 = 45
(See Fig. 4) and when 𝑛0 = 10 & 𝑛 = 50, we can also

Y. Yuan, K. Tole, F. Ni, K. He et al.: Preprint submitted to Elsevier

Page 8 of 14

ASA-GS for Solving the CBPP-CI
Table 3
Experimental results on the random benchmarks with circular bins for 𝑟𝑖 = 𝑖.
𝑛0

𝑛

𝐴𝑙𝑔.

bin 1

bin 2

bin 3

bin 4

bin 5

bin 6

𝐹

𝐹𝐴 − 𝐹𝑇

8

35
44

10

48

11

52

12

59

13

64

14

67

15

73

16

79

17

84

18

87

19

92

20

97

0.84
0.84
0.84
0.82
0.84
0.83
0.85
0.85
0.85
0.85
0.85
0.85
0.85
0.87
0.87
0.85
0.86
0.86
0.86
0.86
0.87
0.85
0.87
0.86
0.87
0.86

0.81
0.77
0.80
0.75
0.84
0.80
0.84
0.80
0.82
0.80
0.83
0.80
0.82
0.81
0.82
0.80
0.83
0.82
0.84
0.82
0.83
0.82
0.84
0.83
0.84
0.82

0.71
0.68
0.80
0.75
0.79
0.74
0.82
0.74
0.81
0.74
0.83
0.77
0.79
0.77
0.78
0.74
0.81
0.77
0.80
0.78
0.80
0.75
0.82
0.80
0.81
0.74

0.07
0.70
0.73
0.70
0.72
0.71
0.73
0.72
0.72
0.73
0.74
0.79
0.72
0.65
0.73
0.80
0.76
0.78
0.74
0.80
0.74
0.80
0.76
0.74
0.71

0.09
0.08
0.10
0.09
0.08
0.16
0.25
0.73
0.70
0.10
0.18
0.71
0.72
0.06
0.14
0.13

0.12
0.13
-

-2.87
-3.23
-3.86
-4.27
-3.86
-4.25
-3.86
-4.25
-3.87
-4.24
-3.88
-4.23
-4.31
-4.38
-3.78
-3.88
-4.87
-5.26
-4.24
-4.32
-4.84
-5.28
-4.19
-4.28
-3.87
-4.27

0.36

9

ASA-GS
TOA
ASA-GS
TOA
ASA-GS
TOA
ASA-GS
TOA
ASA-GS
TOA
ASA-GS
TOA
ASA-GS
TOA
ASA-GS
TOA
ASA-GS
TOA
ASA-GS
TOA
ASA-GS
TOA
ASA-GS
TOA
ASA-GS
TOA

5 2
1

2

1

2

7 3

6 6

5

9 84 7 9 9 9 6 5 7
4 9
8 4 4 8 4 5 8
1

3

3

1
1

5 2

3

2

2

3

5

6

3

1

2

1

1

94
1

2

1

2

3

94

3

3

9

0.39
0.39
0.37
0.35
0.07
0.10
0.39
0.08
0.44
0.09
0.40

6 6

7 5 7

8

5
6
5 6
4
7 7 7 6
8
7

6 7

8 9 8 9 8 8
2

0.41

3

4 5 4

Fig. 4: Packing layouts generated by ASA-GS (top) and TOA (bottom) for the fixed benchmark 𝑟 = 𝑖 with 9 × 5 circles.

notice that ASA-GS packs 50 circles in 5 bins while TOA
uses six bins for the same set of circular items. For the fixed
benchmarks, ASA-GS has an average of 21% improvement.
For the random benchmarks, we can also observe that
in all the instances, ASA-GS returns a feasible solution
compared to TOA with an overall average improvement of
30% for 𝑟 = 𝑖 benchmarks in Table 3. We show the packing

layout when 𝑛0 = 11 & 𝑛 = 52 in Fig. 5 for the random
benchmarks.

5.2. Comparison
on 𝑟𝑖 =
√

√

𝑖

Here 𝑟𝑖 =
𝑖 has a smaller variation of the circle’s
radii. Similarly, we test the two algorithms on this set of
benchmarks ranging from 8 − 20 instances. Table 4 and 5
represent fixed and random benchmarks respectively.

Y. Yuan, K. Tole, F. Ni, K. He et al.: Preprint submitted to Elsevier

Page 9 of 14

ASA-GS for Solving the CBPP-CI

4

1

9

1

8 9
9 6 10
3

3

7

3

8

9 6

7
11 5 86
6
11 7 9 10
5 11
11
10
9
4
6 7
4 10 4
9 9
11
11 8 10 10 9 6 9 7 6 5 8
8
2

3

3

1

2

3

1

2

2

2

2

2

1

2

4

3

4

4

4

4

1

3

2

1

3

1

3

2 2 2

1

2

4
1

3

1

11

1

2

3

3

3

2

4

11

2

7

9

4

9

6 5

Fig. 5: Packing layouts generated by ASA-GS (top) and TOA (bottom) for the random benchmark 𝑟𝑖 = 𝑖 with 11 − 52 circles.

Table 4
√
Experimental results on the fixed benchmarks with circular bins for 𝑟𝑖 = 𝑖.
𝑛0

𝑛

𝐴𝑙𝑔.

𝐵𝑖𝑛0

bin 1

bin 2

bin 3

bin 4

𝐹

𝐹𝐴 − 𝐹𝑇

8

40

0.76

45

10

50

11

55

12

60

13

65

14

70

15

75

16

80

17

85

18

90

19

95

20

100

0.84
0.81
0.83
0.83
0.83
0.83
0.86
0.85
0.85
0.86
0.85
0.85
0.86
0.83
0.85
0.86
0.86
0.85
0.86
0.85
0.87
0.87
0.87
0.86
0.86
0.87

0.78
0.76
0.81
0.75
0.80
0.75
0.80
0.78
0.81
0.76
0.81
0.78
0.80
0.76
0.81
0.76
0.80
0.79
0.80
0.78
0.81
0.79
0.81
0.78
0.82
0.78

0.76
0.76
0.76
0.70
0.78
0.74
0.79
0.74
0.80
0.75
0.79
0.74
0.78
0.75
0.79
0.75
0.80
0.76
0.80
0.77
0.80
0.77
0.79
0.77
0.80
0.75

0.39
0.45
0.37
0.49
0.39
0.48
0.37
0.42
0.32
0.42
0.37
0.44
0.37
0.47
0.38
0.47
0.39
0.44
0.39
0.45
0.38
0.44
0.40
0.46
0.40
0.47

-3.55
-3.64
-3.54
-3.66
-3.56
-3.65
-3.51
-3.57
-3.47
-3.56
-3.52
-3.59
-3.51
-3.64
-3.53
-3.61
-3.53
-3.59
-3.53
-3.60
-3.51
-3.57
-3.53
-3.60
-3.54
-3.60

0.09

9

ASA-GS
TOA
ASA-GS
TOA
ASA-GS
TOA
ASA-GS
TOA
ASA-GS
TOA
ASA-GS
TOA
ASA-GS
TOA
ASA-GS
TOA
ASA-GS
TOA
ASA-GS
TOA
ASA-GS
TOA
ASA-GS
TOA
ASA-GS
TOA

0.77
0.80
0.81
0.81
0.82
0.82
0.82
0.83
0.83
0.84
0.84
0.84

Table 4 is for the fixed benchmarks, from which we can
notice that ASA-GS outperforms TOA in all the instances
with an average improvement of 8%. We show the significant
improvements of the packing layout in Fig. 6.
We can notice that ASA-GS packs the items with lesser
bins than TOA for the random benchmarks in Table 5. We
can observe that when 𝑛0 = 8 (or 9, 10, 12, 13, 15, 16,
18, 19), ASA-GS uses fewer bins than TOA. We use 𝑛0 =
16 & 𝑛 = 81 to demonstrate the packing layout for this

0.12
0.09
0.06
0.09
0.07
0.13
0.08
0.06
0.07
0.06
0.07
0.06

benchmark in Fig. 7. For these random benchmarks, we can
notice an overall improvement of 26%.

5.3. Further Analysis
Since our solution methods are stochastic, we further analyze and assess the two proposed algorithms’ significance
comparison by using a T-tail statistical hypothesis test on
𝐻0 : 𝜇𝑇 = 𝜇𝐴 . 𝐻0 denotes the null hypothesis, which equates
to no difference between the results returned by TOA and
ASA-GS. We apply the commonly used 𝛼 = 0.05 as our
thresh-hold value. For each table we generated the p-value

Y. Yuan, K. Tole, F. Ni, K. He et al.: Preprint submitted to Elsevier

Page 10 of 14

ASA-GS for Solving the CBPP-CI
Table 5
√
Experimental results on the random benchmarks with circular bins for 𝑟𝑖 = 𝑖.
𝑛0

𝑛

𝐴𝑙𝑔.

bin 1

bin 2

bin 3

bin 4

𝐹

𝐹𝐴 − 𝐹𝑇

8

29
36

10

51

11

56

12

61

13

63

14

66

15

77

16

81

17

83

18

89

19

93

20

97

0.83
0.82
0.84
0.80
0.86
0.84
0.85
0.85
0.86
0.83
0.86
0.84
0.86
0.83
0.86
0.85
0.86
0.86
0.86
0.85
0.86
0.87
0.87
0.86
0.85
0.85

0.79
0.72
0.75
0.74
0.81
0.76
0.80
0.75
0.82
0.76
0.82
0.79
0.81
0.75
0.83
0.76
0.81
0.76
0.81
0.76
0.84
0.77
0.81
0.80
0.81
0.78

0.07
0.05
0.73
0.76
0.68
0.74
0.73
0.75
0.74
0.74
0.65
0.74
0.73
0.72
0.78
0.7
0.79
0.74
0.75
0.76
0.77
0.74
0.80
0.75

0.05
0.07
0.05
0.10
0.14
0.07
0.18
0.06
0.07
0.05
0.14

-1.96
-2.25
-1.91
-2.25
-2.87
-3.21
-2.83
-2.89
-2.87
-3.24
-2.88
-3.21
-2.79
-2.91
-2.87
-3.25
-2.92
-3.28
-3.21
-3.33
-2.89
-3.19
-2.90
-3.21
-3.2
-3.29

0.29

9

ASA-GS
TOA
ASA-GS
TOA
ASA-GS
TOA
ASA-GS
TOA
ASA-GS
TOA
ASA-GS
TOA
ASA-GS
TOA
ASA-GS
TOA
ASA-GS
TOA
ASA-GS
TOA
ASA-GS
TOA
ASA-GS
TOA
ASA-GS
TOA
4

13 14
2

5 3

3

7

7

4

2

4

2

7

4

5

8

14

14

2

6

2

14

14

2

3

12 8 13

2
1

4 3

1

2

3

4

1

10 10
11 10 5 10
11 9 8 9 10
5

1

14

3

9

1

2

14

3

4

3

13 13 14
4

1

3

4

Group

Table

p–value

𝑟𝑖 = 𝑖

Table 2
Table 3
Table 4
Table 5

0.0000662229
0.0000107770
0.0000000252
0.0000037048

𝑖

0.33
0.12
0.38
0.36
0.12
0.30
0.31
0.09

12

10 11 12
4
6

13 11

7 7 7 8
12 12
7
8
12 12 7 12 55 5
8
6

13

11 11 11

Table 6
T–test statistical analysis.

√

0.37

1

6

13

13

6

6

9 9 9

8

Fig. 6: Packing layouts generated by ASA-GS (top) and TOA (bottom) for the fixed benchmark 𝑟𝑖 =

𝑟𝑖 =

0.06

6

13
3

1

0.34

10 7

13
11
5
8 12
9
10
14
11
14 11
9 9 5 8
9 7 5 12 10 10 8 6
6 6
2

1

1

0.34

√

𝑖 with 14 × 5 circles.

and compared with the 𝛼 = 0.05 value as shown in Table 6.
We reject the null hypothesis from the generated results
and claim with a confidence interval (CI) of 95% that our
proposed algorithms are statistically distinct.
To further demonstrate the typical performance pattern
of the two algorithms, we illustrate the performance comparisons of the two algorithms.
In Fig. 8, the Y-axis represents the optimization function
while the X-axis represents the number of circles (𝑛). A red
(blue) line presents ASA-GS (TOA). We can notice a distinct

Y. Yuan, K. Tole, F. Ni, K. He et al.: Preprint submitted to Elsevier

Page 11 of 14

ASA-GS for Solving the CBPP-CI
7
8 11
14
7
14 14
12
10
14
11 12
13
8
6
15 14 7 15
10 12 6 13 12 6 6 6 6 12
9 7

8

3

1

1

3

5

2

8

4

16

2 2

5

2
1

11 10 9 9
8

5

9

10 7 11

11

10

8

7

13 7 13

13

12 13
10 9 9 9
14 14
12 12 13 10 8 7 8 10
14
15
6
15
7
13 12 12 13 10 9 7 78 11 6
9 6
16 13 14 10 11 8 11 11 6 6
15
6
16
14
3

1

3

1

4

4

3

2

4

1

3
3

4

5

1

16

52

2

4

9 6

15

5

4

2

3
3

3

1

1

4

4

5

5

2

2

1

2

52

2 2

5

11

4

7 7 7 6

Optimization function (F)

a) Fixed benchmarks with circular bin ri = i
−4.8
ASA−GS
TOA
−5
−5.2
−5.4
−5.6
40

50

60
70
80
Number of circles (n)

90

100

√
c) Fixed benchmarks with circular bin ri = i
−3.4
ASA−GS
TOA
−3.5

−3.6

−3.7
40

50

60
70
80
Number of circles (n)

90

Optimization function (F)

Optimization function (F)

Optimization function (F)

Fig. 7: Packing layouts generated by ASA-GS (top) and TOA (bottom) for the random benchmark 𝑟𝑖 =

100

√

𝑖 with 16 − 81 circles.

b) Random benchmarks with circular bin ri = i
−2
ASA−GS
TOA
−3
−4
−5
−6
20

40
60
80
Number of circles (n)

100

√
d) Random benchmarks with circular bin ri = i
−1.5
ASA−GS
TOA
−2
−2.5
−3
−3.5
20

40
60
80
Number of circles (n)

100

Fig. 8: ASA-GS versus TOA.

variation of ASA-GS and TOA lines that do not intersect,
indicating that the ASA-GS completely outperforms the base
TOA on all instances.
√
Lastly, we record the runtimes for 𝑟 = 𝑖 and 𝑟𝑖 = 𝑖
benchmarks as shown in Table 7. The execution time of
TOA is in micro-seconds while ASA-GS takes less than 200
seconds. In summary, the performance clearly shows ASAGS efficiency outperforms TOA in a reasonable amount of
time in all the instances. And in some instances, we can
notice a reduction in the number of bins used. Moreover,
Table 3 and Table 5 show that the density of 𝑏𝑖𝑛1 and 𝑏𝑖𝑛2 is

usually greater than that of 𝐵𝑖𝑛0 . It indicates that the packing
density of ASA-GS on the top few bins is much higher
than the best packing results for SCPP on the packomonia
website, inferring the high quality of our solution for the
CBPP-CI.

Y. Yuan, K. Tole, F. Ni, K. He et al.: Preprint submitted to Elsevier

Page 12 of 14

ASA-GS for Solving the CBPP-CI
Table 7
Runtimes for ASA-GS execution on all benchmarks.
𝑟𝑖 = 𝑖

𝑟𝑖 =

fixed

random

√

𝑖

fixed

random

𝑛0

𝑛

𝑡

𝑛

𝑡

𝑛

𝑡

𝑛

𝑡

8
9
10
11
12
13
14
15
16
17
18
19
20

40
45
50
55
60
65
70
75
80
85
90
95
100

12
23
19
22
26
30
35
40
45
52
56
62
68

35
44
48
52
59
64
67
73
79
84
87
92
97

34
32
36
41
59
68
45
98
60
70
86
82
144

40
45
50
55
60
65
70
75
80
85
90
95
100

24
30
39
47
51
63
68
75
89
98
110
128
138

29
36
51
56
61
63
66
77
81
83
89
93
97

53
73
65
92
90
95
122
152
157
95
196
198
146

6. Conclusion

References

In this paper, we introduce a new variant of bin packing
problem termed the circle bin packing problem with circular
items (CBPP-CI). For packing solutions, we define the tangent occupying action (TOA) to quickly pack the items into a
bin as compactly as possible to minimize the number of bins
used. Besides, we design a new form of optimization function embedding the number of bins used and the maximum
density gap of the bins to evaluate the solution quality. We
then propose the adaptive simulated annealing with greedy
search (ASA-GS) algorithm to attain better solutions. The
greedy search strategy can speed up the convergence rate.
Based on the framework of simulated annealing algorithm,
the parameters such as the times of greedy search, the
acceptance probability are adaptive along with the number
of items, which can help to sample the parameter space much
more efficiently and attain a better solution for instances in
a broad scale. To avoid getting trapped in local optimum,
we propose two novel perturbation strategies, sector perturbation and circle perturbation. Experimental results show
that ASA-GS exhibits good performance on the solution
quality and computational time. Besides, the packing quality
is better than that of the constructive algorithm TOA on
all the CBPP-CI instances we generated. As this is a new
problem, there is no baseline algorithm available. However,
we see that the packing density of ASA-GS on the top few
bins is much higher than the state-of-the-art results on the
single circle packing problem, indicating the high quality of
our solution.

Akeb, H., Hifi, M., M’Hallah, R., 2009. A beam search algorithm for the
circular packing problem. Computers & Operations Research 36, 1513–
1528.
Akeb, H., Hifi, M., Negre, S., 2011. An augmented beam search-based
algorithm for the circular open dimension problem. Computers &
Industrial Engineering 61, 373–381.
Christensen, H.I., Khan, A., Pokutta, S., Tetali, P., 2017. Approximation
and online algorithms for multidimensional bin packing: A survey.
Computer Science Review 24, 63–79.
Chung, F.R., Garey, M.R., Johnson, D.S., 1982.
On packing twodimensional bins. SIAM Journal on Algebraic Discrete Methods 3, 66–
76.
Demaine, E.D., Fekete, S.P., Lang, R.J., 2010. Circle packing for origami
design is hard. arXiv preprint arXiv:1008.1224 .
Eckardi, S., 2018. Packomania website 2018 www.packomania.com.
Packomania .
Faroe, O., Pisinger, D., Zachariasen, M., 2003. Guided local search for the
three-dimensional bin-packing problem. Informs journal on computing
15, 267–283.
Fu, Z., Huang, W., Lü, Z., 2013. Iterated tabu search for the circular open
dimension problem. European Journal of Operational Research 225,
236–243.
Geng, X., Chen, Z., Yang, W., Shi, D., Zhao, K., 2011. Solving the traveling
salesman problem based on an adaptive simulated annealing algorithm
with greedy search. Applied Soft Computing 11, 3680–3689.
Grosso, A., Jamali, A., Locatelli, M., Schoen, F., 2010. Solving the problem
of packing equal and unequal circles in a circular container. Journal of
Global Optimization 47, 63–81.
He, K., Dosh, M., 2017. A greedy heuristic based on corner occupying
action for the 2d circular bin packing problem, in: National Conference
of Theoretical Computer Science, Springer. pp. 75–85.
He, K., Huang, M., Yang, C., 2015. An action-space-based global optimization algorithm for packing circles into a square container. Computers &
Operations Research 58, 67–74.
He, K., Huang, W., Jin, Y., 2012. An efficient deterministic heuristic
for two-dimensional rectangular packing. Computers & Operations
Research 39, 1355–1363.
He, K., Tole, K., Ni, F., Yuan, Y., Liao, L., 2021. Adaptive large neighborhood search for solving the circle bin packing problem. Computers and
Operations Research 127, 105140. doi:https://doi.org/10.1016/j.cor.
2020.105140.

Acknowledgement
This work is supported by National Natural Science
Foundation (62076105) and Natural Science Foundation of
Jiangsu Province (BK20181409).

Y. Yuan, K. Tole, F. Ni, K. He et al.: Preprint submitted to Elsevier

Page 13 of 14

ASA-GS for Solving the CBPP-CI
Hifi, M., M’Hallah, R., 2002. A best-local position procedure-based
heuristic for two-dimensional layout problems. Stud. Inform. Univ. 2,
33–56.
Hifi, M., Paschos, V.T., Zissimopoulos, V., 2004. A simulated annealing
approach for the circular cutting problem. European Journal of Operational Research 159, 430–448.
Huang, W.Q., Li, Y., Li, C.M., Xu, R.C., 2006. New heuristics for packing
unequal circles into a circular container. Computers & Operations
Research 33, 2125–2142.
Johnson, D.S., 1973. Near-optimal bin packing algorithms. Ph.D. thesis.
Massachusetts Institute of Technology.
Kang, J., Park, S., 2003. Algorithms for the variable sized bin packing
problem. European Journal of Operational Research 147, 365–372.
doi:https://doi.org/10.1016/S0377-2217(02)00247-3.
Kirkpatrick, S., Gelatt, C.D., Vecchi, M.P., 1983. Optimization by simulated annealing. science 220, 671–680.
Lodi, A., Martello, S., Monaci, M., 2002. Two-dimensional packing
problems: A survey. European journal of operational research 141, 241–
252.
Lodi, A., Martello, S., Vigo, D., 1999. Heuristic and metaheuristic
approaches for a class of two-dimensional bin packing problems. INFORMS Journal on Computing 11, 345–357.
López, C.O., Beasley, J., 2016. A formulation space search heuristic for
packing unequal circles in a fixed size circular container. European
Journal of Operational Research 251, 64–73.
Lü, Z., Huang, W., 2008. Perm for solving circle packing problem.
Computers & Operations Research 35, 1742–1755.
Lubachevsky, B.D., Graham, R.L., 1997. Curved hexagonal packings of
equal disks in a circle. Discrete & Computational Geometry 18, 179–
194.
Mhand, H., Rym, M., 2004. Approximate algorithms for constrained
circular cutting problems. Computers and Operations Research 31, 675
– 694.
Monaci, M., Toth, P., 2006. A set-covering-based heuristic approach for
bin-packing problems. INFORMS Journal on Computing 18, 71–85.
Parreño, F., Alvarez-Valdés, R., Oliveira, J.F., Tamarit, J.M., 2010. A hybrid
grasp/vnd algorithm for two-and three-dimensional bin packing. Annals
of Operations Research 179, 203–220.
Wang, H., Huang, W., Zhang, Q., Xu, D., 2002. An improved algorithm for
the packing of unequal circles within a larger containing circle. European
Journal of Operational Research 141, 440–453.
Wei, L., Oon, W.C., Zhu, W., Lim, A., 2011. A skyline heuristic for the 2d
rectangular packing and strip packing problems. European Journal of
Operational Research 215, 337–346.
Zhizhong, Z., Xinguo, Y., Kun, H., Zhanghua, F., 2018. Adaptive tabu
search and variable neighborhood descent for packing unequal circles
into a square. Applied Soft Computing 65, 196 – 213.

Y. Yuan, K. Tole, F. Ni, K. He et al.: Preprint submitted to Elsevier

Page 14 of 14

