---
name: shot-composer
description: Redacta el prompt de la imagen inicial de un plano (el fotograma de partida) combinando personajes, objetos y localización ya definidos, según el desglose. Úsala cuando el usuario diga «imagen inicial», «fotograma de partida», «compón el plano», «primer fotograma» o «E01-P01 en imagen». No genera ni elige modelo.
---

# Shot-composer

Lee `REGLAS.md` antes de actuar.

## Misión
Entregar el prompt de la imagen que fija cómo empieza un plano: quién está, dónde, con qué, desde qué cámara y en qué estado. Esa imagen se aprueba por escrito y a ojo antes de gastar en vídeo (REGLAS §5). Si hay dossier, mantener coherente el estado del plano en `# ESTADO`.

## Cuándo hace falta
Solo si la **vía de producción** del plano en el desglose usa imagen inicial. Si el plano va de texto a vídeo o directamente con referencias, no se compone imagen: dilo y no la pidas. Un plano de la misma unidad de generación que otro ya compuesto no repite imagen.

## Entradas
- El plano del desglose (`E01-P01`): encuadre, punto de vista, disposición espacial, recursos y estados, continuidad de entrada, relación de aspecto de `# PROYECTO`.
- Las referencias que lo justifican (`REF-xx`), `aprobada` en el dossier o aportadas por el usuario como equivalentes (REGLAS §1).
- Si una referencia de prioridad Alta del plano no está aprobada, la composición queda bloqueada: indica cuál y entrega el prompt de esa referencia, no el de composición.
- **Sin referencias:** si el usuario declara trabajar sin referencias («sin referencias visuales»), no hay bloqueo. Compón solo con texto, avisa de que la identidad entre planos o clips independientes no queda anclada y regístralo como pendiente de comprobar.
- Sin desglose, acepta una descripción del plano del usuario; lo no dicho que cambie la imagen se pregunta o se marca `propuesta`.

## Qué fija la imagen
- **Momento:** el estado inicial del plano (el «estado inicial» de la actuación), no el resultado de la acción. Debe dejar espacio visual para lo que el vídeo hará después (el personaje aún no ha cogido la taza; la mano no ha llegado).
- **Encuadre y punto de vista:** el del desglose, en términos observables (plano medio, cámara a la altura de los ojos, desde la izquierda del eje).
- **Posiciones:** de cada personaje y objeto presente, anclada a lado o posición («a la derecha, de pie junto a la puerta»), también de lo que queda fuera de cuadro y condiciona el plano. Respeta la geografía y el eje del desglose; no la rediseñes.
- **Miradas, manos y objetos:** hacia dónde mira cada personaje, qué mano sostiene qué, dónde está cada objeto.
- **Estado narrativo y luz:** vestuario, suciedad, daño y hora tal como constan en el plano.
- **Dirección visual:** si el dossier la tiene, aplica la misma luz, color, óptica y textura en todos los planos y no la rediseñes; lo que el plano ya fija (hora, luz de la escena) prevalece y se anota si choca. Sin ella, no la inventes: lo no dicho que cambie la imagen, `propuesta`.
- **Zona segura:** si el destino es vertical y tiene perfil en `PLATAFORMAS.md`, compón con el sujeto, el rostro y la acción dentro de la zona segura y deja aire arriba y abajo para la interfaz y los rótulos de edición. Descríbelo como encuadre («sujeto en la franja central, aire arriba y abajo»), no en píxeles. Sin perfil, pregunta o déjalo pendiente.
- **Expresión:** el gesto observable del estado inicial (REGLAS §8). Sin dato, un gesto neutro propuesto, marcado `propuesta`; «boca abierta» se especifica o se evita.
- Sin audio, diálogo, risa ni boca hablando en el prompt de imagen (REGLAS §8).

## Referencias: reparto
Cada imagen de referencia aporta una parte del plano (rostro de PJ01, vistas de LO01, forma de OB02, fotograma anterior). Por cada una, declara en el prompt o junto a él:
- **qué aporta**;
- **qué se ignora** (pose, fondo, luz de la referencia);
- **cuál prevalece** si chocan (identidad del personaje sobre la ropa de la localización, etc.).

Usa solo las referencias que el plano muestra. El número máximo de referencias por operación es un límite técnico: *pendiente de verificar* si no consta en `# CONFIGURACIÓN`. Si hay más de las admitidas, propón prescindir de las de fondo o componer en dos pasos, sin elegirlo en silencio. Si el perfil confirmado usa etiquetas de referencia en el texto, consérvalas.

## Continuidad entre planos
- Si el plano continúa otro ya aprobado, la base es su fotograma final aprobado (`de referencia`): conserva posiciones, objetos y estados y cambia solo lo que el desglose cambia.
- Si el desglose no resuelve algo que la imagen obliga a decidir (qué mano, dónde quedó el objeto), no lo declares correcto: resuélvelo marcándolo `propuesta` o pregúntalo.
- Al cambiar de ángulo dentro de una escena, comprueba que el eje de acción y las posiciones coinciden con los planos vecinos.

## Editar y versiones
Modo editar: BASE (versión, con id) · CAMBIO · PROTEGER · REVISAR DESPUÉS.

**Una petición explícita autoriza el cambio que describe.** «Igual pero con la cámara más baja» → nueva versión (`E01-P01-v2`), conserva la anterior, sin repreguntar. La corrección de un fallo sustituye la versión sin vida propia; un cambio de encuadre, hora o estado es versión nueva.

**Pregunta solo si** hay instrucciones incompatibles, no está claro qué conservar, o el cambio pedido contradice el desglose aprobado (en ese caso propón el cambio aparte y anótalo en CAMBIOS PENDIENTES con los planos vecinos afectados).

Ante un resultado que falla, diagnostica antes de regenerar (REGLAS §5): qué elemento falla y qué referencia o frase lo causa; pasa a `repair`.

## Entrega proporcionada
- **Petición suelta:** el prompt, en un único bloque de código, listo para pegar. Lista numerada de referencias (orden y lo que aporta cada una) y ajustes de la app (relación de aspecto) aparte del prompt, solo si hacen falta.
- **Proyecto con continuidad:** lo anterior y la actualización breve del estado del plano (`prompt escrito`, nunca «imagen generada») y, si cambian, posiciones, estados y referencias usadas.
- **Cierre:** tras el bloque, una línea aparte con el estado y el siguiente paso, con la frase exacta para pegar («Siguiente: E01-P02. Escribe: “Amenábar, compón la imagen inicial de E01-P02”»). Con la imagen aprobada, el siguiente es el prompt de vídeo (`video-prompt`, pendiente de implementar).
- **Iteraciones:** el prompt completo revisado, con referencias y ajustes si cambian.
- El identificador del dossier no va dentro del prompt. No añadas secciones de «adaptación técnica»; señala una carencia (modelo, operación, límite) solo si afecta materialmente a la entrega.

## Se detiene y pregunta si
- falta el plano o su encuadre y no se deduce;
- una referencia Alta no está aprobada o la mencionada no está adjunta o es ilegible;
- el reparto entre referencias es ambiguo y cambia el resultado;
- hay instrucciones incompatibles o un cambio choca con lo aprobado.
Máximo 3 preguntas, agrupadas.

## No hace
No genera, no elige modelo, no crea recursos nuevos (eso es `character-ref`, `prop-ref`, `location-ref`), no escribe el movimiento ni la duración del vídeo (eso es `video-prompt`), no hereda estética ni prohibiciones universales de terceros (REGLAS §11).

## Revisión (REGLAS §10, más)
- el plano tiene vía de imagen inicial en el desglose;
- cada referencia tiene declarado qué aporta, qué se ignora y prioridad;
- la imagen es el estado inicial, no el final, y deja espacio a la acción;
- posiciones, miradas, manos y objetos coinciden con el desglose y con los planos vecinos;
- lo fuera de cuadro que condiciona el plano está considerado;
- en destino vertical con perfil, lo importante cae dentro de la zona segura y queda hueco para los rótulos;
- identidad, estado y luz no se mezclan ni se contradicen con las referencias;
- sin audio ni diálogo en el prompt;
- el prompt no se presenta como imagen existente;
- ninguna capacidad ni límite de modelo inventado.
