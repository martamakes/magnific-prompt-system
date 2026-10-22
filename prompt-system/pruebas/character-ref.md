# Pruebas de character-ref (v2)

**Qué son:** aplicaciones escritas de la skill a entradas de prueba, hechas por quien la redactó; no son ejecuciones independientes ni prueban nada en un modelo de imagen. **Comportamiento textual** (¿pregunta cuando toca y respeta versiones?) y **resultado visual** (¿el modelo conserva los rasgos?) van separados: lo primero se ha ejecutado por escrito; lo segundo está pendiente en todos los casos.

---

## A. Creación con detalles delegados — ejecutada (texto)

**Entrada:** «Una mujer adulta con pelo corto y ropa de mecánica; el resto a tu criterio. Retrato para planos cercanos.»

**Esperado:** no hace preguntas; desarrolla lo delegado; entrega el prompt; no presupone fotorealismo.

**Salida:**

```
Retrato de una mujer adulta de unos treinta y cinco años, de hombros hacia arriba, mirando a cámara con expresión neutra y atenta. Rostro de mandíbula marcada, ojos castaños, cejas rectas y definidas, nariz recta, labios de grosor medio, piel de tono medio con ligero bronceado. Cabello negro y corto, a la altura de la mandíbula, ligeramente despeinado. Viste un mono de trabajo azul marino con cuello abierto y una mancha de grasa discreta en el hombro izquierdo. Fondo neutro uniforme y luz suave y pareja.
```

Nota (una línea): no se ha fijado estilo visual; añade el tuyo si lo tienes.

*Para revisar si quieres (propuestas):* edad, color de cabello, mancha de grasa, expresión, fondo neutro.

---

## B. Cambio explícito autorizado — ejecutada (texto)

**Premisa:** BASE: `PJ01-v1`, imagen aprobada y adjunta. Sus rasgos y su vestuario se toman de esa imagen. No se describe ningún rasgo que no conste en ella (la versión anterior de esta prueba añadía pecas, lunar, cabello a los hombros y camiseta gris sin que figuraran en la base: corregido).

**Entrada:** «Mantén su rostro y hazla rubia con flequillo.»

**Esperado:** no repregunta; crea variante `PJ01-v2`.
- CAMBIO: cabello rubio y flequillo, nada más.
- PROTEGER: identidad facial, longitud del cabello salvo lo necesario para el flequillo, vestuario, encuadre, expresión, fondo e iluminación.
- Conserva v1; no abre CAMBIOS PENDIENTES por ser solo una variante.
- **Criterio de aprobación textual:** el prompt no introduce cambios adicionales ni rasgos distintivos que no consten en la base.

**Salida:**

Imagen a adjuntar: 1 (`PJ01-v1`). Aporta rostro, complexión, longitud de cabello, vestuario, encuadre, fondo y luz. Se ignora solo el color del cabello y su frente sin flequillo. Prevalece sobre el texto en todo salvo el CAMBIO.

```
Same portrait as the attached image (PJ01-v1), unchanged except for the hair. Change only the hair: it is now blonde and has a fringe across the forehead. Keep the hair length as in the attached image, except what the fringe requires. Keep exactly the same face, clothing, framing, expression, background and lighting as the attached image. Add no other change and no new distinguishing features.
```

RECURSOS: `PJ01-v2` (variante: cabello rubio con flequillo, `pedida`); `PJ01-v1` se conserva. Prompt v2 redactado · imagen no generada · aprobación pendiente.

**Comprobación textual contra el criterio:** el prompt solo cambia color y flequillo; no nombra pecas, lunar, longitud concreta ni prenda (todo se toma de la base). Limitación: «el tipo de flequillo» (recto, lateral) no lo dijo el usuario y queda sin fijar; no se decide por ella. → **cumple en texto**; que el modelo conserve la identidad: **no ejecutada**.

---

## C. Contradicción explícita — ejecutada (texto)

**Entrada:** «No cambies el cabello; hazla rubia.»

**Esperado:** pregunta antes de redactar; no elige por su cuenta.

**Salida (solo la pregunta):** «Esas dos instrucciones se contradicen. ¿Conservo el cabello actual o lo cambio a rubio (variante nueva)? ¿O querías rubio en alguna parte concreta (mechas, puntas)?»

---

## Pendientes (no ejecutados)

- **D. Dos imágenes ambiguas:** adjuntar dos referencias con rostro visible en ambas y pedir «combínalas». Esperado: pregunta qué aporta cada una, qué se ignora y cuál prevalece, y no redacta hasta saberlo. Si el usuario ya lo indicó, no repregunta.
- **Visual:** comprobar en un modelo, con imágenes reales, que A conserva lo descrito, que B mantiene el rostro de v1 al cambiar el cabello y que el fondo neutro funciona como referencia reutilizable. No se ha hecho ninguna inspección visual.
