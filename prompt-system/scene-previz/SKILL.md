---
name: scene-previz
description: Redacta la especificación de una previsualización 3D de un plano o escena (volúmenes y posiciones, cámaras, qué se quiere comprobar) para que el usuario la monte a mano o con la herramienta que prefiera. Úsala cuando el usuario diga «previsualiza el plano», «previz», «blocking 3D», «prueba de cámara» o «comprueba la geografía de la escena». No ejecuta ninguna herramienta ni genera archivos.
---

# Scene-previz

Lee `REGLAS.md` antes de actuar.

## Misión
Escribir la **especificación** de una previsualización sencilla: qué se monta, dónde, con qué cámaras y qué se quiere comprobar. La monta el usuario (a mano o con la herramienta 3D que elija). Esta skill no ejecuta ni controla ninguna herramienta (REGLAS §1, §5).

## Cuándo se usa
Solo si resuelve una **incertidumbre concreta** que el texto no resuelve: geografía de un espacio, posiciones relativas, eje de acción entre planos, recorrido de cámara, escala entre objetos. Que exista una herramienta 3D no es motivo. Si el desglose ya deja claro lo que se quiere comprobar, no se hace previz.

Si no hay incertidumbre que nombrar, dilo y no escribas la especificación.

## Entradas
- Plano(s) o escena del desglose, con disposición espacial y eje de acción si constan.
- La incertidumbre a resolver, en una frase. Si el usuario no la dice, se pregunta.
- Referencias aprobadas de localización, personajes y objetos, solo para escala y proporciones.
- Herramienta o destino de la previsualización, si el usuario lo dice; si no, la especificación va en forma común.

## Qué contiene la especificación
1. **Qué se comprueba** (una o dos frases) y qué decisión depende de ello.
2. **Escala y unidades.** Una unidad de medida y una altura de referencia (por ejemplo, la de un personaje). Si no constan, `propuesta`.
3. **Volúmenes.** Formas simples (cajas, cilindros, siluetas) con nombre, tamaño aproximado y posición respecto a un origen. Sin detalle estético: es geografía, no aspecto.
4. **Posiciones iniciales y recorridos** de lo que se mueve: desde dónde y hacia dónde, incluido lo que queda fuera de cuadro (no visible ≠ inexistente).
5. **Cámaras.** Una por línea: identificador, plano al que corresponde, posición, hacia dónde apunta, tipo de plano y movimiento si lo hay. Respeta el eje de acción del desglose.
6. **Qué mirar en el resultado**, como lista de comprobaciones: qué se ve en cuadro, qué queda fuera, si los cortes respetan el eje, si la escala es creíble.

## Escena preparada, referencia aprobada y plano final
Tres cosas distintas; no se confunden ni se cuentan como hechas por existir una anterior:
- **Escena preparada:** la previsualización montada. Resuelve una duda de geografía o cámara. No es una imagen aprobada.
- **Referencia aprobada:** una captura de la previz que el usuario ha revisado y decide usar como imagen de referencia. Pasa por el ciclo normal de estados (`propuesta` → `prompt escrito` → `imagen generada` → `aprobada`).
- **Plano final:** lo que se genera con el modelo. Que el modelo respete la geometría de una referencia no está garantizado; **pendiente de verificar** con generaciones reales.

## Límites
- No cambia decisiones del desglose aprobado. Si la previz muestra que algo no funciona, propone el cambio como `propuesta` y lo deja en manos del usuario.
- No sustituye al guion ni al desglose: apoya una duda concreta.
- No inventa capacidades de ninguna herramienta 3D ni de los modelos. Lo que no consta se marca *pendiente de verificar* (REGLAS §3).
- Usar una captura como referencia de vídeo o imagen depende de los límites del modelo (`MODELOS.md`).
- Si una herramienta ejecuta código o acepta órdenes automáticas, esa configuración y su riesgo son del usuario y quedan fuera de esta skill.

## Prueba mínima (propuesta)
Para validar el método antes de usarlo en un proyecto real, `propuesta` y sin probar: dos figuras sencillas, una mesa y dos cámaras. Se comprueba si las capturas dejan ver la geografía y si un cambio de cámara respeta el eje. Sirve para ver si el método aporta algo; no demuestra nada sobre el modelo de generación.

## Entrega proporcionada
- **Petición suelta:** la especificación, en forma de lista, más la línea de qué se comprueba.
- **Proyecto:** lo anterior, ligado a los planos (`E01-P02`), con el estado `propuesta`.
- **Iteración:** la especificación completa revisada; cambia una cosa por intento y anota qué se cambió.
- **Cierre:** línea aparte con el siguiente paso y la frase exacta para pegar.

## Se detiene y pregunta si
- no hay una incertidumbre concreta que resolver;
- faltan plano(s) o disposición espacial y no se pueden deducir;
- se pide algo que depende de una función de herramienta que no consta.
Máximo 3 preguntas, agrupadas.

## No hace
No ejecuta herramientas ni scripts, no crea archivos 3D, no genera imágenes ni vídeo, no elige herramienta ni modelo, no decide por el usuario si la previz sustituye a una referencia, no monta (`edit-plan`).

## Revisión (REGLAS §10, más)
- hay una incertidumbre nombrada y la especificación la resuelve;
- escala, unidades y origen definidos o marcados `propuesta`;
- posiciones y recorridos coherentes con el desglose, incluido lo fuera de cuadro;
- cada cámara ligada a un plano y al eje;
- distingue escena preparada, referencia aprobada y plano final;
- nada de la herramienta ni del modelo presentado como capacidad garantizada;
- sin términos de ningún proyecto o ejercicio concreto.
