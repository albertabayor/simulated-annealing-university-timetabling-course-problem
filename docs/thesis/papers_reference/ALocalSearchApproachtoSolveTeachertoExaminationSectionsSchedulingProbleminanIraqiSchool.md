A Local Search Approach to Solve Teacher to Examination Sections
Scheduling Problem in an Iraqi School
Dalia Sami Jasim
Daliasami99@gmail.com

,

Abstract : assigning teachers to examination sections is a type of Proctor Assignment Problem (PAPt) that require scheduled
a timetable. assigning teachers to examination sections involves assign a teacher for each section and finally come up with
list of ( teacher-section) and list of teachers names that free of duty for same day Taking into consideration hard and soft
constraints . To solve this problem we proposed a simulated annealing local base technique. we proposed an appropriate
neighborhood structure for our problem by searching the problem space to exchange the values that make the solution far
from feasible with values that make the solution near to optimality this heuristic behavior of our neighborhood structure is
the main factors leads us an optimal solution. The performance of our approach is tested over one of biggest schools in
Babylon province , Iraq ,this school contains 43 sections versus 50 teachers . Experimental results show that our approach is
able to generate successfully the required timetable.
Keywords- timetable scheduling; simulated annealing; local search.

INTRODUCTION
The development of the personal computer in terms of
software and hardware and its entry into all institutions in
Iraq including schools, at the same time , the presence of
researchers as teachers in Iraqi schools all this made the
problems in Iraqi schools a new fields for research. One of
the nowadays problems in Iraqi schools is the increasing
number of students versus an almost fixed number of
teachers, this issue led to many problems that the staff
suffers from.
One of these problems is assigning teachers to examination
sections. What complicated the problem is the increasing
number of examination sections to fit the increasing
number of students and we have to assign a teacher to
every section. Hence, we are confronting a timetable
scheduling problem , scheduling is characterized as the

allocation of resources over time to carry out a collection of
tasks [1] and the objective is to allocate a set of entities to
a limited number of resources over time, in such a way to
meet a set of predefined schedule requirements. Our
problem belongs to Academic Scheduling Problems that
can be categorized into two different types which are either
course or exam timetabling [2].examination timetable is a
multidimensional assignment problem that educational
institutions necessity to solve orderly. They need to assign
exams to time slots in a particular interval and at the same
time assign rooms as well as invigilators to exams to satisfy
diverse and complex constraints [3]. This problem is a type
of Proctor Assignment Problem (PAPt) where a university
assigning teaching assistants to serve as a proctor in final
exams. A (PAPt) problem is an NP-hard problem [4]. Nearly
the optimization techniques have been adopted in all

1

domains to discover best solution from the feasible
solutions.
It is NP-hard to solve problems with partial information and
few assumptions. Different meta-heuristic techniques are
utilized to optimize the solution of NP-hard problems [4].
Many papers described the usage of meta-heuristics
methods to solve the Academic Scheduling Problems, in [5]
researcher formulated the problem as a mixed-integer
program with a single objective and carried out a scatter
search solution procedure. [6] Developed a hybrid genetic
algorithm (GA) solution for the initial assignment problem.
Also [7] used a mixed integer programming to formulate
the assignment problem, and to derive an optimal
assignment the researcher developed a prototype system
based on spreadsheet software.
In Iraqi schools, the exam is conducted twice a year in the
middle of the academic year for ten days and in the end of
the academic year also for ten days. Scheduling teachers to
sections are carried out by the school staff before starting
the exam in a short time to update the list of teachers to
record changes in the teaching staff. According to the
opinion of experts in this field, every day takes between
two to three hours of preparation, all this lead to timeconsuming and inaccurate scheduling.
In this paper, we propose a local search approach using
Simulated Annealing algorithm to solve teachers to
sections scheduling problem.
several researchers used Simulated Annealing to solve
timetable scheduling problem, [8] came up with an
approach includes instead of swapping two assignments as
in a standard Simulated Annealing, a series of swaps
between pairs of time slots performed heuristically. A new
structure of the neighborhood solution was proposed to
find the best neighbor. This experiment using the proposed
heuristic show that this strategy is better than existing
approaches.
the researcher in [9], Integrate the Honey Badger Algorithm
(HBA) with sand cat swarm optimization (SCSO) to address
the limitations of the HBA, thereby enhancing the quality of
the solutions. The SCSO is capable of efficiently identifying
optimal solutions.
[10] Employed a Dual-sequence Simulated Annealing
algorithm as an improvement algorithm. To control the
selection of neighborhood structures within the Dualsequence Simulated Annealing. The Round Robin (RR)
algorithm was utilized. The performance of the proposed
approach is tested over 11 benchmark datasets.
Experimental results show that this approach is able to
generate competitive results when compared with other
state-of-the-art techniques.
[11] outlines the creation of a web-based course scheduling
system that employs an advanced genetic algorithm. The
improved approach incorporates a heuristic mutation that
specifically targets the alteration of infeasible genes,

thereby enhancing the algorithm's ability to explore and
exploit solutions effectively.
[12] Applied the Simulated Annealing algorithm for the
nurse scheduling problem. The results of experiments
showed that more accurate solutions can be obtained from
Simulated Annealing algorithm. Also, applied SA offers
meaningfully better solutions in a reasonable time
compared to other methods.
In the same context, we used Simulated Annealing
algorithm to convert manually scheduling of assigning
teachers to examination sections to a computer problem
gives us an accurate result for all ten days of the exam
within 2 seconds.
Transforming manually problems into computer problem in
Iraq schools is a new step toward Exploit time and
experiences that already exist in Iraqi schools, what is
important here is the right accomplishment to these
problems in an efficient way by computer programming
and artificial intelligence tools to be a compelling reason for
this transformation.

MATERIALS AND METHODS
1. PROBLEM DESCRIPTION
In this study we examined one of biggest schools in Babylon
province, Iraq ,this school contains 43 examination
sections versus 50 teachers; we have ten days of exam
every day we have to assign a teacher to each section and
at the same time every teacher have to be out of duty for
at least one day. Finally come up with list of
(teachersection) and a list of teachers names that free of duty for
same day.
For this problem we have two type of constraint hard
constraint that is :
1- Teacher name must not appear twice in a single day.
2- Exact teacher name must not appear in the same
section for all ten days.
And we have a soft constraint that is every teacher has to
be free of duty for one day at least. An improvement in the
quality of any solution for the timetabling problem is
concerned with the minimization of soft constraint
violations, which includes the number of teachers affected
by the violations. The objective cost function is calculated
as the sum of the number of violations of the soft
constraints, in our problem it will be:
∑ (reptetion_exact_teacher_name_for_all_ten_days)<= 9.
2. META-HEURISTIC
Solving hard problems considerable a research challenge
which could not be effectively addressed by the exact or
heuristic methods. This lead to the application of meta2

heuristic or hybrid meta-heuristic approaches in the recent
past. These hybrid meta-heuristic approaches are said to be
superior in giving an optimal or at least feasible results
within a specific time period [13]. Meta-heuristic
techniques are divided into two classes:
First one is the local search based methods that deals with
a single object in one iteration .local search based
techniques are also called single solution based techniques.
In this approach, a single solution is created, and then
modified using local search. Simulated Annealing is one of
the local search based method [14]
The second one is local search with population based
search: Population-based optimization algorithms are
nature-inspired usually locate a near-optimal solution to
optimization problems. Every population-based algorithm
has the common characteristics of finding out a global
solution to the problem. A population begins with initial
solutions and gradually moves toward a better solution
area of search space based on the information of their
fitness [15].

Fig2 the example of solution structure

3. SIMULATED ANNEALING
Simulated Annealing is a local search method and was first
introduced by [16] which mimic the principles of the
metallurgy of metals boiling and cooling to achieve a fixed
crystal lattice structure with lower energy state. The
algorithm initializes by generating an initial random
solution. After that, an adjacent solution is being generated
and these two solutions will be evaluated by an objective
function. If the cost of the neighbor is lower than the cost
of the initial solution and lowers the energy of the system,
the neighbor will be accepted as an improved solution. As
for a non-improving solution, it will gradually be accepted
with a probability value given by a probability function. In
SA, the performance of the algorithm is highly dependent
on its parameters.
Well explored neighborhood gives us the chance to good
quality solutions to be obtained as demonstrated in the
works of [17].We used the Simulated Annealing algorithm
that presented in [18] and the pseudo code for the used
Simulated Annealing algorithm is illustrated in figure 1.
We use the same parameters as in [18] where the initial
temperature T0 is equal to 5000 and the final temperature
Tf is equal to 0.05. The number of iterations, NumOfIte is
set to be 10000000 at every iteration, T is decreased by a
where a is defined as:

Fig1 the pseudo code for Simulated Annealing

In the do-while loop, a neighbor is defined by exchange the
number (represent teacher) that repeated for ten times
with numbers that repeated less than 9 times. A worse
candidate solution is accepted if the randomly generated
number, Random Number, is less then e-d/T where is a
difference between the quality of the old and new solutions
(i.e. d = f(Sol*) – f(Sol)). The process continues until the
temperature T is less than the final temperature Tf.

5. SOLUTION STRUCTURE
In this paper, to generate an initial solution we follow a
strategy that leads us to satisfy hard constraint , so with
consideration of not violated the hard constraint with every
new assignment we check if it violates the hard constraint
to replace this assignment with another randomly initiate
assignment and so on until finish all the assignment matrix,
finally we will get a solution that satisfies hard constraint
and ready to put it in Simulated Annealing algorithm trying
to satisfy soft constraints and reach an optimal solution.

a = (log (T) – log (0.05)) / NumOfIte

3

We represent our solution as a two-dimensional matrix
that it is columns from 0 to nine refer to the ten days of the
exam, the rows from 0 to 42 refer to the sections and the
cells of this matrix is the teacher's ID numbers that
represented as integers from 0 to 49.

Fig3 the result of many times execution versus the

number of iteration for each implementation

Fig2 solution structure

6. FITNESS FUNCTION
The objective function considered in this paper minimizes
the number of teachers that assign to examination sections
for 10 times, because every teacher has to be out of duty
at least for one day ,we solved this issue by generating
neighborhood solution with this consideration.
In order to generate a neighborhood that trying to satisfies
the soft constraint, we presented an approach to deal with
this problem by exchanging the teacher ID that we
represent it as a numbers from 0 to 49,so if it repeated for
ten times (there is no out of duty day for this teacher ), we
explore our solution to find a teacher that repeated less
than nine times to replace it with this teacher ID that
appears for ten times ,and at same time not violated the
hard constraint, if this replacing process come up with
violated the hard constraint ,we have to find another
teacher ID to replace it with the present ID , in this way we
may reach the optimality or not , because for some
implementations we cannot find teacher ID that not
violated the hard constraint so in this way we cannot reach
a feasible solution .
7. RESULTS and DISCUSSION
We built our program step by step using JAVA language by
NetBeans IDE 8.2 Platform, we used a local search
algorithm Simulated Annealing to deal with assigning
teachers to examination sections problem, the result of
many times execution versus the number of iteration for
each implementation represented in the figure3:

The behavior of Simulated Annealing algorithm that it is
able to escape local optimum by allowing some “bad”
moves make our program reach an optimal solution for
some implementations, at same time The choice of an
appropriate neighborhood structure is crucial for the
performance of the local search algorithm and has to be
done in a specific way.
The problem key-specific choice concerns the
neighborhood function definition. The efficiency of
Simulated Annealing is highly influenced by the
neighborhood function used. In this work we proposed an
appropriate neighborhood structure in order to solve this
problem by searching the problem space to exchange the
values that make the solution far from feasible with values
that make the solution near to optimality this heuristic
behavior of our neighborhood structure is the main factor
leads us to an optimal solution. The designated program
produce a matrix that represents the solution (figure 4 give
an example of this result) .we design a function that
converts every integer value to a Corresponding text.
every column in the matrix refers to an examination day,
every row in the matrix represent an examination section
and every cell in matrix represent a teacher id, after
reading a file of all teachers names we can Match every id
to a teacher.
In this way The final step of our program is the came up
with a text file that contains a schedule for all ten days of
exam, this text file contains: sections numbers, teacher
names for every section and a list of out of duty teachers
names for every day, figure 5 shows an example of a single
day from the text file that our program come up with.
In our approach, we found an optimal solution with the
Simulated Annealing algorithm, and this solution used to
solve real life problem of assigning teachers to examination
sectors. We presented our result to the staff of the school
that responsible for preparing the schedule of the teachers
to examination sections in this school and our result
satisfies all the persons in charge and it is very practical
because of the Indiscriminate nature of the solution we can
get a different teachers list every time of execution.
4

our program came up with an optimal solution represented
via an integer matrix. Last part of our program converted
the integer solution to a text file that is ready to use in the
targeted school (as presented in figure 5), and the random
approach give us the opportunity to get different
distribution for names every execution, this consider
another positive point for this work.
Converted this problem from a manual solution that needs
a lot of efforts to a computer problem is a good leap. In the
Same context presented a good solution within 2 seconds
considered a qualitative change in Iraqi schools.
As a future work, we need to work on course timetable
scheduling for schools that take about two months to
complete it, and schedule examination timetable the mid
and final year exams.

REFERENCES

Fig4 the resulted integer matrix

CONCLUSION
This paper presented a local search algorithm for the
teachers to examination sections assignment problem. We
examined this problem on a dataset from one of the biggest
Iraqi schools, we designed a program using JAVA language
to solve this problem using Simulated Annealing algorithm,
the program start with generating a new solution that
satisfy the hard constraint then we adjust simulated
annealing parameters to increase our chance to get fast
feasible solution. In this work we adopted a sophisticated
neighborhood structure that try to meet soft Constraint,

[1] Martín-Santamaría, Raúl,López-Ibáñez, Manuel,Stützle,
Thomas, On the automatic generation of metaheuristic
algorithms for combinatorial optimization problems,
European Journal of Operational Research,vol328,2024.
[2] Sara Ceschia, Luca Di Gaspero, Andrea Schaerf,
Educational timetabling: Problems, benchmarks, and stateof-the-art results,European Journal of Operational
Research,Volume 308, Issue 1,2023.
[3] Atiyeh Modirkhorasani, Pooya Hoseinpour,
Decentralized exam timetabling: A solution for conducting
exams during pandemics,Socio-Economic Planning
Sciences,Volume 92,2024.
[4] A. Amuthan ; K. D.Thilak, Survey on Tabu Search metaheuristic optimization, Signal Processing, Communication,
Power and Embedded System (SCOPES), 2016 International
Conference on,2017.
[5] R. Martí, H. Lourenço and M. Laguna, Assigning
Proctors to Exams with Scatter Search, Operations
Research/Computer Science Interfaces Series book series
(ORCS, volume 12),2001.
[6] R. M. Awad, J. W. Chinneck , Proctor Assignment at
Carleton University, INTERFACES 28: 2 March–April (pp.
58–71), 1998.
[7] T. Koide , Mixed integer programming approach on
examination proctor assignment problem , 19th
International Conference on Knowledge Based and
Intelligent Information and Engineering Systems,2015.
[8] D. Zhang , Y. Liu , R. M’Hallah , S. C.H. Leung , A simulated
annealing with a new neighborhood structure based
algorithm for high school timetabling problems , European
Journal of Operational Research 203 550–558,2010.

5

[9] Seyyedabbasi, A., Tareq Tareq, W.Z. & Bacanin, N. An
Effective Hybrid Metaheuristic Algorithm for Solving Global
Optimization Algorithms. Multimed Tools Appl 83, 85103–
85138 (2024).
[10] S. Abdullah, K. Shaker, B. McCollum, and P. McMullan,
Dual Sequence Simulated Annealing with Round-Robin
Approach for University Course Timetabling , P. Cowling
and P. Merz (Eds.): EvoCOP LNCS 6022, pp. 1–10, 2010.
[11] Dexter Romaguera, Jenie Plender-Nabas, Junrie
Matiasa, Lea Austero, Development of a Web-based
Course Timetabling System based on an Enhanced Genetic
Algorithm, Seventh Information Systems International
Conference (ISICO 2023).
[12] H. Jafari d an N. Salmasi, Maximizing the nurses’
preferences in nurse scheduling problem: mathematical
modeling and a meta-heuristic algorithm , J Ind Eng 11:439–
458 DOI 10.1007/s40092- 015-0111-0, Int 2015 .
[13] S. Muthuraman and V. P. Venkatesan , A
Comprehensive Study on Hybrid Meta-Heuristic
Approaches Used for Solving Combinatorial Optimization

Problems , Computing and Communication Technologies
(WCCCT), World Congress on,2017 .
[14] R. Ilyas and Z. Iqbal , Study of hybrid approaches used
for university course timetable problem (UCTP) , Industrial
Electronics and Applications (ICIEA), IEEE 10th Conference
on,2015.
[15] S. Satapathy and A. Naik, Social group optimization
(SGO): a new population evolutionary optimization
technique , Complex Intell. Syst. 2:173–203 DOI
10.1007/s40747-016-0022-8 , 2016.
[16] S. Kirkpatrick , C. D. Gelatt and M. P. Vecchi,
Optimization by Simulated Annealing, Science , New Series,
Vol. 220, No. 4598. , pp. 671-680, 1983.
[17] M. M. Mafarja and Seyedali Mirjalili , Hybrid Whale
Optimization Algorithm with simulated annealing for
feature selection, Neurocomputing Volume 260, Pages
302-312, 18 October 2017.
[18] S. Abdullah and E. K. Burke , A Multi-start Very Large
Neighbourhood Search Approach with Local Search
Methods for Examination Timetabling , Conference:
Proceedings of the Sixteenth International Conference on
Automated Planning and Scheduling, ICAPS 2006, Cumbria,
UK, June 6-10, 2006.

6

