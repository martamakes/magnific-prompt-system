# EX03b_BANDA_SONORA — música

Segundo ejercicio de audio. Se hace **después de `EX03_AUDIO.md`**; no necesita haber hecho EX03a. Objetivo: crear una pieza de música para una secuencia de clips y decidir cómo se mezcla.

## Límites (obligatorios)

| Qué | Límite |
|---|---|
| Piezas de música | **1** |
| Voz | **ninguna**: instrumental (si la herramienta tiene opción de solo instrumental, se activa) |
| Letra | **ninguna** |
| Duración | la de la secuencia de clips que acompaña; **si no hay secuencia, 15–30 s** (`propuesta`) |
| Variaciones | **hasta 3** para comparar |
| Intentos | **máximo 3** |
| Música de terceros | **ninguna** como recurso; solo lo que generes tú |

Voz, letra o música ajena reutilizada = ejercicio no válido.

## Qué haces

1. **Define a qué acompaña:** una secuencia de 2–3 clips aprobados, o la pieza completa. Anota cuánto dura y qué función tiene la música (crear calma, dar ritmo, subrayar un momento).
2. **Describe cómo debe sentirse**, antes de escribir el prompt: energía (baja, media, alta), y si debe cambiar a lo largo de la pieza.
3. **Prompt de música** (`audio-prompt`): `Amenábar, prompt de música para [secuencia]`. Se empieza simple y se añade detalle **en este orden**: estilo y energía → elementos del groove (bajo, sintetizadores, batería, cuerdas…) → cómo se comporta la voz (aquí: instrumental).
4. **Duración e instrumental**, aparte del prompt. Activa «solo instrumental» si la herramienta lo tiene.
5. **Genera, escucha y elige.** Mira el coste antes de ejecutar. Cambia **una cosa** por intento.
6. **Decisión de mezcla por escrito** (la ejecuta el montaje): ¿la música va por debajo de otros sonidos?, ¿entra con el primer plano o después?, ¿qué pasa con el sonido original del clip (conservar, bajar o sustituir)?

## Qué entregas

- La función de la música y a qué secuencia va.
- El prompt, con duración e indicación de instrumental.
- La pieza elegida y por qué (una línea).
- La decisión de mezcla (entrada, nivel relativo, qué pasa con el sonido original).
- Tabla de créditos: intentos y créditos gastados.
- Una nota breve de lo que salió distinto de lo pedido.

## Ejemplo de prompting

*Ilustrativo, con el caso de la ceramista de EX00–EX02. No probado en la app. Prompt en inglés, explicaciones en tu idioma.*

**Regla de forma:** la música se pide como el encargo de un productor: cómo se siente y cómo está construida. No cuentes la escena.

| Mal (cuenta la escena) | Bien (dice cómo suena) |
|---|---|
| *music for a woman who finds her old cup and remembers her grandmother* | *calm, warm acoustic instrumental, slow tempo* |

**Primera versión, simple** (estilo y energía):
```
Calm, warm acoustic instrumental, slow tempo, gentle and contemplative
```

**Versión con detalle** (se añade en orden: estilo → elementos → voz):
```
Calm, warm acoustic instrumental, slow tempo, gentle and contemplative. Soft fingerpicked nylon guitar, light upright bass, brushed drums with very low energy, a faint warm synth pad underneath. Instrumental only, no vocals.
```
Ajustes: 20 s, solo instrumental activado, 3 variaciones.

**Si la música no encaja**, dile a Amenábar qué oyes:
```text
La batería es demasiado presente y compite con los efectos. Es el prompt de la música de la secuencia.
```
Siguiente intento: cambiar solo «brushed drums with very low energy» por «no drums, only a soft percussion shaker» y anotar el resultado.

**Si algún día lleva voz con letra:** la letra va en un bloque **separado, al final**, con secciones simples (verso, estribillo), para que el modelo distinga lo que se canta de lo que describe la música. No es de este ejercicio.

## Comprobación del profesor (solo texto)

- [ ] Una sola pieza, instrumental, sin voz ni letra.
- [ ] El prompt describe cómo suena (estilo, elementos), no la historia del plano.
- [ ] Se añadió el detalle en orden: estilo, elementos, voz.
- [ ] Duración e instrumental indicados aparte.
- [ ] Hay decisión de mezcla por escrito (entrada, nivel, sonido original).
- [ ] No más de 3 intentos, con un solo cambio entre intentos.
- [ ] No se usó música de terceros como recurso.
- [ ] La tabla de créditos está completa.

Es una comprobación del texto y de lo entregado; no valida la calidad musical.

## Después

`EX03c_DIALOGO_LIPSYNC.md`, o al plan de montaje (`edit-plan`) y al módulo 5, donde se ajusta la mezcla.
