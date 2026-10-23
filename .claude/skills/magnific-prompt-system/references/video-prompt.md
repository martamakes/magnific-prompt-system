# Video-prompt

Lee `references/reglas.md` antes de actuar.

## Misión
Entregar el prompt que describe qué ocurre en el tiempo en un plano: acción, cámara y ritmo. Si hay dossier, mantener coherente el estado del plano en `# ESTADO`.

## Entradas
- El plano del desglose (`E01-P01`): acción, actuación (estado inicial → estímulo → reacción → estado final), cámara, duración orientativa, sonido, continuidad, unidad de generación y vía de producción.
- Según la vía:
  - **Imagen inicial:** la imagen del plano, `aprobada` (de `shot-composer` o aportada por el usuario).
  - **Texto a vídeo o referencias:** las referencias `aprobada` que el plano usa.
- `Audio:` de `# PROYECTO` (por defecto `sin audio`) y modelo de la tarea de `# CONFIGURACIÓN` (REGLAS §5).
- Sin desglose, acepta una descripción del plano del usuario; lo no dicho que cambie el resultado se pregunta o se marca `propuesta`.

**Puerta:** no se redacta el vídeo de un plano cuya imagen inicial no esté aprobada, ni con referencias Alta sin aprobar (REGLAS §5, `breakdown` §D). Dilo, indica cuál falta y entrega el prompt de esa pieza. **Excepción:** si el usuario declara trabajar sin referencias, no hay bloqueo por referencias; se escribe solo con texto, avisando de que la identidad entre clips independientes no queda anclada (pendiente de comprobar). La imagen inicial, si la vía la usa, sigue siendo necesaria.

## Dos tareas distintas
- **Imagen a vídeo:** la imagen ya fija lo que se ve (personajes, lugar, luz, encuadre inicial). El prompt describe solo lo que cambia: movimiento, cámara, evolución de la luz o del estado. No redescribas la imagen ni contradigas nada de ella.
- **Texto a vídeo o con referencias:** el prompt lleva además sujeto, lugar y luz, y cada referencia con su papel (qué aporta, qué se ignora, cuál prevalece), igual que en las demás skills.

### Con vídeo de referencia
Cuando el plano use un clip como referencia, explicita el reparto:
- **Identidad:** qué referencia fija al personaje y, si procede, su vestuario.
- **Acción:** qué se toma del clip (gesto, recorrido, ritmo o movimiento de cámara). No supongas que se hereda todo.
- **Cambios:** qué se sustituye respecto al clip y qué debe conservarse.

Redacta la transformación de forma directa: qué elemento de qué referencia se sustituye por cuál. Usa etiquetas de recursos solo si su sintaxis está confirmada para el modelo y la interfaz de la tarea.

Que el catálogo admita vídeo de referencia no demuestra transferencia exacta de movimiento ni sustitución de personajes (`references/modelos.md`). Ese comportamiento queda pendiente de verificar en la app; la intención del prompt no se presenta como capacidad comprobada.

Usa material propio o con autorización adecuada; que la herramienta acepte un recurso no acredita permiso para reutilizarlo.

## Contenido del prompt
No hay fórmula obligatoria. Incluye, en este orden salvo que convenga otro:
1. **Acción** observable, en sucesión temporal (REGLAS §8: gesto, no interpretación; separa expresión, acción corporal y vocal).
2. **Cámara:** fija o movimiento, y desde dónde, según el desglose.
3. **Cambios de luz, atmósfera o estado** si los hay durante el plano. Con dirección visual en el dossier, el aspecto (luz, color, óptica) es el mismo en todos los planos; con imagen inicial, ya viene en ella y no se redescribe.
4. **Ritmo:** pausas con función narrativa, velocidad, momento en que se lee el estímulo y la reacción.
5. **Audio**, solo según el campo `Audio:` (ver abajo).

Lo que no se menciona lo decide el modelo, también la cámara: si el desglose fija cámara, dila.

## Cámara
*Criterio de trabajo mío, sin verificar con el modelo ni con generaciones reales; la única fuente de cámara por modelo es `references/modelos.md`.*
- **Fija por defecto.** La cámara se mueve solo si el movimiento aporta algo que el plano quieto no da. Si no puedes decir qué aporta, queda fija. Un movimiento por plano.
- **Según la función del plano:**

| Lo que el plano necesita | Movimiento a considerar |
|---|---|
| Llevar la atención a un detalle o dar peso a un momento | acercamiento lento |
| Revelar contexto o dar escala | alejamiento o panorámica |
| Acompañar a un sujeto que se desplaza | seguimiento (al lado, delante o detrás) |
| Mostrar volumen o espacio de un sujeto u objeto | órbita |
| Urgencia, tensión o aire documental | cámara en mano |
| Calma o contemplación | fija, o desplazamiento muy lento |
| Pasar la atención de un sujeto a otro sin cortar | panorámica |

- **Cómo se redacta:** tipo de movimiento, dirección respecto al sujeto, velocidad (lenta, constante, que se acelera), encuadre al inicio y al final, y qué queda a la vista al terminar. Sin interpretaciones («con tensión»): observable.
- **Imagen inicial:** el encuadre de partida lo fija la imagen y el movimiento arranca de ella. Un movimiento que muestra algo que la imagen no contiene (alejarse, girar) obliga al modelo a **inventarlo**: si eso importa (personaje, objeto, lugar), necesita referencia aprobada o se cambia el movimiento; si no importa, dilo.
- **Duración:** el movimiento ocupa la duración del plano. Un recorrido grande en un plano corto sale brusco: acorta el recorrido o alarga el plano.
- **Eje y tramos:** respeta el eje de acción del desglose. En un plano partido en tramos, la posición final de cámara de uno es la inicial del siguiente.
- **Modelo:** si el perfil de `references/modelos.md` lista movimientos predefinidos, se elige uno de esa lista y no se inventa un nombre. Cómo se combina con el texto del prompt y cuánto lo respeta cada modelo: *pendiente de verificar*; se anota tras la primera prueba real.

## Criterios de redacción
*Recomendaciones de repos comunitarios, no verificadas en Magnific (REGLAS §3); trátalas como criterio de partida y anota cualquier comprobación real. Donde el handbook de Magnific (v1.2) coincide, se indica.*
- **Una acción principal y un movimiento de cámara principal por plano** (coincide con el handbook de Magnific). Si el desglose pide más, es un problema de carga de acción (`breakdown` §C): propón dividir en planos o tramos, no lo apiles en un prompt.
- **Negaciones:** no niegues lo que se ve («sin coche rojo» puede producirlo); redáctalo como lo que sí aparece. Se pueden negar una referencia («no uses a las personas de la referencia 2»), una pista («sin música») o un defecto de generación («sin parpadeos»).
- **Texto en pantalla** (títulos, letreros que el plano no necesite): fuera del prompt, al montaje. Si un letrero debe verse, es parte de la imagen y no se puede asegurar (dilo).
- **No describas atributos fijos que ya están en la imagen o referencia** con otras palabras: pueden derivar. Cita la referencia.

## Duración y tramos
- La duración sale del desglose. Los límites del modelo (duración mínima y máxima, referencias admitidas, primer y último fotograma, audio) salen del perfil del modelo de la tarea en `references/modelos.md`; si falta el perfil o el campo, *pendiente de verificar*. Comprueba que la vía elegida es compatible: en el perfil de Seedance, primer y último fotograma no se combinan con referencias.
- Un plano largo o con varias fases se divide en **tramos**, cada uno con tiempo orientativo y **estado final** (físico y, si aplica, posición de cámara) que sirve de punto de partida del siguiente. Mantén la misma referencia de identidad en todos.
- Que un clip largo derive (rostro, objetos, cámara) es una hipótesis comunitaria, sin cifra verificada: no fijes un umbral.
- Los tiempos por tramo son **estimación escrita**; solo la prueba real los comprueba.
- Plano con varias acciones: se pueden marcar beats con tiempo (`00:00`, `00:02`…), una acción por beat y el último dentro de la duración. Forma del handbook de Magnific (ejemplo con Seedance 2.5, `documentada`); su eficacia con el modelo de la tarea, pendiente de comprobar.
- Un tramo que continúa otro parte del fotograma final aprobado del anterior (continuidad, como en `shot-composer`).
- Cambiar duración total o número de planos requiere autorización.

## Audio (REGLAS §8)
- `sin audio`: ni sonido ni diálogo ni boca hablando.
- `audio externo`: ningún sonido descrito en el prompt; el sonido va a montaje. Cierra con «No music. No subtitles.» (el handbook de Magnific cierra así sus prompts para obtener un clip limpio; `documentada`, avísalo en la entrega).
- `audio en Magnific`: el prompt puede llevar diálogo (texto exacto aprobado, con interpretación aparte), efectos y música, **solo si** el modelo de la tarea lo soporta; si no consta, *pendiente de verificar*. Avisa del mayor riesgo y gasto. Forma documentada en el handbook de Magnific: efectos y ambiente en palabras llanas (`SFX: …`), diálogo entre comillas atribuido a un personaje con la entrega descrita, un solo hablante por beat, «No music» para obtener solo efectos y añadir la pista en montaje, «No subtitles» para evitar subtítulos incrustados.
- Si el audio se añade después con las herramientas de la app (REGLAS §8), este prompt queda sin audio; los prompts del sonido los escribe `audio-prompt` y su colocación pasa al plan de montaje. Dato de los tutoriales: en la voz a partir de texto, el modo «extender» en automático ajusta la duración del vídeo a la del habla.
- No añadas diálogo, risa ni gritos no previstos.

## Editar, versiones y fallos
Modo editar: BASE (versión, con id) · CAMBIO · PROTEGER · REVISAR DESPUÉS.

- **Una petición explícita autoriza el cambio que describe** → versión nueva (`E01-P01-v2`), la anterior se conserva, sin repreguntar.
- **Un cambio por intento.** Tras un resultado fallido, diagnostica qué falló y cambia una sola cosa; registra qué se cambió y qué resultó. Si varios intentos no lo resuelven, simplifica el plano (acción, cámara, tramos) en vez de reformular de nuevo. Para el diagnóstico, deriva a `repair`.
- Pregunta solo ante instrucciones incompatibles, qué conservar poco claro, o un cambio que contradice el desglose aprobado (propónlo aparte y anótalo en CAMBIOS PENDIENTES).

## Entrega proporcionada
- **Petición suelta:** el prompt, en un único bloque de código, listo para pegar. Referencias (lista numerada, papel de cada una) y ajustes de la app (duración, relación de aspecto) aparte del prompt, solo si hacen falta.
- **Proyecto con continuidad:** **Guarda el prompt en `prompts.md` antes de responder** (REGLAS §9) y di en qué entrada queda; si no está escrito ahí, no está entregado. lo anterior y la actualización breve del estado (`prompt escrito`, nunca «clip generado»), con los tramos y el estado final de cada uno.
- **Cierre:** línea aparte con el estado y el siguiente paso con la frase exacta para pegar («Siguiente: E01-P02. Escribe: “Amenábar, prompt de vídeo de E01-P02”»). Con todos los clips generados, el siguiente es el plan de montaje (`edit-plan`) o la revisión.
- **Iteraciones:** el prompt completo revisado, con referencias y ajustes si cambian.
- El identificador del dossier no va dentro del prompt. Si el perfil confirmado usa etiquetas de referencia, consérvalas. No añadas secciones de «adaptación técnica»; señala una carencia solo si afecta materialmente.

## Se detiene y pregunta si
- falta el plano, o la imagen inicial / referencias necesarias no están aprobadas;
- falta el modelo de la tarea y es imprescindible (REGLAS §5);
- el reparto de referencias es ambiguo y cambia el resultado;
- hay instrucciones incompatibles o un cambio choca con lo aprobado.
Máximo 3 preguntas, agrupadas.

## No hace
No genera, no elige modelo, no crea imagen ni recursos (`shot-composer`, `*-ref`), no monta (`edit-plan`), no hereda estética ni prohibiciones universales de terceros (REGLAS §11).

## Revisión (REGLAS §10, más)
- imagen inicial y referencias requeridas aprobadas;
- el prompt de imagen a vídeo no redescribe ni contradice la imagen;
- una acción y una cámara principal; la carga coincide con `breakdown` §C;
- si la cámara se mueve, se dice qué aporta, el encuadre de inicio y de fin, y si lo que revela está en la imagen o en una referencia aprobada;
- recorrido de lo que se mueve (desde dónde, hacia dónde), manos y estado final coherentes con el desglose y con el plano siguiente;
- tramos con estado final y tiempos marcados como estimación;
- sin negación de objetos visibles ni texto en pantalla no resuelto;
- audio conforme al campo `Audio:`;
- el prompt no se presenta como clip existente;
- ningún límite ni capacidad de modelo inventado.
