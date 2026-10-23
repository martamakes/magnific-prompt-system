---
name: breakdown
description: Convierte un guion en un desglose técnico por planos, un desglose de recursos (personajes, vestuario, props, localizaciones) y, tras aprobarlo, el plan de referencias (REF-01…). Úsala cuando el usuario diga «divide en planos», «haz el desglose», «qué imágenes necesito» o «plan de referencias».
---

# Breakdown

Lee `REGLAS.md` antes de actuar.

## Misión
Dos entregables a partir del guion. Distingue escena, plano y clip generado; no son equivalentes.

## A. Desglose técnico por plano
**Dónde cortar una escena.** Criterio de trabajo (no regla universal): un plano es una vista continua de cámara (REGLAS §7), así que un plano nuevo solo se justifica si cambia algo que el espectador necesita ver de otra forma:
- el punto de vista o el encuadre que hace falta para entender la acción (de un gesto en detalle a una vista general);
- el sujeto de la atención (de un personaje u objeto a otro);
- el lugar o el momento (esto abre otra escena, no otro plano);
- la carga de acción del plano supera lo que cabe (§C), y el encargo permite dividir.
Si nada de eso cambia, se mantiene el mismo plano. Con un número de planos o una duración total fijados por el encargo, el reparto se ajusta a ellos; no se cambian en silencio. Cada corte propuesto lleva su motivo en «función narrativa».

Por cada plano:
- identificador (`E01-P01`);
- función narrativa o comunicativa;
- acción;
- disposición espacial y eje de acción, cuando haya interacción espacial relevante (ver más abajo);
- encuadre y punto de vista;
- cámara fija o movimiento previsto;
- duración orientativa;
- sonido, anotado por tipo (diálogo / voz en off · efectos de acción · ambiente · música; «—» en los que no apliquen) (según `Audio:` de PROYECTO: con `sin audio`, «—»; con `audio externo`, anotado para montaje y marcado «externo», sin entrar en prompts; con `audio en Magnific`, anotado y marcado «Magnific» para el prompt de vídeo; la duración del plano no se ajusta a diálogo);
- recursos y estados presentes (incluidos los que quedan fuera de cuadro);
- continuidad de entrada y salida;
- conexión con otros planos;
- vía de producción propuesta (texto a vídeo, imagen inicial, referencias…);
- unidad de generación: plano independiente, clip con varios planos o secuencia;
- alternativa más sencilla, cuando sea necesaria.

Cuando proceda (no en todos los planos), añade actuación: estado inicial → estímulo → reacción observable → estado final, y objetivo de la mirada. Un personaje puede mantener una expresión o actitud sin transición. Describe el gesto observable; no lo conviertas en una interpretación («mira la puerta» no significa «espera a alguien»).

Las indicaciones son planificación creativa: no las presentes como capacidades garantizadas del modelo.

### Disposición espacial y eje de acción
Solo cuando haya personajes u objetos que interactúan en el espacio; no es obligatorio para una imagen suelta ni para un plano sin interacción espacial relevante. Indica:
- posición de personajes y objetos, también de los que queden fuera de cuadro (no visible ≠ inexistente);
- acceso o entrada;
- posición de cámara respecto al eje, cuando sea necesaria para que los cortes encajen.

Define la geografía una vez y mantenla; no añadas movimientos para arreglar una contradicción previa.

## B. Desglose de recursos
- personajes y estados;
- vestuario;
- props y estados;
- localizaciones;
- referencias disponibles;
- referencias pendientes;
- planos que usan cada recurso.

## C. Carga de acción por plano
Comprobación cualitativa, sin ratio universal de acciones por segundo ni máximo arbitrario. Para cada plano:
- qué debe comprender el espectador;
- qué acciones son sucesivas y cuáles pueden simultanearse;
- desplazamientos y manipulaciones necesarios;
- tiempo para reconocer el estímulo y para leer la reacción;
- pausas con función narrativa;
- estado inicial y final;
- si la acción exige prisas incompatibles con el tono.

Si un plano está sobrecargado, por este orden:
1. empieza más cerca del momento significativo (acciones ya iniciadas);
2. elimina pasos secundarios o redundantes;
3. redistribuye el tiempo entre planos;
4. propón dividir el plano solo si el encargo lo permite.

No cambies en silencio la duración total ni el número de planos. Marca cada comprobación como **estimación escrita**; solo una prueba temporal (ensayo, animatic o similar) la convierte en comprobada.

## D. Plan de referencias
Se genera cuando el usuario aprueba el desglose, no antes. Convierte las «referencias pendientes» de B en una lista de trabajo ordenada; sin ella el usuario no sabe qué imagen toca hacer.

Una fila por referencia, numerada (`REF-01`, `REF-02`…):

| REF | Qué | Vistas o estados | Lo justifica (planos) | Prioridad | Estado |
|---|---|---|---|---|---|

Reglas:
- **Las vistas salen de los planos**, no de una plantilla. Si un plano muestra a Isabel de perfil, pide perfil; si los vecinos salen de espaldas, pide espaldas. Si ningún plano necesita una vista, no la pidas.
- **Hoja de vistas** (frente, perfil, espaldas en una sola imagen) cuando un personaje necesita 2 o más vistas; imagen única en los demás casos.
- **Estados y variantes** (vestuario, peinado, daño, versión «pintado» frente a «vivo») son referencias aparte, con identidad heredada de la base.
- Incluye también objetos, localizaciones y combinaciones personaje + vestuario que los planos usen.
- **Hoja de vestuario** (`character-ref`): línea opcional, solo si el vestuario es importante y se repite en varios planos. Prioridad Media por defecto; Alta solo si el usuario lo pide. Si no se quiere, no se genera y no bloquea.
- **Objeto real de marca o de la colección:** si el usuario tiene foto real, se usa como referencia directa y no se genera una versión nueva (puede deformar textos y detalles). Anota qué vista falta si los planos lo muestran desde otro lado.
- **Prioridad:** Alta si bloquea planos de varias escenas o el protagonista; Media si afecta a una escena; Baja si es de fondo.
- Todas empiezan en estado `propuesta`; pasan a `prompt escrito`, `imagen generada` y `aprobada` según el dossier (ver `PROYECTO.md`, `# ESTADO`).
- Una referencia Alta sin aprobar bloquea la composición.
- Orden de trabajo sugerido: protagonista → localización principal → resto de personajes → objetos → variantes.

## Alternativas y unidad de generación
- Distingue: clip con un único plano · clip que contiene varios planos con cortes · varios clips independientes.
- **Zona segura:** en destino vertical, el encuadre de cada plano deja el sujeto y la acción dentro de la zona segura del perfil de `PLATAFORMAS.md` y reserva hueco para los rótulos de edición; sin perfil, queda pendiente. No hace falta repetirlo en cada plano: se anota en las restricciones y se señalan solo los planos que lo comprometen.
- **Duración máxima por generación:** sale del perfil del modelo de la tarea en `MODELOS.md`, no de un número de la skill. Un plano que la supere se divide en tramos o se pasa a varios clips (`video-prompt`, «Duración y tramos»). Sin perfil o con el dato pendiente, no la supongas: dilo y pregunta.

### Criterio de bloques
Criterio de trabajo (mío, sin verificar con el modelo): el bloque, es decir lo que se genera de una vez, lo marca la historia y la carga de acción, y el máximo del modelo solo lo limita.
1. **Parte de la narrativa.** Lo que forma una unidad (una acción completa, una escena corta, un momento continuo sin cambio de lugar) tiende a ser un bloque; un cambio de lugar o de momento abre otro (ver «Dónde cortar una escena»).
2. **Comprueba la carga (§C).** Si el bloque no cabe con tiempo para leer estímulo y reacción, se divide aunque el modelo admita más duración. Que el modelo permita X segundos no obliga a llenarlos.
3. **Aplica el máximo del perfil.** Si el bloque lo supera, se divide en el punto con menos coste de continuidad (una pausa, un cambio de encuadre ya previsto). Con varios planos en un clip, respeta además el número de planos y la duración por plano que declare el perfil.
4. **Cada bloque anota** su duración orientativa, su estado final (que sirve de punto de partida del siguiente si hay continuidad) y qué unión se espera con el siguiente.
5. **Las uniones entre bloques son de `edit-plan`.** Aquí solo se anota la unión prevista; el desglose no monta.
6. **Menos bloques, menos generaciones**, pero un bloque largo es más difícil de corregir: si falla en un tramo, se regenera entero (REGLAS §5, economía de generación). Solo se agrupa cuando la historia lo pide, no por ahorrar.
Sin perfil del modelo o con el máximo pendiente de verificar, los bloques se proponen por narrativa y carga y se marcan «máximo por comprobar». El número de planos y la duración total del encargo no cambian (§A).
- La alternativa más sencilla conserva las restricciones del encargo (número de planos, duración, condiciones). Si solo hay alternativa cambiándolas, pide autorización en vez de aplicarla.
- No afirmes que agrupar sea más sencillo sin justificarlo; la viabilidad de un clip con cortes depende del modelo y queda pendiente de verificar.

### Acción común con variantes de entorno
Solo cuando el guion lo pida, identifica los planos que repiten una acción en distintos entornos:
- qué permanece: identidad, acción y, cuando proceda, encuadre o cámara;
- qué cambia: localización, atmósfera, vestuario u otros elementos;
- referencia común, si existe, y papel que cumple;
- punto previsto de enlace: fase del gesto, dirección del movimiento y posición del sujeto en cuadro.

Es un patrón de planificación, no una garantía de repetición exacta. Cada variante conserva su identificador y su vía de producción. La unión se anota como prevista; su resolución corresponde a `edit-plan`.

No presupongas que todas las variantes deban generarse en un solo clip ni cambies el número de planos o la duración aprobados.

## Entradas
Guion (o sección GUION). Si no existe, pide el guion o sugiere pasar por script. Acepta un guion equivalente aportado por el usuario.

## Se detiene si
Un plano no tiene función o contenido suficientemente definidos para planificarlo, o la duración total no cuadra con el objetivo del brief: señálalo y propón ajuste.

Un plano puede mostrar una acción, un estado, un objeto, un espacio o una pausa deliberada. No se exige movimiento ni transición emocional en todos los planos.

## Salida
Las secciones DESGLOSE TÉCNICO y RECURSOS del dossier, listas para pegar (si `# DESGLOSE TÉCNICO` es un puntero a `desglose.md`, el desglose va en ese archivo y el dossier conserva solo el puntero; ver `PROYECTO.md`), más «Decisiones pendientes» si las hay. Tras la aprobación, el plan de referencias (D), también para pegar en `# ESTADO`. Revisión compartida (REGLAS §10) antes de entregar: verifica contra el propio texto del desglose, no solo que los campos estén rellenos.
