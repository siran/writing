---
title: A Maxwell Universe – Appendix A: Newton’s Method and the Invention of Mass
date: 2026-01-01 10:20
---


# Appendix A: Newton’s Method

Throughout this text, we have argued that mass is an operational parameter—a
coefficient of change—rather than a primitive substance. To understand why this
distinction matters, it is illuminating to look at how Isaac Newton actually
formulated his dynamics.

Modern textbooks condense Newton’s Second Law into the crisp algebraic equation:

$$
F = ma
$$

However, Newton never wrote this equation. In fact, the *Principia* (1687)
contains almost no algebra in the modern sense. It is written entirely in the
language of Euclidean geometry, using ratios, proportions, and limits of
geometric shapes.

Newton did this because algebra was considered less rigorous at the time. To
convince his peers, he had to prove his new physics using the ancient, trusted
tools of Greek geometry.

But this geometric presentation hid the true engine of his discovery: the
**Method of Fluxions**.


## The Hidden Calculus

Newton viewed the universe not as a static collection of shapes, but as a system
in continuous motion. He did not think in terms of static variables ($x, y$),
but in terms of flowing quantities which he called **Fluents**.

The rate at which these quantities changed he called **Fluxions**, denoted by a
dot over the variable ($\dot{x}$).

* **Fluent ($x$):** Distance (a quantity flowing in time).

* **Fluxion ($\dot{x}$):** Velocity (the speed of the flow).

* **Moment ($o$):** An infinitely small interval of time.

When Newton derived relationships, he did so by letting time flow forward by a
tiny moment $o$.

For example, to find the rate of change of a quantity $y = x^2$, he would
increment the fluent $x$ by its momentary change $\dot{x}o$:

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

This is the essence of calculus. But notice the perspective: reality is defined
by **flow** ($\dot{x}$), not by static position.


## Mass as a Coefficient of Flow

When Newton introduced "Quantity of Matter" (Mass), he did so to solve a problem of flow. He needed to explain why some objects change their flow ($\dot{x}$) more reluctantly than others when pushed.

In Definition II of the *Principia*, he wrote:


> *"The quantity of motion is the measure of the same, arising from the velocity and quantity of matter conjointly."*


He did not define mass as "stuff." He defined it as the thing you must multiply velocity by to get the correct "quantity of motion" (momentum).

$$
\text{Motion} \propto \text{Mass} \times \text{Velocity}
$$

Dynamics came first; mass was invented to linearize the dynamics.

In a Maxwell Universe, we return to this priority. The "flow" (electromagnetic flux) is the fundamental reality. What we call "mass" is simply the impedance—the resistance to change—that arises when that flux is knotted into a complex topology.
