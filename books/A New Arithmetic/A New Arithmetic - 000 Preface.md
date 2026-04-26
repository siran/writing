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

The word *real* matters: ultrareals are only positive.

The word *ultra* matters too. Ultrareals are not merely the usual real numbers renamed. They keep track of something standard arithmetic usually suppresses: the relation between numbers being added.

One could call them superreal numbers. I use *ultrareal* because the letter `U` is the natural symbol for the visible positive square-form:

```text
U = u^2
```

Also, *ultra* points beyond the usual negative extension of the number line. In reality there are no negative things. There is no such thing as a negative apple that gets added to a dozen:

```text
12 + (-1) = 11
```

The symbol `-1 < 0` does not name an ultrareal. It names an operation, direction, cancellation, comparison, or rotation applied to positive values.

Standard arithmetic legitimately treats numbers as non-interacting. In the ultrareals, this becomes a special case: the case where the relation term is zero.

```text
k = 0
```

Once relation is admitted as part of the arithmetic data, the general two-term form is:

```text
U +_{k} V = u^2 + v^2 + 2kuv
```

where:

```text
U = u^2
V = v^2
```

and `k` is an interaction descriptor with values:

```text
-1 <= k <= 1
```

Usually `k` measures alignment between `U` and `V`.

The important cases are:

```text
k =  1   aligned joining
k =  0   non-interaction
k = -1   opposition
```

So:

```text
aligned:        U +_{1} V = (u + v)^2
standard:       U +_{0} V = u^2 + v^2
opposed:        U +_{-1} V = (u - v)^2
```

To see the aligned case directly, start with two ultrareals:

```text
U = u^2
V = v^2
```

Aligned addition first joins the inner values, then squares:

```text
U +_{1} V = (u + v)^2
```

Expanding gives:

```text
(u + v)^2 = u^2 + v^2 + 2uv
```

The term `2uv` is the interaction term.

Standard arithmetic is not thrown away. It is recovered as:

```text
k = 0
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
1 +_{0} 1 = 2
```

Other relations give other wholes:

```text
1 +_{1} 1 = 4
1 +_{-1} 1 = 0
```

When the parts interact, the whole includes the interaction term.

