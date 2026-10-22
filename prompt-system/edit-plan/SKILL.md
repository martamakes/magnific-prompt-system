---
name: edit-plan
description: Redacta el plan de montaje de una pieza: orden y duración de los clips, tipo de unión entre clips, colocación y mezcla del sonido y texto en pantalla. Úsala cuando el usuario diga «plan de montaje», «cómo monto los clips», «orden de clips», «dónde va el sonido», «transiciones» o «títulos». No monta ni genera.
---

# Edit-plan

Lee `REGLAS.md` antes de actuar.

## Misión
Entregar el plan para montar los clips en el editor que el usuario use: qué va en qué orden, cómo se unen, dónde entra cada sonido y qué texto aparece. Es el último paso del recorrido; no genera nada ni elige editor.

## Entradas
- Guion, desglose y `# PROYECTO` (duración objetivo, formato, `Audio:`).
- Los clips: los planos del desglose y, si existen, lo que se generó de verdad (duración real, último fotograma, qué falló).
- Si un plano tiene **varios intentos** generados (`-v2`, `-v3`…), cuál es cada uno y qué tiene de bueno o de malo; el usuario lo dice, no lo ves tú.
- El sonido anotado por tipo en el desglose y, si existen, los prompts o piezas de `audio-prompt`.
- Sin dossier, acepta una lista de clips y una descripción del usuario; lo no dicho que cambie el resultado se pregunta o se marca `propuesta`.

**Trabaja con lo generado, no con lo planeado.** Si hay clips, parte de su duración real y de cómo acaban; si no, el plan queda como `propuesta` sobre la duración orientativa. No declares una unión correcta sin ver cómo terminan y cómo empiezan los clips que une (REGLAS §10).

## Contenido del plan
En este orden, solo lo que la pieza necesita:

1. **Orden y duración.** Los clips en secuencia, con duración (real u orientativa) y suma frente a la duración objetivo. Cambiar la duración total o el número de clips requiere autorización.
   **Varios intentos de un plano (selección de tramos).** Criterio de trabajo, sin verificar: no hace falta quedarse con un intento entero; puede usarse un tramo de cada uno.
   - Por plano, una fila por tramo elegido: intento (`E01-P02-v2`) · de qué segundo a qué segundo · por qué se elige. Los segundos los da el usuario tras revisar los clips o son estimación marcada; no los inventes.
   - Si el plano necesita una duración y un solo tramo no la cubre, indica qué tramos se encadenan y la unión entre ellos.
   - Tramos de intentos distintos solo se unen si coinciden posición, mano, mirada, luz y eje en el punto de unión; si no se puede asegurar, déjalo como pendiente o deriva a `repair`.
   - Elegir tramos ahorra regenerar (REGLAS §5), pero no sustituye al diagnóstico de lo que falló.
   - Un intento que no se usa queda anotado como descartado, sin borrar su identificador.
2. **Uniones.** Una por cada paso entre clips, con su tipo. Los tipos son los cinco del handbook de Magnific (v1.2), `documentada`:
   - *corte seco:* ruptura limpia; es el valor por defecto cuando nada tiene que conectarse;
   - *enlace congelado:* el primer fotograma del clip siguiente repite el último del anterior;
   - *puente de acción:* un movimiento empieza al final de un clip y se completa al principio del siguiente, desde otro ángulo;
   - *corte por coincidencia:* dos fotogramas comparten forma, posición o color mientras cambia la escena;
   - *portal:* la cámara entra en algo que llena el cuadro y sale en otro sitio.
   El tipo lo decide el guion o el brief («sin cortes», «mientras tanto», «se convierte en…»). Sin pista, corte seco; el portal no es valor por defecto y se usa como mucho una vez. Si una unión exige que el clip siguiente continúe el anterior, anótalo para `video-prompt` (estado final que sirve de punto de partida).
   Comprueba en cada unión la continuidad del desglose: posición, mano, mirada y eje de acción.
3. **Sonido.** Una fila por pieza:
   - tipo (diálogo / voz en off · efecto · ambiente · música);
   - de dónde viene (prompt de `audio-prompt`, herramienta de audio de la app, banco o grabación del usuario);
   - plano o clip al que va y dónde entra, como estimación escrita (la sincronía real se ajusta en el editor);
   - mezcla: nivel relativo (más fuerte, de fondo, bajo la voz) y, si el clip ya tiene sonido, qué se conserva, qué se baja y qué se sustituye.
   Con `sin audio`, la sección va vacía. Con `audio externo` o `audio en Magnific` cuando el sonido ya está en el clip, anota qué se conserva. Sin música ni voz que el proyecto no pida (REGLAS §8).
4. **Texto en pantalla.** Títulos, rótulos o subtítulos que `video-prompt` dejó fuera del prompt: texto exacto, en su idioma original, en qué clip y cuánto tiempo. Lo que no se pidió, no se añade. En destino vertical, colócalo dentro de la zona segura del destino (`PLATAFORMAS.md`); sin perfil, pendiente. Comprueba que no tape rostro ni acción.
5. **Pendientes.** Qué clips faltan o hay que regenerar, qué unión no se puede asegurar y qué decide el usuario.

## Formato y entrega
- **Dos tablas.** Clips: una fila por clip o tramo (orden · clip · duración · unión con el siguiente · texto). Sonido: una fila por pieza (tipo · origen · a qué va · entrada · mezcla), porque un ambiente puede cruzar varios clips. Debajo, lo que no cabe en las tablas.
- **Petición suelta:** el plan, sin preámbulo. **Proyecto:** el plan y la actualización breve del estado (`plan escrito`, nunca «montado»).
- Los tiempos son **estimación escrita** hasta que se montan. El plan no fija software, formato de exportación ni ajustes de color (no los pide el recorrido).
- **Cierre:** línea aparte con el estado y el siguiente paso con la frase exacta para pegar (por ejemplo, el prompt de sonido que falta o el clip que hay que regenerar con `repair`).

## Se detiene y pregunta si
- no hay clips ni desglose con los que ordenar;
- la suma de duraciones no cuadra con el objetivo y hay que decidir qué recortar;
- una unión exige regenerar un clip y no está claro si se autoriza;
- se pide música, voz o texto que el proyecto no incluye.
Máximo 3 preguntas, agrupadas.

## No hace
No monta ni exporta, no elige editor ni herramienta, no genera clips ni sonido (eso es `video-prompt` y `audio-prompt`), no hereda estética ni prohibiciones universales de terceros (REGLAS §11).

## Revisión (REGLAS §10, más)
- la suma de duraciones frente a la objetivo, sin cambiar la total en silencio;
- cada unión con tipo y justificada por el guion o por el valor por defecto;
- continuidad (posición, mano, mirada, eje) comprobada en cada unión;
- cada sonido del desglose figura en el plan o queda como pendiente;
- sonido coherente con `Audio:`; mezcla de lo que ya trae cada clip;
- texto en pantalla exacto y solo el pedido;
- cada tramo elegido de varios intentos con su intento, sus segundos y su motivo, y la continuidad comprobada en las uniones entre intentos;
- tiempos marcados como estimación; el plan no se presenta como montaje hecho;
- ningún límite ni capacidad de herramienta inventado.
