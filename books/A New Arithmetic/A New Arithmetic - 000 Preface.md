# Preface: A New Arithmetic

The first claim of this book is simple:

$$
1 + 1 \text{ is not necessarily only } 2.
$$

There may also be a relation term.

Ordinary arithmetic is not wrong. It is a recovered case: the arithmetic of
quantities treated as non-interacting parts. This book describes a broader
arithmetic in which a number is first a positive square-form, and the same
symbol $+$ can act at the layer named by its operands.

The numbers described here are called *ultrareal numbers*. An ultrareal number
is written:

$$
U = u^2,\qquad u\ge 0.
$$

The capital letter names the visible value. The lower-case letter names the
inner magnitude, or natural inner state. The ultrareal domain is the positive
real line with zero included:

$$
\mathbb U=\{u^2\mid u\in\mathbb R_{\ge0}\}=[0,\infty).
$$

The point is not that ordinary nonnegative real numbers have been renamed. The
point is that the square-form separates visible value from inner magnitude. Once
that distinction is explicit, addition can ask a more precise question. Are the
lower-case inner states being joined? Are the upper-case visible values being
counted without interaction? Or are upper-case ultrareals being joined through a
specified relation?

For two ultrareals,

$$
U=u^2,\qquad V=v^2,
$$

upper-case addition is lifted from the inner states:

$$
U+V := (u+v)^2.
$$

If the inner-state product distributes, this expands as:

$$
(u+v)^2=u^2+uv+vu+v^2.
$$

The two middle terms are the interaction descriptor:

$$
d(U,V):=uv+vu.
$$

So the same rule can be written:

$$
U+V=u^2+d(U,V)+v^2.
$$

When the descriptor is being emphasized, the same joined value may be written:

$$
U\,d\,V := uu+uv+vu+vv.
$$

Since $uu=u^2$ and $vv=v^2$:

$$
U\,d\,V=U+V=u^2+d(U,V)+v^2.
$$

This is not a different arithmetic operation. It is the interaction notation
for the same overloaded addition.

In common commutative scalar cases, $uv=vu$, so:

$$
U+V=u^2+v^2+2uv.
$$

In angular or otherwise projected scalar cases, the descriptor may be
normalized by a coefficient $\kappa$:

$$
d(U,V)=uv+vu\rightsquigarrow 2\kappa uv.
$$

Then the common scalar reduction is:

$$
U+V=u^2+v^2+2\kappa uv.
$$

This is not a separate addition operator. It is a reduction of the same
overloaded $+$ after the relation of the inner states has been specified.

When the projected coefficient is $\kappa=0$, the interaction term vanishes and
ordinary addition is recovered:

$$
U+V=u^2+v^2.
$$

When $\kappa=1$, the parts are aligned. When $\kappa=-1$, the parts are
opposed:

$$
U+V=(u+v)^2,\qquad U+V=(u-v)^2.
$$

Thus the novelty is not the binomial identity. The novelty is the placement of
that identity inside arithmetic: the cross term is treated as relation data, not
as an accidental expansion.

For angular or phase-like quantities, the normalized coefficient is often
written:

$$
\kappa=\cos\Delta,
$$

where $\Delta$ is the relative difference between two oriented inner
presentations. The angle is not part of the definition of a lone ultrareal. A
single ultrareal has natural inner state $u$. Orientation is introduced only
when the problem being modeled requires it.

This distinction matters for signs. There are no negative ultrareals. The base
domain is $\mathbb R_{\ge0}$. To notate opposition and turn, one may adjoin the
symbol $i$ with $i^2=-1$. That notation records presentation or relation. It
does not create a negative member of $\mathbb U$. Inside the ultrareal layer,
value remains positive, with zero included as the boundary.

The physical analogy is energy. Energy-like quantities are positive
square-values. Their amplitudes may align, oppose, or carry phase, but the
measured density remains nonnegative. Ultrareal arithmetic abstracts that
pattern: keep value positive, keep relation explicit, and recover ordinary
arithmetic when relation is zero.

The book proceeds in that order. First it defines ultrareal numbers. Then it
defines overloaded addition by layer. Then it states the admissibility condition
that keeps joined values inside $\mathbb U$. Only after that does it introduce
angular difference, Euler notation, opposition, and signs.
