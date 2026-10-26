# EX03_AUDIO — opciones de audio y cómo trabajarlo

Introducción a los tres ejercicios de audio. Se hace **después de `EX02_ANIMACION.md`**: el audio se trabaja sobre clips ya aprobados.

| Ejercicio | Tema |
|---|---|
| `EX03a_EFECTOS.md` | efectos y ambiente |
| `EX03b_BANDA_SONORA.md` | música |
| `EX03c_DIALOGO_LIPSYNC.md` | diálogo y sincronía labial |

Los tres son independientes: se puede hacer uno sin los otros. Orden recomendado: a → b → c, de menos a más riesgo y gasto.

## Las tres opciones de audio de un proyecto

El campo `Audio:` de `# PROYECTO` (por defecto `sin audio`) decide cómo se trabaja. `REGLAS.md` §8 lo define.

| Opción | Qué significa | Quién redacta qué | Riesgo y gasto |
|---|---|---|---|
| **Sin audio** | Ningún prompt lleva sonido, voz ni boca hablando. El sonido, si lo hay, se pone en el montaje | nadie | el más bajo |
| **Audio externo** | Diálogo, voz en off, efectos y música se piensan y anotan en guion y desglose y se generan **fuera del prompt de vídeo**, con la herramienta que elijas | `audio-prompt` redacta los prompts de audio | medio |
| **Audio en Magnific** | El prompt de **vídeo** puede llevar diálogo (texto exacto aprobado), efectos y música; los prompts de imagen, nunca | `video-prompt` (en el prompt de vídeo) o `audio-prompt` (herramientas de audio de la app) | el más alto: más gasto y más fallos |

**Audio nativo en el vídeo.** Antes de escribir audio dentro de un prompt de vídeo, comprueba qué admite el modelo (`MODELOS.md`). Hoy consta que Seedance 2.0 admite efectos y la opción «sin música»; el **diálogo y la sincronía labial están pendientes de verificar**. Lo que no consta no se da por hecho: se prueba con un clip corto y se anota.

## Dos vías cuando el audio va en Magnific

1. **Dentro del prompt de vídeo**, si el modelo genera audio nativo.
2. **Después, sobre un clip ya generado**, con las herramientas de audio de la app (voz a partir de texto o de un audio subido, efectos, música, aislar sonido). Esta vía no es un prompt de vídeo: su prompt lo redacta `audio-prompt`, y la colocación en el vídeo es plan de montaje (`edit-plan`).

Las dos vías vienen del handbook y los tutoriales de Magnific (`documentada`, sin comprobar con tu cuenta ni con tu modelo).

## Herramientas

La herramienta la eliges tú: Magnific (incorpora ElevenLabs para voz y música), ACE Studio, Suno, ElevenLabs u otra. El sistema **no elige herramienta ni voz**. Controles y límites (duración, variaciones, créditos) de las que no son Magnific: pendiente de verificar.

## Cómo se trabaja, siempre igual

1. **Decide el campo `Audio:`** antes de empezar el proyecto.
2. **Anota el sonido en el desglose**, por tipo y por plano: diálogo o voz en off · efectos de acción · ambiente · música.
3. **Un prompt por tipo de sonido**: no se mezclan en el mismo. Lo redacta `audio-prompt`.
4. **El prompt va en inglés**, en un bloque; lo que debe oírse literal (diálogo, letra) conserva su idioma. Duración y ajustes, en una línea aparte.
5. **Genera, escucha y aprueba** antes de pasar al siguiente. Un prompt escrito no es un audio generado.
6. **La colocación y la mezcla** (niveles, solapes, música por debajo de la voz) se deciden en el plan de montaje (`edit-plan`) y se ejecutan en DaVinci Resolve (módulo 5).

Frase para empezar:
```text
Amenábar, prompt de audio de E01-P02: [qué suena y a qué plano va].
```

## Reglas comunes a los tres ejercicios

- Un tipo de sonido por prompt. Efectos describen lo que **se oye**, no la historia.
- No se añade diálogo, risa ni gritos que no estén aprobados.
- Cambia **una sola cosa** por intento y anota qué cambió.
- Mira el coste antes de ejecutar y anota créditos gastados.
- El audio sirve para aprender la forma de trabajo; la mezcla fina es del módulo 5.

## Por verificar antes de dar la clase

- [ ] Qué herramientas de audio tiene tu cuenta de Magnific y su coste en créditos.
- [ ] Si el modelo de vídeo que uses genera diálogo y sincronía labial, y con qué calidad.
- [ ] Duración máxima de cada pieza en la herramienta elegida.
