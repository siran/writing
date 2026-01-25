## Lemma: A detector without a trigger cannot exist

**Claim.** Any functioning which-way detector necessarily introduces a nonzero
activation threshold, and therefore necessarily creates **zero overlap** between
the detector-conditioned contributions. Consequently, the interference cross
term vanishes.


### Step 1 — What “functioning detector” means physically

A detector is not “a question.” It is a device with two stable operational
conditions:

- **Ready** (it can wait without firing),
- **Triggered** (it has registered an event).

Denote these by two distinct macrostates:

$$
|0\rangle \quad \text{(ready)}, \qquad |1\rangle \quad \text{(triggered)}.
$$

For the device to be usable, the ready state must persist for long times in the
absence of an incident signal.


### Step 2 — Stability requires a nonzero activation threshold

If there were no energetic threshold separating “ready” from “triggered,” then:

- thermal noise,
- ambient electromagnetic fluctuations,
- internal microscopic motion,

would constantly drive transitions between the two conditions.

In other words: the device would fire continuously and would not qualify as a
detector.

Therefore, any functioning detector requires a **nonzero activation barrier**
$E_{\mathrm{th}}>0$ separating operationally distinct macrostates.

This is not a modeling choice. It is the definition of a usable trigger.


### Step 3 — A working which-way detector implies a conditional interaction

A which-way detector must couple differently depending on whether the electron
passes the monitored slit region or not.

Let $q$ denote the detector’s internal coordinates (collectively),
and let the initial detector state be $\chi_0(q)$.

After interaction, the joint state must take the form:

$$
\Psi(x,q)=\psi_L(x)\,\chi_L(q)+\psi_R(x)\,\chi_R(q),
$$

where $\chi_L$ and $\chi_R$ are the detector states produced
conditional on the electron’s passage near the monitored region.

This is simply the minimal mathematical encoding of “the detector can, in
principle, register the passage.”


### Step 4 — The screen intensity contains an explicit overlap factor

The screen does not read $q$, so the recorded intensity is:

$$
I(x)=\int dq\,|\Psi(x,q)|^2.
$$

Expand exactly:

$$
|\Psi|^2
=
|\psi_L|^2|\chi_L|^2
+
|\psi_R|^2|\chi_R|^2
+
\psi_L\psi_R^*\,\chi_L\chi_R^*
+
\psi_L^*\psi_R\,\chi_L^*\chi_R.
$$

Integrate term-by-term:

$$
I(x)=|\psi_L|^2+|\psi_R|^2
+
\psi_L\psi_R^*\,\Gamma
+
\psi_L^*\psi_R\,\Gamma^*,
$$

where the detector overlap factor is

$$
\Gamma := \int dq\,\chi_L(q)\chi_R^*(q)=\langle \chi_R|\chi_L\rangle.
$$

Thus interference survives **if and only if** $\Gamma\neq 0$.


### Step 5 — A trigger forces zero overlap (not “small overlap”)

Because a detector has a true activation barrier $E_{\mathrm{th}}>0$, the
conditional interaction necessarily pushes the detector into **different basins
of its internal state space** depending on whether the monitored slit was
traversed.

These basins correspond to mutually exclusive operational states. They are not
merely “slightly different.” They are **distinct physical configurations** of
the device.

In the language of $q$:

- $\chi_L(q)$ is supported on a region of detector state space
  corresponding to “interaction sufficient to be trigger-capable,”
- $\chi_R(q)$ is supported on a region corresponding to “no such
  interaction.”

These supports do not overlap:

$$
\chi_L(q)\chi_R(q)=0 \quad \text{for all } q.
$$

Therefore:

$$
\Gamma=\int dq\,\chi_L(q)\chi_R^*(q)=0.
$$

This is a hard zero-overlap statement. No gradual qualifier is required.


### Step 6 — Consequence: the cross term vanishes identically

With $\Gamma=0$:

$$
I(x)=|\psi_L(x)|^2+|\psi_R(x)|^2.
$$

The interference term is absent because the two detector-conditioned
contributions are **mutually exclusive** in the full physical state space.

No observer is needed. No epistemic step is needed. The disappearance follows
from (i) linear wave evolution and (ii) the existence of a real trigger barrier.

---


### Naming note

We avoid the word “orthogonality” and say instead:

- **zero overlap** ($\Gamma=0$),
- **mutual exclusivity** of detector-conditioned states,
- **disjoint support** in detector state space.

These express exactly what is used in the derivation.
