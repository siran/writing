## Maxwell-transport invariance between isolated observers

We need a statement that does not smuggle “inertial frames” as a primitive.

Define an **isolated observer** as an observer describing a region in which the
energy-flow pattern is unforced and unperturbed, so that the net momentum flux
through a large closed surface vanishes. In the flow-first language, this is the
condition that there is no preferred direction of net $\mathbf{S}/c^2$ momentum
throughput in that region.

Now impose the only requirement we need:

**Requirement (transport-law sameness).** Two isolated observers describing the
same electromagnetic transport process must be able to write the same vacuum
Maxwell transport law.

In vacuum, Maxwell implies the wave operator

$$
\mathcal{O}_c := \partial_t^2 - c^2 \nabla^2,
$$

so transport-law sameness is the statement that the same process satisfies

$$
\mathcal{O}_c \Phi = 0
\quad\Longleftrightarrow\quad
\mathcal{O}'_c \Phi = 0,
$$

for any field component $\Phi$, with the same constant
$c$, when expressed in either observer’s coordinates.

Equivalently: the wave operator is preserved up to an overall nonzero factor
(which does not change the solution set of a linear homogeneous PDE):

$$
\mathcal{O}_c = \lambda\,\mathcal{O}'_c,\qquad \lambda\neq 0.
$$

This is not a statement about “space” having a metric. It is a statement about
two descriptions of the same transport process agreeing on the transport PDE.


## Hyperbolic mixing is forced by operator invariance

Assume the two isolated observers are in relative uniform translation along the
$x$-axis. By homogeneity and straight-line preservation, the
re-description is linear. By symmetry in the transverse directions, take
$y'=y$, $z'=z$.

Write the most general linear mixing of $t$ and $x$:

$$
x' = a x + b t,\qquad t' = d x + e t,
$$

with constants $a,b,d,e$ depending only on the relative translation rate.

Compute how derivatives transform (chain rule):

$$
\partial_x = a\,\partial_{x'} + d\,\partial_{t'},\qquad
\partial_t = b\,\partial_{x'} + e\,\partial_{t'}.
$$

Now impose wave-operator invariance in 1D:

$$
\partial_t^2 - c^2 \partial_x^2 = \lambda\left(\partial_{t'}^2 - c^2 \partial_{x'}^2\right).
$$

Expand the left-hand side:

$$
(b\partial_{x'} + e\partial_{t'})^2 - c^2(a\partial_{x'} + d\partial_{t'})^2.
$$

Collect coefficients of $\partial_{x'}^2$, $\partial_{x'}\partial_{t'}$,
$\partial_{t'}^2$:

1) Mixed term must vanish (since the RHS has no $\partial_{x'}\partial_{t'}$):


$$
2(be - c^2 a d)=0
\quad\Longrightarrow\quad
be = c^2 a d.
$$

2) Coefficients must match $\lambda(\partial_{t'}^2 - c^2\partial_{x'}^2)$:


$$
e^2 - c^2 d^2 = \lambda,
$$

$$
b^2 - c^2 a^2 = -\lambda c^2.
$$

Now identify the relative translation rate $v$ by the motion of the
primed origin $x'=0$:

$$
0 = a x + b t \quad\Rightarrow\quad x = -\frac{b}{a}t,
\qquad v := \frac{dx}{dt} = -\frac{b}{a}.
$$

So $b = -a v$.

Use $be=c^2ad$:

$$
(-av)e = c^2 a d \quad\Rightarrow\quad d = -\frac{v e}{c^2}.
$$

Plug into $e^2 - c^2 d^2 = \lambda$:

$$
e^2 - c^2\left(\frac{v^2 e^2}{c^4}\right)=\lambda
\quad\Rightarrow\quad
e^2\left(1-\frac{v^2}{c^2}\right)=\lambda.
$$

Plug $b=-av$ into $b^2 - c^2 a^2 = -\lambda c^2$:

$$
a^2 v^2 - c^2 a^2 = -\lambda c^2
\quad\Rightarrow\quad
a^2\left(1-\frac{v^2}{c^2}\right)=\lambda.
$$

Thus $a^2=e^2$. Choose the orientation-preserving branch
$a=e$. Fix the overall scale by choosing $\lambda=1$ so that the
inverse has the same form. Then

$$
a=e=\gamma,\qquad \gamma:=\frac{1}{\sqrt{1-\frac{v^2}{c^2}}},
$$

and therefore

$$
b=-\gamma v,\qquad d=-\gamma\frac{v}{c^2}.
$$

We have derived the unique linear mixing forced by $\mathcal{O}_c$ invariance:

$$
x'=\gamma(x-vt),\qquad
t'=\gamma\left(t-\frac{v}{c^2}x\right),\qquad
y'=y,\quad z'=z.
$$

This is the precise sense in which “hyperbolic mixing” is not assumed: it is
forced by preserving the Maxwell transport operator.


## Hyperbolic velocity composition follows immediately (no Galilean c±v)

Let a signal or feature move with $u=dx/dt$.

Differentiate:

$$
dx'=\gamma(dx-v\,dt),
$$

$$
dt'=\gamma\left(dt-\frac{v}{c^2}dx\right).
$$

Thus

$$
u'=\frac{dx'}{dt'}=\frac{u-v}{1-\frac{uv}{c^2}}.
$$

In particular, if $u=c$, then $u'=c$:

$$
\frac{c-v}{1-\frac{v}{c}}=c.
$$

This is the exact point where the classical ether-drift argument fails: it uses
additive composition $u\mapsto u\pm v$, which contradicts the operator
invariance of Maxwell transport.


## Virtual observer at the end of an arm: why v<c is forced

Place a virtual observer co-moving with the mirror at the end of an arm. If the
mirror recedes at speed $v\ge c$ relative to the background description,
then no Maxwell wavefront emitted from the beam splitter can ever intersect it.
Thus closure of the measurement requires

$$
v<c.
$$

This is a pure transport-closure constraint: finite transport cannot catch a
receding boundary faster than the transport rate itself.


## Michelson–Morley recomputed with Maxwell-consistent bookkeeping

We now recompute the round-trip time difference that Michelson–Morley intended
to detect.

The experiment tests whether the predicted arm-time asymmetry from a Galilean
ether-drift model is real. It does not test “space curvature.” It tests whether
Maxwell transport behaves like Galilean projectile transport. It does not.

We proceed as follows:

- Let the apparatus be at rest in the primed description $(t',x',y',z')$.
- Let the arm lengths measured in that apparatus description be $L$
  (parallel) and $L$ (perpendicular).
- Light propagation in vacuum satisfies $\mathcal{O}'_c\Phi=0$ in the primed
  description, so the transport rate is $c$ in all directions in
  that description.


Because interference is evaluated at a single recombination event (the same
physical event), the predicted phase difference is description-independent.
Therefore, computing the arm times in the apparatus description is sufficient.


### Parallel arm (apparatus description)

Outbound: distance $L$ at transport rate $c$ gives

$$
T'_{\parallel,\text{out}}=\frac{L}{c}.
$$

Return: same distance and same rate gives

$$
T'_{\parallel,\text{back}}=\frac{L}{c}.
$$

Hence

$$
T'_\parallel = \frac{2L}{c}.
$$


### Perpendicular arm (apparatus description)

Identical logic:

$$
T'_\perp = \frac{2L}{c}.
$$

Thus the predicted round-trip difference is

$$
\Delta T' := T'_\parallel - T'_\perp = 0.
$$

This null result is not obtained by postulating length contraction. It is
obtained because the apparatus description is constrained to preserve the
Maxwell transport operator, which fixes the transport structure and forbids the
Galilean $c\pm v$ timing model.


## Why the Galilean triangle timing produces a false asymmetry

The classic ether-wind computation implicitly mixes two incompatible rules:

- It uses Galilean addition (projectile intuition) to assign different forward
  and backward speeds $c\pm v$ along the parallel arm.
- It uses a Euclidean velocity triangle for the perpendicular arm.


But Maxwell-consistent transport does not allow that mixture.

The correct rule is: the transport PDE is preserved. That forces the hyperbolic
composition law, and it forces the re-description mixing derived above.

Once you enforce $\mathcal{O}_c=\lambda\mathcal{O}'_c$, the “c±v” step is not
available, so the predicted asymmetry disappears at its source.


## Why rotation does not change a back-and-forth interferometer outcome

A Michelson interferometer compares two *two-way* (out-and-back) times along two
orthogonal arms of equal length.

Under the Maxwell-consistent re-description above, the two-way time in the
apparatus description depends only on the arm length and $c$:

$$
T'_{\text{two-way}}=\frac{2L}{c},
$$

independent of arm orientation.

Therefore rotating the apparatus does not change the predicted two-way timing
difference: the null result is rotation-invariant.

This is different from configurations that compare *one-way* transport around a
loop (e.g. Sagnac-type loops): there the observable is sensitive to circulation
around an enclosed area and to rotation. Michelson–Morley is a symmetric
back-and-forth comparison and therefore is insensitive to pure rotation in the
ideal limit.


## Conclusion

Michelson–Morley attempted to detect a Galilean ether-drift asymmetry. That
asymmetry is derived by assuming additive velocity composition $c\pm v$.

Source-free Maxwell transport forbids that assumption: preserving the Maxwell
wave operator forces hyperbolic mixing and hyperbolic velocity composition.

With Maxwell-consistent bookkeeping, the two arm round-trip times are equal in
the apparatus description, and the null result follows without any additional
postulates.
