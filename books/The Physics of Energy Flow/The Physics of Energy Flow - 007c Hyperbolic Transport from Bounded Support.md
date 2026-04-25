---
title: The Physics of Energy Flow - Hyperbolic Transport from Bounded Support
date: 2026-03-26
---

# 7c. Hyperbolic Transport from Bounded Support

Chapter 7b showed that transport is most cleanly described by two quantities:

- transported content $\mu$,
- realized support $\Sigma$.


Density is then derived as

$$
\bar u = \frac{\mu}{\Sigma}.
$$

That chapter also showed that increasing energy density does not increase the local
transport speed. Instead, it reduces the amount of support advanced over a fixed
time interval.

We now ask the next question:

> if transport along a chosen axis can proceed only at the local bound
> $c$,
> how should the effective motion of a localized configuration be described?


The answer is that motion is not primitive. It is the imbalance of opposite
bounded transports.


## Transport along a chosen axis

Fix an axis.

Along that axis, the local transport of content can contribute in two opposite
directions only:

- forward, at speed $+c$,
- backward, at speed $-c$.


Let the transported contents in those two directions over a fixed interval be

$$
\mu_+,
\qquad
\mu_-,
$$

with

$$
\mu_+ \ge 0,
\qquad
\mu_- \ge 0.
$$

These are not two substances. They are the forward and backward directional
contributions of the same transport process along the chosen axis.


## Effective velocity as transport imbalance

The total transported content is

$$
\mu_{\mathrm{tot}} = \mu_+ + \mu_-.
$$

The net directed transport is

$$
\mu_{\mathrm{net}} = \mu_+ - \mu_-.
$$

Define the effective velocity by weighting the two directional contributions by
their transport speeds:

$$
v_{\mathrm{eff}}
:=
\frac{(+c)\mu_+ + (-c)\mu_-}{\mu_+ + \mu_-}.
$$

This gives

$$
v_{\mathrm{eff}}
=
c\,\frac{\mu_+ - \mu_-}{\mu_+ + \mu_-}.
$$

Thus effective motion is the normalized imbalance of opposite bounded transport
contributions.


## Immediate consequences

This formula has the correct limiting behavior.

If the directional contributions are equal,

$$
\mu_+ = \mu_-,
$$

then

$$
v_{\mathrm{eff}} = 0.
$$

If all transport is forward,

$$
\mu_- = 0,
$$

then

$$
v_{\mathrm{eff}} = c.
$$

If all transport is backward,

$$
\mu_+ = 0,
$$

then

$$
v_{\mathrm{eff}} = -c.
$$

So the transport bound is built in:

$$
|v_{\mathrm{eff}}| \le c.
$$

This bound is not imposed externally. It follows from the fact that all
directional contributions themselves move at speed at most $c$.


## Ratio form

Define the directional-content ratio

$$
r := \frac{\mu_+}{\mu_-},
\qquad
r > 0.
$$

Then

$$
\frac{v_{\mathrm{eff}}}{c}
=
\frac{r-1}{r+1}.
$$

This already shows that the effective velocity is bounded even though the ratio
$r$ itself can range over all positive values.


## Hyperbolic parameter

Introduce a parameter $\eta$ by writing

$$
r = e^{2\eta}.
$$

Then

$$
\frac{v_{\mathrm{eff}}}{c}
=
\frac{e^{2\eta}-1}{e^{2\eta}+1}
=
\tanh\eta.
$$

So

$$
v_{\mathrm{eff}} = c\,\tanh\eta.
$$

This is the hyperbolic form of bounded transport.

It has not been introduced by coordinate geometry. It follows directly from:

- opposite directional contributions,
- finite transport speed,
- and velocity defined as normalized transport imbalance.


## Interpretation of $\eta$

The parameter $\eta$ is not an abstract coordinate.

It measures the logarithmic bias between forward and backward transport:

$$
\eta = \frac{1}{2}\ln\frac{\mu_+}{\mu_-}.
$$

So:

- $\eta = 0$ means balanced transport,
- $\eta > 0$ means forward bias,
- $\eta < 0$ means backward bias.


The more strongly one direction dominates, the larger the magnitude of
$\eta$.


## Why this is hyperbolic

The bounded ratio

$$
-1 < \frac{v_{\mathrm{eff}}}{c} < 1
$$

is represented by the unbounded parameter $\eta \in \mathbb R$ through

$$
\frac{v_{\mathrm{eff}}}{c} = \tanh\eta.
$$

This is exactly the same mathematical structure that later appears in hyperbolic
kinematics.

Here, however, it arises directly from transport bookkeeping.

It is not introduced by spacetime postulates. It is forced by bounded
directional transport.


## Support interpretation

In the language of Chapter 7b:

- $\mu_+$ and $\mu_-$ are the transported contents in the two
  directions,
- each directional contribution advances along realized support at speed
  $c$,
- the effective velocity is the net bias of those support-borne transports.


Thus motion is not a primitive translation of a rigid object through a
background.

It is the organized imbalance of opposite transport contributions within one
continuous flow.


## Momentum-conservation interpretation

This same result may be read dynamically.

If a localized knot changes its motion, it cannot create momentum from nothing.

Any increase in forward-directed transport must be balanced by counter-transport
elsewhere in the total system.

So propulsion is not the appearance of net motion from nowhere. It is the
reweighting of forward and backward transport contributions under continuity.

The effective velocity then records the resulting imbalance.


## Summary

This chapter establishes:

- transport along an axis resolves into opposite directional contributions,
- each contribution is bounded by the same local transport speed
  $c$,
- effective motion is the normalized imbalance of those contributions,
- therefore


  $$
  v_{\mathrm{eff}} = c\,\frac{\mu_+ - \mu_-}{\mu_+ + \mu_-},
  $$

- and equivalently


  $$
  v_{\mathrm{eff}} = c\,\tanh\eta,
  \qquad
  \eta = \frac{1}{2}\ln\frac{\mu_+}{\mu_-}.
  $$

Hyperbolic transport is therefore a direct consequence of bounded support-based
energy flow.

The next step is composition: how successive reweightings of transport bias
combine.
