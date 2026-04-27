# Ultrareal Numbers

An ultrareal number is a positive square-form:

$$
U = u^2
$$

The number is $U$. The inner magnitude is $u\ge0$. The
full inner state is $ue^{i\phi}$. The unrotated case has $\phi=0$,
so $ue^{i0}=u$.

More generally, a capital $N$ names a number:

$$
N = n^2
$$

In ordinary use, numbers are densities. They are visible values instantiated in
what we handle: things counted, amounts measured, values assigned, distances
crossed, times waited, balances owed or received. The square-form says that the
handled number is the visible density; the lower-case symbol names the inner
magnitude behind that density.

This is not a trick of notation. Every positive number can be seen as a square,
and this way of seeing separates two layers:

$$
\begin{aligned}
\text{visible value:}\quad &U,\\
\text{inner magnitude:}\quad &u,\\
\text{inner state:}\quad &ue^{i\phi}.
\end{aligned}
$$

The basic ultrareal domain is the set of visible square-values:

$$
UR = \{u^2 \mid u\in\mathbb R_{\ge0}\}=[0,\infty).
$$

Here $u$ is the inner magnitude. It is not a negative quantity. The
phase is always present:

$$
ue^{i\phi}.
$$

When there is no turn, $\phi=0$. When orientation, opposition, or return
has to be represented, $\phi$ changes. The magnitude remains
$u\ge0$.

So ultrareals are positive square-forms: nonnegative, and positive except at
zero. They are numbers as values or magnitudes. They are not absences or
removals. Opposition is a relation between positive ultrareals, carried by
orientation in the inner layer.

For every ultrareal, the modulus is the value itself:

$$
|U| = U = u^2 \ge 0.
$$

It vanishes only at zero:

$$
|U|=0 \quad\Longleftrightarrow\quad U=0.
$$

This is the precise square-form sense in which the ultrareal layer is positive
definite.

This matches ordinary experience. Existing things appear as positive values. We
meet an apple, not a negative apple. We meet a block, not a negative block. When
an apple is taken from a dozen, that apple does not vanish into numerical
oblivion. If the dozen becomes eleven, one apple has been re-turned somewhere:
eaten, stored, owed, moved, or counted from another side of the relation. In
this sense, turning and rotation let arithmetic represent real changes without
pretending that existing things disappear into negative existence.

Debt should not be placed in a minus layer. Debt $D$ is a positive
future claim:

$$
D = d^2
$$

Debt is value assigned to future settlement. It exists positively as an
obligation, claim, record, or relation. Only a bookkeeping view assigns a minus
sign to one side of that positive relation.

If a language names a "negative-apple," then the named thing is still positive
as a unit: one negative-apple is one positive unit of the kind negative-apple. A
thing can be called "negative" by role, direction, opposition, debt, or
bookkeeping side, but existence itself remains positive.

The sign belongs to the label, role, direction, or relation. It does not make
the existing unit negative.

**There are no negative ultrareals.**

This does not mean a square-value can never carry a minus sign in ordinary
notation. It means that such notation describes a rotated presentation, not an
ultrareal value produced by a negative inner magnitude.

The proof is direct. Let $U$ be a nonzero ultrareal:

$$
U=u^2,\qquad u\in\mathbb R_{\ge0},\qquad U>0.
$$

For any allowed inner magnitude $r\in\mathbb R_{\ge0}$, the square is
nonnegative:

$$
r^2\ge0.
$$

Therefore no allowed inner magnitude can produce the minus-signed visible value
of a positive ultrareal. If such an $r$ existed, then:

$$
r^2=-U.
$$

But the left side is nonnegative and the right side is below zero in ordinary
signed notation. So a minus-signed visible value is not produced by an allowed
inner magnitude.

To obtain the ordinary minus-signed presentation of $U$, the inner
state must take a quarter-turn:

$$
i=e^{i\pi/2}.
$$

Then:

$$
(iu)^2=(e^{i\pi/2}u)^2=e^{i\pi}u^2.
$$

The factor $e^{i\pi}$ is the unit half-turn. Ordinary notation writes that
half-turn with the minus sign. The sign is therefore the description of a
rotation, not the discovery of a negative ultrareal.

The conclusion is:

$$
u\in\mathbb R_{\ge0} \Longrightarrow u^2\in UR,
\qquad
ue^{i0}=u,
\qquad
ue^{i\phi} \text{ carries phase, not negative magnitude.}
$$

Thus $(iu)^2$ is not a basic ultrareal value. It is a square-value
returned through a non-real turn in the inner layer and then described with the
ordinary minus sign.

The claim is not that old algebra cannot manipulate minus signs. The claim is
that the ultrareal layer has no negative magnitude. Minus signs mark rotation,
opposition, removal, cancellation, or comparison in the layer beneath positive
value.

## Self-Return and Magnitude

The full inner state is:

$$
z=ue^{i\phi}.
$$

The raw square of this state is:

$$
z^2=(ue^{i\phi})^2=u^2e^{i2\phi}.
$$

So the raw square is not generally the ultrareal value $u^2$. It is a rotated
square-presentation:

$$
u^2e^{i2\phi}=u^2(\cos 2\phi+i\sin 2\phi).
$$

The positive ultrareal value is obtained by pairing the state with its return:

$$
U=z\bar z.
$$

Since:

$$
\bar z=ue^{-i\phi},
$$

we have:

$$
\begin{aligned}
z\bar z
&=(ue^{i\phi})(ue^{-i\phi})\\
&=u^2e^{i\phi-i\phi}\\
&=u^2.
\end{aligned}
$$

Back-expanded through Euler's form, the same calculation is:

$$
\begin{aligned}
z\bar z
&=u^2(\cos\phi+i\sin\phi)(\cos\phi-i\sin\phi)\\
&=u^2(\cos^2\phi+\sin^2\phi)\\
&=u^2.
\end{aligned}
$$

The conjugate is therefore not an arbitrary mathematical trick. It is the
inverse turn: the state meeting its own return. The result behaves like a
standing-wave-like magnitude. A phase and its reverse do not travel away from
one another in the value; they close into a stationary positive density.

This does not mean numbers are literally physical waves. It means the
ultrareal value is a self-returning magnitude, while phase remains available for
relation.

When two states are joined, phase no longer cancels as self-phase. Let:

$$
z_1=ue^{i\phi_1},\qquad z_2=ve^{i\phi_2}.
$$

Then:

$$
\begin{aligned}
|z_1+z_2|^2
&=(z_1+z_2)(\bar z_1+\bar z_2)\\
&=u^2+v^2\\
&\quad+uv\left(e^{i(\phi_1-\phi_2)}+e^{-i(\phi_1-\phi_2)}\right)\\
&=u^2+v^2+2uv\cos(\phi_1-\phi_2).
\end{aligned}
$$

Self-phase cancels in a single ultrareal. Relative phase remains between
ultrareals, and that remaining relation is the interaction term.
