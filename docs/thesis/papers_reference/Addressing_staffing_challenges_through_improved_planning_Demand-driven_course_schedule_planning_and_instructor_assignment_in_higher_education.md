Decision Support Systems 187 (2024) 114345

Contents lists available at ScienceDirect

Decision Support Systems
journal homepage: www.elsevier.com/locate/dss

Addressing staffing challenges through improved planning: Demand-driven
course schedule planning and instructor assignment in higher education
Guisen Xue , O. Felix Offodile , Rouzbeh Razavi , Dong-Heon Kwak , Jose Benitez *
Department of Information Systems and Business Analytics, Ambassador Crawford College of Business and Entrepreneurship, Kent State University, Kent, USA

A R T I C L E I N F O

A B S T R A C T

Keywords:
Academic scheduling
Mixed integer linear programming (MILP)
Decision support system
Integrated optimization

This paper presents a novel decision support system (DSS) to address the University Course Timetabling Problem
(UCTP). The solution decomposes the NP-complete UCTP into two sub-problems, allowing a structured approach
to addressing the complexities inherent in the UCTP process. A mixed integer linear programming (MILP) model
is proposed to integrate academic year course schedule planning and instructor assignment, accommodating
various constraints to meet student demands. The model optimizes the number of course sections and strategically schedules instructors, aiming to reduce the number of new and distinct courses assigned to them. Historical data from an academic department encompassing multiple disciplines, including Computer Information
Systems, Business Management, and Business Analytics, at a large public university in the U.S. is used to develop
the model, and the results are compared with the actual course schedule and instructor assignment. The results
demonstrate that the proposed DSS would result in a 14 % reduction in the number of course sections offered,
translating to approximately $130,000 in annual savings. Additionally, it could significantly reduce the number
of new courses assigned to instructors by up to 81 % and the number of distinct course sections assigned to them
by 29 %.

1. Introduction
In the last decade, universities have faced considerable financial
challenges stemming from a continuous decline in enrollment and
underfunding [1,2]. The recent Covid-19 pandemic has further intensified these difficulties [3]. To maintain financial stability, many universities have adopted proactive measures, such as freezing faculty
hiring, reducing salaries for faculty and staff, using additional scholarships to attract potential students, and deploying part-time instructors.
However, due to pedagogical, accreditation, and other strictures, the use
of part-time instructors may be limited, especially if course staffing can
be strategically managed with efficient scheduling models.
Staff costs, including salaries and other benefits, typically constitute
the largest portion of university expenditures. For example, the National
Center for Education Statistics (NCES) reported that instruction
accounted for 26 % of total expenses for 4-year public institutions in
2019–20 [4], while Stanford University noted that 64 % of total expenditures for the fiscal year 2022–23 were spent on salaries and benefits [5]. Consequently, addressing staff costs is vital for effective cost

control and optimization in universities. This study, therefore, aims to
minimize staff costs by better aligning the number of course sections
with students’ course demand within the University Course Timetabling
(UCT) framework. The efficient allocation of instructors, facilities, and
other resources is critical for universities to offer the best possible education to their students, facilitating timely progression toward graduation through well-designed course timetables and other services. The
University Course Timetabling Problem (UCTP) is a complex, multidimensional assignment problem that involves assigning students and
instructors to course sections at designated timeslots and classrooms [6].
The UCTP has been proven to be NP-complete [7]. While many NPcomplete problems can be solved efficiently in practice, integrating all
dimensions of the UCTP into a comprehensive model presents a particularly challenging problem. This complexity arises due to the numerous
binary variables involved across all assignment problems, necessitating
the use of advanced heuristic algorithms to achieve solutions of uncertain accuracy within a reasonable timeframe. The existing literature on
UCT is abundant with models and methods [8]. However, only a few
studies, such as [9–11], detailed actual implementations of automated

* Corresponding author.
E-mail addresses: gxue@kent.edu (G. Xue), foffodil@kent.edu (O.F. Offodile), rrazavi@kent.edu (R. Razavi), dkwak@kent.edu (D.-H. Kwak), jbenite1@kent.edu
(J. Benitez).
https://doi.org/10.1016/j.dss.2024.114345
Received 29 February 2024; Received in revised form 23 September 2024; Accepted 24 September 2024
Available online 25 September 2024
0167-9236/© 2024 The Authors. Published by Elsevier B.V. This is an open access article under the CC BY-NC license (http://creativecommons.org/licenses/bync/4.0/).

G. Xue et al.

Decision Support Systems 187 (2024) 114345

timetabling systems. The survey study in [12] also identified a persistent
gap between UCT literature and its practical application in academia.
While the literature tends to focus on developing more sophisticated
methods for solving timetabling problems, academic practice often
prioritizes the design and development of user-friendly and interactive
tools that cater to the institution’s instructional needs [8]. Consequently, there is an ongoing demand for automated approaches that
facilitate the effective transfer of past knowledge to final schedules,
addressing timetabling problems in academic institutions. The aim of
the International Timetabling Competition (ITCs) series, initiated in
2002, is to address the common UCTP by incorporating practical considerations. One of the recent iterations, ITC 2019, sought to optimize
the assignment of times, rooms, and students to courses [13]. However,
the competition did not consider course schedule planning, which establishes the number of sections for each course, or the instructor
assignment problem, which determines a university’s teaching capacity.
As a result, universities intending to implement this system must first
determine the number of sections for each course and assign instructors
accordingly.
This study aims to bridge the gap between advanced models and
algorithms available in academia and the practical needs of colleges and
universities in optimizing course scheduling and instructor assignments
using historical data. The resulting schedules should meet students’
course demands with a minimum number of course sections while
maximizing instructor preferences. To achieve this, we first propose a
process-based DSS framework (detailed in Section 2) that incorporates
primary decision problems before the publication of the final schedule.
Subsequently, we introduce an integrated model for course schedule
planning and instructor assignment that generates the optimal number
of sections for each course and assigns instructors to each section to
satisfy forecasted course demands with minimal staff cost. Meeting
students’ course demands is treated as a hard constraint, while instructors’ preferences are addressed by minimizing the number of new
course preparations and the number of distinct courses they are assigned
each semester. Limiting the number of new course preparations allows
instructors to spend more time refining their existing materials and
pedagogy, thereby increasing their effectiveness in the classroom.
Similarly, reducing the number of distinct courses assigned to each
instructor during each semester fosters deeper content expertise and
reduces the cognitive load associated with switching between different
subjects, leading to improved instructional quality and higher job
satisfaction. The proposed framework is adaptable and parameterized,
allowing for adjustments in weighting to enable departments to prioritize either the minimization of distinct course sections or new course
preparations based on the collective faculty preferences.
The study makes several contributions to the UCTP literature: (1) it
proposes a process-based decision support system that simplifies the NPcomplete UCTP into two more manageable hierarchical models; (2) it
integrates the deeply interconnected tasks of course schedule planning
and instructor assignment into a single comprehensive model, efficiently
generating optimal course-section-instructor combinations from basic
inputs; (3) it considers instructors’ preferences by assigning them fewer
new courses and distinct courses, thereby minimizing their course
preparation time and enhancing teaching quality; and (4) it demonstrates the practical application of the proposed flexible model, showing
positive results in reducing staff costs and alleviating financial pressures
on universities. The practicality of the proposed model is particularly
crucial. A recent comprehensive survey of UCTP solutions in the literature indicates that many existing solutions are not viable in real-world
settings due to their limited flexibility and the impractical nature of
these methodologies [14]. Our research can assist department chairs in
efficiently planning timetables, minimizing complaints from both instructors and students, and reducing staffing costs while accounting for
various practical constraints.
The organization of the paper is as follows: In Section 2, the proposed
process-based DSS framework is presented. In Section 3, the related

literature on UCTP is reviewed. In Section 4, the integrated model of
course schedule planning and instructor course assignment is introduced. Section 5 utilizes a case study from a large public university in
the United States to validate the proposed model. The proposed solution
is analyzed and compared with the actual course schedule and instructors’ assignment in the subsequent academic year. Finally, in Section 6, conclusions and directions for future research are presented and
discussed.
2. Process-based decision support system framework
In response to the complex NP-complete nature of the UCTP, which
involves the intricate process of determining course sections, instructor
assignments, and the allocation of classrooms and timeslots, this study
introduces a process-based DSS that effectively decomposes the UCTP
into two more manageable sub-models. This approach facilitates a more
structured method for addressing the complexities inherent in the
timetabling process, as shown in Fig. 1.
Initially, course demands are forecasted by leveraging current student enrollment and historical course registration data. Employing
advanced data mining and predictive modeling techniques can enhance
the accuracy of these predictions [15]. Nonetheless, predicting course
demands is a complex undertaking as factors such as changes in the
economy, demographics of the student population, students’ individual
preferences, and unexpected events such as natural disasters or public
health emergencies can influence course demands [3]. Furthermore,
these uncertainties are more pronounced when predicting demand for
classes for new incoming students. Fortunately, a certain degree of inaccuracy in demand prediction is tolerable, as subsequent instructor and
classroom assignments can offer flexibility by accommodating some
margins of error in demand prediction.
Subsequently, the course schedule planning problem is considered to
determine the optimal number of sections for each course in the upcoming academic year given the forecasted course demands. Inputs
encompass the number of students eligible to register for each course,
the proportion of qualified students registering for each course, the
threshold for opening a new section, the maximum capacity for each
section, and courses scheduled in the same semester of the previous
academic year, among other factors. The output of this model, the
number of sections for each course, serves as input for the instructor
assignment problem.
Additional inputs include the number of full-time faculty members,
the courses taught by each faculty member in the prior academic year,
the qualifications of each faculty member to teach specific courses, each
faculty member’s annual teaching load, the minimum required percentage of course sections taught by full-time faculty, and other pertinent factors. The output of the instructor assignment problem, which is
the primary focus of this study, is the course-section-instructor combination, which subsequently serves as input for the timeslot and classroom assignment problems. In the event that the available full-time
faculty members cannot fully staff all course sections, administrators
may need to consider additional strategies. These strategies could
include hiring adjunct instructors from a pool of qualified candidates,
negotiating overload assignments with full-time faculty (with appropriate compensation upon mutual agreement), or, in rare cases,
canceling course sections. The specific strategy adopted by a university
will depend on its unique situation and requirements, which may vary
from one institution to another. While these decisions are ultimately the
responsibility of university administrators and fall outside the direct
scope of the proposed decision support system, they represent important
considerations in the broader context of university course scheduling.
Owing to the high interdependence between the two aforementioned
problems, they should be optimized concurrently. The integrated optimization of highly interactive decision layers has demonstrated
remarkable performance in manufacturing and supply chain systems
[16,17]. In the present study, we propose an integrated optimization
2

G. Xue et al.

Decision Support Systems 187 (2024) 114345

Fig. 1. Overview of the University Course Timetabling Problem (UCTP) and the decomposition into sub-models for the DSS.

model for the Course Schedule Planning and Instructor Assignment
problems, denoted as CSPIA, in the planning horizon of one academic
year to satisfy the forecasted students’ demand for courses. The model
defines and minimizes the number of new courses and sections of
distinct courses to be taught by faculty members, as these necessitate
considerable preparation and may not align with their teaching preferences. The integrated model determines the optimal number of sections
for each course and optimally assigns full-time faculty to teach each
section in the fall and spring semesters of the subsequent academic year
based on their teaching expertise (or preference) and other qualifications. The output of our model, the course-section-instructor combination, effectively bridges the gap between UCTP literature and practical
applications in academia.
Subsequently, the timeslot assignment part of the model determines
the timeslots allocated to course section and instructor combinations,
considering factors such as the number of work days per week, the
number of timeslots per work day, the number of times each course
meets per week, and the minimum and maximum work days for each
faculty and course section. The output consists of section-instructortimeslot combinations.
Lastly, the classroom assignment part of the models assigns classrooms to each course section based on predetermined section-instructortimeslot combinations as well as other factors, such as the available
number of classrooms with varying capacities and the maximum seating
capacity of each classroom. If there is a shortfall in classrooms, the
timeslots of course sections must be adjusted to ensure that a classroom
is assigned to each lecture. Due to the interaction between timeslots and
classroom assignment problems, they should be optimized simultaneously. While assigning some course sections to non-traditional classrooms, such as university libraries, and converting some sections to
online instruction may alleviate the need for department-owned classrooms, it remains practical to reduce classroom requirements. Lindahl
et al. [18] recognize this as a strategic decision in UCTP.

categorized into two distinct types: master timetables and demanddriven systems [19]. Extensive surveys cover various formulations for
automated timetabling, including techniques such as graph coloring,
integer linear programming, network flow techniques, Tabu search,
rule-based approaches, and constraint logic programming [20].
A study in [14] provides a comprehensive and recent overview of the
methodologies applied to the UCTP, classifying them based on chronology and datasets. This review discusses perspectives, trends, challenges, and opportunities in UCTP, noting the popularity of metaheuristic and hybrid methodologies. It also highlights the gap between
state-of-the-art academic solutions and their practical real-world application, attributing this to their limited flexibility and inability to provide
comprehensive solutions. Table 1 summarizes the methodologies, findings, and limitations of past UCTP studies.
Considering the studies listed in Table 1, only a few address the
quantity of course sections [24–26]. The study in [24] introduces a
demand-driven, multi-objective hierarchical mathematical model for
departmental course scheduling in undergraduate courses. The generated course schedules determine which courses to offer, the number of
sections for each course, the timeslots for course sections, and the
assignment of faculty to each course section. However, the hierarchical
models are solved sequentially, disregarding the inherent interaction
between course schedule planning and instructor assignment problems,
which may affect the feasibility of the solutions in practice. Additionally,
the balance between full-time and adjunct instructors is ignored,
impacting the practicality of the solution.
The mathematical formulation of the UCTP is presented in [25] and
is solved through lexicographical optimization with four ILP subproblems solvable sequentially with CPLEX. This approach, however,
disregards instructors’ preferences for courses and timeslots, making the
solution less practical. Moreover, the hierarchical solution may affect
the feasibility of the upper-level solutions. In [26], traditional operational issues are broadened to include strategic concerns that may influence resulting timetables that cannot be altered at short notice. This
study explores two strategic decisions concerning the teaching period
problem (e.g., determining the number of timeslots or whether to add
extra timeslots) and the room planning problem (e.g., selecting which
rooms to use), which have received limited attention in the literature.
However, the instructors’ preferences are expressed as the minimum
working days and curriculum compactness, ignoring new and distinct

3. Related studies
The UCTP has garnered significant interest from both researchers
and academic administrators over the years. Comprehensive reviews of
the problem are documented in both early works [19–21] and more
recent studies [14,22,23]. The course timetabling problem is
3

G. Xue et al.

Decision Support Systems 187 (2024) 114345

Table 1
Summary of methodologies, findings, and limitations of previous UCTP studies.
Source

CSP

IA

TA

CA

[24]

X

X

X

Multi-objective MIP

[25]

X

X

Decomposed
metaheuristic
approach

[26]

X

X

X

Methodology

Bi-objective MIP

[27]

X

[28,29]

X

X

MIP

[30]

X

X

MIP

[31]

X

X

Multi-objective LP

[32]

X

X

stochastic
programming

[33]

X

X

X

IP

[10]

X

X

X

IP

[34]

X

X

MIP

[35]

X

X

Two-stage IP

[36]

X

X

IP

[37]

X

X

MIP

[38]

X

X

MIP

[39]

X

X

Simulated annealing

[40]

X

X

NA

[41]

X

X

IP

[42]

X

[3]

MIP

MIP
X

IP

Findings

Limitations

The faculty schedules can address important
priorities, such as minimizing expected course
conflicts.
The proposed sequential procedure generates
similar or better solutions with lower solution
complexity.

Models are solved sequentially, leading to potential
infeasibility of upper-level model; full-time and adjunct
instructor balance is ignored.
Instructor preference for courses is ignored and the
hierarchical solution may affect the feasibility of the upperlevel solutions.
The preferences are expressed as the minimum working days
and curriculum compactness, ignoring new course
preparation.
The section quantity for each course is fixed and the model is
not adaptable to dynamic student demands.
The section quantity for each course is fixed and the course
preference of instructors is ignored.
Hard to solve the large-scale MILP model and instructors’
preferences for courses are ignored.
The course schedule, including section quantity and
instructors that teach each section, is predetermined.
Not adaptable to dynamic course demands and doesn’t
consider course preferences of teachers.
The approach considers the preference of teachers for rooms
and timeslots but ignores that for courses.
Ignoring multiple sections of the same course and the course
preference of instructors.

The models show that the rooms, teaching periods
and timetable quality affect one another.
The results show high performance in maximizing
teachers’ preferences.
The approach improves instructor satisfaction and
utilization of rooms.
The method produces better solutions better than
the manual allocation.
The model balances the instructors’ and
administration’s preferences.
The approach with cancellation risk of courses
shows good performance.
The proposed method generates better timetables
than the current practice.
The proposed system improves use of classroom
capacity when assigning courses to classrooms.
The proposed adaptive tabu search algorithm is
effective compared with other reference
algorithms.
The proposed two-stage model can find high
quality solutions and reduce student flows between
lectures.
The obtained schedule can reduce idle periods for
students and utilize classrooms more efficiently.
The approach considers the allocation of students
to classes and assignment of rooms and time
periods to classes.
The approach assigns classes to rooms when room
capacities are drastically reduced during COVID.
The proposed solver with penalization generates
satisfactory solutions.
This paper added student sectioning to traditional
UCTP.
The multi-stage process can adjust the timetable to
satisfy the varying demands for different student
groups.
The model ensures that students choose their
preferred time slots.
The method for classroom assignment problems
offers a systematic solution.

Lack of adaptability to dynamic student demands and
instructors’ preferences for courses to teach.
Ignoring the determination of course-section-instructor
combination.
This study only assigned courses to timeslots and rooms,
ignoring the determination of course sections quantities and
instructor assignment.
The course-section-instructor combination is known in
advance and not adaptable to dynamic course demands;
instructor preference is ignored.
Instructors’ preference is not considered, and the model is
not applicable to dynamic course demands.
Lack of adaptability to dynamic demands and ignoring
instructor assignment.
Knowing the section quantity and instructor assignment in
advance.
Ignoring the assignment of instructors.
Ignoring the effects of course demands on section quantities
of each course and instructor preference.
Lack of adaptability to dynamic student demands and
instructor/timeslot availability.

Notes: CSP-course schedule planning, IA-instructor assignment, TA-timeslot assignment, CA-classroom assignment, MIP-mixed integer programming, IP-integer
programming.

course preparation.
Another stream of research focuses solely on assigning instructors,
timeslots, and/or classrooms to predetermined course sections, ignoring
the determination of the quantity of course sections to satisfy dynamic
course demands and the course preferences of instructors [10,27–34]. In
[27], a MILP model is presented that balances instructors’ load and
preferences with instructor assignment to courses with preset schedules
across two semesters, but the number of sections per course is regarded
as constant. Mixed-integer programming models for assigning timeslots
and faculty to different course sections [28,29] address gender issues
across multiple departments. While these models incorporate features
aimed at minimizing class conflicts and enhancing traffic flow, they do
not consider the number of sections per course or variations in course
demand.
Addressing the UCTP, a model proposed in [30], concurrently integrates instructor assignment and course scheduling. However, this
model, similar to [31], is unable to accommodate variations in student
demand or determine the optimal number of sections for each course,
limiting its practicality and effectiveness. The study in [32] considers

the risk of course cancellation, focusing on maximizing satisfaction for
students and professors. Yet, the proposed integrated model does not
address course schedule planning and is not adaptable to dynamic
course demands. An integrated integer programming model for generating a comprehensive timetable in a term is proposed in [33]. The aim
of this model is to minimize the violation of preferences and rules
associated with different penalties. However, it does not consider student demands and preferences for courses or the consequent impact on
the number of course sections. An integer programming model for
instructor-course-time-slot assignments is introduced in [10], addressing practical issues like back-to-back classes and inter-departmental
classroom leveling. However, this study neither considers the optimal
number of sections for each course nor accounts for variations in course
demand.
Without considering course schedule planning and instructor
assignment, several studies concentrate on assigning classrooms and/or
timeslots to predetermined course sections [34–42]. In [34], a mathematical formulation for the conventional UCTP is presented, utilizing a
hybrid Adaptive Tabu Search algorithm for its solution. Despite this, the
4

G. Xue et al.

Decision Support Systems 187 (2024) 114345

model fails to incorporate crucial elements such as course schedule
planning and instructor assignment, which detracts from its practicality.
The study in [35] proposes a two-stage model to optimize student flows
between consecutive lectures, but it also overlooks course schedule
planning related to student demands and instructor assignment. In [36],
integer programming is employed to assign groups of courses to groups
of timeslots and rooms. However, the model does not account for the
number of sections of each course, faculty assignment to courses, or the
variations in course demand. The mixed integer programming model in
[37] allocates students to classes and assigns rooms and timeslots to
classes while [38] only formulates the classroom assignment problem
into a mathematical model. However, their course-section-instructor
combination is also predetermined, making it less adaptable to dynamic course demands, and instructors’ preferences for taught courses
are ignored. The study in [39] introduces student sectioning and distribution constraints to the traditional UCTP, proposing a simulated
annealing solver to find optimal solutions. Similarly, Müller et al. [40]
integrate time slot and classroom assignment with student sectioning, an
approach inspired by the practical challenges faced in ITC 2019. In
contrast, the research in [41] focuses specifically on scheduling common
courses for students in parallel groups. Meanwhile, [42] employs data
analytics to identify key issues contributing to delayed graduations and
developed a model to optimize class scheduling, ensuring that students
could select their preferred time slots. In [3], a mixed integer programming model is proposed to assign course sections to classrooms
when room capacities are drastically reduced during COVID. However,
these studies are all constrained by a fixed course-section-instructor
combination, limiting their flexibility to adapt to changing demands
and conditions.
As shown in Table 1, the majority of the existing literature focuses on
timeslot and classroom assignment or related operational aspects, often
neglecting course schedule planning and instructor assignment. These
elements are typically viewed as predetermined when addressing UCTP.
From a methodological perspective, various approaches have been
proposed to address UCTP, as evidenced in [25,31,34]. However, recent
advances in computer software and hardware have led to increased
attention on MILP models, as highlighted in [26]. Examples include
integer programming models for classroom assignment [38], analysis of
student flows between lectures [35], and MILP models for balancing
instructor workload [27]. While these approaches offer valuable insights, they often overlook crucial aspects of course schedule planning,
such as accommodating fluctuating student demands and assigning instructors effectively. Additionally, treating the number of sections per
course as constant may limit the adaptability of solutions.
In summary, prior research has notably advanced the understanding
of the UCTP, yet they fall short in certain areas. Specifically, these
studies often overlook the variation in course requirements and the
preferences of both students and instructors. Moreover, reviewing
existing literature highlights the need for an integrated optimization
model that considers the interrelated nature of course schedule planning, instructor assignment, and student course demands, to bridge the
gap between the literature and academic practice. The present study
aims to address these limitations by proposing an integrated optimization model for course schedule planning and instructor assignment,
considering both student and instructor preferences and ensuring the
feasibility of the solutions in practice.

4.1. Entities
The key entities in the proposed integrated model of curricula design
and faculty course assignment are as follows.
Courses, Sections, and Meeting Frequency: Each course in the
schedule typically comprises one or more sections, and each section is
organized to meet one or more times a week at specified days and times.
For instance, courses that meet once a week are scheduled for 2.75 h on
either Monday, Tuesday, Wednesday, or Thursday. Conversely, courses
meeting twice a week are scheduled for 1.25 h per session, typically on
Mondays and Wednesdays or Tuesdays and Thursdays. The maximum
number of students allowed in each course section is a function of the
specific pedagogical requirements of the course and room capacity. Each
course section is assigned a timeslot that corresponds to its meeting
period.
Instructors: The model in this study includes all full-time faculty
members (both tenure-track and non-tenure-track) with predetermined
qualified courses to teach. A prevalent practice in academic institutions
is to prioritize the assignment of courses to full-time faculty to whom the
institution has a financial commitment. If available full-time instructors
are insufficient to meet all course staffing requirements, administrators
often resort to various strategies depending on their preferences and
circumstances. These strategies include tapping into a pool of eligible
adjunct instructors, negotiating overload assignments with full-time
faculty for additional compensation, temporarily increasing the capacity of some of the existing sections to reduce the number of sections if
possible, or even canceling a section in extreme cases. Depending on
their needs, requirements, policies, and available resources, each
department may adopt a different approach or a mix of these solutions to
address the problem when the capacity of their full-time faculty cannot
meet course demands. Consequently, the model in this study is primarily
focused on assigning full-time instructors.1
Students: Students are allowed to enroll in the offered course sections provided they satisfy the prerequisite requirements for each
course. Student demand for each course is estimated based on the
number of students qualified to enroll in each course during the target
academic year.
4.2. Assumptions
For the designated academic year, the model incorporates the
following assumptions, which are made without loss of generality:
• Instructors are sensitive to changes in course scheduling, particularly
when assigned to teach new or distinct courses. This assumption is
based on the reasonable belief that compared with maintaining a
consistent schedule of familiar courses, significant alterations in
course assignments can demand extra preparation and effort from
instructors, potentially impacting their satisfaction. Additionally,
reducing the number of distinct courses assigned to each instructor
fosters deeper content expertise and reduces the cognitive load
associated with switching between different subjects, leading to
improved instructional quality and higher job satisfaction.
• The teaching responsibilities of full-time faculty are distributed
evenly across semesters to facilitate efficient schedule planning. If a
faculty member’s total teaching load for the year is an even number,
it is divided equally between the two semesters. If it is an odd
number, it is split into two nearly equal parts. This predetermined

4. Model development
The proposed integrated model can simultaneously determine the
optimal number of sections of each course and the optimal sectioninstructor combination based on students’ demand for courses in an
academic year.

1

If needed, adjunct instructors can be included in the initial scheduling with
minimal modifications by adding a penalty for the number of course sections
assigned to them. Different adjuncts can be assigned varying penalties to reflect
the preference to deploy them based on such factors as qualifications and
experience.
5

Decision Support Systems 187 (2024) 114345

G. Xue et al.

distribution considers various factors, including research activities,
service commitments, and tenure status.
• There is a limit to the proportion of courses taught by adjunct faculty
in compliance with accreditation requirements.
• Each course section has a set maximum enrollment capacity, which is
determined based on the specific educational requirements of the
course.
• The number of full-time faculty remains consistent throughout the
academic year; no considerations are made for new hires or attrition.
• A single instructor teaches each course section.
• Only tenure-track faculty who are actively engaged in research are
permitted to teach graduate-level courses.
• The number of undergraduate students eligible to register for any
given course and the percentage of those who do enroll are both
predictable and can be forecasted with a high degree of accuracy.

in imbalanced considerations: α = 0 would completely ignore whether a
course assigned to an instructor has been previously taught by them, and
α = 1 may lead to the assignment of sections of several different courses
to each instructor. Moreover, we have defined a dummy instructor (i=0)
with a very large teaching capacity (i.e. l0 = M) and qualifications to
teach all courses (i.e., a0j = 1, ∀j ) to absorb all unstaffed sections,
ensuring optimization feasibility. The sum of X0js over all courses and
semesters, represents the number of course sections assigned to the
dummy instructor (i.e. unstaffed course sections). Therefore, adding the
∑J ∑2
penalty term,
j=1
s=1 M • X0js , to the objective function aims to
discourage assigning course sections to the dummy instructor unless
there is no feasible solution. If an instructor is assigned to teach the same
new course in both semesters of the academic year, the course should
not be treated as new in the second semester. Therefore, the effect of
applying a double penalty in the model should be adjusted. This is
achieved by deducting the applied penalty (i.e., α) when this scenario
occurs, indicated by Gij being equal to 1.
s. t.,
∑J ∑2
Xijs ≤ li
∀i
(2)
j=1
t=1

4.3. Notations
The notations for the integrated model CSPIA are shown in Table 2.
4.4. Model formulation

∑J
j=1

In Model CSPIA, the objective is to minimize the sum of the number
of new courses as well as sections of distinct courses assigned to full-time
faculty and the penalty of unstaffed sections:
∑I ∑J ∑2 [
] ∑J ∑2
min i=1
α • Vijs + (1 − α) • Yijs +
M • X0js − α
j=1
s=1
j=1
s=1
∑I ∑J
•
Gij
i=1
j=1

−

∑J
j=1

(
∑J

Ujs ≤

(1)

Xij1 −

Xij1 −
j=1

Xij2 ≤ 1

∑J

∀i > 0

(3)

≤ 1 ∀i > 0

(4)

)

Xij2
j=1

qjs • rjs
≤ Ujs + 1
mjs

∀j, s

(
)
M • Zjs − 1 ≤ qjs • rjs − mjs • Ujs − th < M

In this objective function, minimizing the sum of Vijs across all instructors and courses means minimizing new preparations, and minimizing Yijs across all instructors and courses translates to minimizing the
total number of distinct courses assigned to instructors. The parameter,
α, varies between 0 and 1 and is chosen based on collective faculty
preferences, where a higher α (closer to 1) places more weight on
reducing the number of new courses, and values closer to 0 put more
emphasis on reducing the number of distinct course sections. In practice,
α should not be exactly set to 0 or 1, as these extreme values would result

Wjs = Ujs + Zjs
Xijs ≥ Yijs

∀j, s

(6)

∀j, s

(7)

∀i > 0, j, s

(8)

Xijs ≤ M • Yijs
Yijs ≤ aij

(5)

∀i > 0, j, s

∀i > 0, j, s

(9)
(10)

Table 2
Notations for Model CSPIA.
Indices:
i = 0,1,2, …, I, index of full-time instructor. Index 0 represents a dummy instructor to ensure feasibility.
j = 1,2, …, J, index of course.
s = 1,2, index of semester.
Parameters:
li = fixed workload of instructor i in an academic year.
aij =1, if instructor i is qualified to teach course j; and 0 otherwise.
bij =1, if instructor i taught course j in last academic year; and 0 otherwise.
qjs = number of qualified students to register for course j in semester s.
rjs = percentage of qualified students to register for course j in semester s.
mjs = maximal number of students registering for course j in semester s.
th = new section opening threshold.
pt = minimum percentage of sections taught by full-time faculty.
n = the total number of undergraduate courses (the first n courses in all J courses are undergraduate)
α = parameter balancing between minimizing the number of new courses and distinct courses assigned to instructors
M: a large number.
Variables:
Zjs = 1, if the number of students who cannot be accommodated by Ujs sections of course j in semester s exceeds the threshold th, that is, the remainder of qjs rjs /mj is larger than or
equal to the threshold th, meaning opening a new section; and 0 otherwise.
Xijs = number of sections of course j taught by instructor i in semester s.
Auxiliary variables:
Wjs = actual number of sections of course j in semester s.
Yijs = 1, if instructor i teaches course j in semester s; and 0 otherwise.
Vijs =1, if instructor i teaches new course j in semester s; and 0 otherwise.
Ujs = lower bound of sections of course j in semester s determined by the course demand.
Gij =1, if instructor i is assigned new course j in both semesters s = 1 and s = 2; and 0 otherwise.

6

G. Xue et al.

Decision Support Systems 187 (2024) 114345

Gij ≤ Vijs

∀i > 0, j, s

(11)

∀i > 0,j

(12)

Gij ≥ Vij1 +Vij2 − 1
Wjs ≥

∑I

Wjs =

∑I

i=0

i=0

Xijs

∀s, j = 1, …, n

(13)

Xijs

∀s, j = n + 1, …, J

(14)

2
∑I ∑J ∑
i=1

j=1

X0js = Wjs −

s=1

Xijs ≥ pt •

∑I
i=1

Xijs

2
∑J ∑
j=1

s=1

∀s, j

Wjs

(15)
(16)

Yijs , Vijs , Zjs , Gjs ∈ {0, 1} ∀i > 0, j, s

(17)

Xijs , Ujs = 0, 1, 2, …

(18)

∀i, j, s

(MSBA) program, the Master of Business Administration (MBA) program, and PhD concentrations in information systems and management.
Each undergraduate major has a corresponding minor, and there are
additional minors in Leadership, Healthcare, and Military & Leadership
Studies. The diverse range of disciplines and faculty in this department
makes it an ideal setting for implementing the UCTP, whose solutions
are applicable and scalable to university systems’ scheduling needs.
Adjunct instructors and PhD students supplement the teaching workforce in undergraduate programs when needed.
The teaching qualifications and workload of the current full-time
faculty are summarized in Table 3. Model CSPIA is used to address the
integrated optimization of course scheduling and instructor assignment
for two semesters of the target academic year. The model’s output includes the maximum percentage of course sections taught by full-time
faculty and the optimal instructor assignments for these sections. During the target academic year, the M&IS department offered 45 undergraduate and 17 graduate courses, many with multiple sections. Of the
178 sections taught, full-time faculty delivered 102 course sections
(57.3 %). The College’s accrediting agency requires that at least 60 % of
sections be taught by full-time faculty (pt). Hence, the department must
carefully plan its course schedule to meet this requirement.
Graduate courses in the department are exclusively taught by tenuretrack and research-active full-time faculty. However, during fall and
spring semesters of the target year, three graduate courses (64,005,
64,036, and 64,038) were taught by doctoral-qualified, non-tenuretrack full-time faculty. Faculty workload, defined as the number of
course sections taught per academic year, is capped based on their
research productivity and service commitments. Currently, the
threshold for opening a new section is set at 4, meaning a new section is
created when student registrations exceed this number.
Courses in the PhD program vary each semester but are known in
advance and typically taught by doctoral-qualified, tenure-track fulltime faculty. The workload for these faculty members can be adjusted
when they are assigned to teach doctoral-level courses. Consequently,
doctoral-level courses are not included in our model, as their exclusion
does not significantly affect the scheduling of undergraduate courses.
This is because the teaching capacity at the doctoral level can be supplemented with adjunct instructors at the undergraduate level if
necessary.
The Course Numbers (CNs) for the target academic year, the number

Constraints (2) specify the maximum annual workload for each fulltime faculty member. Constraints (3) and (4) are the linearized versions
∑
∑J
of ∣ Jj=1 Xij1 −
j=1 Xij2 ∣ ≤ 1, representing that the difference in the
number of sections a faculty member can teach across consecutive semesters cannot exceed 1. Constraints (5) define the minimum and
maximum number of sections that should be opened each semester,
which is dependent on the course demand (calculated as total enrollment times the percentage of each student type enrolled in each course).
The parameters rjs are forecasted from historical data. Constraints (6)
dictate whether an additional section is required to meet the course
demand. If the difference rjs • pjs − mjs • Ujs (representing the number of
students unable to enroll in course j due to the capacity limitation of Ujt
sections) equals or exceeds the threshold th, then an additional section
(Zjs = 1) is to be opened.
Constraints (7) are responsible for calculating the actual number of
sections for each course that are available for registration. Constraints
(8) and (9) guarantee that if an instructor is assigned to teach one or
more sections of a course, a binary variable indicating this assignment is
set to 1; if not, it is set to 0. Constraints (10) ensure that instructors are
assigned only to courses for which they are qualified. Constraints (11)
and (12) introduce a binary variable to indicate whether an instructor is
assigned to teach the same new course in both the first and second semesters. Constraints (13) ensure that the number of undergraduate
course sections taught by instructors in each semester does not surpass
the actual number of available sections. Constraints (14) stipulate that
only tenure-track and research-active full-time faculty are eligible to
teach graduate courses. Constraints (15) define the teaching capacity
limits, mandating that the proportion of sections taught by full-time
faculty complies with the accreditation requirements for each academic year. Constraints (16) define the number of unstaffed course
sections in each semester, which are assigned to the dummy instructor.

Table 3
Faculty information.

5. Model implementation
The proposed model is implemented in the Department of Management and Information Systems (M&IS), at Kent State University (KSU) to
assist in its course schedule planning and instructor assignment in the
target academic year.

Faculty

List of Courses

Workload per
Year

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

44,285, 64,185
44,285, 64,185
44,043, 64,042, 64,082
24,163, 34,167, 44,062, 44,163, 64,042
30,062, 34,180, 44,763
24,053, 34,054, 34,070, 44,040, 44,140, 44,292
34,165, 34,180, 34,185, 64,158
34,164, 34,165, 34,180, 34,185, 44,660, 64,158
24,167, 34,036, 34,170
34,180, 44,091, 44,185, 64,271
44,192
24,056, 34,156, 34,060, 44,062, 44,152, 64,005,
64,041
34,034, 34,068, 64,005, 64,082
24,163, 34,060, 34,175, 44,062, 44,152, 44,392
24,053, 34,054, 64,005, 64,036, 64,037, 64,038,
64,060, 64,061, 64,092
24,163, 34,157, 34,158, 34,159
24,053, 34,156, 64,005, 64,011, 64,018, 64,036,
64,037, 64,038, 64,060, 64,061, 64,099
24,053, 24,165, 44,048
34,165, 34,180, 44,445,44,183, 44,292,
44,499,68,051
64,005, 64,011, 64,018, 64,060

4
5
6
4
3
12
4
5
4
5
4

12
13
14

5.1. Case introduction

15
16

In the M&IS Department, the current 20 full-time faculty, some of
whom teach across various majors, offer courses in four undergraduate
majors: Business Management (BMGT), Computer Information Systems
(CIS), General Business (GBUS), and Human Resource Management
(HRM). They also teach in the Master of Science in Business Analytics

17
18
19
20

7

6
4
8
4
1
4
6
14
4

G. Xue et al.

Decision Support Systems 187 (2024) 114345

of students eligible to enroll in these courses (as derived from teaching
and learning platforms like Blackboard), the registration percentages for
each course, and the projected course demands are all detailed in
Table 4. In the fall semester of the target year, the department offered 41
courses, while in the spring, the number of courses increased to 50.

minimizing the number of new courses assigned to instructors, whereas
a larger α emphasizes reducing the number of distinct courses per
instructor each semester. The academic year under consideration consisted of 86 sections in the fall semester and 92 in the spring. When
utilizing the proposed model CSPIA, the department could have efficiently met course demand with only 72 sections in the fall and 81 in the
spring. This reduction of 25 sections (14 %) over the year translates to an
estimated annual decrease in staffing costs of approximately $130,000.
Moreover, the percentage of sections staffed by full-time instructors
increased from 57 % (102 out of 178) to 65 % (100 out of 153), meeting
the accreditation requirements.
The benefits of using the model CSPIA extend beyond reducing the
total number of course sections and increasing the percentage of sections
delivered by full-time instructors. Notable improvements are observed
in the number of new courses and distinct course sections assigned to
full-time instructors, impacting instructor satisfaction and teaching

5.2. Model performance and results
Model CSPIA is solved with the branch-and-bound method in
LINGO18 on a Microsoft Surface Pro 4.0 computer with 8.0G RAM and
Inter (R) Core (TM) i5-6300u CPU @ 2.49 GHz processors. In the model,
there are 9052 integer variables and 16,936 constraints. The model
achieves its optimal solution in an impressively short timeframe of under
5 s.
Table 5 presents the outcomes of applying model CSPIA under three
distinct values of the parameter α. As discussed, a smaller α prioritizes
Table 4
Course registration forecast.
Fall 2019

Spring 2020

CN

MS

QS

RP (%)

RF

CN

MS

QS

RP (%)

RF

24,053
24,056
24,163
24,165
24,167
34,036
34,054
34,060
34,068
34,070
34,156
34,157
34,165
34,167
34,180
34,185
44,007
44,009
44,043
44,048
44,062
44,091
44,152
44,163
44,183
44,185
44,192
44,284
44,285
44,292
44,293
44,392
44,660
64,005
64,018
64,036
64,060
64,082
64,158
64,185
68,051

180
360
210
100
40
38
50
135
40
40
40
50
50
40
45
50
40
50
55
25
50
20
50
25
45
40
25
45
45
25
35
44
50
40
30
30
30
40
40
40
40

1527
1527
1527
187
187
150
828
993
150
150
978
200
843
150
843
843
150
473
150
150
473
100
473
473
100
100
80
100
575
93
93
473
100
60
28
88
28
88
60
60
60

24.23
13.03
33.92
23.53
14.97
16.00
11.35
32.83
24.67
26.67
4.19
17.50
20.52
22.67
25.27
10.79
12.67
7.61
36.67
3.33
21.14
11.00
22.62
19.24
56.00
53.00
16.25
20.00
33.91
45.16
37.63
14.59
44.00
90.00
121.43
51.14
103.57
32.95
58.33
18.33
46.67

370
199
518
44
28
24
94
326
37
40
41
35
173
34
213
91
19
36
55
5
100
11
107
91
56
53
13
20
195
42
35
69
44
54
34
45
29
29
35
11
28

24,053
24,056
24,163
24,165
24,167
34,054
34,060
34,068
34,070
34,156
34,158
34,159
34,164
34,165
34,167
34,170
34,175
34,180
34,185
44,007
44,009
44,043
44,048
44,062
44,140
44,152
44,163
44,187
44,192
44,284
44,285
44,292
44,392
44,395
44,445
44,492
44,499
44,763
64,011
64,037
64,038
64,041
64,042
64,060
64,061
64,082
64,092
64,099
64,158
64,185
64,271

240
320
230
100
40
50
185
30
38
40
50
50
50
60
40
30
40
60
55
40
55
40
30
50
30
50
26
25
20
40
45
20
50
10
25
20
45
38
21
30
30
35
35
30
30
40
25
25
30
40
35

1527
1527
1527
187
187
828
993
150
150
978
60
60
643
843
150
150
843
843
843
150
473
150
150
473
93
473
473
473
80
100
575
93
93
80
100
100
100
100
28
28
28
60
60
28
28
28
28
50
60
60
60

43.55
19.32
34.38
24.60
21.39
11.84
30.61
15.33
24.67
5.93
23.33
18.33
1.71
16.84
22.67
16.00
2.85
18.98
12.10
22.67
8.03
38.00
13.33
18.60
11.83
27.48
19.45
1.27
10.00
24.00
65.39
10.75
87.10
3.75
47.00
11.00
45.00
38.00
67.86
103.57
103.57
80.00
78.33
10.71
96.43
107.14
21.43
30
25.00
41.67
75.00

665
295
525
46
40
98
304
23
37
58
14
11
11
142
34
24
24
160
102
34
38
57
20
88
11
130
92
6
8
24
376
10
81
3
47
11
45
38
19
29
29
48
47
3
27
30
6
15
15
25
45

Notes: CN: course number, MS: maximum seat, QS: quantity of qualified students; RP: registration percentage, RF: registration forecast.
8

G. Xue et al.

Decision Support Systems 187 (2024) 114345

Table 5
Performance improvement of model CSPIA.
Actual value
Section quantity
Sections by full-time faculty
Remaining sections
Distinct course sections assigned to full-time instructors
New course sections assigned to full-time instructors

Model output (α = 0.01, 0.5, 0.99)

Difference

Fall

Spring

Total

Fall

Spring

Total

86
48
38
42
8

92
54
38
50
19

178
102
76
92
27

72
(50,51,51)
(22,21,21)
(30,32,33)
(4,4,3)

81
(50,49,48)
(31,32,33)
(34,33,38)
(2,1,1)

153
100
53
(64,65,65)
(6,5,5)

25
2
23
(28,27,27)
(21,22,22)

Notes: A single value for the cell under “Model output” indicates that this value remains constant for different α values.

performance. For instance, with α = 0.5, the total number of new sections assigned to instructors falls from 27 to 5, representing an 81 %
reduction. Similarly, the number of distinct course sections assigned to
full-time instructors decreases from 92 to 65, representing a 29 %
reduction. These reductions enable instructors to spend more time
engaging deeply with their courses, ultimately enhancing teaching
quality and satisfaction.
Furthermore, as the results suggest, increasing α from 0.5 to 0.99
does not yield any changes in this particular case, as the total number of
new course sections and distinct course sections assigned to full-time
instructors remains the same. The impact of variations in α on the
model’s performance is examined in more detail in the following section, particularly under different teaching load conditions. Finally,
setting α to extreme values of 0 or 1 is not recommended as discussed.
Extreme values would entirely ignore one of the model’s goals (i.e.,
reducing the number of new or distinct course sections) without substantially improving the other goal. For example, setting α to zero leads
to 64 distinct course sections assigned to instructors (the same as when α
is 0.01) but increases the number of new course sections assigned to 76,
as the model completely disregards whether an instructor has taught a
specific course before the assignment. Similarly, with α set to 1, the
number of new course sections assigned to instructors remains at 5 (the
same as when α is 0.99), but the number of distinct course sections
assigned to instructors increases to 73.
In summary, the model CSPIA offers significant benefits and improvements, including reduced staffing costs, increased percentage of
course sections delivered by full-time instructors, and enhanced
instructor satisfaction and performance by minimizing the number of
new and distinct course sections assigned.

Fig. 2. Total number of distinct course sections assigned to full-time instructors
under varying total teaching load requirements.

5.3. Impact of variations of α parameter on model performance
Fig. 3. Total number of new course sections assigned to full-time instructors
under varying total teaching load requirements.

To gain deeper insights into the model CSPIA, it is crucial to understand the trade-offs between the two goals integrated into its objective function. Specifically, it is important to understand how the total
number of distinct course sections assigned to instructors can be
exchanged for the number of new courses assigned to them under
different course demands, and vice versa. This is achieved by examining
the effect of the α parameter on the model CSPIA’s performance under
various teaching loads.
Fig. 2 shows the sum of distinct course sections assigned to full-time
instructors when hypothetically varying the number of course sections
they are required to deliver. Results are presented for three α values:
0.01, 0.5, and 0.99. As the figure demonstrates, the sum of distinct
course sections assigned to instructors increases with teaching load. For
any given teaching load, the number of distinct sections is one or two
fewer when α is 0.01 compared to 0.99. Interestingly, results for α = 0.5
are sometimes similar to the lower extreme and sometimes to the upper.
Similarly, Fig. 3 illustrates the number of new course sections
assigned to instructors under the same varying teaching loads as in
Fig. 2. Comparing the two figures reveals noteworthy insights. For
instance, when instructors are required to deliver 70-course sections,
with α = 0.01, they are assigned 36 distinct sections, while this increases

to 38 when α is 0.99. However, as shown in Fig. 3, this leads to instructors having to deliver three additional new course sections (5 with
α = 0.01 compared to 2 with α = 0.99). This difference becomes more
pronounced at a teaching load of 75 sections, where a reduction of two
distinct sections results in 4 new sections being assigned. However, the
difference in new courses assigned remains about one or two courses for
the remaining demand values.
These observations suggest that under most demand scenarios, a
decrease in the number of distinct course sections assigned to instructors
is often accompanied by a corresponding increase in the number of new
course sections they are required to teach. Understanding this relationship allows administrators to leverage the α parameter to balance
these two competing objectives in alignment with collective faculty
preferences. Furthermore, the model’s robustness to variations in α, as
evidenced by its consistent performance across different α values, enhances its usability and practicality. This means that administrators can
achieve desirable outcomes with the model CSPIA without extensive
fine-tuning or precise parameter optimization, thereby streamlining the
9

G. Xue et al.

Decision Support Systems 187 (2024) 114345

decision-making process and facilitating the efficient allocation of
instructional resources.

satisfaction, highlighting its potential value for academic departments
facing similar scheduling challenges.

5.4. The impact on timeslot and classroom assignments

6.2. Contributions to research

While the primary objective of the proposed model CSPIA is to
optimize the assignment of instructors to course sections, the resulting
output serves as a critical input for the subsequent phase of academic
scheduling. Notably, the allocation of timeslots and classrooms to each
section is contingent upon the determination of course-section instructor
combinations, underscoring the pivotal role of the model’s output in the
comprehensive scheduling process.
Moreover, the model’s emphasis on minimizing the number of sections through efficient scheduling significantly contributes to the subsequent timeslot and classroom assignment problem. A reduced number
of sections not only streamlines the scheduling process but also enhances
flexibility in assigning optimal timeslots and classrooms. Furthermore,
instructors assigned to new courses or those with a higher number of
distinct courses are prioritized in the selection of their preferred timeslots and classrooms. This prioritization recognizes the additional
preparation required for new courses and the challenges associated with
managing a diverse course load, promoting a more equitable and satisfactory scheduling outcome for instructors.

The first theoretical contribution is the introduction of a novel
process-based decision support system (DSS) framework that decomposes the complex UCTP into two manageable hierarchical optimization models. The higher-level model generates course-sectioninstructor combinations to meet forecasted demands and minimize instructors’ preparation. The lower-level model then assigns timeslots and
classrooms to these combinations. This approach ensures courses, sections, and instructor assignments are optimized, prioritizing instructors
with new or many distinct courses for preferred timeslots and classrooms, thereby enhancing overall fairness and satisfaction. Decomposing a complex NP-hard UCTP problem into manageable hierarchical
problems that can be solved sequentially is particularly advantageous as
it reduces computational complexity without sacrificing performance.
Moreover, it provides insights into different steps of the solution,
allowing for user interventions and modifications if necessary.
The second contribution is the conceptualization and formulation of
an integrated optimization model that simultaneously addresses course
schedule planning and instructor assignment, filling a critical gap in the
existing literature. This integration is crucial for generating feasible
solutions, as the number of course sections and the availability of
qualified instructors are inherently interdependent. Each course section
must be taught by a qualified instructor, necessitating an integrated
approach to generate feasible solutions for both models. To the best of
our knowledge, this is the first study to integrate course schedule
planning and instructor assignment problems in UCTP. Prior studies
either ignored one of them [10,25–33] or both [3,34–38], leading to
potentially infeasible course schedule when assigning instructors. By
incorporating both aspects into a joint optimization framework, the
proposed model enhances the practicality and applicability of UCTP
solutions in real-world academic settings. The final theoretical contribution of this study lies in formulating a multi-objective optimization
framework that seeks to prioritize instructors’ preferences by minimizing the number of new courses assigned to them and minimizing the
number of distinct courses assigned to them during each semester.
Although these two objectives may not always be optimized simultaneously, the proposed optimization framework allows administrators to
balance these competing objectives based on the collective preferences
of the instructors.

6. Conclusions and future work
6.1. Overview and key findings
The ideal DSS framework for addressing the UCTP is expected to
provide a solution that encompasses the comprehensive scheduling of
courses, sections, instructors, timeslots, and classrooms. Due to the
inherent complexity and unique characteristics of UCTP, this study
proposed a novel process-based DSS framework that simplifies the UCTP
by breaking it into two more manageable hierarchical models. The
upper-level model, which was also the primary focus of this study, is an
integrated model addressing course schedule planning (determining the
number of sections per course) and instructor assignment (assigning
instructors to sections) to minimize costs and maximize instructor
satisfaction by seeking to minimize the number of new and distinct
course sections assigned to them during each semester. The lower-level
model would address timeslot and classroom assignments.
Departing from much of the existing literature, which often focuses
on assigning instructors, timeslots, or classrooms to pre-determined
course sections [18,21,28,34], this study proposed a novel mixedinteger linear programming (MILP) model to integrate course schedule
planning and instructor assignment, aiming to meet the forecast demands for courses over two consecutive semesters (fall and spring). The
model was successfully applied to a real-world UCTP setting within a
multi-disciplinary academic department at a large U.S. public university. The model’s focus on minimizing instructor course preparation and
its integration of common departmental constraints suggest applicability to other institutions. Results demonstrated a potential reduction of
up to 14 % in the number of sections (approximately $130,000 in savings), an increase in the percentage of course sections taught by full-time
faculty from 57.3 % to 66 %, and reductions of up to 81 % in new course
assignments and 29 % in the number of distinct courses assigned to
instructors. These combined benefits contribute to significant cost savings, improved resource allocation, and enhanced instructor satisfaction
and performance.
Further analysis examined the trade-offs between minimizing new
course assignments and reducing the number of distinct courses per
instructor using the α parameter. The impact of varying α on model
performance was investigated under different teaching loads, providing
insights into balancing these competing objectives. In summary, the
proposed model CSPIA offers a practical and effective solution for universities in cost reduction, resource allocation, and instructor

6.3. Contributions to practice
In addition to its theoretical contributions, this study introduces
several practical advancements that directly address the needs of academic institutions. The proposed DSS framework is a user-friendly,
interactive tool that bridges the gap between theoretical models and
practical application, effectively catering to the specific instructional
needs of academic institutions. Distinctively, this research is the first to
prioritize the practical concerns of instructors, in contrast to previous
studies that predominantly focused on optimizing course preferences,
which often led to scheduling conflicts. Our approach centers on two key
objectives for instructors: minimizing the number of new course preparations and reducing the number of distinct courses assigned each semester. The proposed DSS framework is parameterized, allowing
institutions to balance these objectives based on the collective preferences of their faculty, thereby facilitating a flexible tradeoff between the
two goals.
The proposed DSS further enhances fairness and instructor satisfaction by decomposing the scheduling problem into two hierarchical
models. The higher-level model determines the offered courses, their
sections, and identifies instructors assigned to new or multiple distinct
courses. These instructors are then prioritized in the lower-level model
10

G. Xue et al.

Decision Support Systems 187 (2024) 114345

to select their preferred timeslots and classrooms.
A major challenge in the development of DSS for UCTP has been the
lack of practicality and user-friendliness. Many existing solutions have
failed to gain widespread acceptance due to these limitations [14].
However, the DSS framework developed in this study has been successfully implemented and evaluated within a large department at a
public university in the United States. Implementing this DSS not only
led to a substantial 14 % reduction in staffing costs, equivalent to
approximately $130,000 annually, thereby alleviating financial pressures on the university, but also yielded significant improvements in
instructor satisfaction. The number of new course sections assigned to
instructors decreased by up to 81 %, and the number of distinct courses
assigned to instructors was reduced by 29 %. These reductions in course
preparation burden and cognitive load directly contribute to improved
instructional quality.
Beyond these tangible benefits, the proposed DSS is notable for its
ability to improve both student and instructor satisfaction by addressing
course demands and preferences, resulting in a more optimized and
effective learning environment. Its user-friendly interface, seamless
integration with existing systems, and reliance on readily available input
data further enhance its practicality and ensure widespread adoption
within academic institutions.

Visualization, Validation, Software, Resources, Methodology, Investigation, Formal analysis, Data curation, Conceptualization. O. Felix
Offodile: Writing – review & editing, Writing – original draft, Visualization, Validation, Supervision, Software, Resources, Project administration, Methodology, Investigation, Formal analysis, Data curation,
Conceptualization. Rouzbeh Razavi: Writing – review & editing,
Writing – original draft, Validation, Supervision, Resources, Project
administration, Methodology, Investigation. Dong-Heon Kwak:
Writing – review & editing, Writing – original draft, Visualization,
Validation, Supervision, Resources, Project administration, Investigation. Jose Benitez: Writing – review & editing, Writing – original draft,
Visualization, Validation, Supervision, Resources, Project administration, Investigation, Funding acquisition.
Declaration of competing interest
None of the authors has any financial or personal relationships that
influenced the development of this work.
Data availability
Data will be made available on request.

6.4. Limitations

Acknowledgments

This study is not without limitations. Firstly, the study relies on
forecasts to determine the number of students for each course. These
forecasts may not be entirely accurate, particularly for courses taken by
new students joining the college, such as freshman or first-year graduate
courses. This issue is exacerbated by unexpected changes, such as pandemics or rapid economic shifts, which can significantly impact enrollment. Additionally, factors like the introduction of new majors or
minors, or the termination of existing ones, which are not explicitly
considered in this study, can also affect course enrollments.
Despite these limitations, it is important to note that the proposed
solution in this study demonstrates some resiliency against student
enrollment forecasts, provided the forecast deviation is not so substantial that it necessitates the addition of an extra section or the cancellation of a section due to significant under-enrollment. Furthermore, while
the benefits of deploying the proposed solution were benchmarked using
data from a department in a public US university, it would be advantageous to benchmark these benefits in other settings, such as smaller
private universities or academic institutions in other countries. While we
believe that the core principles underlying the solution are adaptable
and generalizable, evaluating the proposed solution in more diverse
settings would provide a more comprehensive understanding of its potential advantages.

We want to thank for the research sponsorship received by the
Government of Spain and the European Regional Development Fund
(European Union) (Research Projects PID2021-124725NB-I00,
PID2021-124396NB-I00, and TED2021-130104B-I00).
References
[1] S. Maldonado, J. Miranda, D. Olaya, J. Vasquez, W. Verbeke, Redefining profit
metrics for boosting student retention in higher education, Decis. Support. Syst.
143 (2021) 113493.
[2] E.N. Maltz, K.E. Murphy, M.L. Hand, Decision support for university enrollment
management: implementation and experience, Decis. Support. Syst. 44 (1) (2007)
106–123.
[3] C. Cardonha, D. Bergman, R. Day, Maximizing student opportunities for in-person
classes under pandemic capacity reductions, Decis. Support. Syst. 154 (2022)
113697.
[4] N. C. for Education Statistics, Postsecondary institution expenses, retrieved 25 Oct
2023, from, https://nces.ed.gov/programs/coe/indicator/cue, 2023.
[5] Stanford University, Finances. https://facts.stanford.edu/administration/finances/
, 2022.
[6] J. Miranda, P.A. Rey, J.M. Robles, A web architecture based decision support
system for course and classroom scheduling, Decis. Support. Syst. 52 (2) (2012)
505–513.
[7] S. Even, A. Itai, A. Shamir, On the complexity of timetable and multicommodity
flow problems, SIAM J. Comput. 5 (4) (1976) 691–703.
[8] J.S. Tan, S.L. Goh, G. Kendall, N.R. Sabar, A survey of the state-of-the-art of
optimisation methodologies in school timetabling problems, Expert Syst. Appl. 165
(2021) 113943.
[9] K. Schimmelpfeng, S. Helber, Application of a real-world university-course
timetabling model solved by integer programming, OR Spectr. 29 (2007) 783–803.
[10] C. Martin, Ohio university’s college of business uses integer programming to
schedule classes, Interfaces 34 (6) (2004) 460–465.
[11] J. van den Broek, C. Hurkens, G. Woeginger, Timetabling problems at the tu
Eindhoven, Eur. J. Oper. Res. 196 (2009) 877–885.
[12] N. Pillay, A survey of school timetabling research, Ann. Oper. Res. 218 (1) (2014)
261–293.
[13] T. Muller, H. Rudova, Z. Mullerova, University course timetabling and
international timetabling competition 2019, in: Proceedings of the 12th
International Conference on the Practice and Theory of Automated Timetabling
(PATAT-2018) vol. 1, 2018.
[14] M.C. Chen, S.N. Sze, S.L. Goh, N.R. Sabar, G. Kendall, A survey of university course
timetabling problem: perspectives, trends and opportunities, IEEE Access 9 (2021)
106515–106529.
[15] D. Delen, A comparative analysis of machine learning techniques for student
retention management, Decis. Support. Syst. 49 (4) (2010) 498–506.
[16] G. Xue, O.F. Offodile, Integrated optimization of dynamic cell formation and
hierarchical production planning problems, Comput. Ind. Eng. 139 (2020) 106155.
[17] X. Zheng, M. Yin, Y. Zhang, Integrated optimization of location, inventory and
routing in supply chain network design, Transp. Res. B Methodol. 12 (2019) 1–20.
[18] M. Lindahl, A.J. Mason, T. Stidsen, M. Sorensen, A strategic view of university
timetabling, Eur. J. Oper. Res. 266 (1) (2018) 35–45.

6.5. Future research extensions
This study serves as a foundation for several potential research extensions. First, the model’s scope can be expanded by incorporating
additional features such as faculty recruitment and retention, as well as
the impact of reduced teaching capacity due to factors like layoffs or
sabbaticals. Second, the integration of advanced predictive analytics
techniques, such as artificial neural networks, can be explored to
enhance the accuracy and precision of course demand forecasts based on
historical enrollment and external data. Finally, implementing functionalities that allow for conducting what-if analyses under various
future demand scenarios can provide insights into the model’s sensitivity and robustness, thereby enabling more informed decision-making
regarding course offerings and resource allocation.
CRediT authorship contribution statement
Guisen Xue: Writing – review & editing, Writing – original draft,
11

G. Xue et al.

Decision Support Systems 187 (2024) 114345
From 2017 to 2021, he worked at Kent State University as an Adjunct Professor and
research scholar. His research interests span the fields of Operations Research, Business
Analytics, and Information Systems (IS). Much of his research has been on the optimization
of manufacturing systems, university timetabling, and analytics in healthcare and mobile/
website usage patterns. He is also interested in the impact of cybersecurity curiosity and
goal setting on goal attainment and performance in cybersecurity training. His studies
were published in the International Journal of Production Economics, Computers & Industrial
Engineering, Big Data, and Journal of Medical Internet Research.

[19] M.W. Carter, G. Laporte, Recent developments in practical course timetabling, in:
Second International Conference on Practice and Theory of Automated
Timetabling, PATAT 97 vol. 545, Springer-Verlag, Berlin, Heidelberg, 1997,
pp. 3–19.
[20] A. Schaerf, A survey of automated timetabling, Artif. Intell. Rev. 13 (1999) 87–127.
[21] E.K. Burke, S. Petrovic, Recent research directions in automated timetabling, Eur.
J. Oper. Res. 140 (2) (2002) 266–280.
[22] J.S. Tan, S.L. Goh, G. Kendall, N.R. Sabar, A survey of the state-of-the-art of
optimisation methodologies in school timetabling problems, Expert Syst. Appl. 165
(2021) 113943.
[23] S. Ceschia, L. Di Gaspero, A. Schaerf, Educational timetabling: problems,
benchmarks, and state-of-the-art results, Eur. J. Oper. Res. 308 (1) (2023) 1–18.
[24] J. Boronico, Quantitative modeling and technology driven departmental course
scheduling, Omega 28 (3) (2000) 327–346.
[25] J. Van den Broek, C. Hurkens, G. Woeginger, Timetabling problems at the TU
Eindhoven, Eur. J. Oper. Res. 196 (3) (2009) 877–885.
[26] M. Lindahl, A.J. Mason, T. Stidsen, M. Sorensen, A strategic view of university
timetabling, Eur. J. Oper. Res. 266 (1) (2018) 35–45.
[27] B. Domenech, A. Lusa, A MILP model for the teacher assignment problem
considering teachers’ preferences, Eur. J. Oper. Res. 249 (3) (2016) 1153–1160.
[28] S.M. Al-Yakoob, H.D. Sherali, Mathematical programming models and algorithms
for a class-faculty assignment problem, Eur. J. Oper. Res. 173 (2) (2006) 488–507.
[29] S.M. Al-Yakoob, H.D. Sherali, A mixed-integer programming approach to a class
timetabling problem: a case study with gender policies and traffic considerations,
Eur. J. Oper. Res. 180 (3) (2007) 1028–1044.
[30] A. Gunawan, K.M. Ng, K.L. Poh, A hybridized lagrangian relaxation and simulated
annealing method for the course timetabling problem, Comput. Oper. Res. 39 (12)
(2012) 3074–3088.
[31] N.A. Ismayilova, M. Sagir, R.N. Gasimov, A multiobjective faculty-course-time slot
assignment problem with preferences, Math. Comput. Model. 46 (7) (2007)
1017–1029.
[32] P. Yasari, M. Ranjbar, N. Jamili, M.-H. Shaelaie, A two-stage stochastic
programming approach for a multiobjective course timetabling problem with
courses cancelation risk, Comput. Ind. Eng. 130 (2019) 650–660.
[33] K. Schimmelpfeng, S. Helber, Application of a real-world university-course
timetabling model solved by integer programming, OR Spectr. 29 (2007) 783–803.
[34] Z. Lü, J.-K. Hao, Adaptive tabu search for course timetabling, Eur. J. Oper. Res. 200
(1) (2010) 235–244.
[35] H. Vermuyten, S. Lemmens, I. Marques, J. Beliën, Developing compact course
timetables with optimized student flows, Eur. J. Oper. Res. 251 (2) (2016)
651–661.
[36] M. Dimopoulou, P. Miliotis, Implementation of a university course and
examination timetabling system, Eur. J. Oper. Res. 130 (1) (2001) 202–213.
[37] E. Rappos, E. Thiémard, S. Robert, J.F. Hêche, A mixed-integer programming
approach for solving university course timetabling problems, J. Sched. 25 (4)
(2022) 391–404.
[38] A.E. Phillips, H. Waterer, M. Ehrgott, D.M. Ryan, Integer programming methods for
large-scale practical classroom assignment problems, Comput. Oper. Res. 53
(2015) 42–53.
[39] K. Sylejmani, E. Gashi, A. Ymeri, Simulated annealing with penalization for
university course timetabling, J. Sched. 26 (5) (2023) 497–517.
[40] T. Müller, H. Rudová, Z. Müllerová, Real-world university course timetabling at the
International Timetabling Competition 2019, J. Sched. (2024) 1–21.
[41] E. Steiner, U. Pferschy, A. Schaerf, Curriculum-based university course timetabling
considering individual course of studies, CEJOR 21 (2024) 1–38.
[42] M. Chen, X. Huang, H. Chen, X. Su, J. Yur-Austin, Data driven course scheduling to
ensure timely graduation, Int. J. Prod. Res. 61 (1) (2023) 336–361.

O. Felix Offodile is a Professor in the Department of Information Systems & Business
Analytics at Kent State University. His research and teaching interests cover business
analytics, operations management, robotics and technology assessment, cellular
manufacturing, supply chain management, and inventory management. His research
publications have appeared in the International Journal of Production Research, International
Journal of Production Economics, Technometrics, European Journal of Operational Research,
IIE Transactions, Journal of Manufacturing Systems, OMEGA, and Robotics and Computer
Integrated Manufacturing.
Rouzbeh Razavi is an Associate Professor in the Department of Information Systems and
Business Analytics at Kent State University. His academic career, commencing in 2017 at
Kent State University, follows a series of professional roles in the industry. He served as the
Director of Group Decision Sciences at the Commonwealth Bank of Australia in New York
City and as a Senior Scientist in the Advanced Analytics Department at SAP. Earlier in his
career, Dr. Razavi served as a Research Scientist at Bell Labs for several years. His contributions to the field are marked by over 70 scholarly publications and 30 international
patent applications.
Dong-Heon (Austin) Kwak is an Associate Professor of IS at the Department of Information Systems and Business Analytics, Kent State University. He received his Ph.D. in IS
from the University of Wisconsin-Milwaukee, USA. His research focuses on cyberbullying,
cyberloafing, persuasion, gamification, and IT training. His research has been published in
the Journal of the Association for Information Systems, European Journal of Information Systems, Information & Management, Internet Research, Computers in Human Behavior, and
Computers & Education.
Jose Benitez is a Professor of IS, Department Chair of Information Systems and Business
Analytics, and the Bridgestone Endowed Chair in International Business at the Ambassador
Crawford College of Business and Entrepreneurship, Kent State University, Kent, Ohio,
USA. His research interests cover the impact of digitalization on companies and individuals and the development of theory and quantitative research methods in IS research.
His research has been published in about 60 papers in leading journals including MIS
Quarterly, Information Systems Research, Journal of Operations Management, Production and
Operations Management, Journal of Management Information Systems, Journal of the Association for Information Systems, European Journal of Information Systems, Journal of Information Technology, Information & Management, Decision Support Systems, Decision Sciences, and
Journal of Business Research. Jose was recognized as an Association for Information Systems (AIS) Distinguished Member Cum Laude in July 2021 and received the AIS Sandra
Slaughter Service Award in December 2022. He currently serves as a Senior Editor of the
European Journal of Information Systems, Information & Management, and Decision Support
Systems and as an Associate Editor of the Journal of the Association for Information Systems.
He also serves as an Editorial Review Board member for Information Systems Research. In
addition, Jose has served as a Guest Editor of Decision Sciences. His teaching interests and
instructional expertise cover managing digital business transformation, digital innovation,
the business value of digital technologies, IT management, IT strategy, theory development, and quantitative research methods in IS research at graduate and undergraduate
levels. Jose is a passionate speaker who enjoys working with students, colleagues, and
executives to positively impact the business world and society. He has also provided
consulting services and worked on IT development and digital transformation projects
with many leading companies worldwide. Jose can be contacted at jbenite1@kent.edu.

Guisen Xue is a Ph.D. Student in the Department of Information Systems and Business
Analytics at Kent State University, Kent, Ohio, USA. He received a B.S. in Industrial Engineering in 2004 and his Ph.D. in Systems Engineering in 2012 from Beihang University.

12

