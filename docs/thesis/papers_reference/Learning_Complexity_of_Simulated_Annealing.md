Learning Complexity of Simulated Annealing

arXiv:2003.02981v2 [cs.LG] 29 Jun 2020

Avrim Blum∗

Chen Dan†

Saeed Seddighin‡

Abstract
Simulated annealing is an effective and general means of optimization. It is in fact inspired
by metallurgy, where the temperature of a material determines its behavior in thermodynamics.
Likewise, in simulated annealing, the actions that the algorithm takes depend entirely on the
value of a variable which captures the notion of temperature. Typically, simulated annealing
starts with a high temperature, which makes the algorithm pretty unpredictable, and gradually
cools the temperature down to become more stable.
A key component that plays a crucial role in the performance of simulated annealing is
the criteria under which the temperature changes namely, the cooling schedule. Motivated by
this, we study the following question in this work: “Given enough samples to the instances of a
specific class of optimization problems, can we design optimal (or approximately optimal) cooling
schedules that minimize the runtime or maximize the success rate of the algorithm on average
when the underlying problem is drawn uniformly at random from the same class? ”
We provide positive results both in terms
of sample complexity and simulation complexity 1 .
√
e m) samples suffice to find an approximately optimal
For sample complexity, we show that O(
e 1/3 )
cooling schedule of length m. We complement this result by giving a lower bound of Ω(m
on the sample complexity of any learning algorithm that provides an almost optimal cooling
schedule. These results are general and rely on no assumption. For simulation complexity,
however, we make additional assumptions to measure the success rate of an algorithm. To
this end, we introduce the monotone stationary graph that models the performance of simulated
annealing. Based on this model, we present polynomial time algorithms with provable guarantees
for the learning problem.

∗
Toyota Technological Institute at Chicago, supported in part by the National Science Foundation under grants
CCF-1733556, CCF-1800317, and CCF-1815011.
†
CMU, supported in part by the National Science Foundation under grant CCF-1800317.
‡
Toyota Technological Institute at Chicago, supported in part by the National Science Foundation under grants
CCF-1733556 and CCF-1535795.
1
We call the overall runtime of the algorithm that determines the cooling schedule the simulation complexity

1

Introduction

The goal of this work is to better understand how we can design efficient simulated annealing
(SA) algorithms. Simulated annealing is a well-known heuristic method to tackle hard problems.
Term annealing originates from thermodynamics, referring to the way that metals cool and anneal.
Instead of the energy of the material, simulated annealing utilizes the objective function of an
optimization problem. Surprisingly, the implementation of SA is very simple as it is very similar to
hill-climbing. The only difference is that instead of picking the best move in every step, simulated
annealing picks a random move. If the selected move improves the quality of the solution, then the
move is always accepted. Otherwise, the algorithm makes the move anyway with some probability
less than 1. The probability decreases exponentially with the badness of the move, which is the
amount by which the solution is worsened. This is shown by ∆(E). One example of the annealing
criteria is given below:
Pr[ accepting a downhill move at time step i] ≃ 1 − e∆(E)/ti .
where parameter ti is the temperature of the algorithm at step i which is used to determine
this probability. The ti parameter is analogous to temperature in an annealing system at time step
i. At higher values of temperature, downhill moves are more likely to occur. As the temperature
tends to zero, they become more and more unlikely, until the algorithm behaves more or less
like hill-climbing. In a typical SA optimization, the temperature starts at a high value and is
gradually decreased according to a cooling schedule. Simulated annealing is used for a broad class
of computational problems ranging from SAT to travelling salesman problem, to VLSI routing, etc.
as experiments strongly support the efficiency of simulated annealing in practice [3, 14].
Indeed the efficiency of an SA algorithm significantly depends on its cooling schedule [1, 4, 14,
15, 16, 19, 20, 21, 23]. One simple cooling schedule is to start with a single temperature t0 and
decrease the temperature linearly with a rate of α to obtain lower temperatures gradually. We
use this simple cooling strategy to present illustrating examples, nonetheless we consider a more
generalized setting in this work. The literature has also gone beyond simple cooling schedules and
several non-linear methods have been proposed so far [1, 4, 14, 15, 16, 19, 20, 21, 23]. It is not hard
to imagine that even for different instances of the same problem, the optimal cooling schedules may
vary significantly.
Therefore in this work, we take a learning approach towards designing simulated annealing
algorithms, using the PAC-style model for data-driven algorithm design introduced in [11] and
used to analyze a wide range of important families of algorithms and heuristics in [5, 6, 7, 8]. In
brief, we consider a distribution D over a specific class of instances of a presumably hard problem
(such as SAT) and aim to design near-optimal cooling schedules for such instances, analyzing both
sample complexity (the number of instances from D we need to observe) and simulation complexity
(runtime) needed for learning. Our approach is particularly motivated by the work of [8].

1.1

The Learning Problem

As aforementioned, an SA algorithm makes a random walk on the nodes of a search graph. Each
node of this graph represents a potential (not necessarily optimal) solution for the underlying problem and the energy of a node is a value reflecting how close this solution is to an optimal solution.
We assume that for each node, its energy and neighbors are available via oracle queries. One thing
to keep in mind is that the number of nodes in this huge search graph may be exponentially large
and that we only have local views on the nodes of the graph. For instance, when the underlying

2

problem is SAT, we may have 2k nodes where k is the number of variables in the SAT problem and
each node represent an assignment of true/false to the variables.
Crucial to any cooling schedule are the parameters that maximize its performance. This could be
as simple as just a real value specifying the cooling rate or as complicated as a sequence of variables
determining the exact value of the temperature at every step. Take for instance, the simplest case
in which a parameter t0 and linear cooling rate α formulate the temperature at every step. In this
case, at step i, ti = t0 (1 − αi) formulates the temperature. Therefore, the learning algorithm has to
find the optimal pair (t0 , α) that maximizes efficiency. It is an easy exercise to see that the learning
problem is actually not very challenging in this case. Although this simple formulation involves
infinitely many (t0 , α) pairs that need to be searched over, via careful discretization techniques,
one can narrow down the set of possible (t0 , α) pairs to polynomially many candidates and iterate
over them to find the optimal cooling schedule2 . Samples are used to determine how well each
cooling schedule performs in practice. More precisely, samples are used to approximate the score
of a cooling schedule.
However, we go beyond linear cooling schedules and include more sophisticated systems (i.e.,
non-linear cooling schedules). Our setting is pretty general: we denote the cooling schedule by
a vector E = ht1 , t2 , . . . , tm i where m is the number of steps our algorithm takes and ti specifies
the temperature at time i. Any non-increasing sequence of values makes a valid cooling schedule.
The problem becomes more challenging with this representation; Even after discretizing the temperatures, still there are exponentially many cooling schedules and determining an approximately
optimal schedule is non-trivial.
Recall that each node of the search graph corresponds to a potential solution for the underlying
problem. In case of SAT for instance, each node can be an assignment of the true/false values to
the variables. We label a subset of nodes in the search graph as acceptable solution nodes. These
nodes correspond to solutions that are acceptable for the underlying problem. In the case of SAT,
a node whose corresponding solution satisfies all of the clauses is a solution node. The score of an
SA algorithm with a specific cooling schedule is the likelihood of reaching an acceptable solution
node after a fixed number of steps. We would like to point out that although a reasonable energy
function for the nodes of the search graph gives higher energies to the acceptable solution nodes,
we make no particular assumption on the energies in our setting. We remark that if the cooling
schedule is available, it is computationally easy to evaluate the score of the algorithm. We run the
SA algorithm according to the cooling schedule and once it terminates we find out if the solution
found by the algorithm is acceptable for the problem. By repeating this process enough times, we
can estimate the score of the cooling schedule very accurately.
Indeed the optimal parameters may vary for different problems or even for different instances of
the same problem and therefore we need to also incorporate the problem instances in our setting.
To illustrate the importance of the cooling schedule, consider the example shown in Figure 1.1. In
the example shown in Figure 1.1, there is one solution node (colored in red) which has an energy of
3n and the search graph consists of a clique of vertices with distinct energies one of whose vertices
has a path to the solution node. The energies of the nodes of this path are increasing. Let us
assume that the initial state of the algorithm is the node colored in green. It is easy to verify that
an extreme strategy that never accepts downhill moves has zero chance of reaching the solution
node and another extreme strategy that always accepts all downhill moves requires a cubic number
of steps to reach the solution node. However, a strategy that accepts each downhill move with
probability 1/2 only requires O(n2 ) steps in expectation to reach the solution node.
Motivated by this example, we define our general problem in the following way:
2

This improvement comes with a small error to the quality of the solution.

3

2

1

2n

3

2n − 1

4

..

..
n−2

n−1

n

2n + 1

2n + 2

2n + 3

2n + 4

...

3n

Figure 1: A search graph with 3n nodes is illustrated in this figure. The numbers on the nodes
show their energy or in other words goodness of the nodes. In this example, we consider the red
node to be the only solution of the problem.
Let D be a distribution over a specific class of instances3 of a hard problem (such as SAT).
Denote the set of valid (combination of) parameters for the SA algorithm by F = {E1 , E2 , . . . , }.
Moreover, let for an instance I ∼ D and a set of parameters E ∈ F, score(I, E) be a function that
reflects how well an SA algorithm with parameters E works on instance I. This is basically the
likelihood of finding a solution, if our SA algorithm uses E as its cooling schedule. Our goal is to
find a set of parameters E ∈ F that maximizes efficiency. In other words,
EI∼D [score(I, E)]
is (approximately) maximized.
We clarify the notation by a simple example. Let us go back to the basic setting in which
we formulate the temperature at each step with a pair (t0 , α). In this case, F = R+ × (0, 1/m)
would be the set of all valid parameters. Moreover, a natural example for score is the probability
of finding a correct solution after a given (say m) number of steps. This way, the problem is to find
a temperature t0 and a cooling rate α that maximize the success probability after performing m
moves of SA. Our attention in this work is focused on an even more general setting. We denote the
cooling schedule by a sequence of non-increasing temperatures ht1 , t2 , . . . , tm i for a fixed m. Thus,
in our setting we have F ⊆ (R+ )m subject to the temperatures being non-increasing. For simplicity,
and without loss of generality, we assume that the energies of the nodes are integer numbers in
range {1, 2, . . . , emax }.
Any SA algorithm basically makes a random walk on a search graph in which every node
represents a potential/partial solution for the problem. For instance, when the underlying problem
is SAT, every node of the search graph is a true/false assignment to the variables of the program.
The energy of each node is a local guess on how well that solution satisfies the goals of the problem.
For the case of SAT for instance, one simple energy function for a node is the number of clauses the
corresponding solution satisfies. In our setting, we make no assumption on the energy of the nodes
though in practice we expect that a higher energy signals a better solution. Since an SA algorithm
3

For instance industrial instances of SAT.

4

makes a random walk, its state at every step can be shown via a distribution over the nodes of
the search graph. Initially, this distribution shows the likelihood of each node being used as the
starting solution and as the algorithm proceeds, the distribution changes based on the criteria of
the random walk. The final state of the algorithm represents the likelihood of each node reported as
the final solution. Thus, we wish the final distribution of our algorithm to be highly concentrated
on the solution nodes.
We evaluate our learning algorithm based on two quantities: sample complexity and simulation
complexity 4 . The former measures the number of samples one needs in order to find an (approximately) optimal cooling schedule and the latter measures the runtime of the learning algorithm in
order to find an optimal cooling schedule.

1.2

Our Results and Techniques

Our main results are concerned with the sample complexity of the learning problem. As a typical
challenge for learning problems, we have to face the issue that the space of the problem is infinitely
large as there are infinitely many cooling schedules for an SA algorithm. In order to prove a
bound on the sample complexity, the first step is to show that by losing a small additive error, we can bound the space of the solutions to a finite set. We begin by explaining this in Section 2.
Step 1: From infinity to linear: In this step, we show that although the space of the problem
is infinitely large, only a polynomial number of samples suffice to approximate the optimal solution
within desirable guarantees. This step is quite classic as discretization is the typical approach to
bound the solution set.
Recall that m is the length of the random walk in the search graph. We show in Section 2 that
e
O(m)
samples from the distribution suffice to approximate the optimal cooling schedule within a
e hides the polylogarithmic factors (both in terms of m and emax ).
small additive error. Notice that O
This basically gives an almost linear upper bound on sample complexity based on the number of
steps of the algorithm.
Roughly speaking, the total number of samples we need in order to approximate the optimal
cooling schedule is logarithmic in terms of the number of candidate solutions we have. Initially,
the space of cooling schedules is infinitely large, however, a discretization technique can reduce the
e
space of candidate solutions to 2O(m) many. More precisely, we define a discretized temperature
e
set T whose size is O(m)
and show that there is an almost optimal solution that only uses the
e
temperatures in T . This reduces the space of candidate solutions to (O(m))m ≤ 2O(m) which
e
implies that the sample complexity is bounded by O(m).
The only non-trivial part of the above analysis is to show that a discretized set of temperatures
e
with size O(m)
is enough to approximate the optimal cooling schedule within an arbitrarily small
additive error. Let us fix an ǫ > 0 and assume that the goal is to construct a discretized set of
temperatures T such that there is a cooling schedule that only uses the temperatures of T and
its score is at most ǫ smaller than the optimal solution. One convenient way to construct such
a set is to make sure for each t > 0 there is a t′ ∈ T such that for any 1 ≤ x ≤ emax we have
′
|e−x/t − e−x/t | ≤ ǫ/m. Then we can imply that if we replace every temperature ti of the optimal
solution with its corresponding t′i of the discretized set, each step we make a different decision with
probability at most ǫ/m and thus the total error is bounded by ǫ. That is, with probability 1 − ǫ
our algorithm traverses the exact same path as had we not modified the optimal cooling schedule.
4
This is equivalent to the notion of running time if we assume that our SA procedure halts after a polynomial
number of steps.

5

It is not hard to prove that such a condition can be met by having O(m log emax ) elements in |T |
which gives us an almost linear bound on the sample complexity.
Theorem 2.1, [restated informally]. For any ǫ > 0, the sample complexity of approximating the
eǫ (m).
learning problem within an additive error of ǫ is bounded by O

Up to this point we show that an almost linear number of queries is sufficient for approximating
an optimal cooling schedule. This raises two questions: i) Can we improve the bound such that the
dependence on m is subpolynomial? In particular, do polylogarithmically many samples suffice for
our purpose? ii) If the answer to the first question is negative, can we prove a linear lower bound
on the sample complexity? As we show in the following, the answer to both questions is negative!

Step 2: A polynomial lower bound: We present a negative answer to the first question.
Although this step gives us a lower bound, our improved upper bound is actually inspired by
this lower bound. The first attempt to prove a lower bound is to understand the limit of the
discretization technique explained above. Therefore, we ask the following question: “assuming that
our algorithm first constructs a discretized set of temperatures and then seeks to find an optimal
solution that only uses the discretized temperatures, how many samples do we need?” Indeed, the
answer to this question does not imply a lower bound in general, but it does give us an insight into
the problem which leads to a general lower bound.
To answer the above question, we need to understand what is the smallest set T of temperatures
that can be used to make a cooling schedule whose score is very close to the optimal solution? The
e √m), otherwise the
search graph shown in Figure 2 proves that |T | should be at least as large as Ω(
guarantee may not hold.
In the search graph of Figure 2, we set m′ = m/100. For a fixed τ , we set x in a way that
−x/τ
e
= 1/2, that is if the temperature is equal to τ the probability of making a downhill move is
exactly equal to 1/25 . The goal of this search graph is to start the SA algorithm from the initial
node and the only acceptable solution node is the final node.
√

m′ + 1

initial
0

0

x

2x

3x

0

x

2x

3x

final
0

...

...

√
( m′ − 1)x

√

m′ x upper path

√
( m′ − 1)x

√

m′ x

lower path

Figure 2: The search graph is depicted for a fixed temperature τ . x = τ ln 0.5 is chosen in a way
that e−x/τ = 1/2 holds.
5

For now, we assume x can be an arbitrary real number but this comes without loss of generality.

6

The search graph of Figure 2 is particularly interesting because of the following observations: i)
A cooling schedule of length m only having temperature τ is guaranteed to reach the final node with
high probability. ii) A cooling schedule of length m that does not contain any temperature in range
e −1/2 )), τ (1 + Ω(m
e −1/2 ))] has very little chance to reach the final node. As a consequence,
[τ (1 − Ω(m
if the multiplicative distance between two consecutive temperatures in our discretized set is more
e −1/2 ), one can delicately design such a search graph for which our discretization
than 1 + Ω(m
performs poorly while the optimal solution gets a score close to 1. This implies that the size of the
e √m) to prove a bound.
discretized set has to be at least Ω(
e √n) samples6 ,
While the above argument shows that our specific algorithm definitely needs O(
it does not give a lower bound in general. However, we show in Section 4 with a slightly more
e 1/3 ) samples from the distribution in
advanced analysis that any algorithm requires at least Ω(m
order to guarantee a non-trivial bound. While the heart of the proof is based on the same search
graph, in order to extend the observation to all algorithms, we slightly lose on the exponent of m
in the lower bound.
Theorem 3.3, [restated informally]. Any learning algorithm that approximates the solution within
e 1/3 ) samples from the distribution.
an additive error of 0.5 needs at least Ω(m
Before proceeding to the third step, we would like to note an implication of this result in the
context of simulated annealing. There have been several attempts in the literature to understand
the complexity of simulated annealing. One question asked in the literature from both theoretical
and practical standpoints is if there is a meaningful difference between Simulated Annealing and
the Metropolis Algorithm [12, 26]. Metropolis is a special case of simulated annealing where the
temperature does not change by time. That is the cooling schedule repeats a single temperature
m times. While this observation was made previously, our lower bound also implies that (from a
theoretical standpoint) there is a meaningful difference between the two algorithms as Metropolis
can be learned with much fewer samples which shows there are cases for which simulated annealing
performs much better. Another example is when the temperature drops linearly for which the
sample complexity is small. More generally, this lower bound actually shows a gap between SA
and any special case of SA whose cooling schedule has complexity smaller than m1/3 . For instance,
it shows that an extended version of Metropolis that uses m1/3−ǫ many different temperatures in
the cooling schedule is not competitive with the general SA algorithm.
Step 3: From linear to sublinear: Perhaps the more surprising result of this paper is that
e √m). Our algorithm is almost identical to the one
the sample complexity can be improved to O(
e √m).
explained in Step 1 except that we construct a smaller set T whose size is bounded by O(
Then
we argue that the total number of cooling schedules with this temprature set is bounded by
e √
e √m).
2O( m) which leads to sample complexity O(
The first pointer to this result is that there is no clear way to improve the lower bound of Step 2.
Keep in mind that for the lower bound, we construct a search graph for which a particular cooling
e −1/2 ),
schedule works well, but if we multiply (or divide) each temperature by a small factor 1+ Ω(m
the score of the algorithm drops significantly. Obviously, if one comes up with a better search graph
e −1/2−ǫ ) breaks the solution, then it shows that it is
for which a multiplicative factor of 1 + Ω(m
e √m) with the discretization technique. Failure to make
impossible to obtain an upper bound of O(
a better bad instance brings us to the possibility that maybe massaging each temperature by a
e −1/2 ) cannot hurt the score of the cooling schedule significantly.
multiplicative factor of 1 + O(m
We show that this is indeed the case!
6

See the proof of Theorem 4.2 for more details.

7

Recall that in Step 1, in order to prove that the discretized cooling schedules perform almost
optimally, we show that there is a discretized cooling schedule that behaves the sames as the optimal
cooling schedule with probability 1 − ǫ. That is, in the unlikely event of making a different decision
(we call it a mistake) we give 0 credit to our discretized cooling schedule, yet we prove that the
score is pretty close to that of the optimal. Clearly, this is a loose upper bound as we do not expect
to lose too much by making a single mistake.
We illustrate the idea with a toy problem. Consider a complete binary tree of depth m. The
root has depth 0 and the leaves have depth m. Each leaf is attributed to a score which is either 0
or 1. The score of each non-leaf node is the average of the scores of its children. In other words,
if we make a random walk towards the leaves with equal probability of going to each child, the
score of a node is equal to the probability of reaching a leaf with score 1 using the random-walk.
Let us call this even-random-walk and consider a different type of random-walk, namely unevenrandom-walk. The uneven-random-walk is pretty much the same as the even random walk, except
that at some depth i uniformly drawn from [1, m], an adversary may change the decision of which
child to go to. The toy-problem is to understand how much the score of a node hurts by replacing
even-random-walk by uneven-random-walk.
To study this, we attribute to each node a deviation value which is equal to the absolute value
of the difference between the scores of it children. This roughly captures an upper bound of the
score we lose, if we traverse the edges of that node with a different criteria (other than 1/2, 1/2).
Thus, we need to know what is the average deviation values of the nodes in an even-random-walk?
This roughly tells us how much we lose in the score, if an adversary changes the criteria of the walk
at some random point!
√
The upper bound on the answer is O(1/ m) no matter how the leaves are scored. It goes
beyond the scope of this paper, but we mention the idea in the hope that it helps a mindful
reader decipher some of steps that we take in the proof of Lemma 4.1. Define a deviation function
f (x) : [0, 1] → [0, 0.25] = x − x2 . One can show by induction that starting from each node v of
√
depth i, the average sum of deviations in a random walk is bounded by O((f (sv ) + (m − i)/m) m)
where sv is the score of node v (obtained via even-random-walk).
The toy problem illustrates that in the event that our optimal solution makes decisions with
√
probability 1/2, 1/2 (which is indeed the case for our lower bound), we can afford to make O( m)
mistakes and not lose much in the average score. This does not hold if the decisions are made
with different probabilities. To see this, consider the case that only the rightmost leaf has a score
1 and the rest of the leaves have scores 0. Moreover, the probability of going to the right child in
the random walk is 1 − ǫ/m and the probability of going to the left child is ǫ/m. In this case, the
average deviation is Ω(1) when we start from the root and make a random walk according to the
probabilities.
The next observation is that when the decisions are not necessarily 1/2, 1/2 say p, 1 −
p, multiplying the temperature by a factor of 1 + x changes the probabilities by at most
max{ln 1/p, 1} min{p, 1 − p}x (see Observation 4.5). That is, as the probabilities deviate from
1/2, the probability of making a “mistake” drops linearly. More precisely, the multiplicative term
√
min{p, 1 − p} gives us extra power to deal with these situations. For instance, if p < 1/ m or
√
e
when we multiply the
p > 1 − 1/ m then the probabilities change by an additive error of O(1/m)
−1/2
e
temperature by a factor of 1 + O(m
). This error is tolerable since we can afford to have an
error of ǫ/m for each decision we make.
The proof is based on the above ideas but the analysis is quite involved and rather cryptic
by nature. We show in Section 4 that if the temperatures in the discretized set are at most
e −1/2 ) away from each other (multiplicative), then one can make a cooling schedule by the
1 + O(m
discretized temperatures whose score is arbitrarily close to that of the optimal solution. This then
8

e √m) on the sample complexity of the problem.
can be used to obtain an upper bound of O(

Theorem 4.2, [restated informally]. For any ǫ > 0, the sample complexity of approximating the
eǫ (√m).
learning problem within an additive error of ǫ is bounded by O

The second part of the paper is concerned with the computational aspects of the learning
problem. Although we prove that the sample complexity is polynomial without any assumptions,
it seems that extra assumptions are necessary for the runtime concerns. Notice that we make no
assumption on the underlying problem and the only information available to us when we sample an
instance of the problem is a huge search graph containing exponentially many vertices. Even if we
bring the underling problem into the setting, it is not clear how we can make use of the conditions
of a problem such as SAT to find the right cooling schedule. Keep in mind that the complexity of
the underlying problem is the reason we use simulated annealing in the first place. Therefore, we
introduce a stylized model to make the problem more tractable. We call our model the monotone
stationary graph. Although the model relies on extra assumptions, it features nice properties that
make it particularly suitable for our purpose.
First, it gives a compact representation for every instance of the problem. Up to this point, we
treated each problem instance as a huge search graph with exponentially many vertices which is
too big to store in the memory let alone optimizing the solution over it. Our model represents the
search graphs in a more efficient way. Next, notice that even if we fix a well-defined representation
for a search graph, one should be able to recover the new representation of a problem instance
without spending too much time (and of course without taking a complete look at the already
exponentially large search graph). Our model makes it possible to recover the stationary graph in
polynomial time. Finally, the any model used for our problem has to give us enough structure so
that finding an approximately optimal cooling schedule becomes polynomially tractable in the new
setting. This is the most important feature of our model.
In our model, we represent each instance of the problem as a graph. Vertices of this graph
correspond to the temperatures in our discretized set. Intuitively, for a temperature t ∈ T , its
corresponding vertex in the graph represent the state of an SA algorithm that runs infinitely many
steps with temperature t. Thus, when the state of our algorithm is close to such a stationary
distribution, we assume that our algorithm is pointing at the corresponding vertex in the monotone
stationary graph. We draw edges between the vertices to specify how many steps we need to take
in the SA algorithm to move between the stationary distributions. Since in our model, the state of
an algorithm can be approximated with a node in this graph, we can also determine its score by
examining the corresponding stationary distribution.
Therefore, given n instances of the underlying problem, our goal is to find a cooling schedule
that obtains the highest average score for these instances by our model. We consider the following
three settings and provide a solution for each one of them: 1) identical-paths: in this setting, we
assume that the optimal cooling schedule traverses the same path for all n instances. 2) separatepaths: in this setting, we allow the optimal solution to use different paths for different instances. 3)
separate-paths + all-satisfied: This is a special case of the second setting where we know that there
exists a cooling schedule of length m that is optimal for all instances and brings us to the last node
for each monotone stationary graph.
To obtain polynomial time solutions, we introduce the notion of an (α, ǫ)-approximate cooling
schedule. In such a solution we allow the cooling schedule to violate the size constraint by a factor
of α with the promise that its score is no more than ǫ smaller than the score of the optimal cooling
schedule of length m. With this notation, we present computational results shown in Table 1.2.
We assume throughout this paper that the scores improves as energy increases. Also, a downhill
9

move is a move which hurts the energy of a node and thus is accepted with some probability smaller
than 1. However, whenever the score of a node does not hurt in a move, such a move is always
made.
Sample complexity

e √m)
Upper bound:
O(
e √m)
Ω(
Lower bound:
(for our discretization approach)
e 1/3 )
Lower bound:
Ω(m
(for any learning algorithm)
Simulation complexity
identical paths
separate paths
separate paths + all-satisfied
exact solution
exact solution (O(log n|T |), 0) approximation
in time
in time
in time
n
poly(m, n, |T |)
poly(m, n, |T | )
poly(m, n, |T |)
Table 1: In the computational results, T is the set of the discretized temperatures and n is the
e √m) and
number of sampled used in the learning algorithm. We show in Section 2 that |T | = O(
e √m) is almost without loss of generality but we treat them as separate parameters for the
n = O(
sake of generality.

2

Discretization and Sample Complexity

In this section, we give an analysis for the sample complexity of the problem. Recall that, for any
problem instance I and any sequence of m temperatures E = ht1 , t2 , . . . , tm i, we define score(I, E)
to be the probability of finding an acceptable solution of I using temperatures in E. We say E is
ε-approximately optimal, if EI∼D score(I, E) ≥ supE ′ EI∼D score(I, E ′ ) − ε. That is, no other cooling
schedule of the same length can achieve a significantly higher success rate. Our goal is to prove
that learning an ε-approximately optimal cooling schedule only requires a polynomial number of
i.i.d. samples from D.
One of the difficulties in finding near-optimal cooling schemes is that there are infinitely many
e
options available. We show that by discretizing the temperatures into O(m/ε)
different values, we
only lose an additive error of ε in the success rate when running the algorithm on any instance of
the problem. Note that, we are not making any assumptions yet: we only rely on the fact that the
algorithm is evaluated based on the success rate. Discretizing the temperature makes designing
efficient algorithms possible too as we will show in Section 7. Our main result is an upper bound
e √m) for the sample complexity which is explained in details later in Section 4. Here we start
of O(
e
as a warm-up by giving an upper bound of O(m).
Theorem 2.1. The sample complexity of computing
 an ε-approximately optimal cooling schedule
with length m is bounded by O ε−2 m log( meεmax ) .

Proof. Recall that we assume that the energies of the nodes are in set {0, 1, 2, · · · , emax }. The
proof can be divided into the following steps:
• We start by showing that it is possible to discretize the temperatures to T =
{d1 , d2 , d3 , . . . , d|T | }, such that for any sequence of m temperatures E = ht1 , t2 , . . . , tm i, there
10

exists a sequence of m discrete temperatures E ′ = ht′1 , t′2 , . . . , t′m i ∈ T m , such that
|score(I, E) − score(I, E ′ )| ≤ ε/3
for any instance I of the problem. In other words, the discretized temperatures preserve the
score approximately.
• Then, we show the sample complexity of learning an ε/3-approximately optimal temperature EOPT in T m is polynomial. This is achieved by standard concentration results in finite
hypothesis space since T m has only a finite number of cooling schedules.
• Finally, we conclude that EOPT is ε-approximately optimal in Rm
≥0 .
ε
Define a parameter δ in a way that (1 − δ)m = 1 − ε/3, that is, δ = Θ( m
). We first construct
our discretized temperatures as T = T1 ∪ T2 ∪ · · · ∪ Temax , where

Tj = {

j
| ∀ integer 1 ≤ i ≤ ⌈1/δ⌉}.
ln(1/(iδ))

(1)

Roughly speaking, this discretization has the nice property that for any 1 ≤ j ≤ emax , set
{ej/t | ∀t ∈ Tj } evenly divides [0, 1]. Therefore, for each temperature t, we can find a nearest neighbor e
t in T defined as
e
t := arg min t − e
t ,
t∈T

which implies ej/et − ej/t ≤ δ for any 0 ≤ j ≤ emax . Notice that the value of ∆(E) in our SA

algorithm is always in range {0, 1, . . . , emax } and thus for t and e
t, e∆(E)/t and e∆(E)/et are always
within an additive range of δ regardless of the value of ∆(E). Our key observation is that for any
′
′
′ ′
sequence E = ht1 , t2 , . . . , tm i ∈ Rm
≥0 , there exists a sequence of m temperatures E = ht1 , t2 , . . . , tm i ∈
m
′
T , such that running the simulated annealing algorithms with discrete temperature in E keeps
the trajectories the same as E with probability at least 1 − δ. To this end, we define t′i = tei .
Assuming the two runs share the same randomness, then these two runs are the same at each step
with probability at least 1 − δ. We only need to check the correctness for two cases, when a move
is a downhill move or a uphill move.
For an uphill move, the correctness is obvious since both runs accept the move with probability
′
1. For a downhill move, the accepting probability are e∆(E)/ti and e∆(E)/ti , respectively. By
choosing t′i = e
ti , the difference is at most
′

|e∆(E)/ti − e∆(E)/ti | ≤ δ.

(2)

Therefore, we have proved that for each step, the two runs are the same with probability 1 − δ,
hence they remain the same at all steps with probability at least (1 − δ)m = 1 − ǫ/3. Assuming the
score function is bounded in [0, 1], then the scores are different with at most 1 when the two runs
are different. Hence, the expectation of difference is upper bounded by
|score(I, E) − score(I, E ′ )| ≤ 1 − (1 − δ)m =

ε
3

Next, we will show that finding a near-optimal cooling schedule in T m requires polynomial sample
complexity. The technique is based on standard Hoeffding and union bounds. We define n as the
upper bound on the number of samples and let I1 , I2 , · · · , In be n problem instances sampled i.i.d.
11

from D and S be a uniform distribution over {I1 , I2 , · · · , In }. For a given sequence of temperatures
E ∈ T m , by Hoeffding’s Inequality we have 7
|EI∼D score(I, E) − EI∼S score(I, E)| ≤
2

ε
3

2

with probability at least 1 − e− 9 nε . Therefore, by union bound, this inequality holds for all
2
2
E ∈ T m with probability at least 1 − |T |m e− 9 nε . Since we would like this event to happen with
high probability, we wish to give a value to n to make sure
2

2

1 − |T |m e− 9 nε ≥ 1 − m−10

(3)

Define EOPT(S) = arg minE∈T m EI∼S score(I, E) be the empirically best discretized cooling schedule,
and EOPT(D) = arg minE∈T m EI∼D score(I, E) be the population best discretized cooling schedule.
Condition on the two events above, we have:
EI∼D score(I, EOPT(S) ) − sup EI∼D score(I, E) = EI∼D score(I, EOPT(S) ) − EI∼S score(I, EOPT(S) )
E∈Rm
≥0

+ EI∼S score(I, EOPT(S) ) − EI∼S score(I, EOPT(D) )

+ EI∼S score(I, EOPT(D) ) − EI∼D score(I, EOPT(D) )

+ EI∼D score(I, EOPT(D) ) − sup EI∼D score(I, E)
E∈Rm
≥0
ε ε
ε
≥ − + 0 − − ≥ −ε
3
3 3
Hence, we have proved
EI∼D score(I, EOPT(S) ) ≥ sup EI∼D score(I, E) − ε

(4)

E∈Rm
≥0

In other words, OPT(S) is ε-approximately optimal.
2
Sample complexity: we need to set n in a way that meets Inequality (3), i.e. |T |m e−cnε ≤
m−10 . Therefore, we have


memax 
n = Θ ε−2 m log(|T |) = Θ ε−2 m log(
) .
ε

The dependence of the above bound on emax is logarithmic which is loose when emax can obtain
exponentially large values. We show that this can be further improved. More precisely, we show
2
max )
max )
) = Θ( m log(e
). Therefore,
this by a more careful construction of T , such that |T | = Θ( m log(e
δ
ε
we can improve the upper bound on the sample complexity to




m log(emax )
−2
−2
n = O ε m log(|T |) = O ε m log
.
ε
S
We construct the discretized temperatures as T = j∈J Tj , where J = {1, (1 + δ), (1 + δ)2 , (1 +
δ)3 , · · · , emax } and Tj defined as (1). In order to improve the sample complexity, it suffices to show
that for each temperature t there is a e
t in T such that
e

e∆(E)/t − e∆(E)/t ≤ O(δ)

7

Hoeffding’s Inequality: Let X1 , X2 , · · · , Xn ∼i.i.d. P and Xi ∈ [0, 1], then | n1

with probability at least 1 − 2e

−2nε2

12

Pn

1
i=1 Xi − E[ n

Pn

i=1 Xi ]| ≤ ε holds

holds for all and ∆(E) ∈ [0, emax ].
By the definition of J, there always exists a j ∗ ∈ J, such that ∆(E) ≤ j ∗ ≤ (1 + δ)∆(E).
Recall that our discretization has the nice property that for any j ∈ J, set {ej/t | ∀t ∈ Tj } evenly
∗
∗
divides [0, 1]. Therefore, there exists a e
t ∈ Tj ∗ , such that |ej /t − ej /et | ≤ δ.
Using Observation 4.4, now we can bound the difference e∆(E)/et − e∆(E)/t :
e

e

∗

e

∗

e

∗

∗

e∆(E)/t − e∆(E)/t ≤ e∆(E)/t − ej /t + ej /t − ej /t + ej /t − e∆(E)/t
j∗
j∗
− 1) + δ + O(
− 1)
∆(E)
∆(E)
=O(δ)

≤O(

and the rest of the proof remains the same.
Corollary 2.2 (of Theorem 2.1). The sample complexity
of computing
an ε-approximately optimal


m log emax
−2
) .
m log(
cooling schedule with length m is bounded by O ε
ε

13

3

Lower Bound

This section is dedicated to proving a lower bound for the sample complexity of any algorithm.
Similar to our upper bound, our lower bound is also very general and without any assumptions.
We show that any algorithm that approximates the optimal schedule within a small additive error
e 1/3 ) samples from the distribution.
requires at least Ω(m
e 1/3 )
The overall idea of the proof is summarized in the following. We construct l = |L| = Ω(m
different search graphs L = {s1 , s2 , . . . , sl }. Our construction has a nice property that each search
graph requires a certain sequence of temperatures to be present in the cooling schedule in order
to find a desirable solution after at most m steps. We refer to such sequences as keys. For each
search graph, having its key in the cooling schedule guarantees that the search graph is traversed
successfully with high probability when we use that cooling schedule. However, the length of each
key is smaller than m which allows us to bring multiple keys in an almost optimal solution. The keys
are designed in a way that they do not share any elements in common. That is, a temperature used
for a key specific to a search graph offers little benefit to the other search graphs. Our distribution
e
D is a uniform distribution over a subset LD ⊆ L which contains Θ(l)
(but much smaller than
l) search graphs from L. The crux of the argument is that by knowing LD , one can construct a
sequence of size m which includes all the keys of the search graphs in LD that achieves a score close
e
to 1 on average. However, LD is unknown to the learner and if we draw fewer than Ω(l)
samples,
there is no hope to get any score more than 0.1. Therefore, any learning scheme needs at least
e = Ω(m
e 1/3 ) samples from the distribution to report an approximate solution.
Ω(l)
Let c = 100 be a large constant. Recall that m is the length of the optimal solution. We define
e 2/3 ) which determines both the width of each gadget and the size of the key
a parameter m′ = Θ(m
√
for each gadget. More precisely, we set the width of each gadget to m′ and the size of the key for
each gadget to 2cm′ . Let us first explain how each gadget is constructed and then show how the
gadgets can be used to prove a lower bound on the sample complexity.
√

m′ + 1

initial
0

0

x

2x

3x

0

x

2x

3x

final
0

...

...

√
( m′ − 1)x

√

m′ x upper path

√
( m′ − 1)x

√

m′ x

lower path

Figure 3: The search graph is depicted for a fixed temperature τ . x = τ ln 0.5 is chosen in a way
that e−x/τ = 1/2 holds.
Each gadget is made for a specific temperature. We fix the temperature to be τ and construct
the corresponding gadget, namely G(τ ) in the following way: As shown in Figure 3, our gadget is
constructed of two identical paths. In the upper path, the first node has an energy of 0 and has
14

√
an outgoing edge to the second vertex. For the next m′ − 2 vertices, vertex i + 1 has an energy
of ix and three outgoing edges:
√ 1) two edges to vertex i and one edge to√vertex i + 2. Finally, the
last node has an energy of m′ x and has two outgoing edges to vertex m′ . x = (ln 1/2)τ is set
in a way that when the temperature is equal to τ the probability of accepting a downhill move is
exactly equal to 1/2.
The lower path is constructed exactly the same way as the upper path. To connect the two paths
together, we put an edge from the last node of the upper path to the last node of the lower path.
Finally we add two dummy nodes to the search graph. The first dummy node has a single outgoing
edge to the first vertex of the upper path and the second dummy node has a single incoming edge
from the first node of the lower path. The goal of the gadget is to start from the first dummy node
and reach the second dummy node. We call the first and the second dummy nodes the initial and
final nodes respectively.
We define the key K(τ ) to be a sequence of size 2cm′ only containing temperature τ . As shown
in Lemma 3.1, starting from an arbitrary node of G(τ ) and running the SA algorithm on cooling
schedule K(τ ) our algorithm ends at the final node with probability at least 0.9.
Before bringing the proof, we state an observation for which we provide a proof in the appendix.
Observation 3.1. Let c = 100, x0 = 0 and x1 , x2 , . . . , xk be k variables constructed in the following
way:

xi−1 − 1 with probability pb ,

xi−1
with probability ps ,


xi−1 + 1 with probability pf .
Then we have:

(i). For pb = ps = pf = 1/3 we have max{xi } ≥

p

k/c + 2 with probability at least 0.95.

√

ck log k with probability at least 1 − 1/k2 .
√
′
′
√ k , pf ≤ 1/3− c log
√ k , ps = 1−pb −pf we have max{xi } <
(iii). For any k′ ≤ k, pb ≥ 1/3+ c log
k′ /2
′
′
k
k
with probability at least 1 − 1/k′2 .
(ii). For pb = ps = pf = 1/3 we have max{xi } <

Lemma 3.1. An SA algorithm that starts from any node of G(τ ) and runs on cooling schedule
K(τ ) ends at the final node with probability at least 0.9.
Proof. We prove the lemma for an SA algorithm that starts from the initial node. Indeed this
implies the lemma for any other starting node since in order to reach the final node, one needs to
traverse all nodes of the search graph starting from the initial node.
To this end, we show that after cm′ steps our SA algorithm reaches the last node of the lowerpath with probability at least 0.95. With a similar analysis, one can show that starting from the
last node of the lower-path, after cm′ steps our algorithm reaches the final node with probability
at least 0.95 after cm′ steps. Then, by applying the union bound, we imply that after 2cm′ steps,
our algorithm reaches the final node with probability at least 0.9.
From here on, our aim is to prove that starting from the initial node, our algorithm reaches
the last node of the lower-path with probability at least 0.95 after cm′ steps. Notice that since
the temperature is always equal to τ , in every step, our node in the search graph gets closer to
the destination with probability at least 1/3 and get farther from the destination with probability
at most 1/3. Due to Observation 3.1 (item (i)) after cm′√steps, with probability at least 0.95 at
some point the number of times we go forward is at least m′ + 2 more than the number of times
we go backward which means we reach the last node of the lower-path. This implies that with
15

probability at least 0.95 our algorithm reaches the last node of the lower-path after cm′ steps. A
similar analysis proves that the next cm′ steps take us to the final node with probability at least
0.9 which implies that 2cm′ steps suffices to reach the final node with probability at least 0.9. 
We also show that any cooling schedule needs a certain amount of temperatures close to τ to
reach the final node with a considerable probability.
′

m
temperatures
Lemma 3.2. Let E be a cooling schedule of length m containing no more than 4c log
2
m′
√

′

2

√

′

′

2

′

√ log m , τ m +c
√ log m ]. If an SA algorithm starts from the initial node and runs
in range [τ m −c
m′
m′
with cooling schedule E, the probability that it reaches the final node is at most 0.1.

Proof. The intuition behind the proof is the following: For the upper-path, we would like to go
to the right and thus a low temperature is desirable. For the lower-path however, since we would
like to go to the left, we would like the temperature to be as high as possible. The key point is
that in the cooling schedule, the temperatures are decreasing, thus either all the temperatures we
use for traversing the upper-path are at least τ or all of the temperatures we use for traversing the
lower-path are bounded by τ . Any one of the two events makes it unlikely to get a high score.
We assume w.l.o.g that we would like to traverse the upper-path with temperatures higher
m′
than τ . Notice however that except for 4c log
temperatures, all the rest are more than τ by a
2
m′
√

2
′
m′ +c
√ log m . Since we strictly favor lower temperatures, the most desirable
m′
√
2
′
m′ +c
m′
√ log m followed by
temperatures
τ
cooling schedule in this case is a sequence of m − 4c log
2
′
′
m
m
m′
temperatures
τ
.
We
show
that
it
is
still
very
unlikely
to
traverse
the
upper-path
using this
2
4c log m′

multiplicative factor of

sequence.
To keep the analysis simple, we avoid the edge cases and assume that the goal is to start from
the second vertex and never go back to the first vertex. This way, the probability of going forward or
going backward only depends on the temperature and does not depend on the current vertex. If the
temperature is equal to τ then with probability
pf = 1/3 we go forward and with probability pb =
√

2
′
m′ +c
√ log m we go backward and with probability at
m′
′
′
√ m we go forward with probability at most pf ≤ 1/3− c log
√ m . Due to Observation
least pb ≥ 1/3+ c log
m′
m′
√
2
′
m′ +c
m′
√ log m ,
steps
with
temperature
τ
or
m
steps
with
temperature
τ
3.1, if we proceed 4c log
2
′
′
m
m
√
′2 . Thus,
e
our position does not improve by more that m′ /2 with probability at least 1 − O(1)/m

1/3 we go backward. If the temperature is τ

√
′2 .
e
in total the amount of improvement is bounded by m′ with probability at least 1 − O(1)/m
The above analysis fails when we bring in to the setting the first node of the upper-path since
the probability of going to the right at this node is more than other nodes. However, we make the
following argument: in order to traverse the upper-path, at some point we reach the second node
of the upper-path and never go back. Let us say this happens at step i. Thus, from step i on,
we never go backwards and therefore all the probabilities are only a function of the temperature
(and not the current node). The downside however, is that there are m different possible choices
for i which multiplies the bad event probability
√ by m. However, since we show in the above′2that
e
, we
increasing the position by an additive term of m′ is not possible with probability 1− O(1)/m
can imply
by
union
bound
that
starting
from
any
position
i,
increasing
the
position
by
an
additive
√
′2 << 0.1 (for a large enough choice
e
term m′ is not possible with probability at least 1 − O(m)/m
of m) which completes the proof.

Now we are ready to prove the lower bound using Lemmas 3.1 and 3.2.
e
e 1/3 ) samples from
Theorem 3.3. Even if emax = 2Θ(1) , any learning algorithm requires at least Ω(m
the distribution in order to obtain an additive error less than 0.5.

16

e 1/3 ) and m′ = Θ(m
e 2/3 ). To be more precise,
Proof. As mentioned earlier, we have l, |LD | = θ(m
we set l = 40cm1/3 log m, m′ = m2/3 log m/2c and |LD | = m1/3 / log m.
Assume for now that we have √l different temperatures 1 ≤ τ1 < τ2 < . . . < τl such that their
2
′
′
√ log m .
multiplicative distance is at least m +10c
′
m

As outlined earlier, LD is a uniform distribution over m1/3 / log m search graphs corresponding
to temperatures τ1 , τ2 , . . . , τl . Each combination has equal probability of forming LD . Distribution
D is a uniform distribution over the search graphs corresponding to the elements of LD . The
optimal solution consists of the keys for all the search graphs corresponding to the temperatures of
LD . Since the size of the key for each search graph is 2cm′ = m2/3 log m and |LD | = m1/3 / log m,
this makes a cooling schedule of size m. Lemma 3.1 implies that the score of such a cooling schedule
is at least 0.9 on average.
On the other hand, after drawing fewer than m1/3 /(100 log m) samples, we can get a score of
1 for at most a 0.01 fraction of the search graphs of LD but the average score for the rest of the
instances would be smaller than 0.2 by Lemma 3.2 (Notice that the gap between the temperatures
is large enough). Thus, Ω(m1/3 / log m) samples are necessary to obtain an additive error smaller
than 0.5.
To construct
the temperatures we do the following: We set x1 = 1 and for 1 < i ≤ l we set
√
2 log m′
m′ +10c
√
+ 1⌉. Finally we set τi = xi / ln 2 to obtain e−xi /τi = 0.5. To make sure all
xi = ⌈xi−1
m′
the energies are non-zero, we add 1 to the energy of all nodes in all gadgets.


17

4

Improved Upper Bound

We show in this section that the bound of Theorem 2.1 can be significantly improved. The proof is
based on two observations: 1) first we show that the discretized set of temperatures can be made
smaller while keeping the additive error small and 2) the proof can be modified to improve the
sample complexity using the new discretized set. We first start by explaining the former.
Our discretization is very similar to that of Theorem 2.1 except that in the construction of the
e −1/2 ) instead of Θ(1/m). This implies that
temperatures we allow for a multiplicative error of Θ(m
e −1/2 ) (instead
the multiplicative distance between consecutive elements of T is bounded by 1 + Θ(m
of 1 + Θ(1/m)). This obviously leaves us with a smaller set of temperatures which later can be
used to improve the sample complexity but the crucial part of the analysis is to show this smaller
set suffices to bound the error by a small ǫ. We prove that for any sequence of temperatures
E = ht1 , t2 , . . . , tm i, there exists another sequence E ′ = ht′1 , t′2 , . . . , t′m i such that t′i ∈ T for all
1 ≤ i ≤ m and that the scores of E and E ′ are very close for every search graph. Obviously we set t′i
e −1/2 ).
as the largest element of T which is not greater than ti . Therefore we have 1 ≤ ti /t′i ≤ 1+ O(m
Let us introduce a deviation function f (x) : [0, 1] → [0, 0.25] = x − x2 which plays an important
role in the proof of Lemma 4.1. The proof of this section is rather mathematical and unintuitive.
For more intuition and as to why such a strange function is necessary for the proof we encourage the
reader to review Section 1. Before proceeding to the proof of Lemma 4.1, we state some properties
of function f as auxiliary observations as well as some mathematical inequalities which are used in
the proof of the bound. We defer the proofs of these observations to appendix.
Observation 4.1. Let x, y ∈ [0, 1] be two real values and 0 ≤ p ≤ 1 be a multiplicative factor.
Then we have:
pf (x) + (1 − p)f (y) ≤ f (px + (1 − p)y) − min{p, 1 − p}(x − y)2 .
Since (x−y)2 is always non-negative therefore Observation 4.1 implies that pf (x)+(1−p)f (y) ≤
f (px + (1 − p)y) always holds. By recursing on this inequality we can extend it to the case of more
than two variables.
Observation 4.2 (as a corollary of Observation 4.1). Let p1 , p2 , . . . , pk be non-negative probabilities
whose total sum is equal to 1 and x1 , x2 , . . . , xk be k real values in range [0, 1] . Then we have:
X
X
pi f (xi ) ≤ f (
pi xi ).
Also, we show that for two real numbers 0 ≤ x, y ≤ 1 we have |x − y| ≥ |f (x) − f (y)|.
Observation 4.3. For any two real numbers 0 ≤ x, y ≤ 1 we have |x − y| ≥ |f (x) − f (y)|.
Observation 4.4. For any 0 ≤ p ≤ 1 and any 0 ≤ x we have
p − p1+x ≤ x.
We also present a slightly modified version of Observation 4.4 which provides a better bound
for limited p.
Observation 4.5. For any 0 < p < 1 and any 0 ≤ x ≤ 1 we have
p − p1+x ≤ max{ln 1/p, 1} min{p, 1 − p}x.
Now we are ready to prove Lemma 4.1.
18

Lemma 4.1. Let I be an instance of the underlying problem and E = ht1 , t2 , . . . , tm i and E ′ =
−1/2
ht′1 , t′2 , . . . , t′m i be two cooling schedules such that 1 ≤ ti /t′i ≤ 1 + ǫm
4 log m for some ǫ > 0. Then we
have
score(I, E ′ ) ≥ score(I, E) − ǫ.
Proof.
Our proof is based on induction. Define E +k (E ′+k ) to be a cooling schedule starting from
element k + 1 of E (E ′ ) (E +0 = E and E ′+0 = E ′ ). We denote the vertices of the search graph by
u1 , u2 , . . . (their number may be exponentially large) and define scoreui (I, E +k ) as the average score
we obtain if we initiate the search on node ui and run the algorithm using cooling schedule E +k .
When k = m, then E +k is empty which means scoreui (I, E +k ) is either equal to 0 or 1 depending
on whether ui is an acceptable solution node in the search graph. A similar notation also holds
for E ′ . Our aim is to prove that for any ui and k we have scoreui (I, E ′+k ) ≥ scoreui (I, E +k ) − ǫ
which immediately implies score(I, E ′ ) ≥ score(I, E) − ǫ. However, to use induction, we strengthen
the hypothesis. We show that


m−k
(5)
scoreui (I, E ′+k ) ≥ scoreui (I, E +k ) − ǫ′ f (scoreui (I, E +k )) +
m
where ǫ′ = ǫ/2. Notice that since the value of f is always in range [0, 0.25], Inequality (5) is already
stronger than what we wish to prove in the end. The base case is when k = m which means the
random walk has terminated and that scoreui (I, E ′+k ) = scoreui (I, E +k ). Thus, for a fixed k < m,
provided that Inequality (5) holds for any vertex ui and k′ = k + 1, we show Inequality (5) holds
for any pair (ui , k).
Recall that in every step of the SA algorithm, we first randomly draw an outgoing edge of the
current node and then decide whether we traverse through that edge or not. Therefore
scoreui (I, E ′+k ) = Euj ∼N (ui ) [scoreui ,uj (I, E ′+k )]
where N (ui ) denotes the set of neighbors of vertex ui and scoreui ,uj (I, E ′+k ) is the score of node ui
for the event that the drawn edge is (ui , uj ).
Let us first fix an edge (ui , uj ) and introduce an edge variant of Inequality (5), namely Inequality
(6) for which we give a proof in the following.


m−k
′+k
+k
′
+k
scoreui ,uj (I, E ) ≥ scoreui ,uj (I, E ) − ǫ f (scoreui ,uj (I, E )) +
.
(6)
m
For simplicity of notation, let us define a = scoreui (I, E +(k+1) ) and b = scoreuj (I, E +(k+1) ). Similarly,
define a′ = scoreui (I, E ′+(k+1) ) and b′ = scoreuj (I, E ′+(k+1) ). If the energy of node uj is more than
the energy of node ui then the decision is deterministic regardless of the temperature and we have
scoreui ,uj (I, E +k ) = b
and
scoreui ,uj (I, E ′+k ) = b′ .

19

This implies that
scoreui ,uj (I, E +k ) − scoreui ,uj (I, E ′+k ) = b − b′


m−k−1
′
≤ ǫ f (b) +
m


m−k−1
′
+k
= ǫ f (scoreui ,uj (I, E )) +
m


m
−
k
′
+k
≤ ǫ f (scoreui ,uj (I, E )) +
m

(7)

where Inequality (7) follows from the induction hypothesis. This basically means that


m−k
′+k
+k
′
+k
scoreui ,uj (I, E ) ≥ scoreui ,uj (I, E ) − ǫ f (scoreui ,uj (I, E )) +
m
which is desired. Thus, it only remains to prove Inequality (6) for the cases that the energy
decreases. This is the only case where E and E ′ behave differently. In this case, depending the
temperatures tk+1 and t′k+1 our SA algorithm moves to node uj or stays at node ui . Let p be
the probability of rejecting the downhill move to node uj when the temperature is equal to tk+1
and p′ the same probability for the case that the temperature is t′k+1 . Recall that the acceptance
′
probabilities are equal to 1−e−∆(E)/tk+1 and 1−e−∆(E)/tk+1 (for E and E ′ respectively) where ∆(E)
′
is the difference between the energies of nodes ui and uj . Thus, p = e−∆(E)/tk+1 and p′ = e−∆(E)/tk+1
−1/2
and since 1 ≤ tk+1 /t′k+1 ≤ 1 + ǫm
4 log m then we have
ǫm−1/2

p1+ 4 log m ≤ p′ ≤ p.
Note that scoreui ,uj (I, E +k ) and scoreui ,uj (I, E ′+k ) can be formulated as
scoreui ,uj (I, E +k ) = pa + (1 − p)b

(8)

scoreui ,uj (I, E ′+k ) = p′ a′ + (1 − p′ )b′

(9)

and
due to the acceptance probabilities. Thus, we have:
scoreui ,uj (I, E ′+k ) = p′ a′ + (1 − p′ )b′


m−k−1
′
′
≥ p a − ǫ [f (a) +
]
m


m−k−1
′
′
+ (1 − p ) b − ǫ [f (b) +
]
m


= p′ a − ǫ′ f (a)


+ (1 − p′ ) b − ǫ′ f (b)
m−k−1
− ǫ′
m 

= p a − ǫ′ f (a)


+ (1 − p) b − ǫ′ f (b)
m−k−1
− ǫ′
m
20

by induction hypothetis

− (p − p′ )([a − ǫ′ f (a)] − [b − ǫ′ f (b)])


≥ p a − ǫ′ f (a)


+ (1 − p) b − ǫ′ f (b)
m−k−1
− ǫ′
m
− (p − p′ )(|a − b| + ǫ′ |f (a) − f (b)|)


≥ p a − ǫ′ f (a)


+ (1 − p) b − ǫ′ f (b)
m−k−1
− ǫ′
m
− (p − p′ )(|a − b| + |f (a) − f (b)|)


≥ p a − ǫ′ f (a)


+ (1 − p) b − ǫ′ f (b)
m−k−1
− ǫ′
m
− 2(p − p′ )|a − b|

p ≥ p′

p ≥ p′

and ǫ′ ≤ 1

p ≥ p′

and |a − b| ≥ |f (a) − f (b)|
(Observation 4.3)

≥ [pa + (1 − p)b] − ǫ′ f ([pa + (1 − p)b])

Observation 4.1

= scoreui ,uj (I, E +k ) − ǫ′ f (scoreui ,uj (I, E +k ))

by Equation (8)

′

2

+ ǫ min{p, 1 − p}(a − b)
m−k−1
− ǫ′
m
− 2(p − p′ )|a − b|
′

2

+ ǫ min{p, 1 − p}(a − b)
m−k−1
− ǫ′
m
− 2(p − p′ )|a − b|


m−k
= scoreui ,uj (I, E +k ) − ǫ′ f (scoreui ,uj (I, E +k )) +
m


′
2
+ ǫ min{p, 1 − p}(a − b) + 1/m
− 2(p − p′ )|a − b|

which is exactly the same as (6) except for additional additive expressions of the last two lines.
Thus, to complete the proof of Inequality (6) we need to show


ǫ′ min{p, 1 − p}(a − b)2 + 1/m ≥ 2(p − p′ )|a − b|.
(10)
Based on the values of p and a − b we consider the following three cases separately:
(i). 0 ≤ |a − b| ≤ m−1/2
(ii). 0 ≤ p ≤ m−1/2
(iii). m−1/2 ≤ |a − b| ≤ 1 and m−1/2 ≤ p ≤ 1

21

−1/2

1+ ǫm

Case (i): 0 ≤ |a − b| ≤ m−1/2 : By Observation 4.4 and the fact that p 4 log m ≤ p′ ≤ p we can
−1/2
imply p − p′ ≤ ǫm
4 log m . Therefore the right hand side of Inequality (10) is bounded by
ǫm−1/2
a−b
4 log m
ǫm−1/2
=
a−b
2 log m
ǫm−1/2 −1/2
m
≤
2 log m
ǫ
=
2m log m
ǫ′
=
m log m
ǫ′
≤
m

2(p − p′ ) a − b ≤ 2

since |a − b| ≤ m−1/2

which implies Inequality (10) since the left hand side is at least ǫ′ /m.

Case (ii): 0 ≤ p ≤ m−1/2 : Let us first give a bound on the value of p − p′ .
ǫm−1/2

p − p′ ≤p − p1+ 4 log m

≤ max{ln 1/p, 1} min{p, 1 − p}
≤(ln

√

m)m−1/2

≤m−1/2
ǫ
=
4m
ǫ′
=
2m

ǫm−1/2
4 log m

ǫm−1/2
4 log m

by Observation 4.5

(11)

(11) is maximized for p = m−1/2

ǫm−1/2
4

since log m ≥ ln

√

m

since ǫ′ = ǫ/2

Also, |a − b| is bounded by 1 so the the right hand side is bounded by ǫ′ /m. Since the left hand
side is at least ǫ′ /m then Inequality (10) holds.

Case (iii): m−1/2 ≤ |a − b| ≤ 1 and m−1/2 ≤ p ≤ 1: In this case, we leverage Observation 4.5 to

22

show that
p − p′ ≤p − p

−1/2

1+ ǫm
4 log m

ǫm−1/2
4 log m

≤ max{ln 1/p, 1} min{p, 1 − p}
≤(ln

√

m) min{p, 1 − p}

by Observation 4.5

ǫm−1/2
4 log m

since p ≥ m−1/2

ǫm−1/2
4
ǫ′ m−1/2
= min{p, 1 − p}
2

since log m ≥ ln

≤ min{p, 1 − p}

√

m

since ǫ′ = ǫ/2

Therefore, the right hand side of Inequality (10) can be bounded by
ǫ′ m−1/2
|a − b|
2
= min{p, 1 − p}(ǫ′ m−1/2 )|a − b|

2(p − p′ )|a − b| ≤2 min{p, 1 − p}

≤ min{p, 1 − p}(ǫ′ m−1/2 )|a − b|
=ǫ′ min{p, 1 − p}|a − b|2

|a − b|
m−1/2

since |a − b| ≥ m−1/2

=ǫ′ min{p, 1 − p}(a − b)2
which proves Inequality (10) since the left hand side is lower bounded by ǫ′ min{p, 1 − p}(a − b)2 .
So far, we have proven that Inequality (6) holds for every pair of vertices (ui , uj ). All that
remains is to show that Inequality (6) implies Inequality (5). To show this, we point out that by
definition we have
scoreui (I, E ′+k ) = Euj ∼N (ui ) [scoreui ,uj (I, E ′+k )].
By applying Inequality (6) we obtain:
h
i
scoreui (I, E ′+k ) =Euj ∼N (ui ) scoreui ,uj (I, E ′+k )


m−k
+k
′
+k
≥Euj ∼N (ui ) scoreui ,uj (I, E ) − ǫ [f (scoreui ,uj (I, E )) +
]
m
h
i
=Euj ∼N (ui ) scoreui ,uj (I, E +k )


m−k
′
+k
]
− Euj ∼N (ui ) ǫ [f (scoreui ,uj (I, E )) +
m
h
i
=Euj ∼N (ui ) scoreui ,uj (I, E +k )
h
i
− ǫ′ Euj ∼N (ui ) f (scoreui ,uj (I, E +k ))
− ǫ′

m−k
m h

i
≥Euj ∼N (ui ) scoreui ,uj (I, E +k )
23

(12)



− ǫ′ f Euj ∼N (ui ) [scoreui ,uj (I, E +k )]
− ǫ′

m−k
m h

i
=Euj ∼N (ui ) scoreui ,uj (I, E +k ) − ǫ′ scoreui ,uj (I, E +k )
− ǫ′

m−k
m



m−k
=scoreui (I, E +k )) − ǫ′ f (scoreui (I, E +k )) +
m
which implies Inequality (5). Inequality (12) follows from Observation 4.2.



Lemma 4.1 suggests that we can have a discretized temperature set T with size
√
O( m log m log emax ) that can make an almost optimal cooling schedule for any search graph.
If we naively count the number of possible cooling schedules, then we obtain a bound of
√
( m log m log emax )m which gives us the same upper bound as Corollary 2.2. However, a better analysis can show that the number of possible cooling schedules limited to the temperatures in
T is bounded by


√
√
m
m log m log emax
√
( m log m log emax )
m log m log emax
√
which gives us a sample complexity of Oǫ ( m(log m + log emax )).
Theorem 4.2. The sample complexity of computing an ε-approximately optimal cooling schedule
√
with length m is bounded by Oǫ ( m(log m + log emax ))..

24

5

A Computational Model to Evaluate SA Algorithms

In this section, we introduce a model to evaluate the performance of an SA algorithm. The purpose
of this model is to study the computational aspects of finding an optimal cooling schedule. We call
this model the monotone stationary graph. For simplicity, (and indeed without loss of generality
as we show in Section 28 ), we narrow down the space of the temperatures used in any algorithm
to a finite set T = {d1 , d2 , d3 , . . . , d|T | }. Therefore from here on, we focus our attention on the
discretized temperatures in T and assume that any algorithm (including any optimal solution) only
uses temperatures in set T . Recall that every instance I of the underlying problem translates to a
search graph for our SA algorithm. The goal of the the monotone stationary graph is to represent
the search graph in a compact manner so that we can evaluate the performance of a cooling schedule
on each instance. Thus, monotone stationary graph is made by the search graph and may differ
between different instances of the problem.
Recall that every state of an SA algorithm A corresponds to a distribution RA over the vertices of
the search graph. Initially, RA is the same for all algorithms and shows the probability distribution
over the vertices on which our algorithm initiates the search. One example is when our algorithm
starts with a fixed node of the search graph in which case RA is a deterministic distribution.
Alternatively, RA may be a uniform distribution when our algorithm starts with a random node
of the search graph. As we perform more steps of the algorithm, RA changes based on the criteria
of the random walk and we hope that the correlation between RA and the energy of the nodes
becomes stronger. Ideally, we would like our algorithm to end up with a distribution RA highly
concentrated on the solution nodes.
Let us for every temperature t ∈ |T |, define a stationary distribution St which is a distribution
of probabilities over the nodes of the search graph that an SA algorithm converges to after infinitely
many steps of running on temperature t. Stationary distributions of simulated annealing are important and have been subject to a plethora of studies in the past decades [2, 9, 13, 17, 22, 25].
Intuitively, stationary distributions have positive correlation with the score of the nodes and as the
temperature drops we expect the stationary distributions to provide higher (average) scores. Thus,
the ideal case is when the state of our algorithm is very close to the stationary distribution for the
lowest temperature for which the average score is the highest. The computational barrier is the
convergence rate of the distributions. An algorithm that starts from an initial distribution and runs
on a temperature t may need exponentially many steps to converge to the stationary distribution St
whereas an algorithm that first reaches a stationary distribution St′ for a higher temperature and
then attempts to reach St may only need a small number of steps. This is perhaps best shown by
the work of Wegener [26] wherein the author showed that for the minimum spanning tree problem,
a cooling schedule that gradually decreases the temperature is exponentially faster than a cooling
schedule that repeats a certain temperature. Thus, moving to intermediate stationary distributions
may significantly improve the convergence rate of the algorithm.
Motivated by the above argument, we consider a model in which the states of any algorithm
move between the stationary distributions. Let d1 > d2 > d3 > . . . > d|T | be all the distinct
temperatures in T . We construct a graph with |T | + 1 nodes v0 , v1 , v2 , . . . , v|T | such that node
vi corresponds to the set of all states close enough to the stationary distribution of temperature
di . Also, v0 is a special node corresponding to the initial distribution of the starting nodes. We
assume that for every node vi , the distances to the stationary distribution of temperature di are
so small such that the difference in the performance is negligible. Due to this assumption, our
model features monotonicity. More precisely, a cooling schedule that repeats a temperature t for
8

A loss of ǫ > 0 is incurred to the score of any algorithm in the discretized setting.

25

100 times is no better than the same cooling schedule that repeats t for 101 times.
In our model, we add edges between the nodes to denote transitions between stationary distributions. The labels of these edges indicate the number of steps needed for transition between a
node vi to a node vj .
vi

hdj , dj , dj , . . . , dj i

vj

Figure 4: A transition is shown between two graph nodes.
Finally, we make one more assumption to complete the notion of monotonicity. If we have three
temperatures di > dj > dk the length of the edge from vi to vk is not smaller than the length of
the edge from node vj to node vk . Another interpretation of this property is the following: in order
to reach the stationary distribution of a temperature dk , it is easier to start from the stationary
distribution of a temperature closer to dk rather than a temperature with a much higher difference.
Although for some very delicately constructed examples this may fail, the assumption is along the
common perception for the behavior of the SA algorithms [1, 2].
With the above definition, every path in the monotone stationary graph corresponds to a
sequence of temperature which is made by the concatenation of the labels of the edges. A path can
be traversed with a sequence of temperatures E if its corresponding label is a subsequence of E.
Given a sequence of temperatures E = ht1 , t2 , . . . , tm i, one can travel from node v0 of the stationary
distribution graph to a set of nodes via E. In order to model the score of a cooling schedule E, we
assume that it takes us to the right most node vi such that there is a path from v0 to vi whose
label is a subsequence of E. Implicit to our model is the assumption that stationary distributions
become better9 as the temperature drops. Thus, the scoring function gives us higher scores for
lower temperatures.
For our computational results, we assume that the score of each cooling schedule is evaluated
based on the above model. We compete against an optimal cooling schedule that uses a sequence of
at most m moves. Thus, we can assume w.l.o.g that the length of every (existing) edge is bounded
by m. This along with the monotonicity property of our model implies that there is a trivial
cooling schedule with |T |m many moves that performs at least as well as the optimal schedule with
m steps. That is, in our model, a cooling schedule that contains m copies of each temperature
performs always as well as any cooling schedule of length m. Although we allow the size constraint
to be violated by a small factor, our aim is to keep the length of our approximately optimal cooling
schedule close to m.
Our model may raise a concern for a thoughtful reader. We only incorporate the types of
algorithms whose states move between the stationary distributions. What if the optimal solution
never gets close enough to some of the stationary distributions, yet moves towards them in order
to reach the stationary distributions for lower temperatures (see Figure 5)?
9

More concentration on the solution nodes.

26

vi

hdj , dj , dj , dj , dj , dj , dj , dj i

hdk , dk , dk i

vj

hdj ,
d

j,d
dk, dk
j i, d k , d k ,
d
h k

vk

, d ki

Figure 5: Red edges show the cooling schedule of the optimal solution. In this case, the optimal
solution moves toward the stationary distribution of temperature dj without getting close enough
to its stationary distribution.
Although this may very well be the case in practice, the goal of this model is competing with
the optimal algorithm that moves between the stationary distributions (and thus such a scenario
is ruled out). We justify our model by the following intuitive argument: If moving towards a
stationary distribution Sdj makes a significant difference in the convergence rate for stationary
distribution Sdk , it should be the case that a considerable portion of the path to the stationary
distribution of Sdj is already traversed. Thus, if we multiply the number of dj steps of the algorithm
by a small constant, this algorithm should reach the stationary distribution of Sdj . In other words,
the optimal algorithm that adheres to our model may not necessarily be the optimal algorithm,
however, if we allow for more steps (by a multiplicative constant factor), we expect that the optimal
algorithm of our model performs as well as the optimal algorithm in the unrestricted setting.

5.1

Computational Results

Although our model is general, we use the SAT problem to explain the terminology. Assume that
the search graph contains 2k vertices where every vertex is a true/false assignment to k variables of
the underlying problem. Every node of the search graph is associated with a value which we refer
to as energy. This concept reflects how close this node is to a solution. One example of such energy
function is the amount of clauses satisfied by that solution. Also, the score of a cooling schedule E
is equal to the probability of finding a solution for the problem via simulated annealing using E as
a cooling schedule. We model this quantity with the monotone stationary graph.
Recall that we are given a distribution D over a class of SAT instances and our aim is to design a
learning algorithm that computes/approximates a cooling schedule with the highest average score.
In other words, our goal is to find a cooling schedule E for simulated annealing that maximizes
EI∼D [score(I, E)].
We model the performance of a simulated annealing algorithm by the monotone stationary
graph explained previously. We compete against the score of the optimal cooling schedule with
at most m steps subject to our model. Notice that, the optimal cooling schedule may in fact get
a higher score than what our model suggests but we only give credit to that schedule based on
our model and not the actual likelihood of finding a solution. Nonetheless, our hope is that the
difference between the practical results and our model is negligible.
We assume throughout this paper that the number of steps of the optimal cooling schedule
is equal to m. However, in order to compete with the optimal solution, we allow more steps for
our algorithm. We define an algorithm A to be (α, ǫ)-approximate, if the number of steps of A is
27

bounded by αm and the average score of A differs from the optimal solution by at most an additive
error of ǫ.
We show in Section 2 that from a sample-complexity standpoint, a learning algorithm only
e √m) samples from D (Theorem 4.2). This result is indeed not dependent on the monotone
needs O(
stationary graph. However, the computational complexity of the solution requires more assumption
on the score of cooling schedules. To this end, we define four scoring systems and analyze each of
the systems separately.
e √m) samples from D and find the solution
Our results in Section 2 show that if we draw n = O(
that maximizes the average score on these n samples, the objective is approximately maximized for
D. Therefore, in the computational results, we assume that n problem instances I1 , I2 , . . . , In are
given and our goal is to find a sequence that maximizes the average score for those instances. We
consider the following two settings for our problem:
• separate paths: For each instance I, the optimal cooling schedule runs on a sequence of temperatures that move between the nodes of the stationary distribution graph. However, the
sequence of stationary nodes may vary between different instances.
• identical paths: The optimal cooling schedule chooses a sequence va1 , va2 , . . . , vax of the nodes
and does the following: starts and runs the algorithm by temperature da1 so long as all
instances reach stationary distribution va1 . Then, proceeds with applying temperature da2
until all input instances reach stationary distribution va2 and so on. In this case, the path
taken in the stationary distribution graph is the same for all instances of the problem.
We bring an example to illustrate the difference of the two models. Consider a distribution D
of the SAT instances which returns instances I1 and I2 with equal probabilities. Let us assume that
the monotone stationary graphs of the two instances are as shown in Figure 6. In the separate
paths setting, the optimal sequence of temperatures that reaches the lowest stationary distribution
for both instances is hd1 , d2 , d2 , d2 , d2 i. Notice that in this case, for I1 the path to v2 is through v1
but for I2 the path consists of a direct edge from v0 to v2 . However, the choice of separate paths
is not allowed in the identical paths model. Therefore, in the identical paths setting, the optimal
solution is hd1 , d1 , d1 , d1 , d2 , d2 , d2 , d2 i which is through v1 for both instances.
hd2 , d2 , d2 , d2 i

hd2 , d2 , d2 , d2 , d2 , d2 , d2 , d2 i

v0

hd1 i

v1

hd2 , d2 , d2 , d2 i

v0

v2

hd1 , d1 , d1 , d1 i

v1

hd2 , d2 , d2 , d2 i

v2

(b) Monotone stationary graph for I2

(a) Monotone stationary graph for I1

Figure 6: An example to show the difference between the separate paths setting and identical paths
setting.
Moreover, we also study a more restricted setting, in which in the optimal solution, all instances
of the problem reach the stationary distribution for the lowest temperature. We call this setting
the all-satisfied setting.
For each combination of the settings we provide an algorithm along with its analysis. Table 5.1
summarizes the time complexity of our algorithm in each setting.
One last thing to keep in mind before we go to the technical discussion is that monotone
stationary graphs are not available to our algorithms. Therefore, the first step is to learn such a
28

identical paths
exact solution
in time
poly(m, n, |T |)

separate paths
exact solution
in time
poly(m, n, |T |n )

separate paths + all-satisfied
(O(log n|T |), 0) approximation
in time
poly(m, n, |T |)

graph for a given instance I of the problem. We begin by explaining this in Section 6 and then
bring our algorithms in Section 7.
hd5 , d5 , d5 , d5 , d5 , d5 i
hd2 , d2 , d2 , d2 i

v0

hd1 , d1 , d1 i

v1

hd2 , d2 i

v2

hd3 , d3 i

v3

hd4 , d4 , d4 i

v4

hd5 , d5 i

v5

hd3 , d3 , d3 , d3 i
Figure 7: An example of the monotone stationary graph is shown. Only non-trivial edges are shown
in this figure. For instance, an edge of length 6 from v3 to v5 can be implied from the edge (v1 , v5 ).
To remind the reader of our assumptions, we bring a list of assumptions that we make for the
model and the results:
• (for the model): The state of any algorithm moves between stationary distributions.
• (for the model): For i < j < k the length of the edge from vi to vk is not smaller than that
of vj to vk .
• (for the model): For any path P , a cooling schedule that contains the labels of the edges of
the path as subsequence can take us to the end vertex. The score of a cooling schedule is
equal to that of the best stationary distribution reachable via that schedule.
• (for the model): The score improves as i increases for vi .
• (in order to learn the monotone stationary graph): For every instance of the problem, there
is a cooling schedule of length m that takes us to node v|T | .
• (in order to learn the monotone stationary graph): There is a noticeable difference between
the scores of the nodes of the monotone stationary graph. That is, by running poly(n, m, |T |)
experiments we can tell whether two cooling schedules E1 and E2 take us to the same node or
not.

6

Learning A Monotone Stationary Graph

In this section, we show how one can learn the monotone stationary graph for a particular instance
of the problem in polynomial time. Recall that score(E, I) denotes the success probability of finding
a solution to the problem. We make two assumptions to learn the monotone stationary graph. The
29

first assumption is that for every instance there exists a sequence of length m that takes us to the
optimal node (corresponding to the lowest temperature) in the monotone stationary graph. The
second assumption is that there is a noticeable difference between the score of the nodes. That is,
for any two cooling schedules E1 and E2 we can tell whether they take us to the same node in the
monotone stationary graph or they take us to different nodes by running the SA algorithm several
times and comparing their success ratios.
The discretization of the the temperatures is w.l.o.g as we show in Section 2. Also, we ignore
all edges whose sizes are more than m. This obviously does not hurt the optimal solution since its
length is bounded by m.
Observation 6.1. Given a sequence E of temperatures, we can verify in polynomial time whether
E takes us to v|T | . That is, we can answer in polynomial time whether E is at least as good as any
other sequence or not.
Proof. By the above assumptions, a sequence that contains m repetitions of each temperature
has to take us to node v|T | (otherwise there is no path of length m to v|T | ). Thus, by running the
algorithm on this sequence, we can learn the average score of that node in time poly(m, |T |). Now,
for a sequence E, we just need to run the algorithm several times and verify whether the success
rate is close to s|T | or not.

Using Observation 6.1, we can construct the monotone stationary graph for an instance I of the
problem.
Lemma 6.1. Given an instance I of the problem, one can construct the underlying graph G(I) in
time poly(m, |T |).
Proof. We assume that there is a path of length m from node v0 to node v|T | . Thus, a sequence
containing m repetitions of each temperature takes us there. Now, imagine we wish to answer the
following question:
k
}|
{
z
“Is there an edge from node vi to node v|T | with label hd|T | , d|T | , . . . , d|T | i? ”
To answer the above question, we can construct a sequence of temperatures that contains m
repetitions of all temperatures d1 , d2 , . . . , di . Next, we add k repetitions of temperature d|T | to the
end of this sequence. If this sequence takes us to node v|T | , then there is an edge from vi to v|T |
with a label that contains at most k copies of d|T | . Thus, we can answer the query with a binary
search.
Using the above machinery, we can extract all the edges that end at node v|T | . Based on this
information, we can find the smallest path that takes us from node v|T |−1 to node v|T | and then
recursively solve the problem for node v|T |−1 . With the same argument, we can discover all of the
edges for all vertices of the graph.


7

Computing/Approximating the Optimal Cooling Schedule

The problem that we are concerned with in this section is computing (or approximating) the optimal
cooling schedule for a set of problem instances. More precisely, let I1 , I2 , . . . , In be n instances of
the problem whose monotone stationary graphs are available. The goal here is to find a cooling
schedule whose size is close to m and and whose average score for the n instances is close to the
optimal solution.
30

7.1

Identical Paths

The easier setting that we study is identical paths. In this setting, we compete with the optimal
solution that chooses the same path for all instances. In other words, in such solutions, we fix a
set of nodes va1 , va2 , . . . , vak and find a cooling schedule that takes all instances through this path.
More precisely, we put enough temperatures da1 to make sure all instance reach vertex va1 . Next,
we proceed by doing the same thing for va2 and so on.
We show that in this setting the problem of finding the optimal cooling schedule reduces to
shortest path. Construct a graph G with the same vertex set as the monotone stationary graphs.
We put a directed edge from vertex vi to vertex vj of G, if and only if such an edge exists in the
corresponding monotone stationary graphs of all instance. Moreover, we set the length of this edge
as the largest length in all the graphs. Finally, we find the lowest temperature di (meaning that i
is maximized) such that vertex vi is reachable from vertex v0 via a path of length at most m. We
prove that this algorithm is optimal.
Algorithm 1: Exact algorithm for the identical paths setting.
1: for 1 ≤ k ≤ n do
(k)
2:
Let ri,j be the minimum number of repetitions for temperature dj to make a transition
from node vi to vj on the k-th monotone stationary graph.
(k)
3: ri,j := maxk∈[n] ri,j .
4: Let ri,j = 0 when i ≥ j.
5: Construct a graph with vertices v0 , · · · , v|T | and pairwise distances ri,j .
6: Find the the shortest paths from v0 to all nodes of the graph.
7: Find the largest q such that node vq is within a distance of m from v0 .
8: Output the optimal sequence of temperatures made by this path.

Theorem 7.1. Given n monotone stationary graphs for n instances of the problem, one can find in
polynomial time a cooling schedule of length m that maximizes the average score for the n instances
in the same paths setting
Proof. The proof is based on the fact that the path is the same for all instances. Thus, in order
to make a transition from vertex vi to vertex vj , one needs to add as many copies of temperature
dj as the size of the largest label among all instances. Thus, the furthest we can get from node v0
is a node vi whose distance from v0 is bounded by m on the graph we make.


7.2

Separate Paths

The more challenging setting is when we allow the instances to have different paths in the optimal
solution. In this case, the problem is much harder since we have to consider n different monotone
stationary graphs and solve the problem with respect to all of them. However, it is not hard to see
that if n is constant, one can find the optimal cooling schedule of length m in polynomial time.
Lemma 7.2. Given n monotone stationary graphs for n instances of the problem, one can find
e
in time O(m|T
|n+1 ) a cooling schedule of length m that maximizes the average score for the n
instances in the separate paths setting
Proof. The proof is similar to the proof of Theorem 7.1. However, since we may traverse a different
path for every graph, we need to construct our graph more carefully. To this end, our vertex set
31

hd5 , d5 , d5 , d5 , d5 , d5 i
hd2 , d2 , d2 , d2 i

v0

hd1 , d1 , d1 i

v1

hd2 , d2 i

v2

hd3 , d3 i

v3

hd4 , d4 , d4 i

v4

hd5 , d5 i

v5

hd3 , d3 , d3 , d3 i
Figure 8:
All the dashed edges are crossing for vertex v2 .
Moreover, sequence
hd1 , d1 , d2 , d2 , d2 , d2 , , d3 , d3 , d3 , d3 , , d4 , d4 , d4 , d4 , d5 , d5 i is an acceptable sequence that encompasses
all the red edges. The edges that are not drawn are implied by the edges depicted in the figure.
would be the multiplication of the vertex sets for the monotone stationary graphs. That is, we put
(|T | + 1)n different vertices in our graph such that every vertex shows one combination of the nodes
for the instances.
Every vertex has O(m|T |) different edges that shows how the combination changes by adding
1 ≤ i ≤ m copies of temperature dj to the sequence. Finally, we compute the distances of all
vertices from node (v0 , v0 , . . . , v0 ) and find the one whose distance is bounded by m and its score
is maximized. Then, we recover the path to that node and report it.

Obviously, the runtime of Lemma 7.2 is not polynomial when n is super constant. Therefore, for
asymptotically larger n’s, we present a polynomial time algorithm that approximates the solution.
Our algorithm works for the all-satisfied setting, which means that there is an optimal solution that
brings all instances to the vertex corresponding to the lowest temperature. Our algorithm loses a
polylogarithmic factor in the size of the sequence but obtain the same score as the optimal solution
with high probability.
Let us assume for simplicity that the score for each instance Ik is equal to 1 if and only if our
sequence takes us to node v|T | in its monotone stationary graph. Otherwise the score is equal to 0.
Our algorithm is not dependent on this assumption, yet it makes the explanation much simpler.
We begin by an observation that translates the definition of score into the set cover setting.
We say a cooling schedule E is an acceptable cooling schedule for an instance I of the problem if
E takes us all the way to node v|T | in its monotone stationary graph. Define an edge from a vertex
vi to a vertex vj to be crossing for a vertex vk if i < k ≤ j holds. Moreover, we say a sequence E
encompasses an edge from vi to vj from a particular monotone stationary graph if E contains at
least as many repetitions of temperature dj as the label of the edge from vi to vj . An example of
the definitions is shown in Figure 8.
Now, we are ready to state an observation that plays an important role in our algorithm.
Observation 7.1. A sequence of temperatures E is acceptable for an instance I of the problem if
and only if for every 1 ≤ i ≤ |T |, E encompasses at least one crossing edge with vi .
Proof. The necessity of the condition is trivial. If E does not encompass a crossing edge for a
vertex vi , then E cannot reach vertex vi in monotone stationary graph. The vice versa also holds.
Suppose for the sake of contradiction that a sequence E encompasses a crossing edge for every vertex
but it does not take us to node v|T | . In this case, there exists a vertex vi , such that all vertices vi−1
32

hd5 , d5 , d5 , d5 , d5 , d5 i
hd2 , d2 , d2 , d2 i

v0

hd1 , d1 , d1 i

v1

hd2 , d2 i

v2

hd3 , d3 i

v3

hd4 , d4 , d4 i

v4

hd5 , d5 i

v5

hd3 , d3 , d3 , d3 i
Figure 9: For m = 9 the optimal sequence of temperatures is hd1 , d1 , d1 , d5 , d5 , d5 , d5 , d5 , d5 i. All
the edges skipped in the figured can be implied from the edges shown by monotonicity.
is reachable but none of the vertices vj is reachable for j ≥ i are reachable using E. This means
that E does not encompass an edge that crosses vertex vi otherwise we could have reached vertex
vi using E.

We are now ready to state the main theorem of this section.

Theorem 7.3. Let I1 , I2 , . . . , In be n monotone stationary graph with the guarantee that there
exists a cooling schedule of length m that is acceptable for all instance. One can find in polynomial
time a cooling schedule for the SA algorithm whose average score is equal to that of the optimal
cooling schedule of size m. Our algorithm is randomized and gives a solution with probability at
least 1 − e−100 . Also, the average size of the cooling schedule is bounded by O(m(log |T | + log n)).
Proof. Observation 7.1 gives us a strong tool to analyze the solution. Let OPT be the optimal
cooling schedule of size m which is acceptable for all instances. Due to Observation 7.1, OPT
encompasses at least one crossing edge for all vertices of all monotone stationary graphs. To
formalize this, define a set
m

}|
{
z
S ={hd1 i, hd1 , d1 i, . . . , hd1 , d1 , . . . , d1 i}∪
m

}|
{
z
{hd2 i, hd2 , d2 i, . . . , hd2 , d2 , . . . , d2 i}∪
..
.
m

}|
{
z
{hd|T | i, hd|T | , d|T | i, . . . , hd|T | , d|T | , . . . , d|T | i}

to be the set of all possible repetitions for all temperatures and for each element e ∈ S, define ℓ(e)
to be the size of e. In addition to this, for each element e ∈ S, define ce = {0, 1} to be equal to 1
if and only if OPT contains ℓ(e) repetitions of the character corresponding to e.
To clarify the definitions, consider an example with only a single instance shown in Figure 9. In
this case, m = 9 and the optimal sequence of temperatures is OPT = hd1 , d1 , d1 , d5 , d5 , d5 , d5 , d5 , d5 i.
In this case S contains 45 = m|T | elements out of which only chd1 ,d1 ,d1 i and chd5 ,d5 ,d5 ,d5 ,d5 ,d5 i are
equal to 1. Moreover, ℓ(hd1 , d1 , d1 i) = 3 and ℓ(hd5 , d5 , d5 , d5 , d5 , d5 i) = 6 hold.
For a vertex vi in graph Ik , define crossingl(Ik , vi ) to be the set of elements in S that correspond
to the crossing edges of vi . This way, the optimal solution of the problem can be formulated via
the following integer feasibility program:
33

constraints:

P
P ℓ(e)ce

≤m
.≥ 1
∀1 ≤ k ≤ n and 1 ≤ i ≤ |T |
(13)
ce
∈ {0, 1} ∀e ∈ S
where the variables of the program are ce ’s. Indeed by relaxing the conditions of IP 13 we can
obtain LP 14.
P
constraints: P ℓ(e)ce
≤m
.≥ 1 ∀1 ≤ k ≤ n and 1 ≤ i ≤ |T |
(14)
e∈crossingl(vi ,Ik ) ce
0 ≤ ce ≤ 1
∀e ∈ S
Now we solve LP 14 and construct a solution as follows: for each element e ∈ S, we add e to
our solution independently with probability min{αce , 1}, where α = 100(log |T | + log n).
First, it’s easy to see the expected length of our solution is bounded by αm:
e∈crossingl(vi ,Ik ) ce

E[length] =

X

Pr[e is picked]ℓ(e) =

e∈S

X
e∈S

min(αce , 1)ℓ(e) ≤

X
e∈S

αce ℓ(e) ≤ αm

where the last step is due to the constraint in LP.
Next, we will show that with high probability, the resulting sequence is acceptable for each
instance Ik . Consider the case when the resulting sequence is not acceptable for Ik . By Observation
7.1, there exists a vi such that none of the edges in crossingl(vi , Ik ) were encompassed in our solution.
By union bound, the probability of this bad event can be upper bounded by
Pr[Ik is not satisfied] ≤

|T |
X
i=1

Pr[∀e ∈ crossingl(vi , Ik ) wasn’t picked]

(15)

Now we focus on the probability inside the summation. Since each element was selected independently, this probability equals to
Pr[∀e ∈ crossingl(vi , Ik ) wasn’t picked] =

Y

Pr[e wasn’t picked]

e∈crossingl(vi ,Ik )

=

Y

e∈crossingl(vi ,Ik )

max(1 − αce , 0).

If αce ≥ 1 for some e ∈ crossingl(vi , Ik ), then the probability is 0. Otherwise, since 1 − x ≤ e−x , we
have
P
Y
− e∈crossingl(v ,I ) αce
i k
≤ e−α
max(1 − αce , 0) ≤ e
e∈crossingl(vi ,Ik )

Therefore, by 15
Pr[Ik is not satisfied] ≤ |T |e−α

Using union bound again, we have

Pr[any instance Ik is not satisfied] ≤

X

Pr[Ik is not satisfied]

1≤k≤n
−α

≤|T |ne

≤e−100

Hence, we proved that with probability 1 − e−100 , the resulting sequence is acceptable for each
instance Ik .

34

References
[1] E. Aarts and J. Korst. Simulated annealing and boltzmann machines. 1988.
[2] E. H. Aarts et al. Simulated annealing: Theory and applications. 1987.
[3] C. Aragon, D. Johnson, L. McGeoch, and C. Schevon. Simulated annealing performance
studies. In Workshop on Statistical Physics in Engineering and Biology, pages 865–892, 1984.
[4] N. Azizi and S. Zolfaghari. Adaptive temperature control for simulated annealing: a comparative study. Computers & Operations Research, 31(14):2439–2451, 2004.
[5] M.-F. Balcan, D. DeBlasio, T. Dick, C. Kingsford, T. Sandholm, and E. Vitercik. How much
data is sufficient to learn high-performing algorithms? arXiv preprint arXiv:1908.02894, 2019.
[6] M.-F. Balcan, T. Dick, and M. Lang. Learning to link. In ICLR, 2020.
[7] M.-F. Balcan, T. Dick, T. Sandholm, and E. Vitercik. Learning to branch. In International
Conference on Machine Learning, pages 353–362, 2018.
[8] M.-F. Balcan, V. Nagarajan, E. Vitercik, and C. White. Learning-theoretic foundations of
algorithm configuration for combinatorial partitioning problems. In Conference on Learning
Theory, pages 213–274, 2017.
[9] R. Eglese. Simulated annealing: a tool for operational research. European journal of operational
research, 46(3):271–281, 1990.
[10] D. A. Freedman et al. On tail probabilities for martingales. the Annals of Probability, 3(1):100–
118, 1975.
[11] R. Gupta and T. Roughgarden. A PAC approach to application-specific algorithm selection.
SIAM Journal on Computing, 46(3):992–1017, 2017.
[12] B. Hajek. Cooling schedules for optimal annealing. Mathematics of operations research,
13(2):311–329, 1988.
[13] D. Henderson, S. H. Jacobson, and A. W. Johnson. The theory and practice of simulated
annealing. In Handbook of metaheuristics, pages 287–319. Springer, 2003.
[14] S. Kirkpatrick, C. D. Gelatt, and M. P. Vecchi. Optimization by simulated annealing. science,
220(4598):671–680, 1983.
[15] J. Lam and J.-M. Delosme. An efficient simulated annealing schedule: derivation. Yale University, New Haven, Connecticut, Technical Report, 8816, 1988.
[16] J. Lam and J.-M. Delosme. Performance of a new annealing schedule. In Proceedings of
the 25th ACM/IEEE Design Automation Conference, pages 306–311. IEEE Computer Society
Press, 1988.
[17] D. Mitra, F. Romeo, and A. Sangiovanni-Vincentelli. Convergence and finite-time behavior of
simulated annealing. Advances in applied probability, 18(3):747–771, 1986.
[18] M. Mitzenmacher and E. Upfal. Probability and computing: randomization and probabilistic
techniques in algorithms and data analysis. Cambridge university press, 2017.
35

[19] Y. Nourani and B. Andresen. A comparison of simulated annealing cooling strategies. Journal
of Physics A: Mathematical and General, 31(41):8373, 1998.
[20] J. D. Nulton and P. Salamon. Statistical mechanics of combinatorial optimization. Physical
Review A, 37(4):1351, 1988.
[21] M. Sacco. Stochastic relaxation, gibbs distributions and bayesian restoration of images.
[22] P. Serafini. Simulated annealing for multi objective optimization problems. In Multiple criteria
decision making, pages 283–292. Springer, 1994.
[23] E. Triki, Y. Collette, and P. Siarry. A theoretical study on the behavior of simulated annealing
leading to a new cooling schedule. European Journal of Operational Research, 166(1):77–92,
2005.
[24] J. Tropp et al. Freedman’s inequality for matrix martingales. Electronic Communications in
Probability, 16:262–270, 2011.
[25] P. J. Van Laarhoven, E. H. Aarts, and J. K. Lenstra. Job shop scheduling by simulated
annealing. Operations research, 40(1):113–125, 1992.
[26] I. Wegener. Simulated annealing beats metropolis in combinatorial optimization. In International Colloquium on Automata, Languages, and Programming, pages 589–601. Springer,
2005.

36

A

Omitted Proofs of Section 3

Proof of Observation 3.1: For Observation 3.1.(i), define τr = {arg mini≥0 : xi = r}. We would
like to prove that,
Pr[τ√k/c ≤ k] ≥ 0.95
(16)
By the Markov property, τr is the sum
copies of τ1 . Let the probability generating
P of r independent
j , then we have F (z) = F (z)r . Furthermore,
Pr(τ
=
j)z
function of τr be Fr (z) := E[z τr ] = ∞
r
r
1
j=0
we have the following recurrence about F1 (z) :
F1 (z) =
Hence,


z
1 + F1 (z) + F1 (z)2
3

(17)

p

3(z + 3)(1 − z)
2z
One important property about F1 (z) is that for all z ∈ [0, 1],
√
F1 (z) ≤ 1 − 1 − z
F1 (z) =

(3 − z) −

(18)

(19)

By Markov’s inequality,
E[z τr ]
z
zk √
(1 − 1 − z)r
= inf
z
zk
1
1
1 r
(z := 1 − ) = (1 − √ ) (1 − )−k
k
k
k
√
(r := c k) ≤ exp(−c − 1)

(20)

Pr[τr ≥ k] ≤ inf

(21)
(22)
(23)

Hence we have completed the proof.
For Observation 3.1.(ii) and (iii), we need a classical result in martingale concentration inequalities, the Freedman’s inequality for scalar martingales [10, Thm. (1.6)], see also [24, Thm. (1.1)].
Theorem A.1 (Freedman). Consider a real-valued martingale {Yk : k = 0, 1, 2, . . . } with difference
sequence {Xk : k = 1, 2, 3, . . . }. Assume that the difference sequence is uniformly bounded:
|Xk | ≤ R

almost surely

for k = 1, 2, 3, . . . .

Define the predictable quadratic variation process of the martingale:
Wk :=

Xk

j=1

Ej−1 Xj2



for k = 1, 2, 3, . . . .

Then, for all t ≥ 0 and σ 2 > 0,


Pr[∃k ≥ 0 : Yk ≥ t and Wk ≤ σ 2 ] ≤ exp −

t2 /2
σ 2 + Rt/3



.

When the difference sequence {Xk } consists of independent random variables, the predictable
quadratic variation is no longer random. In this case, Freedman’s inequality reduces to the usual
Bernstein inequality.
37

To prove 3.1, we let yk = xk + kγ where γ = pb − pf , then yk is a martingale since the difference
sequence ∆k = yk −yk−1 has expectation zero.PFurthermore, the difference sequence ∆k is uniformly
bounded with |∆k | ≤ R := 1+|γ|, and Wk = kj=1 Ej−1 (∆2k ) ≤ kR2 . By the Freedman’s inequality,


t2 /2
.
(24)
Pr[max yk ≥ t] ≤ exp − 2
k
kR + Rt/3
Since we have R = 1 + |γ| and yk = xk + kγ, (24) is equivalent to


t2 /2
Pr[max xk ≥ t − kγ] ≤ exp − 2
.
k
kR + tR/3
√
Let t = 3R k log k, we have

(25)

t2 /2
t2 /(2R2 )
t2 /(2R2 )
t2
=
≥
=
≥ 2 log k
kR2 + Rt/3
k + t/(3R)
k+k
4kR2
Rearranging terms gives
p
1
Pr[max xk ≥ 3(1 + |γ|) k log k − kγ] ≤ 2 .
k
k

(26)

When pf = pb = ps = 13 , we have γ = 0 and the above inequality is equivalent to
p
1
Pr[max xk ≥ 3 k log k] ≤ 2 .
k
k

(27)

′

k
and we only needs to prove that
This proves (ii). For (iii), we note that γ = pb − pf ≥ 2c√log
k′

p
3(1 + |γ|) k log k − kγ ≤
Note that
√

√

k′
2

(28)

p
p
k
3(1 + |γ|) k log k − kγ ≤ 3 k log k − γ.
2

(29)

p
k
9 log k
3 k log k ≤ γ +
2
γ

(30)

p
9 log k
9 log k √ ′ 9 √ ′
k ≤
k
3(1 + |γ|) k log k − kγ ≤
=
γ
2c log k′
c

(31)

k
When γ ≥ 6 √log
, RHS is negative so the inequality holds trivially. Otherwise, we have γ =
k
√
√
′
log k
√k < 6 √
, hence k′ ≥ O(1) logk2 k > k. By AM-GM inequality,
2c log
′
k
k

Therefore, we have

Hence, let c = 9 completes the proof.



38

B

Omitted Proofs of Section 4

Proof of Observation 4.1: The proof is given below:




pf (x) + (1 − p)f (y) =p x − x2 + (1 − p) y − y 2



=(px + (1 − p)y) − (px + (1 − p)y)2 − (p − p2 )(x2 + y 2 − 2xy)


=(px + (1 − p)y) − (px + (1 − p)y)2 − (p − p2 )(x − y)2


≤(px + (1 − p)y) − (px + (1 − p)y)2 − min{p, 1 − p}(x − y)2


=f (px + (1 − p)y) − min{p, 1 − p}(x − y)2 .

(32)

Inequality (32) follows from the fact that both p and 1 − p are in range [0, 1] and thus p(1 − p) ≤
min{p, 1 − p}.


Proof of Observation 4.3:

|f (x) − f (y)| =|[x − x2 ] − [y − y 2 ]|

=|(x − y) − (x2 − y 2 )|

=|(x − y) − (x − y)(x + y)|

=|(x − y)(1 − (x + y))|
=|x − y||(1 − (x + y))|
≤|x − y|

where the last inequality holds since 0 ≤ x + y ≤ 2 and therefore −1 ≤ 1 − (x + y) ≤ 1 which
implies 0 ≤ |1 − (x + y)| ≤ 1.

Proof of Observation 4.4: To prove the observation, we take the first derivative of p − p1+x
which is equal to

d 
p − p1+x = 1 − (1 + x)px
dp

which means that the function is maximized (or minimized) at p0 = (1 + x)−1/x . It is easy to see
that since p − p1+x is non-negative in range [0, 1] and is equal to 0 at both p = 0 and p = 1 then
the expression should be maximized at p0 . Thus, the maximum value for p − p1+x is bounded by
p0 − p1+x
= p0 (1 − px0 )
0
≤ 1 − px0

= 1 − ((1 + x)−1/x )x
= 1 − (1 + x)−1

= 1 − 1/(1 + x)

= x/(1 + x)
≤ x.


Proof of Observation 4.5: We first show the proof for the case of p ≤ 1/2. We start by the
famous inequality 1 + y ≤ ey [18] which holds for any y ∈ R. Therefore, we have 1 − ey ≤ −y. By
setting y = −x ln 1/p we obtain
1 − e−x ln 1/p ≤ x ln 1/p
39

Notice that e−x ln 1/p can be written as (e− ln 1/p )x = (eln p )x = px . Thus, we have
1 − px ≤ x ln 1/p
Multiplying both sides by p gives us
p − p1+x ≤ p(ln 1/p)x
which proves the observation for p ≤ 1/2. Next, we show the statement for p ≥ 1/2. In this
case, we prove p − p1+x ≤ (1 − p)x which implies the observation. Our goal here is to prove
p − p1+x − (1 − p)x ≤ 0 for any p ∈ [0.5, 1] and any 0 ≤ x ≤ 1. Thus, we take the derivative of p to
bound its maximum value.

d 
p − p1+x − (1 − p)x = 1 − (1 + x)px + x
dp
which is equal to 0 only at p0 = 1. At p0 we have p − p1+x − (1 − p)x = 0 which is not greater
than 0. Also, since for p = 0 the expression p − p1+x − (1 − p)x is equal to −x which is negative, it
means that the function is maximized at p = 1. Thus, p − p1+x − (1 − p)x is always upper bounded
by 0 which means p − p1+x ≤ (1 − p)x.


40

