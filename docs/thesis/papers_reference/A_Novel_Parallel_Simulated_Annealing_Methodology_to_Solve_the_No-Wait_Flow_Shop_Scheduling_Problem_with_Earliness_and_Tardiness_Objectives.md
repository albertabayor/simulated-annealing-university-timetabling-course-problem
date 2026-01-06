processes
Article

A Novel Parallel Simulated Annealing Methodology to Solve
the No-Wait Flow Shop Scheduling Problem with Earliness and
Tardiness Objectives
Ismet Karacan 1,2, *, Ozlem Senvar 3
1
2

3

*

Citation: Karacan, I.; Senvar, O.;

and Serol Bulkan 3

AN-EL Anahtar ve Elektrikli Ev Aletleri Sanayi A.S., Istanbul 34896, Turkey
Industrial Engineering Doctorate Programme, Institute of Pure and Applied Sciences, Marmara University,
Istanbul 34722, Turkey
Department of Industrial Engineering, Marmara University, Istanbul 34854, Turkey
Correspondence: ismetkaracan@marun.edu.tr

Abstract: In this paper, the no-wait flow shop problem with earliness and tardiness objectives is
considered. The problem is proven to be NP-hard. Recent no-wait flow shop problem studies focused
on familiar objectives, such as makespan, total flow time, and total completion time. However, the
problem has limited studies with solution approaches covering the concomitant use of earliness and
tardiness objectives. A novel methodology for the parallel simulated annealing algorithm is proposed
to solve this problem in order to overcome the runtime drawback of classical simulated annealing
and enhance its robustness. The well-known flow shop problem datasets in the literature are utilized
for benchmarking the proposed algorithm, along with the classical simulated annealing, variants
of tabu search, and particle swarm optimization algorithms. Statistical analyses were performed to
compare the runtime and robustness of the algorithms. The results revealed the enhancement of the
classical simulated annealing algorithm in terms of time consumption and solution robustness via
parallelization. It is also concluded that the proposed algorithm could outperform the benchmark
metaheuristics even when run in parallel. The proposed algorithm has a generic structure that can be
easily adapted to many combinatorial optimization problems.

Bulkan, S. A Novel Parallel Simulated
Annealing Methodology to Solve the
No-Wait Flow Shop Scheduling
Problem with Earliness and Tardiness

Keywords: production scheduling; no-wait flow shop scheduling problem; earliness and tardiness;
mixed-integer programming; parallel simulated annealing

Objectives. Processes 2023, 11, 454.
https://doi.org/10.3390/
pr11020454
Academic Editors: Danyu Bai,
Xin Chen, Dehua Xu, Jedrzej
Musial and Raul D.S.G. Campilho
Received: 20 December 2022
Revised: 20 January 2023
Accepted: 28 January 2023
Published: 2 February 2023

Copyright: © 2023 by the authors.
Licensee MDPI, Basel, Switzerland.
This article is an open access article
distributed under the terms and
conditions of the Creative Commons
Attribution (CC BY) license (https://
creativecommons.org/licenses/by/
4.0/).

1. Introduction
Flow shop scheduling problems (FSSPs) consist of n jobs that should be processed
on m different machines. In the classical FSSP, it is assumed that there exists an unlimited
buffer between two successive machines. The no-wait flow shop scheduling problem
(NWFSSP) is a special case of the generic FSSP in that each operation of a job has to be
processed immediately after the preceding operation, without any delay. Consequently, the
problem has a permutation schedule that should be processed on no-buffer machines [1].
The permutation constraint ensures that all jobs are processed in the same order on the
machines [2]. The NWFSSP is fundamental to applications in real-life production environments, especially for jobs including quick obsolescence risk for manufactured products
or their components. Examples are processes of canned food, critical operations of metals
while forging, and production with chemical reactions [3].
Graham et al. [4] introduced the α | β | γ notation to define a scheduling problem,
where α stands for the machine environment, β denotes any special constraint, and γ represents the objective function or functions of the problem. The machine environment shows
the shopfloor setup, such as parallel machines, flow shop, and job shop. The constraints
present the special cases of processes such as permutation (prmu), no-wait (nwt), blocking
(block), and recirculation (rcrc). The last field hosts the objectives, e.g., total completion

Processes 2023, 11, 454. https://doi.org/10.3390/pr11020454

https://www.mdpi.com/journal/processes

Processes 2023, 11, x FOR PEER REVIEW

Processes 2023, 11, 454

2 of 27

constraints present the special cases of processes such as permutation (prmu), no-wait
(nwt), blocking (block), and recirculation (rcrc). The last field hosts the objectives, e.g.,
2 of 26
total completion time, makespan, flow time, earliness, and tardiness. In this study, the
NWFSSP is considered to minimize total earliness and tardiness that is denoted by
𝐹 | 𝑛𝑤𝑡|∑𝐸 + ∑𝑇 . NWFSSP problems with 𝑚 machines have been proven to be NP-hard
time,
flow
time,𝑚earliness,
tardiness.
In this
the NWFSSP
is conin
the makespan,
strong sense,
where
is higherand
than
3 [5]. There
are study,
a considerable
number
of
sidered
to
minimize
total
earliness
and
tardiness
that
is
denoted
by
F
nwt
E
+
Tj .
|
|
∑
∑
n
j
published studies that dealt with the NWFSSP with makespan, total completion time, or
NWFSSP
problems
with
m
machines
have
been
proven
to
be
NP-hard
in
the
strong
sense,
only tardiness objectives. Correspondingly, total earliness and tardiness objectives may
where
m is higher
than 3studies
[5]. There
are awith
considerable
number
of published
studies that
be
encountered
in many
dealing
scheduling
problems.
In some studies,
the
dealt
with
the
NWFSSP
with
makespan,
total
completion
time,
or
only
tardiness
due date was also included in the model as a constraint rather than an objective.objectives.
The surCorrespondingly,
earliness
and
tardiness
objectives
may be
encountered
in many
vey
by Allahverdi total
[6] covered
over
300
papers in
the literature
containing
no-wait
constudies
dealing
with
scheduling
problems.
In
some
studies,
the
due
date
was
also
included
straints. The problem with the notation 𝐹 | 𝑛𝑤𝑡 | ∑ 𝑇 that considers minimizing only toin the model as a constraint rather than an objective. The survey by Allahverdi [6] covered
tal tardiness was recently studied by Aldowaisan and Allahverdi [7], Liu et al. [8], and
over 300 papers in the literature containing no-wait constraints. The problem with the
Ding et al. [9]. However, a relatively small body of literature is concerned with the
notation Fm | nwt| ∑ Tj that considers minimizing only total tardiness was recently studied
NWFSSP by
minimizing total earliness and tardiness. Some studies [10–16] built the probby Aldowaisan and Allahverdi [7], Liu et al. [8], and Ding et al. [9]. However, a relatively
lem to minimize multiple objectives by integrating due date constraints and objectives
small body of literature is concerned with the NWFSSP by minimizing total earliness and
such as makespan, total flow time, and resource consumption. Huang et al. [17] studied
tardiness. Some studies [10–16] built the problem to minimize multiple objectives by intethe flexible FSSP to minimize total weighted earliness and tardiness under the due-wingrating due date constraints and objectives such as makespan, total flow time, and resource
dow constraint. Some of these studies had the goal of minimizing total tardiness and earconsumption. Huang et al. [17] studied the flexible FSSP to minimize total weighted earliliness with minor nuances. Arabameri and Salmasi [18] handled the weighted objective
ness and tardiness under the due-window constraint. Some of these studies had the goal of
under a sequence-dependent setup time constraint providing a mixed-integer linear prominimizing total tardiness and earliness with minor nuances. Arabameri and Salmasi [18]
gramming
(MILP)
model
and a timing
comparing setup
the performance
of the
cushandled the
weighted
objective
under aalgorithm,
sequence-dependent
time constraint
providtomized
particle
swarm
optimization
(PSO)
and
tabu
search
(TS)
metaheuristics.
Schaller
ing a mixed-integer linear programming (MILP) model and a timing algorithm, comparing
and
Valente [19] of
studied
the NWFSSP
by swarm
minimizing
total earliness
andtabu
tardiness
the performance
the customized
particle
optimization
(PSO) and
searchand
(TS)
compared
dispatching
heuristics.
They
compared
the
dispatching
heuristics
under
the admetaheuristics. Schaller and Valente [19] studied the NWFSSP by minimizing total earliness
ditional
time-allowed
constraint
in another
study [20].
et al. [21]heurisproand tardiness
and compared
dispatching
heuristics.
TheyGuevara-Guevara
compared the dispatching
posed
a
GA
algorithm
for
the
problem
under
a
sequence-dependent
setup
time
constraint
tics under the additional time-allowed constraint in another study [20]. Guevara-Guevara
and
it witha dispatching
heuristics.
Zhu et al.under
[22] implemented
a discrete learnet al.compared
[21] proposed
GA algorithm
for the problem
a sequence-dependent
setup
ing
fruit
fly
algorithm
for
the
distributed
NWFSSP
with
weighted
objectives
under thea
time constraint and compared it with dispatching heuristics. Zhu et al. [22] implemented
common
due datefruit
constraint
and compared
it to only iterated
greedy
idle time
inserdiscrete learning
fly algorithm
for the distributed
NWFSSP
withwith
weighted
objectives
tion
evaluation.
Qiandue
et al.
[23]
applied and
the matrix
cube-based
of distribution
under
the common
date
constraint
compared
it to onlyestimation
iterated greedy
with idle
algorithm
(MCEDA)
under sequence-dependent
setup
andcube-based
release timeestimation
constraints,
time insertion
evaluation.
Qian et al. [23] applied
thetime
matrix
of
benchmarked
with
seven
metaheuristic
algorithms.
distribution algorithm (MCEDA) under sequence-dependent setup time and release time
Ingber [24]
addressed with
the primary
shortcomingalgorithms.
of the SA algorithm as its time-conconstraints,
benchmarked
seven metaheuristic
suming
computational
steps.
Due
to
its
oscillation
during
for alternative
Ingber [24] addressed the primary shortcoming of the
thesearch
SA algorithm
as its solutimetions,
the algorithm
requiressteps.
extensive
time
present reasonable
solutions.
consuming
computational
Due to
its to
oscillation
during the incumbent
search for alternative
Many
parallelized
versions
have been
developed
overcome
this disadvantage.
Figure 1
solutions,
the algorithm
requires
extensive
time totopresent
reasonable
incumbent solutions.
includes
the taxonomy
by Greening
[25]
that was to
produced
during
his doctoral dissertaMany parallelized
versions
have been
developed
overcome
this disadvantage.
Figure 1
tion.
includes the taxonomy by Greening [25] that was produced during his doctoral dissertation.

Figure1.1.Taxonomy
Taxonomyof
ofparallel
parallel simulated
simulated annealing
annealing methodologies
methodologies [25].
[25].
Figure

Greening [25] divided parallel simulated annealing (PSA) algorithms into two main
categories. Synchronous algorithms share information during runtime, while asynchronous
algorithms have limited or no communication. Synchronous algorithms calculate the same
cost function. Asynchronous algorithms work faster by ignoring synchronization and
allowing errors but result in lower outcome quality. Synchronous algorithms are divided

Processes 2023, 11, 454

3 of 26

into two subcategories: serial-like and altered generation. Serial-like algorithms generate
new states as applied in a sequentially running algorithm. Altered generation applies
different strategies for state generation.
In the past years, many studies have been proposed to overcome the disadvantages of
the SA algorithm. Fast simulated annealing (FSA) by Szu and Hartley [26] and very fast
simulated reannealing (VFSA) by Ingber [27] are among the prominent studies that altered
the cooling process for more rapid convergence to the global minimum. Malek et al. [28]
proposed a parallel SA strategy to solve the TSP problem in which parallel algorithms
compare their solutions at a certain timepoint and restart with the initial temperature
with the incumbent solution. On the basis of these studies, Yao [29] proposed a new
simulated annealing algorithm (NSA) that is exponentially faster compared to VFSA. With
a different approach, Roussel-Ragot and Dreyfus [30] suggested a general parallel form
with two different temperature regimes. In this approach, parallel processors are in touch
to update the approved current solution globally when a move is accepted. Mahfoud
and Goldberg [31] integrated SA into the genetic algorithm to enrich the population at
each iteration. Lee and Lee [32] evaluated various types of moving schemes for parallel
synchronous and asynchronous SA strategies with multiple Markov chains. Wodecki
and Bożzejko [33] implemented a parallel SA version considering the flow shop problem
with a makespan objective in which parallel threads run simultaneous searches. In this
implementation, incumbent solutions of all threads are changed to new ones if a thread
finds a better solution than the current best solution. As a similar approach to this study,
Bożejko and Wodecki [34] developed a procedure that runs a master thread and multiple
slave threads. The slave threads iteratively search for better solutions. Upon finding a
better incumbent solution, a thread tries intensification iterations and reports the result. All
slave threads run again on the new incumbent solution with different temperatures. The
results of the study demonstrated average values away from the optimum solution even for
20 jobs. The possible root cause of this failure could be premature convergence due to the
greedy intensification of threads inconsistent with the cooling process of the SA algorithm.
Czapiński [35] worked on the permutation flow shop problem in order to reduce total flow
time. The study included master and worker nodes. Worker nodes obtain feedback on their
results after a certain number of iterations to the master node. The incumbent solution is
updated by the best solution shared with the master node. Worker nodes run again with the
updated incumbent solution as the initial solution. Ferreiro et al. [36] implemented parallelrunning asynchronous graphics processing unit (GPU) threads beginning with the same
instructions but different initial solutions. Sonuc et al. [37] coded another GPU algorithm on
the Compute Unified Device Architecture (CUDA) platform that runs independent threads
to solve the binary knapsack problem. Richie and Ababei [38] provided a synchronous
methodology with a managing thread that distributes the calculations to the worker threads.
Turan et al. [39] suggested the multithread simulated annealing (MTSA) algorithm with
master and slave threads. The created slave thread continues running until the defined
number of non-improving iterations. Non-improving indicates that the global best solution
cannot be improved. Upon completion of the thread runs, solutions are gathered into the
pool. Vousden [40] compared the performances of asynchronous and synchronous SA
implementations with regard to race conditions. Zhou et al. [41] benchmarked multiple
threads of SA without communication initialized with different solutions. Coll et al. [42]
built synchronous GPU threads that communicate in predefined time intervals and resume
their runs on the best incumbent solution so far. Yildirim [43] deployed a multithread
methodology with a hybrid structure where SA is fed by optimizer sub-threads. Even
though many further studies are present in the literature, this review covered most of the
parallelization approaches.
In the remainder of this paper, an MILP model is introduced to define the research
problem. A simulated annealing (SA) metaheuristic variant, namely, the simulated annealing multithread (SAMT) algorithm, is proposed to solve the problem. The contributions of
this algorithm and study are as follows:

Processes 2023, 11, 454

4 of 26

1.
2.
3.
4.

Improving the runtime drawback of the SA algorithm;
Enhancing its robustness to converge to the global optimum solution;
Providing a new solution approach to NWFSSP, minimizing total earliness and tardiness;
Enabling parallel processing without excessive resource allocation.

The motivation behind this study is an aim to contribute to improvements in field
optimization, more specifically metaheuristics. Even though metaheuristics were introduced after intense studies and analysis, there are still open issues to be optimized. A
good example is the study by Deng et al. [44], where the authors improved the mutation
strategy of the differential evolution algorithm and even compared the novel methodology to the previously improved differential evolution algorithm methodologies. Similarly,
Cai et al. [45] worked on the quantum-inspired evolutionary algorithm to improve multiple
shortcomings, such as poor runtime, search capability, and difficulty in assigning rotation
angles. With the same focus, this study introduces a novel methodology that improves
the original SA without requiring excessive computational resources. Section 2 of the
paper states the research problem and details the proposed and benchmark metaheuristic
algorithms. Section 3 introduces the benchmark results and comparative analysis. Section 4
includes the discussion, conclusion, and future prospects.
2. Methodology
The NWFSSP imposes processing of the jobs without interruption from the beginning
on the first machine until completion on the last machine. Since the objective function also
includes minimization of earliness in addition to tardiness, adding a delay between jobs
may improve the objective function value (OFV) by avoiding the early completion of a
job. However, unforced idleness would not be practical in most cases of the NWFSSP [46].
The disadvantages may be operational costs, such as machine running costs, setup costs,
and buffer costs that exceed any cost incurred due to earliness. As a result, the problem
is proposed to have a non-delay schedule. An MILP model is suggested to formulate
the problem. To provide integrality, two dummy jobs with zero processing times on all
machines should be added to the model as the initial and last jobs. Thus, the MILP model
has n00 = n + 2 jobs and m machines. Each job may be processed only on one machine at a
time. Similarly, one machine can process only one job at a time. The proposed MILP model,
its parameters, and its decision variables are outlined below.
Parameters:
gijk = Slack time between completion time of Job j and starting time of Job k on Machine i,
if Job k is processed immediately after Job j.
M = a very large number.
Decision variables:
Ej = Earliness of Job j.
Tj = Tardiness of Job j.
Cij = Completion time of Job j on Machine i.
x jk = 1, if Job k is processed immediately after Job j, and 0 otherwise.
The MILP model on NWFSSP minimizing total earliness and tardiness:
n

n

j =2

j =2

Min z = ∑ Ej + ∑ Tj ,

(1)



Subject to : Cik + M 1 − x jk ≥ Cij + gijk + pik i = 1, . . . , m ; j, k = 1, . . . , n + 2; j 6= k, (2)
m

Cmk + M (1 − x1k ) ≥ ∑ pik ; k = 1, . . . , n + 2,

(3)

Cmj − d j − Tj + Ej = 0; j = 1, . . . , n + 2,

(4)

i =1

Processes 2023, 11, 454

5 of 26

n +2

∑ x jk = 1; k = 1, . . . , n + 2

(5)

j =1

n +2

∑ x jk = 1; j = 1, . . . , n + 2

(6)

x(n+2),1 = 1,

(7)

x jk ∈ {0, 1}; j = 1, . . . , n + 2 ; k = 1, . . . , n + 2 ; j 6= k,

(8)

Cij, Tj , Ej , gijk , pik ≥ 0; i = 1, . . . , m ; j = 1, . . . , n + 2,

(9)

k =1

where the objective function in Equation (1) minimizes the sum of total earliness and
tardiness; the constraint in Equation (2) ensures that the completion time of a job on a
machine is the summation of the completion time of the preceding job, the slack time
between these jobs, and the processing time of the job; the constraint in Equation (3)
guarantees that the completion time of the first job is its total processing time on all
machines; the constraint in Equation (4) calculates the earliness or tardiness by comparing
the completion time and due date of each job; and the constraints in Equations (5) and
(6) ensure that each job has only one predecessor and successor, respectively. The model
consists of n + 2 jobs to satisfy the constraints in Equations (5) and (6). Equation (7) is a
virtual constraint that assigns the first (dummy) job as the predecessor of the last (dummy)
job. It is assumed that each job is processed without any delay once any operation of the
predecessor job does not cause any violation for no-wait processing to be aligned with
real-world applications. Thus, the values of slack time gijk are fixed for any consecutive
jobs independent from their position in the schedule. The calculation of gijk is broadly
explained by Röck [47].
2.1. Neighborhood Operations
Neighborhood operations are applied to reveal neighbor solutions for metaheuristic algorithms. The types of neighborhood operations influence the performance of a
metaheuristic algorithm. Thus, selecting the appropriate operations is the crucial key to
exploring the search space wisely. Three different types are considered in this paper that
are implemented in the proposed or benchmark algorithms.
2.1.1. Insert Operation
The insert operation embraces the insertion of a job in the sequence to a specified
position. Two positions should be determined for this operation. Usually, these positions
are generated randomly or tried successively in an order. Let i and j be integer numbers
from the set {1, . . . , n}. In an insert operation, Job i is removed from the sequence and
inserted into the position prior to Job j. The positions of the jobs after Job j slide toward the
Processes 2023, 11, x FOR PEER REVIEW
6 of 27
end of the schedule. An example operation is shown in Figure 2, where Job 2 is inserted
into Position 4.

Figure 2.
2. Insert
Insert operation
operation of
of Job
Job 22 into
into Position
Position 4.
4.
Figure

2.1.2. Swap Operation
Congruently to an insert operation, two positions should be determined for swap
operations. Let 𝑖 and 𝑗 be integers from the set 1, … , 𝑛 . In the swap operation, the positions of Job 𝑖 and Job 𝑗 are changed mutually. The positions of the remaining jobs do
not change. The example in Figure 3 shows the swap operation of Job 2 and Job 4.

Processes 2023, 11, 454

6 of 26

Figure 2. Insert operation of Job 2 into Position 4.

2.1.2.
2.1.2. Swap Operation
Congruently
Congruently to an
an insert
insert operation,
operation, two
two positions
positions should
should be
be determined
determined for
for swap
swap
operations.
Let 𝑖i and 𝑗j be
the set
set {1,1,…. ., .𝑛, n. }In
. In
swap
operation,
operations. Let
be integers from the
thethe
swap
operation,
the the
popositions
Job
i andJob
Job𝑗 jare
are changed
changed mutually.
mutually. The
The positions
positions of the remaining jobs do
sitions of of
Job
𝑖 and
do
not
not change.
change. The example in Figure
Figure 33 shows
shows the
the swap
swap operation
operation of
of Job
Job 22 and
and Job
Job 4.
4.

Figure 3.
3. Swap
Swap operation
operation of
of Job
Job 22 and
and Job
Job 4.
4.
Figure

2.1.3.
2.1.3. Sub-Interchange
Sub-Interchange Operation
Operation
Defined
[18],
sub-interchange
is executed
by changing
two
Defined by
byArabameri
Arabameriand
andSalmasi
Salmasi
[18],
sub-interchange
is executed
by changing
adjacent
jobs jobs
Job i Job
and𝑖 Job
1. 𝑖 It
that running
sub-interchange
operations
two adjacent
andi +
Job
+ is
1. believed
It is believed
that running
sub-interchange
operaafter
the incumbent
solution
may result
in a better
solution.
tionsupdating
after updating
the incumbent
solution
may result
in a better
solution.
2.2. Proposed Algorithm—Simulated Annealing Multithread (SAMT)
2.2. Proposed Algorithm—Simulated Annealing Multithread (SAMT)
The SAMT algorithm is based on the simulated annealing (SA) metaheuristic. ProThe SAMT algorithm is based on the simulated annealing (SA) metaheuristic. Proposed by Kirkpatrick [48], the SA simulates the annealing process of solids to solve combiposed by Kirkpatrick [48], the SA simulates the annealing process of solids to solve comnatorial optimization problems. In physics, annealing specifies the process in which solids
binatorial optimization problems. In physics, annealing specifies the process in which solare heated rapidly to a maximum temperature and cooled down slowly in heat baths to
ids are heated rapidly to a maximum temperature and cooled down slowly in heat baths
allow them to arrange themselves in the ground state of the solid [49]. The algorithm is
to allow them to arrange themselves in the ground state of the solid [49]. The algorithm is
initialized with a high temperature and cooled slowly. These moves during the cooling proinitialized with a high temperature and cooled slowly. These moves during the cooling
cess avoid algorithm trapping in local optima [50]. The flow of the classical SA algorithm is
process avoid algorithm trapping in local optima [50]. The flow of the classical SA algostated in Algorithm 1 [51].
rithm is stated in Algorithm 1 [51].
Algorithm 1 Simulated Annealing

Algorithm 1 Simulated Annealing

1: Select an initial solution in the solution space s ∈ SS
1: SetSelect
an initial
solution
2:
the initial
temperature
T, in the solution space 𝑠 ∈ 𝑆𝑆
2: SetSet
initial temperature
𝑇, i = 0,
3:
thethe
temperature
iteration counter
4:
thethe
maximum
numberiteration
of repetitions
nmax𝑖 = 0,
3: SetSet
temperature
counter
5:
While
(Stopping
criteria
are
not
met)
4:
Set the maximum number of repetitions 𝑛
6:
Set n = 0,
5:
While (Stopping criteria are not met)
7:
While (n < nmax )
6:
Set 𝑛a new
= 0, solution s0 ∈ SS
8:
Generate
0 ) − f)(s )
7:
While
9:
Calculate ∆ (𝑛
= f<(s𝑛
10:
If (∆ < 0) Generate a new solution 𝑠 ∈ 𝑆𝑆
8:
11:
Set s = s0
12:
Else
−∆
13:
If (Uniform(0, 1) < e( T ) )
14:
Set s = s0
15:
Set n = n + 1
16:
Do
17:
Set i = i + 1
18:
Set T = T (i )
19: Do

A review of the literature suggests that there are still open fields for parallel implementation of the SA algorithm. In this study, a novel approach including the utilization

Processes 2023, 11, 454

7 of 26

of multiple threads is proposed. The simulated annealing multithread (SAMT) algorithm
is proposed to overcome the time disadvantage of the classical SA algorithm and boost
the convergence process. The algorithm is named after its pragmatic structure in which
classical SA runs on a main thread supported by a sub-thread that iteratively updates
the incumbent solution of the main thread with much faster SA runs. Rather than distributing the calculations of the algorithm to available processors, this parallelism aims to
run different SAs simultaneously to improve the consumed time and search the solution
space intelligently to find the global optimum. The SAMT algorithm falls into the altered
generation class of synchronous algorithms considering Greening’s taxonomy [25] with
shared memory. The novel methodology flow is demonstrated in Algorithm 2.
Algorithm 2 Simulated Annealing Multithread (SAMT)
1: Select initial solutions in the solution space sm = st ∈ SS
2: Set the initial temperature T0m
3: Set the temperature iteration counter im = 0
4: Set the maximum number of repetitions nmax
5: Set the operator selection probability ProbOperation ∈ (0, 1)
6: Set the fast sub-thread’s initial temperature T0 f t
7: Set the slow sub-thread’s initial temperature T0st
8: Set the fast sub-thread iteration counter i f t = 0
9: Set the fast sub-thread iteration counter ist = 0
10: Set the thread selection probability coefficient c ∈ (0, 1)
11: MAIN THREAD:
12: While (Stopping criteria are not met)
13:
If (SUB-THREAD is not running)
14:
Calculate ∆ = f (st ) − f (sm )
15:
If (∆ < 0)
16:
Set sm = st
17:
Else
18:
Set st = sm
19:
Run (SUB-THREAD)
20:
Set nm = 0,
21:
While (nm < nmax )
22:
If (Uni f orm(0, 1) < ProbOperation )
23:
s0m = Insert(sm )
24:
Else
25:
s0m = Swap(sm )
26:
Calculate ∆ = f (s0m ) − f (sm )
27:
If (∆ < 0)
28:
Set sm = s0m
29:
Else
−∆

30:
If (Uni f orm(0, 1) < e( Tm ) )
31:
Set sm = s0m
32:
Set nm = nm + 1
33:
Do
34:
Set Tm (im ) = Tm (im + 1)
35:
Set im = im + 1
36: Do
37: Return sm and f (sm )
38: SUB-THREAD:


39:

40:
41:
42:
43:
44:
45:

(1−2c)∗Tm (im )
Tm ( 0 )

< Uni f orm(0, 1))
While (Stopping criteria are not met)
Set nt = 0,
While (nt < nmaxst )
If (Uni f orm(0, 1) < ProbOperation )
s0t = Insert(st )
Else

If (c +

Processes 2023, 11, 454

8 of 26

46:
47:
48:
49:
50:

s0t = Swap(st )
Calculate ∆ = f (s0t ) − f (st )
If (∆ < 0)
Set st = s0t
Else

51:
52:
53:
54:
55:
56:
57:
58:
59:
60:
61:
62:
63:
64:
65:
66:
67:
68:
69:

If (Uni f orm(0, 1) < e Tst )
Set st = s0t
Set nt = nt + 1
Do
Set Tst (ist ) = Tst (ist + 1)
Set ist = ist + 1
Do
Else
While (Stopping criteria are not met)
Set nt = 0,
While (nt < nmaxst )
If (Uni f orm(0, 1) < ProbOperation )
s0t = Insert(st )
Else
s0t = Swap(st )
Calculate ∆ = f (s0t ) − f (st )
If (∆ < 0)
Set st = s0t
Else

70:
71:
72:
73:

If (Uni f orm(0, 1) < e T f t )
Set st = s0t
Set nt = nt + 1
Do
 



74:
75:
76:

( −∆ )

( −∆ )

Set T f t i f t = T f t i f t + 1
Set i f t = i f t + 1
Do

The methodology should be initialized by the setting of parameters. Prior to finalizing
this methodology, several alternative policies are considered, compared, and tested in terms
of simplicity, runtime, efficiency, and implementation complexity. These policies include
a different number of threads with distinct completion times and different schemes of
Processes 2023, 11, x FOR PEER REVIEW
9 of 27
solution updates. The threads in the proposed methodology
have different roles. The fast
thread decreases the runtime by jumping to better solutions in the vicinity of the current
terms of
simplicity, runtime,
efficiency,steps.
and implementation
complexity.
policies
best
solution
with faster
This thread
mayThese
also
manipulate the search by orienting the
include a different number of threads with distinct completion times and different
direction
toward
different
if the
threadhave
provides
schemes of solution
updates.
The threads “hills”
in the proposed
methodology
different a better solution. The slow thread
roles. The fast thread decreases the runtime by jumping to better solutions in the vicinity
has
different aims, such as enabling moves to longer distances in the vicinity, jumping to
of the current best solution with faster steps. This thread may also manipulate the search
by orientingsolutions
the direction toward
different “hills”
if the thread
a better solution.
similar
of nearby
optima,
orprovides
diverging
from local optima. Possible jumps after
The slow thread has different aims, such as enabling moves to longer distances in the
the
completion
of solutions
a sub-thread
are or
presented
Figure
vicinity,
jumping to similar
of nearby optima,
diverging fromin
local
optima. 4.
Possible jumps after the completion of a sub-thread are presented in Figure 4.

Figure 4. Possible jumps by sub-threads on OFV curve.

Figure 4. Possible jumps by sub-threads on OFV curve.

If the sub-thread results in a solution sequence with a better OFV than the global
incumbent solution, the global incumbent solution is updated. An adaptive strategy with
a single sub-thread provided the best solutions After some experimental runs with different parameters, the results also showed that adjusting the initial temperature and runtime
of the sub-thread should be adaptive to achieve elite results. Therefore, the methodology
is revised to have a single master (main) thread and a slave (sub) thread, and the assignment of the algorithm speed (slow or fast) is conducted dependent on a predefined parameter. This strategy attempts to seek a larger space and decreases the probability to be
stuck in local optima due to premature convergence. Both insert and swap operators work

Processes 2023, 11, 454

9 of 26

If the sub-thread results in a solution sequence with a better OFV than the global
incumbent solution, the global incumbent solution is updated. An adaptive strategy with a
single sub-thread provided the best solutions After some experimental runs with different
parameters, the results also showed that adjusting the initial temperature and runtime of
the sub-thread should be adaptive to achieve elite results. Therefore, the methodology is
revised to have a single master (main) thread and a slave (sub) thread, and the assignment
of the algorithm speed (slow or fast) is conducted dependent on a predefined parameter.
This strategy attempts to seek a larger space and decreases the probability to be stuck in
local optima due to premature convergence. Both insert and swap operators work well
on the NWFSSP. Both operators are utilized in the proposed methodology to benefit from
each and avoid becoming trapped in a cycle. At each iteration, the algorithm runs the
insert operator with the probability ProbOperation or the swap operator with the probability
1 − ProbOperation . The temperature-dependent type selection function in the first line of the
sub-thread determines the type of sub-thread depending on the temperature of the main
thread. The value of the constant c determines the initial probabilities to select a fast or
slow thread. In cases where c > 0.50, the slow thread has a lower probability to be selected
at the beginning of the run and the probability increases while Tm decreases. If c < 0.50,
then the fast thread has the advantage with a higher probability. The value c = 0.50 grants
equal probability during all the runs.
2.3. Benchmark Algorithms
The variants of tabu search (TS) and particle swarm optimization (PSO) in the study by
Arabameri and Salmasi [18] were selected as benchmark algorithms since these metaheuristics were applied to the same research problem. The benchmark algorithms are introduced
in Appendix A, where item A1 introduces the TS and its variants: TS with the EDD initial
solution and insertion neighborhood (TSEI), the TS algorithm with a random initial solution
and insertion neighborhood (TSRI), the TS algorithm with the EDD initial solution and
swap neighborhood (TSES), and the TS algorithm with a random initial solution and swap
neighborhood (TSRS); while item A2 describes the PSO algorithm supported by integrating two different local search algorithms: insertion (PSOI) and variable neighborhood
structure (PSOV).
2.4. Test Problems
The test problems are selected from the datasets already introduced by different studies. These problems are widely considered in the literature for benchmark purposes of
scheduling problems. The proposed and benchmark algorithms are verified on Carlier’s
dataset [52], which has eight small-sized problems with 7–14 jobs and 4–9 machines. The
process times in the dataset are generated with a pattern of sorting the digits adjacently. Another dataset for benchmarking consists of the scheduling problems defined by Reeves [53].
Reeves generated this dataset to test his proposed genetic algorithm to solve the FSSP problem. The reason for generating this dataset was his failure to find a publicly shared dataset
for this purpose since there is some evidence that process times cannot be completely
random [54]. Reeves generated this dataset using the suggestions by Rinnooy [55] and his
parameters. The dataset has a maximum of 75 jobs and 20 machines beginning from 20 jobs
and five machines. The famous Taillard dataset [56] is also included for comparison of the
algorithms. The dataset comprises problems with a range of 20–500 jobs and 5–20 machines.
Taillard included in his dataset hard problems to be solved. The process times are created
randomly from a uniform distribution (1, 100). Due to the high number of problems, only
the first problems with the same number of jobs and machines in the datasets by Reeves
and Taillard are considered.

Processes 2023, 11, 454

10 of 26

Due dates for the problems are created according to the rule proposed by Arabameri
and Salmasi [18]. The due date may be randomly produced from the interval in
Equation (10).





R
R
, LB × 1 − TF +
,
(10)
d j ∼ LB × 1 − TF −
2
2
where LB is the lower bound of the makespan, TF is the tightness factor, and R is the
range parameter. The TF and R values are selected from the set {0.2, 0.5, 0.8}. To avoid the
possibility of negative due date creation, {0.8, 0.5} and {0.8, 0.8} combinations are ignored
for TF and R, respectively. Hence, a total of 27 different problems are solved with seven
different due date schemes, resulting in 189 combinations. Among the methods to calculate
the LB in the literature, the method by Taillard [56] is preferred due to its concrete and
meaningful structure. The LB can be calculated according to Equation (11).
(
!)
m

LB = max max(αi + β i + γi ), max
i

j

∑ pij

,

(11)

i =1

where αi , β i , and γi are formulated according to Equations (12)–(14), respectively.
!
i −1

∑ pk j

αi = min
J

(12)

k =1
n

β i = ∑ pij

(13)

j =1

m

γi = min
j

∑ pkj

!
(14)

k = i +1

The problems are divided into three groups according to their sizes considering the
number of jobs. Small-sized problems in Group 1 have up to 20 jobs to be processed.
Medium-sized problems in Group 2 consist of 20–100 jobs. Large-sized problems in Group
3 consist of over 100 jobs.
3. Results
3.1. Results of the Benchmark Runs
All of the metaheuristics involved in this study have several parameters that should be
tuned to achieve favorable solutions. Additionally, the common parameters for benchmark
runs should be determined. The maximum runtime of any run is limited by a function
considering the number of jobs, as stated in Table 1. All metaheuristics except the TSEI and
TSES algorithms are initialized with a random sequence to avoid any bias. The TSEI and
TSES algorithms are initialized with the sequence provided by the EDD rule in which the
jobs with earlier due dates are processed earlier.
Table 1. Runtime limits considering the size of the problem.
Problem Size

Runtime Limit (in s)

Small
Medium
Large

n/2
n∗2
n∗3

The initial temperature of the SA algorithm should be set to a value that allows
acceptance of worse solutions with a determined probability, decreasing systematically.
Since the test runs are terminated according to the runtime criteria for all algorithms, the

Processes 2023, 11, 454

11 of 26

temperature of the SA algorithm is intended to be decreased as a function of time according
to Equation (15) in this study.


tcur
T ( i + 1) = T ( i ) × 1 −
.
(15)
tmax
The parameter tcur in Equation (15) denotes the elapsed time, whereas tmax is the total
assigned runtime. The algorithm stops when the temperature drops to zero. Similarly,
the temperatures of the main and support threads of the SAMT algorithm should also
be managed for smooth synchronization. However, the time limit of the threads should
be arranged within the time limits of the main thread. Tuning the parameters has a high
influence on the performance of a metaheuristic. The guideline by LaTorre et al. [57]
identifies several methods that have gained recent attention to tune the parameters of
metaheuristic algorithms. The focus iterative local search (FocusILS) methodology [58]
was preferred to tune the parameters of the SAMT algorithm. T0m was selected from
a set increasing by 50 until 500 degrees. The set {0.25, 0.50, 0.75} was assigned to find
the best value of constant c and ProbOperation . T0 f t and T0st were tuned by dividing T0m
up to 10. The initial temperature of the SAMT algorithm may be selected as half of the
SA algorithm for better and faster convergence. Insert or swap operators are selected
with equal probability at each iteration. Running the fast thread more frequently at the
initial phase of the algorithm eases discovering the vicinity of the current solution. Rare
searches with a slower thread at this phase produce faster jumps toward the optima region
if possible. The probability of using the slow thread toward the end of the runtime should
be increased. This change is needed to allow the sub-thread to jump from local optima to
different optimum regions by climbing the hills. Setting the parameter c to 0.25 assigns the
probability of running the fast thread to 0.75 and the slow thread to 0.25. The probability
of the fast thread decreases and the slow thread increases linearly during runtime until
the probability of selecting the fast thread stabilizes at 0.25 and that of the slow thread
stabilizes at 0.75. The parameters of the SAMT algorithm are shown in Table 2.
Table 2. The settings of the SAMT algorithm.
Parameter
T0m :
im :
nmax :
ProbOperation :
T0 f t :
T0st :
Fast Thread Runtime:
Slow Thread Runtime:
c:

Value
Number of jobs
Following the total assigned runtime
10
0.50
T0m
5
T0m
3
Master Thread Runtime
150
Master Thread Runtime
60

0.25

The PSO algorithm is dependent on various parameters and variables that directly
affect the performance of the algorithm. Tuning these parameters with ineligible strategies
may lead to disadvantages, such as premature convergence or failing to converge to the
region near the optimum solution. The constants and variables are set to the values suggested by Arabameri and Salmasi [18] to achieve a consequential benchmark environment.
The settings for the PSO algorithm are shown in Table 3.

Processes 2023, 11, 454

12 of 26

Table 3. The settings of PSO algorithms.
Variable/Parameter

Value/Formula

c1
c2
w (PSOI)
w (PSOV)
p − size (PSOI)
p − size (PSOV)
Number of local search iterations

2.05
2.05
cur
0.9 − 0.5xt
tmax
1.0
30
20
10 × n

While the w value for the PSOV algorithm is set to a fixed value, the value for the
PSOI algorithm is updated regularly at each iteration dependent on a maximum number of
iterations tmax and current iteration tcur .
The metaheuristics are compared with the percentage gap (PG), which is the relative
percentage deviation of the algorithm compared to the best solution. PG may be calculated
according to Equation (16).
PG =

( AlgOFV − MinOFV )
× 100,
MinOFV

(16)

where AlgOFV is the OFV value of the selected algorithm, and MinOFV is the minimum OFV
value provided by all algorithms for the corresponding problem. Since the metaheuristics
have a stochastic nature, all metaheuristics had triple runs for each benchmark problem.
The result tables show the average PG of three runs at each problem. SAMT has a main
thread and a sub-thread during its runs. For the sake of fairness, the benchmark algorithms
were run twice at each iteration, and the better solution was selected as if they ran two
threads asynchronously. Algorithms were coded in the C# programming language. The
codes were compiled and run on a single computer with Intel(R) Core (TM) i7-6500U CPU
and 8 GB RAM.
The accuracies of the metaheuristic algorithms were verified by comparing them with
the MILP results solved on the Carlier dataset. Each problem in the dataset was assigned
seven due dates with different due dates creating schemes resulting in 56 test problems.
The problems were solved using the Gurobi Solver optimally. Each algorithm could find
the optimal result for each problem.
The results of the Reeves dataset are shared in Table A1 of Appendix B. The table has
solutions for 49 problems. The last digit in the problem names represents the index for the
due date scheme. The results of the Taillard dataset are shown in Table A2 of Appendix B.
The table contains 84 problems. The indices and corresponding TF and R values for due
date creation are shown in Table 4.
Table 4. Due date creation scheme.
Index

TF

R

1

0.20

0.20

2

0.20

0.50

3

0.20

0.80

4

0.50

0.20

5

0.50

0.50

6

0.50

0.80

7

0.80

0.20

Processes 2023, 11, 454

13 of 26

3.2. Comparative Analyses
The algorithms are evaluated under identical conditions and on the same test problems.
Therefore, comparative analyses are performed through analysis of variance (ANOVA)
considering solutions of the benchmark in terms of the robustness of the results. The
two-way ANOVA results in Table 5 reveal that the factors job and algorithm, as well as
their interaction, have a significant effect on the values of PG.
Table 5. ANOVA table for PG.
Level

DoF

Sum of Sq.

Mean Sq.

F Value

Prob. (>F)

Algorithm

7

115.8

16.54

47.57

0.0000

Group

2

581.3

290.65

835.75

0.0000

Algorithm × group

14

162.5

11.61

33.37

0.0000

Residual

1488

517.5

0.35

Due to the significance, post hoc analyses were conducted to reveal the differences
in the group × algorithm interaction with pairwise comparisons. A concern during this
analysis is keeping the family-wise error rate under control [57]. Tukey’s HSD (honestly
significant difference) and Scheffe tests were applied for pairwise comparisons. Tukey’s
HSD has a high sensitivity for pairwise comparisons in balanced conditions while the
Scheffe method maintains the family-wise error rate under strict control [59]. A p-value
lower than 0.05 shows that the instances are significantly different. Small-sized problems,
in terms of the number of jobs, are not taken into consideration for evaluation since all the
algorithms return the same OFV for all problems in this group.
The comparison results of Tukey’s HSD statistics for medium-sized problems are
demonstrated in Table A3 of Appendix C. The results in Table A1 reveal that the TSRS
algorithm performs significantly worse compared to the PSOI, PSOV, SA, and SAMT
algorithms, whereas the TSES algorithm has worse results compared to the SA and SAMT
algorithms in terms of OFV performance. The remaining values explain that there is no
significant difference among the SA, SAMT, TSRI, TSEI, PSOI, and PSOV algorithms in this
group. As a result, only the TS algorithms with the swap operator dissociate from the group
since they provide considerably low-quality solutions. Tukey’s HSD results for large-sized
problems in Table A4 of Appendix C prove that the problems supply different solution
qualities when the size of the problem increases. Only the means of three comparisons are
similar according to Table A2, which are PSOV vs. PSOI, TSRI vs. PSOI, and TSRI vs. TSEI.
The SAMT algorithm notably outperforms the remaining metaheuristic algorithms with a
consistent solution quality at all levels. Figure 5 shows the increasing distinction of solution
robustness provided by different algorithms in terms of PG means vs. the number of jobs.
The post hoc results for PG according to the Scheffe method in Table A5 of Appendix C align
with the results of Tukey’s HSD. Having higher p-values to avoid type I error, the analysis
suggests that the SAMT performs significantly better than TSRS considering medium-sized
problems, in addition to outperforming all algorithms considering large-sized problems.
Apart from the robustness of the solution, the runtime to find the best OFV is another
characteristic that should be assessed to determine the performance of the algorithms.
Another two-way ANOVA table is established to understand whether there is a significant
difference or not among the mean values of runtimes of the algorithms.

gorithms with a consistent solution quality at all levels. Figure 5 shows the increasing
distinction of solution robustness provided by different algorithms in terms of PG means
vs. the number of jobs. The post hoc results for PG according to the Scheffe method in
Table A5 of Appendix C align with the results of Tukey’s HSD. Having higher p-values to
avoid type I error, the analysis suggests that the SAMT performs significantly better than
14 of 26
TSRS considering medium-sized problems, in addition to outperforming all algorithms
considering large-sized problems.

Processes 2023, 11, 454

Average PG

Average PG vs No. of Jobs
5
4.5
4
3.5
3
2.5
2
1.5
1
0.5
0
20

30

50

75

100

200

500

No. of Jobs
SAMT

SA

TSEI

TSRI

TSES

TSRS

PSOV

PSOI

Figure 5.
5. Average
percentage gap
gap vs.
vs. no.
no. of
of jobs.
jobs.
Figure
Average percentage

Apart
from the
robustness
solution,
runtime
to find
theruntimes
best OFVisisnot
another
The
ANOVA
results
in Tableof6the
reveal
that atthe
least
one mean
of the
equal
characteristic
that
should
be
assessed
to
determine
the
performance
of
the
algorithms.
to the remaining means. Only Tukey’s HSD comparisons that are significantly different are
Another
two-way
ANOVA
table
established
to understand
whether
there method
is a signifilisted
in Table
A6 of
Appendix
C, is
and
the significant
results from
the Scheffe
are
cant difference
shown
in Table or
A7.not among the mean values of runtimes of the algorithms.
The ANOVA results in Table 6 reveal that at least one mean of the runtimes is not
Table
table for means.
runtime.Only Tukey’s HSD comparisons that are significantly difequal6.toANOVA
the remaining
ferent are listed in Table A6 of Appendix C, and the significant results from the Scheffe
Level
DoF
Sum of Sq.
Mean Sq.
F Value
Prob.(>F)
method are shown in Table A7.
Algorithm

7

277,595

Table 6. ANOVA
table for runtime.
Job
13
123,270,879
Algorithm
Level × job

39,656

42.9

0.0000

9,482,375

10,258.8

0.0000

1,017,397
11,180
12.1
0.0000
DoF91
Sum
of Sq.
Mean
Sq.
F Value
Prob.(>F)
1400
1,294,042
924
7
277,595
39,656
42.9
0.0000
Job
13
123,270,879
9,482,375
10,258.8
0.0000
Algorithm
× job of Tukey’s
91
0.0000
The p-value
HSD1,017,397
test in Table A611,180
proves that the12.1
mean runtimes
to find
the best
solution of the
SA and SAMT
algorithms are
Residual
1400
1,294,042
924 significantly different for problems
with at least 50 jobs. The SAMT algorithm also provides a runtime advantage compared to
all benchmark
metaheuristics
for problems
with
and 500
Evaluating
the to
results
The p-value
of Tukey’s HSD
test in Table
A6200
proves
thatjobs.
the mean
runtimes
find
from
thesolution
Scheffe method
in and
TableSAMT
A7 asalgorithms
a group suggests
that SAMTdifferent
can find for
the problems
best OFV
the best
of the SA
are significantly
significantly
more
rapidly
than SA,
TSEI, PSOI,
and PSOV
for the problems
that
contain
with at least 50
jobs.
The SAMT
algorithm
also provides
a runtime
advantage
compared
200
as well as
more rapidly than
all algorithms
in the
case
the job
number the
increasing
to alljobs,
benchmark
metaheuristics
for problems
with 200
and
500ofjobs.
Evaluating
results
to
500.
According
to
Figure
6,
it
is
possible
to
conclude
that
the
SAMT
algorithm
needs
a
from the Scheffe method in Table A7 as a group suggests that SAMT can find the best OFV
shorter
runtime
to
find
the
best
OV
in
comparison
to
the
SA
algorithm,
thus
yielding
better
significantly more rapidly than SA, TSEI, PSOI, and PSOV for the problems that contain
or
algorithm
better
or case
equalofobjective
functionincreasvalues
200equal
jobs, solutions.
as well as The
moreSAMT
rapidly
than all provides
algorithms
in the
the job number
in
shorter
run
times
compared
to
the
SA
algorithm.
ing to 500. According to Figure 6, it is possible to conclude that the SAMT algorithm needs
Residual
Algorithm

Processes 2023, 11, x FOR PEER REVIEW

15 of 27

a shorter runtime to find the best OV in comparison to the SA algorithm, thus yielding
15 of 26
better or equal solutions. The SAMT algorithm provides better or equal objective function
values in shorter run times compared to the SA algorithm.

Processes 2023, 11, 454

Average Runtime to Find the Best Solution

Processes 2023, 11, x FOR PEER REVIEW

1600

1,452.14

1400

a shorter runtime to find the best OV in comparison to the SA algorithm, thus yielding
better or equal solutions. The SAMT algorithm provides better or equal objective function
values in shorter run times compared to the SA algorithm.

1,096.00

1000

Average Runtime to Find the Best Solution

800
600

1400

400

1200

0

545.29

1600

Runtime

Runtime

1200

200

15 of 27

1,452.14

1000

27.21
800
8.64
600

137.14
65.14

78.96
38.32
30

50

75

100

0

SAMT
30

260.81
No. of
Jobs

137.14
65.14

78.96
38.32

27.21
8.64

SA

TSEI

50

1,096.00

545.29

400
200

410.36

260.81
185.29

200

410.36

500

185.29

TSES

TSRI

TSRS

75

PSOV

100

PSOI
200

500

No. of Jobs

Figure 6. Comparison of average runtimes to find the best solution.
Figure 6. Comparison of average runtimes to find the best solution.
SAMT

SA

TSEI

TSES

TSRI

TSRS

PSOV

PSOI

Figure77demonstrates
demonstratesthe
theimprovement
improvementby
bySAMT
SAMTcompared
comparedto
tothe
theclassical
classicalSA.
SA.The
The
Figure
Figure
6. Comparison
of the
average
runtimes
find
the
best solution.runs
SAMT
compared
average
ofto two
asynchronous
runs
offor
SAbeing
for being
fair.
the
SAMT
isiscompared
toto
the
average
of two
asynchronous
of SA
fair. In
theIncase
case
GP,Scheffe
both Scheffe
and Tukey’s
HSDhoc
post
hoc analysis
suggests
that SAMT
is signifof
GP,ofboth
and
Tukey’s
HSD
post
analysis
suggests
that
SAMT
is
significantly
Figure 7 demonstrates the improvement by SAMT compared to the classical SA. The
icantly
for the toproblems
inof the
large-sized
set.increases
The
PGbeing
increases
nearly
linearly
better
forbetter
the
problems
in
large-sized
set. The PG
nearly
while
the
SAMT
is compared
thethe
average
two asynchronous
runs
of
SA for
fair.linearly
In the
number
ofofnumber
jobs
increases
as
seen
inHSD
Figure
7a.
Considering
the
runtime
to
find the
GP, both
Scheffe
Tukey’s
post hoc
analysis
suggests
that SAMT
is
signifwhilecase
the
of jobsand
increases
as
seen
in Figure
7a. Considering
the
runtime
tobest
find
icantly
better HSD
for
thesuggests
problems
in
theSAMT
large-sized
set. The
increases
nearly
solution,
Tukey’s
is better
for
problems
75linearly
orwith
more75
jobs.
The
the best
solution,
Tukey’s
HSDthat
suggests
that
SAMT
isPG
better
for with
problems
or more
while the number of jobs increases as seen in Figure 7a. Considering the runtime to find
more
Scheffe method
suggests
that
the number
of number
jobs should
be ashould
minimum
jobs. conservative
The
more
conservative
Scheffe
method
suggests
that
the
of
jobs
be a
the best solution, Tukey’s HSD suggests that SAMT is better for problems with 75 or more
of
200jobs.
to derive
significance.
Figure
7b
presents
that
the
difference
gradually
increases
minimum
of
200
to
derive
significance.
Figure
7b
presents
that
the
difference
gradually
The more conservative Scheffe method suggests that the number of jobs should be a
with
an
exponential
trend.
post hoc
analysis
and
Figure
7 confirm
that
the proposed
minimum
200exponential
to
derive The
significance.
Figure
7b presents
that
theand
difference
gradually
increases
withofan
trend.
The
post
hoc
analysis
Figure
7 confirm
that the
increases
with
an
exponential
trend.
The
post
hoc
analysis
and
Figure
7
confirm
that
the
SAMT
outperforms
the
classical
SA
in
terms
of
both
runtime
and
solution
robustness,
even
proposed SAMT outperforms the classical SA in terms of both runtime and solution
roproposed
SAMT
outperforms
the
classical
SA
in
terms
of
both
runtime
and
solution
roifbustness,
the SA runs
two
asynchronous
threads
and the better
OFVand
of these
threads
is selected
even
if
the
SA
runs
two
asynchronous
threads
the
better
OFV
of
these
bustness, even if the SA runs two asynchronous threads and the better OFV of these
for
comparison.
threads
is selected
for
threads
is selected
forcomparison.
comparison.

(a)

(b)

Figure 7. Average PG (a) and runtime to find the best solution (b). Comparison of SA and SAMT

Figurefor
7. significantly
Average PG
(a) and
runtime to find the best solution (b). Comparison of SA and SAMT for
different
cases.
(a)
(b)
significantly
different cases.

7. Average
(a) and runtime to find the best solution (b). Comparison of SA and SAMT
4.Figure
Discussion
andPG
Conclusions
for significantly different cases.

In this paper, a novel parallel metaheuristic methodology named SAMT based on SA
was proposed. The motivation of the study was to improve the poor runtime performance
and search capability of the classical algorithm. In the methodology, a sub-thread runs
in parallel to update the search direction of the main thread adaptively. The aim is to

Processes 2023, 11, 454

16 of 26

increase the capability of classical SA to find better solutions in shorter runtimes. The
NWFSSP with earliness and tardiness objectives, Fn | nwt| ∑ Ej + ∑ Tj , is considered for
benchmarking. The literature review revealed that earliness and tardiness objectives for
NWFSSP have not been widely studied. The most common practice to solve the research
problem benefits from dispatching rules and heuristics. A major problem with dispatching
rules and heuristics is their incapability to update themselves during runtime in contrast
to metaheuristics. The study by Arabameri and Salmasi [18] was selected as the reference
for benchmarking since the study included two important metaheuristic algorithms with
different parameters.
The test runs and results of comparative analyses revealed that the SAMT algorithm
could provide more robust solutions compared to the classical SA algorithm, variants of
the PSO algorithms, and TS algorithms, whereby the solutions of the SAMT algorithm
were slightly better in most cases of medium-sized problems and all cases of large-sized
problems, even when the benchmark algorithms ran double asynchronous threads. Another
contribution of this study was the enhancement of the runtime to provide a better solution
in comparison to the SA algorithm. The SAMT algorithm consumed less time to find
the best solution in large problems compared to benchmark problems. Unlike parallel
computing, the proposed SAMT algorithm introduces independent parallel threads to
enhance the robustness of the solution and overcome the runtime disadvantage of the
classical SA algorithm. As intended, multiple threads of the SAMT algorithm grant a
divergence–convergence strategy that enables the algorithm to explore the solution space
more thoroughly and rapidly. The adaptive search strategy with a single slave thread is
the novelty of this study. A temperature-dependent function stochastically determines
the speed of the sub-thread at each run. Thus, the algorithm is adapted to jump into the
solution space to decrease runtime and increase robustness.
The number of threads and parameters of the SA algorithm for each thread directly
affected the performance of the SAMT algorithm. Hence, it is important to fine-tune each
parameter systematically. An easy implementation for a single computer is through the
FocusILS parameter tuning tool. The contribution of the study is the adaptive parameter
tuning strategy of a single slave thread after analysis with the design of experiments (DOE).
The purpose of the study was to present that the SA algorithm may be improved in terms of
both time and result performance without excessive resource requirements, and the newly
proposed algorithm is a robust methodology to solve the NWFSSP with the objective of
addressing total earliness and tardiness. In future studies, the method may be enhanced by
deploying it on multiple CPUs/GPUs with a distributed programming methodology. This
method will be evaluated on different combinatorial optimization problems to confirm its
efficiency. Another aspect will be to adapt different types of metaheuristics to a parallel
methodology to solve the NWFSSP, before comparing them with the SAMT algorithm.
Author Contributions: Conceptualization, I.K., O.S. and S.B.; methodology, I.K., O.S. and S.B.;
software, I.K.; validation, I.K. and O.S.; formal analysis, I.K. and O.S.; investigation, I.K.; resources,
I.K.; data curation, I.K.; writing—original draft preparation, I.K.; writing—review and editing, O.S.
and S.B.; visualization, I.K.; supervision, O.S. and S.B.; project administration, S.B. All authors have
read and agreed to the published version of the manuscript.
Funding: The APC was funded by the company AN-EL Anahtar ve Elektrikli Ev Aletleri Sanayi A.S.
Institutional Review Board Statement: Not applicable.
Informed Consent Statement: Not applicable.
Data Availability Statement: Scheduling problems were selected from the datasets introduced
by Carlier [52], Reeves [53], and Taillard [56]. Due dates were randomly created as explained in
the paper.
Conflicts of Interest: The authors declare no conflict of interest. The funders had no role in the design
of the study; in the collection, analyses, or interpretation of data; in the writing of the manuscript; or
in the decision to publish the results.

Processes 2023, 11, 454

17 of 26

Appendix A
This appendix includes the descriptions of benchmark algorithms.
Appendix A.1. Tabu Search (TS)
The TS algorithm was proposed by Glover [60] to solve integer programming problems. Furthermore, Glover et al. [61] published a user guide introducing perspectives for
implementing TS on combinatorial or nonlinear problems. TS has been widely applied to
scheduling problems. The algorithm iteratively improves the incumbent solution until the
termination criteria are met. Short-term memory is utilized to restrict recent moves in the
neighborhood to explore better solutions and avoid entrapment in local optima, while longterm memory helps to update the neighborhood dynamically to intensification [62]. Recent
moves are added to the tabu list (TL) and restricted for a defined number of iterations.
Considering the study by Arabameri and Salmasi [18], the size of the TL is determined
according to Equation (A1).
n
(A1)
| TL| = 7 +
15
An aspiration criterion should be defined to enable a better move to be confirmed
even if it is in the tabu list. The aspiration criterion for this study is set as the objective
value of the incumbent solution. Any move that has a better objective function than the
current best solution is accepted regardless of the TL.
The TS algorithm is an incremental metaheuristic algorithm that iteratively updates
an initial solution. Arabameri and Salmasi [18] evaluated three types of initial solutioncreation mechanisms. Earliest due date (EDD) is the sequence in which the jobs are ordered
according to their due dates in ascending order. The longest tardiness/earliness rate (LTER)
rule considers the ratio of weights of earliness and tardiness, which are assumed to be
“1” in this study. A random initial solution is formed with a sequence in which jobs are
embedded in their positions randomly. Thus, two of these mechanisms are benchmarked
in this study since LTER cannot grant an initial solution where all weights are equal to
1. Four combinations of TS algorithms are TS with the EDD initial solution and insertion
neighborhood (TSEI), TS with a random initial solution and insertion neighborhood (TSRI),
TS with the EDD initial solution and swap neighborhood (TSES), and TS with a random
initial solution and swap neighborhood (TSRS). Until stopping criteria are met, a defined
number of moves are carried out at each iteration, and the best move is selected as the
new current solution if it is better than the current solution or meets the aspiration criteria.
To improve the robustness of TS solutions, n moves are compared at each iteration to
balance the tradeoff between the number of moves at each iteration and the total number
of iterations. The pseudocode of the TS algorithm is shown in Algorithm A1.

Processes 2023, 11, 454

18 of 26

Algorithm A1 Tabu Search
1: Find the initial sequence Sinit by a construction heuristic or randomly
2: Set the best sequence Sbest = Sinit
3: Set the current sequence Scurr = Sinit
4. Set tabu list TL = ∅
5: Set k max = The maximum number of iterations
6: Set k = 1
7: While (k ≤ kmax )
8: Create the set N (Scurr ) as neighbor solutions of Scurr
9: Find the best solution S in the set N (Scurr )
10:
If (S ∈
/ TL)
11:
If (OFV v(S) < v(Scurr ))
12:
Set Scurr = S
13:
Set v(Scurr ) = v(S)
14:
If (OFV v(S) < v(Sbest ))
15:
Set Sbest = S
16:
Set v(Sbest ) = v(S)
17:
Else
18:
If (OFV v(S) < v(Sbest )) (Aspiration)
19:
Set Sbest = S
20:
Set v(Sbest ) = v(S)
21:
Set Scurr = S
22:
Set v(Scurr ) = v(S)
23:
Set k = k + 1
24: Do
25: Return Sbest and vbest

Appendix A.2. Particle Swarm Optimization (PSO)
Kennedy and Eberhart [63] proposed the PSO algorithm as a social method to solve
continuous nonlinear functions. The PSO algorithm is a population-based metaheuristic
that iteratively updates its individuals. These individuals (namely, particles) represent
solution instances that move with varying velocities and directions toward better solutions.
The velocity and the direction of the particles are determined by the positions of both the
global best solution and the best solution of the particle, the previous velocity, and the
previoushdirection. Theiposition of thehi-th particle at ithe k-th iteration may be represented
k , where V k = V k , V k , · · · V k denotes its velocity.
as Pik = Pi1k , Pk2 , · · · Pin
in
i1 i2
i
i
The best position
until
the
k-th
iteration
of a particle that is called p-best may be
h
i

denoted as Bk = B1k , B2k , . . . , Bnk . The global best particle at the k-th iteration (namely, gh
i
best) is demonstrated with the notation Bk = G1k , G2k , . . . , Gnk . The particles move toward
p-best and g-best at each iteration to explore better solutions. Hence, the velocity of a
particle may be updated according to Equation (A2) at each iteration as a function of the
previous velocity, p-best, and g-best.




Vik+1 = w × Vik + c1 × rand1 × Bik − Pik + c2 × rand2 × Gik − Pik ,
(A2)
where w is the up-to-date inertia weight that arranges the impact of the previous velocity,
c1 and c2 are acceleration coefficients, and rand1 and rand2 are uniform random numbers
from the interval [0, 1]. Upon calculation of V, P may be updated according to Equation
(A3) at each iteration.
Pik+1 = Pik + Vik+1 .
(A3)
Being a powerful metaheuristic, the PSO algorithm also has drawbacks that limit
convergence to the global best solution in some conditions. Commonly, the algorithm is
trapped in local optima in high-dimensional spaces, and the rate of convergence is very low
in the iterative process [64]. Hence, many improved, hybrid, or integrated versions have

Processes 2023, 11, 454

19 of 26

been suggested by researchers. In line with the study by Arabameri and Salmasi [18], the
PSO algorithm is supported by integrating two different local search algorithms, insertion
(PSOI) and variable neighborhood structure (PSOV). The flow of the PSOI algorithm is
shown in Algorithm A2.
Algorithm A2 PSOI Local Search
1: Set the iteration number k = 1
2: Set k max = The maximum number of iterations
3: Calculate OFV v for sequence S
4: While (k ≤ kmax )
5:
Pick random integers i and j from the set [1, n]
6:
Set a new sequence S0 by executing Insert (i, j) on sequence S
7:
Calculate OFV v0 of sequence S0
8:
If (v0 < v)
9:
Set S = S0
10:
Set v = v0
11:
Set k = k + 1
12: Do
13: Return S and v

The PSOI algorithm has a simple local search strategy that iteratively collates the
solutions acquired by random moves with an insert operation and updates the incumbent
solution to check if the new sequence returns a better OFV. The PSOV algorithm constitutes
a relatively complex local search methodology. The pseudocode of the PSOV local search
methodology is summarized in Algorithm A3. PSO-VNS attempts to discover better
solutions by consulting insertion and swap operations sequentially. Upon perceiving a
better OFV, the sub-interchange operation is executed to investigate the solution space
further with the aim of improving the solution. The local search terminates after a defined
number of maximum iterations.
Algorithm A3 PSOV Local Search
1: Set the iteration number k = 1
2: Set k max = The maximum number of iterations
3: Calculate OFV v for sequence S
4: While (k ≤ kmax )
5:
Pick random integers i and j from the set [1, n]
6:
Set a new sequence S0 by executing Insert (i, j)/Swap (i, j) on sequence S
7:
Calculate OFV v0 of sequence S0
8:
If (v0 < v)
9:
Set S = S0
10:
Set v = v0
11:
Set a new sequence S0 by finding the best solution from
12:
Subinterchange on sequence S
13:
Calculate OFV v0 of sequence S0
14:
If (v0 < v)
15:
Set S = S0
16:
Set v = v0
17:
Else
18:
Set a new sequence S0 by executing Swap (i, j)/Insert (i, j)
19:
on sequence S
20:
Calculate OFV v0 of sequence S0
21:
If (v0 < v)
22:
Set S = S0
23:
Set v = v0
24:
Set k = k + 1
25: Do
26: Return S and v

Processes 2023, 11, 454

20 of 26

Appendix B
This appendix contains the results of the benchmark datasets. Table A1 shows the
results of the Reeves dataset.
Table A1. Results of Reeves dataset.
Problem

Size

Minimum

SAMT

SA

TSEI

TSES

TSRI

TSRS

PSOV

PSOI

REC01-1
REC01-2
REC01-3
REC01-4
REC01-5
REC01-6
REC01-7
REC07-1
REC07-2
REC07-3
REC07-4
REC07-5
REC07-6
REC07-7
REC13-1
REC13-2
REC13-3
REC13-4
REC13-5
REC13-6
REC13-7
REC19-1
REC19-2
REC19-3
REC19-4
REC19-5
REC19-6
REC19-7
REC25-1
REC25-2
REC25-3
REC25-4
REC25-5
REC25-6
REC25-7
REC31-1
REC31-2
REC31-3
REC31-4
REC31-5
REC31-6
REC31-7
REC37-1
REC37-2
REC37-3
REC37-4
REC37-5
REC37-6
REC37-7

20 × 5
20 × 5
20 × 5
20 × 5
20 × 5
20 × 5
20 × 5
20 × 10
20 × 10
20 × 10
20 × 10
20 × 10
20 × 10
20 × 10
20 × 15
20 × 15
20 × 15
20 × 15
20 × 15
20 × 15
20 × 15
30 × 10
30 × 10
30 × 10
30 × 10
30 × 10
30 × 10
30 × 10
30 × 15
30 × 15
30 × 15
30 × 15
30 × 15
30 × 15
30 × 15
50 × 10
50 × 10
50 × 10
50 × 10
50 × 10
50 × 10
50 × 10
75 × 20
75 × 20
75 × 20
75 × 20
75 × 20
75 × 20
75 × 20

6044
5113
3567
7412
6904
7124
12,076
7636
6690
5603
11,882
11,155
13,542
19,193
9896
9711
9468
16,141
16,733
15,970
25,294
17,490
13,630
11,977
23,013
20,592
22,911
38,065
21,567
19,609
14,718
31,156
32,517
30,218
49,750
41,984
35,382
28,949
54,628
47,261
48,125
84,550
127,794
107,509
95,511
174,195
172,490
158,079
253,315

0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00

0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.19
0.25
1.26
0.23
0.36
0.11
0.18

0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.79
0.79
1.46
1.22
1.99
1.25
0.86

0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.13
0.00
0.00
0.00
0.00
0.00
0.00
0.01
0.00
0.00
0.00
0.01
0.00
0.97
0.93
2.12
1.50
1.92
1.51
1.14

0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.86
0.86
1.36
1.20
1.45
0.83
0.77

0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.13
0.00
0.00
0.00
0.00
0.00
0.00
0.17
0.00
0.00
0.00
0.02
0.01
0.00
0.00
0.01
0.00
0.01
0.00
1.00
0.79
2.76
1.21
1.62
1.14
0.81

0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.01
0.00
0.00
0.00
0.69
0.64
1.73
0.42
0.60
0.36
0.30

0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.59
0.64
1.68
0.24
0.58
0.33
0.29

Table A2 presents the results of Taillard’s problems.

Processes 2023, 11, 454

21 of 26

Table A2. Results of Taillard dataset.
Problem

Size

Minimum

SAMT

SA

TSEI

TSES

TSRI

TSRS

PSOV

PSOI

TAI001-1
TAI001-2
TAI001-3
TAI001-4
TAI001-5
TAI001-6
TAI001-7
TAI011-1
TAI011-2
TAI011-3
TAI011-4
TAI011-5
TAI011-6
TAI011-7
TAI021-1
TAI021-2
TAI021-3
TAI021-4
TAI021-5
TAI021-6
TAI021-7
TAI031-1
TAI031-2
TAI031-3
TAI031-4
TAI031-5
TAI031-6
TAI031-7
TAI041-1
TAI041-2
TAI041-3
TAI041-4
TAI041-5
TAI041-6
TAI041-7
TAI051-1
TAI051-2
TAI051-3
TAI051-4
TAI051-5
TAI051-6
TAI051-7
TAI061-1
TAI061-2
TAI061-3
TAI061-4
TAI061-5
TAI061-6
TAI061-7
TAI071-1
TAI071-2
TAI071-3
TAI071-4
TAI071-5
TAI071-6
TAI071-7
TAI081-1
TAI081-2
TAI081-3
TAI081-4
TAI081-5
TAI081-6
TAI081-7
TAI091-1
TAI091-2
TAI091-3
TAI091-4
TAI091-5
TAI091-6
TAI091-7
TAI101-1
TAI101-2
TAI101-3
TAI101-4
TAI101-5
TAI101-6
TAI101-7
TAI111-1
TAI111-2
TAI111-3
TAI111-4
TAI111-5
TAI111-6
TAI111-7

20 × 5
20 × 5
20 × 5
20 × 5
20 × 5
20 × 5
20 × 5
20 × 10
20 × 10
20 × 10
20 × 10
20 × 10
20 × 10
20 × 10
20 × 20
20 × 20
20 × 20
20 × 20
20 × 20
20 × 20
20 × 20
50 × 5
50 × 5
50 × 5
50 × 5
50 × 5
50 × 5
50 × 5
50 × 10
50 × 10
50 × 10
50 × 10
50 × 10
50 × 10
50 × 10
50 × 20
50 × 20
50 × 20
50 × 20
50 × 20
50 × 20
50 × 20
100 × 5
100 × 5
100 × 5
100 × 5
100 × 5
100 × 5
100 × 5
100 × 10
100 × 10
100 × 10
100 × 10
100 × 10
100 × 10
100 × 10
100 × 20
100 × 20
100 × 20
100 × 20
100 × 20
100 × 20
100 × 20
200 × 10
200 × 10
200 × 10
200 × 10
200 × 10
200 × 10
200 × 10
200 × 20
200 × 20
200 × 20
200 × 20
200 × 20
200 × 20
200 × 20
500 × 20
500 × 20
500 × 20
500 × 20
500 × 20
500 × 20
500 × 20

5337
4097
2910
7118
6016
6219
11,210
8415
7553
6180
12,358
11,900
11,108
19,275
11,434
11,256
9593
19,362
19,276
21,420
31,878
29,891
24,332
15,589
31,761
26,324
17,286
53,175
43,470
35,949
26,059
55,980
51,615
50,136
86,223
69,200
58,340
51,722
92,524
95,055
89,895
140,138
129,568
99,123
66,640
134,753
111,145
88,702
210,576
167,093
126,832
94,769
200,061
177,140
164,182
306,976
237,085
215,998
186,009
313,809
300,851
310,201
442,923
629,975
491,187
375,423
737,822
650,818
579,224
1,105,327
893,397
773,905
655,942
1,124,882
1,054,993
1,000,185
1,589,543
5,577,501
4,773,182
4,037,988
6,817,377
6,535,252
6,092,434
9,449,083

0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00

0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.20
0.00
0.00
0.00
0.04
0.00
0.19
0.36
0.00
0.00
0.63
0.09
0.07
0.00
0.24
0.21
0.53
0.22
0.34
0.00
0.06
0.74
0.94
0.25
0.74
0.53
0.85
0.47
0.28
0.64
0.87
0.37
0.46
0.66
1.12
0.56
0.87
0.49
0.75
0.27
0.80
1.02
0.63
0.96
0.83
1.25
1.42
0.98
0.70
0.41
1.75
1.08
0.57
1.80
1.64
0.93
0.69
1.26
2.20
1.52
1.92
0.56
0.21

0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
1.13
0.52
0.81
0.00
0.81
0.92
0.35
0.90
0.00
0.41
1.74
0.32
1.50
0.72
0.27
0.42
0.92
0.93
1.03
1.21
0.71
0.42
1.86
4.62
1.40
3.01
1.99
0.93
0.52
0.82
0.91
1.33
1.91
1.96
1.02
1.31
1.06
1.32
1.26
1.29
2.15
1.94
2.30
2.06
3.47
1.89
1.87
3.17
2.37
1.20
2.76
2.33
2.28
3.53
1.34
1.65
1.80
2.24
3.20
2.55
2.97
1.65
1.23

0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
2.44
4.63
0.53
0.13
0.77
5.94
0.43
1.19
0.66
1.67
1.75
1.00
0.45
0.85
0.32
0.84
1.34
0.75
1.69
1.22
1.16
1.92
2.22
3.34
1.48
2.46
4.14
1.20
0.94
1.19
3.37
1.58
1.38
3.28
2.18
1.84
2.31
2.12
1.44
2.28
2.91
2.34
2.82
0.53
2.51
2.53
2.47
2.76
1.77
1.14
3.04
3.02
2.20
3.00
2.73
1.93
2.88
3.42
4.29
3.63
4.03
2.70
2.28

0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
1.37
1.37
0.00
1.10
2.70
0.75
1.14
0.55
0.10
0.00
0.45
0.46
1.69
0.97
0.22
0.97
0.50
0.43
0.54
0.13
1.01
1.63
1.21
2.04
1.97
1.21
2.27
1.13
0.71
1.24
1.32
0.96
0.82
2.05
2.50
0.82
1.84
1.61
1.42
0.73
3.03
1.94
1.78
2.13
2.68
1.88
2.15
2.55
1.88
1.19
2.58
2.56
2.03
3.24
2.40
1.70
1.84
2.29
3.24
2.54
2.97
1.66
1.25

0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
4.24
2.34
4.64
1.32
5.89
1.45
1.41
4.29
0.41
0.92
1.04
1.28
2.85
1.04
0.77
0.68
0.80
0.78
1.55
2.34
0.99
1.24
3.74
3.02
2.75
1.88
5.32
1.47
1.60
2.29
2.30
1.58
1.09
2.92
3.59
1.57
1.53
3.60
2.16
2.46
3.07
2.51
3.19
1.11
2.06
2.74
2.24
2.92
1.31
0.94
3.39
2.42
2.24
3.67
3.92
2.11
4.07
4.53
5.45
4.71
5.30
4.02
3.47

0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.35
0.80
0.00
0.61
0.00
0.41
0.73
0.22
0.31
0.80
0.03
0.08
0.00
0.33
0.29
0.72
0.32
0.30
0.58
0.15
0.83
1.14
0.78
1.35
0.87
1.34
0.74
0.36
0.58
0.49
0.87
0.94
0.74
0.92
0.49
1.24
0.89
0.82
0.48
1.54
1.08
1.37
1.30
1.76
2.07
1.62
1.87
1.32
0.80
1.95
1.62
1.23
2.64
2.47
1.28
1.62
2.21
3.20
2.55
2.93
1.60
1.22

0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.73
0.44
1.81
0.00
0.00
0.00
0.26
0.42
0.61
0.00
0.52
0.09
0.46
0.00
0.23
0.39
0.82
0.29
0.49
0.87
0.50
0.37
1.05
1.62
1.52
0.78
0.53
0.71
0.35
0.94
0.94
0.77
0.62
0.99
1.10
0.97
1.30
1.21
1.23
0.88
1.13
1.15
1.26
1.54
2.13
1.75
1.87
1.76
1.27
1.14
2.35
1.52
1.26
2.36
2.77
1.34
1.64
2.23
3.17
2.54
2.95
1.62
1.23

Processes 2023, 11, 454

22 of 26

Appendix C
The appendix contains the results of the post hoc analysis.
Table A3. Tukey’s HSD results for algorithm × group for Group 2 considering PG.
Algorithm

Group

Algorithm

Group

Difference

Lower

Upper

P Adj

PSOV
SA
SAMT
TSEI
TSES
TSRI
TSRS
SA
SAMT
TSEI
TSES
TSRI
TSRS
SAMT
TSEI
TSES
TSRI
TSRS
TSEI
TSES
TSRI
TSRS
TSES
TSRI
TSRS
TSRI
TSRS
TSRS

2
2
2
2
2
2
2
2
2
2
2
2
2
2
2
2
2
2
2
2
2
2
2
2
2
2
2
2

PSOI
PSOI
PSOI
PSOI
PSOI
PSOI
PSOI
PSOV
PSOV
PSOV
PSOV
PSOV
PSOV
SA
SA
SA
SA
SA
SAMT
SAMT
SAMT
SAMT
TSEI
TSEI
TSEI
TSES
TSES
TSRI

2
2
2
2
2
2
2
2
2
2
2
2
2
2
2
2
2
2
2
2
2
2
2
2
2
2
2
2

−0.0168
−0.0831
−0.1462
0.1173
0.2931
0.1148
0.4113
−0.0663
−0.1294
0.1342
0.3100
0.1317
0.4281
−0.0631
0.2005
0.3763
0.1980
0.4944
0.2635
0.4393
0.2610
0.5575
0.1758
−0.0025
0.2939
−0.1783
0.1181
0.2964

−0.3354
−0.4017
−0.4648
−0.2013
−0.0254
−0.2038
0.0927
−0.3849
−0.4480
−0.1844
−0.0086
−0.1869
0.1095
−0.3817
−0.1181
0.0577
−0.1206
0.1758
−0.0551
0.1207
−0.0576
0.2389
−0.1428
−0.3211
−0.0247
−0.4969
−0.2005
−0.0222

0.3018
0.2355
0.1724
0.4359
0.6117
0.4334
0.7299
0.2523
0.1892
0.4527
0.6286
0.4503
0.7467
0.2555
0.5190
0.6949
0.5166
0.8130
0.5821
0.7579
0.5796
0.8761
0.4944
0.3161
0.6125
0.1403
0.4367
0.6150

1.0000
1.0000
0.9935
0.9998
0.1221
0.9998
0.0007
1.0000
0.9989
0.9980
0.0687
0.9985
0.0003
1.0000
0.8193
0.0042
0.8358
0.0000
0.2864
0.0001
0.3047
0.0000
0.9434
1.0000
0.1190
0.9349
0.9997
0.1097

Table A4. Tukey’s HSD results for algorithm × group for Group 3 considering PG.
Algorithm

Group

Algorithm

Group

Difference

Lower

Upper

P Adj

PSOV
SA
SAMT
TSEI
TSES
TSRI
TSRS
SA
SAMT
TSEI
TSES
TSRI
TSRS
SAMT
TSEI
TSES
TSRI
TSRS
TSEI
TSES

3
3
3
3
3
3
3
3
3
3
3
3
3
3
3
3
3
3
3
3

PSOI
PSOI
PSOI
PSOI
PSOI
PSOI
PSOI
PSOV
PSOV
PSOV
PSOV
PSOV
PSOV
SA
SA
SA
SA
SA
SAMT
SAMT

3
3
3
3
3
3
3
3
3
3
3
3
3
3
3
3
3
3
3
3

−0.0644
−0.5441
−1.4248
0.5017
0.9945
0.4557
1.6113
−0.4796
−1.3603
0.5661
1.0589
0.5201
1.6757
−0.8807
1.0457
1.5385
0.9998
2.1554
1.9264
2.4192

−0.5334
−1.0130
−1.8937
0.0327
0.5255
−0.0133
1.1424
−0.9486
−1.8293
0.0971
0.5899
0.0512
1.2068
−1.3496
0.5768
1.0696
0.5308
1.6864
1.4575
1.9502

0.4045
−0.0751
−0.9558
0.9706
1.4634
0.9247
2.0803
−0.0107
−0.8914
1.0351
1.5278
0.9891
2.1447
−0.4117
1.5147
2.0075
1.4687
2.6244
2.3954
2.8882

1.0000
0.0057
0.0000
0.0206
0.0000
0.0697
0.0000
0.0378
0.0000
0.0028
0.0000
0.0120
0.0000
0.0000
0.0000
0.0000
0.0000
0.0000
0.0000
0.0000

Processes 2023, 11, 454

23 of 26

Table A4. Cont.
Algorithm

Group

Algorithm

Group

Difference

Lower

Upper

P Adj

TSRI
TSRS
TSES
TSRI
TSRS
TSRI
TSRS
TSRS

3
3
3
3
3
3
3
3

SAMT
SAMT
TSEI
TSEI
TSEI
TSES
TSES
TSRI

3
3
3
3
3
3
3
3

1.8805
3.0361
0.4928
−0.0460
1.1097
−0.5388
0.6169
1.1556

1.4115
2.5671
0.0238
−0.5149
0.6407
−1.0077
0.1479
0.6867

2.3494
3.5050
0.9618
0.4230
1.5786
−0.0698
1.0858
1.6246

0.0000
0.0000
0.0264
1.0000
0.0000
0.0067
0.0005
0.0000

Table A5. Scheffe method’s significant results for algorithm × group for GP.
Algorithm

Group

Algorithm

Group

Difference

Lower

Upper

P Adj

TSRS
SAMT
TSES
TSRS
SAMT
TSES
TSRS
SAMT
TSEI
TSES
TSRI
TSRS
TSEI
TSES
TSRI
TSRS
TSRS
TSRS

2
3
3
3
3
3
3
3
3
3
3
3
3
3
3
3
3
3

SAMT
PSOI
PSOI
PSOI
PSOV
PSOV
PSOV
SA
SA
SA
SA
SA
SAMT
SAMT
SAMT
SAMT
TSEI
TSRI

2
3
3
3
3
3
3
3
3
3
3
3
3
3
3
3
3
3

0.5575
−1.4248
0.9945
1.6113
−1.3603
1.0589
1.6757
−0.8807
1.0457
1.5385
0.9998
2.1554
1.9264
2.4192
1.8805
3.0361
1.1097
1.1556

0.0377
−2.1898
0.2294
0.8463
−2.1253
0.2939
0.9107
−1.6457
0.2807
0.7735
0.2348
1.3904
1.1614
1.6542
1.1154
2.2711
0.3446
0.3906

1.0772
−0.6597
1.7595
2.3763
−0.5953
1.8239
2.4408
−0.1157
1.8107
2.3035
1.7648
2.9204
2.6914
3.1842
2.6455
3.8011
1.8747
1.9206

0.0139
0.0000
0.0001
0.0000
0.0000
0.0000
0.0000
0.0026
0.0000
0.0000
0.0000
0.0000
0.0000
0.0000
0.0000
0.0000
0.0000
0.0000

Table A6. Tukey’s HSD results for algorithm × job considering time to find the best OFV.
Algorithm

Jobs

Algorithm

Jobs

Difference

SAMT
TSRI
TSRS
SAMT
TSRI
TSRS
SAMT
TSRI
SAMT
SAMT
SAMT
SAMT
TSEI
TSES
TSRI
SAMT

50
50
50
50
50
50
50
50
75
75
75
100
100
100
100
100

PSOI
PSOI
PSOI
PSOV
PSOV
PSOV
SA
SA
PSOI
PSOV
SA
PSOI
PSOI
PSOI
PSOI
PSOV

50
50
50
50
50
50
50
50
75
75
75
100
100
100
100
100

−54.4286
−49.5000
−40.2500
−54.7500
−49.8214
−40.5714
−40.6429
−35.7143
−80.0000
−77.7143
−72.0000
−89.9048
−55.5714
−49.0000
−50.0476
−90.5238

Lower

Upper

P Adj

−89.8820
−84.9534
−75.7034
−90.2034
−85.2748
−76.0248
−76.0963
−71.1677
−150.9068
−148.6211
−142.9068
−130.8428
−96.5095
−89.9381
−90.9857
−131.4619

−18.9752
−14.0466
−4.7966
−19.2966
−14.3680
−5.11802
−5.1895
−0.2609
−9.0932
−6.8075
−1.0932
−48.9667
−14.6334
−8.0619
−9.1095
−49.5857

0.0000
0.0000
0.0040
0.0000
0.0000
0.0033
0.0032
0.0443
0.0047
0.0089
0.0386
0.0000
0.0000
0.0011
0.0006
0.0000

Processes 2023, 11, 454

24 of 26

Table A6. Cont.
Algorithm

Jobs

Algorithm

Jobs

Difference

Lower

Upper

P Adj

TSEI
TSES
TSRI
SAMT
TSEI
TSRS
SAMT
SAMT
SAMT
TSEI
TSES
TSRI
TSRS
PSOV
SA
SAMT
TSEI
TSES
TSRI
TSRS
SAMT
SAMT
TSEI
TSES
TSRI
TSRS

100
100
100
100
100
100
200
200
200
200
200
200
200
500
500
500
500
500
500
500
500
500
500
500
500
500

PSOV
PSOV
PSOV
SA
SA
SAMT
PSOI
PSOV
SA
SAMT
SAMT
SAMT
SAMT
PSOI
PSOI
PSOI
PSOI
PSOI
PSOI
PSOI
PSOV
SA
SAMT
SAMT
SAMT
SAMT

100
100
100
100
100
100
200
200
200
200
200
200
200
500
500
500
500
500
500
500
500
500
500
500
500
500

−56.1905
−49.6190
−50.6667
−75.5238
−41.1905
61.0000
−150.0000
−143.4286
−134.9286
141.7857
128.4286
129.7857
114.0000
138.4286
133.4286
−222.7143
127.4286
115.7143
115.0000
140.5714
−361.1429
−356.1429
350.1429
338.4286
337.7143
363.2857

−97.1285
−90.5571
−91.6047
−116.4619
−82.1285
20.0619
−200.1387
−193.5673
−185.0673
91.6470
78.2899
79.6470
63.8613
67.5218
62.5218
−293.6211
56.5218
44.8075
44.0932
69.6646
−432.0497
−427.0497
279.2360
267.5218
266.8075
292.3789

−15.2524
−8.6810
−9.7286
−34.5857
−0.2524
101.9381
−99.8613
−93.2899
−84.7899
191.9244
178.5673
179.9244
164.1387
209.3354
204.3354
−151.8075
198.3354
186.6211
185.9068
211.4782
−290.2360
−285.2360
421.0497
409.3354
408.6211
434.1925

0.0000
0.0008
0.0004
0.0000
0.0451
0.0000
0.0000
0.0000
0.0000
0.0000
0.0000
0.0000
0.0000
0.0000
0.0000
0.0000
0.0000
0.0000
0.0000
0.0000
0.0000
0.0000
0.0000
0.0000
0.0000
0.0000

Table A7. Scheffe method’s significant results for algorithm × job considering time to find the best OFV.
Algorithm

Group

Algorithm

Group

Difference

Lower

Upper

P Adj

SAMT
SAMT
SAMT
TSEI
SAMT
SAMT
SAMT
TSEI
TSES
TSRI
TSRS

200
200
200
200
500
500
500
500
500
500
500

PSOI
PSOV
SA
SAMT
PSOI
PSOV
SA
SAMT
SAMT
SAMT
SAMT

200
200
200
200
500
500
500
500
500
500
500

−150.0000
−143.4286
−134.9286
141.7857
−222.7143
−361.1429
−356.1429
350.1429
338.4286
337.7143
363.2857

−284.9514
−278.3799
−269.8799
6.8343
−413.5643
−551.9929
−546.9929
159.2928
147.5785
146.8642
172.4357

−15.0486
−8.4772
0.0228
276.7371
−31.8642
−170.2928
−165.2928
540.9929
529.2786
528.5643
554.1358

0.0005
0.0048
0.0503
0.0080
0.0000
0.0000
0.0000
0.0000
0.0000
0.0000
0.0000

References
1.
2.
3.
4.
5.
6.
7.
8.

Pinedo, M. Scheduling; Springer: New York, NY, USA, 2012; Volume 29.
Miyata, H.H.; Nagano, M.S.; Gupta, J.N. Integrating preventive maintenance activities to the no-wait flow shop scheduling
problem with dependent-sequence setup times and makespan minimization. Comput. Ind. Eng. 2019, 135, 79–104. [CrossRef]
Emmons, H.; Vairaktarakis, G. Flow Shop Scheduling: Theoretical Results, Algorithms, and Applications; Springer Science & Business
Media: New York, NY, USA, 2012; Volume 182.
Graham, R.L.; Lawler, E.L.; Lenstra, J.K.; Kan, A.H.G.R. Optimization and approximation in deterministic sequencing and
scheduling: A survey. Ann. Discret. Math. 1979, 5, 287–326.
Giaro, K. NP-hardness of compact scheduling in simplified open and flow shops. Eur. J. Oper. Res. 2001, 130, 90–98.
Allahverdi, A. A survey of scheduling problems with no-wait in process. Eur. J. Oper. Res. 2016, 255, 665–686. [CrossRef]
Aldowaisan, T.; Allahverdi, A. Minimizing total tardiness in no-wait flowshops. Found. Comput. Decis. Sci. 2012, 37, 149–162.
[CrossRef]
Liu, G.; Song, S.; Wu, C. Some heuristics for no-wait flowshops with total tardiness criterion. Comput. Oper. Res. 2013, 40, 521–525.
[CrossRef]

Processes 2023, 11, 454

9.
10.
11.
12.
13.
14.
15.
16.
17.
18.
19.
20.
21.

22.
23.

24.
25.
26.
27.
28.
29.
30.
31.
32.
33.
34.
35.
36.
37.
38.
39.

25 of 26

Ding, J.; Song, S.; Zhang, R.; Gupta, J.N.; Wu, C. Accelerated methods for total tardiness minimisation in no-wait flowshops. Int. J.
Prod. Res. 2015, 53, 1002–1018. [CrossRef]
Javadi, B.; Saidi-Mehrabad, M.; Haji, A.; Mahdavi, I.; Jolai, F.; Mahdavi-Amiri, N. No-wait flow shop scheduling using fuzzy
multi-objective linear programming. J. Frankl. Inst. 2008, 345, 452–467.
Tavakkoli-Moghaddam, R.; Rahimi-Vahed, A.R.; Mirzaei, A.H. Solving a multi-objective no-wait flow shop scheduling problem
with an immune algorithm. Int. J. Adv. Manuf. Technol. 2008, 36, 969–981. [CrossRef]
Abdollahpour, S.; Rezaian, J. Two new meta-heuristics for no-wait flexible flow shop scheduling problem with capacitated
machines, mixed make-to-order and make-to-stock policy. Soft Comput. 2017, 21, 3147–3165. [CrossRef]
Gao, F.; Liu, M.; Wang, J.-J.; Lu, Y.-Y. No-wait two-machine permutation flow shop scheduling problem with learning effect,
common due date and controllable job processing times. Int. J. Prod. Res. 2018, 56, 2361–2369. [CrossRef]
Li, Z.; Zhong, R.Y.; Barenji, A.V.; Liu, J.J.; Yu, C.X.; Huang, G.Q. Bi-objective hybrid flow shop scheduling with common due date.
Oper. Res. 2021, 21, 1153–1178. [CrossRef]
Lv, D.-Y.; Wang, J.-B. Study on resource-dependent no-wait flow shop scheduling with different due-window assignment and
learning effects. Asia-Pac. J. Oper. Res. 2021, 38, 2150008. [CrossRef]
Allali, K.; Aqil, S.; Belabid, J. Distributed no-wait flow shop problem with sequence dependent setup time: Optimization of
makespan and maximum tardiness. Simul. Model. Pr. Theory 2022, 116, 102455. [CrossRef]
Huang, R.-H.; Yang, C.-L.; Liu, S.-C. No-wait flexible flow shop scheduling with due windows. Math. Probl. Eng. 2015,
2015, 456719. [CrossRef]
Arabameri, S.; Salmasi, N. Minimization of weighted earliness and tardiness for no-wait sequence-dependent setup times
flowshop scheduling problem. Comput. Ind. Eng. 2013, 64, 902–916. [CrossRef]
Schaller, J.; Valente, J.M. Minimizing total earliness and tardiness in a nowait flow shop. Int. J. Prod. Econ. 2020, 224, 107542.
[CrossRef]
Schaller, J.; Valente, J.M.S. Scheduling in a no-wait flow shop to minimise total earliness and tardiness with additional idle time
allowed. Int. J. Prod. Res. 2022, 60, 5488–5504. [CrossRef]
Guevara-Guevara, A.F.; Gómez-Fuentes, V.; Posos-Rodríguez, L.J.; Remolina-Gómez, N.; González-Neira, E.M. Earliness/tardiness minimization in a no-wait flow shop with sequence-dependent setup times. J. Proj. Manag. 2022, 7, 177–190.
[CrossRef]
Zhu, N.; Zhao, F.; Wang, L.; Ding, R.; Xu, T.; Jonrinaldi. A discrete learning fruit fly algorithm based on knowledge for the
distributed no-wait flow shop scheduling with due windows. Expert Syst. Appl. 2022, 198, 116921. [CrossRef]
Qian, B.; Zhang, Z.-Q.; Hu, R.; Jin, H.-P.; Yang, J.-B. A Matrix-Cube-Based Estimation of Distribution Algorithm for No-Wait
Flow-Shop Scheduling With Sequence-Dependent Setup Times and Release Times. IEEE Trans. Syst. Man. Cybern. Syst.
2022, 1–12. [CrossRef]
Ingber, L. Simulated annealing: Practice versus theory. Math. Comput. Model. 1993, 18, 29–57. [CrossRef]
Greening, D.R. Simulated Annealing with Errors. Ph.D. Thesis, UCLA, California, LA, USA, 1995.
Szu, H.; Hartley, R. Fast simulated annealing. Phys. Lett. A 1987, 122, 157–162. [CrossRef]
Ingber, L. Very fast simulated re-annealing. Math. Comput. Model. 1989, 12, 967–973. [CrossRef]
Malek, M.; Guruswamy, M.; Pandya, M.; Owens, H. Serial and parallel simulated annealing and tabu search algorithms for the
traveling salesman problem. Ann. Oper. Res. 1989, 21, 59–84. [CrossRef]
Yao, X. A new simulated annealing algorithm. Int. J. Comput. Math. 1995, 56, 161–168. [CrossRef]
Roussel-Ragot, P.; Dreyfus, G. A problem independent parallel implementation of simulated annealing: Models and experiments.
IEEE Trans. Comput. Des. Integr. Circuits Syst. 1990, 9, 827–835. [CrossRef]
Mahfoud, S.W.; Goldberg, D.E. Parallel Recombinative simulated annealing: A genetic algorithm. Parallel Comput. 1995, 21, 1–28.
[CrossRef]
Lee, S.-Y.; Lee, K.G. Synchronous and asynchronous parallel simulated annealing with multiple Markov chains. IEEE Trans.
Parallel Distrib. Syst. 1996, 7, 993–1008.
Wodecki, M.; Bożzejko, W. Solving the flow shop problem by parallel simulated annealing. In International Conference on Parallel
Processing and Applied Mathematics; Springer: Berlin/Heidelberg, Germany, 2001; pp. 236–244.
Bożejko, W.; Wodecki, M. The new concepts in parallel simulated annealing method. In International Conference on Artificial
Intelligence and Soft Computing; Springer: Berlin/Heidelberg, Germany, 2004; pp. 853–859.
Czapiński, M. Parallel simulated annealing with genetic enhancement for flowshop problem with Csum. Comput. Ind. Eng. 2010,
59, 778–785. [CrossRef]
Ferreiro, A.M.; García, J.A.; López-Salas, J.G.; Vázquez, C. An efficient implementation of parallel simulated annealing algorithm
in GPUs. J. Glob. Optim. 2013, 57, 863–890. [CrossRef]
Sonuc, E.; Sen, B.; Bayir, S. A parallel approach for solving 0/1 knapsack problem using simulated annealing algorithm on CUDA
platform. Int. J. Comput. Sci. Inf. Secur. 2016, 14, 1096.
Richie, J.E.; Ababei, C. Optimization of patch antennas via multithreaded simulated annealing based design exploration. J.
Comput. Des. Eng. 2017, 4, 249–255. [CrossRef]
Turan, H.H.; Kosanoglu, F.; Atmış, M. A multi-skilled workforce optimisation in maintenance logistics networks by multi-thread
simulated annealing algorithms. Int. J. Prod. Res. 2021, 59, 2624–2646. [CrossRef]

Processes 2023, 11, 454

40.
41.

42.
43.
44.
45.
46.
47.
48.
49.
50.
51.
52.
53.
54.
55.
56.
57.
58.
59.
60.
61.
62.
63.
64.

26 of 26

Vousden, M.; Bragg, G.M.; Brown, A.D. Asynchronous simulated annealing on the placement problem: A beneficial race condition.
J. Parallel Distrib. Comput. 2022, 169, 242–251. [CrossRef]
Zhou, X.; Ling, M.; Lin, Q.; Tang, S.; Wu, J.; Hu, H. Effectiveness Analysis of Multiple Initial States Simulated Annealing
Algorithm, A Case Study on the Molecular Docking Tool AutoDock Vina. Available online: https://ssrn.com/abstract=4120348
(accessed on 19 December 2022).
Coll, N.; Fort, M.; Saus, M. Coverage area maximization with parallel simulated annealing. Expert Syst. Appl. 2022, 202, 117185.
[CrossRef]
Yildirim, G. A novel hybrid multi-thread metaheuristic approach for fake news detection in social media. Appl. Intell. 2022, 1–21.
[CrossRef]
Deng, W.; Xu, J.; Song, Y.; Zhao, H. Differential evolution algorithm with wavelet basis function and optimal mutation strategy
for complex optimization problem. Appl. Soft Comput. 2021, 100, 106724. [CrossRef]
Cai, X.; Zhao, H.; Shang, S.; Zhou, Y.; Deng, W.; Chen, H.; Deng, W. An improved quantum-inspired cooperative co-evolution
algorithm with muli-strategy and its application. Expert Syst. Appl. 2021, 171, 114629. [CrossRef]
Valente, J.M.; Alves, R.A. Beam search algorithms for the early/tardy scheduling problem with release dates. J. Manuf. Syst. 2005,
24, 35–46. [CrossRef]
Röck, H. The three-machine no-wait flow shop is NP-complete. J. ACM 1984, 31, 336–345. [CrossRef]
Kirkpatrick, S.; Gelatt, C.D.; Vecchi, M.P. Optimization by simulated annealing. Science 1983, 220, 671–680. [CrossRef] [PubMed]
Van Laarhoven, P.J.; Aarts, E.H. Simulated annealing. In Simulated Annealing: Theory and Applications; Springer: Dordrecht, The
Netherlands, 1987; pp. 7–15.
Nikolaev, A.G.; Jacobson, S.H. Simulated annealing. In Handbook of Metaheuristics; Springer: Boston, MA, USA, 2010; pp. 1–39.
Bagherlou, H.; Ghaffari, A. A routing protocol for vehicular ad hoc networks using simulated annealing algorithm and neural
networks. J. Supercomput. 2018, 74, 2528–2552. [CrossRef]
Carlier, J. Ordonnancements à contraintes disjonctives. RAIRO Oper. Res. 1978, 12, 333–350. [CrossRef]
Reeves, C.R. A genetic algorithm for flowshop sequencing. Comput. Oper. Res. 1995, 22, 5–13. [CrossRef]
Amar, A.D.; Gupta, J.N.D. Simulated versus real life data in testing the efficiency of scheduling algorithms. IIE Trans. 1986, 18,
16–25. [CrossRef]
Rinnooy Kan, A.H. Machine Scheduling Problems: Classification, Complexity, and Computations. Ph.D. Thesis, University of
Amsterdam, Amsterdam, The Netherlands, 1976.
Taillard, E. Benchmarks for basic scheduling problems. Eur. J. Oper. Res. 1993, 64, 278–285. [CrossRef]
LaTorre, A.; Molina, D.; Osaba, E.; Poyatos, J.; Del Ser, J.; Herrera, F. A prescription of methodological guidelines for comparing
bio-inspired optimization algorithms. Swarm Evol. Comput. 2021, 67, 100973. [CrossRef]
Hutter, F.; Hoos, H.H.; Leyton-Brown, K.; Stuetzle, T. ParamILS: An automatic algorithm configuration framework. J. Artif. Intell.
Res. 2009, 36, 267–306. [CrossRef]
Lee, S.; Lee, D.K. What is the proper way to apply the multiple comparison test? Korean J. Anesthesiol. 2018, 71, 353–360. [CrossRef]
Glover, F. Future paths for integer programming and links to artificial intelligence. Comput. Oper. Res. 1986, 13, 533–549.
[CrossRef]
Glover, F.; Taillard, E.; de Werra, D. A user’s guide to tabu search. Ann. Oper. Res. 1993, 41, 1–28. [CrossRef]
Glover, F.; Laguna, M. Tabu search. In Handbook of Combinatorial Optimization; Springer: Boston, MA, USA, 1988; pp. 2093–2229.
Kennedy, J.; Eberhart, R. Particle swarm optimization. In Proceedings of the ICNN’95-international Conference on Neural
Networks, Perth, WA, Australia, 27 November–1 December 1995; Volume 4, pp. 1942–1948.
Li, M.; Du, W.; Nian, F. An adaptive particle swarm optimization algorithm based on directed weighted complex network. Math.
Probl. Eng. 2014, 2014, 434972. [CrossRef]

Disclaimer/Publisher’s Note: The statements, opinions and data contained in all publications are solely those of the individual
author(s) and contributor(s) and not of MDPI and/or the editor(s). MDPI and/or the editor(s) disclaim responsibility for any injury to
people or property resulting from any ideas, methods, instructions or products referred to in the content.

