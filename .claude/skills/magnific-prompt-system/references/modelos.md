# MODELOS — directorio de modelos

Perfil por modelo para que las skills lean el de **la tarea** (REGLAS §5) y no supongan límites. **No es una lista de preferencias ni elige modelo por el usuario.**

**Estado:** primer borrador `propuesta`. Fuente de todo lo marcado «catálogo»: listado de solo lectura del catálogo de Magnific, 2026-10-22. Es lo que el catálogo declara, no una prueba hecha en la app. El usuario lo valida contra la app y, al validar, cambia la fuente de cada campo a «app, fecha».

**Reglas de uso**
- Un valor sin fuente no cuenta. `pendiente de verificar` = nadie lo ha comprobado; no se rellena por parecido con otro modelo.
- Si el modelo de la tarea no está aquí, se pregunta al usuario o se copia la plantilla (final del archivo) y se rellena con él.
- El catálogo cambia: si un campo importa para la decisión, se reconfirma antes de apoyarse en él.
- Duración máxima por generación, nº de referencias y similares **se leen de aquí**; ninguna skill lleva un número propio.

---

## Vídeo

### Seedance 2.0 (modelo base de vídeo)
| Campo | Valor | Fuente |
|---|---|---|
| Tipo | vídeo | catálogo |
| Duraciones | 4–15 s, pasos de 1 s | catálogo |
| Proporciones | 21:9 · 16:9 · 4:3 · 1:1 · 3:4 · 9:16; «auto» desde el primer fotograma | catálogo |
| Resoluciones | 480p · 720p · 1080p · 4K | catálogo |
| Longitud máxima del prompt | 40 000 caracteres | catálogo |
| Referencias | sí. Imagen 9 · vídeo 3 · personaje 9 · producto 1 · estilo 1 · audio 3 · color y efecto (sin límite indicado) | catálogo |
| Referencias de audio | requieren al menos una referencia visual; 2–15 s; mp3/wav; ≤15 MB | catálogo |
| Primer / último fotograma | sí; el último exige el primero. **No se combinan con referencias** | catálogo |
| Multiplano en un clip | sí, hasta 6 planos, 1–12 s cada uno, total ≤15 s | catálogo |
| Movimiento de cámara | lista de 52 valores predefinidos (truckLeft, pushIn, orbitLeft, handheld…) | catálogo |
| Audio nativo | efectos de sonido admitidos; opción «sin música» disponible; el resumen del catálogo habla de «native audio». Diálogo y sincronía labial: **pendiente de verificar** | catálogo (parcial) |
| Seed | pendiente de verificar (el catálogo no lo menciona) | — |
| Texto dentro del vídeo | no se usa en este flujo (el texto va en el editor); sin verificar | — |
| Imagen de entrada | jpeg/png/webp/heic/heif; 300–6000 px; proporción 0,4–2,5; límite de peso: valor `30000` sin unidad indicada | catálogo |
| Vídeo de entrada | mp4/mov; 2–15 s; ≤3 vídeos; ≤200 MB | catálogo |
| Estado | beta | catálogo |

### Seedance 2.0 Fast
Igual que 2.0 salvo: resoluciones 480p · 720p. Resumen del catálogo: borradores rápidos cuando importan los controles de Seedance o el audio nativo. Resto de campos como 2.0 (catálogo); seed y texto, pendiente de verificar.

### Seedance 2.5
| Campo | Valor | Fuente |
|---|---|---|
| Duraciones | 4–30 s, pasos de 1 s | catálogo |
| Resoluciones | 480p · 720p · 1080p · Draft | catálogo |
| Proporciones | como 2.0 | catálogo |
| Longitud máxima del prompt | 30 000 caracteres | catálogo |
| Referencias | imagen 30 · vídeo 10 (afecta al coste) · personaje 30 · producto 1 · estilo 1 · audio 10 · color y efecto | catálogo |
| Referencias de audio | **no** exigen referencia visual; 2–30 s | catálogo |
| Primer / último fotograma | como 2.0; no se combinan con referencias | catálogo |
| Multiplano en un clip | hasta 6 planos, 1–12 s cada uno, total ≤30 s | catálogo |
| Audio nativo | el resumen del catálogo cita audio nativo y lipsync; detalle de diálogo: pendiente de verificar | catálogo (parcial) |
| Seed · texto en vídeo | pendiente de verificar | — |
| Estado | beta; destacado | catálogo |

### Otros de vídeo en el catálogo (sin perfil completo)
- **Seedance 1.5 Pro:** 4–12 s; sin referencias (solo primer y último fotograma); prompt ≤2 500 caracteres; beta.
- **MiniMax H3 Max:** 5–15 s; 480p/768p; referencias imagen 9 · personaje 9 · vídeo 3 · audio 3; el sonido (efectos) es obligatorio.
- **Seedance 2.0 Mini:** marcado `private` (interno o con flag), no disponible en general.
Fuente de las tres líneas: catálogo, 2026-10-22. Si una tarea usa alguno, se rellena su perfil con la plantilla.

---

## Imagen

### Nano Banana (modelo base de imagen)
| Campo | Valor | Fuente |
|---|---|---|
| Tipo | texto a imagen | catálogo |
| Proporciones | auto · 1:1 · 21:9 · 16:9 · 9:16 · 4:3 · 4:5 · 5:4 · 3:4 · 3:2 · 2:3 | catálogo |
| Resoluciones | el catálogo no lista ninguna: pendiente de verificar | — |
| Referencias | sí; tipos: estilo · personaje · producto · imagen. Cuántas: pendiente de verificar | catálogo (parcial) |
| Seed | pendiente de verificar | — |
| Texto dentro de la imagen | no se usa en este flujo (el texto va en el editor); sin verificar | — |
| Edición con imagen de entrada | pendiente de verificar | — |
| Requiere plan premium | sí | catálogo |

### Variantes de la familia (catálogo, 2026-10-22)
| Modelo | Proporciones | Resoluciones | Nota del catálogo |
|---|---|---|---|
| Nano Banana 2 | las del base más 8:1 · 4:1 · 1:4 · 1:8 | 1k · 2k · 4k | tamaño personalizado hasta proporción 8 |
| Nano Banana 2 Lite | 1:1 · 2:3 · 3:2 · 4:3 · 3:4 · 5:4 · 4:5 · 16:9 · 9:16 · 21:9 | no lista | rápido y barato; para borradores e iteración |
| Nano Banana Pro | como el base | 1k · 2k · 4k | máxima fidelidad en un activo final; sirve para consistencia de personaje y referencias según el catálogo |
| Nano Banana 2.1 | — | 1k · 2k · 4k | `private`, no disponible en general |
Todas: referencias de estilo · personaje · producto · imagen. Seed y texto en imagen: pendiente de verificar en todas.

---

## Plantilla para un modelo nuevo
```
### <Nombre del modelo>
| Campo | Valor | Fuente |
|---|---|---|
| Tipo (imagen · vídeo · audio) | | |
| Duraciones (vídeo / audio) | | |
| Proporciones | | |
| Resoluciones | | |
| Referencias: ¿admite? ¿cuántas? ¿de qué tipos? | | |
| Primer / último fotograma · extensión de clip | | |
| Varios planos en un clip | | |
| Audio nativo (efectos · música · diálogo) | | |
| Seed | | |
| Texto dentro de la imagen o vídeo | | |
| Longitud máxima del prompt | | |
| Observaciones | | |
```
Valor desconocido → `pendiente de verificar`. Cada valor lleva fuente y fecha.
