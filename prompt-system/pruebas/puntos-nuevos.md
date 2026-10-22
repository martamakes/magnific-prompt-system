# Pruebas de los puntos nuevos (2026-10-22)
**Qué son:** aplicaciones escritas y manuales de las skills, hechas por quien las redactó (no son ejecuciones independientes); no se ha visto imagen, vídeo ni audio, ni se ha generado nada. Comprueban el comportamiento textual. Salvo dato contrario, el caso es «La segunda taza» v0.5 y todo lo diseñado es `propuesta`. Las que necesitan imagen o clips reales están marcadas «no ejecutada».

Cubren: hoja de vestuario, dirección visual, criterio de corte, criterio de bloques, perfiles de modelo (`MODELOS.md`), selección de tramos (`edit-plan`), feedback de `repair` y `location-ref` sin letreros.

---

## H. Hoja de vestuario (`character-ref`)
**H1. Base aprobada.** Entrada: «Hoja de vestuario de M1» con REF-01 `aprobada`. Esperado: hereda la identidad de REF-01; vistas de la persona vestida, muestras de tejido, detalles, paleta; cada prenda con tipo, color, tejido y corte, lo no dicho como `propuesta`; inglés; sin inventar prendas.

Salida (prompt):
```
Costume sheet for the same woman as in the reference image, keeping her face, hair and build exactly. Layout on a plain neutral background with soft even light: three full-body views of her dressed (front, left profile, back); close-up fabric swatches of each garment; close-ups of the details that distinguish them; a row of colour swatches with the palette. Garments: a loose, soft mustard-yellow cotton cardigan with a relaxed fit and a round neckline; a plain cream cotton T-shirt; dark straight trousers; flat house shoes. Calm, neutral expression in every view. Everything matches the reference image.
```
Aparte: prendas, tejidos y corte son `propuesta` (el caso solo fija «prenda de casa, un color»); la referencia aporta la identidad.

**Resultado H1:** el prompt no lleva etiquetas; coincide con la skill tras corregir W1 (antes la skill las exigía y este prompt las omitía: el defecto quedaba oculto).

**H1-control 1 (por defecto, sin etiquetas).** Entrada: la de H1. Esperado: el prompt de H1 tal cual; las vistas se identifican por su disposición («three full-body views… front, left profile, back») y la explicación va fuera del prompt. Revisado: no hay títulos ni rótulos → **cumple (texto)**.

**H1-control 2 (el usuario las pide).** Entrada: «Hoja de vestuario de M1, con etiquetas en cada panel.» Esperado: la skill lo permite (petición explícita); añade al prompt una frase del tipo «Add a short label under each panel: “FRONT”, “LEFT PROFILE”, “BACK”, “FABRIC”, “COLOURS”», con el texto literal entre comillas, y avisa de que es texto dentro de la imagen y que puede salir con errores. Sin pedirlas, no se añaden. → **cumple (texto)**; si el modelo escribe bien las etiquetas: **no ejecutada**.

**Prenda con texto propio.** Entrada: «Hoja de vestuario con una camiseta que lleva estampada la palabra “NORD”.» Esperado: el estampado se conserva como parte de la prenda («cotton T-shirt with the word “NORD” printed on the chest»); la norma de no etiquetar no lo elimina. → **cumple (texto)**.

**H2. Base sin aprobar.** Entrada: «Hoja de vestuario de M1» con REF-01 en `propuesta`. Esperado: dice que la hoja parte de la base aprobada y entrega el prompt de la base (como en las variantes); no escribe la hoja.
Salida: «La hoja de vestuario parte de la hoja de vistas aprobada y REF-01 aún es `propuesta`. Te dejo el prompt de REF-01; cuando la apruebes, escribo la hoja.» → **cumple**.

**H3. Prenda con foto.** Entrada: foto de una chaqueta de M2 «solo la chaqueta». Esperado: declara qué aporta (corte, tejido, color de la chaqueta) y qué se ignora (persona, fondo, pose); no repregunta. → **cumple** (texto). Fidelidad visual: **no ejecutada**.

---

## V. Dirección visual (`brief`, `shot-composer`, `video-prompt`)
**V1. Pieza de varios planos.** Entrada: idea de la pieza de 3 planos. Esperado: pregunta la dirección visual en **una** línea.
Salida: «¿Tienes un look en mente (luz, color, óptica, textura), una imagen de referencia, o lo propongo yo? “Sin look definido” también vale.» → **cumple**.

**V2. Una sola imagen.** Entrada: «una imagen de una taza». Esperado: no pregunta (un solo plano no necesita coherencia entre planos). → **cumple**.

**V3. «Sin look definido».** Esperado: respuesta completa; no repregunta; el campo se omite o queda «sin look definido». → **cumple**.

**V4. Imagen de look.** Entrada: una foto de una película como look. Esperado: se registra `de referencia` y su papel es solo el aspecto (luz, color, tratamiento), no su contenido, personas ni lugar; el prompt de composición no copia su contenido. → **cumple** (texto). Que el modelo separe aspecto y contenido: **no ejecutada**.

**V5. Propagación.** Dirección visual «luz natural suave de ventana, paleta cálida desaturada, 35 mm» `propuesta`. Esperado: `shot-composer` lo aplica a los 3 planos sin redefinirlo; `video-prompt`, con imagen inicial, no lo redescribe. Comprobado en texto: P01–P03 llevan la misma frase de luz y de paleta; el prompt de vídeo de imagen a vídeo no la repite. → **cumple**.

---

## C. Criterio de corte (`breakdown` §A)
**C1. Nada cambia.** Entrada: «Una mujer toma café sentada junto a la ventana, 8 s, sin cambios de lugar ni de sujeto.» Esperado: un solo plano; no corta por cortar.
Salida: «Un plano de 8 s: no cambia el punto de vista, el sujeto ni el lugar. Si quieres un detalle de la taza, dímelo y lo añado con su motivo.» → **cumple**.

**C2. Cambia el sujeto.** Entrada: «Entra otra mujer y se sienta; la primera la mira.» Esperado: corte propuesto con motivo en «función narrativa»: cambia el sujeto de la atención. → **cumple** (es la lógica de P01→P02→P03 del caso).

**C3. Número de planos fijado.** Entrada: el caso, que impone 3 planos. Esperado: si un plano está cargado (P02), no añade un cuarto; ajusta dentro de los tres y lo dice. → **cumple**.

**C4. Cambio de lugar.** Entrada: «De la cocina al pasillo.» Esperado: abre otra escena (`E02`), no solo otro plano. → **cumple**.

---

## B. Criterio de bloques (`breakdown`, «Criterio de bloques»)
**B1. Modelo con máximo suficiente.** Caso: 15 s, 3 planos; perfil Seedance 2.0 (≤15 s, hasta 6 planos por clip). Esperado: la historia no pide agrupar y P02 es el plano más cargado → tres bloques independientes, y dice que un clip con tres planos cabe en el perfil pero no lo propone por ahorro; deja la elección.
Salida: «Tres bloques de 5 s (un plano cada uno). Un clip único con tres planos entraría en el máximo de 15 s del perfil, pero aquí no lo recomiendo: si P02 falla, se regenera todo. Si prefieres menos generaciones, es una opción.» → **cumple**.

**B2. Pieza de 25 s.** Perfil Seedance 2.0 (máx. 15). Esperado: divide donde haya menos coste de continuidad (pausa o corte previsto) y anota estado final y unión de cada bloque. → **cumple** (texto).

**B3. Sin perfil o máximo pendiente.** Modelo no listado. Esperado: propone por historia y carga, marca «máximo por comprobar» y no supone un número. → **cumple**.

**B4. Fragmentación innecesaria.** Un momento continuo de 6 s con el modelo en 15 s. Esperado: un bloque; no lo parte por prudencia. → **cumple**.

---

## M. Perfiles de modelo (`video-prompt`, `REGLAS` §5)
**M1. Vía incompatible.** Entrada: «Prompt de vídeo de P03 con la imagen inicial aprobada y las referencias REF-01 y REF-04», modelo Seedance 2.0. Esperado: avisa de que en el perfil el primer fotograma no se combina con referencias y pregunta qué vía quiere (imagen inicial sola, o referencias sin fotograma inicial); no escribe una mezcla imposible.
Salida: «Según el perfil, Seedance 2.0 no admite primer fotograma y referencias a la vez. ¿Imagen inicial sola (la identidad va en la imagen) o referencias sin imagen inicial?» → **cumple**. Que la app lo rechace de verdad: **pendiente de validar** (fuente: catálogo).

**M2. Plano más largo que el máximo.** Plano de 20 s, Seedance 2.0. Esperado: divide en tramos con estado final y lo dice. → **cumple**.

**M3. Modelo sin perfil.** Entrada: otro modelo. Esperado: no usa los números de Seedance; pregunta o deja la adaptación pendiente. → **cumple**.

**M4. Campo pendiente.** Entrada: «¿Puedo fijar la seed?». Esperado: «pendiente de verificar» (el catálogo no la menciona); no la da por válida. → **cumple**.

---

## S. Selección de tramos (`edit-plan`)
**S1. Dos intentos con segundos.** Entrada: «P02: v1 está bien de 0 a 2 s pero la silla falla; v2 está bien de 2 a 5 s». Esperado: tabla de tramos y comprobación de unión.

| Plano | Tramo | Intento | Segundos | Motivo |
|---|---|---|---|---|
| P02 | 1 | `E01-P02-v1` | 0–2 | gesto de M2 bien |
| P02 | 2 | `E01-P02-v2` | 2–5 | silla bien |

Unión v1→v2 en el segundo 2: antes de darla por buena, comprobar posición de M2 (de pie, junto a la silla en v1; ¿ya empezando a sentarse en v2?), mano, mirada y luz. No se puede asegurar sin ver los clips → pendiente. Descartados: ninguno. → **cumple**.

**S2. Sin segundos.** Entrada: «Usa lo mejor de cada intento». Esperado: no inventa tiempos; pide el segundo de cada tramo en una pregunta. → **cumple**.

**S3. Unión que no encaja.** Entrada: en v1 M2 mira a la izquierda y en v2 a la derecha en el punto de unión. Esperado: no une; propone otro punto de unión o pasa a `repair`. → **cumple**.

**S4. Un solo intento.** Esperado: no activa el apartado. → **cumple**.

---

## R. Feedback de `repair`
**R1. Falta el segundo.** Entrada: «La mano sale mal.» Esperado: una pregunta con frase de ejemplo; no diagnostica.
Salida: «¿En qué segundo y de quién? Por ejemplo: “a los 3 s, la mano derecha de M1 atraviesa la taza”.» → **cumple**.

**R2. Con segundo y elemento.** Entrada: «A los 3 s la mano derecha de M1 atraviesa la taza.» Esperado: diagnóstico observable; causa `propuesta`; un solo cambio.
Salida: «Falla: a los 3 s, la mano derecha de M1 y la taza 2 se solapan. Se protege el resto. Causa probable (`propuesta`): el prompt junta soltar la taza y retirar la mano en el mismo beat. Cambio único: separar en dos beats (0:03 soltar, 0:04 retirar la mano). Prompt corregido (`E01-P01-v2`) + REVISAR DESPUÉS: segundo 3–4, la mano.» → **cumple**. Si el cambio resuelve el fallo: **no ejecutada**.

**R3. Imagen.** Entrada: «En la imagen la taza está a la izquierda de la silla, abajo a la derecha.» Esperado: el elemento y su posición bastan; no pide segundo. → **cumple**.

**R4. Vídeo sin verlo.** Entrada: «No me gusta el vídeo». Esperado: no lo juzga; pide el qué y el cuándo. → **cumple**.

---

## L. `location-ref` sin letreros
**L-1.** Entrada: «Cocina con un cartel de neón que ponga “OPEN”.» Esperado: no escribe texto legible en el lugar; lo dice y ofrece una pared lisa en ese punto; el texto va al editor. Salida: «Sin letreros legibles: dejo la pared lisa en ese punto y el texto se añade en el editor de vídeo.» → **cumple**.

**L-2.** Entrada: cocina del caso. Esperado: ningún cartel, rotulación ni etiquetas. Revisado el prompt de REF-02 de `plan-referencias-y-audio.md`: no los lleva. → **cumple**.

---

## Cierre auditable
**Qué son estas pruebas:** aplicaciones escritas y manuales, hechas por quien redactó las skills; **no son ejecuciones independientes**. No se ha validado ningún resultado visual ni audiovisual.

- **W1 (resuelto en la skill).** Se quitaron las etiquetas obligatorias de la hoja de vestuario (`character-ref/SKILL.md`). Las dos comprobaciones de H1 (sin etiquetas por defecto; con ellas si se piden) y la de texto propio de una prenda están escritas arriba; **hay que repetirlas con cada cambio de la skill**.
- **Caso B de `character-ref.md`:** reescrito con base `PJ01-v1` explícita, CAMBIO, PROTEGER y criterio textual. Pendiente de tu revisión; no se da por aprobado.
- **Revisadas en texto, a contrastar por ti** con las entradas y salidas de este archivo: H, V, C, B, M, S, R, L. «Cumple» significa que el texto del caso coincide con lo esperado escrito antes; no que el sistema funcione.
- **Pendiente de ejecución:** S (clips reales), R2 en resultado, `edit-plan` D, todo lo visual.
- **M (perfiles):** los datos salen del catálogo; la validación en la app es tuya (opción A) y las restricciones de la app siguen pendientes en la operación concreta.
- **Datos del perfil:** dependen de tu validación de `MODELOS.md`.
- **`repair`:** una hipótesis no es una causa demostrada y un prompt corregido no es un resultado arreglado.
