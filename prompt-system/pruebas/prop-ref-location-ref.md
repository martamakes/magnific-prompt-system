# Pruebas de prop-ref y location-ref
**Qué son:** aplicaciones escritas de las skills a entradas de prueba, hechas por quien las redactó; no son ejecuciones independientes ni prueban nada en un modelo de imagen. Comprueban el **comportamiento textual** (¿pregunta cuando toca?, ¿entrega solo el prompt?, ¿separa identidad, estado y uso?, ¿respeta las reglas comunes?). Todo lo diseñado aquí es `propuesta`. Caso de datos: «La segunda taza» v0.5.

---

## PROP-REF

### A. Creación con detalles delegados — ejecutada (texto)
**Entrada:** «La taza 2 de La segunda taza: esmalte ocre, forma y asa propias; el resto a tu criterio. La taza se acerca con la mano en P03.»

**Esperado:** sin preguntas; desarrolla lo delegado; solo identidad (sin mano, sin posición en mesa); escala dada porque P03 depende del alcance; sin texto ni marcas; en inglés; el estado de la REF es «prompt escrito».

**Salida:**
```
Reference photograph of a single ceramic coffee cup standing upright on a flat surface, three-quarter view from slightly above. Hand-thrown look: rounded body, widest at the middle and narrowing gently to the base, a thick rim that is slightly uneven. A single loop handle on the right, joined at the rim and at the lower body. Plain ochre glaze, semi-gloss, a little darker where it pools near the base, with no pattern or markings. About 9 cm tall, the size of an ordinary coffee cup held in one adult hand. Plain neutral background, soft even light. Only the cup is in the frame.
```
Línea aparte: *Estado: OB02 prompt escrito. Siguiente: aprobar la imagen antes de usarla en la composición de P01.* Altura (9 cm), forma de la base y lado del asa: `propuesta` (el caso solo fija «ocre, forma y asa propias»).

**Resultado:** cumple. Observación: el lado del asa en la referencia (derecha) no fija el lado en escena; la skill ya dice que posición y mano son de la composición.

### B. Cambio explícito → variante — ejecutada (texto)
**Entrada:** «Mantén la taza igual pero con el asa rota.»

**Esperado:** sin repreguntar; `OB02-v2`, la anterior se conserva; el cambio es de estado, no de identidad; entrega el prompt completo revisado.

**Salida:** mismo prompt que A con «The handle is snapped off near the rim, leaving a small clean break; everything else about the cup is unchanged.» y nota: *OB02-v2 (estado: asa rota). OB02 se conserva. CAMBIOS PENDIENTES: ningún plano usa la versión rota; sin impacto.*

**Resultado:** cumple. Aviso: el caso no usa una taza rota (el guion la excluye por la restricción «sin recuerdos»); la prueba comprueba la mecánica, no una necesidad del caso.

### C. Instrucciones contradictorias → pregunta — ejecutada (texto)
**Entrada:** «Mantén el esmalte ocre de cerámica y hazla de cristal transparente.»

**Esperado:** detecta la incompatibilidad y pregunta antes de escribir; una sola pregunta; no elige en silencio.

**Salida:** «¿Material ocre de cerámica o cristal transparente? Son incompatibles. Dime cuál conservar, o si quieres una taza de cristal ámbar (variante con identidad distinta).»

**Resultado:** cumple.

### D. Foto real del objeto — ejecutada (texto)
**Entrada:** «Tengo una foto real de la taza, de frente y con el asa a la izquierda; P03 la muestra en detalle desde arriba.»

**Esperado:** no se genera una versión nueva (REGLAS: foto real = referencia directa); indica qué vista falta (desde arriba); pregunta solo si la foto no está adjunta.

**Salida:** «Usa tu foto como referencia directa de OB02; no hace falta generar una. Falta la vista desde arriba que muestra P03. ¿Puedes hacer una foto cenital, o la generamos a partir de esta con este prompt?» + bloque con el prompt de detalle cenital que cita «the cup in reference image 1» y deja en palabras solo la vista.

**Resultado:** cumple. Pendiente de ver: que la vista generada conserve el esmalte.

---

## LOCATION-REF

### A. Creación con geografía fijada — ejecutada (texto)
**Entrada:** «La cocina de La segunda taza: mesa pequeña en el centro, silla B a la derecha de perfil mirando a la izquierda, puerta al fondo a la izquierda, luz natural de ventana por la mañana; el resto a tu criterio.»

**Esperado:** sin preguntas; sin personas ni tazas (lugar vacío; la taza es prop y entra en la composición); elementos fijos anclados a lado o posición; una sola luz; escala dada; en inglés; ángulo base = el del eje de acción (cámara siempre en el mismo lado).

**Salida:**
```
Interior reference photograph of a small, ordinary kitchen on a morning, seen from a fixed camera at eye level on the near side of the room. A small square wooden table stands in the centre of the room. To the right of the table an empty wooden chair is seen in profile, facing left. At the back left of the room an open door leads to a dimly lit hallway. A window on the left wall lets in soft natural morning light that falls across the table. Pale painted walls, warm wooden floor, a few simple worn cupboards along the back wall. The room is empty of people and of cups, with nothing on the table. About 3 by 4 metres, ceiling at about 2.5 metres.
```
Línea aparte: *Estado: LO01 prompt escrito. Siguiente: aprobar la vista general y, si los planos cortan entre ángulos, pedir las vistas que figuren en el plan.* Propuestas: dimensiones, armarios, suelo y hall.

**Resultado:** cumple, con dos reservas: (1) «nothing on the table» es una negación de lo que se ve… pero lo que se ve en la referencia es la mesa vacía; se deja como descripción del estado. (2) La ventana a la izquierda es `propuesta` (el caso solo dice «luz natural de ventana»); la luz de P02 y la posición de la ventana podrían chocar con la puerta al fondo a la izquierda; anotado como por comprobar.

### B. Variante (noche) con la base sin aprobar — ejecutada (texto)
**Entrada:** «Haz la misma cocina de noche.» (LO01 en `prompt escrito`, sin imagen aprobada).

**Esperado según la skill:** «Una variante no se hace hasta que la base esté aprobada». Pero también «Una petición explícita autoriza el cambio que describe». Las dos reglas chocan.

**Salida (criterio aplicado):** «LO01 aún no está aprobada, así que la variante de noche (LO01-v2) espera a la imagen base. Mientras tanto, te dejo el texto del cambio para cuando se apruebe: …» + el delta de luz sin prompt completo.

**Resultado:** **hallazgo L1.** La regla de cierre y la de petición explícita se contradicen cuando la base no está aprobada. Lo que parece razonable (esperar a la base aprobada y dejar el delta preparado) no está escrito; es una inferencia mía. Decisión tuya: ¿se permite escribir la variante antes de aprobar la base, o se mantiene el bloqueo?

### C. Cierre de la localización — ejecutada (texto)
**Entrada:** Plan hipotético con LO01 vista general `aprobada` (Alta) y REF-04 contraplano (Alta) `propuesta`. «¿Está cerrada la cocina?»

**Esperado:** no cerrada; indica cuál falta; entrega el prompt de la siguiente vista.

**Salida:** «No: falta REF-04 (contraplano, Alta). Siguiente: REF-04. Escribe: “Amenábar, dame el prompt de REF-04”.» + prompt de contraplano.

**Resultado:** cumple. **Hallazgo L2:** el caso real no tiene plan de referencias (solo RECURSOS con estado `pendiente`), así que el cierre solo se puede comprobar con un plan hipotético. Para probarlo de verdad hay que pasar el caso por el apartado D de `breakdown` («plan de referencias»).

### D. Foto del lugar no adjunta — ejecutada (texto)
**Entrada:** «Usa la cocina de mi casa, te paso la foto.» (sin adjunto).

**Esperado:** no inventa; pide la imagen o confirma que se escribe solo con texto; una sola pregunta.

**Salida:** «No veo la foto adjunta. ¿La pegas, o escribo la cocina solo con texto?»

**Resultado:** cumple.

---

## Hallazgos
- **L1 (resuelto, aplicado en `location-ref`).** Decisión de la usuaria: la variante solo se escribe con la base aprobada, también si se pide de forma explícita; se dice que falta la base. Es lo que ya hacía la prueba B. Texto original del hallazgo: contradicción en `location-ref` entre «petición explícita autoriza la variante» y «una variante no se hace hasta que la base esté aprobada». `prop-ref` no tiene esta segunda regla. Opciones: (a) mantener el bloqueo y que la petición explícita no lo salte; (b) permitir escribir la variante pero avisar de que depende de una base sin aprobar. No toco la skill hasta que elijas.
- **L2.** «La segunda taza» no tiene plan de referencias; el cierre de localización y las prioridades Altas no están probadas sobre el caso real.
- **P1.** Las dos skills fijan «fondo y luz neutros» (prop) y «lugar vacío» (location) como punto de partida; su eficacia como referencia reutilizable sigue sin comprobar.
- **Sin probar:** nada de esto se ha visto en imagen. Falta comprobar que OB02 y LO01 mantienen identidad entre planos, y que el prompt en inglés rinde con Nano Banana.
