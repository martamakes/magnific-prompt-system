# EX03c_DIALOGO_LIPSYNC — diálogo y sincronía labial

Tercer ejercicio de audio, el de más riesgo y más gasto. Se hace **después de `EX03_AUDIO.md`**; conviene haber hecho antes EX03a. Objetivo: que un personaje diga una frase corta con la boca sincronizada.

**Es el único ejercicio donde alguien habla.** En EX00–EX02 el diálogo y el lip sync estaban prohibidos.

## Límites (obligatorios)

| Qué | Límite |
|---|---|
| Personajes que hablan | **1** |
| Frases | **1**, corta (**una oración**) |
| Clip | **1**, con la imagen inicial aprobada del personaje |
| Texto | **exacto y aprobado por ti antes** de generar; nadie añade palabras, risas ni gritos |
| Voz | la eliges tú en el catálogo de la herramienta; **no se clona** ninguna voz |
| Duración | la frase cabe en la del plano (**4–6 s** orientativo, `propuesta`) |
| Intentos | **máximo 3** por vía |
| Voces de terceros | **ninguna** |

Dos personajes, más de una frase, voz clonada o texto cambiado a mitad = ejercicio no válido.

## Las dos vías

Elige **una** y registra por qué. Se puede probar la otra solo si sobra saldo.

| Vía | Cómo funciona | Cuándo conviene | Estado |
|---|---|---|---|
| **A. Dentro del prompt de vídeo** (audio nativo) | El prompt de vídeo lleva el diálogo y el modelo genera voz y labios | Si el modelo lo admite y quieres un solo paso | Seedance 2.0: diálogo y lipsync **pendientes de verificar**; Seedance 2.5: el catálogo cita «audio nativo y lipsync», detalle pendiente (`MODELOS.md`). Se prueba con un clip corto y se anota |
| **B. Después, sobre un clip ya generado** | Con la herramienta de voz de la app (Speak): voz a partir de texto o de un audio subido, aplicada al clip | Si quieres elegir la voz y controlar mejor el texto | `documentada` en tutorial de Magnific; sin comprobar con tu cuenta. Con extensión «auto» la app adapta el vídeo al habla (dato de tutorial) |

Con la vía B, el prompt de voz lo redacta `audio-prompt`; con la A, `video-prompt`.

## Qué haces

1. **Decide el campo `Audio:`** del proyecto: `audio en Magnific` para la vía A o la B dentro de la app; `audio externo` si la voz la haces fuera.
2. **Escribe la frase y apruébala.** En su idioma original, en bloque propio, sin añadidos. Cuenta cuánto tarda en decirse y comprueba que cabe en el plano.
3. **Elige una vía** y anota el motivo.
4. **Imagen inicial del personaje** hablando-a-punto-de-hablar: boca cerrada o relajada, mirada definida. «Boca abierta» no equivale a hablar: se especifica.
5. **Redacta el prompt** (`video-prompt` para la A, `audio-prompt` para la B).
6. **Genera, escucha y mira los labios.** Mira el coste antes de ejecutar. Si falla, dile a `repair` **a qué segundo y qué falla** (labios desfasados, voz que no coincide, palabra distinta, rostro que deriva). Un cambio por intento.
7. **Decide:** repetir, cambiar de vía o resolver en el montaje (sustituir la voz o cortar antes del fallo).

## Qué entregas

- La frase aprobada y su duración estimada.
- La vía elegida y el motivo.
- La imagen inicial aprobada y el clip (o el clip más la voz).
- El prompt, con la voz y la interpretación (tono, ritmo) por separado.
- El registro de intentos: qué falló (segundo y elemento), qué cambiaste, qué resultó.
- Tabla de créditos: intentos y créditos gastados.
- Una nota: **qué consta ya como verificado** (¿el modelo hace lipsync? ¿con qué calidad?) y qué sigue pendiente. Esa nota sirve para actualizar `MODELOS.md`.

## Ejemplo de prompting

*Ilustrativo, con el caso de la ceramista de EX00–EX02. No probado en la app. El texto del diálogo conserva su idioma; el resto del prompt va en inglés.*

**Reglas de forma:** el texto exacto en bloque propio y entre comillas; la interpretación aparte, una por voz. Describe la acción corporal, la expresión y la voz por separado.

**La frase aprobada** (en español, su idioma original):
```
"Esta taza la hice yo."
```
Duración estimada: 2 s al ritmo normal. Cabe en un plano de 5 s.

**Vía A — dentro del prompt de vídeo** (solo si el modelo lo admite; si no consta, se prueba en corto):
```
Fixed camera. 00:00 The woman looks at the camera, mouth closed, calm. 00:01 She says "Esta taza la hice yo." in a warm, steady voice, then smiles slightly. The window light stays constant. No music. No subtitles.
```
Ajustes: 5 s, 16:9. Referencia: imagen inicial aprobada del personaje.

**Vía B — voz sobre el clip ya generado** (prompt de voz para `audio-prompt`):
```
"Esta taza la hice yo."
```
Interpretación (aparte, una por voz): warm, steady, unhurried, slight smile at the end. Voz: la que elijas del catálogo. Ajustes: duración ≤ la del plano; modo de ajuste del vídeo al habla según la herramienta (pendiente de verificar).

**Mal y bien:**

| Mal | Bien |
|---|---|
| *She talks about how proud she is of her work* (cuenta la intención; el modelo inventa las palabras) | *She says "Esta taza la hice yo."* (texto exacto) |
| *Mouth open* (puede ser grito, risa, sorpresa) | *Mouth closed, calm, then speaks* |

**Si falla**, dile a Amenábar el segundo y el elemento:
```text
En E01-P02, a los 2 segundos los labios se mueven pero la voz va medio segundo por detrás. Es la vía B.
```
Un solo cambio en el siguiente intento, por ejemplo acortar la frase o pedir el ajuste automático de duración. Si tras 3 intentos no encaja, se decide por escrito: cambiar de vía, cubrir con otro plano o doblar en el montaje.

## Comprobación del profesor (solo texto)

- [ ] Un personaje, una frase, un clip.
- [ ] El texto está aprobado antes de generar y es exacto en todos los prompts.
- [ ] La vía elegida está justificada y el campo `Audio:` coincide.
- [ ] La interpretación va aparte del texto y no añade palabras, risas ni gritos.
- [ ] La imagen inicial es del estado previo a hablar (boca cerrada o relajada).
- [ ] No hay voz clonada ni de terceros.
- [ ] No más de 3 intentos por vía, con un solo cambio entre intentos.
- [ ] La nota separa lo verificado de lo pendiente.
- [ ] La tabla de créditos está completa.

Es una comprobación del texto y de lo entregado; no valida la calidad de la voz ni de los labios.

## Después

Con los sonidos aprobados, se pasa al plan de montaje (`edit-plan`: orden, uniones, niveles y solapes entre diálogo, música y efectos) y al módulo 5 (DaVinci Resolve).
