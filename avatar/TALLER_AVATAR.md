# Taller: crear un presentador de IA que habla a cámara, con las herramientas de Magnific

Parte del vídeo «El sistema que llevó mi avatar IA a 100K vistas» (Lorena Bordonaba, YouTube, 32 min, https://www.youtube.com/watch?v=LEvGpuxRLuk), leído por sus subtítulos automáticos. El vídeo usa HeyGen + ElevenLabs. Este taller lo **adapta a Magnific** (imagen, vídeo, voz con ElevenLabs integrado) y deja HeyGen como ruta alternativa (parte 9).

**Cómo leer este documento**
- **[vídeo]** dato o consejo del vídeo. **[mío]** criterio propio, sin verificar.
- **[doc]** lo que consta en el Handbook de Magnific (v1.2) y los tutoriales de Magnific Academy según `prompt-system` (`documentada`). **Ninguno de los nombres de menú, botones, límites ni precios de Magnific se ha comprobado en tu cuenta** (no tengo acceso a la app desde aquí). Cada paso lleva «Comprueba» donde hay que validar algo.
- Prompts pegables en inglés; las explicaciones en tu idioma (`REGLAS.md` §9). El texto que se oye va en su idioma original.

## 0. Qué se construye y qué cambia respecto al vídeo

**Resultado:** un presentador (ficticio, o real con su permiso) con identidad estable que dice un guion corto a cámara, con una voz elegida, montado en un vídeo.

**Diferencia clave [mío, a confirmar]:** HeyGen crea un *avatar persistente*: subes imágenes o un vídeo, y luego generas vídeos largos con solo escribir o subir el audio. Magnific no tiene, hasta donde consta en las skills, una herramienta equivalente de avatar persistente. Aquí el «avatar» es:

> **una hoja de personaje aprobada** (identidad) + **una imagen inicial de habla** (estado antes de hablar) + **clips cortos con voz** (el modelo de vídeo con audio nativo, o la voz de la app aplicada a un clip) + **montaje**.

Consecuencias:
- Las piezas son **clips de segundos**, no un vídeo de 10 minutos de un tirón. Un monólogo largo se corta en tramos (parte 6).
- La identidad se mantiene con referencias y anclas; es el punto débil: se vigila en cada clip.
- La ventaja: control total del aspecto, del encuadre y de la cámara, y todo dentro de una sola herramienta.

**Cuándo elegir cada ruta**

| Necesitas… | Ruta |
|---|---|
| Piezas cortas (15–60 s): intros, anuncios, respuestas breves, redes | **Magnific** (partes 1–8) |
| Monólogos largos y frecuentes con el mismo presentador | **HeyGen** (parte 9) o Magnific + mucho montaje |
| Un presentador dentro de una producción audiovisual con más personajes y localizaciones | **Magnific** (es el flujo del curso) |

## 1. Decisiones previas (hazlas por escrito antes de generar nada)

| Decisión | Opciones | Tu elección |
|---|---|---|
| Real o ficticio | **Real:** conecta más; útil para un CEO o fundador estable **[vídeo]**. **Ficticio:** funciona igual y puede identificarse mejor con la audiencia **[vídeo]** | |
| Permisos | Real: **permiso por escrito** de la persona, incluida su voz. Voz clonada: permiso de la persona de la que procede **[mío]** | |
| Formato | 9:16 (redes) / 16:9 (YouTube) / 1:1 | |
| `Audio:` del proyecto | `audio en Magnific` (voz generada en la app) o `audio externo` (voz grabada o hecha fuera) | |
| Idioma de la voz | | |
| Duración final | 30–60 s para el taller | |
| Guion | Texto exacto, aprobado antes de generar (parte 3) | |

**Regla de oro [vídeo]:** la voz pesa más que la imagen. Un vídeo con voz creíble y aspecto algo imperfecto parece más real que uno perfecto y artificial.

**No uses avatares públicos de una librería [vídeo]:** los puede usar cualquiera y no construyes reconocimiento.

## 2. Parte 1 — La hoja de personaje (identidad)

Objetivo: tener **un solo personaje, aprobado**, con las referencias que mantendrán su cara en todos los clips. Es el `character-ref` del curso.

### Paso 2.1 — Busca el arquetipo en una fuente visual **[vídeo, 03:17]**
Pinterest (o similar). Busca cómo se imagina la gente a tu perfil («profesora de matemáticas», «atención al cliente joven en una startup») y rompe el estereotipo si quieres. Elige **una** imagen de referencia, solo para vestimenta, estilo, ambiente y luz.
- **Comprueba:** tienes derecho a usar esa imagen como referencia, que no es una persona identificable cuyo parecido quieras copiar **[mío]**. Una imagen de referencia **de estilo** no debe ser el rostro de alguien real.

### Paso 2.2 — Descríbela con precisión (para tener un prompt, no solo una imagen)
Pega la imagen a una IA de texto (puede ser Amenábar con la imagen adjunta, o Claude) y pide:
```text
Describe the woman in this image with high precision, as a prompting specialist: clothing, style, hairstyle, camera angle, lighting, shadows, background, colour palette. Do not describe her face in a way that identifies her.
```
**Salida:** una descripción que será la base de tu prompt. Guárdala en tu nota.

### Paso 2.3 — Genera el retrato base (Nano Banana en Magnific)
Con la descripción, genera una persona **nueva**: misma vestimenta y estilo, rostro distinto. Pídela **mirando de frente** para que los rasgos queden claros (se verán en todos los clips).
```text
A young woman of about 30, brown shoulder-length hair, oversized grey hoodie, sitting at a desk in a small startup office. Medium close-up, facing the camera, relaxed neutral expression, mouth closed. Soft window light from the left. Natural skin texture with visible pores, minor asymmetry.
```
- **Genera 2–4 variantes** y elige una. Un cambio por intento si quieres retocar.
- **Comprueba:** rostro sin deformaciones, manos fuera de plano o claras, una sola persona, sin texto ni logotipos inventados.
- **Estado:** `imagen generada` → pasa a `aprobada` cuando tú lo confirmes.

### Paso 2.4 — «Empeora» la imagen para que parezca real **[vídeo, 08:12]**
Cuanto más perfecta, más sintética (piel lisa, ojos brillantes). La técnica del vídeo:
1. Busca una **foto de un setup real y un poco mala** (oficina, habitación, luz dura, cámara de móvil).
2. Pide que el personaje aparezca dentro de ese setup y **absorba sus defectos**.

En Nano Banana, con las dos imágenes adjuntas y sus roles claros **[mío]**:
```text
Image 1 is the woman: keep her face, hair and clothing exactly. Image 2 is the real workspace: use it for the room, the desk, the lighting and the photographic style. Place the woman from image 1 sitting in the workspace of image 2, as if she were recording a video there. Transfer the photographic imperfections of image 2 to her: grain, harsh lighting, slightly dull colours, mild noise. Keep her facing the camera.
```
- **Comprueba:** la cara sigue siendo la del paso 2.3 (si derivó, repite con menos instrucciones); el setup se parece al de la foto real; el aspecto es menos «de estudio».
- **Retoques sencillos, de uno en uno [vídeo]:** «remove the headphones», «remove the logo on the hoodie».
- **Marcas de agua [vídeo]:** las imágenes gratuitas de Gemini las llevan; si tu herramienta añade alguna, mira sus condiciones antes de quitarla **[mío]**.

### Paso 2.5 — Hoja de variaciones (el material de referencia) **[vídeo, 06:00]**
Cuantas más imágenes variadas del mismo personaje y setup, mejor se sostiene la identidad. El vídeo pide **mínimo 4, ideal 10**: hablando, gesticulando distinto, mirando al ordenador, etc.

Con Magnific tienes dos vías:
- **Con Nano Banana:** una imagen por variante, usando la imagen aprobada como referencia de identidad.
- **Con Variations (modo Character) [doc, `PLATAFORMAS.md`]:** genera varias vistas desde una imagen. Úsalo para explorar; las que elijas pasan a `aprobada` una a una.

Variantes mínimas:

| # | Variante | Prompt (añade a la descripción del personaje) |
|---|---|---|
| 1 | Frente, boca cerrada (estado inicial de habla) | `facing the camera, mouth closed, calm` |
| 2 | Hablando | `facing the camera, mid-sentence, mouth slightly open, lively expression` |
| 3 | Gesticulando con la mano | `facing the camera, explaining something with her right hand raised, relaxed` |
| 4 | Mirando a la pantalla | `looking down at the laptop screen on her desk, eyes on the screen` |
| 5 | Ligero giro de cabeza | `head turned slightly to the right, looking off camera` |
| 6–10 | (opcional) otro encuadre, otro setup | |

Pide cada una **sobre la imagen aprobada** como referencia de identidad: «same woman, same clothing, same setup».
- **Comprueba:** en las 10, mismo rostro, mismo pelo, misma ropa, mismo fondo (o el fondo alternativo previsto).
- Descarta las que cambian de cara. No arregles con otro prompt una variante que ya ha derivado: genera otra.

### Entrega de la parte 1
- Imagen de referencia y su descripción.
- Retrato aprobado y versión «en setup real» aprobada.
- 4–10 variantes aprobadas.
- Ficha del personaje: nombre, rasgos que NO cambian (anclas: pelo, ropa, accesorios, marcas), y rasgos que la imagen no enseña, si los hay.

## 3. Parte 2 — Guion y voz

### Paso 3.1 — Escribe el guion exacto
- Corto: 30–60 s ≈ 75–150 palabras en español **[mío; ritmo medio de habla de 2,5 palabras por segundo, a comprobar con tu voz]**.
- Una idea, frases cortas, con pausas naturales.
- **Aprobado por ti antes de generar nada.** Una vez en la herramienta, no se cambia a mitad sin repetir los clips afectados.
- Divídelo en **tramos de 4–8 s** (una o dos frases) **[mío]**: cada tramo será un clip (parte 6).

### Paso 3.2 — Elige la voz **[vídeo, 11:06]**
La voz lo es todo. **Las mejores voces suenan grabadas: no perfectas, con algún ruido, algún golpe de micro**, sobre todo en un avatar ficticio.

Opciones, de menos a más trabajo:

| Opción | Cómo | Cuándo |
|---|---|---|
| **A. Catálogo de la herramienta de voz de Magnific** (Speak, con ElevenLabs integrado [doc]) | Escucha varias voces con tu texto y elige | La más rápida; ideal para el taller |
| **B. Voz diseñada** | Describirla con un prompt, si la herramienta lo permite [vídeo lo muestra en HeyGen/ElevenLabs] | Voz propia sin grabar a nadie |
| **C. Voz clonada** | ~10 s de audio de la persona real [vídeo, ElevenLabs instantánea] | Presentador real, **con permiso**; clonar solo la voz de quien lo autoriza |
| **D. Audio propio** | Grabas el guion y subes la pista [vídeo: la autora lo hace en todos sus vídeos] | Máxima veracidad |

- **Comprueba (Magnific):** qué opciones de voz tiene tu cuenta (catálogo, clonar, diseñar, subir audio), y su coste en créditos. Los nombres del menú: pendiente de verificar.
- **Grabar tu propia pista [vídeo]:** habla como lo harías a cámara, con distintos tonos y pausas naturales. No hace falta un estudio; que no suene a locución.
- **Interpretación (aparte del texto) [doc, `audio-prompt`]:** una sola por voz, por ejemplo: `warm, steady, slightly informal, unhurried`.
- **Aprueba la voz** con 1–2 frases de prueba antes de gastar en vídeo.

### Entrega de la parte 2
- Guion exacto, dividido en tramos con la duración estimada de cada uno.
- Voz elegida (opción A–D) y por qué; la interpretación.
- Permiso por escrito, si es una persona real.

## 4. Parte 3 — Dos formas de hacer que hable (elige una por pieza)

Marca la que uses en el campo `Audio:`.

| | **Vía A. Audio nativo en el vídeo** | **Vía B. Voz sobre un clip ya generado** |
|---|---|---|
| Qué es | El prompt de **vídeo** lleva el texto exacto y el modelo genera voz y labios | Genera el clip **sin audio** y aplicas la voz con la herramienta de voz de la app [doc] |
| Voz | La decide el modelo (menos control) | La eliges tú del catálogo (más control) |
| Modelo | Seedance 2.5: el catálogo cita audio nativo y lipsync, **detalle de diálogo pendiente de verificar**. Seedance 2.0: no consta [`MODELOS.md`] | El de la tarea; la voz se aplica después |
| Riesgo y gasto | Alto (si falla, se repite todo el clip) | Medio (si falla la voz, se repite solo la voz) |
| Cuándo | Para probar rápido una pieza corta | Cuando quieres elegir la voz y controlar el texto |

**Recomendación del taller [mío]:** empieza por la **vía B**. Separa los problemas: primero el clip (rostro y gestos), luego la voz. Prueba la vía A en un clip corto para ver si tu modelo la hace bien, y anótalo.

**Mira el coste antes de ejecutar.** Pasos de calidad: **borrador/480p, 2 generaciones, elegir una y pasarla a alta** (regla de `EX02_ANIMACION.md`).

## 5. Parte 4 — Imagen inicial de habla y primer clip (un solo tramo)

### Paso 5.1 — Imagen inicial del tramo
Es la variante 1 (frente, **boca cerrada, relajada**), o la que corresponda al primer tramo. «Boca abierta» no equivale a «hablando»: se especifica.
- **Comprueba (puerta):** la imagen inicial está `aprobada`. Sin imagen aprobada no se pide vídeo.

### Paso 5.2 — Prompt de vídeo, vía B (el clip sin audio)
Describe solo lo que **cambia**: gestos y cámara. No redescribes a la mujer ni la sala.
```text
Fixed camera, medium close-up. 00:00 The woman looks into the camera and starts speaking, with natural head movement and small hand gestures. 00:03 She nods slightly, then keeps looking at the camera. The window light stays constant. No music. No subtitles.
```
- **Ajustes:** duración 5–6 s, formato de tu decisión (parte 1), **borrador/480p**, 2 generaciones.
- **Mira los dos clips enteros** y elige. Comprueba:
  - la cara se mantiene en todo el clip,
  - las manos no se deforman,
  - la boca no se queda abierta sin hablar,
  - el parpadeo es natural,
  - la cámara no se mueve.
- **Si falla:** `repair`. Dile **segundo y elemento** («a los 3 s la mano derecha tiene seis dedos»). Un cambio por intento, máximo 3 borradores.

### Paso 5.3 — Aplica la voz (vía B)
En la herramienta de voz de Magnific [doc]:
1. Sube el clip aprobado en borrador (o el de alta, si ya lo tienes).
2. Pega el texto exacto del tramo, en bloque propio:
```text
"Hola, soy tu asistente de atención al cliente. Hoy te cuento cómo resolver tu primera consulta en tres pasos."
```
3. Elige la voz del catálogo y escribe la interpretación aparte: `warm, steady, slightly informal`.
4. Duración: **el habla debe caber en la duración del clip**, o usa la extensión automática, que adapta el vídeo al habla [doc, dato del tutorial de Speak; sin comprobar en tu cuenta].
5. Genera y escucha **con el clip puesto**.

**Comprueba:**
- los labios coinciden con el texto (sin retraso),
- ninguna palabra distinta de las aprobadas, ni risas ni gritos,
- la entonación no cambia el sentido,
- la duración no cortó la frase.

### Paso 5.4 — O la vía A: diálogo dentro del prompt de vídeo (prueba corta)
Solo si tu modelo lo admite (Seedance 2.5, a verificar). Mismo prompt con el texto entre comillas:
```text
Fixed camera, medium close-up. 00:00 The woman looks into the camera. 00:01 She says "Hola, soy tu asistente de atención al cliente." in a warm, steady voice, then smiles slightly. The window light stays constant. No music. No subtitles.
```
- Una sola frase corta y 2 borradores. Anota si el modelo respeta el texto, los labios y la voz.
- **Apunta el resultado en la nota «verificado / pendiente»** (sirve para `MODELOS.md`).

### Paso 5.5 — Pasa a alta el tramo elegido
Solo el clip aprobado. Después de subir a alta, vuelve a mirar el clip entero (puede salir algo distinto del borrador: pendiente de verificar si la app reutiliza o regenera).

## 6. Parte 5 — Más de un tramo: el guion completo

Magnific produce clips cortos. Para 30–60 s, encadenas 5–10 tramos.

### Paso 6.1 — Tabla de tramos
| Tramo | Texto | Duración | Imagen inicial | Gesto | Cámara |
|---|---|---|---|---|---|
| T01 | frase 1–2 | 5 s | variante 1 | habla frontal | fija |
| T02 | frase 3 | 4 s | variante 3 | gesto con la mano | fija |
| T03 | frase 4 | 4 s | variante 4 | mira la pantalla | fija |
| … | | | | | |

**Cambiar el gesto y la variante entre tramos** hace el ritmo más natural y esconde los cortes **[mío]**.

### Paso 6.2 — Continuidad entre tramos
- **Mismo personaje, mismo setup, misma luz** en todos (anclas de la ficha).
- Un tramo que continúa otro puede partir del **fotograma final aprobado** del anterior (continuidad de `shot-composer`).
- **Anclas [vídeo, Tao Prompts]:** si el modelo pierde un rasgo, repítelo en una frase: `she keeps the grey hoodie and the dark-framed glasses`. Una frase de apoyo, no una redescripción.
- Evita multitudes animadas: hipótesis del mismo tutorial, sin verificar. Un solo personaje que habla.

### Paso 6.3 — Ritmo y cortes
- Cortes secos entre tramos (jump cut) son normales en un presentador de redes.
- Intercala **planos de recurso** (la pantalla, un objeto, texto en el editor) para esconder un tramo que no salió bien **[mío]**.
- Todo el texto en pantalla, rótulos y subtítulos, va en el editor, nunca dentro del prompt.

### Paso 6.4 — Producción en orden
1. Primero **un** tramo completo (imagen → clip → voz). Cuando funcione, haz el resto.
2. Registra créditos por tramo.
3. Cuando un tramo falla 3 veces: simplifica o resuelve en el montaje (EX02b).

## 7. Parte 6 — Música, ambiente y mezcla

Todo opcional. Se trabaja con `EX03b`/`EX03a`.

- **Música:** instrumental, baja, que no compita con la voz (prompt con estilo, elementos y «no vocals»).
- **Ambiente suave:** sala silenciosa, tecleo ligero. Un solo ambiente, en bucle.
- **Mezcla [doc/`edit-plan`]:** la voz manda; la música por debajo; decide qué pasa con el sonido original del clip (conservar, bajar o sustituir).
- **Subtítulos:** en el editor. Gran parte de la audiencia ve sin sonido.

## 8. Parte 7 — Montaje y entrega

1. **Plan de montaje (`edit-plan`):** orden de tramos, uniones, planos de recurso, música, texto en pantalla y duración total.
2. **Montaje en DaVinci Resolve** (módulo 5) o CapCut **[vídeo usa CapCut]**.
3. **Exportación** en el formato decidido.
4. **Revisión final** con la lista de abajo.

### Lista de calidad de la pieza
- [ ] El rostro es el mismo en todos los tramos.
- [ ] Las manos no se deforman en ningún fotograma.
- [ ] La boca se mueve solo cuando hay voz.
- [ ] Los labios coinciden con el texto y las palabras son las aprobadas.
- [ ] La voz no tiene saltos de volumen ni cortes de frase entre tramos.
- [ ] No hay marcas de agua ni logotipos inventados.
- [ ] El texto en pantalla y los subtítulos están en el editor.
- [ ] La música no compite con la voz.
- [ ] Hay permiso del personaje real y de la voz clonada, si procede.

## 9. Ruta alternativa: HeyGen (la del vídeo)

Para piezas largas y repetidas con el mismo presentador. Resumen exhaustivo del vídeo.

### 9.1 Avatar ficticio [vídeo, 03:17–10:06]
Se usan las **partes 1 y 2 de este taller** (referencia, retrato, setup real, 4–10 variaciones). Después en HeyGen:
1. Inicia sesión (Google). Plan gratuito para seguir el taller; el plan «creador» del vídeo ≈ 25 €/mes (≈ 20 € con descuento) [vídeo; precios sin verificar].
2. **Avatares → Crear avatar** (arriba a la derecha).
3. Sube las imágenes (mínimo 4, ideal 10; puedes añadir otros fondos de la misma persona).
4. Nombre, edad y género.
5. Pasa a la voz (9.3).

### 9.2 Avatar de una persona real [vídeo, 15:46–17:54]
1. Verifica que la persona está delante: hay que **verificar su identidad**.
2. **No grabes en la propia herramienta** si quieres un fondo real: sube un vídeo grabado antes, en el setup definitivo.
3. **Vídeo de entrada:** HeyGen dice que bastan 15 s; la autora usó 4–6 min. La calidad del input fija la del avatar.
4. **Hablando a cámara y con gestos:** mirar al ordenador, parpadear, tocarse el pelo. Si solo hablas a cámara, el avatar solo moverá la boca.
5. Avatares → Crear avatar real → **Upload** (archivo o Google Drive) → nombre.
6. Revisa los avatares alrededor que genera; la autora los eliminó porque cambiaban ropa y fondo.
7. **Verificación:** pulsa el icono de verificación del vídeo, mira a la cámara y lee el texto. Hasta entonces no se puede usar.

### 9.3 La voz en HeyGen [vídeo, 11:06–15:46]
- Librería de voces (escúchalas y elige), diseñar una voz con un prompt, o clonar la tuya dentro de HeyGen.
- **ElevenLabs conectado a HeyGen:** en ElevenLabs, Voces → Crear una voz → clonación instantánea con ~10 s hablando con distintos tonos → nombre e idioma. En HeyGen: Developers → API Key → Crear key → pégala donde pide la conexión.
- **Audio propio:** la autora graba el guion hablando 5–10 min y sube la pista: más veracidad.
- Los proveedores de voz que ofrece HeyGen son ElevenLabs y otro modelo propio; la voz se puede cambiar después.

### 9.4 Generar el vídeo [vídeo, 17:54–20:07]
1. **Usar en vídeo** (flecha arriba).
2. **Build scene by scene** (funcionó mejor que dejarle un guion libre).
3. Sube **texto** (con voz clonada) o tu **audio** (se transcribe solo).
4. Generar.

Compara tres: avatar con voz clonada, avatar con tu voz real, vídeo original.

## 10. Parte 8 (opcional) — Publicación y posicionamiento [vídeo, 20:07–29:06]

No es parte de la creación del presentador.
- **Ideas:** extensiones vidIQ y 1of10 (vídeos que rinden por encima de la media del canal). Inspiración, no copia.
- **Perfil limpio de YouTube** (una cuenta solo para el tema).
- **Guion:** transcripción de un vídeo que haya funcionado → a una IA (Claude) para una estructura propia, no una traducción.
- **Títulos:** vidIQ conectado a Claude por MCP.
- **Producción:** edición sencilla y subida.
- Resultados que cuenta la autora: el canal creció igual y el algoritmo no penalizó al avatar [vídeo; experiencia propia, sin comprobar]. También dice que, si tu trabajo es crear contenido, ser tú conecta más.

## 11. Registro de créditos

| Tramo | Borradores | Pasos a alta | Voz (intentos) | Créditos gastados | Saldo |
|---|---|---|---|---|---|

## 12. Comprobación del profesor (solo texto)

- [ ] Real o ficticio decidido y por escrito; permisos si es real o voz clonada.
- [ ] Hay una referencia, un retrato aprobado, un setup real y 4–10 variantes aprobadas.
- [ ] La imagen no es «perfecta»: grano, luz de setup real o defectos pedidos.
- [ ] Ficha de personaje con anclas.
- [ ] Guion exacto, aprobado y dividido en tramos con duración.
- [ ] Voz elegida y aprobada con una frase de prueba.
- [ ] Vía A o B elegida por pieza y `Audio:` coincide.
- [ ] El prompt del clip describe solo gestos y cámara, no redescribe lo que ya está en la imagen.
- [ ] Imagen inicial con boca cerrada, no con «boca abierta».
- [ ] Se probó en borrador/480p con 2 generaciones y solo el elegido pasó a alta.
- [ ] Los fallos indican segundo y elemento; un cambio por intento; máximo 3.
- [ ] Texto, subtítulos y rótulos están fuera de los prompts.
- [ ] Hay registro de créditos y de lo que salió distinto.
- [ ] Hay una nota «verificado / pendiente» con lo que Magnific hizo en la prueba.

## 13. Pendiente de verificar antes de dar la clase

- [ ] **Herramienta de voz de Magnific:** nombre exacto en el menú, voces disponibles, si hay clonación o diseño de voz, subida de audio propio, y límites de duración.
- [ ] **Voz sobre un clip:** el modo de extensión «auto», y si respeta el texto palabra por palabra.
- [ ] **Audio nativo con diálogo** en tu modelo de vídeo (Seedance 2.5 y 2.0): calidad de labios, voz y respeto del texto.
- [ ] **Variations (modo Character):** número de variantes, cómo mantiene la identidad.
- [ ] **Coste en créditos** de cada paso (retrato, variante, clip borrador, clip alta, voz).
- [ ] **Subir a alta:** si reutiliza o regenera el clip.
- [ ] **Duración máxima de un clip** con el modelo de la tarea (`MODELOS.md`).
- [ ] **Marcas de agua** y condiciones de uso comercial de lo que se genera.
- [ ] **Si Magnific ofrece un avatar persistente:** en tal caso, esta ruta se simplifica (revisa la documentación oficial o el MCP de Magnific).
- [ ] **HeyGen y ElevenLabs:** precios, planes y condiciones sobre avatares reales y voces clonadas (los del vídeo pueden haber cambiado).
- [ ] **Normas de la plataforma** donde publiques sobre etiquetar contenido sintético.
