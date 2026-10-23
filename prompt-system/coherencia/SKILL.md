---
name: coherencia
description: Comprueba que los archivos de un proyecto no se contradicen (guion, desglose, dossier, plataformas) y lista los conflictos con archivo y línea. Úsala cuando el usuario diga «comprueba coherencia», «revisa conflictos», «¿está todo alineado?» o al cerrar una fase. Solo lee; no corrige ni genera.
---

# Coherencia

Lee `REGLAS.md` antes de actuar. Se puede lanzar en cualquier fase y se recomienda al cerrar cada una.

## Misión
Detectar contradicciones y restos entre los archivos del proyecto. Solo lee y informa: no corrige, no reescribe y no cambia estados. Nada se arregla sin que el usuario elija.

## Entradas
Dossier (`proyecto.md`), `guion.md`, `desglose.md` y lo que enlacen, más `PLATAFORMAS.md`. Si falta alguno, dilo y revisa lo que haya; no lo inventes.

## Qué comprueba
1. **Versiones:** qué versión es cada archivo y si el que depende de otro lo sigue (p. ej. guion v1 con desglose v2). Si el guion cambió de versión o de reparto, el desglose y el dossier deben citarlo. Una diferencia de realización se evalúa según «Antes de informar».
2. **Cifras:** número de planos, duración total y por plano, tiempos de la voz.
3. **Estado y origen:** ninguna cabecera dice `aprobada` sobre algo que solo está `propuesta`; el alcance de una aprobación (estructura, copy, tiempos, encuadres) coincide en todos los archivos.
4. **Decisiones sin reflejar:** lo decidido en un archivo (p. ej. una revisión de estilo aplicada) consta en el dossier y en `# CAMBIOS PENDIENTES` si afecta a otros.
5. **Restos:** líneas obsoletas, frases cortadas, punteros rotos, `Audio:` sin fijar mientras otros archivos ya asumen audio.
6. **Constantes compartidas:** colores (HEX), URLs, zona segura y códigos (`PJ01`, `OB02`, `LO03`, `REF-xx`) idénticos en todos los archivos y definidos en alguno.
7. **Recursos:** todo código usado en el desglose existe en RECURSOS, y viceversa.

## Antes de informar
- **Verifica en la versión actual.** Relee el archivo y la línea antes de citar un hallazgo. Si la cita se ha cortado (`cut`, salida truncada) o no la has visto completa, no la uses. Una línea que parece cortada puede ser solo tu lectura.
- **Distingue los niveles** de lo que dice cada archivo, y no los confundas:
  1. tratamiento narrativo (guion) frente a realización (desglose);
  2. propuesta incorporada al documento;
  3. incorporación autorizada por el usuario;
  4. decisión aprobada;
  5. resultado probado.
- **No infieras aprobación** por la presencia de una propuesta en un archivo, ni conviertas una recomendación de `review` en decisión del usuario. Lo aplicado por instrucción acredita el alcance de esa instrucción. No implica por sí solo aprobación global del documento ni validación del resultado. Si el usuario aprueba expresamente una decisión concreta, registra esa aprobación con su alcance.
- **Si dos archivos discrepan,** fija primero el alcance y el estado de cada uno (qué cubre, si es `propuesta` o `aprobada`) y solo entonces di si hay conflicto o cuál prevalece. Una diferencia entre tratamiento narrativo y realización no es conflicto por sí misma. Comprueba si desarrolla aspectos abiertos o contradice una decisión aprobada. Que el cambio esté declarado no acredita su autorización.

## Procedimiento
1. Lee los archivos y anota versión, estado y cifras de cada uno.
2. Contrasta por categorías. Cada hallazgo cita **archivo y línea** de las dos partes en conflicto, con el texto exacto, verificado según «Antes de informar».
3. Clasifica: **de fondo** (cambia lo que se produce) · **menor** (consistencia o limpieza). Separa también lo que es conflicto de lo que es solo una decisión pendiente ya registrada.
4. No des por bueno lo que no has comprobado: indica qué archivos no has podido contrastar.

## Salida
1. Lista de conflictos de fondo, luego menores; cada uno con archivo:línea y texto exacto de ambos lados.
2. «Sin conflicto»: lo comprobado y coincidente.
3. «No comprobado».
4. Una propuesta de resolución por conflicto (cuál archivo manda, o pregunta al usuario) y la pregunta de cuáles aplicar.

## Límites
- No decide qué archivo tiene razón si no consta; lo pregunta.
- No cambia duración, número de planos ni textos aprobados sin autorización.
- No valida calidad visual ni capacidades de modelo.
- Para el estado de la copia instalada de las skills usa `check-sync.py` (en la raíz del repo); no lo adivines.
