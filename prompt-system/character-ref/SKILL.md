---
name: character-ref
description: Redacta el prompt de una referencia visual de personaje (retrato, cuerpo entero, vistas o expresión) para crearlo desde texto, conservar su identidad desde imágenes, combinarla con vestuario, variar su estado narrativo o crear una referencia de expresión, incluida la hoja de vistas (character sheet). Úsala cuando el usuario diga «personaje», «character sheet», «hoja de personaje», «vistas» o «cómo es [nombre]». No genera ni elige modelo.
---

# Character-ref

Lee `REGLAS.md` antes de actuar.

## Misión
Entregar el prompt de una referencia de personaje utilizable sin burocracia: se pide, se recibe. Si hay dossier, mantener coherente la entrada de RECURSOS.

## Qué cubre
Crear desde texto · conservar identidad desde imágenes · identidad + vestuario · variante de estado narrativo o de apariencia · referencia de expresión. Modos crear y editar.

## Formato según el uso (uno por entrega, sin paneles fijos)
- *Retrato:* rostro para planos cercanos o medios.
- *Cuerpo entero:* complexión, postura, vestuario.
- *Vistas:* solo las que hagan falta (espalda, perfil…) para ver construcción de ropa, peinado o rasgos. Si hay plan de referencias, las vistas son las que figuran en él; si no, las que pidan los planos.
- *Hoja de vistas:* una sola imagen con varias vistas de la misma persona (frente, perfil, espaldas), misma altura, mismo vestuario, fondo liso. Úsala cuando el personaje necesita 2 o más vistas. Indica el sentido del perfil («mirando a la izquierda») y exige coherencia de rostro, peinado y ropa entre vistas.
  Reglas de la hoja (criterio de trabajo; que el modelo las cumpla está sin comprobar):
  - *Vistas de cuerpo:* todas de **cuerpo entero**, de la cabeza a los pies con el calzado, a la misma altura y escala y sin recortes en el borde. Si no se quiere cuerpo entero, dilo en el prompt.
  - *Rasgos fijos, una sola vez y concretos:* peinado (recogido o suelto, con o sin flequillo, altura del moño), color, ropa y complementos se describen una vez y sin alternativas. Un rasgo ambiguo puede salir distinto en cada panel.
  - *Lo que el cuerpo entero exige y no está definido* (calzado, pantalón…): lo decide la skill y consta como `propuesta`.
  - *Paneles de detalle* (rostro, manos): indica el encuadre y qué no entra («sin cara», «sin joyas»), para que no se cuele en ellos lo que no pertenece.
  - *Orden y sentido:* fila de vistas de cuerpo y, aparte, la de detalles; sentido del perfil indicado; paneles separados, sin solaparse.
  - *Solo las vistas que pida el plan.* Si el usuario aporta una hoja de ejemplo con más vistas, señala cuáles lleva el ejemplo y cuáles pide el plan, y deja que elija; no las añadas por completar el formato.
  - *Muchos paneles:* si la hoja lleva cinco o más y no sale bien, ofrece partirla en dos (cuerpo entero · detalles), con la primera aprobada como referencia de identidad de la segunda. Es una `propuesta` de trabajo.
  - *Identidad entre intentos:* cada generación puede dar una persona distinta. Para repetir una hoja, usa como referencia la imagen que ya acierta, declarando qué aporta (rostro, peinado) y qué se ignora (encuadre, paneles).
- *Hoja de vestuario:* opcional; una sola imagen con la ropa del personaje, para cuando el vestuario importa y debe repetirse igual en varios planos. Parte de la hoja de vistas del personaje (`aprobada`) y hereda su identidad. Contiene, solo lo que la ropa necesita:
  - las vistas del personaje vestido (frente, perfil, espalda; primer plano del cuello y la cara si el cuello o el pelo importan);
  - muestras de tejido de cada prenda y detalles que la distinguen (bolsillo, botón, cuello, calzado…);
  - paleta de colores de la ropa;
  - Sin títulos, etiquetas ni anotaciones dentro de la imagen, salvo petición explícita del usuario. Identifica las vistas, muestras y detalles mediante su disposición y descríbelos fuera del prompt, cuando haga falta.
  Cada prenda con tipo, color, tejido y corte; lo que el usuario no dice, `propuesta`. Si hay foto de una prenda, declara qué aporta y qué se ignora. Es el formato de un ejemplo aportado por el usuario; que el modelo lo reproduzca fielmente está sin comprobar.
- *Expresión:* una configuración facial concreta que se usará como referencia. Describe lo visible necesario (cejas, párpados, boca, mandíbula); sin ficha emocional completa.

## Creación desde texto
- La lista de rasgos (constitución, rostro, ojos, cejas, nariz, boca, cabello, piel, edad aparente, rasgos distintivos) es una ayuda, no campos obligatorios. Con una descripción breve se puede empezar.
- Si el usuario delega el diseño («a tu criterio», «el resto como veas»), desarrolla lo no definido sin más preguntas. Marca como `propuesta` lo nuevo solo cuando sea útil para revisarlo.
- No presupongas fotorealismo: si el estilo no está dicho, resuélvelo por el contexto o pregunta solo si cambia la tarea.
- Describe lo observable. No añadas ni quites imperfecciones, cicatrices o texturas salvo que estén pedidas o en la referencia; ancla marcas fijas a un punto anatómico (lado, posición). Adulto cuando proceda.
- Fondo y luz neutros y parejos son un **punto de partida** para una referencia reutilizable (que no herede la luz de una escena), no una regla. Procede de castkit; eficacia pendiente de verificar.

## Imágenes de referencia: alcance
Una imagen puede aportar varias cosas a la vez (identidad, cabello, vestuario, pose…). Por cada imagen deja claro:
- **qué aporta**;
- **qué debe ignorarse**;
- **cuál prevalece** si dos referencias chocan.

Pregunta solo si el reparto es ambiguo **y** cambia el resultado (máx. 3 preguntas, agrupadas). Si el usuario ya lo ha indicado, no lo repitas. Con imagen que ya lleva la identidad, usa un asa visual corta y gasta las palabras en lo que la imagen no dice.
Si hay un cambio de material («solo el corte, no el acabado»), dilo. Texto o gráficos en prendas: exactos, con forma, color y colocación.

## Editar y versiones
Modo editar: BASE (versión, con id) · CAMBIO · PROTEGER · REVISAR DESPUÉS.

**Una petición explícita autoriza el cambio que describe.** «Mantén su rostro y hazla rubia con flequillo» → crea una variante con ese cambio (`PJ01-v2`), conserva la versión anterior y no preguntes si se autoriza exactamente eso. Pero la variante solo se escribe con la base `aprobada`: si no lo está, dilo y entrega el prompt de la base.

Distingue:
- *Corrección del mismo recurso* (arreglar un fallo): sustituye la versión sin vida propia.
- *Variante de apariencia o estado*: versión nueva, la anterior se conserva.
- *Sustitución de la versión canónica* («cámbiala en todos los planos»): aclara el alcance o registra sus consecuencias.

**Pregunta solo si:**
- hay instrucciones incompatibles («no cambies el cabello y hazla rubia»);
- no está claro qué debe conservarse;
- se pide sustituir la identidad aprobada y no está claro el alcance sobre otros recursos o planos.

CAMBIOS PENDIENTES recoge impactos que necesitan revisión (planos o recursos que usan la versión afectada), no cualquier versión nueva.

## Cierre del personaje
Un personaje está **cerrado** cuando todas sus referencias de prioridad Alta del plan (`REF-xx`, ver `breakdown` §D) están `aprobada`. Se comprueba contra el plan, no por criterio propio.
- Con una sola imagen aprobada y vistas Altas pendientes, el personaje **no está cerrado**: dilo y entrega el prompt de la siguiente vista.
- Si no hay plan de referencias (proyecto suelto), pregunta una vez qué vistas necesitan los planos o propón las mínimas según el desglose.
- Estado y expresión no cierran la identidad: una variante (`PJ01-v2`) hereda la base y no se hace hasta que la base esté `aprobada`.

## Separación de conceptos
Identidad · estado narrativo (persistente) · expresión · actuación no se mezclan (REGLAS §8). Estado y expresión no alteran la identidad.

## Entrega proporcionada
- **Petición suelta:** el prompt, listo para usar, en un único bloque de código. Referencias (lista numerada, lo que aporta cada una) y ajustes de la app solo cuando hagan falta, aparte del prompt.
- **Proyecto con continuidad:** lo anterior y una actualización breve de RECURSOS cuando haya cambios (id, rasgos fijos, estado, versión, origen de cada dato). Un prompt redactado no es una imagen creada: registra el estado de la REF con los estados de `# ESTADO` (`prompt escrito` · `imagen generada` · `aprobada`); al entregar un prompt, «prompt escrito», nunca «imagen generada».
- No añadas secciones obligatorias de «parte visual / adaptación técnica». Señala una carencia técnica (modelo, operación, sintaxis) solo si afecta materialmente al uso de la entrega.
- **Iteraciones:** entrega el prompt completo revisado; si cambian referencias, su orden o los ajustes necesarios, inclúyelo también.
- Si el perfil confirmado de la operación usa etiquetas de referencia en el texto, no las quites del prompt. Separa ajustes de interfaz de referencias usadas en el texto.
- Nombres de personas reales fuera; el identificador del dossier no va en el prompt.
- **Cierre con plan de referencias:** tras el bloque de código, una línea aparte con el estado de la REF trabajada y el siguiente paso, con la frase exacta para pegar («Siguiente: REF-03, perfil de Isabel. Escribe: “Amenábar, dame el prompt de REF-03”»). Si el personaje queda cerrado, dilo. En una petición suelta no se añade nada.

## Se detiene y pregunta si
- el reparto entre imágenes es ambiguo y cambia el resultado;
- hay instrucciones incompatibles, o no está claro qué conservar;
- se pide sustituir una identidad aprobada con alcance poco claro;
- se menciona una imagen no adjunta o ilegible;
- la identidad debe tomarse de una imagen y falta algo que no se puede deducir;
- la imagen parece una persona real ajena al proyecto: se necesita autorización para usarla (no la nombres).

## No hace
No genera, no elige modelo, no impone paneles (salvo la hoja de vistas o la de vestuario cuando el plan las pide), fichas emocionales ni acabado estético, no hereda prohibiciones universales de otras skills (REGLAS §11).

## Revisión (REGLAS §10, más)
- cada imagen tiene declarado qué aporta, qué se ignora y prioridad;
- los datos del dossier reproducen fielmente lo pedido (sin endurecer «algo hundidos» en «hundidos»); lo añadido consta como `propuesta`;
- identidad, estado y expresión no se mezclan;
- en una hoja de vistas: cuerpo entero, rasgos fijos descritos una vez, lo añadido como `propuesta` y solo las vistas del plan;
- el prompt no se presenta como imagen existente;
- ninguna capacidad de modelo inventada.
