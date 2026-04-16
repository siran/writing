---
title: Experimental Proposal - Longitudinal Delay of an Isolated Interference Fringe
date: 2026-04-16
---

# Experimental Proposal

## Goal

Measure whether the center of a bright interference fringe propagates with a
different longitudinal delay than one of the incident beams that forms it.


## Geometry

1. Split a coherent laser beam into two equal beams.
2. Recombine them at a small angle in a Mach-Zehnder interferometer.
3. Use one output branch, where stable straight fringes are visible.
4. Spatially isolate the center of one bright fringe ridge.
5. Propagate that bright ridge over a known distance `L`.
6. In parallel, propagate one incident beam as a reference over the same
   distance.
7. Amplitude-modulate both channels from the same source.
8. Measure the delay `\tau` of each channel on an oscilloscope or phase meter.


## Interference Model

Let the two equal fields arriving at the final recombination region be

$$
f_1(x,z,t)=A\,e^{i(kz-\omega t)}e^{+iqx/2},
\qquad
f_2(x,z,t)=A\,e^{i(kz-\omega t)}e^{-iqx/2},
$$

with

$$
u := |A|^2.
$$

The raw coherent overlap is

$$
f_{\mathrm{raw}} = f_1 + f_2
=
2A\cos\!\left(\frac{qx}{2}\right)e^{i(kz-\omega t)},
$$

so the raw overlap density is

$$
u_{\mathrm{raw}}(x)=4u\cos^2\!\left(\frac{qx}{2}\right).
$$

Therefore

$$
0 \le u_{\mathrm{raw}}(x) \le 4u.
$$

At a bright-fringe center

$$
x_n = \frac{2\pi n}{q},
$$

the loading reaches

$$
u_{\mathrm{raw}}(x_n)=4u.
$$


## Bright-Core Region

To isolate the strongest part of the fringe, require

$$
u_{\mathrm{raw}}(x) > 3u.
$$

With

$$
x=x_n+\Delta x,
$$

this becomes

$$
4u\cos^2\!\left(\frac{q\Delta x}{2}\right) > 3u,
$$

so

$$
\cos^2\!\left(\frac{q\Delta x}{2}\right) > \frac{3}{4}.
$$

Hence

$$
\left|\frac{q\Delta x}{2}\right| < \frac{\pi}{6},
$$

which gives

$$
|\Delta x| < \frac{\pi}{3q}.
$$

If the fringe period is

$$
\Lambda = \frac{2\pi}{q},
$$

then the bright-core condition is

$$
|\Delta x| < \frac{\Lambda}{6}.
$$

So the central stripe of full width

$$
\frac{\Lambda}{3}
$$

stays above `3u`.


## Observable Mach-Zehnder Outputs

At the final 50/50 beam splitter, the output modes are

$$
f_+(x)=\frac{f_1(x)+f_2(x)}{\sqrt2},
\qquad
f_-(x)=\frac{f_1(x)-f_2(x)}{\sqrt2}.
$$

Therefore

$$
u_+(x)=2u\cos^2\!\left(\frac{qx}{2}\right),
\qquad
u_-(x)=2u\sin^2\!\left(\frac{qx}{2}\right).
$$

So the two outputs are complementary and satisfy

$$
u_+(x)+u_-(x)=2u.
$$

A bright fringe on one output corresponds to a dark fringe on the other, and
the two outputs together recover the full incident two-beam power.


## Measurement Model

Each channel is measured separately against the same modulation source.

For each channel, record several pairs

```text
(L1, tau1), (L2, tau2), (L3, tau3), ...
```

and fit

```text
tau(L) = mL + b.
```

With the zero-length reference chosen appropriately, `b` should be close to
zero, and the slope is

```text
m = d tau / dL = 1 / v.
```

So the propagation speed is recovered directly from the fit as

```text
v = 1 / m.
```

This is done independently for:

- the incident-beam reference,
- the isolated bright-fringe channel.

The comparison is therefore:

```text
v_ref = 1 / m_ref
v_fringe = 1 / m_fringe
```


## Experimental Question

Does the isolated bright-fringe channel yield

```text
v_fringe < v_ref ?
```

If yes, the bright fringe carries an additional longitudinal delay.  
If no, the fringe behaves like the reference beam within experimental error.


## Minimum Requirements

- stable coherent source
- Mach-Zehnder interferometer
- controlled small crossing angle at recombination
- stable fringe pattern
- spatial filter for one bright ridge
- common amplitude modulation source
- oscilloscope or phase-delay readout
- variable path length


## Summary

The proposal is simple:

1. create stable fringes in a Mach-Zehnder output,
2. isolate the center of one bright fringe ridge,
3. measure its delay for several lengths,
4. fit `tau(L)`,
5. recover `v = 1/m`,
6. compare that speed against one incident beam.

This gives a direct experimental test of whether the bright fringe channel
acquires an additional longitudinal delay.
