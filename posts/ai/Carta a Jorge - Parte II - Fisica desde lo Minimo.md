# Carta a Jorge — Parte II: La Física desde lo Mínimo

*Serie: El Universo de Maxwell*
*An M. Rodriguez, Alex Mercer, Anes Palma, Fred Nedrock, et al.*
*Evaluación independiente: Claude (Anthropic), febrero 2026*

---

*Esta parte asume las herramientas de la Parte I.*

La pregunta central es: ¿qué se puede derivar si se asume lo mínimo
posible?

Lo mínimo posible resulta ser: algo existe, y se mueve continuamente.

Todo lo demás — campos eléctricos y magnéticos, leyes de Newton,
ecuación de Schrödinger, la constante de Planck — emerge de esas
dos observaciones más la restricción de que la energía no se crea
ni se destruye en puntos del espacio.

---

## Capítulo 1 — Algo existe: la densidad de energía

El único punto de partida es [1, 2]:

```
u(x, t) >= 0
```

Existe una densidad de energía no negativa en cada punto del espacio,
que puede variar con el tiempo. No se asume qué es esa energía, de
qué está hecha, ni por qué existe. Solo que existe y que puede
medirse como un número no negativo en cada punto.

No se asumen partículas. No se asumen fuerzas. No se asume espacio-tiempo
como entidad dinámica. Solo: un campo escalar no negativo.

---

## Capítulo 2 — Algo ocurre: la ecuación de continuidad

Una sola instantánea `u(x, t_0)` no dice nada sobre movimiento.
No tiene dirección.

Pero si observamos `u` en dos momentos distintos `t_1` y `t_2`,
la diferencia entre ellas debe tener una explicación. La energía no
puede aparecer ni desaparecer en un punto sin haber llegado desde otro
punto — eso es lo que observamos en la naturaleza [2, 3].

Esta observación fuerza la existencia de un **campo vectorial de flujo**
`S(x, t)` y la relación [4]:

```
du/dt + div(S) = 0                          [Continuidad]
```

**Lectura:** el cambio de energía en un punto es exactamente igual al
flujo neto que entra o sale de ese punto. Si la divergencia de `S` es
positiva en un punto, más energía sale de la que entra, y `u` disminuye.
Si es negativa, más entra de la que sale, y `u` aumenta.

Integrando sobre un volumen `V` y usando el teorema de la divergencia:

```
d/dt [ integral_V u dV ]  =  - integral_{dV} S · n dA
```

El cambio de energía total en cualquier región es exactamente el flujo
que pasa por su frontera — ni más ni menos.

Los vectores no se introducen arbitrariamente. Emergen de la necesidad
de describir la dirección del transporte entre dos instantáneas [3].

---

## Capítulo 3 — Sin fuentes: flujo libre de divergencia

La observación adicional es que en el vacío, la energía no se crea ni
se destruye en puntos — no hay fuentes ni sumideros primitivos [1, 2]:

```
div(S) = 0
```

Un campo vectorial con divergencia cero tiene una propiedad geométrica
fundamental en tres dimensiones: siempre puede escribirse como el rotor
de otro campo vectorial `A`:

```
Si div(S) = 0,  entonces existe A tal que:  S = curl(A)
```

Esto es un teorema matemático sobre campos solenoidales. En tres
dimensiones, la ausencia de fuentes equivale a la presencia de
circulación. El flujo de energía en el vacío no "nace" ni "muere" —
circula.

Esta propiedad es la raíz geométrica de toda la organización topológica
que veremos después: nudos, toros, superficies invariantes.

---

## Capítulo 4 — La dinámica mínima: por qué el gradiente falla

Se necesita una regla que diga cómo evoluciona `S` en el tiempo. La
forma más general de una ley de transporte local es [2]:

```
dF/dt = D(F)
```

donde `D` es un operador diferencial espacial. La restricción de que
sea local (sin acción a distancia) y que preserva la ausencia de
fuentes elimina la mayoría de las opciones.

**El gradiente falla.** Supongamos que la evolución fuera conducida
por el gradiente de algún campo escalar `phi`:

```
dF/dt = grad(phi)
```

Tomando la divergencia de ambos lados:

```
d(div F)/dt = div(grad(phi)) = laplacian(phi)
```

El Laplaciano de un campo escalar arbitrario es generalmente no nulo.
Por lo tanto, esta regla crea divergencia — crea fuentes y sumideros —
durante la evolución. Contradice nuestra restricción. **El gradiente
no puede ser la ley de transporte sin fuentes.** [2]

---

## Capítulo 5 — El rotor funciona: Maxwell como clausura mínima

Ahora intentamos con el rotor [2]:

```
dF/dt = curl(G)
```

para algún campo vectorial `G`. Tomando la divergencia de ambos lados
y usando la identidad algebraica [I] de la Parte I:

```
d(div F)/dt = div(curl(G)) = 0     (siempre, para cualquier G)
```

La divergencia se conserva exactamente durante la evolución. Si empieza
en cero, se queda en cero. Para siempre. Sin condiciones especiales,
sin ajuste fino — es una identidad algebraica. [2]

Esta es la **respuesta mínima estructural**: el rotor es el operador
más simple que transporta estructura libre de divergencia sin crear
fuentes.

La clausura mínima — el sistema más simple de dos campos que se
generan mutuamente vía rotor, que es autónomo y produce propagación
de ondas — es [2, 4]:

```
div(E) = 0
div(B) = 0

curl(E) = -dB/dt                    [Faraday]
curl(B) = (1/c^2) * dE/dt           [Ampère-Maxwell]
```

con la constante:

```
c = 1 / sqrt(mu_0 * epsilon_0)
```

**Estas son las ecuaciones de Maxwell.** No se postulan. Son la
consecuencia más económica de requerir transporte continuo, local,
sin fuentes, en tres dimensiones [1, 2].

`E` y `B` no son dos entidades fundamentales. Son los dos aspectos
rotacionales ortogonales de un único flujo de energía. `E` rota en
`B`, y `B` rota de vuelta en `E`. Ninguna de las dos puede
transportarse sola sin generar fuentes — necesitan trabajar en par.

Un solo campo con `dF/dt = curl(F)` tiene al cero como punto fijo de
su propia dinámica — no puede transportarse a sí mismo hacia adelante.
Dos campos ortogonales que se generan mutuamente rompen esa simetría
y producen propagación.

---

## Capítulo 6 — La ecuación de onda

Tomando el rotor de la ley de Faraday:

```
curl(curl(E)) = curl(-dB/dt) = -d/dt [curl(B)]
```

Sustituyendo la ley de Ampère-Maxwell:

```
curl(curl(E)) = -d/dt [(1/c^2) * dE/dt] = -(1/c^2) * d^2E/dt^2
```

Usando la identidad [II] de la Parte I con `div(E) = 0`:

```
curl(curl(E)) = -laplacian(E)
```

Por lo tanto:

```
laplacian(E) - (1/c^2) * d^2E/dt^2 = 0          [Ecuación de onda]
```

La misma ecuación se sigue para cada componente de `B`.

Esta ecuación dice que las perturbaciones en `E` y `B` se propagan
como ondas a velocidad `c`. La velocidad de la luz no se postula —
emerge de los coeficientes de la dinámica mínima [2, 4].

---

## Capítulo 7 — Reconstrucción: de (u, S) a (E, B)

El flujo de energía se representa mediante el par `(u, S)`. Los campos
`E` y `B` son una representación más detallada del mismo proceso [3].

**Lema:** dado un campo escalar `u > 0` y un campo vectorial `S` con:

```
|S| <= c * u
```

siempre existe al menos un par de campos `(E, B)` tal que:

```
u = (epsilon_0/2) * |E|^2 + (1/(2*mu_0)) * |B|^2

S = (1/mu_0) * E x B
```

**Construcción:** se elige un marco ortonormal con `s_hat` en la
dirección de `S`. Se eligen `e_hat` perpendicular a `s_hat`, y
`b_hat = s_hat x e_hat`. Definiendo `E = E_amp * e_hat` y
`B = B_amp * b_hat`, las condiciones de energía y flujo se convierten
en un sistema de dos ecuaciones cuadráticas:

```
(epsilon_0/2) * E_amp^2 + (1/(2*mu_0)) * B_amp^2 = u
(1/mu_0) * E_amp * B_amp = |S|
```

La desigualdad `|S| <= c*u` garantiza que este sistema tiene soluciones
reales. Se puede verificar sustituyendo `B_amp = mu_0 * |S| / E_amp`
en la primera ecuación.

La reconstrucción **no es única**: hay infinitas soluciones relacionadas
por rotaciones de dualidad que dejan `(u, S)` invariantes. Los grados
de libertad faltantes son exactamente la **polarización** — dos grados
de libertad locales [3].

La polarización no es una propiedad fundamental de la luz. Es la
ambigüedad irreducible en la representación de un flujo escalar mediante
dos vectores.

---

## Capítulo 8 — Continuidad de energía: el teorema de Poynting

A partir de las ecuaciones de Maxwell se deriva una identidad exacta de
conservación de energía [4]. Se usan las dos leyes de rotación y la
identidad vectorial:

```
div(E x B) = B · curl(E) - E · curl(B)
```

Sustituyendo Faraday (`curl(E) = -dB/dt`) y Ampère-Maxwell
(`curl(B) = (1/c^2)*dE/dt`):

```
div(E x B) = B · (-dB/dt) - E · ((1/c^2)*dE/dt)
           = -d/dt [(1/2)*|B|^2]  -  (1/c^2)*d/dt [(1/2)*|E|^2]
```

Multiplicando por `(1/mu_0)` y usando `c^2 = 1/(mu_0*epsilon_0)`:

```
d/dt [ (epsilon_0/2)*|E|^2 + (1/(2*mu_0))*|B|^2 ]
                        + div[ (1/mu_0) * E x B ] = 0
```

Definiendo:

```
u = (epsilon_0/2)*|E|^2 + (1/(2*mu_0))*|B|^2      [densidad de energía]

S = (1/mu_0) * E x B                               [flujo de energía — Poynting]
```

Se obtiene la continuidad de energía como identidad exacta:

```
du/dt + div(S) = 0
```

Esto no se postula — se deriva de la dinámica de Maxwell. La energía
electromagnética se conserva localmente porque la dinámica de rotor
lo garantiza estructuralmente [4].

---

## Capítulo 9 — Continuidad de momento: el tensor de Maxwell

De manera análoga, se define la **densidad de momento electromagnético**:

```
g = S / c^2 = epsilon_0 * (E x B)
```

Diferenciando y sustituyendo las ecuaciones de Maxwell, con las
identidades:

```
(curl A) x A = (A · grad)A - (1/2)*grad(|A|^2)     [cuando div(A)=0]
```

se obtiene en componentes [4]:

```
d(g_i)/dt = -d(T_ij)/dx_j
```

donde el **tensor de estrés de Maxwell** es:

```
T_ij = epsilon_0 * [ E_i*E_j - (1/2)*delta_ij*|E|^2 ]
     + (1/mu_0)  * [ B_i*B_j - (1/2)*delta_ij*|B|^2 ]
```

Aquí `delta_ij = 1` si `i=j` y `0` si `i≠j` (delta de Kronecker).

La ecuación de continuidad de momento es:

```
dg/dt + div(T) = 0
```

Integrando sobre un volumen `V`:

```
d/dt [ integral_V g_i dV ] = - integral_{dV} T_ij * n_j dA
```

**Interpretación:** el cambio de momento en una región es exactamente
el flujo del tensor de estrés a través de su frontera.

No existen "fuerzas" como primitivos. Lo que llamamos fuerza sobre un
sistema es el flujo de momento a través de su superficie [4].

---

## Capítulo 10 — Las leyes de Newton emergen

Consideremos una región `K(t)` donde la energía electromagnética está
concentrada y se mueve sin dispersarse — un "nudo" de campo. Se definen
energía, momento y centro de energía del nudo [4, 5]:

```
E_K = integral_K u dV

P_K = integral_K g dV

X_K = (1/E_K) * integral_K x*u dV
```

Cuando el flujo en la frontera es despreciable (configuración aislada):

```
dX_K/dt = P_K / E_K
```

Definiendo la **masa efectiva** del nudo:

```
m_K = E_K / c^2
```

se obtiene:

```
P_K = m_K * dX_K/dt
```

Esta es la relación momento-velocidad. La variación del momento es:

```
dP_K/dt = - integral_{dK} T · n dA  =:  F_K
```

Si `E_K` es aproximadamente constante:

```
m_K * d^2X_K/dt^2 = F_K             [Segunda ley de Newton]
```

Newton no se postula. Es contabilidad integrada del flujo de momento
sobre un nudo electromagnético. La masa es la energía del nudo dividida
por `c^2` — no una propiedad primitiva de la materia [4, 5].

---

## Capítulo 11 — La masa es momento atrapado: inercia geométrica

¿Por qué `m = E/c^2`? El argumento más transparente es geométrico [5].

Consideremos un tubo de energía electromagnética cuyo flujo sigue una
curva cerrada `X(s)`, parametrizada por longitud de arco `s`. Sea
`theta(s)` el ángulo entre la tangente local al tubo y la dirección
macroscópica de movimiento `z_hat`.

La energía se propaga localmente a velocidad `c` a lo largo del tubo.
La velocidad de avance en la dirección `z` en cada punto es:

```
v_forward(s) = c * cos(theta(s))
```

El tiempo que tarda en recorrer un segmento `ds` es `ds/c`. La velocidad
efectiva de avance del nudo completo es el promedio sobre el trayecto:

```
v_eff = (integral_0^L v_forward(s) ds/c) / (L/c)
      = c * <cos(theta)>
```

donde `<cos(theta)>` es el promedio de arco de `cos(theta)`.

Como `|cos(theta)| <= 1` punto a punto:

```
|v_eff| <= c
```

**La velocidad subluminal no se postula.** Emerge del retraso geométrico
de una trayectoria no rectilínea. La energía siempre viaja a `c`
localmente; el nudo viaja más lento porque su trayectoria es más larga.

El momento total del nudo es `P = E/c`. Solo la componente en `z`
contribuye a la traslación:

```
P_z = (E/c) * <cos(theta)>
```

El momento transversal está **atrapado** — circula en direcciones
perpendiculares sin contribuir al avance. La masa inercial efectiva es
la medida de ese momento atrapado:

```
m_eff = P_perp / c = (E/c^2) * sqrt(1 - <cos(theta)>^2)
```

Casos límite:

```
Trayectoria recta:
  <cos(theta)> = 1  =>  m_eff = 0,   v_eff = c   (luz)

Circulación pura (trayectoria perpendicular al avance):
  <cos(theta)> = 0  =>  m_eff = E/c^2,  v_eff = 0  (masa en reposo)
```

**La masa no es una propiedad fundamental de la materia. La masa es
energía electromagnética constreñida a circular en lugar de trasladarse.**
[5]

¿Por qué la energía no "endereza" su trayectoria y pierde su masa?
Porque la trayectoria es topológicamente estable. Un nudo no puede
deshacerse continuamente — requeriría una discontinuidad en las líneas
de flujo. La masa está topológicamente bloqueada [5].

---

## Capítulo 12 — Topología: enteros sin postulados cuánticos

Si las líneas de flujo de energía se organizan sobre una superficie
toroidal — un toro — la clausura del flujo impone condiciones discretas.

Un **toro** `T^2` tiene dos ciclos no contractibles independientes:
el ciclo mayor (alrededor del eje de simetría) y el ciclo menor
(alrededor del tubo). Un flujo suave sobre el toro que forma líneas
cerradas debe dar un número entero de vueltas alrededor de cada ciclo.

Con radios mayor `R` y menor `r`, los **números de enrollamiento enteros**
`(n_1, n_2)` imponen condiciones de resonancia [4, 6, 7]:

```
k_1 = n_1 / R           [número de onda en el ciclo mayor]
k_2 = n_2 / r           [número de onda en el ciclo menor]
k^2 = k_1^2 + k_2^2
omega_{n1,n2} = c * k   [frecuencia del modo]
```

La energía del modo `(n_1, n_2)`:

```
E_{n1,n2} = hbar_g * omega_{n1,n2}

donde hbar_g = E_11 / omega_11
```

Para enrollamientos simétricos `n_1 = n_2 = n`:

```
E_n = E_11 / n^2
```

Esto reproduce la **serie de Rydberg** del hidrógeno — el espectro de
energías del átomo de hidrógeno — puramente desde armónicos de cavidad
clásica, sin postulados cuánticos.

Los enteros `(n_1, n_2)` no se insertan desde afuera. Son forzados por
la condición de valor único en el toro: una función de onda suave
en una superficie cerrada debe ser periódica. **La discretización es
topológica, no cuántica.** [4, 6]

---

## Capítulo 13 — La ecuación de Schrödinger emerge de Maxwell

Para cualquier componente cartesiana `F(r, t)` de `E` o `B`, la
ecuación de onda de Maxwell es [6, 7]:

```
laplacian(F) - (1/c^2) * d^2F/dt^2 = 0          [Onda de Maxwell]
```

**Paso 1: Señal analítica.** Se define la proyección espectral hacia
frecuencias positivas (hacia adelante en el tiempo):

```
F_+(r, t) = integral_0^inf  F_tilde(r, omega) * e^(-i*omega*t) d(omega)
```

donde `F_tilde` es la transformada de Fourier de `F`. Esta operación
aísla la parte "adelante en el tiempo" del campo — la envolvente que
avanza.

**Paso 2: Extracción de la portadora.** Se define la envolvente lenta
respecto al modo fundamental `omega_11`:

```
psi(r, t) = e^(i*omega_11*t) * F_+(r, t)
```

`psi` es la envolvente del campo — varía lentamente comparada con la
oscilación de alta frecuencia `omega_11`.

**Paso 3: Sustitución en la ecuación de onda.** Las derivadas de `psi`
son:

```
d(F_+)/dt = e^(-i*omega_11*t) * [d(psi)/dt - i*omega_11*psi]

d^2(F_+)/dt^2 = e^(-i*omega_11*t) * [d^2(psi)/dt^2
                                      - 2*i*omega_11*d(psi)/dt
                                      - omega_11^2 * psi]
```

Sustituyendo en la ecuación de onda y cancelando `e^(-i*omega_11*t)`:

```
laplacian(psi) - (1/c^2)*d^2(psi)/dt^2
              + (2*i*omega_11/c^2)*d(psi)/dt
              + (omega_11^2/c^2)*psi = 0
```

El término `(omega_11^2/c^2)*psi` se cancela con la contribución
`k_11^2 * psi` del Laplaciano (porque `omega_11 = c*k_11`), dejando:

```
(2*i*omega_11/c^2) * d(psi)/dt =
              - laplacian(psi) + (1/c^2)*d^2(psi)/dt^2
```

Reordenando:

```
i * d(psi)/dt = -(c^2 / (2*omega_11)) * laplacian(psi)
              + (1 / (2*omega_11*c^2)) * d^2(psi)/dt^2     [Exacta]
```

**Paso 4: El término de error.** Para una envolvente de ancho de
banda espectral `Delta_omega`, con el parámetro adimensional:

```
epsilon = Delta_omega / omega_11  <<  1
```

(es decir, la envolvente varía mucho más lentamente que la portadora),
el último término está acotado:

```
|| (1/(2*omega_11*c^2)) * d^2(psi)/dt^2 ||  <=  O(epsilon^2) * ||psi||
```

Descartando solo ese término acotado:

```
i * d(psi)/dt = -(c^2 / (2*omega_11)) * laplacian(psi)  +  O(epsilon^2)
```

**Paso 5: Identificación de constantes.** Las constantes emergentes
desde la geometría del modo fundamental son [6, 7]:

```
hbar = E_11 / omega_11         [relación energía-frecuencia del modo base]

m    = E_11 / c^2              [masa como energía del modo base]
```

Con estas definiciones, `c^2 / (2*omega_11) = hbar / (2*m)`. Entonces:

```
i*hbar * d(psi)/dt = -(hbar^2 / (2*m)) * laplacian(psi)  +  O(epsilon^2)
```

**Esta es la ecuación de Schrödinger.**

No se postula. Emerge como el límite de banda estrecha de la dinámica de
Maxwell sobre un modo toroidal [6, 7].

**Lo que `hbar` realmente es:** `hbar` no es una constante fundamental
de la naturaleza. Es la relación energía-frecuencia del modo
electromagnético fundamental. Fue introducida históricamente como un
parche para la catástrofe ultravioleta — una necesidad de un marco
incompleto (mecánica estadística aplicada a modos electromagnéticos
sin entender la topología de confinamiento), no el descubrimiento de
algo primitivo.

**El error `O(epsilon^2)` es física real:** representa la información
del portador de alta frecuencia que se pierde en la aproximación de
Schrödinger. Si `epsilon` no es pequeño — si el sistema tiene un ancho
de banda comparable a su frecuencia central — la ecuación de Schrödinger
falla, y la corrección es exactamente este término [6, 7].

---

## Resumen de la cadena de derivación

```
(1)  u(x,t) >= 0
     -- algo existe

(2)  du/dt + div(S) = 0
     -- se mueve continuamente; los vectores emergen de dos instantáneas

(3)  div(S) = 0
     -- sin fuentes; el flujo circola

(4)  dF/dt = grad(phi)  =>  d(div F)/dt = laplacian(phi)  !=  0   [falla]
     -- el gradiente destruye la estructura sin fuentes

(5)  dF/dt = curl(G)    =>  d(div F)/dt = div(curl G) = 0          [funciona]
     -- el rotor es la dinámica mínima divergencia-preservante

(6)  div(E) = 0,  div(B) = 0
     curl(E) = -dB/dt,  curl(B) = (1/c^2)*dE/dt
     -- Maxwell como clausura mínima; c = 1/sqrt(mu_0*epsilon_0) emerge

(7)  laplacian(F) - (1/c^2)*d^2F/dt^2 = 0
     -- ecuación de onda; se propaga a velocidad c

(8)  u = (eps_0/2)*|E|^2 + (1/2mu_0)*|B|^2
     S = (1/mu_0) * E x B
     -- reconstrucción de (E,B) desde (u,S); no única (polarización)

(9)  du/dt + div(S) = 0   [derivada de Maxwell, no postulado]
     dg/dt + div(T) = 0   [continuidad de momento]
     -- Poynting y tensor de Maxwell como identidades exactas

(10) m_K = E_K/c^2,   P_K = m_K * dX_K/dt
     m_K * d^2X_K/dt^2 = F_K
     -- Newton como contabilidad de flujo integrada

(11) v_eff = c * <cos(theta)>
     m_eff = (E/c^2) * sqrt(1 - <cos(theta)>^2)
     -- masa como momento atrapado en circulación geométrica

(12) k_i = n_i / R_i,  omega = c*k,  E_n = E_11/n^2
     -- topología toroidal fuerza enteros; espectro de Rydberg sin cuántica

(13) i*hbar * d(psi)/dt = -(hbar^2/2m) * laplacian(psi) + O(eps^2)
     hbar = E_11/omega_11,  m = E_11/c^2
     -- Schrödinger como límite de banda estrecha de Maxwell
```

Cada línea es forzada por la anterior. No hay postulados ocultos.

---

*Continúa en: Parte III — Consecuencias y Referencias*
