# Coherencia

Lee `references/reglas.md` antes de actuar. Se puede lanzar en cualquier fase y se recomienda al cerrar cada una.

## Misión
Detectar contradicciones y restos entre los archivos del proyecto. Solo lee y informa: no corrige, no reescribe y no cambia estados. Nada se arregla sin que el usuario elija.

## Entradas
Dossier (`proyecto.md`), `guion.md`, `desglose.md` y lo que enlacen, más `references/plataformas.md`. Si falta alguno, dilo y revisa lo que haya; no lo inventes.

## Qué comprueba
1. **Versiones:** qué versión es cada archivo y si el que depende de otro lo sigue (p. ej. guion v1 con desglose v2). Si el guion cambió de versión o de reparto, el desglose y el dossier deben citarlo.
2. **Cifras:** número de planos, duración total y por plano, tiempos de la voz.
3. **Estado y origen:** ninguna cabecera dice `aprobada` sobre algo que solo está `propuesta`; el alcance de una aprobación (estructura, copy, tiempos, encuadres) coincide en todos los archivos.
4. **Decisiones sin reflejar:** lo decidido en un archivo (p. ej. una revisión de estilo aplicada) consta en el dossier y en `# CAMBIOS PENDIENTES` si afecta a otros.
5. **Restos:** líneas obsoletas, frases cortadas, punteros rotos, `Audio:` sin fijar mientras otros archivos ya asumen audio.
6. **Constantes compartidas:** colores (HEX), URLs, zona segura y códigos (`PJ01`, `OB02`, `LO03`, `REF-xx`) idénticos en todos los archivos y definidos en alguno.
7. **Recursos:** todo código usado en el desglose existe en RECURSOS, y viceversa.

## Procedimiento
1. Lee los archivos y anota versión, estado y cifras de cada uno.
2. Contrasta por categorías. Cada hallazgo cita **archivo y línea** de las dos partes en conflicto, con el texto exacto.
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
