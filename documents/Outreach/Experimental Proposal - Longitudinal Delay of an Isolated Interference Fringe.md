---
title: Experimental Proposal - Longitudinal Delay of an Isolated Interference Fringe
date: 2026-04-16
---

# Experimental Proposal

## Goal

Measure whether the center of a bright interference fringe propagates with a
different longitudinal delay than one of the incident beams that forms it.


## Rationale

For a laser beam of energy density $u$ advancing longitudinally at
speed $c$, the energy flux is

$$
J = u\,c.
$$

Suppose two coherent beams arrive at the final recombination region, each
carrying density $u$. Then for one incident channel,

$$
J_0 = u\,c.
$$

For two equal incident beams, the total incoming budget is

$$
J_{\mathrm{in}} = 2u\,c.
$$

The tested hypothesis is not that brightness by itself slows propagation. It
is that coherent overlap compresses the same incoming transport budget into
fewer effective longitudinal channels. If the two beams overlap coherently and
recover a bright-fringe center with local density $4u$, then the same incoming
budget concentrated into that denser channel gives

$$
c_{\mathrm{eff}}=\frac{J_{\mathrm{in}}}{4u}
=
\frac{2u\,c}{4u}
=
\frac{c}{2}.
$$

So the hypothesis is simple: if two incoming channels are recovered as one
denser bright channel, the same incoming budget implies a lower effective
longitudinal speed, operationally like a refractive slowdown.


## Complementary Outputs

Let the two equal fields arriving at the final recombination region be

$$
f_1(x,z,t)=A\,e^{i(kz-\omega t)}e^{+iqx/2},
\qquad
f_2(x,z,t)=A\,e^{i(kz-\omega t)}e^{-iqx/2},
$$

where $x$ is the transverse coordinate across the fringes, $z$ is the
longitudinal propagation coordinate, $t$ is time, $A$ is the common field
amplitude, $k=2\pi/\lambda$ is the optical wave number, $\omega$ is the
optical angular frequency, and $q$ is the transverse phase-gradient parameter
that sets the fringe spacing. Let

$$
u := |A|^2.
$$

At the final 50/50 beam splitter, the two output modes are

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

So the two outputs satisfy

$$
u_+(x)+u_-(x)=2u.
$$

A bright fringe on one output corresponds to a dark fringe on the other. This
is the basic $\cos^2+\sin^2=1$ structure of the two output branches.


## Raw Overlap Peak

Before output-mode normalization, the direct coherent overlap is

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

with $n$ an integer, the loading reaches

$$
u_{\mathrm{raw}}(x_n)=4u.
$$

This is the local peak used in the $c_{\mathrm{eff}}$ estimate: two incident
channels of density $u$ can recover a bright-center loading of
$4u$.


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

stays above $3u$.


## Crossing Angle and Fringe Width

If the two beams recombine with total crossing angle $\theta$, then the
transverse wave-number difference is

$$
q = 2k\sin\!\left(\frac{\theta}{2}\right),
\qquad
k=\frac{2\pi}{\lambda}.
$$

This is the small recombination-angle triangle: the opening angle between the
two rays sets the transverse phase gradient and therefore the fringe spacing.

Therefore the fringe period is

$$
\Lambda = \frac{2\pi}{q}
=
\frac{\lambda}{2\sin(\theta/2)}
\approx
\frac{\lambda}{\theta}
\quad
(\theta \ll 1).
$$

A $1\,\mathrm{m}$ Mach-Zehnder arm is practical, but the fringe width is set by
the recombination angle $\theta$, not by the arm length.

For a HeNe laser,

$$
\lambda = 632.8\,\mathrm{nm}.
$$

Choosing a fairly wide fringe with

$$
\theta = 0.2\,\mathrm{mrad},
$$

gives

$$
\Lambda \approx \frac{632.8\times 10^{-9}}{2\times 10^{-4}}
\approx
3.16\,\mathrm{mm}.
$$

Then the bright-core region above $3u$ has full width

$$
\frac{\Lambda}{3} \approx 1.05\,\mathrm{mm}.
$$

That is large enough for straightforward spatial isolation.

If the detector or entrance slit is centered on the fringe maximum and has
active width $a$, then the worst-case sampled loading is

$$
u_{\mathrm{edge}} = 4u\cos^2\!\left(\frac{\pi a}{2\Lambda}\right).
$$

For the same HeNe example:

- if $a=0.25\,\mathrm{mm}$, then $u_{\mathrm{edge}}\approx 3.94u$;
- if $a=0.50\,\mathrm{mm}$, then $u_{\mathrm{edge}}\approx 3.76u$.

So a practical target is a sensor or slit width in the range

$$
0.25\,\mathrm{mm} \;\text{to}\; 0.50\,\mathrm{mm},
$$

centered on the bright-fringe maximum.


## Measurement Model

1. Split a coherent amplitude-modulated laser beam into two equal beams.
2. Recombine them at a small angle in a Mach-Zehnder interferometer.
3. Use one output branch, where stable straight fringes are visible.
4. Spatially isolate the center of one bright fringe ridge.
5. Propagate that bright ridge over a known distance $L$.
6. In parallel, propagate one incident beam as a reference over the same
   distance.
7. Amplitude-modulate both channels from the same source.
8. For each channel, measure the delay $\tau$ relative to the common
   modulation signal on an oscilloscope or phase meter.

For each channel separately, collect pairs $(L_i,\tau_i)$, where $L_i$ is the
propagation distance and $\tau_i$ is the measured delay:

$$
(L_1,\tau_1),\ (L_2,\tau_2),\ (L_3,\tau_3),\ \ldots
$$

and fit

$$
\tau(L)=mL+b.
$$

Here $b$ is the fixed zero-length offset, which should be close to zero after
referencing. The local slope estimates are

$$
m_i = \frac{\delta \tau_i}{\delta L_i},
$$

and the regression returns the mean slope

$$
\langle m \rangle \approx \frac{d\tau}{dL}.
$$

Since

$$
\tau = \frac{L}{v},
$$

the speed is

$$
v = \frac{1}{\langle m \rangle}.
$$

This is done independently for the incident-beam reference and for the
isolated bright-fringe channel:

$$
v_{\mathrm{ref}} = \frac{1}{\langle m_{\mathrm{ref}} \rangle},
\qquad
v_{\mathrm{fringe}} = \frac{1}{\langle m_{\mathrm{fringe}} \rangle}.
$$


## Experimental Question

The standard-optics expectation is

$$
v_{\mathrm{fringe}} = v_{\mathrm{ref}}
$$

within experimental error. The tested alternative is

$$
v_{\mathrm{fringe}} < v_{\mathrm{ref}}.
$$

So the experimental question is:

$$
v_{\mathrm{fringe}} < v_{\mathrm{ref}} \; ?
$$

If yes, the bright fringe carries an additional longitudinal delay. If no, the
fringe behaves like the reference beam within experimental error.


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
4. fit $\tau(L)$,
5. recover $v = 1/\langle m \rangle$,
6. compare that speed against one incident beam.


This gives a direct experimental test of whether the bright fringe channel
acquires an additional longitudinal delay.
