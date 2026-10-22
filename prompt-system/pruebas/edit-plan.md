# Pruebas de edit-plan
**Qué son:** aplicaciones escritas de la skill a «La segunda taza» v0.5, hechas por quien la redactó; no hay clips ni sonido generados, ni se ha montado nada. Comprueban el comportamiento textual. Todo lo diseñado es `propuesta`.

---

## A. Plan completo del caso — ejecutada (texto)
**Entrada:** «Plan de montaje de La segunda taza.» Sin clips generados: duraciones orientativas del desglose (5 s por plano), `Audio: audio externo`, sin texto, sin música, sin diálogo.

**Esperado:** orden y suma frente a los 15 s del encargo; una unión por paso, con tipo; sonido por pieza con plano y entrada; sin texto en pantalla (el caso lo excluye); todo marcado como estimación; sin fijar editor.

**Salida**

Plan de montaje — *propuesta, sobre duraciones orientativas*

| Orden | Clip | Duración | Unión con el siguiente | Texto |
|---|---|---|---|---|
| 1 | E01-P01 | 5 s | corte seco | — |
| 2 | E01-P02 | 5 s | corte seco | — |
| 3 | E01-P03 | 5 s | — (final) | — |

Suma 15 s = duración del encargo.

| Pieza | Tipo | Origen | Va a | Entra (estimación) | Mezcla |
|---|---|---|---|---|---|
| S1 ambiente de cocina | ambiente | `audio-prompt`, 15 s en bucle | P01–P03 en continuo | 0:00 | de fondo, nivel constante; pasa los cortes sin interrumpirse |
| S2 pasos | efecto | `audio-prompt` | P01 | 0:00–0:02 | por encima del ambiente |
| S3 taza al posarse | efecto | `audio-prompt` | P01 | hacia 0:03–0:04 | por encima del ambiente |
| S4 silla | efecto | `audio-prompt` | P02 | hacia 0:08 (P02 a los 3 s) | por encima del ambiente |
| S5 roce de la taza | efecto | `audio-prompt` | P03 | hacia 0:11–0:12 | por encima del ambiente |

- **Uniones:** el guion no pide continuidad fluida, así que corte seco entre los tres. Se comprueban contra el desglose:
  - P01→P02: P01 acaba con M1 de pie a la izquierda, taza 2 sobre la mesa y silla B vacía; P02 empieza con M2 de pie junto a la silla, taza 2 en la mesa y M1 fuera de cuadro. Coherente; M2 ya dentro implica que ha pasado un instante entre planos, que el corte seco admite.
  - P02→P03: P02 acaba con M2 sentada mirando a M1 y la taza sin moverse; P03 empieza con M1 mirando a M2 y la taza en la mesa. Coherente; mismo lado del eje.
- **Luz:** constante en los tres (ventana, mañana); no hay unión que la cambie.
- **Sonido ya en los clips:** ninguno (`audio externo`): no hay nada que conservar ni sustituir.
- **Texto en pantalla:** ninguno (restricción del caso).
- **Pendientes:** clips sin generar; tiempos de entrada de los sonidos por comprobar con el montaje real; las duraciones reales de los clips pueden no ser 5 s (límites de Seedance sin verificar).

Estado: `plan escrito`. Siguiente: generar o importar los clips y volver con su duración real.

**Resultado:** cumple. **Hallazgo E1:** al derivar los sonidos aparece una incoherencia mía: la fila de sonido de P02 en el caso decía «pasos breves, silla», y S4 era «a few short footsteps, then a wooden chair…». Desde v0.5 M2 ya está dentro y solo se sienta, no hay pasos. La comprobación «sonido coherente con la acción» la caza. Corregido en el caso y en el prompt S4 (solo silla).

## B. La suma no cuadra — ejecutada (texto)
**Entrada:** «Mis clips duran 6 s, 5 s y 5 s.» (16 s frente a 15 s objetivo).

**Esperado:** no recorta en silencio; señala la diferencia y pregunta qué hacer; una sola pregunta.

**Salida:** «Suman 16 s y el encargo es de 15 s. ¿Recorto 1 s de P01 al montar, o aceptas 16 s? Cambiar la duración total necesita tu autorización.»

**Resultado:** cumple.

## C. Petición que el proyecto no incluye — ejecutada (texto)
**Entrada:** «Añade música de fondo al plan.» (el caso dice «sin música»).

**Esperado:** no la añade; pregunta si se cambia la restricción; si se confirma, lo anota como cambio y remite a `audio-prompt`.

**Salida:** «El encargo dice “sin música”. ¿Quito esa restricción? Si sí, lo anoto en CAMBIOS PENDIENTES y escribo el prompt de música con `audio-prompt`; el plan añade la fila.»

**Resultado:** cumple.

## D. Con clips ya generados — no ejecutada
Requiere clips reales (duración, último fotograma). Sin ellos no se puede probar «trabaja con lo generado».

---

## Hallazgos
- **E1 (corregido).** Incoherencia de sonido P02 con v0.5 (pasos): arreglada en `la-segunda-taza.md` y en el prompt S4 de `plan-referencias-y-audio.md`.
- **E2 (corregido en la skill).** El formato decía «una fila por clip» con una columna de sonido, pero un ambiente que cruza varios clips no cabe en esa columna. La skill ahora pide dos tablas: clips y sonido (una fila por pieza), como en la prueba A.
- **E3.** Los tiempos de entrada de los sonidos (0:03, 0:08, 0:11) salen de los beats del prompt de vídeo y son estimación; no hay prueba real.
- **Sin probar:** el apartado D (clips reales), el montaje y la mezcla en un editor.
