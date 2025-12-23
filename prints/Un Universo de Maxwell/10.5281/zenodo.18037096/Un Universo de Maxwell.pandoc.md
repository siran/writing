---
title: Un Universo de Maxwell
subtitle: |+
  Todo lo conocido a partir de energía electromagnética.
  Parte I
author: An M. Rodriguez
description: Recuperar masa y carga a partir de energía electromagnética en un universo de Maxwell sin fuentes; o qué habría ocurrido si Maxwell hubiese precedido a Newton.
series: Un Universo de Maxwell
publisher: Preferred Frame Prints
editor: An M. Rodriguez
lang: es-ES
rights: CC-BY-NC-ND-4.0
cover-image: https://assets.preferredframe.com/A%20Maxwell%20Universe/Un%20Universo%20de%20Maxwell.png
identifier:
- scheme: DOI
  text: doi:10.5281/zenodo.17982296
fontsize: 12pt
linestretch: 1.32
header-includes:
  - \renewcommand{\footnotesize}{\fontsize{11pt}{13pt}\selectfont}
  - \setlength{\skip\footins}{16pt}
  - \usepackage{titlesec}
  - \titleformat{\section}[block]{\bfseries\Large\raggedleft}{\hfill\thesection.}{0.8em}{\hfill}
  - \titlespacing*{\section}{0pt}{4ex plus 1ex minus 0.5ex}{1.8ex}
---

```{=latex}
\clearpage
\thispagestyle{empty}
\vspace*{0.30\textheight}
\begin{center}
{\bfseries\Large Dedicatoria}\par
\vspace{2.2em}
{\itshape A mi amigo, que contribuyó a casi toda idea aquí escrita; a sabiendas, ignorándolas, o incluso contradiciéndolas.\par \vspace{0.6em} A ti también, lector.}\par
\end{center}
\clearpage
```

```{=html}
<div class="page-break"></div>
```

```{=latex}
\iffalse
```
# Dedicatoria {#dedicatoria .chapter .unlisted}

A mi amigo, que contribuyó a casi toda idea aquí escrita; a sabiendas,
ignorándolas, o incluso contradiciéndolas.

A ti también, lector.

```{=latex}
\fi
```

```{=latex}
\clearpage
\thispagestyle{empty}
\begin{center}
\vspace*{0.11\textheight}
{\bfseries\fontsize{24pt}{32pt}\selectfont Tabla de Contenidos}\par
\end{center}
\vspace{1.0em}
\noindent{\color[gray]{0.65}\rule{\textwidth}{0.6pt}}
\color{black}
\vspace{2.0em}
```

```{=html}
<div class="page-break"></div>
<h1 class="toc-page-title">Tabla de Contenidos</h1>
```

\begingroup
\setcounter{tocdepth}{1}
\renewcommand{\contentsname}{}
\setlength{\parskip}{0.35em}
\tableofcontents
\endgroup

```{=html}
<div class="toc">
<ul>
<li><a href="#prefacio">Prefacio</a>
</li>
<li><a href="#parte-i-fundamentos-de-la-realidad">PARTE I — FUNDAMENTOS DE LA REALIDAD</a>
</li>
<li><a href="#1-de-la-oscuridad-luz">1. De la oscuridad, luz</a>
</li>
<li><a href="#2-tiempo">2. Tiempo</a>
</li>
<li><a href="#3-ordenamientos">3. Ordenamientos</a>
</li>
<li><a href="#4-conteo-de-pasos">4. Conteo de pasos</a>
</li>
<li><a href="#5-espacio">5. Espacio</a>
</li>
<li><a href="#6-platn-y-la-caverna">6. Platón y la caverna</a>
</li>
<li><a href="#7-lgica-matemticas-y-realidad">7. Lógica, matemáticas y realidad</a>
</li>
<li><a href="#apndice-supuestos-y-compromisos-derivados">Apéndice — Supuestos y compromisos derivados</a>
</li>
<li><a href="#sinopsis">Sinopsis</a>
</li>
</ul>
</div>
```


```{=html}
<div class="page-break"></div>
```

```{=latex}
\clearpage
\thispagestyle{empty}
\begin{center}
\vspace*{0.28\textheight}
{\begingroup\setlength{\baselineskip}{2.1\baselineskip}
{\bfseries\fontsize{26pt}{52pt}\selectfont Prefacio}\par
\endgroup}
\end{center}
\clearpage
```

```{=latex}
\vspace*{0.18\textheight}
```
# Prefacio {#prefacio .chapter}

Este texto constituye la primera parte de *Un Universo de Maxwell*, pero ha sido
escrito deliberadamente para poder leerse como un documento autónomo.

No presupone teorías físicas específicas, ni requiere aceptar conclusiones
desarrolladas en volúmenes posteriores. Su único compromiso es metodológico:
partir de lo mínimo que puede afirmarse sin introducir entidades, estructuras
o leyes de manera prematura, innecesaria o no fundamentada en hechos.

Aquí no se asume espacio, tiempo, materia, campos, partículas, ni marcos
geométricos. Tampoco se asume lógica, matemática o leyes físicas como
fundamentales. En su lugar, el texto explora lo que puede reconstruirse a partir
exclusivamente de relaciones que aparecen como “causas” y “efectos”.

El objetivo de esta primera parte no es proponer una teoría física alternativa,
sino establecer un fundamento ontológico claro sobre el cual cualquier dinámica
posterior —incluida una ontología basada únicamente en las ecuaciones de
electromagnetismo de Maxwell— pueda construirse sin ambigüedad conceptual.

El lector no está invitado a estar de acuerdo, sino a seguir el razonamiento.
Si las conclusiones no resultan convincentes, el punto de desacuerdo debería
poder señalarse con precisión.

En ese sentido, este texto no pretende cerrar debates, sino hacerlos
operacionalmente claros.

```{=latex}
\clearpage
\thispagestyle{empty}
\begin{center}
\vspace*{0.28\textheight}
{\begingroup\setlength{\baselineskip}{2.1\baselineskip}
{\bfseries\fontsize{26pt}{52pt}\selectfont PARTE I — FUNDAMENTOS DE LA REALIDAD}\par
\endgroup}
\end{center}
\clearpage
```

```{=latex}
\vspace*{0.18\textheight}
```
# PARTE I — FUNDAMENTOS DE LA REALIDAD {#parte-i-fundamentos-de-la-realidad .chapter}

La Parte I desarrolla un marco en el que los eventos son el punto de partida, en
lugar del tiempo o el espacio.

Un cambio registrado crea la distinción básica entre “antes” y “después”.

Sistemas que actualizan su estado en respuesta a influencias construyen
ordenamientos internos y, a partir de esos ordenamientos, emerge el tiempo.

Los pasos causales enlazan eventos en cadenas y, luego, en bucles. Los bucles
sostienen patrones recurrentes y pueden funcionar como relojes. Contar pasos
causales da duración y también distancia: el número mínimo de pasos entre dos
eventos. Al reunir todas las distancias por pares se obtiene una geometría
efectiva.

El espacio y la dimensión emergen cuando estas distancias pueden mapearse con
baja distorsión en un espacio de alguna dimensión. Múltiples mapeos implican una
dimensión no única; el fracaso de todo mapeo de baja distorsión implica que la
geometría no aplica. El espacio y la dimensión son, por tanto, constructos
relacionales, no ingredientes fundamentales de la realidad.

El mismo mecanismo de compresión explica la aritmética y las leyes matemáticas.
Patrones estables se vuelven reglas simbólicas; cuando los patrones cambian, las
reglas cambian con ellos. La matemática funciona allí donde la realidad ofrece
regularidades y falla allí donde no las ofrece.

A lo largo de la Parte I se repite un tema: no accedemos a la estructura causal
subyacente en sí misma; accedemos solo a sus efectos, y a partir de ellos
construimos representaciones que siguen siendo válidas únicamente mientras los
patrones observados permanezcan estables.

```{=latex}
\clearpage
\thispagestyle{empty}
\begin{center}
\vspace*{0.28\textheight}
{\begingroup\setlength{\baselineskip}{2.1\baselineskip}
{\bfseries\fontsize{26pt}{52pt}\selectfont 1. De la oscuridad, luz}\par
\endgroup}
\end{center}
\clearpage
```

```{=latex}
\vspace*{0.18\textheight}
```
# 1. De la oscuridad, luz {#1-de-la-oscuridad-luz .chapter}

La realidad no comienza con el espacio o el tiempo, sino con el hecho
simple de que hay eventos que ocurren.

A menudo asumimos que los eventos ocurren por una razón. Esto no tiene por qué
ser así y, aun si lo fuera, no tenemos acceso directo a la información causal,
sino solo de manera indirecta, a través de sus efectos.

Una razón es una historia añadida después. Lo que importa es simplemente que
ocurra un cambio y que este sea registrado de un modo que afecte a lo que
sigue. Una vez que un cambio es registrado, el sistema ocupa un estado
distinto. La distinción entre “antes” y “después” no se añade al evento; es el
evento en sí.

No es necesario apelar a una inteligencia que registre lo ocurrido, sino solo
a un cambio de estado persistente —como una marca en una mesa— que restringe
las interacciones futuras. La marca no es un registro del evento. La marca *es*
el evento, en la medida en que produce una diferencia.

El sentido de razón o de explicación surge únicamente como una historia
reactiva, una forma de organizar transiciones una vez que el cambio ha sido
notado por una entidad capaz de razonar (tema que se aborda más adelante en
[^EmergenceOfSelf]).

Esta reactividad no se limita a las mentes conscientes. Todo aquello que cambia
en respuesta a causas y produce efectos es, en este sentido mínimo,
**operacionalmente consciente** [^OperationalAwareness]. Un bucle causal
auto-sostenido cumple esta condición: puede actualizar su propio estado en
respuesta a influencias entrantes. Al hacerlo, distingue estados y sigue
transiciones, no mediante ningún “plan de acción”, lo cual implicaría una
conciencia que aún no hemos definido, sino simplemente en virtud de su
existencia continuada como bucle. En este sentido operativo mínimo, un bucle
causal auto-sostenido “nota” el cambio.

[^OperationalAwareness]: Palma, A., & Rodriguez, A. M. (2025). *Operational Awareness in a Maxwell-Only Universe: A Formal Implication of Panpsychism*. ResearchGate. https://doi.org/10.13140/RG.2.2.13647.60324/1

[^EmergenceOfSelf]: Rodriguez, A. M. (2025). *Emergence of Self-Awareness from a Cause–Effect Loop*. https://preprints.preferredframe.com/Emergence%20of%20Self-Awareness%20from%20a%20Cause%E2%80%93Effect%20Loop/Emergence%20of%20Self-Awareness%20from%20a%20Cause%E2%80%93Effect%20Loop%20v2.md.html

```{=latex}
\clearpage
\thispagestyle{empty}
\begin{center}
\vspace*{0.28\textheight}
{\begingroup\setlength{\baselineskip}{2.1\baselineskip}
{\bfseries\fontsize{26pt}{52pt}\selectfont 2. Tiempo}\par
\endgroup}
\end{center}
\clearpage
```

```{=latex}
\vspace*{0.18\textheight}
```
# 2. Tiempo {#2-tiempo .chapter}

El tiempo es, por tanto, un constructo útil: una herramienta que la conciencia
operativa utiliza para organizar su estado. Cada bucle forma su propia noción
interna de tiempo. Sin embargo, mantenemos acuerdos colectivos: ciertos patrones
de eventos (“causas”) tienden a preceder a otros (“efectos”). Quienes no
comparten la interpretación dominante suelen ser considerados “irracionales”,
aunque esto solo refleja diferentes correspondencias entre cambio y orden.

Podemos considerar la “realidad” [^WhatIsReality?] como un Nodo con una
estructura interna incognoscible [^Uncomputable], inescrutable o simplemente
inaccesible. Todo lo que sabemos es que dicha estructura parece reproducir de
forma consistente patrones de transiciones a partir de los cuales inferimos
“antes” y “después”.

Lo que llamamos “el pasado” se reconstruye *ahora*, a partir de evidencia
presente. Si aparece nueva evidencia, nuestra reconstrucción —“el pasado”— puede
cambiar. El prolongado debate sobre si la grasa dietaria era perjudicial o
beneficiosa es un ejemplo conocido que más tarde se demostró que había
utilizado datos selectivos [^FatDebate]. La realidad consensuada es frágil. Sin
anclajes externos, las interpretaciones se sienten arbitrarias, lo que da lugar
a la pregunta persistente: ¿qué es real?

[^WhatIsReality?]: La realidad —“todo lo que es”— incluye todo lo que puedes
pensar y todo aquello que sospechas que existe aunque no lo consideres de
manera consciente. Cualquier definición formal es parcial.

[^Uncomputable]: Como en la caverna de Platón: la estructura subyacente es
inaccesible en principio. Solo vemos sombras y llamamos a algunas “causas” y a
otras “efectos”.

[^FatDebate]: A finales del siglo XX, la ciencia de la nutrición presentó a la
grasa como la principal causa de las enfermedades cardíacas, pero revisiones
posteriores mostraron informes selectivos e influencia industrial. Datos
contradictorios habían sido minimizados. Un nuevo análisis reveló una relación
más débil de la que se afirmaba, mostrando cómo puede formarse un consenso a
partir de evidencia distorsionada.

```{=latex}
\clearpage
\thispagestyle{empty}
\begin{center}
\vspace*{0.28\textheight}
{\begingroup\setlength{\baselineskip}{2.1\baselineskip}
{\bfseries\fontsize{26pt}{52pt}\selectfont 3. Ordenamientos}\par
\endgroup}
\end{center}
\clearpage
```

```{=latex}
\vspace*{0.18\textheight}
```
# 3. Ordenamientos {#3-ordenamientos .chapter}

A partir de la relación primitiva

$$
n_i \succ n_j,
$$

que significa (siendo $n_i$ y $n_j$ estados registrados) “$n_i$ precede a
$n_j$”, surge un ordenamiento: antes y después. Podemos llamar a esta sucesión
de eventos $i$ y $j$ un **paso causal**.

Una sucesión de eventos forma una **cadena causal**: i $\to$ a $\to$ b $\to$ c $\to$ d $\to$ j.

Las cadenas pueden formar bucles:

... $\to$ j $\to$ i $\to$ a $\to$ b $\to$ c $\to$ j $\to$ i $\to$ ...

y pueden cruzarse consigo mismas sin restricción. El aprendizaje ofrece una
buena ilustración de múltiples **registros efectivos** y, por tanto, de
múltiples “cierres”.

Un bucle puede considerarse “cerrado” cuando su patrón se estabiliza en algún
sentido útil, es decir, cuando su persistencia queda asegurada. Sin
embargo, un bucle “cerrado” debe continuar propagándose, como se mencionará más
adelante.

Los bucles causales recurrentes (i $\to$ {a, b, c} $\to$ i $\to$ {d, e, f} $\to$ i …) pueden
funcionar como relojes. La precisión puede variar, pero la recurrencia es
suficiente.

Nótese que un efecto que no produce causas posteriores marca el final de una
cadena causal. Tal punto final no puede ser registrado: no hay influencia de
retorno. Por lo tanto, el hecho mismo de que algo sea notado implica que el
notador es, en esencia, un bucle causal auto-sostenido.

```{=latex}
\clearpage
\thispagestyle{empty}
\begin{center}
\vspace*{0.28\textheight}
{\begingroup\setlength{\baselineskip}{2.1\baselineskip}
{\bfseries\fontsize{26pt}{52pt}\selectfont 4. Conteo de pasos}\par
\endgroup}
\end{center}
\clearpage
```

```{=latex}
\vspace*{0.18\textheight}
```
# 4. Conteo de pasos {#4-conteo-de-pasos .chapter}

Al contar bucles o pasos causales, la conciencia operativa define duraciones. El
tiempo es un conteo emergente, no un parámetro externo.

La distancia surge al contar cuántos pasos causales conectan dos eventos. Si una
señal viaja desde el evento $i$ hasta el evento $j$ a través de una cadena mínima
de longitud $L_{ij}$, entonces

$$
d(i, j) \propto L_{ij}.
$$

Si no existe ningún camino, la distancia es infinita o indefinida. Si el único
camino disponible regresa al mismo evento, el conteo de ida y vuelta se
convierte en una medida efectiva de separación.

La distancia, por tanto, no es una coordenada espacial, sino una medida
operativa de separación causal.

Estas distancias causales definen una geometría efectiva. Los observadores
intentan representarlas en espacios familiares de alguna dimensión elegida.

De forma más técnica, podemos pensar en un mapa $\mathcal{M}$ hacia un espacio
de dimensión $D$, donde a cada evento se le asigna un punto, y las distancias
entre esos puntos aproximan las distancias causales $d$:

$$
\|\mathcal{M}(i) - \mathcal{M}(j)\| \approx d(i, j).
$$

Cuando tales mapas presentan baja distorsión, los observadores operativos
perciben los eventos correspondientes como formando una estructura de dimensión
$D$ bajo el mapa $\mathcal{M}$. Si múltiples mapeos funcionan, la dimensión no
es única. Si ninguno lo hace, todos esos mapas son defectuosos y la geometría
resulta mal definida.

Así, el espacio, el tiempo y la dimensión no son fundamentales; surgen de la
forma en que la conciencia operativa comprime patrones relacionales. La
geometría y la distancia aparecen solo después de que patrones causales
repetidos se estabilizan en expectativas.

```{=latex}
\clearpage
\thispagestyle{empty}
\begin{center}
\vspace*{0.28\textheight}
{\begingroup\setlength{\baselineskip}{2.1\baselineskip}
{\bfseries\fontsize{26pt}{52pt}\selectfont 5. Espacio}\par
\endgroup}
\end{center}
\clearpage
```

```{=latex}
\vspace*{0.18\textheight}
```
# 5. Espacio {#5-espacio .chapter}

Si la distancia es el conteo de pasos causales entre dos eventos, entonces lo
que llamamos “espacio” es el conjunto de todas esas distancias.

Al reunir las separaciones causales en una sola estructura, la conciencia
operativa intenta formar una representación geométrica coherente.

Si el conjunto completo de distancias causales puede mapearse con baja
distorsión [^DistorsionYUtilidad] en algún espacio de dimensión $D$, decimos que
los eventos parecen ser $D$-dimensionales. Si no existe ningún mapeo de baja
distorsión, la noción misma de dimensión se descompone.

Los mismos datos de distancia pueden admitir múltiples mapeos. Una
configuración puede ajustarse a un triángulo, a dos triángulos superpuestos, a
una estrella u otras formas. Nada impone una interpretación única; distintas
interpretaciones pueden incluso coexistir y funcionar adecuadamente.

Solo tenemos efectos —las distancias causales— y, a partir de ellos, inferimos
patrones con una precisión operativamente aceptable. El mapeo preferido suele
ser (aunque no siempre) aquel que comprime las relaciones con mínima
complejidad manteniendo una distorsión tolerable. La navaja de Occam refleja
esta preferencia.

Este mecanismo de reconocimiento de patrones no se limita a la geometría. La
aritmética emerge del mismo modo. Actos causales repetidos —poner una manzana en
una bolsa y luego otra— se estabilizan en un patrón fiable. A partir de ello, la
conciencia operativa forma la abstracción de que $1+1=2$. Si dos manzanas
produjeran de forma fiable tres, la aritmética codificaría eso, y volveríamos a
considerar el universo como “matemático”. La regla no se descubre bajo la
realidad; se extrae de efectos considerados suficientemente consistentes y luego
se utiliza para predecir efectos adicionales.

En algunos contextos, $1+1$ puede tomar cualquier valor permitido por las
reglas. Puede definirse un sistema formal en el que $1+1=3$ y construir a partir
de él una matemática consistente. Incluso en contextos cotidianos, combinar dos
cosas rara vez duplica una cantidad de manera limpia. El resultado depende de
las reglas de combinación: postura, palanca, estrategia. Solo una vez que esas
reglas son acordadas, la expresión $1+1=2$ se convierte en el enunciado
correcto. La “verdad” de la aritmética refleja supuestos operativos, no el
sustrato causal.

El espacio, el tiempo, la dimensión y la aritmética surgen del mismo mecanismo:
reconocer regularidades en eventos conectados causalmente y comprimirlas en
representaciones estables y predictivas.

[^DistorsionYUtilidad]: Es decir, operativamente útil para la persistencia del
bucle.

```{=latex}
\clearpage
\thispagestyle{empty}
\begin{center}
\vspace*{0.28\textheight}
{\begingroup\setlength{\baselineskip}{2.1\baselineskip}
{\bfseries\fontsize{26pt}{52pt}\selectfont 6. Platón y la caverna}\par
\endgroup}
\end{center}
\clearpage
```

```{=latex}
\vspace*{0.18\textheight}
```
# 6. Platón y la caverna {#6-platn-y-la-caverna .chapter}

Platón ilustró los límites de nuestro acceso a la realidad con su famosa
*Alegoría de la caverna* [^LaCavernaDePlaton]: vemos sombras, no los objetos que
las producen, la fuente real.

Nuestras interpretaciones son reconstrucciones moldeadas por una observación
limitada. No existe un punto de vista externo desde el cual pueda contemplarse
la estructura verdadera ni de manera completa.

No tenemos acceso directo —o, dicho de otro modo, nunca podemos observar— el
sustrato causal subyacente de la realidad; solo registramos los efectos.

Cualquier geometría, dimensión o patrón que asignemos refleja la forma en que
estos efectos pueden comprimirse en una representación utilizable. Un
observador distinto, o un muestreo distinto de la misma estructura causal,
puede construir una representación diferente sin contradicción.

Las sombras en la caverna de Platón corresponden a los patrones relacionales que
detectamos. Los “objetos” que proyectan esas sombras son las relaciones
causales subyacentes, inaccesibles en sí mismas. Inferimos su organización a
partir de efectos recurrentes y, cuando esos efectos cambian, la imagen
inferida debe cambiar con ellos. Ninguna representación que construyamos está
garantizada como única, completa, consistente o estable.

Esta perspectiva elimina la suposición de que exista una única descripción
espacial o matemática correcta esperando ser descubierta. Nuestros modelos no
son espejos de una geometría externa; son herramientas operativas construidas a
partir de las limitadas regularidades que podemos registrar. Como los
prisioneros en la caverna, trabajamos con proyecciones, no con la estructura que
las produce.

Lo que llamamos “realidad” es, por tanto, una reconstrucción: un arreglo
estable de patrones inferidos que sigue siendo útil mientras los efectos
causales disponibles lo sostengan.

[^LaCavernaDePlaton]: Platón, *La República*, Libro VII. La alegoría describe a
prisioneros encadenados que solo ven sombras proyectadas en una pared y las
toman por la realidad, sin acceso directo a los objetos ni a la fuente de la
luz que las produce.

```{=latex}
\clearpage
\thispagestyle{empty}
\begin{center}
\vspace*{0.28\textheight}
{\begingroup\setlength{\baselineskip}{2.1\baselineskip}
{\bfseries\fontsize{26pt}{52pt}\selectfont 7. Lógica, matemáticas y realidad}\par
\endgroup}
\end{center}
\clearpage
```

```{=latex}
\vspace*{0.18\textheight}
```
# 7. Lógica, matemáticas y realidad {#7-lgica-matemticas-y-realidad .chapter}

Mucho se ha dicho sobre que la realidad es “matemática”, aunque rara vez se
define qué significa exactamente esa afirmación. Los argumentos anteriores
sugieren una visión más simple: atribuimos patrones a la realidad. A veces los
reconocemos genuinamente; otras veces los proyectamos y luego tratamos esa
proyección como si fuese real.

Las matemáticas no tienen por qué, y en ningún sentido se entiende que,
gobiernen el mundo. Incluso si la realidad admite estructura matemática en algún
sentido, las matemáticas son inmensamente más vastas que cualquier cosa que el
mundo físico pueda instanciar. La mayor parte de las matemáticas no tiene, hasta
donde sepamos, ningún correlato físico.

Con mayor frecuencia, vemos el mundo a través de las matemáticas que hemos
construido. Las matemáticas —y, por extensión, la física— describen aquellos
aspectos de la realidad que presentan patrones estables y compresibles. Cuando
un patrón es lo suficientemente regular como para ser anticipado, lo
codificamos simbólicamente y lo llamamos “ley”. Cuando el patrón se rompe, la
ley se rompe con él.

No es, entonces, que la realidad sea matemática, ni que las matemáticas sean el
“lenguaje de la naturaleza”. Más bien, las matemáticas son una herramienta de
modelado que aplicamos a las regularidades que podemos aislar y predecir. Allí
donde la realidad resiste ser comprimida en patrones estables, las matemáticas
simplemente no aplican.

Las matemáticas funcionan porque seleccionamos qué pueden describir —y a qué
patrones prestamos atención—, no porque la naturaleza esté hecha de números,
estructuras o, en su reetiquetado más reciente, “información”.

Lo mismo ocurre con la lógica. La lógica no es una ley impuesta a la realidad;
es una abstracción destilada de comportamientos considerados causales estables y
repetibles. La lógica clásica refleja un mundo en el que los estados están bien
separados y las transiciones son consistentes.

Así como la geometría espacial emerge de la compresión de distancias causales
en mapeos de baja distorsión (§§4–5), la estructura lógica emerge de la
compresión de transiciones causales en reglas de inferencia estables.

Cuando las estructuras causales cambian, la lógica extraída de ellas también
cambia. Que la física moderna tolere superposición o descripciones
incompatibles no significa que la realidad viole la lógica; significa que las
categorías lógicas clásicas ya no comprimen adecuadamente los patrones causales
observados.

Este trabajo, por tanto, no parte ni de la lógica ni de las matemáticas, sino de
patrones que aparecen como “causas” y “efectos”. La lógica y las matemáticas
aparecen más tarde, como herramientas moldeadas por las regularidades que las
interacciones causales resultan exhibir.

```{=latex}
\clearpage
\thispagestyle{empty}
\begin{center}
\vspace*{0.28\textheight}
{\begingroup\setlength{\baselineskip}{2.1\baselineskip}
{\bfseries\fontsize{26pt}{52pt}\selectfont Apéndice — Supuestos y compromisos derivados}\par
\endgroup}
\end{center}
\clearpage
```

```{=latex}
\vspace*{0.18\textheight}
```
# Apéndice — Supuestos y compromisos derivados {#apndice-supuestos-y-compromisos-derivados .chapter}

Este trabajo adopta una ontología mínima. Solo los tres primeros supuestos son primitivos; los demás se derivan de ellos.


## A.1 Supuestos fundamentales

**A1. Hay eventos que ocurren.**
Es decir, hay cambios.

**A2. Un cambio puede ser registrado.**
Algunos cambios persisten como diferencias de estado.

**A3. Un cambio registrado es en sí mismo el efecto que sigue.**
Un cambio registrado es un nuevo estado, y no se requiere nada más.

No se asumen el espacio, el tiempo, la materia, las leyes, la lógica ni las
matemáticas.


## A.2 Compromisos derivados

Los siguientes se derivan de A1–A3.

**A4. Existe el orden.**
Si un cambio registrado es un nuevo estado, existe una distinción entre
“antes” y “después”. Esto define un orden.

**A5. El tiempo es orden, no sustancia.**
El tiempo surge a partir de la identificación operacional de estados etiquetados
como “antes” y “después”.

**A6. La existencia es persistencia.**
Todo lo que existe lo hace solo en la medida en que sostiene su propio estado.
Un punto final de una cadena causal que no produce efectos subsecuentes no es
observable y, por tanto, es operacionalmente equivalente a la inexistencia.

El espacio, la distancia, la geometría, la dimensión, las matemáticas y la
lógica surgen como compresiones adicionales de patrones estables en estos
ordenamientos, como se desarrolla en §§4–7.


## A.3 No-supuestos

Este trabajo **no** asume:

- El espacio como un contenedor.
- El tiempo como un parámetro que fluye.
- El espaciotiempo como una estructura fundamental.
- La geometría como primitiva.
- La dimensión como intrínseca.
- La materia, la masa, las partículas, los campos, las fuerzas o las cargas como
  sustancias o dinámicas ontológicamente separadas y no electromagnéticas.
- Postulados cuánticos o axiomas probabilísticos.
- Objetos matemáticos como ontológicamente previos.
- Observadores como entidades fundamentales.
- La conciencia como primitiva.

Todas estas nociones aparecen, si lo hacen, solo como **descripciones
emergentes** derivadas de patrones estables de causa–efecto.


## A.4 Alcance y límites

Esta parte no hace afirmaciones sobre la naturaleza última del sustrato causal.
Aborda únicamente lo que puede inferirse a partir de los efectos observables y
sus regularidades.

Toda representación construida aquí sigue siendo válida solo en la medida en
que los patrones observados persistan. No se afirma ninguna garantía de
unicidad, completitud ni permanencia.


## A.5 Rol en la obra completa

La Parte I establece el fundamento ontológico requerido para el desarrollo
posterior de un universo exclusivamente regido por las ecuaciones del
electromagnetismo de Maxwell.

Las partes siguientes presentan dinámicas específicas. Nada en esta parte
depende de esas dinámicas, y nada en las partes posteriores modifica los
supuestos enumerados arriba.

```{=latex}
\clearpage
\thispagestyle{empty}
\begin{center}
\vspace*{0.28\textheight}
{\begingroup\setlength{\baselineskip}{2.1\baselineskip}
{\bfseries\fontsize{26pt}{52pt}\selectfont Sinopsis}\par
\endgroup}
\end{center}
\clearpage
```

```{=latex}
\vspace*{0.18\textheight}
```
# Sinopsis {#sinopsis .chapter}

Un Universo de Maxwell parte de una premisa simple: hay eventos que ocurren.

Un cambio registrado introduce orden. A partir de relaciones de causa–efecto se
definen el tiempo, la distancia, el espacio, la dimensión, las matemáticas y las
leyes físicas. No se asume la preexistencia de un espaciotiempo ni de
estructuras fundamentales. El sustrato subyacente, si lo hay, no es accesible de
forma directa: solo se manifiesta a través de efectos cuyas regularidades son
comprimidas en modelos simbólicos.

La Parte I establece este fundamento ontológico. Prepara el terreno para
volúmenes posteriores, donde la materia, la masa y la carga no aparecen como
entidades puntuales primitivas, sino como configuraciones electromagnéticas
extendidas y auto-sostenidas, gobernadas enteramente por la dinámica de las
ecuaciones de Maxwell.