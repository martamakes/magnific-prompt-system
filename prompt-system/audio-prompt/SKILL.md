---
name: audio-prompt
description: Redacta el prompt de un sonido (efecto, ambiente, música, voz o aislamiento) para pegarlo en las herramientas de audio de Magnific. Úsala cuando el usuario diga «prompt de música», «prompt de efectos», «sonido para E01-P02», «banda sonora», «voz en off» o «prompt de audio». No genera audio.
---

# Audio-prompt

Lee `REGLAS.md` antes de actuar.

## Misión
Entregar el prompt de una pieza de sonido, igual que las demás skills entregan el de una imagen o un vídeo: se pide, se recibe, se pega en la herramienta que el usuario use. Si hay dossier, mantener coherente el sonido anotado en el desglose.

## Herramienta
- La generación de audio es **solo dentro de Magnific**: sus herramientas de voz, efectos y música. ElevenLabs aparece únicamente como tecnología integrada en Magnific (voz y música); no se deriva a Suno, ACE Studio, ElevenLabs directo ni otros servicios. Si el usuario pide otro, dile que este sistema prepara audio para Magnific y pregunta si quiere seguir así.
- Escribe el prompt en la forma común (abajo) y no preguntes salvo que cambie el resultado: letra aparte, duración o controles propios de la herramienta.
- Controles y límites (duración, variaciones, calidad, créditos): los de los tutoriales de Magnific son `documentada`; lo demás, *pendiente de verificar* (REGLAS §3). No los inventes.

## Cuándo se hace cada audio
Voz y banda sonora son tareas y momentos distintos; no se piden a la vez.
- **Preproducción, para la animática:** solo diálogo o voz en off, para fijar tiempos, pausas y ritmo (`edit-plan`). Es diálogo de animática, no sincronía labial.
- **Sincronía labial:** tarea aparte, sobre el clip de vídeo (vías de `EX03c`). Los diálogos de la animática se **conservan** si sirven; no se regeneran por defecto, solo si cambia el texto, la voz o la interpretación, y con aprobación del usuario.
- **Final del montaje, con el vídeo delante:** ambientes, efectos y banda sonora. Antes no se generan, salvo una guía provisional que el usuario pida.

## Entradas
- El sonido anotado en el desglose por tipo (diálogo / voz en off · efectos de acción · ambiente · música) y el plano o escena a la que va.
- `Audio:` del proyecto. Con `sin audio` no se escribe nada de audio. Con `audio externo` o `audio en Magnific`, este es el camino para el sonido que no va dentro de un prompt de vídeo.
- Sin desglose, acepta la descripción del usuario; lo no dicho que cambie el resultado se pregunta o se marca `propuesta`.

## Un prompt por tipo de sonido
Los tipos no se mezclan en un prompt: cada uno es una pieza distinta.

**Efecto o ambiente** (`documentada`, tutorial de efectos de Magnific)
- Una frase corta y directa. Se describe lo que se oye, no por qué ocurre: qué suena, qué hace y, si hace falta, dónde.
- Ejemplos del tutorial: «car drifting»; «light rain on a window, quiet room ambience».
- Tres capas separadas en el montaje: **ambientes** (continuos, en bucle), **efectos puntuales** (pasos, roces, golpes, apariciones, transiciones) y música. Un elemento visible que debe sonar = un prompt de efecto.
- Efecto desde texto o desde vídeo (sincronización con la escena, *pendiente de verificar*): prueba primero desde vídeo en un plano corto; si inventa de más o no acierta con la acción, genera el sonido por elemento y se coloca a mano en el montaje.
- Indica aparte: duración orientativa según el sonido (el tutorial usa 5 s para un golpe seco y 10 s para una textura), si va en bucle (ambiente continuo sí; sonido con principio y fin, no) y cuántas variaciones comparar (el tutorial pide 4).
- Menos es más: sustantivos y acciones claros; sin historia ni descripciones largas.

**Música** (`documentada`, tutorial de Music Generator de Magnific; modelos y duración personalizada según la cuenta, *pendiente de verificar*)
- Funciona como el encargo de un productor: cómo debe sentirse y cómo está construida. Se puede empezar simple («upbeat French touch pop track, energetic and danceable») y añadir detalle por este orden:
  1. estilo y energía;
  2. elementos que forman el groove (bajo, sintetizadores, batería…);
  3. cómo se comporta la voz: instrumental, o ganchos vocales solo como textura rítmica, o voz con letra (cómo suena, cómo canta, qué papel tiene).
- Con letra: bloque de letra **separado al final**, con secciones simples (verso, estribillo). Mantenerlo aparte ayuda al modelo a distinguir lo que se canta de lo que describe la música.
- Indica aparte: duración, y si la herramienta tiene opción de solo instrumental, activarla cuando no haya voz.
- **Pieza larga (un montaje entero):** antes de escribir, anota entre 4 y 6 cambios de sonido ligados a giros visuales o narrativos (no a cada corte), con tramo y función. Una pieza continua con un motivo recurrente y un arco (inicio espacioso → desarrollo → contraste → punto álgido → resolución), con duración personalizada; que respete cada cambio al segundo se comprueba escuchando. Varias pruebas con el mismo encargo, comparando modelos. Para un tramo que no funcione, regenera una alternativa de ese bloque con el mismo motivo e instrumentación; no cinco piezas independientes. Añade «dejar espacio para ambientes y efectos» y excluye lo que no quieras (voz, coros, estructura de canción, golpes épicos constantes).
- Para un clip con música ya existente en el vídeo: Magnific permite conservar el sonido original, bajar la música por debajo o sustituirlo; es una decisión de mezcla, anótala en el plan de montaje.

**Voz** (`documentada`, tutorial de Speak de Magnific)
- Texto exacto aprobado, tal cual, en su idioma original (REGLAS §9) y en bloque propio. La interpretación (tono, ritmo, emoción) va aparte, una por voz.
- Voz: la elige el usuario en el catálogo de la herramienta; no la inventes. Si el sonido va sobre un clip, mide antes la lectura o la voz real y compárala con la duración del plano. Si no cabe y la duración es obligatoria, no ajustes en silencio: el usuario elige entre recortar el texto, cambiar la interpretación (ritmo) o replantear los planos; si la duración es flexible, indica que se ajustará (en Speak, el modo de extensión «auto» adapta el vídeo al habla; dato de tutorial, sin comprobar con tu cuenta).
- No añadas frases, risas ni gritos no previstos (REGLAS §8).

**Aislar un sonido** (`documentada`)
- La herramienta pide describir en palabras el sonido que se quiere aislar de un audio existente. Una frase, con el nombre del sonido.

## Idioma y forma
- El prompt va en **inglés**, en un único bloque de código por pieza (REGLAS §9). Lo que debe oírse literal (diálogo, letra) conserva su idioma entre comillas o en su bloque.
- Duración, bucle, variaciones y demás ajustes, fuera del bloque, en una línea.
- Describe lo que se oye; no cuentes la escena ni cites la imagen.

## Ligar el sonido al plano
- Anota en cada pieza a qué plano o escena va (`E01-P02`) y en qué momento entra, como estimación escrita; la sincronización real se decide en el montaje.
- Un plano puede necesitar varias piezas (un efecto y un ambiente). Una pieza por prompt.
- Sonido que ya describe el desglose como «externo» o «Magnific» sale de aquí; no se copia dentro de prompts de imagen o vídeo salvo que `Audio:` sea `audio en Magnific` y el modelo de vídeo lo admita (`video-prompt`).

## Entrega proporcionada
- **Petición suelta:** el prompt en su bloque y los ajustes en una línea.
- **Proyecto:** **Guarda el prompt en `prompts.md` antes de responder** (REGLAS §9) y di en qué entrada queda; si no está escrito ahí, no está entregado. lo anterior, con el plano al que va, y el estado `prompt escrito`, nunca «audio generado».
- **Iteraciones:** el prompt completo revisado; cambia una cosa por intento y anota qué se cambió.
- **Cierre:** línea aparte con el siguiente paso y la frase exacta para pegar.

## Se detiene y pregunta si
- falta el sonido o el plano al que va y no se puede deducir;
- el texto de la voz no está aprobado;
- pide un límite o una función de una herramienta que no consta (se marca *pendiente de verificar*).
Máximo 3 preguntas, agrupadas.

## No hace
No genera audio, no elige voz, no clona voces, no monta (`edit-plan`), no hereda estética ni prohibiciones universales de terceros (REGLAS §11).

## Revisión (REGLAS §10, más)
- un tipo de sonido por prompt;
- efectos describen lo que se oye, no la historia;
- música con estilo, elementos y voz; letra aparte si la hay;
- voz con el texto exacto aprobado, sin añadidos;
- coherente con `Audio:` y con el sonido anotado en el desglose;
- ningún límite de herramienta inventado;
- no se presenta como audio existente.
