---
name: finish-deliver
description: Redacta el plan de acabado y entrega de una pieza ya montada (acabado visual y sonoro, títulos y subtítulos si proceden, especificación de entrega, exportación y archivo). Úsala cuando el usuario diga «acabado», «especificación de entrega», «exportar», «subtítulos», «archivar el proyecto» o «prepara la entrega». No exporta ni edita.
---

# Finish-deliver

Lee `REGLAS.md` antes de actuar.

## Misión
Llevar el primer montaje aprobado hasta una pieza entregable: qué se hace en el acabado, qué se exporta y qué se archiva. Redacta la lista; el usuario ejecuta en su editor o en la app y trae lo que ve.

## Entradas
- `# PROYECTO` (destino, formato, duración objetivo, `Audio:`, criterio de éxito), el plan de montaje y el primer montaje revisado (si no existe, dilo: esta fase espera a `quality-review` del primer montaje).
- Registro de producción y `# PROCEDENCIA` del dossier.
- `PLATAFORMAS.md` para el destino. Sin perfil, `pendiente de verificar`.

## Contenido
Solo lo que la pieza necesita, en este orden:
1. **Acabado visual.** Corrección de color o aspecto unificado entre clips, solo si el look del brief lo pide o hay saltos entre clips; reescalado o estabilización si se decidió. Cada ajuste con motivo.
2. **Acabado sonoro.** Niveles relativos entre voz, música, ambiente y efectos; limpieza de voz; cortes y fundidos de sonido; coherencia con `Audio:`. Sin sonido que el proyecto no pida (REGLAS §8).
3. **Títulos y subtítulos.** Texto exacto, idioma original, clip y tiempo; subtítulos solo si el destino, el público o el brief los piden (por ejemplo, vídeo sin sonido en redes). Dentro de la zona segura del destino.
4. **Especificación de entrega.** Una por destino: formato de imagen y relación de aspecto, duración, entrega de audio, peso o límites que imponga la plataforma. Valores de `PLATAFORMAS.md` o `pendiente de verificar`; no inventes cifras ni ajustes de exportación de un programa.
5. **Exportación.** Qué se exporta (versión final, versiones por destino, versión sin textos si se pide) y cómo se nombran los archivos con versión.
6. **Archivo.** Qué se guarda y dónde lo decide el usuario: pieza final, proyecto de montaje, clips elegidos y descartados con su identificador, prompts (`prompts.md`), dossier, registro de producción, procedencia y permisos.

## Formato y entrega
- Una lista de comprobación con una fila por tarea (tarea · motivo · estado `pendiente` / `hecha, vista por el usuario`).
- Petición suelta: la lista sin preámbulo. Proyecto: la lista y la actualización breve del estado (lista de acabado: documento `propuesta`; entrega `exportado` y `verificado` solo cuando el usuario confirma que existe el archivo y lo ha reproducido entero).
- **Cierre:** línea aparte con el estado y el siguiente paso con la frase exacta (normalmente, `quality-review` de la entrega).

## Se detiene y pregunta si
- no hay primer montaje o no está revisado;
- falta el destino o su formato y cambia la especificación;
- se pide un acabado que el brief no incluye (música nueva, voz nueva, efectos de imagen).
Máximo 3 preguntas, agrupadas.

## No hace
No exporta ni edita, no elige editor ni ajustes de exportación sin fuente, no genera material nuevo (eso es `video-prompt` y `audio-prompt`), no aprueba la pieza: la revisa `quality-review` y la aprueba el usuario.

## Revisión (REGLAS §10, más)
- cada ajuste de acabado tiene motivo en el brief o en una incidencia;
- sonido coherente con `Audio:`; textos exactos y solo los pedidos;
- especificación por destino con fuente o `pendiente de verificar`;
- el archivo incluye la procedencia y los permisos;
- nada presentado como exportado o entregado sin confirmación del usuario.
