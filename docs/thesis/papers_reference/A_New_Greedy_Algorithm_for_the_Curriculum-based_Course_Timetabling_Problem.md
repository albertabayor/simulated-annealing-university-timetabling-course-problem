Düzce Üniversitesi Bilim ve Teknoloji Dergisi, … (2022) …

Düzce Üniversitesi
Bilim ve Teknoloji Dergisi
Araştırma Makalesi

Müfredat Tabanlı Ders Çizelgeleme Problemi
için Yeni Bir Açgözlü Algoritma
Batuhan COŞAR a,

Bilge SAY b ,

Tansel DÖKEROĞLU c,*

a

Bilgisayar Mühendisliği Bölümü, Mühendislik Fakültesi, Atılım Üniversitesi, Ankara
Yazılım Mühendisliği Bölümü, Mühendislik Fakültesi, Atılım Üniversitesi, Ankara
c
Yazılım Mühendisliği Bölümü, Mühendislik Fakültesi, Çankaya Üniversitesi, Ankara
* Sorumlu yazarın e-posta adresi: tdokeroglu@cankaya.edu.tr
b

ÖZ
Bu çalışma, iyi bilinen Müfredat Tabanlı Ders Çizelgeleme Problemini optimize etmek için yeni bir açgözlü
algoritmayı açıklamaktadır. Açgözlü algoritmalar, en iyi çözümü bulmak için yürütülmesi uzun zaman alan kaba
kuvvet ve evrimsel algoritmalara iyi bir alternatiftir. Birçok açgözlü algoritmanın yaptığı gibi tek bir buluşsal
yöntem kullanmak yerine, aynı problem örneğine 120 yeni buluşsal yöntem tanımlıyor ve uyguluyoruz. Dersleri
müsait odalara atamak için, önerilen açgözlü algoritmamız En Büyük-İlk, En Küçük-İlk, En Uygun, Önce
Ortalama Ağırlık ve En Yüksek Kullanılamaz ders-ilk buluşsal yöntemlerini kullanır. İkinci Uluslararası Zaman
Çizelgesi Yarışması'nın (ITC-2007) kıyaslama setinden 21 problem örneği üzerinde kapsamlı deneyler
gerçekleştirilir. Önemli ölçüde azaltılmış yumuşak kısıtlama değerlerine sahip 18 problem için, önerilen açgözlü
algoritma sıfır sabit kısıtlama ihlali (uygulanabilir çözümler) rapor edebilir. Önerilen algoritma, performans
açısından son teknoloji ürünü açgözlü buluşsal yöntemleri geride bırakıyor.
Anahtar Kelimeler: Ders zaman çizelgesi oluşturma, Açgözlü algoritmalar, buluşsal yöntemler, eniyileme

A New Greedy Algorithm
for the Curriculum-based Course Timetabling Problem
ABSTRACT
This study describes a novel greedy algorithm for optimizing the well-known Curriculum-Based Course
Timetabling (CB-CTT) problem. Greedy algorithms are a good alternative to brute-force and evolutionary
algorithms, which take a long time to execute in order to find the best solution. Rather than employing a single
heuristic, as many greedy algorithms do, we define and apply 120 new heuristics to the same problem instance.
To assign courses to available rooms, our proposed greedy algorithm employs the Largest-First, Smallest-First,
Best-Fit, Average-weight first, and Highest Unavailable course-first heuristics. Extensive experiments are carried
out on 21 problem instances from the benchmark set of the Second International Timetabling Competition (ITC2007). For 18 problems with significantly reduced soft-constraint values, the proposed greedy algorithm can report
zero hard constraint violations (feasible solutions). The proposed algorithm outperforms state-of-the-art greedy
heuristics in terms of performance.
Keywords: Course-timetabling, Greedy algorithms, heuristics, optimization

Geliş: …/…/2022, Düzeltme: …/…/2022, Kabul: …/…/2022

I. INTRODUCTION
The course timetabling problem is a well-known optimization problem. Satisfying constraints such as
curriculum compactness, matching classroom size with the number of students, minimizing the
number of used classrooms, minimizing the distance between classrooms and many other such
constraints are some criteria that must be optimized [1]. The Course Timetabling problem has Rooms
and Instructors as resources that must be allocated together simultaneously and placed to schedule an
hour of a course [2]. Greedy algorithms are efficient polynomial-time approaches that work with
heuristics to solve a hard problem. G greedy algorithms often do not provide optimal solutions [3].
However, they are still promising enough to generate approximate solutions in reasonable amounts of
time [4].
This study presents a new greedy algorithm (Greedy-CB-CTT) for optimising the Curriculum-Based
Course Timetabling (CB-CTT) problem. Periods assigned to all courses in the same curriculum must be
distinct as the same student cannot be in two different classrooms on the same day period. The CB-CTT
algorithms try to find the best weekly assignment of university lectures to classrooms and day periods
[5]. The main goal of this study is to minimize the total number of soft constraint violations while
preserving the 28 satisfaction of hard constraints. Since the problem is NP-Hard and large instances of
the problem cannot be solved optimally in practical times, the greedy algorithms are good alternatives
to brute-force and evolutionary algorithms that spend hours of execution times to discover optimal or
best achievable solutions. Instead of using a single heuristic, we simultaneously define and evaluate 120
heuristics on the same problem instance and report the overall best solution [6]. Because according to
the No Free Lunch Theorem (NFL) there cannot be a single heuristic that will give the best results for
all problems [7].
Our proposed greedy algorithm (Greedy-CB-CTT) sorts the courses using Largest-Course-First,
Smallest-Course-First, and Average-Course-First [8], for the number of students enrolled in a course
[9]. Other parameters for ordering courses are the number of unavailable hours, the number of courses
in a curriculum, the number of lecture hours, and the minimum working days. The second set of ordering
heuristics is the availability of the rooms. Their capacity can be ordered according to four criteria:
largest, smallest, average-size and best-fit, matching the number of students enrolled in the course being
assigned to a classroom. To evaluate the performance of our proposed algorithm, we carried out
experiments on 21 problem instances from the Second International Timetabling Competition (ITC2007) benchmark set [10]. The results verify that the proposed greedy algorithms can report feasible
solutions (i.e., zero hard constraint violations) with significantly reduced soft-constraint values.
The main contributions of this article are as follows: 120 new heuristics are proposed to solve the CBCTT problem. Popular task and page ordering heuristics are combined in the Greedy-CB-CTT
algorithms to select the results of the best heuristic according to the behaviour of the problem instances.
Average course size and average room-size first heuristics are applied to the CB-CTT problem for the
first time, and the results are reported. It was possible to obtain better results than classical
largest/smallest first greedy heuristic algorithms, yielding solutions giving significantly lower hard and
soft constraint violations. In 18 of the 21 problem instances of the ITC-2007 benchmark set, hard
constraint violations are reduced to zero in a few milliseconds during the experiments.
In section 2, related studies for state-of-the-art algorithms are presented. The formal problem definition
is given in section 3. The details of heuristics and the proposed algorithm are introduced in section 4.
The experimental setup obtained results and comparison with state-of-the-art algorithms are reported in
section 5. Concluding remarks and future work are provided in section 6 of the study.

II. RELATED WORK
P.I.Tillet presented the results of the feasibility of determining an optimal assignment of lecturers to
courses using an operations research model in 1975 [11]. It was one of the first applications in this area.
Recent surveys about the university course timetabling problems give detailed information about the
operations research techniques, metaheuristics and other intelligent novel methods for the CB-CTT [12–
15]. MirHassani et al. analyze the primary considerations of recent papers on the university course
timetabling problems and introduce the hard and soft constraints and most currently used objective
functions [16]. Bettinelli et al. give a good classification of problem types in this domain: Examination
Timetabling, Post-Enrollment-based Course Timetabling, and Curriculum-Based Course Timetabling,
the latter being the focus of our study [5]. Initial approaches focused on linear and integer programming
models [17–19], recent variants of which still provide promising results as methods, reducing the
number of integer variables [20] or using minimal perturbation models to minimize the effects of dealing
with the resolution of infeasible parts [21].
Geiger presents local search algorithms for the International Timetabling Competition 2007 (ITC 2007)
[22]. His heuristics are based on threshold acceptance, dealing with local optima by a deterministic
acceptance of inferior solutions. A stochastic search 1 of neighbors is developed by removing some
lecture assignments and reassigning them to new day-period slots randomly. Zhipeng & Jin-Kao develop
an Adaptive Tabu Search algorithm for the CB-CTT problem [23]. Their Tabu Search algorithm
integrates features such as original double Kempe chains (a method used in the study of graph coloring
problems [24]) neighbourhood structure, a penalty-guided perturbation operator and an adaptive search
mechanism. Gulcu & Akkan develop two multi-objective Simulated Annealing (SA) algorithms to
identify a good Pareto front (the best solution set concerning the objective function) defined by the
solution quality (penalty associated with soft-constraint violations) and a robustness measure [25].
Akkan et al. work on a bi-criteria optimisation problem model and solve the CB-CTT problem using a
hybrid Multi-objective Genetic Algorithm (GA), which uses Hill Climbing and SA algorithms [26].
Thepphakorn et al. develop a Particle Swarm Optimization (PSO) timetabling application to solve realworld datasets [27]. The results verify that the algorithm has a faster convergence speed than classical
GA. Goh et al. combine different local search algorithms into an iterative two-stage procedure, Tabu
Search with Sampling and Perturbation and an improved variant of SA; their reported results are
competitive to best-known solutions reported in the literature [28]. Bagger et al. apply Benders’
decomposition to the solution of the problem to generate cuts that connect the schedule and room
allocation [29]. Combining Great Deluge and Tabu Search, iterative local search algorithms combined
with SA are among the different methods that have been evaluated [30].
Coster et al. prepared an analysis of the CB-CTT instances [31]. They investigated machine learning
methods to automate algorithm selection. They showed how problem space analysis and algorithm
selection cooperate. Akkan et al. formulated the problem as a bi-criteria optimization problem [32]. A
multi-objective simulated annealing algorithm and a surrogate measure are used to calculate the fitness
values. Experiments showed that when the proposed algorithm uses a multi-start approach, it provides
the best Pareto optimal solutions. Colajanni & Daniele formulated a completely new model that satisfies
the planning constraints and the compactness of the curricula [33]. The preferences of the teachers, the
minimum number of working days, maximum capacity, and stability of the classrooms are considered
during the study.

III. PROBLEM DEFINITION
The CB-CTT problem is in the class of NP-hard problems. It includes allocating courses, lectures and
students to a fixed set of time slots and rooms [12]. This problem must obey hard and soft constraints
while performing the allocation of resources. Soft constraints are better satisfied to increase students'
and instructors' quality and satisfaction levels using these timetables [34–36]. Due to its exponential
growth behaviour, the scheduling cannot be solved in polynomial time. The main goal of algorithms is
to minimize the penalties of constraints [12, 35].









HC1 Each lecture of a course must be scheduled in a distinct time period and a room.
HC2: Any two lectures cannot be assigned in the same time period and in the same room.
HC3: an instructor can teach only one course at a given time period, and also, the lectures of
courses in the same curriculum are assumed to be attended by the same set of students.
Therefore, two courses in the same curriculum cannot be scheduled for the same period.
HC4: If the lecturer of a course is listed as not available for a given period, then no lectures of
the same teacher can be assigned to that period.
SC1: The number of students registered to a course cannot be greater than the capacity of the
classroom where the lecture is assigned. The penalty calculated for a room smaller than the
number of registered students is given by the formula (RoomSize - NumberOfStudents) × 2.
SC2: To make it easier for students to remember in which classroom meets, it is preferred to
assign all lectures of a course to the same room.
SC3: To allow students to attend at least part of a course’s weekly meetings, it is preferred not
to schedule all of the course hours to the same day and distribute its lectures to a minimum
number of days.
SC4: If possible, a student’s courses are preferred to be on the same day and closely distributed
within the same day. For example, if in a given curriculum, there is one lecture not adjacent to
any other lecture in the same curriculum on the same day, a violation is counted.

We can define the CB-CTT problem in terms of N courses C = c1, c2 ,..., cN all of which must be
scheduled in a set of P periods T =t1, t2,..., tP , and a set of M rooms, R =r1, r2 ,..., rM . Each course ci
contains li lectures that must be scheduled to time periods. A time period is a pair of weekday (D days,
typically Monday through Friday) and a timeslot (P periods 1 consisting of D days and H daily timeslots
(means P = D × H ). Also, there are S curricula, CR = Cr1, Cr2,...,CrS where each curriculum Crk is a
group of courses that are assumed to share the same students. Typically these curricula will contain must
courses of a university department (I : day of week, J : time period of the day, K: Group of students,
L: Lecturers, M : Courses, N : Classrooms).
All lecture hours of a given course must be on a different time period. For any given (day, time, course).
Any two lectures cannot be assigned in the same period and to meet in the same room. For the day I,
and time period J, classroom N, the sum of all Xi,j,k,l,m,n (day i , time j , curriculum k , course m, classroom
n) for a certain (day, time, classroom) must be zero or one. An instructor can teach only one course at a
given time period, and also, the lectures of courses in the same curriculum are assumed to be attended
by the same set of students. Therefore, any two courses in the same curriculum cannot be scheduled to
the same time (day, period). Lecturer, L, for a given day I, and time period, J, can be assigned to teach
at most once. The variable Xi,j,k,l,m,n (day i, time j, curriculum k, lecturer l, course m, classroom n) can
have only two values 0 or 1, meaning a lecturer is assigned to teach that course on that day period or
not. The summation below for any given Lecturer must be zero or one. Two courses in the same
curriculum cannot be scheduled to the same time period. For given curriculum K, the day I, and time J,
the below summation must be zero or one. If the lecturer of a course (Lecturer L) is not available at a
given period (day I, time J), then no lectures of that lecturer can be assigned to that period.

IV. PROPOSED HEURISTICS
Our study develops several heuristics to satisfy the hard and soft constraints. It will be very practical to
have several heuristics that can provide solutions satisfying the constraints. Special algorithms reducing
soft constraint violations can also be developed separately and can perform small modifications on the
resulting timetables where all hard constraints have been eliminated. The proposed Greedy Heuristics
are defined in terms of classroom sizes and course sizes [37] as in Tables 1 and 2.

A. COURSE ORDERING HEURISTICS
Highest unavailable hours first heuristic: A high number of unavailable hours listed for a course makes
it very difficult to find a suitable time period for that course. For this reason, one of the course ordering
heuristics sorts courses in non-increasing order of their unavailable hours. Therefore, scheduling such
courses won’t conflict with any other course in the same curriculum becomes easier. The largest,
smallest, and average course first: As the names imply in these course ordering heuristics, the number
of students registered to courses is used to decide which courses are assigned to a classroom first. By
assigning courses that will have a larger impact on the resulting timetables first, there will be no need to
change these first decisions because of conflicts with less important courses (in terms of the number of
registered students). The first course assigned to a classroom can be chosen as the largest size, the
smallest size, or the closest to the average size courses. This is achieved by sorting courses in terms of
course sizes and choosing the first, the last, or the median course in the sorted list. The chosen course is
removed from the list of courses, and the process is repeated until all of the courses are assigned to a
classroom.

B. ROOM ORDERING HEURISTICS
In this heuristic, the classrooms are assigned to courses by considering their student capacities. The bestfit, the worst-fit (the largest classroom size), and average size, which is the median size classroom among
all of the available classrooms, sorted in order of classroom sizes are used. The Classroom-Heuristics
are combined with Course-Heuristics that determine the course to be assigned to that classroom. Finally,
a timetable is decided by choosing an available day-time period in that classroom. Since there are four
possible ordering choices for Classrooms and ten orders for choosing a Course, there are potentially 40
greedy heuristics that must be investigated to select the one(s) that give the best-expected results. Tables
1 and 2 provide the names of the heuristics used in our proposed algorithm and their ids.
Table 1. Course ordering heuristics.
Id
1
2
3
4
5
6
7
8
9
10

Heuristic Description
Course with most students first
Course with average number of students first
Course with least number of students
Course with highest number of unavailable day/periods
Course with most number of hours first, if equal then largest unavailable hours
Course with most number of unavailable hours first, if equal more students
Course in curricula with most courses first, next courses with more students
Course in curricula with most unavailable hours first, next more students
Courses with highest number of lecture hours
Course with highest number of minimum working days, if equal more lecture hours

Table 2. Room ordering heuristics
Id
1
2
3
4

Room ordering heuristics
Largest Room First
Smallest Room First
Average Room First
Best Fitting (with enough capacity) Room

C. THE PROPOSED GREEDY ALGORITHM (GREEDY-CB-CTT)
The Greedy-CB-CTT algorithm uses the heuristics given above. Nrooms , Ncourses , and Ncurriculum
depict the number of available classrooms, number of courses to be scheduled, and number of curricula
with a set of courses, respectively. They are the input data of the algorithm. The output of the algorithm
is the list of courses assigned to the classrooms. Mainly, the algorithm works with two main nested loops
of rooms and the courses. The ordering heuristics of the classrooms and courses are selected with 40
different methods because four classroom and ten-course ordering alternatives exist. Inside these two
loops, available classrooms are selected according to the minimum hard and soft violation values of the
assignment choices. We define 120 new heuristics. Ten course ordering heuristics combined with four
room ordering heuristics makes a total of 40 distinct heuristics. Each of these 40 heuristics is used in
three higher-level heuristics, Heur-1, Heur-2, and Heur-3, which use different techniques to group
lectures of courses into minimum working days and curricula.The pseudocode of the Greedy-CB-CTT
is given in Algorithm 2.

Algorithm 1: AssignDayPeriod(RID,CID,LH) Pseudocode for finding a (Day, Period) for given Course and
Room

The AssignDayPeriod 1 Algorithm 1 function uses the given Room and Course identifiers to determine
a suitable (Day,Period) to schedule a lecture that doesn’t violate any of the hard constraints. It is used
in all of the heuristic Algorithms 2-4 as it is a shared functionality. MAXPERIOD is the number of
lecture slots available on all days, which is six or seven for COMP benchmark but can be defined by
problem instance as a dynamic parameter. Algorithm 2 is a naive method that assigns lectures of a course
to the first available (Day,Period) slot without attempting to divide lectures of a course to minimum
working days. Since the restriction for minimum working days is not enforced, this heuristic must find
feasible solutions more easily and acts as a lower bound. Algorithm 3 is intelligent that first decides how
to divide the total lecture hours of a course into the designated minimum working days for that course.
Then, it calls the AssignDayPeriod to assign lectures of a course to a particular day. Since minimum
working days is a soft constraint, the solutions returned by this algorithm will have lower penalty scores
compared to Algorithm 2.
Algorithm 2: Pseudocode of the proposed HEUR-1 Greedy Algorithm

Algorithm 3: Pseudocode of the proposed MinWorkingDays HEUR-2 Greedy Algorithm

Algorithm 4: Pseudocode of the proposed Curriculum-first based HEUR-3 Greedy Algorithm

Algorithm 4 exploits the Curriculum-based structure of the CB-CTT model. Another important soft
constraint that must be minimized in CB-CTT benchmark instances is to ensure that the lectures of
courses belonging to the same Curriculum must be scheduled on the same day, and if possible, the
lectures of all courses in the same curriculum must be scheduled consecutively. Since this heuristic
schedules courses in the same curriculum in a bundle, it attempts to find a day with enough free hours
and can accommodate all of the lectures of the same Curriculum courses assigned to that day. Of course,
the total lecture hours of Curriculum courses assigned to a single day must be at most MAXPERIOD,
which is the maximum available lecture slots on a single day.
In this part, we explain the theoretical complexity analysis of our proposed algorithms. The results can
be achieved in a very short time for all of the 21 benchmark problem instances used in ITC-2007. The
proposed algorithm is greedy and its best advantage is that it produces reasonable solutions in
polynomial times. The steps of our heuristics are given below. NC is the number of Courses and NR is
the number of Rooms.
Step 1: Sort Courses according to heuristic course order: O(Nlog N) where N is the number of courses.
Step 2: Sort Rooms according to heuristic room order: O(Nlog N), where N is the number of rooms.
Step 3: for each Course
Step 4: for each Room
Step 5: find (day, period) such that all hard constraints are satisfied: O(1) × O(1)
Steps 1 and 2 are executed in O(N logN) because they require sorting. Steps 3, 4, 5 are O(NC × NR ×
NDays × NPeriods) since each course is considered once, and for each Course each Room is again
considered only once, and NDays × NPeriods is also a constant value. Verifying hard constraints is
O(1) because they involve a simple hash array lookup. The overall time complexity becomes:
O(NClogNC) + O(NRlogNR) + O(NC × NR) × O(1). The running time of our heuristics are equivalent
to sorting algorithms where problem size is defined by the larger number of courses (NC) and the number
of rooms (NR). However, if NC and NR are comparable in size, then the third term O(NCxNR) becomes
O(N2).

V. THE EVALUATION OF EXPERIMENTAL RESULTS
We compare our algorithm with three classical greedy algorithms. Although our algorithm is not in the
class of evolutionary algorithms, we provide a detailed comparison of our study with state-of-the-art
evolutionary algorithms. The results of the evolutionary algorithms are better than our algorithm.
However, since most evolutionary algorithms start with a population generated with greedy algorithms,
we believe our algorithm can be effectively used in this area and significantly improve the convergence
speed of the population-based algorithms. The validator of the competition committee of the ITC-2007
is used to verify our results [10]. Python programming language is used. The PC has eight GB of memory
and an I7 2.4 GHz processor.
The total sum of hard and soft constraints is considered when comparing the proposed heuristics. The
heuristic that outputs the minimum total sum is selected as the best-performing heuristic, whereas the
largest total sum is the worst solution.

A. THE BENCHMARK PROBLEM INSTANCES
The details of the benchmark problem instances used in our experiments are given in Table 3 [10]. The
range of the data provided in the columns is 30 to 121 for #courses, 5 to 20 #rooms, 5 to 6 #days, 5 to 6
#periods_per_day, #curricula varying from 13 to 150. It is called #constraints (the number of unavailable
periods where a given course cannot be scheduled), ranging from 53 to 1368. comp01 is one of the
easiest problem instances with the smallest number of courses, 30, only six classrooms, 14 curricula,
and just 53 unavailable periods in the problem set. Two of the hardest problem instances are comp10
and comp12, which have 115 and 88 courses, 67 and 150 curricula, 18 and 11 rooms, 694 and 1368
constraints, respectively.
We give the average results of our proposed heuristics (Heur-1, Heur-2, Heur-3) in Table 4. Heur-1
obtained the maximum number of feasible solutions (6.2). The total sum of Heur-2 is the minimum
(84238.1). The worst solutions are generally reported by Heur-3. The execution time of each heuristic
is reported to be not more than a few milliseconds during the experiments.
Table 5 reports the best results and the algorithms that have obtained the best result. We obtained a
feasible solution (the total sum of the hard constraints is zero) for 18 of 21 benchmark problem instances.
The overall hard constraint value is observed to be 0.19 for 21 problem instances. We obtained one or
two hard constraint violations for the problem instances that we have not reported any zero hard violation
values. The total sum of hard and soft constraints is 867.62 and 867.81, respectively. Heur-1 were the
best heuristic, with eight reported best results.
We present the solution of three classical greedy algorithms commonly used in the literature. Our main
goal was to outperform these heuristics. The algorithms are the largest course to the largest room first,
1 the smallest course to the smallest room first, and the best-fit greedy algorithms. Table 6 gives the
results of the largest course to the largest room first greedy algorithm. In Table 7, we give the results of
the smallest course to the smallest room first greedy algorithm. Table 8 presents the result of the bestfit greedy algorithm that assigns the courses to the rooms with minimum empty spaces. No solution has
been found among these three algorithms with zero hard violations. It can be observed that the largest
course to largest room first algorithm is the one that reports the best solutions in average. This algorithm
reports a total point of 713.4 for 21 problem instances. The smallest course to the smallest room first
algorithm is the worst among the three algorithms, with the highest 3390.4 points. When a comparison
is made with the algorithms we have developed, it can be seen that the performance of our algorithm is
much better, with a general average score of 867.1 and the ability to find feasible solutions for 18
problem instances. The execution time of each algorithm was not more than ten milliseconds during the
experiments.

Table 3. The details of the ITC-2007 benchmark problem instances.
problem
comp01
comp02
comp03
comp04
comp05
comp06
comp07
comp08
comp09
comp10
comp11
comp12
comp13
comp14
comp15
comp16
comp17
comp18
comp19
comp20
comp21

name

#courses

#rooms

#days

#periods/day

#curricula

#constraints

Fis0506-1
Ing0203-2
Ing0304-1
Ing0405-3
Let0405-1
Ing0506-1
Ing0607-2
Ing0607-3
Ing0304-3
Ing0405-2
Fis0506-2
Let0506-2
Ing0506-3
Ing0708-1
Ing0203-1
Ing0607-1
Ing0405-1
Let0304-1
Ing0203-3
Ing0506-2
Ing0304-2

30
82
72
79
54
108
131
86
76
115
30
88
82
85
72
108
99
47
74
121
94

6
16
16
18
9
18
20
18
18
18
5
11
19
17
16
20
17
9
16
19
18

5
5
5
5
6
5
5
5
5
5
5
6
5
5
5
5
5
6
5
5
5

6
5
5
5
6
5
5
5
5
5
9
6
5
5
5
5
5
6
5
5
5

14
70
68
57
139
70
77
61
75
67
13
150
66
60
68
71
70
52
66
78
78

53
513
382
396
771
632
667
478
405
694
94
1368
468
486
382
518
548
594
475
691
463

Table 4. The average results obtained with Heur-1, Heur-2, and Heur-3 for 21 problem instances.
ALG

Total Hard

Total Soft

Total Sum

Feasible Found

Min at

Max at

Heur-1

94.7

86471.4

86566.1

6.2

0.2

0.0

Heur-2
Heur-3

165.9
114.9

84072.2
86759.6

84238.1
86874.5

4.0
5.4

0.4
0.1

0.0
0.5

Table 5. The best results and the algorithms that report the solutions.
problem
comp01
comp02
comp03
comp04
comp05
comp06
comp07
comp08
comp09
comp10
comp11
comp12
comp13
comp14
comp15
comp16
comp17
comp18
comp19
comp20
comp21
Avg

ALG

Total Hard

Total Soft

Total Penalty

Heur-1: 1/5
Heur-2: 4/8
Heur-3: 4/1
Heur-2: 4/7
Heur-1: 4/8
Heur-3: 4/4
Heur-1: 1/1
Heur-3: 4/5
Heur-2: 1/5
Heur-3: 4/1
Heur-1: 4/3
Heur-2: 4/8
Heur-3: 4/3
Heur-2: 4/7
Heur-3: 4/1
Heur-1: 4/1
Heur-1: 1/8
Heur-2: 4/5
Heur-3: 4/4
Heur-1: 4/7
Heur-1: 1/6

0
2
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
1
0
1
0.19

234
800
600
574
1287
838
1005
580
629
796
190
1129
612
668
600
899
2776
426
607
953
2017
867.62

234
802
600
574
1287
838
1005
580
629
796
190
1129
612
668
600
899
2776
426
608
953
2018
867.81

Table 6. The results of the greedy algorithm which matches the largest course, in terms of number of students, to
the largest room.
problem

HC1

HC2

HC3

HC4

SC1

SC2

SC3

SC4

Total

comp01
comp02
comp03
comp04
comp05
comp06
comp07
comp08
comp09
comp10
comp11
comp12
comp13
comp14
comp15
comp16
comp17
comp18
comp19
comp20
comp21
total
Avg

0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0

30
96
56
58
47
105
144
52
86
117
18
55
56
90
56
105
82
31
101
98
86
1569
74.7

13
64
59
44
65
82
84
71
60
67
8
97
61
82
59
70
81
44
82
86
38
1317
62.7

0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0

4
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
4
0.2

285
635
570
515
405
785
900
555
585
795
260
555
540
675
570
775
725
425
595
850
665
12665
603.1

20
74
76
92
230
114
178
74
56
122
12
244
84
94
76
110
108
48
96
146
106
2160
102.9

3
11
6
10
3
9
15
7
6
11
2
4
6
7
6
10
8
1
9
9
9
152
7.2

312
720
652
617
638
908
1093
636
647
928
274
803
630
776
652
895
84
474
700
1005
780
14981
713.4

Table 7. The results of the greedy algorithm which matches the smallest course to the smallest room first.
problem

HC1

HC2

HC3

HC4

SC1

SC2

SC3

SC4

Total

comp01
comp02
comp03
comp04
comp05
comp06
comp07
comp08
comp09
comp10
comp11
comp12
comp13
comp14
comp15
comp16
comp17
comp18
comp19
comp20
comp21
total
Avg

0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0

15
101
64
62
53
102
114
63
83
126
21
52
64
83
64
112
77
17
93
125
90
1581
75.3

14
66
57
56
62
85
77
64
72
97
7
87
67
73
57
61
91
51
84
76
48
1352
64.4

0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0

483
3483
3247
5496
10412
852
344
3013
3477
204
1306
2577
6342
3098
3247
1746
349
2122
1257
2347
673
56075
2670.2

270
635
555
540
360
780
915
550
540
795
260
555
525
675
555
785
720
410
570
840
665
12500
595.2

1
124
122
64
310
144
116
86
108
98
12
224
94
92
122
116
158
56
108
166
138
2470
117.6

4
8
7
6
3
11
14
9
7
10
3
1
9
7
7
9
11
1
8
11
8
154
7.3

769
4250
3931
6106
11085
1787
1389
3658
4132
1107
1581
3357
6970
3872
3931
2656
1238
2589
1943
3364
1484
71199
3390.4

Table 8. The results of of the best-fit greedy algorithm.
problem

HC1

HC2

HC3

HC4

SC1

SC2

SC3

SC4

Total

comp01
comp02
comp03
comp04
comp05
comp06
comp07
comp08
comp09
comp10
comp11
comp12
comp13
comp14
comp15
comp16
comp17
comp18
comp19
comp20
comp21
total
Avg

2
1
1
0
0
0
1
1
0
2
0
0
0
0
1
0
3
0
2
0
0
14
0.7

26
81
70
53
67
97
167
68
62
128
35
90
78
66
70
112
101
57
92
126
140
1786
85.0

13
76
64
49
45
66
79
68
65
76
7
77
59
76
64
63
72
32
52
92
31
1226
58.4

0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0

88
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
88
4.2

300
655
555
520
430
765
895
560
540
805
270
560
530
675
555
775
725
440
595
835
675
12660
602.9

12
104
78
80
186
116
162
78
94
102
0
234
70
118
78
120
126
20
74
144
136
2132
101.5

3
4
6
8
0
9
9
10
4
9
1
3
7
6
6
8
8
0
6
8
10
125
5.9

403
763
639
808
616
890
1066
648
638
916
271
979
607
799
639
903
859
460
675
987
821
15205
724.0

Table 9. Competition results of ITC-2007; the best discovered results on all the 21 competition instances (given
in boldface).
problem

Müller

Lü&Hao

Atsuta

Geiger

Clark

Batuhan

comp01
comp02
comp03
comp04
comp05
comp06
comp07
comp08
comp09
comp10
comp11
comp12
comp13
comp14
comp15
comp16
comp17
comp18
comp19
comp20
comp21

5
51
84
37
330
48
20
41
109
16
0
333
66
59
84
34
83
83
62
27
103
79.8

5
55
71
43
309
53
28
49
105
21
0
343
73
57
71
39
91
69
65
47
106
80.9

5
50
82
35
312
69
42
40
110
27
0
351
68
59
82
40
102
68
75
61
123
85.8

5
111
128
72
410
100
57
77
150
71
0
442
622
90
128
81
124
116
107
88
174
180

10
111
119
72
426
130
110
83
139
85
3
408
113
84
119
84
152
110
111
144
169
132.5

234
802
600
574
1287
838
1005
580
629
796
190
1129
612
668
600
899
2776
426
608
953
2018
916

Avg

B. COMPARISON WITH STATE-OF-THE-ART ALGORITHMS
We compare the experimental performance results of our algorithms with state-of-the-art algorithms in
the literature. Although our algorithms are not in this class of algorithms, we think these results can give
a good understanding of the recent studies about the CB-CTT problem. In Table 9, we can compare the
best-known results reported in the literature with those discovered by our algorithms. The algorithms
we compare against our solutions are obtained from recent papers [22, 23, 38–40]. The total scores of
the results on 21 problems are presented. The best schedules are given in bold digits. The best algorithms
in the literature are primarily evolutionary and require much time to converge, whereas our algorithms
spend only a few millisecond optimization time.

VI. CONCLUSION AND FUTURE WORK
We outperformed classical greedy algorithms, the largest course to the largest room first, the smallest
course to the smallest room first, and the best-fit greedy algorithms. The performance of our algorithm
is better, with a general average score of 867.80 and finding feasible solutions for all problem instances.
The most important advantage of our algorithm is that it is much faster than evolutionary approaches
and works well with even large problem instances. While the evolutionary algorithms spend hours of
computation time, our algorithm can get feasible solutions in a few milliseconds. The No Free Lunch
Theorem (NFL) [7] tells us that there will always be new ideas and approaches leading to better
optimization algorithms to solve a given problem. Instead of being forgotten in a short time, it is far
more likely that most of the currently known optimization methods have at least one niche, one area
where they are excellent. It has been experimentally shown that greedy heuristics can help eliminate
hard constraint violations in CB-CTT. These results verify that it might as well be possible to find new
greedy algorithms to eliminate at least a substantial portion of soft constraint violations. Further research
is needed to determine which greedy heuristic would perform better on a given CB-CTT problem
instance. New benchmark problem instances are also being introduced. It can be interesting to apply our
proposed algorithm to these new problem sets and observe the results, justifying our experimental
findings on different benchmark datasets.

VII. REFERENCES
[1] P. Michael, and K. Hadavi, "Scheduling: theory, algorithms and systems development," Operations
research proceedings, Berlin, 1992, pp. 35-42.
[2] W. Ruegg, A history of the university in Europe: Volume 3, universities in the nineteenth and early
twentieth centuries, vol. 3, Cambridge University Press, 2004, pp.1800-1945.
[3] D. Ronald, and V.N. Temlyakov, "Some remarks on greedy algorithms," Advances in computational
Mathematics, vol. 5, pp. 173-187, 1996.
[4] A.R. Barron, A. Cohen, W. Dahmen, RA. DeVore, “Approximation and learning by greedy
algorithms,” The annals of statistics, vol. 36, no. 1, pp. 64-94. 2008.
[5] A. Bettinelli, V. Cacchiani, R. Roberti, and P. “Toth An overview of curriculum-based course
timetabling,” Top, vol. 23, no. 2, pp. 313-349, 2015.
[6] E.K. Burke, M. Gendreau, M. Hyde, G. Kendall, G. Ochoa, E. Özcan, and R. Qu, “Hyperheuristics: A survey of the state of the art,” Journal of the Operational Research Society, vol. 64, no.
12, pp. 1695-1724. 2013.

[7] D.H. Wolpert, and W.G. Macready, “No free lunch theorems for optimization,” IEEE transactions
on evolutionary computation, vol. 1, no. 1, pp. 67-82, 1997.
[8] G. Dosa, J. Sgall, “Optimal analysis of best bin packing,” International Colloquium on Automata,
Languages, and Programming, 2014, pp.429-441.
[9] K. Fleszar, and C. Charalambous, “Average-weight-controlled bin-oriented heuristics for the onedimensional bin-packing problem,” European Journal of Operational Research, vol. 210, no. 2, pp.
176-184, 2011.
[10] G.L. Di, B. McCollum, and A. Schaerf, “The second international timetabling competition (ITC2007): Curriculum-based course timetabling (track 3),” Technical Report 1.0, Queen’s University,
Belfast, United Kingdom, 2007.
[11] P.I. Tillett, “An operations research approach to the assignment of teachers to courses,” SocioEconomic Planning Sciences, vol. 9, no. 3-4, pp. 101-104, 1975.
[12] H. Babaei, J. Karimpour, and A. Hadidi, “A survey of approaches for university course timetabling
problem,” Computers & Industrial Engineering, vol. 86, pp. 43-59, 2015.
[13] S. Abdullah, H. Turabieh, B. McCollum, and P. McMullan, “A hybrid metaheuristic approach to
the university course timetabling problem,” Journal of Heuristics, vol. 18, no. 1, pp. 1-23, 2012.
[14] I. Boussaïd, J. Lepagnot, and P. Siarry, “A survey on optimization metaheuristics,” Information
sciences, vol. 237, pp. 82-117, 2013.
[15] T. Dokeroglu, E. Sevinc, T. Kucukyilmaz, and A. Cosar, “A survey on new generation
metaheuristic algorithms,” Computers & Industrial Engineering, vol. 137, no. 106040, 2019.
[16] S.A. MirHassani, and F. Habibi, “Solution approaches to the course timetabling problem,” Artificial
Intelligence Review, vol. 39, no. 2, pp. 133-149, 2013.
[17] A. Gary, and C. Robert, “Matching Faculty to Courses,” College and University, vol. 46, pp. 8389, 1971.
[18] J.S. Dyer, and J.M. Mulvey, “An integrated optimization/information system for academic
departmental planning,” Management Science, vol. 22, no. 12, pp. 1332-1341, 1976.
[19] W. Shih, and J.A. Sullivan, “Dynamic course scheduling for college faculty via zero-one
programming,” Decision Sciences, vol. 8, no. 4, pp. 711-721, 1977.
[20] N.Christian, F. Bagger, S. Kristiansen, M. Sørensen, and T.R. Stidsen, “Flow formulations for
curriculum-based course timetabling,” Annals of Operations Research, vol. 280, no. 1, pp. 121-150,
2019.
[21] A.E. Phillips, C.G. Walker, M. Ehrgott, and D.M. Ryan, “Integer programming for minimal
perturbation problems in university course timetabling,” Annals of Operations Research, vol. 252, no.
2, pp. 283-304, 2017.
[22] M.J. Geiger, “Applying the threshold accepting metaheuristic to curriculum based course
timetabling,” Annals of Operations Research, vol. 194, no.1, pp. 189-202, 2012.
[23] Z. Lu, and J.K. Hao, “Adaptive tabu search for course timetabling,” European journal of
operational research, vol. 200, no. 1, pp. 235-244, 2010.

[24] T. Dokeroglu, and E. Sevinc, “Memetic Teaching–Learning-Based Optimization algorithms for
large graph coloring problems,” Engineering Applications of Artificial Intelligence, vol. 102, no.
104282, 2021.
[25] A. Gulcu, and C. Akkan, “Robust university course timetabling problem subject to single and
multiple disruptions,” European Journal of Operational Research, vol. 283, no. 1, pp. 630-646., 2020.
[26] C. Akkan and A. Gulcu, “A bi-criteria hybrid Genetic Algorithm with robustness objective for the
course timetabling problem,” Computers and Operations Research, vol. 90, pp. 22-32, 2018.
[27] T. Thepphakorn, and P. Pongcharoen, “Variants and parameters investigations of particle swarm
optimisation for solving course timetabling problems,” International Conference on Swarm Intelligence,
2019, pp. 177-187.
[28] S. LengGoh, G. Kendall, and N.R. Sabar, “Improved local search approaches to solve the post
enrolment course timetabling problem,” European Journal of Operational Research, vol. 261, no. 1, pp.
17-29., 2017.
[29] N.C.F. Bagger, M. Sorensen, and TR. Stidsen, “Benders’ decomposition for curriculum-based
course timetabling,” Computers and Operations Research, vol. 91, pp. 178-189, 2018.
[30] T. Song, S. Liu, X. Tang, X. Peng, and M. Chen, “An iterated local search algorithm for the
University Course Timetabling Problem,” Applied Soft Computing, vol. 68, pp. 597-608, 2018.
[31] A.De Coster, N.Musliu, A.Schaerf, J.Schoisswohl, and K.Smith-Miles, “Algorithm selection and
instance space analysis for curriculum-based course timetabling,” Journal of Scheduling, vol. 25, no 1,
pp. 35-58, 2022.
[32] C.Akkan, A.Gülcü, and Z.Kuş, “Bi-criteria simulated annealing for the curriculum-based course
timetabling problem with robustness approximation,” Journal of Scheduling, pp. 1-25, 2022.
[33] G.Colajanni, and P.Daniele, “A new model for curriculum-based university course
timetabling,” Optimization Letters, vol. 15, no 5, pp. 1601-1616., 2021.
[34] H. Asmuni, “Fuzzy methodologies for automated university timetabling solution construction and
evaluation,” Ph.D. dissertation, University of Nottingham, United Kingdom, 2008.
[35] J.H. Obit, “Developing novel meta-heuristic, hyper-heuristic and cooperative search for course
timetabling problems,” Ph.D, University of Nottingham, United Kingdom, 2010.
[36] T.A. Redl, “A study of university timetabling that blends graph coloring with the satisfaction of
various essential and preferential conditions,” Ph.D., Rice University Houston, USA, 2004.
[37] B.M. Cosar, “New greedy algorithms to optimize the curriculum-based course timetabling problem,
“ M.S thesis, Atilim University, Ankara, Turkey, 2021.
[38] T. Muller, “ITC2007 solver description: a hybrid approach,” Annals of Operations Research, vol.
172, no. 1, pp. 429-446, 2009.
[39] M. Atsuta, K. Nonobe, and T. Ibaraki, “ITC-2007 Track2: an approach using general CSP solver,”
Citeseer, 2008.
[40] M. Clark, M. Henz, and B. Love, “Quikfix—a repair-based timetable solver,” The Seventh
International Conference on the Practice and Theory of Automated Timetabling,” Citeseer, 2008.

