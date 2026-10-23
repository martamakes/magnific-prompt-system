# Repair

Lee `references/reglas.md` antes de actuar.

## Misión
Entender por qué un resultado no sirve y entregar el prompt corregido para pegar en la app. Diagnostica antes de regenerar (REGLAS §5): cada intento cuesta créditos.

## Entradas
- El prompt que se usó y las referencias adjuntas (qué papel tenía cada una).
- El resultado: imágenes que el usuario adjunte, o su descripción de lo que ve. **No ves un vídeo**: trabaja con fotogramas que aporte o con lo que describa, y dilo. Lo que no se ha visto no se diagnostica como hecho.
- **Dónde falla, en el feedback del usuario.** Para un vídeo, el segundo (o tramo) en que ocurre y el elemento concreto (qué personaje u objeto, qué parte: mano, rostro, llave, cámara). Con eso se diagnostica sobre un hecho; sin ello, «se ve raro» no basta. Si falta, se pide (ver más abajo). En una imagen, el elemento y su posición en el encuadre. Un fotograma del segundo indicado vale más que la descripción.
- Qué se esperaba: el plano del desglose y su estado inicial y final, si hay dossier.
- Intentos anteriores y qué se cambió en cada uno.

## Diagnóstico
En este orden, solo lo que el resultado muestra:
1. **Qué falló, observable, con su segundo y su elemento:** el gesto, la posición, la identidad, la acción o el sonido concretos, no «queda raro». Separa lo que está bien (se protege) de lo que falla.
2. **Dónde puede estar la causa**, como hipótesis ordenadas por probabilidad, cada una con la frase o la referencia que la sugiere:
   - *el prompt:* instrucción ambigua, contradictoria, repetida o con demasiadas acciones;
   - *las referencias:* una falta, chocan entre sí o el reparto de papeles no está claro;
   - *el plan:* el plano del desglose está sobrecargado o pide algo que el modelo no sostiene (marcado *pendiente de verificar*);
   - *el modelo:* límite o comportamiento propio; solo si lo anterior no lo explica, sin inventar capacidades.
3. **La causa se marca `propuesta`**: sin prueba de que es esa, es una hipótesis. Un solo intento no la confirma.

## El arreglo
- **Un cambio por intento.** Elige el de más probabilidad y menor coste. Si el cambio lo resuelve algo que no exige regenerar (recortar, reencuadrar, cambiar el montaje con `edit-plan`), propónlo antes.
- Conserva lo que funciona (PROTEGER). Lo que se cambia va en la versión nueva (`E01-P01-v2`); la anterior se conserva.
- Si el fallo nace en el desglose (plano sobrecargado, continuidad que no cierra), propón el cambio aparte y anótalo en CAMBIOS PENDIENTES; no lo apliques.
- **Tras varios intentos sin mejora, simplifica** el plano (acción, cámara, número de tramos) en vez de reformular otra vez. Si lo simplificado cambia el desglose aprobado, pide autorización.
- Si el fallo está en la imagen inicial, corrige la imagen antes de gastar en vídeo.

## Formato y entrega
- **Petición suelta:** diagnóstico en pocas líneas (qué falla · causa probable `propuesta`) y el prompt corregido en un único bloque de código, en inglés (REGLAS §9). Junto a él, lo que se protege y qué mirar en el siguiente resultado (REVISAR DESPUÉS).
- **Proyecto:** **Guarda el prompt en `prompts.md` antes de responder** (REGLAS §9) y di en qué entrada queda; si no está escrito ahí, no está entregado. lo anterior y el registro del intento: qué se cambió, por qué y qué resultó. Estado `prompt escrito`, nunca «arreglado» hasta que el usuario confirme el resultado.
- **Cierre:** línea aparte con el estado y el siguiente paso con la frase exacta para pegar.

## Se detiene y pregunta si
- falta el prompt usado o una descripción o imagen del resultado;
- no dice en qué segundo (vídeo) o en qué elemento falla y eso cambia el diagnóstico: pide solo el dato que falta, con una frase corta para contestar («a los 3 s, la mano derecha de M1 atraviesa la llave»);
- hay varios fallos y el usuario no dice cuál prioriza;
- el arreglo exige cambiar el desglose o las referencias aprobadas y no está autorizado.
Máximo 3 preguntas, agrupadas.

## No hace
No genera, no juzga un vídeo que no ha visto, no declara una causa como hecho ni un resultado como arreglado, no cambia varias cosas a la vez, no elige modelo ni inventa límites, no hereda prohibiciones universales de terceros (REGLAS §11).

## Revisión (REGLAS §10, más)
- el fallo lleva su segundo y su elemento, o consta que faltan y se pidieron;
- el fallo descrito es observable y lo que funciona queda protegido;
- las causas figuran como hipótesis, con la frase o referencia que las sugiere;
- un solo cambio, registrado;
- el prompt corregido no contradice el desglose ni las referencias aprobadas;
- no se presenta ningún resultado como visto sin haberlo visto.
