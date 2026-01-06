Pamukkale Univ Muh Bilim Derg, 30(1), 17-30, 2024

Pamukkale Üniversitesi Mühendislik Bilimleri Dergisi
Pamukkale University Journal of Engineering Sciences
A simulated annealing algorithm for the faculty-level university course
timetabling problem
Fakülte seviyesinde üniversite ders çizelgeleme problemi için bir tavlama
benzetimi algoritması
Hatice ERDOĞAN AKBULUT1*

, Feristah OZÇELİK2

, Tugba SARAÇ2

1Department of Industrial Engineering, Faculty of Engineering and Natural Sciences, Antalya Bilim University, Antalya, Turkey.

hatice.erdogan@antalya.edu.tr
2Department of Industrial Engineering, Faculty of Engineering and Architecture, Eskisehir Osmangazi University, Eskisehir, Turkey.

fdurmaz@ogu.edu.tr, tsarac@ogu.edu.tr

Received/Geliş Tarihi: 18.12.2021
Accepted/Kabul Tarihi: 23.03.2023

Revision/Düzeltme Tarihi: 15.03.2023

doi: 10.5505/pajes.2023.00483
Research Article/Araştırma Makalesi

Abstract
In this study, faculty-level university course timetabling problem with
double major and minor program constraints where classrooms are
shared with several faculties is taken into account. This is the first study
considering all these constraints together. A goal programming model
is proposed to solve the considered problem. Since it is not possible to
find a feasible solution for large-size problems with the proposed model
in a time limit, a simulated annealing algorithm is developed. The
performance of the proposed solution methods is tested by using
randomly generated test problems. In addition, a case study is
performed at the engineering faculty of a private university.
Computational results show the success of the proposed simulated
annealing algorithm to solve large-sized problems. An 83%
improvement was achieved with the proposed algorithm for the real-life
problem.

Öz
Bu çalışmada, dersliklerin fakülteler arasında paylaşıldığı, çift anadal
ve yan dal kısıtlarının olduğu fakülte seviyesinde üniversite ders
çizelgeleme problemi ele alınmıştır. Bu çalışma, tüm bu kısıtları bir
arada ele alan ilk çalışmadır. Ele alınan problemi çözmek için bir hedef
programlama modeli önerilmiştir. Önerilen model ile büyük boyutlu
problemler için süre limiti içinde uygun çözüm bulmak mümkün
olmadığından, bir tavlama benzetimi algoritması geliştirilmiştir.
Önerilen çözüm yöntemlerinin performansı rassal türetilmiş test
problemleri kullanılarak sınanmıştır. Ayrıca özel bir üniversitenin
mühendislik fakültesinde vaka çalışması yapılmıştır. Deneysel sonuçlar,
önerilen tavlama benzetimi algoritmasının büyük boyutlu problemleri
çözmedeki başarısını ortaya koymuştur. Gerçek hayat problemi için
önerilen algoritma ile %83 oranında iyileşme sağlanmıştır.

Keywords: Faculty-level university course timetabling, Simulated
annealing, Goal programming, Double major program, Minor
program.

Anahtar kelimeler: Fakülte seviyesinde üniversite ders çizelgeleme,
Tavlama benzetimi, Hedef programlama, Çift anadal programı, Yandal
programı.

1 Introduction
Scheduling is the arrangement of entities (work, people, tools,
courses, etc.) by place and time and subject to constraints to
achieve a specific goal [1]. Scheduling problems can be seen in
many areas such as manufacturing, health, and education. The
timetabling problem, which is a type of scheduling problem, is
assigning a specified number of events, such as courses, exams,
and meetings, to a limited number of periods in a way to satisfy
constraints [2]. In educational institutions, frequently
encountered timetabling problems occur with the scheduling of
courses and exams [3],[4]. Systemic imperatives, preferences of
educational institutions, students, instructors, and limited
resources such as classrooms, equipment, and instructors add
to the challenges of the educational timetabling problem.
The university course timetabling problem (UCTP) is usually
classified as curriculum-based or post-enrollment-based. The
curriculum-based course timetabling problem occurs when a
conflict arises in assigning courses to a student group
dependent on a specific curriculum. The post-enrollment-based
course timetabling problem occurs when a conflict arises in
assigning courses after registration.

*

In the literature, the course timetabling problem is considered
in different ways. In some studies, courses can be assigned to
periods or the classroom, while in other studies, the courses are
assigned to both the periods and the classroom. In cases where
it is not known formerly which instructor will teach the course,
the course is assigned to both the instructor and the period
and/or classroom.
In this study, we looked at a UCTP that is based on the
curriculum and in which courses are assigned to both times and
classrooms. The problem is the faculty-level course timetabling
problem, where classrooms are shared by various faculties. For
this reason, attention has been paid to the availability of the
classroom when assigning the courses to the classroom and
period. As it is known, all courses in the department's
curriculum must be completed in the double major program. In
the minor program, certain courses must be taken. For that
reason, when considering double major programs, it is
generally desirable not to overlap the compulsory courses of
the same semester in both programs. However, since the
number of courses required to be taken in minor programs is
less, it may be possible to avoid conflicts regardless of the
semester. In this way, an opportunity is created for minor
students to complete the program on time. By considering the

Corresponding author/Yazışılan Yazar

17

Pamukkale Univ Muh Bilim Derg, 30(1), 17-30, 2024
H. Erdoğan Akbulut, F. Ozçelik, T. Saraç
constraints of the double major and minor programs together,
it is hoped that a more suitable course timetable will be
developed for both student groups. This study was motivated
by the UCTP at the engineering faculty of a private university.
To address the problem, a goal programming model was
developed. Also, the simulated annealing (SA) algorithm was
proposed to solve large-sized problems. The performance of
the proposed methods was tested with randomly generated
problems and data taken from the engineering faculty of a
private university. The results obtained by both methods were
compared.
The paper is structured as follows: Section 2 presents a
literature review on the faculty-level course timetabling
problem in universities. Section 3 introduces the addressed
problem and proposes the goal programming model. Section 4
describes the developed SA algorithm. Section 5 presents the
experimental results and interpretations. Finally, Section 6
concludes and suggests future research.

2 Literature review
Detailed information on the university course timetabling
problem can be found in the literature review studies of Babaei
et al. [5] and Altunay and Eren [6]. In this section, we present
studies dealing with the faculty-level course timetabling
problem.
MirHassani [7] developed an integer programming model for
faculty-level course timetabling problem. In making coursetime assignments, MirHassani [7] aimed to minimize conflicts
by penalizing the less preferred times and the overlapping of
courses.
Ismayilova et al. [8] presented a multi-objective 0-1 integer
programming model for faculty-level course timetabling
problems that took into account the preferences of both the
administration and the faculty members.
Cura [9] proposed an SA approach for the course timetabling
problem at the Faculty of Business Administration of Istanbul
University. The study aimed to maximize the preferences of
faculty members by considering their seniority. The developed
approach consisted of two stages: searching for courses that
could be placed in the same time slot and assigning the courses
to the most appropriate time. In the study, besides the SA
approach, the problem was also solved with a genetic algorithm
and a tabu search algorithm. As a result, Cura [9] obtained
better results with SA compared to other algorithms.
Al Tarawneh and Ayob [10] developed a tabu search method
using a multi-neighborhood approach to address the course
timetabling problem in Kebangsaan Malaysia University
Engineering Faculty.
Nguyen et al. [11] proposed a new hybrid algorithm consisting
of a combination of harmony search and the bee algorithm for
the UCTP in Vietnam. The proposed approach was compared
with variable neighborhood search, tabu search, and bee
algorithms by taking fourteen datasets from the Faculty of
Information Technologies of the Ho Chi Minh City University of
Science in Vietnam.
Demir and Celik [12] addressed a curriculum-based course
timetabling problem for Atatürk University Engineering
Faculty. The integer programming technique was used for the
problem to maximize total satisfaction by considering the
preferences of the faculty members. The developed

mathematical model reached the optimal solution for the
problem with only two departments.
Abdelhalim and El Khayat [13] propose a utilization-based
genetic algorithm to maximize resource utilization. In the
study, the classroom utilization rate was defined to be used in
the objective function. This rate consists of the product of the
frequency rate, which measures how often a class is used by the
total number of hours it is available, and the occupancy rate,
which measures how full a class is relative to its total capacity.
The study's goal was to achieve classrooms with the highest
occupancy and frequency rates while minimizing other soft
constraint violations. It has been observed that unnecessary
resource use is prevented with their proposed approach.
Borchani et al. [14] addressed the course timetabling problem
of the Faculty of Economics and Administrative Sciences of the
University of Tunisia. They proposed a variable neighborhood
descent approach to solve the problem. Ertane [15] addressed
the problem of assigning courses to the day, time interval, and
classroom. The study included the constraint of not overlapping
the courses taken by successive student groups in different
departments for students doing double majors. To solve the
problem, the decomposition method is used in the study.
Ozkan [16] worked on a faculty-level UCTP for Hacettepe
University’s Faculty of Economics and Administrative Sciences
and developed an integer linear programming model and twostage heuristic algorithm to solve the problem. Thepphakorn
and Pongcharoen [17] developed the cuckoo search algorithm
and tested it on the data of an engineering faculty. The
performance of the developed algorithm was compared with
that of particle swarm optimization and hybrid particle swarm
optimization algorithms.
Alnowaini and Aljomai [18] suggest an automated system to
create faculty timetabling using a genetic algorithm and
implement the proposed system for three departments of a
faculty. The authors suggested that the developed system be
expanded to include the entire faculty in the future. Ariyazand
et al. [19] presented a multiobjective model to maximize the
desirability of professors. The Faculty of Humanities of the
Islamic Azad was selected as a case study, and five different
metaheuristics (the bat algorithm, cuckoo search, artificial bee
colony, firefly algorithm, and genetic algorithm) were used to
solve the problem.
In Table 1, the constraints, the objective functions, and the
solution methods of the reviewed studies are given.
Explanations for all of the abbreviations used in Table 1 are
given in Appendices A1, A2, A3, and B. In this study, H1, H2, H3,
H4, H6, H7, H8, H11, H12, H14, H15, H16, and H17 hard
constraints were considered. Although it is rarely discussed in
the literature, the hard constraint H6 was included in this study
because of the common use of classrooms with other faculties.
The double major program constraint was addressed by Ertane
[15] for the first time. Ertane [15] dealt with minimizing the
overlap of the courses of consecutive student groups of
different departments. In this study, considering that most of
the courses of the first-year student groups in the faculty are
common, the double major program constraint is handled to
minimize the overlap of the compulsory courses of the same
student groups in the different departments. Also, we
considered the minor program constraint, and all these
constraints were considered together for the first time for the
UCTP at the faculty level. Finally, the O2 objective function was
adopted in line with the literature.

18

Pamukkale Univ Muh Bilim Derg, 30(1), 17-30, 2024
H. Erdoğan Akbulut, F. Ozçelik, T. Saraç

Table 1. Constraints, objective function, and solution methods of the reviewed studies.
Study
MirHassani [7]
Ismayilova et al. [8]
Cura [9]
Al Tarawneh and Ayob [10]
Nguyen et al. [11]
Demir and Celik [12]
Abdelhalim and El Khayat
[13]
Borchani et al. [14]
Ertane [15]
Ozkan [16]
Thepphakorn and
Pongcharoen [17]
Alnowaini and Aljomai [18]
Ariyazand et al. [19]
Our study

Constraints
H1, H2, H5, H7, H8, H9, H19, H20, S2, S3, S14
H1,H3,H5
H1, H2, H3, H4, H20
H1, H2, H3, H7, H8, H12, S1, S15, S16
H1, H2, H3, H4, H6, H7, H9, H12, H13, H16, H18, S1, S3, S9,
S11, S14, S15, S16, S17
H1, H2, H3, H4, H7, H8, H11, H12, H14, S4
H1, H2, H10, H12, H14, H16, S1, S15, S16

Objective functions
O2, O6
O4, O5
O3
O2
O2

Solution methods
IP
MOP, AHP, ANP
SA
TS
HM (HS, BA)

O3
O1, O2

IP
GA

H1, H2, H3, H12, H14, S16
H2, H3, H4, H7, H18, S4, S5, S6, S7, S8,S18
H1, H2, H3, H9, H11, H12, H14, H15, H16, S4, S10, S14
H1, H2, H3, H7, H8, H11, H13, H16, S14

O2
O2,O7
O2
O1, O2

VND
ILP
ILP, TS, SA
CS

H1,H2,H3,H12,S11,S12,S14,S15,S16,S17
H1,H2,H3,H4,H11,H12,S12,S14
H1, H2, H3, H4, H6, H7, H8, H11, H12, H14, H15, H16, H17,
S1, S4, S6, S18,S19

O6
O3
O2,O7,O8

GA
BTA, CS, ABC, FA, GA
GP, SA

3 Problem definition and mathematical
model
The motivation of this study is to find a solution to the facultylevel course timetabling problem at a private university. The
considered engineering faculty consists of five departments.
Based on the curriculum at the beginning of each semester, the
departments determine the courses to be opened for all
student groups, the weekly hours of each course, and the
instructors. In addition, there are common courses given to the
same student groups in different departments. Since the
number of students who have to take these common courses
is large, the courses are divided into sections, and it is
determined which student group has to take which section.
During the term, students have both compulsory and elective
courses; these courses have a minimum of one and a maximum
of four weekly course hours. One-hour and two-hour courses
are assigned to one day, while three-hour courses are assigned
to either one session or two sessions, determined by the
instructors’ preference. Four-hour courses are assigned in two
sessions on two different days. In addition, the first and
second-year student groups of a department have only
compulsory courses. The third and fourth-year student groups
of a department have both compulsory and elective courses.
In the university, different faculties and vocational schools use
the buildings in common. While the classrooms are shared,
laboratories and studios are assigned to specified
departments or faculties. For this reason, courses are assigned
according to the availability of classrooms between 9:00 and
20:00 on weekdays. Courses are assigned to classrooms of a
suitable type and capacity. While the course timetabling is
generated, course assignments are made according to the
instructors’ availability.
In this study, a goal programming model was developed for
solving the faculty-level course timetabling problem. The
model consisted of seven goals listed below:
G1

:

G2

:

The two or more hours of courses of the student
group should not be assigned during the lunch
break,
The different two courses of the student group
should not be assigned consecutive periods
during the lunch break,

G3

:

G4

:

G5

:

G6

:

G7

:

The compulsory courses of consecutive student
groups in a department should not overlap,
The course hours of the first or second-year
student groups should not exceed certain hours
per day,
The course hours of the third or fourth-year
student groups should not exceed certain hours
per day,
No course hour conflicts for double major
program students,
No course hour conflicts for minor program
students.

Definitions of index sets, parameters, and decision variables
used in the model are given below:
Index sets
𝐶 = {𝑖, 𝑝 | 𝑖, 𝑝 = 1, … , 𝐼} Set of course indices
𝐼 = {𝑗 | 𝑗 = 1, … , 𝐽} Set of instructor indices
𝐷𝐸 = {𝑚, 𝑚′ | 𝑚, 𝑚′ = 1, … , 𝑀} Set of department indices
𝑆𝐺 = {𝑛, 𝑢 | 𝑛, 𝑢 = 1, … , 𝑁} Set of student group indices
𝐷𝐴 = {𝑙 | 𝑙 = 1, … , 𝐿} Set of day indices
𝑃 = {𝑘 | 𝑘 = 1, … , 𝐾} Set of period indices
𝐶 = {𝑞, 𝑜 |𝑞, 𝑜 = 1, … , 𝑄} Set of classroom indices
𝑆 = {𝑤 | 𝑤 = 1, … , 𝑊} Set of session indices
𝐶𝑇 = {𝑣 | 𝑣 = 1, … , 𝑉} Set of classroom-type indices
Parameters
𝑎𝑖
𝑏𝑖

:
:

ℎ𝑖
𝑔𝑞
𝑐𝑞
𝑑𝑖𝑚𝑛

:
:
:
:

𝑎𝑠𝑖𝑚

:

𝑒𝑙𝑘𝑞

:

𝑓𝑗𝑖

:

The weekly hour of course 𝑖,
The estimated number of students to take
course 𝑖,
The number of sessions for course 𝑖
The type of classroom 𝑞,
The capacity of classroom 𝑞,
1, if course 𝑖 belongs to student group 𝑛 of
department m; 0, otherwise,
1, if course 𝑖 is an elective course of department
𝑚; 0, otherwise,
1, if classroom 𝑞 is available on day 𝑙 at period 𝑘;
0, otherwise,
1, if instructor 𝑗 teaches course 𝑖; 0, otherwise,

19

Pamukkale Univ Muh Bilim Derg, 30(1), 17-30, 2024
H. Erdoğan Akbulut, F. Ozçelik, T. Saraç
𝑟𝑗𝑙

:

𝑠𝑖𝑤
𝑠𝑎𝑖𝑚

:
:

𝑘𝑘𝑖𝑣

:

𝑀𝑀
𝑇1

:
:

𝑇2

:

𝑇3

:

𝑇4

𝑇5

𝑇6
𝑇7

1, if instructor 𝑗 is available on day 𝑙; 0,
otherwise,
the hours of session 𝑤 of course 𝑖,
1, if course 𝑖 belongs to the minor program of
department 𝑚; 0, otherwise,
1, if course 𝑖 can be assigned to classroom type
𝑣; 0, otherwise,
A large enough positive number,
The target value for the goal that a maximum of
one hour of a course may overlap with the lunch
break. It is taken as 1
The target value for the goal that a maximum of
one course is allowed to overlap with the lunch
break. It is taken as 1.
The target value for the goal that the maximum
number of overlapping compulsory course
hours for consecutive student groups at a
period. It is taken as 1,
The target value for the goal that the number of
course hours per day for the first or second-year
student groups should not exceed 8 hours. It is
taken as 8,
The target value for the goal that the number of
course hours per day for third or fourth-year
student groups should not exceed 8 hours. It is
taken as 8
The target value for the goal that the maximum
number of overlapping course hours for double
major students at a period. It is taken as 1
The target value for the goal that the maximum
number of overlapping course hours for minor
students at a period. It is taken as 1.

:

:

:
:

𝑑5++
𝑚𝑛𝑙

1, if the value of 𝑑4+
𝑚𝑛𝑙 is a positive number; 0,
otherwise,
1, if the value of 𝑑5+
𝑚𝑛𝑙 is a positive number; 0,
otherwise.

:

The constraints and the objective function of the developed
mathematical model are given below:
𝐿

𝐾

∀𝑖

(1)

𝑙=1 𝑘=1 𝑞=1

𝑋𝑖𝑙(𝑘+1)𝑞 − 𝑋𝑖𝑙𝑘𝑞 − 𝑋𝑖𝑙(𝑘+2)𝑞 ≤ 0 ∀ 𝑖, 𝑙, 𝑘, 𝑞, 𝑤 | 𝑠𝑖𝑤 =
2, (𝑘 + 2) ≤ 𝐾
−𝑋𝑖𝑙(𝑘−1)𝑞 + 𝑋𝑖𝑙𝑘𝑞 − 𝑋𝑖𝑙(𝑘+1)𝑞 ≤ 0
∀ 𝑖, 𝑙, 𝑘, 𝑞, 𝑤 | 𝑠𝑖𝑤 = 3

∀ 𝑚, 𝑛, 𝑙, 𝑘

(2)

𝐼

(8)

∑ 𝑋𝑖𝑙𝑘𝑞 = 𝑦𝑖1𝑙𝑞 𝑠𝑖1

∀𝑖, 𝑙, 𝑞| ℎ𝑖 = 1

(9)

∀𝑖| ℎ𝑖 = 1

(10)

𝑘=1
𝑄

𝐿

∑ ∑ 𝑦𝑖1𝑙𝑞 = 1
𝑙=1 𝑞=1
𝐾

𝑊

∑ 𝑋𝑖𝑙𝑘𝑞 = ∑ 𝑦𝑖𝑤𝑙𝑞 𝑠𝑖𝑤
𝑘=1

∀ 𝑖, 𝑙, 𝑞 | ℎ𝑖 = 2

(11)

∀ 𝑖 | ℎ𝑖 = 2

(12)

𝑤=1
𝑊

𝑄

𝐿

∑ ∑ ∑ 𝑦𝑖𝑤𝑙𝑞 = 2
𝑤=1 𝑙=1 𝑞=1
𝑄

∑ ∑ 𝑦𝑖𝑤𝑙𝑞 ≤ 1

∀ 𝑖, 𝑙 | ℎ𝑖 = 2

(13)

𝑤=1 𝑞=1
𝐼

𝐾

𝑄

∑ ∑ ∑ 𝑓𝑗𝑖 𝑋𝑖𝑙𝑘𝑞 ≤ 𝑀𝑀 𝑟𝑗𝑙

∀ 𝑗, 𝑙

(14)

𝑖=1 𝑘=1 𝑞=1

𝑏𝑖 𝑋𝑖𝑙𝑘𝑞 ≤ 𝑐𝑞
𝐿

∀ 𝑖, 𝑙, 𝑘, 𝑞

(15)

∀𝑖, 𝑞, 𝑣| 𝑘𝑘𝑖𝑣 = 1, 𝑔𝑞 ≠ 𝑣

(16)

𝐾

∑ ∑ 𝑋𝑖𝑙𝑘𝑞 = 0
𝑙=1 𝑘=1
𝐼

𝐼

(∑ 𝑑𝑖𝑚𝑛 𝑋𝑖𝑙𝑘𝑞 + ∑ 𝑎𝑠𝑝𝑚 𝑋𝑝𝑙𝑘𝑜 ) ≤ 1
𝑖=1

𝑝=1

+
𝑋𝑖𝑙4𝑞 + 𝑋𝑖𝑙5𝑞 + 𝑑1−
𝑚𝑛𝑞𝑖𝑤𝑙𝑘 − 𝑑1𝑚𝑛𝑞𝑖𝑤𝑙𝑘 = 𝑇1

(17)

(18)

+
𝑋𝑖𝑙4𝑞 + 𝑋𝑖𝑙5𝑞 + 𝑑2−
𝑚𝑛𝑙𝑞𝑖𝑝𝑜𝑘 − 𝑑2𝑚𝑛𝑙𝑞𝑖𝑝𝑜𝑘 = 𝑇2

∀ 𝑚, 𝑛, 𝑖, 𝑝, 𝑙, 𝑘, 𝑞, 𝑜 | 𝑖 ≠ 𝑝, (𝑞 = 𝑜 𝑜𝑟 𝑞 ≠ 𝑜),

𝑖=1 𝑞=1

(19)

( 𝑑𝑖𝑚𝑛 = 1 𝑜𝑟 𝑎𝑠𝑖𝑚 = 1), ( 𝑑𝑝𝑚𝑛 = 1 𝑜𝑟 𝑎𝑠𝑝𝑚 = 1)

𝑄

∑ ∑ 𝑎𝑠𝑖𝑚 𝑋𝑖𝑙𝑘𝑞 ≤ 1

(7)

𝐾

∀ 𝑚, 𝑛, 𝑞, 𝑖, 𝑤, 𝑙, 𝑘 | 𝑠𝑖𝑤 > 1

𝑄

∑ ∑ 𝑑𝑖𝑚𝑛 𝑋𝑖𝑙𝑘𝑞 ≤ 1

(6)

∀𝑚, 𝑛, 𝑙, 𝑘, 𝑞, 𝑜| 𝑛 ∈ {3,4}, 𝑞 ≠ 𝑜

𝑄

∑ ∑ ∑ 𝑋𝑖𝑙𝑘𝑞 = 𝑎𝑖
𝐼

∀ 𝑙, 𝑘, 𝑞| 𝑒𝑙𝑘𝑞 = 0

𝑖=1

−
+
−
+
−
+
𝑑3+
𝑚𝑛𝑖𝑢𝑝𝑙𝑘 , 𝑑4𝑚𝑛𝑙 , 𝑑4𝑚𝑛𝑙 , 𝑑5𝑚𝑛𝑙 𝑑5𝑚𝑛𝑙 , 𝑑6𝑚𝑚′ 𝑛𝑙𝑘𝑞𝑜 , 𝑑6𝑚𝑚′ 𝑛𝑙𝑘𝑞𝑜 ,

:

(5)

𝐼

∑ 𝑋𝑖𝑙𝑘𝑞 = 0

+
−
+
−
+
𝑑1−
𝑚𝑛𝑞𝑖𝑤𝑙𝑘 , 𝑑1𝑚𝑛𝑞𝑖𝑤𝑙𝑘 , 𝑑2𝑚𝑛𝑙𝑞𝑖𝑝𝑜𝑘 , 𝑑2𝑚𝑛𝑙𝑞𝑖𝑝𝑜𝑘 , 𝑑3𝑚𝑛𝑖𝑢𝑝𝑙𝑘 , 𝑑3𝑚𝑛𝑖𝑢𝑝𝑙𝑘,

𝑑4++
𝑚𝑛𝑙

∀ 𝑙, 𝑘, 𝑞

𝑖=1

𝑊

+
𝑑7−
𝑚𝑚 ′ 𝑛𝑙𝑘𝑞𝑜 , 𝑑7𝑚𝑚′ 𝑛𝑙𝑘𝑞𝑜 : deviation variables

(4)

𝐼

∑ 𝑋𝑖𝑙𝑘𝑞 𝑒𝑙𝑘𝑞 ≤ 1

1, if course 𝑖 is assigned to classroom 𝑞 on day
𝑙 at period k; 0, otherwise
1, if session 𝑤 of course 𝑖 is assigned to
classroom 𝑞 on day 𝑙; 0, otherwise

𝑦𝑖𝑤𝑙𝑞

∀ 𝑗, 𝑙, 𝑘

𝑖=1 𝑞=1

Decision variables
𝑋𝑖𝑙𝑘𝑞

𝑄

𝐼

∑ ∑ 𝑓𝑗𝑖 𝑋𝑖𝑙𝑘𝑞 ≤ 1

∀ 𝑚, 𝑛, 𝑙, 𝑘

(3)

𝑖=1 𝑞=1

20

Pamukkale Univ Muh Bilim Derg, 30(1), 17-30, 2024
H. Erdoğan Akbulut, F. Ozçelik, T. Saraç
𝑄

𝑄

𝐼

𝑖=1

(20)

− 𝑑3+
𝑚𝑛𝑖𝑢𝑝𝑙𝑘 = 𝑇3
𝐾

𝑝=1

− 𝑑6+
𝑚𝑚′ 𝑛𝑙𝑘𝑞𝑜 = 𝑇6

∀ 𝑚, 𝑛, 𝑖, 𝑢, 𝑝, 𝑙, 𝑘 | 𝑖 ≠ 𝑝, 𝑢 = (𝑛 + 1 ), 𝑑𝑖𝑚𝑛 = 1, 𝑑𝑝𝑚𝑢 = 1
𝐼

𝐼

(∑ 𝑑𝑖𝑚𝑛 𝑋𝑖𝑙𝑘𝑞 + ∑ 𝑑𝑝𝑚′𝑛 𝑋𝑝𝑙𝑘𝑜 ) + 𝑑6−
𝑚𝑚′ 𝑛𝑙𝑘𝑞𝑜

(∑ 𝑑𝑖𝑚𝑛 𝑋𝑖𝑙𝑘𝑞 + ∑ 𝑑𝑝𝑚𝑢 𝑋𝑝𝑙𝑘𝑞 ) + 𝑑3−
𝑚𝑛𝑖𝑢𝑝𝑙𝑘
𝑞=1
𝑞=1

∀ 𝑚, 𝑚′ , 𝑛, 𝑙, 𝑘, 𝑞, 𝑜|𝑚 ≠ 𝑚′ , 𝑞 ≠ 𝑜, 𝑛 > 1

𝑄
𝐼

+
(∑ ∑ ∑ 𝑑𝑖𝑚𝑛 𝑋𝑖𝑙𝑘𝑞 ) + 𝑑4−
𝑚𝑛𝑙 − 𝑑4𝑚𝑛𝑙 = 𝑇4

𝑖=1

∀ 𝑚, 𝑛, 𝑙 | 𝑛 ∈ {1,2}
𝐼

𝐾

𝐼

(∑ 𝑑𝑖𝑚𝑛 𝑋𝑖𝑙𝑘𝑞 + ∑ 𝑠𝑎𝑝𝑚′ 𝑋𝑝𝑙𝑘𝑜 ) +

(21)

𝑖=1 𝑘=1 𝑞=1

𝑝=1

+
𝑑7−
𝑚𝑚′ 𝑛𝑙𝑘𝑞𝑜 − 𝑑7𝑚𝑚′ 𝑛𝑙𝑘𝑞𝑜 = 𝑇7

𝑄

𝑋𝑖𝑙𝑘𝑞 ∈ {0,1}

∀ 𝑖, 𝑙, 𝑘, 𝑞

𝑦𝑖𝑤𝑙𝑞 ∈ {0,1}

∀ 𝑖, 𝑤, 𝑙, 𝑞

𝑖=1 𝑘=1 𝑞=1
𝐾

(26)

∀ 𝑚, 𝑚′ , 𝑛, 𝑙, 𝑘, 𝑞, 𝑜|𝑚 ≠ 𝑚′ , 𝑞 ≠ 𝑜, 𝑛 > 1

(∑ ∑ ∑ 𝑑𝑖𝑚𝑛 𝑋𝑖𝑙𝑘𝑞 ) +
𝐼

(25)

𝑄

(22)

+
(∑ ∑ ∑ 𝑎𝑠𝑝𝑚 𝑋𝑝𝑙𝑘𝑜 ) + 𝑑5−
𝑚𝑛𝑙 − 𝑑5𝑚𝑛𝑙 = 𝑇5

++
𝑑4++
∀ 𝑚, 𝑛, 𝑙
𝑚𝑛𝑙 , 𝑑5𝑚𝑛𝑙 ∈ {0,1}
−
+
+
𝑑1𝑚𝑛𝑞𝑖𝑤𝑙𝑘 , 𝑑1𝑚𝑛𝑞𝑖𝑤𝑙𝑘 , 𝑑2−
𝑚𝑛𝑙𝑞𝑖𝑝𝑜𝑘 , 𝑑2𝑚𝑛𝑙𝑞𝑖𝑝𝑜𝑘 ,

𝑝=1 𝑘=1 𝑜=1

∀ 𝑚, 𝑛, 𝑙 | 𝑛 ∈ {3,4}

(27)

+
−
+
−
𝑑3−
𝑚𝑛𝑖𝑢𝑝𝑙𝑘 , 𝑑3𝑚𝑛𝑖𝑢𝑝𝑙𝑘 , 𝑑4𝑚𝑛𝑙 , 𝑑4𝑚𝑛𝑙 , 𝑑5𝑚𝑛𝑙 ,

++
𝑑4+
𝑚𝑛𝑙 ≤ 𝑀𝑀 𝑑4𝑚𝑛𝑙

∀ 𝑚, 𝑛, 𝑙 | 𝑛 ∈ {1,2}

(23)

++
𝑑5+
𝑚𝑛𝑙 ≤ 𝑀𝑀 𝑑5𝑚𝑛𝑙

∀ 𝑚, 𝑛, 𝑙 | 𝑛 ∈ {3,4}

−
+
−
𝑑5+
𝑚𝑛𝑙 , 𝑑6𝑚𝑚′ 𝑛𝑙𝑘𝑞𝑜 , 𝑑6𝑚𝑚′ 𝑛𝑙𝑘𝑞𝑜 , 𝑑7𝑚𝑚′ 𝑛𝑙𝑘𝑞𝑜 ,

(24)

𝑑7+
𝑚𝑚′ 𝑛𝑙𝑘𝑞𝑜 ≥ 0
𝑠𝑢𝑏𝑗𝑒𝑐𝑡 𝑡𝑜

𝑀

𝑁

𝑄

𝐼

𝑊

𝐿

𝐾

𝑀

𝑁

𝐿

𝑄

𝐼

𝑄

𝐼

𝐾

min 𝑓 = ∑ ∑ ∑ ∑ ∑ ∑ ∑ 𝑑1+
∑
∑ ∑ ∑ 𝑑2+
𝑚𝑛𝑞𝑖𝑤𝑙𝑘 ⁄𝑀𝑁𝐿 + ∑ ∑ ∑ ∑
𝑚𝑛𝑙𝑞𝑖𝑝𝑜𝑘 ⁄𝑀𝑁𝐿
𝑝=1 𝑜=1 𝑘=1
𝑖=1
𝑚=1 𝑛=1 𝑞=1 𝑖=1 𝑤=1 𝑙=1 𝑘=1
𝑚=1 𝑛=1 𝑙=1 𝑞=1
𝑠𝑖𝑤>1
(𝑑𝑖𝑚𝑛 =1
𝑝≠𝑖
𝑜𝑟
(𝑑𝑝𝑚𝑛=1
𝑎𝑠𝑖𝑚 =1)
𝑜𝑟
𝑎𝑠𝑝𝑚 =1)
𝑀

𝑁

𝐼

𝑁

𝐼

𝐿

𝐾

𝑀

2

𝐿

++
+ ∑ ∑ ∑ ∑ ∑ ∑ ∑ 𝑑3+
𝑚𝑛𝑖𝑢𝑝𝑙𝑘 ⁄𝑀(𝑁 − 1)𝐿𝐾 + ∑ ∑ ∑ 𝑑4𝑚𝑛𝑙 ⁄𝑀𝑁𝐿
𝑚=1 𝑛=1 𝑖=1 𝑢=1 𝑝=1 𝑙=1 𝑘=1
𝑢=𝑛+1 𝑝≠𝑖
𝑀

4

𝐿

𝑚=1 𝑛=1 𝑙=1
𝐿

𝐾

𝑁

𝑀

𝑄

𝑀

𝑄

𝑀
+
+ ∑ ∑ ∑ 𝑑5++
𝑚𝑛𝑙 ⁄𝑀𝑁𝐿 + ∑ ∑ ∑ ∑ ∑ ∑ ∑ 𝑑6𝑚𝑚′ 𝑛𝑙𝑘𝑞𝑜 ⁄( ) (𝑁 − 1)𝐿𝐾
2
′
𝑙=1 𝑘=1 𝑛=1 𝑚=1 𝑞=1 𝑚 =1 𝑜=1
𝑚′ ≠𝑚 𝑜≠𝑞

𝑚=1 𝑛=3 𝑙=1
𝐿

𝐾

𝑁

𝑀

𝑄

𝑀

𝑄

+ ∑ ∑ ∑ ∑ ∑ ∑ ∑ 𝑑7+
𝑚𝑚′ 𝑛𝑙𝑘𝑞𝑜 ⁄𝑀(𝑁 − 1)𝐿𝐾
𝑙=1 𝑘=1 𝑛=1 𝑚=1 𝑞=1 𝑚′ =1 𝑜=1
𝑚′ ≠𝑚 𝑜≠𝑞

Eq. (1) ensures that all courses are assigned the number of
hours per week required by the curriculum. Eq. (2) and Eq. (3)
guarantee that a student group does not have more than one
compulsory or elective course at the same period on any given
day. Eq. (4) guarantees that no instructor is assigned to more
than one course and classroom on the same day and period.
Eq. (5) does not allow a classroom to be assigned more than
one course on a suitable day and period. Eq. (6) guarantees
that no course can be assigned to the unavailable day and
period of a classroom. If a session has two or three hours, Eq.
(7) and Eq. (8), respectively, ensure assigning all of these
hours consecutively. Eq. (9) and Eq. (10) ensure that the
courses with a single session are assigned to a single day. Eq.
(11), Eq. (12), and Eq. (13) provide that the courses with two
sessions are assigned on two different days. Eq. (14) ensures

that the courses of an instructor are assigned to the
instructor’s available days. Eq. (15) is the capacity constraint
of classrooms. Eq. (16) ensures that courses are assigned to
the appropriate type of classroom. Eq. (17) ensures that the
compulsory courses of the third- and fourth-year student
groups of a department do not conflict with the elective
courses of this department. Eq. (18) and Eq. (19) ensure that
student groups have at least a one-hour gap during the lunch
break (12:00-14:00) as much as possible. It is guaranteed by
Eq. (20) that, as much as possible, the compulsory courses of
consecutive student groups do not overlap. Eq. (21) ensures
that, as much as possible, the total compulsory course hours of
the first and second-year student groups of a department do
not exceed eight hours in a day. Eq. (22) ensures that, as much
as possible, the total hours of compulsory and elective courses

21

Pamukkale Univ Muh Bilim Derg, 30(1), 17-30, 2024
H. Erdoğan Akbulut, F. Ozçelik, T. Saraç
of the third and fourth-year student groups of a department do
not exceed eight hours in a day. Eq. (23) and Eq. (24) are for
++
the calculation of 𝑑4++
𝑚𝑛𝑙 and 𝑑5𝑚𝑛𝑙 . Eq. (25) ensures that, as
much as possible, a double major program student’s
compulsory courses and the compulsory courses of the same
student group of the double major department do not overlap.
Eq. (26) ensures that, as much as possible, a minor program
student’s compulsory courses do not overlap with the minor
program’s courses. The sign constraints of decision variables
are shown in Eq. (27). The objective function of the model is to
minimize the total of the undesired deviations. Each goal was
normalized by dividing it by its upper bound, and all goals
were considered to have equal weight.

4 Proposed SA algorithm
Simulated annealing (SA) is one of the classic metaheuristic
algorithms that has been successfully applied in the solution of
many problems in the literature, including university course
timetabling problems. The advantages of the simulated
annealing algorithm are strong local searching ability and
short running time [20]. The SA algorithm has been coded in
Python. The details of the developed SA algorithm are given in
the following subsections.
4.1

Sort unassigned courses in descending order of the estimated maximum
number of students
Sort classrooms in ascending order of their student capacity
for 𝑖 in 𝑠𝑜𝑟𝑡𝑒𝑑𝐶𝑜𝑢𝑟𝑠𝑒𝑠:
for 𝑞 in 𝑠𝑜𝑟𝑡𝑒𝑑𝐶𝑙𝑎𝑠𝑠𝑟𝑜𝑜𝑚𝑠:
Find periods as long as the course hour in classrooms that are
available and have enough capacity
if the available classrooms (𝑞1 ) and periods (𝑡𝑖1 ) were found;
if the instructor and student groups of the course 𝑖 were
available at periods (𝑡𝑖1);
Check whether the course 𝑖 was given in two sessions
if the course 𝑖 was given in one session;
The course 𝑖 (session(w)=1) was assigned to
classroom (𝑞1) at periods (𝑡𝑖1)
break
else;
The course 𝑖 (w=1) was assigned to the
classroom (𝑞1) at periods (𝑡𝑖1)
Find the periods except for the day of
the periods (𝑡𝑖1) as much as the course hour in
classrooms that is available and has enough
capacity for course 𝑖 (w=2)
if the available classrooms (𝑞2 ) and
periods (𝑡𝑖2) are found;
if the instructor and student groups of
the course 𝑖 are available at periods (𝑡𝑖2 );
The course 𝑖 (w=2) was assigned to
the classroom (𝑞2 ) at periods (𝑡𝑖2)
break

Figure 2. Pseudocode of the initial solution generation
mechanism.

Representation of the solution

The solutions are represented as a matrix, where the rows
represent the classrooms and the columns represent the
periods. A day was divided into eleven periods, from 9:00 to
20:00. Since only the weekdays were considered, a week
consists of 55 periods. Cells of the matrix contain information
about the assignment of the courses and the availability of the
classrooms. The cell is ‘0’ if the classroom is not available and
‘1’ if it is available. If there is a course code in a cell, this course
is assigned to the related time and classroom.

4.4

Cooling plan and termination criteria

The cooling plan used in this study is given in Eq. (28).
T𝑡𝑐+1 = α × T𝑡𝑐

(28)

In Eq. (28), 𝑡𝑐, 𝑇𝑡𝑐 represent the temperature change counter
and temperature value in step tc, respectively. The algorithm
was terminated when the temperature decreased to the final
temperature or when the total number of steps (𝑁𝑡𝑐 ) reached
the maximum value it could take or when the objective
function value reached 0.
4.5

Pseudocode of the developed SA algorithm

The pseudocode of the developed SA algorithm is shown in
Figure 3.
Figure 1. Solution representation.
A sample solution matrix is shown in Figure 1. For example,
the first session of CS 101 was assigned to classroom CR1
between 9:00 and 11:00 on Monday, and the second session of
CS 101 was assigned to classroom CR1 between 9:00 and
10:00 on Thursday.
4.2

Initial solution

An initial solution was generated by prioritizing the course
with the largest number of students and the classrooms with
the smallest capacity. The pseudocode of the initial solution
generation mechanism is shown in Figure 2.
4.3

Neighborhood structure

In this study, the simple move neighborhood and swap
neighborhood structures were used together. In a simple
move neighborhood structure, a randomly selected course
was moved to a randomly selected available classroom and
period. The swap neighborhood structure changes the
assignment of two randomly selected courses while ensuring
feasibility. The neighbor solutions were generated by using
one of the structures that were randomly selected.

In Figure 3, 𝑓, 𝑓𝑛𝑒𝑤 ,𝑇0 , 𝑇𝑓𝑖𝑛𝑎𝑙 , 𝑁𝑡𝑐 , 𝑡𝑐, 𝑟𝑛, 𝑇𝑡𝑐 , ∝, 𝑟𝑎𝑠 represents
the current objective function value, the neighbor solution's
objective function value, the initial temperature, the final
temperature, the total number of steps, the temperature
change counter, the number of steps at each temperature,
temperature value in step 𝑡𝑐, the cooling rate, a random
number between 0 and 1, respectively.

5 Experimental results and discussion
The proposed mathematical model and SA algorithm were
tested by randomly generated test problems and using
engineering faculty data from a private university. With the
proposed solution approaches, first a sample problem, then
test problems, and a real-life problem are solved.
All tests were performed on a PC with an Intel (R) Core (TM)
i5 - 035G11CPU @1.19 GHz processor and 8 GB of RAM. The
mathematical model was solved by GAMS/Cplex solver. The
time limit was set to 3600 seconds in GAMS.
As a result of the preliminary tests, the values of the final
temperature (𝑇𝑓𝑖𝑛𝑎𝑙 ), the cooling rate (α), and the number of
steps at each temperature (𝑟𝑛) parameters were fixed as 0,
0.05, and 10, respectively, as they gave successful results.

22

Pamukkale Univ Muh Bilim Derg, 30(1), 17-30, 2024
H. Erdoğan Akbulut, F. Ozçelik, T. Saraç

Generate an initial solution
Set 𝑇𝑜 ∈ {10, 50, 100}, 𝑇𝑓𝑖𝑛𝑎𝑙 = 0, ∝= 0.05, 𝑟𝑛 = 10, 𝑁𝑡𝑐 ∈ {100,150,200, 250} parameter values 𝑡𝑐 = 1, 𝑟𝑛 = 1
Calculate the current objective function value (𝑓)
if 𝑇𝑡𝑐 > 0, 𝑡𝑐 < 𝑁𝑡𝑐 and 𝑓>0;
if 𝑟𝑛 < 𝐹;
Randomly select a course
Find the neighbor solutions of this course, create a 𝑟𝑒𝑠 list, and append the neighbor solutions in the 𝑟𝑒𝑠 list
if 𝑟𝑒𝑠 > 0;
Randomly select a neighbor solution from the 𝑟𝑒𝑠 list
if the selected neighbor solution was found by using the simple move neighborhood structure;
Calculate the objective function value of the selected neighbor solution, 𝑓𝑛𝑒𝑤
if 𝑓𝑛𝑒𝑤 <𝑓;
This course was assigned to a new classroom and period
𝑓 = 𝑓𝑛𝑒𝑤
𝑟𝑛 = 𝑟𝑛 + 1
else;
(𝑓
−𝑓)
if 𝑟𝑎𝑛(0,1) < exp[− 𝑛𝑒𝑤
]
𝑇𝑡𝑐

This course was assigned to a new classroom and period
𝑓 = 𝑓𝑛𝑒𝑤
𝑟𝑛 = 𝑟𝑛 + 1
else;
𝑟𝑛 = 𝑟𝑛 + 1
else if the selected neighbor solution was found by using a swap neighborhood structure;
Calculate the objective function value of the selected neighbor solution, 𝑓𝑛𝑒𝑤
if 𝑓𝑛𝑒𝑤 < 𝑓;
Swap this course with a selected course
𝑓 = 𝑓𝑛𝑒𝑤
𝑟𝑛 = 𝑟𝑛 + 1
else;
(𝑓
−𝑓)
if 𝑟𝑎𝑛(0,1) < exp[− 𝑛𝑒𝑤
]
𝑇𝑡𝑐

Swap this course with a selected course
𝑓 = 𝑓𝑛𝑒𝑤
𝑟𝑛 = 𝑟𝑛 + 1
else;
𝑟𝑛 = 𝑟𝑛 + 1
else;
𝑟𝑛 = 𝑟𝑛 + 1
else;
𝑡𝑐 = 𝑡𝑐 + 1
T𝑡𝑐+1 = α × Ttc
else if 𝑇𝑡𝑐 = 0 or 𝑡𝑐 = 𝑁𝑡𝑐 or 𝑓=0;
break

Figure 3. Pseudocode of the developed SA algorithm.
For the initial temperature (𝑇0 ), and the total number of steps
(𝑁𝑡𝑐 ) parameters, more than one successful parameter value
was obtained as a result of preliminary tests. Since successful
results were obtained when values of 10, 50, or 100 for the
initial temperature, and 100, 150, 200, or 250 for the total
number of steps were used, all problems were solved with all
combinations of these parameter values in 10 repetitions and
the best results were reported.
5.1

Sample problem

In the sample problem, there are two departments, four
student groups in each department, and 35 courses, including
compulsory and elective courses. The parameters of the
problem were given in Appendices C1, C2, C3, C4, C5, and C6.
The optimal solution was obtained in 32.49 seconds, and the
optimality gap is zero with the proposed mathematical model.
The obtained timetables for Department 1 and Department 2
are shown in Tables 2 and 3, respectively.
The sample problem has also been solved with the proposed
SA algorithm. The SA results for different parameter values are

given in Table 4. As seen from the table, the optimal solution
was obtained with all parameters in a shorter time than
GAMS/Cplex.
5.2

Randomly generated test problems

Two test problems, with three departments and 57 courses
(problem 1) and with four departments and 77 courses
(problem 2), were generated randomly. For both problems, no
feasible solution could be obtained with the mathematical
model within the time limit. The results of SA are given in
Table 5. As seen from the table, successful results with an
objective function value near zero were obtained in a
reasonable time.
5.3

Real-Life problem

A real-life problem from a private university's engineering
faculty was also solved using the proposed solution methods.
There were 107 courses in five departments, 53 instructors,
and 31 classrooms in the related term. As seen in Table 6, the
best result (f = 0.1264) was achieved in 148.64 seconds, and
all results were obtained in less than 300 seconds.

23

Pamukkale Univ Muh Bilim Derg, 30(1), 17-30, 2024
H. Erdoğan Akbulut, F. Ozçelik, T. Saraç

Table 2. Course timetabling of Department 1.
Period\Day

Monday

9:00-10:00

IE 341/
I6/
CR1

10:00-11:00

IE 403/
I6/
CR3

11:00-12:00

IE 403/
I6/
CR3

Tuesday
MATH
IE 407/
201/
I16/
I1/
CR2
CR5
MATH
IE 407/
201/
I16/
I1/
CR2
CR5
IE 407/
I16/
CR2

Wednesday
CS 101/
I3/
CR5

CS 415/
I5/
CR3

IE 341/
I6/
CR2

MATH
211R/
I12/
CR4
MATH
211/
I5/
CR5
MATH
211/
I5/
CR5
IE 351/
I4/
CR1

CS
101L1/I14/
CR6

CS 415/
I5/
CR3

IE 341/
I6/
CR2

IE 351/
I4/
CR1

CS 101L1/
I14/
CR6

IE 491/
I4/
CR1

CS 101/
I3/
CR5

PHYS 101/
I2/
CR5

IE 491/
I4/
CR1

CS 101/
I3/
CR5

MATH 101/
I1/
CR5

IE 201/
I4/
CR4
IE 201/
I4/
CR4

IE 361/
I5/
CR3

13:00-14:00

15:00-16:00

MATH
101/
I1/
CR5
MATH
101/
I1/
CR5

IE 361/
I5/
CR3
IE 361/
I5/
CR3

16:00-17:00

IE 401/
I7/
CR5

IE 371/
I7/
CR1

17:00-18:00

IE 401/
I7/
CR5

IE 371/
I7/
CR1

18:00-19:00

IE 401/
I7/
CR5

19:00-20:00

MATH
201/
I1/
CR5

CS 415/
I5/
CR2

PHYS
101L2/
I13/
CR7
PHYS
101L2/
I13/
CR7
PHYS
101L2/
I13/
CR7

IE 371/
I7/
CR1

PHYS 101/
I2/
CR5

Friday
IE 433/
I16/
CR3

MATH 101/
I1/
CR5

12:00-13:00

14:00-15:00

Thursday

IE 351/
I4/
CR4

PHYS 101/
I2/
CR5

MATH 211/
I5/
CR5

IE 403/
I6/
CR3

PHYS
101L1/
I13/
CR7
PHYS
101L1/
I13/
CR7
PHYS
101L1/
I13/
CR7

IE 433/
I16/
CR3
IE 433/
I16/
CR3

MATH
101R/
I12/
CR5
MATH
101R/
I12/
CR5
IE 405/
I16/
CR3
IE 405/
I16/
CR3
IE 201/
I4/
CR2

IE 405/
I16/
CR3

Table 3. Course timetabling of Department 2.
Period\Day

Monday
CS 472/
I17/
CR4

Tuesday
MATH 201/
I1/
CR5

10:00-11:00

CS 472/
I17/
CR4

MATH 201/
I1/
CR5

11:00-12:00

CS 472/
I17/
CR4

9:00-10:00

Wednesday
CS 101/
I3/
CR5
MATH
CS 361/
101/
I11/
I1/
CR4
CR5
MATH
CS 361/
101/
I11/
I1/
CR4
CR5

12:00-13:00
13:00-14:00
14:00-15:00

MATH 101/
I1/
CR5

CS 441/
I9/
CR2

CS 201/
I8/
CR4
CS 201/
I8/
CR4

CS 491/
I10/
CR3
CS 491/
I10/
CR3

CS 415/
I5/
CR3
CS 415/
I5/
CR3

Thursday
CS 201/
CS 431/
ÖI/
I10/
CR5
CR4

Friday
CS 311/
I10/
CR5
MATH 211R/
I12/
CR4
MATH 211/
I5/
CR5

CS 431/
I10/
CR4

MATH 211/
I5/
CR5

CS 431/
I10/
CR4

24

Pamukkale Univ Muh Bilim Derg, 30(1), 17-30, 2024
H. Erdoğan Akbulut, F. Ozçelik, T. Saraç
Table 3. Continued.
Period\Day

Monday

Tuesday

15:00-16:00

MATH 101/
I1/
CR5

CS 441/
I9/
CR2

CS 101 L2
/I14 /CR6

16:00-17:00

CS 201L/
I15/ CR6

CS 441/
I9/
CR2

CS 101 L2
/I14 /CR6

17:00-18:00

CS 201L/
I15/ CR6

Wednesday

CS 101/
I3/
CR5
PHYS
101/
I2/
CR5
PHYS
101/
I2/
CR5

CS 101/
I3/
CR5
CS 492/
I10/
CR3
CS 311/
I10/
CR2

18:00-19:00

19:00-20:00

Thursday

MATH 201/
I1/
CR5

CS 415/
I5/
CR2

PHYS 101/
I2/
CR5

CS
361/
I11/
CR2

MATH
211/
I5/
CR5

CS 101
L3/
I14/
CR6
CS 101
L3/
I14/
CR6

CS 311/
I10/
CR2

Friday
MATH
CS
101R/
303/
I12/
I9/
CR5
CR2
MATH
CS
101R/
303/
I12/
I9/
CR5
CR2
PHYS
CS
101L3/
303/
I13/
I9/
CR7
CR2
PHYS
101L3/
I13/
CR7
PHYS
101L3/
I13/
CR7

Table 4. Results of sample problem using SA.
𝑻𝟎
10
10
10
10
50
50
50
50
100
100
100
100

𝑵𝒕𝒄
100
150
200
250
100
150
200
250
100
150
200
250

f
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

CPU (sec.)
3.70
1.95
2.83
2.90
3.27
2.80
2.85
2.67
3.55
2.02
2.39
4.10

Table 5. Test results for the randomly generated test problems using SA.
Problem 1
𝑻𝟎
10
10
10
10
50
50
50
50
100
100
100
100

𝑁𝑡𝑐
100
150
200
250
100
150
200
250
100
150
200
250

𝑓
0.014
0.002
0.004
0.004
0.012
0.006
0.006
0.006
0.008
0.006
0.006
0.004

Problem 2
CPU (sec.)
54.11
83.84
113.09
141.52
56.15
87.60
116.99
624.45
56.63
85.24
114.41
140.60

𝑓
0.0893
0.0878
0.0833
0.0792
0.0858
0.0717
0.0813
0.0828
0.1212
0.0954
0.0772
0.0722

CPU (sec.)
465.68
318.34
149.11
207.11
79.88
114.41
146.62
183.35
70.53
109.84
149.49
184.18

Table 6. Test results for the real-life problem using SA.
𝑻𝟎
10
10
10
10
50
50
50
50
100
100
100
100

𝑵𝒕𝒄
100
150
200
250
100
150
200
250
100
150
200
250

F
0.1851
0.1503
0.1618
0.1264
0.1749
0.1768
0.1573
0.1741
0.1861
0.1560
0.1576
0.1622

CPU (sec.)
217.84
92.13
114.29
148.64
55.00
261.29
288.65
141.76
56.61
86.87
109.96
155.87

25

Pamukkale Univ Muh Bilim Derg, 30(1), 17-30, 2024
H. Erdoğan Akbulut, F. Ozçelik, T. Saraç

The deviation values and the objective function value for the
current state and SA result are shown in Table 7. In the current
state, while the faculty course timetabling was prepared in
approximately 2-3 weeks, a better result was achieved in
148.64 seconds with the SA algorithm. As can be seen from the
table, in the current state double major (G6) or minor (G7)
students have much more course overlap than the solution
obtained with the SA algorithm. Another goal is that the
compulsory courses of consecutive student groups do not
overlap as much as possible. In other words, G3 was seen to
have less course overlap with the SA algorithm compared to
the current situation. G4 and G5 were almost provided with
the developed SA algorithm. Finally, G1 and G2 were achieved
with the developed SA algorithm. Considering the objective
function values, an 83% improvement was achieved with the
proposed SA for the real-life problem.
Table 7. The comparison of the SA algorithm’s result with the
current state of the real-life problem.
G1
G2
G3
G4
G5
G6
G7
𝑓

Current state
0.20
0.10
0.082
0.05
0.05
0.048
0.218
0.7490

Proposed SA algorithm
0
0
0.0364
0
0.01
0.020
0.06
0.1264

6 Conclusion
In this study, the faculty-level UCTP was addressed. Since most
of the classrooms were shared with other faculties, the
availability of the classrooms was taken into consideration.
The goals listed below were taken into account in this study,
and a goal programming model was developed in line with
these objectives.





Having a time gap at noon for student groups,
No overlapping of the compulsory courses of
consecutive student groups of departments,
Limiting the course hours of student groups to less
than or equal to eight hours per day,
No overlapping of the courses of the student in the
double major or minor programs.

A SA algorithm was developed to tackle large-sized problems.
The randomly generated test problems and a real-life problem
were solved using the proposed mathematical model and the
developed SA algorithm using different parameter values. In
addition to the solution time advantage, the SA algorithm
reached successful solutions within a reasonable time for
problems for which the mathematical model failed to find a
feasible solution.
In future studies, new constraints may be added to the facultylevel course timetabling problem, such as not assigning a
course to the last time of the day and setting the hours per day
for student groups to a specified minimum. The size of the
problem can be enlarged to include the courses of more than
one faculty and department. Hence, a more suitable course
timetable will be developed for students who wish to engage
in a double major or minor program both within and across
faculties. Different heuristics, meta-heuristics, or hybrid
algorithms can be used to solve the considered problem.

7 Author contribution statements
In the scope of this study, Hatice ERDOĞAN AKBULUT in the
formation of the idea, the design, the assessment of obtained
results, the literature review, supplying the data used, and
examining the results; Feristah OZÇELIK, in the formation of
the idea, the design, examining the results and the spelling and
checking the article in terms of content; Tugba SARAÇ the
formation of the idea, the design, examining the results and the
spelling and checking the article in terms of content were
contributed.

8 Ethics committee approval and conflict of
interest statement
There is no need to obtain permission from the ethics
committee for the article prepared.
There is no conflict of interest with any person/institution in
the article prepared.

9 References
[1] Wren A. Scheduling, Timetabling and Rostering-A special
Relationship?. Editors:
Burke EK, Ross P.
Practice and Theory of Automated Timetabling,
46-75, Heidelberg, Berlin, Springer, 1996.
[2] Burke EK, Petrovic S, Qu R. “Case-based heuristic
selection for timetabling problems”. Journal of
Scheduling, 9(2), 115-132, 2006.
[3] Petrovic S, Burke E. “University timetabling”. Handbook
of Scheduling: Algorithms, Models, and Performance
Analysis, 45, 1-34, 2004.
[4] Schaerf A. “Survey of automated timetabling”. Artificial
Intelligence Review, 13(2), 87-127, 1999.
[5] Babaei H, Karimpour J, Hadi A. “A survey of approaches
for university course timetabling problem”. Computers
and Industrial Engineering, 86, 43-59, 2015.
[6] Altunay H, Eren T. “A literature review for course
scheduling problem”. Pamukkale University Journal of
Engineering Sciences, 23(1), 55-70, 2017.
[7] Mirhassani SA. “A computational approach to enhancing
course timetabling with integer programming”. Applied
Mathematics and Computation, 175(1), 814-822, 2006.
[8] Ismayilova NA, Saǧir M, Gasimov RN. “A multiobjective
faculty-course-time slot assignment problem with
preferences”. Mathematical and Computer Modelling,
46(7-8), 1017-1029, 2007.
[9] Cura T. “Timetabling of faculty lectures using simulated
annealing algorithm”. İstanbul Commerce University
Journal of Science, 6(12), 1-20, 2007.
[10] Al Tarawneh HY, Ayob M. “Using tabu search with multineighborhood structures to solve university course
timetable UKM case study (faculty of engineering)”.
2011 3rd Conference on Data Mining and Optimization
(DMO), Putrajaya, Malaysia, 28-29 June 2011.
[11] Nguyen K, Nguyen P, Tran N. “A hybrid algorithm of
harmony search and bees algorithm for a university
course timetabling problem”. International Journal of
Computer Science Issues, 9(1), 12-17, 2012.
[12] Demir Y, Çelik C. “An Integer Programming Approach for
Curriculum Based Timetabling Problem Solution”.
Journal of the Faculty of Engineering and Architecture of
Gazi University, 31(1), 145-159, 2016.

26

Pamukkale Univ Muh Bilim Derg, 30(1), 17-30, 2024
H. Erdoğan Akbulut, F. Ozçelik, T. Saraç
[13] Abdelhalim EA, El Khayat GA. “A utilization-based genetic
algorithm for solving the university timetabling problem
(UGA)”.
Alexandria
Engineering
Journal,
55(2), 1395-1409, 2016.
[14] Borchani R, Elloumi A, Masmoudi M. “Variable
neighborhood descent search based algorithms for
course timetabling problem: Application to a Tunisian
University”. Electronic Notes in Discrete Mathematics,
58, 119-126, 2017.
[15] Ertane E. Course Timetabling with Double Major
Constraints. MSc Thesis, Ataturk University, Erzurum,
Turkey, 2018.
[16] Özkan A. Solving University Course Timetabling
Problems with Integer Linear Programming and
Heuristic Approaches. PhD Thesis, Hacettepe University,
Ankara, Turkey, 2019.
[17] Thepphakorn T, Pongcharoen P. “Performance
improvement strategies on cuckoo search algorithms for
solving the university course timetabling problem”.
Expert Systems with Applications, 161, 1-21, 2020.

[18] Alnowaini G, Aljomai AA. "Genetic Algorithm for Solving
University Course Timetabling Problem Using Dynamic
Chromosomes". 2021 International Conference of
Technology, Science and Administration, Taiz, Yemen,
22-24 March 2021.
[19] Ariyazand A, Soleimani H, Etebari F, Mehdizadeh E.
"Improved satisfaction of university faculty by utilizing
the Bat metaheuristic algorithm (Case study of the faculty
of humanities, Islamic Azad University, Parand Branch)".
Journal of Industrial Engineering and Management
Studies, 9(8), 95-108, 2022.
[20] Long J, Wu S, Han X, Wang Y, Liu L. "Autonomous task
planning method for multi-satellite system based on a
hybrid genetic algorithm". Aerospace, 10(1), 1-18, 2023.

Appendix A
Appendix A1. Explanations for the abbreviations of hard constraints.
Identifier
H1
H2
H3
H4
H5
H6
H7
H8
H9
H10
H11
H12
H13
H14
H15
H16
H17
H18
H19
H20

Explanation
Instructors cannot be assigned to more than one course or classroom at the same period.
Students/student groups cannot be assigned to more than one course or classroom at the same period.
More than one course, instructor, and student group cannot be assigned to a classroom at the same period.
Courses should be assigned to the timetable to fill the number of weekly course hours.
Instructors should be assigned as many courses as they have to teach daily or weekly.
Courses should be assigned to periods when a classroom is available.
The courses given to a single session must be assigned consecutively throughout the course's duration.
Courses assigned to more than one session must be assigned consecutively in the same amount as the course hours
specified in each session, provided that they are not on the same day or consecutive days.
If the course has a predetermined instructor, time, or classroom, it should be assigned to the schedule in advance.
Courses should be assigned to specific days and periods.
Courses should be assigned to a technically feasible classroom.
Courses should be assigned to classrooms with enough capacity, or capacity overruns may be allowed up to a specified
ratio.
Courses should be assigned according to the availability of the student groups to which they are assigned.
All courses must be assigned to the timetable.
Compulsory courses and elective courses to be taken by a student/student group should not conflict.
Courses should be assigned according to the instructor’s preferences.
Courses can only be assigned to the available periods.
Even if a course is divided into more than one session, all sessions should be assigned to the same classroom.
The number of total daily course hours for a student/student group should not exceed the previously specified
number of course hours.
Normal education courses and evening education courses can only be taken at certain times.
Appendix A2. Explanations for the abbreviations of soft constraints.

Identifier
S1
S2
S3
S4
S5
S6
S7
S8
S9
S10
S11

Explanation
The number of courses/course hours that the student group will receive daily should not exceed the specified number
of courses/course hours as much as possible.
For a two-session course, there should be at least a one-day gap between sessions, if possible.
Student groups' courses should not overlap as much as possible.
Compulsory courses of student groups in consecutive years should not overlap as much as possible.
The classroom must have enough space for the course, or overcrowding may be permitted up to a particular ratio as
much as possible.
Courses of students/student groups should not be assigned to lunch break as much as possible.
Courses of consecutive student groups of different departments should not overlap as much as possible.
Departmental courses should not be assigned as much as possible to the other department’s building.
Courses of student groups should be assigned according to the day-time slot preferences as much as possible.
A student group's elective courses should not overlap as much as possible.
Courses of a student group should be assigned to as few days as possible.

27

Pamukkale Univ Muh Bilim Derg, 30(1), 17-30, 2024
H. Erdoğan Akbulut, F. Ozçelik, T. Saraç
Appendix A2. Continued.
Identifier
S12
S13
S14
S15
S16
S17
S18
S19

Explanation
All hours of a course should be given in the same classroom as much as possible.
The hours of a course should be assigned as consecutively as possible.
An instructor’s preferences, such as a day-time slot, course, and classroom, should be provided as much as possible.
An instructor's daily or weekly course or course hours should not exceed the specified number of courses or course hours as
much as possible.
On any given day or block, there should be as few as possible time gaps between the courses that the student group is taking
and/or the instructors are teaching.
An instructor's courses should be assigned to as few days as possible.
Double major program students’ courses should not overlap as much as possible.
Minor program students' courses should not overlap as much as possible.

Appendix A3. Explanations for the abbreviations of objective functions.
Identifier
O1
O2
O3
O4
O5
O6
O7
O8

Explanation
Maximizing the classroom utilization
Minimizing the total penalty for violations of soft constraints
Maximizing the instructor’s preferences
Minimizing the penalty in case the department’s/administrative unit’s preferences are not met
Minimizing the penalty in case the instructors’ preferences are not met
Maximizing the total number of course-classroom-instructor-time or course-instructor-time assignments
Minimizing the double major program student’s course overlap
Minimizing the minor program student’s course overlap

Appendix B
Appendix B. Explanations for the abbreviations of solution methods.
Identifier
ABC
AHP
ANP
BA
BTA
CS
FA
GA
GP
HS
HM
ILP
IP
ILS
MOP
PSO
SA
SP
TS
VND

Explanation
Artificial Bee Colony
Analytic Hierarchy Process
Analytic Network Process
Bees Algorithm
Bat Algorithm
Cuckoo Search
Firefly Algorithm
Genetic Algorithm
Goal Programming
Harmony Search
Hybrid Method
Integer Linear Programming
Integer Programming
Iterated Local Search
Multi-Objective Programming
Particle Swarm Optimization
Simulated Annealing
Stochastic Programming
Tabu Search
Variable Neighborhood Descent

Appendix C
Appendix C1. Compulsory courses for the sample problem.

Department
1

Department

Student
group

1

2

Course code
MATH 101
MATH 101R
PHYS 101
PHYS 101L1
PHYS 101L2
CS 101
CS 101L1
MATH 201
IE 201
MATH 211
MATH 211R

Weekly
course
hours
4
2
3
3
3
3
2
3
3
3
1

Number of
sessions

Instructor

2
1
2
1
1
2
1
2
2
2
1

I1
I12
I2
I13
I13
I3
I14
I1
I4
I5
I12

Maximum number
of students to take
the course
80
80
80
25
25
80
35
85
40
85
50

Classroom
type
1
1
1
2
2
1
3
1
1
1
1

28

Pamukkale Univ Muh Bilim Derg, 30(1), 17-30, 2024
H. Erdoğan Akbulut, F. Ozçelik, T. Saraç
Appendix C1. Continued.
Student
group

Department
1

Department

Course code
IE 341
IE 351
IE 361
IE 371
IE 403
IE 491
MATH 101
MATH 101R
PHYS 101
PHYS 101L3
CS 101
CS 101L2
CS101L3
CS 201
CS 201L
MATH 201
MATH 211
MATH 211R
CS 303
CS 311
CS 361
CS 491
CS 492

3
4

Department
2

1

2

3
4

Weekly
course hours
3
3
3
3
3
2
4
2
3
3
3
2
2
3
2
3
3
1
3
3
3
2
1

Number of
sessions
2
2
1
1
2
1
2
1
2
1
2
1
1
2
1
2
2
1
1
2
2
1
1

Instructor

Maximum number of
students to take the course
40
40
40
40
40
40
80
80
80
25
80
35
35
35
35
85
85
50
40
40
40
40
40

I6
I4
I5
I7
I6
I4
I1
I12
I2
I13
I3
I14
I14
I8
I15
I1
I5
I12
I9
I10
I11
I10
I10

Classroom
type
1
1
1
1
1
1
1
1
1
2
1
3
3
1
1
1
1
1
1
1
1
1
1

Appendix C2. Elective courses for the sample problem.
Department

Department 1

Department 2

Course code

Weekly
course hours

IE 405
IE 407
IE 433
IE 401
CS 431
CS 472
CS 441
CS 415

3
3
3
3
3
3
3
3

Number
of
sessions
1
1
1
1
2
1
1
2

Instructor

Maximum number of students
who can take the course

Classroom
type

I16
I16
I16
I7
I10
I17
I9
I5

45
45
50
80
50
50
50
50

1
1
1
1
1
1
1
1

Appendix C3. Classrooms for the sample problem.
Classroom name
CR1
CR2
CR3
CR4
CR5
CR6
CR7

Classroom type
Normal (1)
Normal (1)
Normal (1)
Normal (1)
Normal (1)
Computer laboratory (3)
Physics laboratory (2)

Classroom capacity
40
52
64
68
144
44
28

Appendix C4. Availability of classrooms based on the period for the sample problem.
Period
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
11
12
13
14
15
16
17
18

CR1
1
1
1
1
1
1
1
0
0
0
0
0
0
0
1
1
1
1

CR2
0
0
0
0
1
1
1
1
1
1
1
1
1
1
0
0
1
1

CR3
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1

CR4
1
1
1
1
1
0
0
1
1
1
1
0
0
0
0
1
1
1

CR5
0
0
0
0
1
1
1
1
1
1
1
1
1
1
1
0
0
0

CR6
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1

CR7
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1

Period
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46

CR1
1
1
0
0
0
1
1
1
1
1
1
0
0
0
0
0
1
1

CR2
1
0
0
0
0
1
1
1
1
1
1
1
1
1
1
1
0
0

CR3
1
1
1
1
1
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
1

CR4
0
0
0
0
0
1
1
1
1
1
1
1
1
1
1
1
1
1

CR5
0
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1

CR6
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1

CR7
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1

29

Pamukkale Univ Muh Bilim Derg, 30(1), 17-30, 2024
H. Erdoğan Akbulut, F. Ozçelik, T. Saraç
Appendix C4. Continued.
Period
19
20
21
22
23
24
25
26
27
28

CR1
1
1
1
1
1
1
1
1
1
1

CR2
1
1
1
1
1
1
1
1
1
1

CR3
1
1
1
1
1
1
1
1
1
1

CR4
1
1
1
1
1
1
1
1
0
0

CR5
0
1
1
1
1
1
1
0
0
0

CR6
1
1
1
1
1
1
1
1
1
1

CR7
1
1
1
1
1
1
1
1
1
1

Period
47
48
49
50
51
52
53
54
55

CR1
1
1
1
1
0
0
1
1
1

CR2
0
0
0
1
1
1
1
1
1

CR3
1
1
1
1
1
1
1
1
1

CR4
1
1
1
0
0
0
0
0
0

CR5
1
1
1
1
1
1
0
0
0

CR6
1
1
0
0
0
0
0
0
0

CR7
1
1
1
1
1
1
1
1
1

*1: Available. 0: not available.

Appendix C5. Daily availability of instructors for the sample problem.
Instructor
I1
I2
I3
I4
I5
I6
I7
I8
I9
I10
I11
I12
I13
I14
I15
I16
I17

Monday(1)
1
1
0
0
1
1
1
0
1
0
0
1
0
1
1
0
1

Tuesday(2)
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
0

Wednesday(3)
1
1
1
1
1
1
0
1
1
1
1
0
1
1
1
0
1

Thursday(4)
0
1
1
1
0
1
0
1
0
1
0
1
1
1
1
0
1

Friday(5)
0
0
1
1
1
0
1
0
1
1
1
1
1
0
1
1
0

*1: Available. 0: not available.

Appendix C6. Minor courses of departments for the sample problem.
Department
Department 1
Department 2

Minor courses
IE 201, IE 341, IE 351
CS 201, CS 303, CS 311

30

