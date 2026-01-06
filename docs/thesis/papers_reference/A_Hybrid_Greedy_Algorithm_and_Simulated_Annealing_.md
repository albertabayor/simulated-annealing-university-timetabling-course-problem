Jurnal Teknik Industri, Vol. 20, No. 2, December 2018,
ISSN 1411-2485 print / ISSN 2087-7439 online

DOI: 10.9744/jti.20.2.89-94

A Hybrid Greedy Algorithm and Simulated Annealing for Single
Container Loading Problem: A Case Study
I Gede Agus Widyadana 1*, Audrey Tedja Widjaja2, Kun Jen Wang 2
Abstract: A single container loading problem is a problem to effectively load boxes in a threedimensional container. There are many researchers in this problem try to find the best solution to
solve the problem with feasible computation time and to develop some models to solve real case
problem. Heuristics are the most method used to solve this problem since the problem is an NPhard. In this paper, we introduce a hybrid greedy algorithm and simulate annealing algorithm to
solve a real container loading problem in one flexible packaging company in Indonesia. Validation
is used to show that the method can be applied practically. We use seven real cases to check the
validity and performance of the model. The proposed method outperformed the solution developed
by the company in all seven cases with feasible computational time.
Keywords: Single container loading problem, greedy algorithm, simulated annealing.

Introduction

variations but also methods to solve the problem.
There are some researchers try to find the best
solution with feasible computation time. Huang
and He [9] used a heuristic caving degree approach
to solve a single container loading problem. Zhu
and Lim [3] solved a single container loading
problem by modifying a greedy algorithm. Huang et
al. [9] proposed an effective heuristic to solve a single
container loading problem. A heuristic method to
solve a single container loading problem was developed by Araya et al. [2] and they called the method as
VCS. Most research used a heuristic approach to solve
a single container loading problem and no one used a
metaheuristic method. However, some metaheuristic
methods are used to solve container loading problem
such as Tabu Search (Liu et al. [10]). In this paper, we
try to develop a hybrid heuristic and metaheuristic
method to solve a single container loading problem
and apply the method to one flexible packaging
company in Indonesia. The hybrid method is applied
to get efficient computation time and effective result.
This paper is presented in four sections. The first
section present background of the paper, the second
section show model and solution development, section
3 shows the application of the solution to a real case
on a company and the last section give the conclusion
of this research.

Container loading problems sometimes are called the
packing problem, have been explored by many
researchers since it plays important roles in logistics.
There are some container loading problems have been
explored to deal with problems in practice since there
are many constraints should be considered such as
constraint related with a container, item, cargo,
positioning, and load (Bortfeldt and Wascher [1]). One
type of container loading problem is a single container
loading problem. The single container routing
problem is a packing problem where a set of boxes are
arranged to be put in a three-dimensional container
with objectives to maximize space utilization. Araya
and Riff [2] used beam search strategy to solve a
single container outing problem and claimed their
method outperform some preceding methods such as
Zhu and Lim [3], Zhu et al. [4], Goncalves and
Resende [6] and Fanslau and Bortfeldt [6].
There are some variations of a single container
loading problem. Lim et al. [7] developed a heuristic
model to solve a single container loading problem with
axle weight constraints that are applied in the
California Vehicle Code (CVC). Wang et al. [8]
developed a single container loading problem by
considering shipment priority that is common in a
real situation. The research focus on a single
container loading problem is not only about problem

Methods
Mathematical Model

1Faculty

of Industrial Technology, Department of Industrial
Engineering, Petra Christian University, Jl. Siwalankerto 121-131
Surabaya 60238, Indonesia.
2 School of Management, Industrial Management Department,
National Taiwan University of Science and Technology, 43, Sec.4,
Keelung Road, Taipei 106, Taiwan, ROC
Email: gede@petra.ac.id, kjwang@mail.ntust.edu.tw

In this model, we use similar notation as Chen et al.
[11] and Huang et al. [9] as below:
n
: Total boxes to be loaded
N
: A set, 𝑁 = {1,2, … , 𝑛}
M
: max {𝑥̅ , 𝑦̅, 𝑧̅}
(𝑝𝑖 , 𝑞𝑖 , 𝑟𝑖 )
: Length, width and height

* Corresponding author

89

Widyadana et al. / Hybrid Greedy Algorithm and Simulated Annealing / JTI, Vol. 20, No. 2, December 2018, pp. 89-94

(𝑥𝑖 , 𝑦𝑖 , 𝑧𝑖 )

:

(𝑙𝑥𝑖 , 𝑙𝑦𝑖 , 𝑙𝑧𝑖 )

:

(𝑤𝑥𝑖 , 𝑤𝑦𝑖 , 𝑤𝑧𝑖 )

:

(ℎ𝑥𝑖 , ℎ𝑦𝑖 , ℎ𝑧𝑖 )

:

(𝛼𝑖𝑗 , 𝛽𝑖𝑗 , 𝛿𝑖𝑗 )

:

of box 𝑖, respectively
coordinates of the left-frontbottom corner of box 𝑖
binary variables showing
whether the length of box 𝑖 is
parallel to the 𝑥-axis, 𝑦-axis or 𝑧axis.
binary variables showing
whether the width of box 𝑖 is
parallel to the x-axis, y-axis or zaxis.
binary variables showing
whether the height of box 𝑖 is
parallel to the x-axis, y-axis or zaxis.
binary variables showing the
relative positions of box i and
box j, such as:
(𝛼𝑖𝑗 , 𝛽𝑖𝑗 , 𝛿𝑖𝑗 ) = (0,0,1) if box 𝑖 is
on the left-hand side of box 𝑗;
(𝛼𝑖𝑗 , 𝛽𝑖𝑗 , 𝛿𝑖𝑗 ) = (0,1,0) or
(𝛼𝑖𝑗 , 𝛽𝑖𝑗 , 𝛿𝑖𝑗 ) = (1,0,0)
if box 𝑖 is behind box 𝑗;
(𝛼𝑖𝑗 , 𝛽𝑖𝑗 , 𝛿𝑖𝑗 ) = (0,1,1) if box 𝑖 is
in front of box 𝑗;
(𝛼𝑖𝑗 , 𝛽𝑖𝑗 , 𝛿𝑖𝑗 ) = (1,0,1) if box 𝑖 is
below of box 𝑗;
(𝛼𝑖𝑗 , 𝛽𝑖𝑗 , 𝛿𝑖𝑗 ) = (1,1,0) if box 𝑖 is
above of box 𝑗;

𝑦𝑖 + 𝑝𝑖 𝑙𝑦𝑖 + 𝑞𝑖 𝑤𝑦𝑖 + 𝑟𝑖 ℎ𝑦𝑖 ≤ 𝑦̅,
𝑧𝑖 + 𝑝𝑖 𝑙𝑧𝑖 + 𝑞𝑖 𝑤𝑧𝑖 + 𝑟𝑖 ℎ𝑧𝑖 ≤ 𝑧̅,

∀𝑖 ∈ 𝑁
∀𝑖 ∈ 𝑁

(10)
(11)

In the third constraint, the length, wide and high of
box i only parallel with one axis x, y, and z.
𝑙𝑥𝑖 + 𝑙𝑦𝑖 + 𝑙𝑧𝑖 = 1,
∀𝑖 ∈ 𝑁
(12)
𝑤𝑥𝑖 + 𝑤𝑦𝑖 + 𝑤𝑧𝑖 = 1,
∀𝑖 ∈ 𝑁
(13)
ℎ𝑥𝑖 + ℎ𝑦𝑖 + ℎ𝑧𝑖 = 1,
∀𝑖 ∈ 𝑁
(14)
𝑙𝑥𝑖 + 𝑤𝑥𝑖 + ℎ𝑥𝑖 = 1,
∀𝑖 ∈ 𝑁
(15)
𝑙𝑦𝑖 + 𝑤𝑦𝑖 + ℎ𝑦𝑖 = 1,
∀𝑖 ∈ 𝑁
(16)
𝑙𝑧𝑖 + 𝑤𝑧𝑖 + ℎ𝑧𝑖 = 1,
∀𝑖 ∈ 𝑁
(17)
where:
𝑥𝑖 , 𝑦𝑖 , 𝑧𝑖 ≥ 0
0 < 𝑥 ≤ 𝑥̅
0 < 𝑦 ≤ 𝑦̅
0 < 𝑧 ≤ 𝑧̅

(18)
(19)
(20)
(21)

Greedy Algorithm
In the first step, we group pallets with the same size
to set the height of stacks are not more than the
height of a container. We use a greedy algorithm to
solve the first step as follows:
1. Sort boxes from the largest size
2. Choose a box with the largest size, put it in first
level, and add one box with the same size and put
it above the first box.
3. Check the total height, if the total height is less
than the container height than choose one box
with the same height and put it on the next level.
4. Continue step 3 until no boxes can be put above
other boxes.
5. Find a new box with largest size and continue
with step 1.
6. Choose one box with the same size and less height
and goes to step two.
7. Continue steps one to six until all boxes have
been stacked.

The Mixed Integer Linear Programming (MILP) from
Huang et al. [9] is:
The fitness function is minimizing container length to
pack all the boxes.
𝑀𝑖𝑛 𝑥
(1)
In the first constraints, all boxes can’t overlap.
𝑥𝑖 + 𝑝𝑖 𝑙𝑥𝑖 + 𝑞𝑖 𝑤𝑥𝑖 + 𝑟𝑖 ℎ𝑥𝑖 ≤ 𝑥𝑗 + 𝑀(1 + 𝛼𝑖𝑗 + 𝛽𝑖𝑗 −
𝛿𝑖𝑗 ), ∀𝑖, 𝑗 ∈ 𝑁, 𝑖 < 𝑗
(2)
𝑥𝑗 + 𝑝𝑗 𝑙𝑥𝑗 + 𝑞𝑗 𝑤𝑥𝑗 + 𝑟𝑗 ℎ𝑥𝑗 ≤ 𝑥𝑖 + 𝑀(1 + 𝛼𝑖𝑗 − 𝛽𝑖𝑗 +
𝛿𝑖𝑗 ), ∀𝑖, 𝑗 ∈ 𝑁, 𝑖 < 𝑗
(3)
𝑦𝑖 + 𝑝𝑖 𝑙𝑦𝑖 + 𝑞𝑖 𝑤𝑦𝑖 + 𝑟𝑖 ℎ𝑦𝑖 ≤ 𝑦𝑗 + 𝑀(1 − 𝛼𝑖𝑗 + 𝛽𝑖𝑗 +
𝛿𝑖𝑗 ), ∀𝑖, 𝑗 ∈ 𝑁, 𝑖 < 𝑗
(4)
𝑦𝑗 + 𝑝𝑗 𝑙𝑦𝑗 + 𝑞𝑗 𝑤𝑦𝑗 + 𝑟𝑗 ℎ𝑦𝑗 ≤ 𝑦𝑖 + 𝑀(2 + 𝛼𝑖𝑗 − 𝛽𝑖𝑗 −
𝛿𝑖𝑗 ), ∀𝑖, 𝑗 ∈ 𝑁, 𝑖 < 𝑗
(5)
𝑧𝑖 + 𝑝𝑖 𝑙𝑧𝑖 + 𝑞𝑖 𝑤𝑧𝑖 + 𝑟𝑖 ℎ𝑧𝑖 ≤ 𝑧𝑗 + 𝑀(2 − 𝛼𝑖𝑗 + 𝛽𝑖𝑗 −
𝛿𝑖𝑗 ), ∀𝑖, 𝑗 ∈ 𝑁, 𝑖 < 𝑗
(6)
𝑧𝑗 + 𝑝𝑗 𝑙𝑧𝑗 + 𝑞𝑗 𝑤𝑧𝑗 + 𝑟𝑗 ℎ𝑧𝑗 ≤ 𝑧𝑖 + 𝑀(2 − 𝛼𝑖𝑗 − 𝛽𝑖𝑗 +
𝛿𝑖𝑗 ), ∀𝑖, 𝑗 ∈ 𝑁, 𝑖 < 𝑗
(7)
1 ≤ 𝛼𝑖𝑗 + 𝛽𝑖𝑗 + 𝛿𝑖𝑗 ≤ 2, ∀𝑖, 𝑗 ∈ 𝑁, 𝑖 < 𝑗
(8)

Simulated Annealing
Simulated Annealing (SA) algorithm used in this
problem is a simple SA algorithm as shown in Figure
1.
Encoding Method
Encoding method represents the solution to the
problem. The solutions are coded into row strings
where the first row represents the loading sequence
into a container and the second row represents the
position of the boxes and represented by a binary
number. An example of the strings is shown in Figure
2. Figure 2 shows the first box loaded is box number
2, the second box is box 4 and so on. In the second row
shows the rotation of the box where 1 represent the

For the second constraint, all boxes can be put in a
container.
𝑥𝑖 + 𝑝𝑖 𝑙𝑥𝑖 + 𝑞𝑖 𝑤𝑥𝑖 + 𝑟𝑖 ℎ𝑥𝑖 ≤ 𝑥̅ ,
∀𝑖 ∈ 𝑁
(9)
90

Widyadana et al. / Hybrid Greedy Algorithm and Simulated Annealing / JTI, Vol. 20, No. 2, December 2018, pp. 89-94

possibility that the solution is not feasible since the
total width or the total length of loaded boxes are
bigger than the container’s width and length. When a
feasible solution can not be found then we set the
fitness function as a big number.
Generation Mechanism of Neighbourhood
Solution
Generation mchanism of neighbourhood solution is a
mechanism to generate a new solution in each
iteration. The generation mechanism in this paper is
as follows:
1. Choose one position randomly and insert to any
new position randomly
2. Check feasibility of the solution, when the
solution is not feasible to change the position from
0 to 1 or from 1 to 0.
3. Try step 2 until a feasible solution is found. When
a feasible solution still can not be found, set
fitness function with big value.
Acceptance Criteria for the Neighbourhood
Solution
The following criterion is used to evaluate whether a
neighbourhood solution is accepted as a new solution
or not.
∆= 𝑆 − 𝑆 ∗
(22)
Where S is a new solution generated by neighborhood
scheme and S is the old solution before neighborhood
scheme is employed. When ∆ is negative then the new
solution is better than the old one, but when ∆ is
positive, there is a possibility for the new solution to
be accepted with certain probability. The acceptance
probability can be represented as Eq. 23.
∆

( )

𝑝 = 𝑒 𝑇𝑖
where:
𝑇𝑖 = temperature at iteration-𝑖

The next step is generating a random number 𝑝𝑚
where 0 < 𝑝𝑚 < 1. When 𝑝𝑚 is less than 𝑝 then a
new solution is accepted, otherwise the new solution
is rejected.
Temperature updating scheme
The temperature updating scheme used in this paper
is the commonly geometric updating scheme as
shown in Eq. 24.

Figure 1 The simulated annealing algorithm

2
0

4
1

10
1

7
1

1
1

3
0

9
0

6
1

8
1

(23)

5
0

Figure 2. A sample of solution

length of a box follows 𝑥-axis and 1 if the length of the
box follows 𝑦-axis.

𝑇𝑖+1 = 𝑘 × 𝑇𝑖
(24)
where 𝑘 is the rate parameter in terms of initial
temperature.

Fitness Function
A fitness function is a criterion that has to be
optimized. In this paper, we try to minimize the area
of the unoccupied container. The fitness function is
equal to the total wide of a container minus the total
area of the boxes loaded in the container. There is a

Stopping Criteria
The simulated annealing algorithm is stopped when
the temperature (𝑇) is less than a specific temperature defines in advance.

91

Widyadana et al. / Hybrid Greedy Algorithm and Simulated Annealing / JTI, Vol. 20, No. 2, December 2018, pp. 89-94

Result and Discussion

convergence solutions in 6 cases, parameters set 2 in
2 cases and parameters set 3 and 4 in 7 cases.
Therefore, we choose parameters set 3 since the
parameters set is the best for running time and
convergence. Even though the solution quality is less
than solution quality or parameters set 4, the
difference is not significant. The solution for seven
cases for every temperature is shown in Figure 3.

The model is used to solve a problem at one flexible
packaging company in Indonesia. There are seven
cases are used to verify and validate the model. The
simplest case is case 1 and the most complicated case
is case 7, as shown in Table 1 and 2. Table 1 and are
the result of the Greedy Algorithm. For example in
Table 2 pallet number 28 is stacked above pallet
number 27 and both pallet become one group pallet.
Pallet number 15 cannot be stacked above pallet 14,
since the total height is more than the container
height. One pallet can be stacked with other pallet
and become one group pallet if they have the same
length and width.

We validate the model result with company’s loading
method and the unused area is shown in Table 5.
Table 2. Data of case 7
Pallet
Pallet
group
number

The good solution of simulated annealing is determined by right parameters setting which is consist of
initial temperature, stopping temperature, k, and the
number of replication. The program is run under
Macro software in OS Windows 8.1 64-bit with
processor Intel(R)Core(TM) i5-4590 CPU @3.30GHz
and RAM 4,00 GB. We use four parameters set as
shown in Table 3. The result of four parameters set is
shown in Table 4.

1
2
3
3
4
4
5
5
6
6
7
8
9
9
10
10
11
11
12
12
13
13
14
14
15
16
16
17
17
18
18
19
20
20

Table 4 shows the best solution in case 1 to 6 for the
four parameters set are the same and parameters set
4 giving the best solution for case 7. Running time for
parameters set 1 and 3 significantly faster than
parameters set 2 and 4. Parameters set 1 result in
Table 1. Data of case 1
Pallet
Pallet
group
number
1
1
2
2
3
3
4
4
5
5
6
6
7
7
8
8
9
9
10
10
11
11
12
12

9
15
10
16
11
17
12
18
13
19
14
20
21
22
1
3
2
4
5
7
6
8
23
24

Pallet size (mm)
880
880
880
880
880
880
880
880
880
880
880
880
880
880
780
780
780
780
780
780
780
780
680
680

1150
1150
1150
1150
1150
1150
1150
1150
1150
1150
1150
1150
1150
1150
1150
1150
1150
1150
1150
1150
1150
1150
1150
1150

160
160
160
160
160
160
160
160
160
160
160
160
160
160
160
160
160
160
160
160
160
160
160
160

Box
height
(mm)
1030
1070
1030
1070
1030
1070
1030
1070
1030
1070
1070
1070
1070
1070
1030
1070
1030
1070
1030
1070
1030
1070
1070
1070

14
15
27
28
31
32
33
34
16
19
17
18
1
2
3
4
5
6
7
10
8
11
9
12
13
20
21
22
23
24
25
26
29
30

Pallet size (mm)
1620
1620
1260
1260
1240
1240
990
990
1090
1090
1090
1090
1020
1020
1020
1020
1020
1020
1020
1020
1020
1020
1020
1020
1020
1390
1390
1390
1390
1370
1370
1370
1260
1260

1120
1120
1320
1320
1320
1320
1320
1320
1120
1120
1120
1020
1020
1020
1020
1020
1020
1020
1020
1020
1020
1020
1020
1020
1020
690
690
690
690
690
690
690
690
690

240
240
170
170
170
170
170
170
170
170
170
170
140
140
140
140
140
140
140
140
140
140
140
140
140
140
140
140
140
140
140
140
170
170

Box
height
(mm)
1250
1250
800
800
800
800
800
800
1180
675
1180
1180
1080
1080
1080
1080
1080
1080
1080
1036
821
1036
821
1036
1036
770
770
770
770
770
770
770
800
800

Table 3. Parameters of simulated annealing
1
2
3
4
Initial
0.11
0.11
0.11
0.11
temperature
Stopping
0.001 0.001 0.0008 0.0008
temperature
3
3
5
5
𝑘
0.9
0.95
0.9
0.95
Number of
30
30
30
30
replication

92

Widyadana et al. / Hybrid Greedy Algorithm and Simulated Annealing / JTI, Vol. 20, No. 2, December 2018, pp. 89-94

Table 4. Parameters set solution
Quality
Parameters
of
Running
set
solution
time
1
6
7
2
6
0
3
6
7
4
7
0

Convergence

Total

6
5
7
7

19
11
20
14

Table 5. Comparison of company’s calculation and the
research method
Case
1
2
3
4
5
6
7

Unused area (m2)
Company’s
method
Our method
0,184
1,978
0,322
0,552
0,3795
0,759
1,242
2,553
0,253
0,322
0,736
0,736
0,989
1,196

Table 5 shows that our method has bigger unused
area compare with the company’s method for all
cases. Since in average palette size is 1 m2, then we
can not add more pallet for cases 2, 3, 5, and 6. Using
our method, we can add more pallet for cases 1, 4, and
7.

Conclusion
In this research, a hybrid greedy algorithm and a
simulated annealing is developed to solve a single
container loading problem in one company. Since
some parameters are crucial to get efficient and
effective solutions, we try four parameter sets and
find the best parameters set. The method is validated
using seven different cases form the company and the
result is compared with the company’s solution. The
proposed methods outperform company’s solution in
seven cases with feasible computation time.
The paper can be extended by considering some real
constraints that have not been considered in this
paper. For example, some buyer asks the weight of
the container should be not too much difference
between the front, middle and back area.

References
1.

2.
3.

93

Bortfeldt A., and Wascher G. Constraints in
Container :oading – A State-of-the-art Review,
European Journal of Operational Research, 229,
2013, pp. 1-20.
Araya I., and Riff M.C., A Beam Search Approach
to the Container Loading Problem, Computers &
Operations Research, 43, 2014, pp. 100-107.
Zhu W, Lim A, A New Iterative-doubling Greedylook Ahead Algorithm for the Single Container

Widyadana et al. / Hybrid Greedy Algorithm and Simulated Annealing / JTI, Vol. 20, No. 2, December 2018, pp. 89-94

4.

5.

6.

7.

Loading Problem, European Journal of Operational Research, 222 (3), 2012, pp.408–417.
Zhu W, Hon W, Lim A, and Weng Y. The Six
Elements to Block-building Approaches for the
Single Container Loading Problem, Applied
Intelligence, 37(3), 2012, pp. 1–15.
Gonçalves J, and Resende M, A Parallel Multipopulation Genetic Algorithm for a Constrained
Two-dimensional Orthogonal Packing Problem,
Journal of Combinatorial Optimization, 22(2),
2011, pp. 180–201.
Fanslau T, and Bortfeldt A, A Tree Search
Algorithm for Solving the Container Loading
Problem, INFORMS Journal on Computing,
22(2), 2010, pp.22–35.
Lim A., Ma H., Qiu C., and Zhu W., The Single
Container Loading Problem with Axle Weight
Constraints, International Journal of Production

Economics, 144, 2013, pp. 358-369.
Wang N., Lim A., and Zhu W., A Multi-round
Partial Beam Search Approach for the Single
Container Loading Problem with Shipment
Priority, International Journal of Production
Economics, 145, 2013, pp. 531-540.
9. Huang W., and He K., A Caving Degree Approach
for the Single Container Loading, European
Journal of Operational Research, 196, 2009, pp.
93-101.
10. Liu J., Yue Y., Donng Z., Maple C., and dam
Keech M., A Novel Hybrid Tabu Search to
Container Loading, 38, 2011, pp. 797-807.
11. Chen, C., Lee, S., and Shen, Q. An Analytical
Model for the Container Loading Problem,
European Journal of Operational Research, 80(1),
1995, pp. 68-76.
8.

94

