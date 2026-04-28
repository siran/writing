# ANA Handoff 04-28

Repo: `C:\Users\an\src\siran\writing`

Book: `books/A New Arithmetic`

This handoff summarizes the current direction of *A New Arithmetic* so a new
agent can continue without restarting the conceptual work.

## Current State

The book is defining **ultrareal arithmetic**. The goal is a formal,
authoritative, logically ordered short book. The intended order is:

1. Define ultrareals.
2. Prove basic closure facts.
3. Show addition exposes an interaction term.
4. Recover standard arithmetic as a special case.
5. Introduce orientation, opposition, Euler notation, and unfolding later.

Do not run builds unless asked. The user uses `make watch`.

## Ultrareals

An ultrareal is a positive square-form:

```math
U=u^2,\qquad u\ge0.
```

Use `\mathbb U`, not `UR`.

The upper-case symbol names the visible ultrareal value. The lower-case symbol
names the inner value/state.

The ultrareal layer is the positive real line with zero included:

```math
\mathbb U=[0,\infty).
```

There are no negative ultrareals.

## Addition

Do not introduce a special sum symbol. The symbol `+` is term-type aware. The
operation is `+(.,.)`: lower-case terms add as inner states, and upper-case
ultrareals return the square-form determined by those inner states.

For ultrareals:

```math
U=u^2,\qquad V=v^2,
```

the ultrareal sum is:

```math
+(U,V)=U+V=(+(u,v))^2=(u+v)^2.
```

Do not frame this as a separate addition concept.

Expansion:

```math
U+V=(u+v)^2=uu+uv+vu+vv.
```

Since:

```math
u^2=uu,\qquad v^2=vv,
```

the middle terms are:

```math
uv+vu.
```

These are the interaction/relation between the parts:

```math
d(U,V)=uv+vu.
```

Standard arithmetic is recovered when this interaction term is not taken into
account / vanishes:

```math
d(U,V)=0,
```

so:

```math
U+V=u^2+v^2.
```

Do not frame `u^2+v^2` as the main definition of ultrareal addition. It is the
ordinary visible reading / recovered non-interaction case.

## Descriptor

The descriptor is not scalar `kappa`; avoid `kappa`.

Descriptor:

```math
d(U,V)=uv+vu.
```

Common commutative scalar case:

```math
uv=vu,\qquad d(U,V)=2uv.
```

Angular case:

```math
d(U,V)=2uv\cos\Delta.
```

Complete opposition:

```math
d(U,V)=-2uv.
```

Zero interaction:

```math
d(U,V)=0.
```

## Interaction Notation

When emphasizing the descriptor, the same sum may be written:

```math
U\,d\,V=uu+uv+vu+vv.
```

This is not a new operation replacing `+`. It is notation displaying the
interaction. Do not invent `\oplus`, `+_d`, or any special sum.

## Commutativity And Associativity

Do not impose commutativity or associativity from the beginning.

Use commutativity, associativity, and distributivity when the arithmetic of the
particular use case supplies them. The bare ultrareal definition does not need
extra laws imposed before the relevant terms have been specified.

The aim is to model the arithmetic aspect of reality, where relation can
matter.

## Preface Direction

The preface should be readable and not proof-heavy.

It should say:

- `1+1` is not necessarily only `2`.
- There is also an interaction term, and it need not always be zero.
- Positive numbers can be written as square-forms:

```math
U=u^2,\qquad V=v^2.
```

- The usual visible reading gives:

```math
U+V=u^2+v^2.
```

- The ultrareal square-form reading gives:

```math
U+V=(u+v)^2=uu+uv+vu+vv.
```

- Therefore `uv+vu` is the relation `d(.,.)` between the parts.
- Standard arithmetic is recovered when the interaction term is not taken into
  account.
- Later chapters rigorously define ultrareals, prove closure, and give
  examples.
- Do not assert density too early. Say later the book shows why an everyday
  real number may be read as a density.

## Orientation

There are no negative ultrareals.

`-1` is not used as in `-1<0` inside the ultrareal layer. It is notation for
opposition / half-turn in presentation.

`i` is a map-side presentation device, a useful geometric trick for
turn/opposition, not an ultrareal value.

```math
i^2=-1.
```

Since `-1` is not positive, `\sqrt{-1}` is not an ultrareal.

Once orientation is available, numbers themselves can be rotated. Orientation
belongs to presentation, not to the base definition of a lone ultrareal.

A lone ultrareal has natural inner state:

```math
u
```

not `ue^{i\phi}`.

Relative difference/opposition is denoted:

```math
\Delta
```

not `\phi`.

## Return Product

Current direction:

```math
z=ue^{i\alpha},\qquad z^*=ue^{-i\alpha}.
```

Return product:

```math
zz^*=u^2.
```

Explain this as return/recovery of positive square-form, not as an ad hoc
"complex conjugate."

The user objected to overcorrecting this with standard complex-geometry
language. Keep return and opposition distinct:

```math
\text{return:}\qquad \alpha\mapsto-\alpha,
```

while exact opposition is a half-turn:

```math
\text{opposition:}\qquad \alpha\mapsto\alpha+\pi.
```

Do not write exact opposition as `\alpha` vs `-i\alpha`.

## Recently Added Files

Recent book files to preserve:

- `books/A New Arithmetic/A New Arithmetic - 002b Multiplication and Powers.md`
- `books/A New Arithmetic/A New Arithmetic - 006 Unfolding.md`
- `books/A New Arithmetic/A New Arithmetic - 005 Rotation, Opposition, and Signs.md`

Do not revert. Review/edit with care.

The renderer collects book `*.md` files alphabetically.

## Review Notes

The new `Unfolding` chapter is promising. It gives the book a spine:
`\mathbb R` and `\mathbb C` are unfoldings/presentations of `\mathbb U`, not new
value layers.

The new multiplication chapter is useful, but should state when it is working
in the ordinary scalar inner-state case. Commutativity, associativity, and
distributivity can be accepted there because that arithmetic supplies them. If
it discusses descriptors, state the compatibility assumptions clearly in the
book's own terms rather than calling ultrareal addition a separate operation.

For power series: if coefficients are positive, the value can stay in the
ultrareal layer when it converges. Signed/complex coefficients should be
explained as rotations/presentations/descriptors, not silently treated as
ultrareal values.

## Process Notes

The user is iterating fast and is sensitive to framing.

Avoid:

- language that treats addition as two separate operations
- invented special sum symbols
- `UR`
- `kappa`
- defining a lone ultrareal with rotation
- treating `-1` as a negative ultrareal
- asserting density before it is grounded

Prefer:

- precise text edits
- short conceptual review
- keeping the proof burden in the rigorous chapters
- preserving the user's new files unless explicitly asked to change them

If asked to finish work, commit and push per repo instructions. If asked for
review only, do not edit unless requested.
