# Preface: Ultrareal Numbers

So the first claim of this book is simple:

```text
1 + 1 is not necessarily only 2.
```

There is also an interaction term.

This book describes ultrareal numbers: numbers that are never negative.

More specifically, an ultrareal number is a positive square-form:

```text
U = u^2
```

The capital `U` names the visible value. The lower-case `u` names the inner value.

This book also uses the capital word *Number* for the values we handle directly. A Number is not first met as an isolated mark. A Number is instantiated in something: a counted thing, a measured amount, a balance, a distance, a duration, a density, a value.

In this sense, Numbers as we know them are densities. They are visible positive values carried by actual instances. In ultrareal notation, a Number appears as:

```text
N = n^2
```

The capital `N` is the visible Number. The lower-case `n` is its inner value.

The word *real* matters: ultrareals are only positive.

The word *ultra* matters too. Ultrareals are not merely the usual real numbers renamed. They keep track of something standard arithmetic does not represent: the relation between numbers being added.

One could call them superreal numbers. I use *ultrareal* because the letter `U` is the natural symbol for the visible positive square-form:

```text
U = u^2
```

Also, *ultra* points beyond the usual negative extension of the number line. In reality there are no negative things. There is no such thing as a negative apple that gets added to a dozen:

```text
12 + (-1) = 11
```

The symbol `-1 < 0` does not name an ultrareal. It names an operation, direction, cancellation, comparison, or rotation applied to positive values.

Standard arithmetic studies numbers as non-interacting. In that model, addition behaves like the mathematical union of sets: the parts are placed together, and the relation term is not part of the calculation.

In ultrareal arithmetic, this becomes a special case: the case where the relation term is zero.

```text
d(U,V) = 0
```

Once relation is admitted as part of the arithmetic data, the operator `+` is overloaded. It is aware of the parts being added: the visible ultrareals `U` and `V`, their inner values `u` and `v`, and their interaction descriptor `d(U,V)`.

The general two-term form is:

```text
U + V = u^2 + v^2 + 2d(U,V)uv
```

where:

```text
U = u^2
V = v^2
```

and `d(U,V)` has values:

```text
-1 <= d(U,V) <= 1
```

Usually `d(U,V)` measures alignment between `U` and `V`.

The important cases are:

```text
d(U,V) =  1   aligned joining
d(U,V) =  0   non-interaction
d(U,V) = -1   opposition
```

So:

```text
aligned:        U + V = (u + v)^2
standard:       U + V = u^2 + v^2
opposed:        U + V = (u - v)^2
```

To see the aligned case directly, start with two ultrareals:

```text
U = u^2
V = v^2
```

Aligned addition first joins the inner values, then squares:

```text
U + V = (u + v)^2
```

Expanding gives:

```text
(u + v)^2 = u^2 + v^2 + 2uv
```

The term `2uv` is the interaction term.

Standard arithmetic is not thrown away. It is recovered as:

```text
d(U,V) = 0
```

The difference is that ultrareal arithmetic does not require the interaction descriptor to be zero.

In this sense, addition makes the parts whole through interaction.

This is why addition is different from just uniting sets and counting. Union says that parts are considered together. Addition asks what whole is produced when the parts are brought into relation.

The same distinction clarifies negative numbers. There are no negative ultrareals. A negative value is not a negative real thing. It is a rotated square-value. We can use the machinery developed around `sqrt(-1)` to write how a positive number can be rotated through the imaginary direction:

```text
-U = (iu)^2
```

because:

```text
i^2 = -1
```

The central claim can now be stated more exactly:

```text
1 + 1 is not necessarily only 2
```

because `2` is the non-interaction case:

```text
d(1,1) = 0
1 + 1 = 2
```

Other relations give other wholes:

```text
d(1,1) =  1   gives   1 + 1 = 4
d(1,1) = -1   gives   1 + 1 = 0
```

When the parts interact, the whole includes the interaction term.
