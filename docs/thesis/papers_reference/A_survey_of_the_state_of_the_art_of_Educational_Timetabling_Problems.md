A survey of the state of the art of Educational
Timetabling Problems
Jade Diane Fernandes Targino
Filgueira
Production Engineering Academic
Department
Paraná Federal University of
Technology
Ponta Grossa, Brazil
https://orcid.org/0000-0002-7510-0511

Hugo Valadares Siqueira
Production Engineering Academic
Department
Paraná Federal University of
Technology
Ponta Grossa, Brazil
https://orcid.org/0000-0002-1278-4602

Attilio Converti
Department of Civil, Chemical and
Environmental Engineering, Pole of
Chemical Engineering
University of Genoa
Genoa, Italy
https://orcid.org/0000-0003-2488-6080

Thiago Antonini Alves
Mechanical Engineering Academic
Department
Paraná Federal University of
Technology
Ponta Grossa, Brazil
https://orcid.org/0000-0003-2950-7377

Abstract— An Educational Timetabling Problem (ETP)
consists of assigning meetings or exams between teachers and
students, considering a list of hard or soft requirements. ETPs
are very challenging assignments classified as NP hard
problems. Given the complexity of the problem, this paper aims
to provide a comprehensive review of the relevant literature in
the field, identifying trends in solution techniques and
approaches. For this purpose, the Preferred Reporting Items for
Systematic Reviews and Meta-Analysis (PRISMA) protocol was
used. The search yielded 55 results; 12 articles were excluded at
the screening stage after being analyzed based on their titles and
abstracts, and 17 others were excluded after further analysis.
The remaining 26 articles were included in the research. The
analyses of solution techniques and approaches to optimize
ETPs reveal that meta-heuristic-based methods are the authors’
most popular choice. It was observed that, despite their
popularity, meta-heuristics are rarely implemented in isolation.
The analysis of the chosen initialization strategy shows that most
authors start with feasible initial solutions and develop a
mechanism to generate them, integrated with the main
algorithm.
Keywords—Educational Timetabling Problems, optimization,
solution techniques.

I.

INTRODUCTION

An Educational Timetabling Problem (ETP) consists of
assigning meetings or exams between teachers and students,
considering a list of different hard or soft requirements. Hard
constraints have to be satisfied to generate a feasible
timetable. Soft constraints are not mandatory, but if a
minimum number of violated soft requirements is obtained,
then the timetable is said to be optimal [1].
Traditionally, Educational timetabling can be classified
into university and (high) school timetabling. Problems
(HSTP). University timetabling is further divided into the
University Course Timetabling Problem (UCTP or UCTTP)
and the University Examination Timetabling Problem (UETP
or UETTP) [2]. However, new formulations are being
introduced in the literature to provide a more accurate
representation of different varieties of the problem, as

Carmelo José Albanez Bastos Filho
Polytechnic Pernambuco University
line 4: Recife, Brazil
https://orcid.org/0000-0002-0924-5341

particular rules of educational institutions worldwide make
the problem highly variable.
Although it has been studied in the literature since the
1960s, introduced by Gotlieb [3] and having a thriving
research community, with notable biannual conference series
such as Practice and Theory of Automated Timetabling
dedicated to timetabling practices and their applications [4],
the timetabling problem is still addressed by manual
scheduling procedures by a majority of universities [5].
According to Muklason et al. in [6], manual scheduling
still causes recurring problems when making a schedule.
These problems include the large amount of time invested in
it, less flexibility to sudden changes, and poor consideration
of students’ needs. Those issues indicate the need for
automation in such tasks. However, it is a very challenging
assignment classified as an NP-hard problem, which means
that the amount of computation required to find solutions
increases exponentially with problem size [7].
Given the complexity of the problem, this paper has the
main goal of providing a review of the relevant literature in
the field, searching for trends in the solution techniques and
approaches, as well as in the problem formulations. To
categorize the solution techniques found in the state of the art,
the categories selected for classification were: metaheuristics, exact optimization methods, hyper-heuristic
approaches, and matheuristic approaches.
It is also of interest in this research to analyze the
initialization strategies used by authors, separating them
according to the feasibility of the initial solutions and the kind
of mechanism used to generate them. The categories of initial
solutions identified are: unfeasible, feasible, and good
quality, and they are usually generated through a solver or
algorithm.
The main contributions of this paper are:
1. Presenting a general overview of the ETPs through
a Systematic Review of Literature;

2. Categorization of the solution techniques and
approaches selected by the authors to address ETPs,
organized in chronological order.
3. Introducing a novel categorization for the
initialization strategy based on the viability of the initial
solutions;
II.

SURVEY METHODOLOGY

This article performs a literature review on recent
approaches to the optimization of ETPs. For this purpose, the
Preferred Reporting Items for Systematic Reviews and MetaAnalysis (PRISMA) protocol was used. The search term
“Educational Timetabling Problem” was used in the IEEE
Xplore, ACM digital library, and Science Direct databases.
The following queries were used: consider only publications
from 2014 onwards. The search on August 23, 2024, yielded
55 results. All articles found were published in English,
although this was not a criterion used in the search.
After the search, all results found were analyzed through
their titles and abstracts (screened). Those that dealt with a
type of problem that did not belong to any ETP variant were
discarded, with 12 articles being excluded at this stage. The
remaining articles were retrieved and assessed for eligibility.
At this point 17, articles were excluded because of the
following criteria: systematic review of literature: 7 articles,
study of problem formulation: 7 articles, case study: 1 article,
study of algorithm selection strategy: 1 article, and
development of an application for generating automated
schedules: 1 article.
In common, all articles excluded have the fact that they
did not study an optimization strategy. The 26 remaining
articles were included in the research. Table I presents the
country of origin for each study, and the content analysis
indicates that Brazil stands out with the highest number of
contributions. Table II displays the distribution of
publications by year. The data reveal a declining trend over
time, which becomes more evident when visualized in Fig. 1.
The next section presents the previous surveys found in
the search. Section IV describes and categorizes the
approaches chosen by the authors to optimize a type of ETP.
Section V describes the initialization strategy found in each
paper and presents a new categorization based on the viability
of initial solutions.
III.

PREVIOUS SURVEYS

The search performed as described in section II returned
seven previous surveys. The references and scope of each of
them are described in Table III. We observed that the results
differ from each other and from the present research in
several aspects.
Babaei, Karimpour and Hadidi [8], Yang, Ayob, and
Nazri [9], and Abdipoor et al. [2] developed their surveys
focused on the UCTP. However, Yang, Ayob, and Nazri
utilized a practical case to study satisfaction factors for the
elaboration of a timetable, while the other two papers are
differentiated for their scopes, as Abdipoor et al. focus on
meta-heuristic approaches, and Babaei, Karimpour and
Hadidi (2015) do not make any kind of limitation.
The researches by Johnes [10] and Drake et al. [11] have
very different objectives from the others and is not even
restricted to the field of ETPs. The first lists Operational

TABLE I

COUNTRY OF ORIGIN PER PUBLICATION

Country Nº of publications
Country
Nº of publications
Australia
1
Indonesia
2
Brazil
7
United Kingdom
3
China
2
Greece
1
Egypt
1
Portugal
2
Mexico
2
Thailand
1
Tunisia
2
Malaysia
2

Research techniques to solve specific topics in education, and
the second reviews the literature on selection hyperheuristics.
Tan et al. [12] were the only authors among the survey
authors found who analyzed optimization methodologies,
specifically for HSTP.
The focus of the research by Ceschia, Di Gaspero and
Schaerf [13], as well as that of the present research, is the
general field of ETPs. However, the researches differ from
each other in the focus as we study optimization strategies
and the authors analyze problem formulations, benchmarks,
and state-of-the-art results. In addition, in the present work,
we are introducing a new categorization of initialization
strategies based on the viability of the solutions.
IV.

SOLUTION TECHNIQUES AND APPROACHES

To categorize the solution techniques found in the state of
the art, we based ourselves on the categories proposed by Tan
et al. [14]. The authors classify existing algorithms into:
mathematical optimization algorithms, meta-heuristic
algorithms, graph coloring algorithms, matheuristic
approaches, hyper-heuristic approaches, and hybrid
approaches.
Instead of using a category of mathematical optimization
algorithms, we chose the term exact optimization methods
that are not synonymous, but the latter is a category of the
former and is sufficient for the purposes of this work.
According to the results found, the categories selected for
classification were, then: metaheuristics, exact optimization
methods, hyper-heuristic approaches, and matheuristic
approaches.
Graph coloring and hybrid approaches were not
considered necessary categories since within the universe of
the analyzed studies, those that used graph coloring did so as
part of another approach. The hybrid approach defined by the
authors involves a combination of the strengths of two or
more metaheuristics. In these cases, we consider that a metaheuristic category already covers the method that uses this
type of strategy.
In the following sections, a brief description of the
solution techniques found in the state of the art will be
provided according to the category in which it is classified.
Table III summarizes the findings of this section.
TABLE II DISTRIBUTION OF PUBLICATIONS BY YEAR
Year
2014
2015
2016
2017
2018
2019
2020
2021
2022

Nº of Publications
5
5
3
4
2
1
3
2
1

TABLE III CLASSIFICATION PER FAMILIES OF METAHEURISTICS

6
5
4
3
2
1
0
2012

2014

2016

2018

2020

2022

2024

Fig. 1. Evolution of the number of publications by year

A. Metaheuristics
As the metaheuristics category had the greatest number of
occurrences, it was considered important to detail the
findings further. In order to do so, the results were then
classified according to the method employed. Table IV shows
all the methods of metaheuristics found and summarizes the
reference in which each one of them was used. The results
indicate that the most popular methods are Variable
Neighborhood Search (VNS), Iterated Local Search (ILS),
Tabu Search (TS), and Simulated Annealing (SA).
Dorneles, Araújo, and Buriol [15] combined the Fix and
optimize (F&O) method with the Variable Neighborhood
Descent (VND) meta-heuristic to compose an optimization
strategy to solve the Class-Teacher Timetabling Problem
with Compactness Requirements (CTTPCR), where each
neighborhood is formed by a decomposition type τ and a
number k. The type of decomposition varies between class,
teacher, and day, and in each case, one of these elements is
selected to have a k number of free elements to be optimized,
while the rest are fixed.
Elloumi et al. [16] demonstrated two size reduction
schemes for the classroom assignment problem, a component
of the UETP. The two procedures provide a partial solution
to the problem, and the remainder of the exams that remain
unallocated to classrooms will be handled using the VNS
meta-heuristic adapted by the authors through the proposition
of neighborhood structures and Local Search (LS) heuristics.
Fong et al. [17] created the method called Artificial Bee
Colony hybridized with Imperialist Nelder-Mead Great
Deluge. The objective of the proposed approach is to improve
the global exploration power of ABC and enhance the local
exploration capacity to adjust the search region of each
solution.
Fonseca and Santos. [18] show the application of three
variations of the VNS metaheuristic to the HSTP. The authors
define the neighborhoods used in the VNS. One of the
variations used, called skewed variable neighborhood search,
was presented by the authors of the paper through the
introduction of a relaxed solution acceptance rule through
which it becomes possible to accept a new solution that is
worse than the current solution if the distance between them
is large enough to trigger the relaxed condition.
Alves, Oliveira and Rocha Neto. [19] used the Genetic
Algorithm (GA) to solve two instances of ETPs for multiple
courses. To solve the problem, the proposed algorithm solves
the schedules of one course at a time, providing partial
solutions that change the parameters to be used by the
algorithm in solving the schedules of the next courses,

Meta-heuristic
Variable Neighborhood Descent
Variable Neighborhood Search
Artificial Bee Colony
Imperialist competitive algorithm
Great Deluge
Iterated Local Search
Genetic Algorithm
Ruin and Recreation
Particle Swarm Optimization
Cat Swarm Optimization
Threshold Acceptance Local
Late Acceptance Strategy
Tabu Search
Simulated Annealing
Cuckoo Search
Hill Climbing

Reference
[15]
[16],[17],[18],[24],[6]
[17]
[17]
[17]
[24],[27],[1],[31]
[19],[22]
[20]
[21]
[25]
[26]
[27]
[27],[6],[29],[1]
[27],[28],[1],[31]
[30]
[23]

Total
1
4
1
1
1
4
3
1
1
1
1
1
4
4
1
1

considering that the same teachers teach different courses.
The order in which the courses are selected is determined by
the complexity of the schedule, that is, courses with a greater
number of pairs (teacher, curricular component) are selected
first.
Li et al. [20] created the algorithm called Stochastic
Evolutionary Ruin and Recreate, based on the principles of
Ruin and Recreate (R&R) incorporated into evolutionary
features. Its general idea is to divide a solution into its
components and assign a score to each component through an
evaluation function that works in dynamic environments. The
scores determine the chances of the components surviving in
the current solution. Therefore, in each iteration, some
components are evaluated as not worth keeping.
TABLE IV CLASSIFICATION OF THE RESULTS ACCORDING TO THE SOLUTION
TECHNIQUE

Reference

MetaHeuristic

[15]
[16]
[17]
[18]
[34]
[35]
[19]
[20]
[21]
[22]
[38]
[36]
[23]
[37]
[24]
[25]
[26]
[27]
[28]
[6]
[29]
[1]
[30]
[31]
[32]
[33]
Total

x
x
x
x

Solution Technique
HyperMatheuristic
heuristic

Mathematical
Optimization

x
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x

20

4

1

1

Problem
CTTPCR
UETP
UCTP
HSTP
UCTP
HSTP
UCTP
UETP
MSP
UCTP
HSTP
UCTP
UCTP
UETP
HSTP
HSTP
UETP
HSTP
UETP
UCTP
UCTP
HSTP
UCTP
UCTP
UCTP
MCTP

Salem and Hassine [21] proposed a PSO-based approach
to solve the Meeting Scheduling Problem (MSP). According
to the authors, ETPs can be understood as variants of this type
of problem. The velocity operator is obtained as
demonstrated by (1):
𝑉 = 𝑐1 . (𝑝𝑏𝑒𝑠𝑡𝑖,𝑡 − 𝑝𝑟𝑒𝑠𝑒𝑛𝑡𝑖,𝑡 ) + 𝑐2 . (𝑔𝑏𝑒𝑠𝑡𝑖,𝑡 −
𝑝𝑟𝑒𝑠𝑒𝑛𝑡𝑖,𝑡 )
(1)
The difference between two particles is given by the
meetings present in one particle (with better performance)
that do not occur at the same time in the other particle (with
worse performance). To obtain a new particle 𝑋𝑖,𝑡+1 , the
result of equation 1 must be added to a particle 𝑋𝑖,𝑡 .
The procedure is done by replacing the time and/or
location of the meetings in the current position 𝑋𝑖,𝑡 with the
times/rooms of the meetings, as in the best position.
Abdelhalim and Khayat [22] used GA to develop a model
for solving a UCTP. The model introduced a new
recombination operator called “utilization crossover” that
focuses on the utilization rate of classrooms, trying to reduce
the number of under/overutilized events (with occupancy
rates lower than 75% and higher than 100%, respectively) and
increase the number of well-utilized events on a
chromosome.
Mauritsius et al. [23] developed a method for solving
ETPs based on the use of heuristics. The method has two
stages: the first is intended to construct an initial schedule that
does not necessarily need to be feasible. In this stage, two
heuristics are used: Largest Degree First (LD), Largest
Weighted Degree First (LWD), and Least Saturation Degree
First (LSD). The first is used to choose the events assigned to
the resources, and the second is used in case of a tie. In the
second stage, new LSD heuristics will be used to make the
schedule feasible.
Saviniec and Constantino [24] proposed five soft
computing algorithms to address HSTP. The main idea
behind the algorithms is the hybridization of the ILS and VNS
metaheuristics with two neighborhood operators created by
the authors to explore the structure of the problem. The two
operators are called matching (MT) and torque (TQ), and the
five algorithms are different combinations between the
metaheuristics and the use and order of the operators: ILSTQ, ILS-MT-TQ, ILS-TQ-MT, VNS-MT-TQ, and VNS-TQMT.
Skoullis, Tessapoulos and Beligiannis [25] proposed a
hybrid algorithm based on Cat Swarm Optimization (CSO)
that consists of two separate basic parts, which are executed
sequentially: The main process, which is the basic CSObased algorithm, and a local search refinement procedure,
applied right after the main process, in an attempt to improve
the quality of the resulting schedule about the number of idle
hours that each teacher has available between their teaching
hours.
Leite et al. [26] developed a cellular evolutionary
algorithm with threshold acceptance metaheuristics and local
search. The cellular evolutionary algorithm generates the
offspring population. For the local search step, the threshold
acceptance metaheuristic is used, where neighboring
individuals generated from a feasible solution are accepted as
the new current solution, even if they perform worse than the
old current solution, as long as the difference between the

performances of the two is less than a pre-established
threshold.
Saviniec, Santos and Costa [27] used parallel
metaheuristic models to propose two resolution methods for
HSTP. The first method is based on central memory and
operates as follows: a group of metaheuristics is executed
concurrently while possibly cooperating through the
exchange of current solutions made through the central
memory that maintains a set of elite solutions.
Leite, Melício and Rosa. [28] built an algorithm for
solving ETPs based on the SA metaheuristic. The method
developed is called Fast Simulated Annealing (FastSA) and
was built with the intention of producing a more efficient
version of SA, accelerating the search process by reducing
the number of solutions fitness evaluations.
Muklason, Iranti and Marom [6] applied a VNS algorithm
hybridized with TS to UCTP. The algorithm is cited by the
authors in previous works applied to solving other types of
problems and works as follows: VNS is applied, and after the
LS phase, the new solutions produced will be evaluated. If
the new solution is better than the current one, it will replace
the current solution, otherwise, it will become part of a list of
unwanted moves.
Chen et al. [29] added controlled randomization to the TS
methodology together with an acceptance threshold
mechanism, to build the tabu search method with controlled
randomization. In the method, during the search for
environments, a solution worse than the current solution X
can be accepted in a controlled manner according to a
threshold τ.
Saviniec et al. [1] resorted to column generation for the
resolution of a new extensive formulation for the HSTP. The
solution model proposed is cooperative parallel. The method
uses a team of metaheuristics to build and improve solutions,
as explained in this section in [27]. The model described
above was modified to incorporate new agents based on
column generation. These agents use partial solutions
obtained by column generation to obtain lower bounds for the
problem and extend them to complete solutions using an
original method that is based on a (F&O) heuristic.
Thepphakorn and Pongcharoen [30] developed the
Cuckoo Search (CS) metaheuristic to solve the UCTP. The
authors analyzed the success of three different strategies: a
parameter setting approach (static and adaptive), an approach
based on movement strategies (Lévy flights and Gaussian
random walk), and a hybridization approach with local search
(insertion operator and exchange operator).
Song et al. [31] proposed an LS algorithm with multiple
neighborhoods based on SA. The authors introduced six
neighborhood operators, three of which are basic and three
specific to the UCTP problem, and the union of all
neighborhoods provides the search space considered by the
algorithm. The combination of neighborhoods is done
through an innovative mechanism proposed by the authors
that promises to balance the quality of the solutions and the
computational cost of obtaining them.
Tung Ngo et al. [32] used GA to solve the UCTP. The
authors modified the method by adding a repair process that
is applied to both the initial solutions and the solutions after
going through the recombination and mutation stages to
ensure that the constraints are respected.

B. Exact Methods of Optimization
A Branch and Check algorithm for solving the Multiphase
Course Timetabling Problem (MCTP) was presented by
Esmaeilbeigi et al. [33]. The problem must first be relaxed
and then solved by a solver. Each time a feasible solution of
the relaxed formulation is obtained, it is checked whether it
is possible to convert this solution into a feasible solution for
the non-relaxed problem. If not, the infeasible solution is
removed.
Whenever an integer feasible solution of the relaxed
formulation is found, this integer solution is checked and is
only accepted as feasible if the integer solution can be
converted into a feasible solution for the non-relaxed
problem. If not, one or more violated constraints are
identified and added to remove this infeasible solution from
the relaxed formulation. As a result, any optimal solution
reported by the solver leads to an optimal feasible solution for
the MCTP.
C. Hyper-heuristics
A hyperheuristic methodology based on ILS that
combines several move operators was proposed by SoriaAlcaraz et al. [34] to solve the UCTP. The operators are lowlevel heuristics and are used within the ILS process to cause
disturbances in the current solutions and are selected through
a mechanism that takes into account a vector of probabilities
and also a score attributed to each of the heuristics according
to their performance.
Ahmed Özcan and Kheiri [35] studied and compared the
performance of 15 hyperheuristics formed by the
combinations of five selection methods and three acceptance
methods, all listed from a literature review developed by the
authors. The 15 hyperheuristics are used to select and
combine 9 low-level heuristics to address 18 instances of
HSTP.
Soria-Alcaraz et al. [36] developed a hyper-heuristic
approach combining add and delete operations within an ILS
methodology to solve UCTPs and UETP. The add and delete
operations can be used to construct a new solution from a
previously existing feasible solution, in which events will be
removed from the timetable and reinserted into other valid
periods. The adding and deleting procedure is done through a
list that keeps track of the add and delete operations
performed and their order.
Muklason et al. [37] developed an approach to solve ETPs
incorporating the concept of fairness from the students'
perspective. The model consists of three phases: In phase 1,
initial feasible solutions are constructed. In phases 2 and 3, a
hyper-heuristic selection is employed, incorporating
reinforcement learning and the GD algorithm as heuristic
selection and move acceptance components, respectively.
Fourteen low-level heuristics commonly used in the literature
for exam scheduling problems were used.
D. Matheuristics
Fonseca, Santos and Carrano [38] proposed a hybrid
method using a variant of the VNS metaheuristic and a
matheuristic to provide the refinement of the best solution
obtained by the VNS. In the matheuristic approach, a
heuristic works at a macro level, controlling LS procedures.
These local searches are integer programming models, in
which a subset of variables is fixed to the current values in

the current solution, and the remaining variables of the model
can be freely modified by the IP solver.
V.

INITIALIZATION STRATEGIES

Due to the large number of constraints in ETPs, finding
feasible initial solutions is often a challenging process. For
this reason, initialization processes are commonly addressed
in the literature. To organize the strategies found during the
analysis of the selected works, we introduced a categorization
for the process of generating initial solutions. The categories
of initial solutions identified are: unfeasible, feasible, and
good quality.
When none or only a fraction of the hard constraints are
to be taken into account during initialization or when the
procedure for constructing the initial solutions is not capable
of guaranteeing their viability, the chosen strategy is to create
unfeasible initial solutions. In this case, since there is no
mechanism to guarantee the viability of the solutions, it is
necessary to develop a step that verifies whether the solutions
have already become feasible before the algorithm meets the
termination criteria.
The strategy of creating feasible initial solutions requires
that the hard constraints be respected, but without worrying
about the soft constraints. By disregarding the soft constraints
to initialize the particles, the authors make it easier for the
algorithm to find initial solutions, which can reduce
computational time. However, since the quality of the
solutions is directly linked to the number of soft constraints
they can satisfy, this can compromise the optimality of the
final solutions.
Good quality initial solutions are generated taking into
account both soft and hard constraints. This strategy is
important since good quality initial solutions increase the
probability of directing the search to better regions of the
search space and further help in the convergence to better
solutions.
In addition, the authors still differ in their initialization
strategy regarding the way to generate the solutions; some
choose to use solvers, and others develop an initialization
mechanism within the algorithm. Table V summarizes all the
procedures described in this section.
VI. CONCLUSION
This paper presents an overview of the solutions
techniques and approaches employed in the optimization of
ETPs. The analyses of solution techniques and approaches to
optimize ETPs reveal that meta-heuristic-based methods are
the most popular choice by authors. It was observed that
despite their popularity, meta-heuristics are hardly
implemented in an isolated manner, and that it is very
common to use of auxiliary heuristics and the hybridization
between meta-heuristics. Other approaches are also
considered by authors in smaller proportions, like hyperheuristics, matheuristics, and exact methods.
Through the analysis of the results found in the literature,
new questions were brought to our consideration, like the
analysis of the initialization strategy chosen. It shows that
most authors prefer to start with feasible initial solutions and
develop a mechanism to generate them integrated with the
main algorithm. Only one author chose the strategy of starting
with initial solutions that consider both hard and soft

TABLE IV CATEGORIZATION OF THE RESULTS ACCORDING TO THE
INITIALIZATION STRATEGY

Reference
[15]
[16]
[17]
[18]
[34]
[35]
[19]
[20]
[21]
[22]
[38]
[36]
[23]
[37]
[24]
[25]
[26]
[27]
[28]
[6]
[29]
[1]
[30]
[31]
[32]
[33]

Initialization Estrategy
Unfeasible
Feasible High Quality
x
x
x
x

x
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x

Mecanismum
Algorithm
solver
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x

constraints. To start with unfeasible solutions is also a
popular choice, whether they are random solutions or
solutions that consider only a fraction of the hard constraints.
We believe that this kind of detailed analysis can be
beneficial to researchers who want to explore the
development of algorithms to optimize ETPs. For future
research, we believe that there is potential to closely look into
the optimization strategies in order to find out how authors
maintain the feasibility of the initial solutions or how they
ensure that unfeasible initial solutions become feasible before
the termination criteria are met.
REFERENCES
[1]

[2]

[3]
[4]

[5]

[6]

[7]
[8]

L. Saviniec, M. O. Santos, A. M. Costa, and L. M. R. dos Santos,
“Pattern-based models and a cooperative parallel metaheuristic for high
school timetabling problems,” Eur J Oper Res, vol. 280, no. 3, pp.
1064–1081, Feb. 2020, doi: 10.1016/j.ejor.2019.08.001.
S. Abdipoor, R. Yaakob, S. L. Goh, and S. Abdullah, “Meta-heuristic
approaches for the University Course Timetabling Problem,” Sep. 01,
2023, Elsevier B.V. doi: 10.1016/j.iswa.2023.200253.
C. C. Gotlieb, “The construction of class-teacher timetables,” in IFIP
Congress, North-Holland Publishing Company, 1962, pp. 73–77.
E. S. K. Siew, S. N. Sze, S. L. Goh, G. Kendall, N. R. Sabar, and S.
Abdullah, “A Survey of Solution Methodologies for Exam Timetabling
Problems,” IEEE Access, vol. 12, pp. 41479–41498, 2024, doi:
10.1109/ACCESS.2024.3378054.
K. Xiang, X. Hu, M. Yu, and X. Wang, “Exact and heuristic methods
for a university course scheduling problem,” Expert Syst Appl, vol. 248,
Aug. 2024, doi: 10.1016/j.eswa.2024.123383.
A. Muklason, R. G. Irianti, and A. Marom, “Automated course
timetabling optimization using tabu-variable neighborhood search
based hyper-heuristic algorithm,” in Procedia Computer Science,
Elsevier B.V., 2019, pp. 656–664. doi: 10.1016/j.procs.2019.11.169.
S. Even, “ON THE COMPLEXITY OF TIMETABLE AND MULTICOMODITY FLOW PROBLEI1S.”
H. Babaei, J. Karimpour, and A. Hadidi, “A survey of approaches for
university course timetabling problem,” Comput Ind Eng, vol. 86, pp.
43–59, 2015, doi: 10.1016/j.cie.2014.11.010.

X. F. Yang, M. Ayob, and M. Z. A. Nazri, “An investigation of
timetable satisfaction factors for a practical university course
timetabling problem,” in 2017 6th International Conference on
Electrical Engineering and Informatics (ICEEI), IEEE, Nov. 2017, pp.
1–5. doi: 10.1109/ICEEI.2017.8312409.
[10] J. Johnes, “Operational research in education,” Jun. 16, 2015, Elsevier
B.V. doi: 10.1016/j.ejor.2014.10.043.
[11] J. H. Drake, A. Kheiri, E. Özcan, and E. K. Burke, “Recent advances
in selection hyper-heuristics,” Sep. 01, 2020, Elsevier B.V. doi:
10.1016/j.ejor.2019.07.073.
[12] J. S. Tan, S. L. Goh, G. Kendall, and N. R. Sabar, “A survey of the
state-of-the-art of optimization methodologies in school timetabling
problems,” Expert Syst Appl, vol. 165, Mar. 2021, doi:
10.1016/j.eswa.2020.113943.
[13] S. Ceschia, L. Di Gaspero, and A. Schaerf, “Educational timetabling:
Problems, benchmarks, and state-of-the-art results,” Jul. 01, 2023,
Elsevier B.V. doi: 10.1016/j.ejor.2022.07.011.
[14] J. S. Tan, S. L. Goh, G. Kendall, and N. R. Sabar, “A survey of the
state-of-the-art of optimization methodologies in school timetabling
problems,” Expert Syst Appl, vol. 165, Mar. 2021, doi:
10.1016/j.eswa.2020.113943.
[15] Á. P. Dorneles, O. C. B. De Araújo, and L. S. Buriol, “A fix-andoptimize heuristic for the high school timetabling problem,” Comput
Oper Res, vol. 52, no. PART A, pp. 29–38, 2014, doi:
10.1016/j.cor.2014.06.023.
[16] A. Elloumi, H. Kamoun, B. Jarboui, and A. Dammak, “The classroom
assignment problem: Complexity, size reduction and heuristics,”
Applied Soft Computing Journal, vol. 14, no. PART C, pp. 677–686,
2014, doi: 10.1016/j.asoc.2013.09.003.
[17] C. W. Fong, H. Asmuni, B. McCollum, P. McMullan, and S. Omatu,
“A new hybrid imperialist swarm-based optimization algorithm for
university timetabling problems,” Inf Sci (N Y), vol. 283, pp. 1–21,
Nov. 2014, doi: 10.1016/j.ins.2014.05.039.
[18] G. H. G. Fonseca and H. G. Santos, “Variable Neighborhood Search
based algorithms for high school timetabling,” Comput Oper Res, vol.
52, pp. 203–208, Dec. 2014, doi: 10.1016/j.cor.2013.11.012.
[19] S. S. A. Alves, S. A. F. Oliveira, and A. R. Rocha Neto, “A Novel
Educational Timetabling Solution through Recursive Genetic
Algorithms.”
[20] J. Li, R. Bai, Y. Shen, and R. Qu, “Search with evolutionary ruin and
stochastic rebuild: A theoretic framework and a case study on exam
timetabling,” Eur J Oper Res, vol. 242, no. 3, pp. 798–806, May 2015,
doi: 10.1016/j.ejor.2014.11.002.
[21] H. Salem and A. Ben Hassine, “Meeting scheduling based on Swarm
Intelligence,” in Procedia Computer Science, Elsevier B.V., 2015, pp.
1081–1091. doi: 10.1016/j.procs.2015.08.153.
[22] E. A. Abdelhalim and G. A. El Khayat, “A Utilization-based Genetic
Algorithm for Solving the University Timetabling Problem (UGA),”
Alexandria Engineering Journal, vol. 55, no. 2, pp. 1395–1409, Jun.
2016, doi: 10.1016/j.aej.2016.02.017.
[23] T. Mauritsius, A. N. Fajar, Harisno, and P. John, “Novel Local
Searches for Finding Feasible Solutions in Educational Timetabling
Problem,” in 2017 5th International Conference on Instrumentation,
Communications, Information Technology, and Biomedical
Engineering (ICICI-BME), 2017, pp. 270–275. doi: 10.1109/ICICIBME.2017.8537723.
[24] L. Saviniec and A. A. Constantino, “Effective local search algorithms
for high school timetabling problems,” Applied Soft Computing
Journal,
vol.
60,
pp.
363–373,
Nov.
2017,
doi:
10.1016/j.asoc.2017.06.047.
[25] V. I. Skoullis, I. X. Tassopoulos, and G. N. Beligiannis, “Solving the
high school timetabling problem using a hybrid cat swarm optimization
based algorithm,” Applied Soft Computing Journal, vol. 52, pp. 277–
289, Mar. 2017, doi: 10.1016/j.asoc.2016.10.038.
[26] N. Leite, C. M. Fernandes, F. Melício, and A. C. Rosa, “A cellular
memetic algorithm for the examination timetabling problem,” Comput
Oper Res, vol. 94, pp. 118–138, Jun. 2018, doi:
10.1016/j.cor.2018.02.009.
[27] L. Saviniec, M. O. Santos, and A. M. Costa, “Parallel local search
algorithms for high school timetabling problems,” Eur J Oper Res, vol.
265, no. 1, pp. 81–98, Feb. 2018, doi: 10.1016/j.ejor.2017.07.029.
[28] N. Leite, F. Melício, and A. C. Rosa, “A fast simulated annealing
algorithm for the examination timetabling problem,” Expert Syst Appl,
vol. 122, pp. 137–151, May 2019, doi: 10.1016/j.eswa.2018.12.048.
[9]

[29] M. Chen, X. Tang, T. Song, C. Wu, S. Liu, and X. Peng, “A Tabu
search algorithm with controlled randomization for constructing
feasible university course timetables,” Comput Oper Res, vol. 123,
Nov. 2020, doi: 10.1016/j.cor.2020.105007.
[30] T. Thepphakorn and P. Pongcharoen, “Performance improvement
strategies on Cuckoo Search algorithms for solving the university
course timetabling problem,” Expert Syst Appl, vol. 161, Dec. 2020,
doi: 10.1016/j.eswa.2020.113732.
[31] T. Song, M. Chen, Y. Xu, D. Wang, X. Song, and X. Tang,
“Competition-guided multi-neighborhood local search algorithm for
the university course timetabling problem,” Appl Soft Comput, vol.
110, Oct. 2021, doi: 10.1016/j.asoc.2021.107624.
[32] S. Tung Ngo, J. Jafreezal, G. Hoang Nguyen, and A. Ngoc Bui, “A
Genetic Algorithm for Multi-Objective Optimization in Complex
Course Timetabling,” in Proceedings of the 2021 10th International
Conference on Software and Computer Applications, in ICSCA ’21.
New York, NY, USA: Association for Computing Machinery, 2021,
pp. 229–237. doi: 10.1145/3457784.3457821.
[33] R. Esmaeilbeigi, V. Mak-Hau, J. Yearwood, and V. Nguyen, “The
multiphase course timetabling problem,” Eur J Oper Res, vol. 300, no.
3, pp. 1098–1119, Aug. 2022, doi: 10.1016/j.ejor.2021.10.014.
[34] J. A. Soria-Alcaraz, G. Ochoa, J. Swan, M. Carpio, H. Puga, and E. K.
Burke, “Effective learning hyper-heuristics for the course timetabling

problem,” Eur J Oper Res, vol. 238, no. 1, pp. 77–86, Oct. 2014, doi:
10.1016/j.ejor.2014.03.046.
[35] L. N. Ahmed, E. Özcan, and A. Kheiri, “Solving high school
timetabling problems worldwide using selection hyper-heuristics,”
Expert Syst Appl, vol. 42, no. 13, pp. 5463–5471, Aug. 2015, doi:
10.1016/j.eswa.2015.02.059.
[36] J. A. Soria-Alcaraz, E. Özcan, J. Swan, G. Kendall, and M. Carpio,
“Iterated local search using an add and delete hyper-heuristic for
university course timetabling,” Applied Soft Computing Journal, vol.
40, pp. 581–593, Mar. 2016, doi: 10.1016/j.asoc.2015.11.043.
[37] A. Muklason, A. J. Parkes, E. Özcan, B. McCollum, and P. McMullan,
“Fairness in examination timetabling: Student preferences and
extended formulations,” Applied Soft Computing Journal, vol. 55, pp.
302–318, Jun. 2017, doi: 10.1016/j.asoc.2017.01.026.
[38] G. H. G. Fonseca, H. G. Santos, and E. G. Carrano, “Integrating
matheuristics and metaheuristics for timetabling,” Comput Oper Res,
vol. 74, pp. 108–117, Oct. 2016, doi: 10.1016/j.cor.2016.04.016.

