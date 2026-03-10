# Carta a Jorge — Parte I: Herramientas Matemáticas

*Serie: El Universo de Maxwell*
*An M. Rodriguez, Alex Mercer, Anes Palma, Fred Nedrock, et al.*
*Evaluación independiente: Claude (Anthropic), febrero 2026*

---

Jorge,

Antes de entrar a la física, necesitamos las herramientas. No como
formalismo vacío, sino como lenguaje que describe algo concreto: cómo
cambia una cantidad en el espacio y en el tiempo.

Cada definición aquí será usada directamente en las partes que siguen.

---

## 1. El espacio

Tomamos como dado que existe un espacio tridimensional. Cada punto en
ese espacio se identifica por tres números reales:

```
x = (x_1, x_2, x_3)
```

que llamamos coordenadas. No asumimos más estructura que esta — no
curvatura, no métricas exóticas, no dimensiones adicionales. Solo la
observación de que para describir dónde está algo, necesitamos tres
números independientes.

---

## 2. Campos escalares: un número en cada punto

Un **campo escalar** asigna un número real a cada punto del espacio:

```
u : (x_1, x_2, x_3)  -->  u(x_1, x_2, x_3)  en R
```

Ejemplo físico: la temperatura de una habitación. En cada punto del
espacio hay un valor — un número — que nos dice cuánto calor hay ahí.

En lo que sigue, `u(x, t)` será la densidad de energía electromagnética:
un número no negativo en cada punto del espacio, que puede cambiar con
el tiempo.

```
u(x, t) >= 0     para todo punto x y todo tiempo t
```

---

## 3. El tiempo: el parámetro del cambio

El **tiempo** `t` es el parámetro que etiqueta el orden de las
configuraciones. No lo asumimos como una dimensión del espacio ni como
algo fundamental — es simplemente el índice que nos permite comparar
dos instantáneas de un campo.

Dadas dos instantáneas `u(x, t_1)` y `u(x, t_2)` con `t_2 > t_1`,
la diferencia entre ellas debe tener una explicación — algo ocurrió
entre los dos momentos.

---

## 4. La derivada con respecto al tiempo: d/dt

La **derivada temporal** de un campo escalar `u(x, t)` mide la tasa
de cambio de `u` en un punto fijo `x` cuando el tiempo avanza:

```
du/dt  =  lim_{Dt->0}  [ u(x, t+Dt) - u(x, t) ] / Dt
```

Interpretación: si `du/dt > 0` en un punto, la energía en ese punto
está aumentando. Si `du/dt < 0`, está disminuyendo.

Cuando existen varias variables (espacio y tiempo), se habla de
**derivada parcial** — varía `t` manteniendo `x` fijo:

```
du/dt    significa: cuánto cambia u cuando t avanza, con x fijo
du/dx_1  significa: cuánto cambia u cuando x_1 avanza, con t fijo
```

La notación `d/dt` y `d/dx` se usará consistentemente para estas
operaciones.

---

## 5. Vectores: dirección y magnitud

Un **vector** en tres dimensiones es una terna de números reales que
representa una cantidad con dirección y magnitud:

```
V = (V_1, V_2, V_3)
```

La **magnitud** del vector es:

```
|V| = sqrt(V_1^2 + V_2^2 + V_3^2)
```

El **producto punto** de dos vectores `A` y `B` es un escalar:

```
A · B = A_1*B_1 + A_2*B_2 + A_3*B_3
```

Mide cuánto "van en la misma dirección". Si `A · B = 0`, los vectores
son ortogonales — perpendiculares entre sí.

El **producto vectorial** (o producto cruz) de dos vectores `A` y `B`
es un nuevo vector perpendicular a ambos:

```
A x B = ( A_2*B_3 - A_3*B_2,
          A_3*B_1 - A_1*B_3,
          A_1*B_2 - A_2*B_1 )
```

---

## 6. Campos vectoriales: un vector en cada punto

Un **campo vectorial** asigna un vector a cada punto del espacio:

```
F : (x_1, x_2, x_3)  -->  F(x_1, x_2, x_3) = (F_1, F_2, F_3)
```

Ejemplo físico: el viento. En cada punto del espacio hay una dirección
e intensidad del viento.

En lo que sigue, `S(x, t)` será el campo vectorial de flujo de energía
electromagnética — el vector de Poynting: en cada punto, indica cuánta
energía pasa por ahí y en qué dirección.

---

## 7. El gradiente: la dirección del cambio más rápido

El **gradiente** de un campo escalar `u` es un campo vectorial que
apunta en la dirección donde `u` crece más rápido:

```
grad(u) = ( du/dx_1,  du/dx_2,  du/dx_3 )
```

Si estás parado en una ladera, el gradiente de la altura apunta
cerro arriba. Su magnitud indica la pendiente.

Propiedad clave: el gradiente de un campo escalar siempre produce
un campo vectorial sin rotación — pero puede tener divergencia.

---

## 8. La divergencia: cuánto "sale" de un punto

La **divergencia** de un campo vectorial `F = (F_1, F_2, F_3)` es
un escalar que mide cuánto el campo "fluye hacia afuera" de un punto:

```
div(F) = dF_1/dx_1 + dF_2/dx_2 + dF_3/dx_3
```

**Interpretación física:** imagina el campo `F` como el flujo de agua.

- Si `div(F) > 0` en un punto: el agua "nace" ahí — hay una fuente.
- Si `div(F) < 0` en un punto: el agua "muere" ahí — hay un sumidero.
- Si `div(F) = 0` en un punto: lo que entra es igual a lo que sale.
  No hay creación ni destrucción local.

Un campo con `div(F) = 0` en todas partes se llama **libre de
divergencia** o **solenoidal**. El flujo de energía electromagnética
en el vacío tiene esta propiedad.

**Teorema de la divergencia** (fundamental): la integral del campo
sobre una superficie cerrada `dV` es igual a la integral de su
divergencia sobre el volumen `V` que encierra:

```
integral_{dV}  F · n  dA  =  integral_V  div(F)  dV
```

donde `n` es el vector normal exterior a la superficie. Este teorema
convierte afirmaciones locales (div = 0) en afirmaciones globales
(nada sale del volumen si no entra).

---

## 9. El rotor (curl): cuánto "rota" un campo

El **rotor** de un campo vectorial `F = (F_1, F_2, F_3)` es un campo
vectorial que mide la rotación local del campo alrededor de cada punto:

```
curl(F) = ( dF_3/dx_2 - dF_2/dx_3,
            dF_1/dx_3 - dF_3/dx_1,
            dF_2/dx_1 - dF_1/dx_2 )
```

**Interpretación física:** imagina una pequeña rueda de paletas sumergida
en el flujo `F`.

- Si `curl(F) != 0` en un punto: la rueda gira — hay rotación local.
- Si `curl(F) = 0` en un punto: la rueda no gira — el flujo es
  localmente irrotacional.

El rotor captura la circulación del campo. Un remolino de agua tiene
rotor no nulo en su centro.

**Identidad algebraica clave** — siempre se cumple, sin excepción:

```
div(curl(F)) = 0     para cualquier campo F
```

La divergencia del rotor de cualquier campo es siempre cero. Esto no
es una propiedad física especial — es una identidad algebraica pura,
consecuencia de que las derivadas mixtas son iguales:
`d^2F / (dx_i dx_j) = d^2F / (dx_j dx_i)`.

Esta identidad es el corazón de toda la construcción que sigue.

---

## 10. El Laplaciano: la segunda derivada espacial

El **Laplaciano** de un campo escalar `u` es la divergencia de su
gradiente:

```
laplacian(u) = div(grad(u))
             = d^2u/dx_1^2 + d^2u/dx_2^2 + d^2u/dx_3^2
```

**Interpretación física:** el Laplaciano compara el valor de `u` en un
punto con el promedio de sus vecinos.

- Si `laplacian(u) > 0`: el punto tiene menos que sus vecinos —
  el campo "tiende hacia" ese punto.
- Si `laplacian(u) < 0`: el punto tiene más que sus vecinos —
  el campo "huye" de ese punto.
- Si `laplacian(u) = 0`: el punto vale exactamente el promedio
  de sus vecinos (condición armónica).

Para un campo vectorial, el Laplaciano se aplica componente a componente:

```
laplacian(F) = ( laplacian(F_1), laplacian(F_2), laplacian(F_3) )
```

**Segunda identidad clave** — para campos libres de divergencia:

```
Si div(F) = 0:

   curl(curl(F)) = grad(div(F)) - laplacian(F)
                 = -laplacian(F)
```

Esto significa: aplicar rotor dos veces sobre un campo sin divergencia
produce el negativo del Laplaciano. Esta identidad es la que produce
la ecuación de onda al aplicar rotor dos veces a las ecuaciones de
Maxwell.

---

## 11. Resumen de las herramientas

```
Campo escalar:     u(x,t)              -- un número en cada punto
Campo vectorial:   F(x,t)              -- un vector en cada punto

Derivada temporal:
   du/dt  =  lim_{Dt->0} [u(t+Dt)-u(t)] / Dt

Gradiente:
   grad(u) = ( du/dx_1, du/dx_2, du/dx_3 )

Divergencia:
   div(F) = dF_1/dx_1 + dF_2/dx_2 + dF_3/dx_3

Rotor:
   curl(F) = ( dF_3/dx_2 - dF_2/dx_3,
               dF_1/dx_3 - dF_3/dx_1,
               dF_2/dx_1 - dF_1/dx_2 )

Laplaciano:
   laplacian(u) = d^2u/dx_1^2 + d^2u/dx_2^2 + d^2u/dx_3^2

Identidades algebraicas (siempre ciertas):
   div(curl(F)) = 0                         [I]
   curl(curl(F)) = -laplacian(F)            [II, cuando div(F)=0]

Teorema de la divergencia:
   integral_{dV} F·n dA = integral_V div(F) dV
```

Con estas herramientas en mano, podemos hablar de física.

---

*Continúa en: Parte II — La Física desde lo Mínimo*

---

*Evaluación independiente basada en los documentos del Programa de
Investigación del Universo de Maxwell [1–12]. Ver referencias completas
al final de la Parte III.*
