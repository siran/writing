---
title: A Maxwell Universe – Appendix A: Newton’s Method and the Invention of Mass
date: 2026-01-01 10:20
---


# Appendix A: Newton’s Method

Throughout this text, we have argued that mass is an operational parameter—a
coefficient of change—rather than a primitive substance. To see why this
distinction matters, it helps to look at how Isaac Newton actually formulated
his dynamics.

Modern textbooks condense Newton’s Second Law into the crisp algebraic equation

$$
F = ma.
$$

Newton does not present the law in this algebraic form. In the *Principia* he
states it verbally:


> “The alteration of motion is ever proportional to the motive force impressed…”
> [^1]


[^1]: Newton, I. (1687). *Philosophiæ Naturalis Principia Mathematica*. Axioms,
or Laws of Motion, Law II. (Trans. Andrew Motte, 1729).

And he frames the whole work in a classical geometric style. Newton even says
explicitly why he does this:


> “…to avoid disputes about the method of fluxions, I have composed the
> demonstrations… in a geometrical way…” [^2]


[^2]: Newton, I. (1715). "Account of the Book entitled Commercium Epistolicum D.
Johannis Collins, & aliorum de Analysi Promota". *Philosophical Transactions of
the Royal Society*, 29(342), 173–224. (Published anonymously). Note: This
admission appears in Newton’s anonymous review of the *Commercium Epistolicum*,
the document central to his priority dispute with Leibniz. In it, he candidly
admits that the geometric style of the *Principia* was a strategic choice to
avoid controversy over his new calculus methods.

So the *Principia* is not “algebra-first physics.” It is *geometry-first
physics*, with the calculus largely kept out of view.


## The Hidden Calculus

Newton’s dynamics are powered by a flow-based view of quantities. In his own
words (in the *intended preface* / fluxional framing):


> “Quantities increasing by continuous flow we call fluents, the speeds of
> flowing we call fluxions and the momentary increments we call moments.” [^3]


[^3]: Newton, I. (1736). *The Method of Fluxions and Infinite Series; with its
Application to the Geometry of Curve-lines*. Preface. (Trans. John Colson).
[Written c. 1671].

This is the stance: reality is described as *generation by flow*. To see the
engine of this discovery, we must look at the "moment" ($o$)—an infinitely small
interval of time.

When Newton derived relationships, he did so by letting time flow forward by
this tiny moment. For example, to find the rate of change of a quantity
$y = x^2$, he would increment the fluent $x$ by its momentary change $\dot{x}o$:

$$
(y + \dot{y}o) = (x + \dot{x}o)^2
$$

Expanding this yields:

$$
y + \dot{y}o = x^2 + 2x\dot{x}o + (\dot{x}o)^2
$$

Subtracting the original state ($y=x^2$) leaves the change:

$$
\dot{y}o = 2x\dot{x}o + \dot{x}^2 o^2
$$

Dividing by the tiny time interval $o$:

$$
\dot{y} = 2x\dot{x} + \dot{x}^2 o
$$

Finally, Newton argued that as the moment $o$ vanishes (becomes "evanescent"),
the last term disappears, leaving the exact dynamic relationship:

$$
\dot{y} = 2x\dot{x}
$$

That is exactly the intuition behind the “moment” computation: take the
relation, advance by a vanishing moment, and keep only what survives as the
moment goes to zero.


## Mass as a Coefficient of Flow

Newton introduces “quantity of matter” (mass) as a *measurable factor* that lets
motion be accounted for consistently. His basic operational definition of matter
already reads like a recipe:


> “Quantity of matter is the measure of the same, arising from its density and
> bulk conjointly.” [^4]


[^4]: Newton, I. (1687). *Philosophiæ Naturalis Principia Mathematica*.
Definition I.

Then, crucially, he defines *quantity of motion* (momentum) as a product-like
measure:


> “The quantity of motion is the measure of the same, arising from the velocity
> and quantity of matter conjointly.” [^5]


[^5]: Newton, I. (1687). *Philosophiæ Naturalis Principia Mathematica*.
Definition II.

So mass is not introduced as mystical “stuff.” It enters as the coefficient
needed so that “motion” (momentum) scales with velocity in the right way.

In that precise sense: **dynamics comes first; mass is the invented coefficient
that linearizes the bookkeeping of change.**

In a Maxwell Universe, we return to this priority. The fundamental “flow” is
electromagnetic energy–momentum flow. What we call “mass” is the effective
resistance to changing that flow—arising when flux is knotted into a stable
topology.
