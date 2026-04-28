# Preface: A New Arithmetic

The first claim of this book is simple:

$$
1 + 1 \text{ is not necessarily only } 2.
$$

There is also an interaction term, and it need not always be zero.

This depends on a choice in mathematics that is not as obvious as it first
appears.

If two real numbers are positive, with zero included, they can be written as
square-forms:

$$
U=u^2,\qquad V=v^2.
$$

If we consider the sum $U+V$ and read only the visible square-values, the usual
answer is immediate:

$$
U+V=u^2+v^2.
$$

That is the standard visible reading. It counts the two square-values.

But the same terms also carry their square-form definition:

$$
U=u^2.
$$

When the same $+$ is read with the square-forms in view, $U+V$ is again a
positive number, and as such it can be written as a square-form. The inner
expression of the sum is:

$$
u+v.
$$

Therefore:

$$
U+V=(u+v)^2=uu+uv+vu+vv.
$$

Since $u^2=uu$ and $v^2=vv$, the question becomes: what is

$$
uv+vu?
$$

Those middle terms are the relation $d(\cdot,\cdot)$ between the parts, the
interaction term that the ordinary visible reading does not take into account.
Numbers treated this way are ultrareals.

The standard arithmetic that we love is not wrong. It is recovered when the
interaction term is not taken into account. This book describes a broader
arithmetic in which a number is first written as a positive square-form:

$$
N=n^2.
$$

The value $N$ is always nonnegative. The lower-case $n$ is the inner value. The
upper-case $N$ is the visible square-value.

Later, after the definition and examples are in place, the book will show what
an ultrareal number is and why a real number from everyday context may be read
as a density.

## What This Book Will Do

First, the book defines ultrareal numbers rigorously as positive square-forms,
with zero included:

$$
U=u^2,\qquad u\ge0.
$$

Second, it proves basic facts about them. In particular, it proves that the
term-type-aware sum of two ultrareals is another ultrareal. The same operation
$+(\cdot,\cdot)$ is read through the terms supplied to it: lower-case terms add
as inner states, while upper-case ultrareals return the square-form determined
by those inner states:

$$
U+V=(u+v)^2.
$$

Third, the book keeps algebraic assumptions explicit. Commutativity,
associativity, and distributivity may be used when the arithmetic of the
particular case supplies them. They are not imposed as extra requirements before
the relevant terms have been specified. When the relevant inner product
distributes, the square can be expanded:

$$
(u+v)^2=u^2+uv+vu+v^2.
$$

The middle terms are not decoration. They are the relation $d(\cdot,\cdot)$
between the parts:

$$
d(U,V)=uv+vu.
$$

When that relation vanishes, ordinary arithmetic is recovered.

Finally, the book introduces orientation. To notate turn and opposition, we
adjoin the symbol $i$, with $i^2=-1$, and use Euler's identity. Here the symbol
$-1$ is not being used as in $-1<0$, since there are no negative ultrareals. It
is a notation convenience, a useful geometric trick on the map of
presentations. In this role, $i$ belongs on the presentation side of the
notation: it records a turn. It is not itself an ultrareal. We know
$\sqrt{-1}$ is not ultrareal, since $i^2=-1$ is not a positive number.

Once orientation is available, numbers themselves can be rotated. A half-turn
looks the same from the square-form: front and back return the same value. A
quarter-turn is different: it is sideways, orthogonal to the ordinary positive
line.

That sideways orthogonality gives meaning to the return product:

$$
n n^*.
$$

The symbol $n^*$ is not an ad hoc complex conjugate. It is the reverse-oriented
inner state, the return needed to recover the positive value from a rotated
presentation. This is how signs, opposition, orthogonality, and ordinary
arithmetic fit inside one positive square-form account.
