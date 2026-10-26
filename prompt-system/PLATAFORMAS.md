# PLATAFORMAS — zonas seguras por destino

Perfil por destino para componer en vertical sin que la interfaz de la app tape lo importante. Las skills leen el perfil del **destino de la tarea** (`# PROYECTO`, «Destino y formato»); ninguna lleva un número propio. **No elige plataforma por el usuario.**

**Estado:** primer borrador, `documentada`. Fuente de todo: texto aportado por la usuaria (2026-10-22), sin cita ni enlace; no comprobado en las apps. Las plataformas cambian estos márgenes: el usuario los valida (superponiendo una plantilla en su editor) y, al validar, cambia la fuente a «app, fecha».

**Reglas de uso**
- Un valor sin fuente no cuenta. Destino no listado o dato ausente: `pendiente de verificar`; se pregunta, no se supone.
- Medidas para un vídeo de **1080×1920 px (9:16)**. Con otra resolución, son proporciones, no píxeles.
- Las medidas dicen qué debe quedar **libre** (sin rostro, sujeto, rótulo ni CTA), no qué debe llenarse.
- Los modelos de imagen y vídeo no respetan píxeles con precisión. Las skills lo piden como **encuadre** (sujeto en la franja central, aire arriba y abajo); el ajuste final se comprueba en el editor con una plantilla superpuesta. Criterio propio, sin verificar.
- No usar una sola plantilla para todos los destinos.

---

## Instagram Reels / Facebook Reels
| Campo | Valor | Fuente |
|---|---|---|
| Libre arriba | 220 px | texto de la usuaria, sin cita |
| Libre abajo | 420 px (sobre todo con contenido patrocinado o música) | ídem |
| Caja segura recomendada | 1010×1280 px, centrada | ídem |
| Consejo de la fuente | usar la zona segura de anuncios incluso en piezas orgánicas, por si se impulsan después | ídem |
| Izquierda / derecha | no indicado; la caja implica unos 35 px por lado | deducido de la caja (cálculo mío) |

## TikTok
| Campo | Valor | Fuente |
|---|---|---|
| Libre arriba | 108 px (búsqueda y navegación) | texto de la usuaria, sin cita |
| Libre abajo | 320 px (cuenta, subtítulos, botones) | ídem |
| Libre a la izquierda | 60 px | ídem |
| Libre a la derecha | 120 px (like, comentarios, compartir) | ídem |

## Meta Ads (anuncios)
Sin perfil propio: la fuente no lo separa. Hasta que el usuario lo valide, se trata como **Reels con zona de anuncios** (la fila de Reels); `propuesta`, sin verificar.

---

## Herramientas de Magnific a considerar

No son destinos ni zonas seguras: herramientas de la app que pueden ayudar en una fase. El sistema no elige herramienta por el usuario.

### Variations (modo Storyboard)
| Campo | Valor | Fuente |
|---|---|---|
| Dónde está | Image Generator → Tools → Variations | descripción del vídeo «How to create a storyboard from one image with Variations» (Magnific How-To, 2026-01-13), sin comprobar en la app |
| Qué hace | A partir de **una imagen** genera una cuadrícula de imágenes coherentes; modos Reframe, Storyboard, Character o Custom | ídem |
| Ajustes | ratio, tamaño de la cuadrícula, calidad; cada imagen se descarga por separado | ídem |
| Siguiente uso | animar los resultados con el Video Generator | ídem |
| Coste en créditos | pendiente de verificar | — |
| Encaje con el flujo | Atajo exploratorio (ángulos y encuadres desde una imagen). No sustituye a `shot-composer`: parte de una sola imagen, no de las referencias aprobadas ni del desglose. `propuesta`, sin probar | criterio propio |

### Eye Candy (vocabulario de cámara)
| Campo | Valor | Fuente |
|---|---|---|
| Qué es | Página vista en clase con tags y gifs de movimientos de cámara y tipos de plano, que el alumno puede adjuntar como referencia | la usuaria, de clase (2026-10-26), sin enlace ni cita |
| Enlace | https://eyecannndy.com/ (el acceso automático devuelve 403: Claude no puede leer la página; el contenido lo aporta el alumno) | la usuaria, 2026-10-26; 403 comprobado 2026-10-26 |
| Tags: movimientos de cámara | ARC, BOLT CAM, CAMERA ROLL, DOLLY, DOLLY ZOOM, DOUBLE DOLLY, FIXED CAM, FOCAL SHIFT, FPV DRONE, HANDHELD, LAZY SUSAN, LOCKED-ON, OMNIDIRECTIONAL, PAN, PARALLAX, PEDESTAL, PROBE, SNORRICAM, TILT, TILT SHIFT, TRACKING, TRUCKING, WANDERING, WHIP PAN, ZOOM | captura de la página aportada por la usuaria, 2026-10-26; agrupación por criterio propio, sin comprobar qué significa cada tag en la página |
| Tags: planos y ángulos | AERIAL, CENTRAL FRAMING, CLOSE-UP, DUTCH ANGLE, FIRST-PERSON, FISHEYE, GROUND LEVEL, HIGH ANGLE, LOW ANGLE, OBJECT POV, OVERHEAD, OVER THE SHOULDER, PROFILE, TWO SHOT, ULTRA WIDE, UNDERWATER, WIDE SHOT, WORMS-EYE | ídem |
| Tags: transiciones, efectos y estilo | ALTERED STATE, ANIMATION, ANTHROPO, ARCHITEXTURE, BOOMERANG, BTS, BULLET TIME, CHOREO, CINEMAGRAPH, COLLAGE, COLOR SHIFT, CONVEYOR, CRASH CUT, CUT-INS, DATAMOSH, DIORAMA, DISTORTIONS, DOUBLE EXPOSURE, DREAMCORE, DUPLICATION, DYSTOPIAN, ECHO PRINT, EPIPHANY, FALLING, FAST MOTION, FEEDBACK, FLASH CUT, FLOATING UI, FOURTH WALL, FREEZE FRAME, GENERATIVE, GESTURE, HALATION, HARD LIGHT, HAZE, INFINITE LOOP, INTERVIEW, JUMP CUT, KALEIDOSCOPE, LEVITATION, LIGHT FLASH, MAGICAL REALISM, MAGNIFICATION, MASKING, MATCH CUT, MATCH MOTION, MATCH SPLIT, MAXIMALISM, MIXED MEDIA, MORPHING, MOTION BLUR, NIGHT VISION, OBJECT PORTAL, PASS THROUGH, PHOTOGRAMMETRY, PHOTOGRAPHY, PIXEL ART, PRODUCT, PROJECTIONS, QUICK CUTS, RATIO SWITCH, REFLECTIONS, SCALE SHIFT, SCREEN IN SCREEN, SET TRANSITION, SHADOW BOX, SHALLOW FOCUS, SILHOUETTE, SLIT-SCAN, SLOW MOTION, SPEED RAMP, SPLIT DIOPTER, SPLIT SCREEN, SPOTLIGHT, STEP-PRINT, STOP MOTION, STUTTER, STYLISTIC SUCK, TABLEAU, THERMAL, TRANSFORMATION, TRANSITIONS, TYPOGRAPHY, VIDEO GAME, VIDEO PORTRAITS, VIGNETTE, VINTAGE, VOID, VOYEUR, WEIRDCORE, WIGGLEGRAM, X-RAY, ZOETROPE | ídem |
| Uso previsto | Fuente de **vocabulario**: el alumno dice el tag o nombre del movimiento o plano y la sección Cámara de `video-prompt` lo traduce a texto de prompt | propuesta |
| Ficha de cada gif | Título de la obra, **Recipe** (descripción en texto de la técnica, p. ej. «Close up flash cut subtle zoom with motion blur»), técnica, director, DOP, colorista, enlace a la fuente y tags de contenido. El alumno copia la Recipe | captura de la ficha «Flash Cut», aportada por la usuaria, 2026-10-26 |
| Gif adjunto al chat | Con `Read` solo se ve un fotograma. Sí se lee extrayendo fotogramas con `ffmpeg` (probado con «Cole Bennett - Flash Cut.gif»: 45 fotogramas, 2,25 s). Prima la Recipe sobre el gif | prueba hecha, 2026-10-26 |
| Derechos | Los gifs son fragmentos de obras de terceros: referencia de estudio, no recurso del proyecto. La página avisa de fotosensibilidad en los flash cuts | criterio propio; aviso de la página |
| Gif como referencia en Magnific | pendiente de verificar si el modelo lo acepta; mientras tanto el movimiento va descrito en el prompt | — |
| Encaje con el flujo | Apoyo opcional al describir cámara; no elige el movimiento por el alumno. `propuesta`, sin probar | criterio propio |

---

### Cambio de ángulo de cámara sobre una imagen (referencia)

Un tutorial de terceros (Tao Prompts, «The ONLY 7 Prompts…») muestra una herramienta de edición de imagen que, a partir de una imagen de un personaje, genera otros ángulos de la misma escena (rotar, acercar, inclinar arriba o abajo) con controles. **No es de Magnific** y no se ha probado aquí: se anota solo como referencia. Las imágenes que da suelen salir suaves y piden un reescalado posterior. Para el flujo del curso, los ángulos nuevos se piden con el prompt de imagen del plano (`shot-composer`).

## Plantilla para un destino nuevo
```
### <Destino>
| Campo | Valor | Fuente |
|---|---|---|
| Resolución y proporción de referencia | | |
| Libre arriba / abajo / izquierda / derecha | | |
| Caja segura | | |
| Observaciones | | |
```
Valor desconocido → `pendiente de verificar`. Cada valor lleva fuente y fecha.
