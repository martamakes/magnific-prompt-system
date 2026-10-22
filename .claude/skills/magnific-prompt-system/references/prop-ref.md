# Prop-ref

Lee `references/reglas.md` antes de actuar.

## Misión
Entregar el prompt de una referencia de objeto utilizable sin burocracia: se pide, se recibe. Si hay dossier, mantener coherente la entrada de RECURSOS (Props y estados).

## Qué cubre
Crear desde texto · conservar identidad desde imágenes · variante de estado (lleno/vacío, nuevo/gastado, cerrado/abierto, roto…) · detalle de una parte · objeto con escala respecto a una mano o un personaje. Modos crear y editar.

## Formato según el uso (uno por entrega, sin paneles fijos)
- *Vista general:* el objeto completo, reconocible, en la orientación que más se usará.
- *Vistas:* solo las que hagan falta (cara oculta, base, interior, cierre…) para ver su construcción.
- *Detalle:* una parte concreta (asa, etiqueta, grieta, mecanismo) cuando el plano la va a mostrar de cerca.
- *Escala:* el objeto junto a algo que fije su tamaño (mano, mesa, otro prop), solo si el tamaño importa en el plano.

## Creación desde texto
- La lista de rasgos (tipo y función, forma y proporciones, tamaño aproximado, material, color, acabado, desgaste, marcas distintivas, partes móviles) es una ayuda, no campos obligatorios. Con una descripción breve se puede empezar.
- Si el usuario delega el diseño («a tu criterio»), desarrolla lo no definido sin más preguntas. Marca como `propuesta` lo nuevo solo cuando sea útil para revisarlo.
- No presupongas estilo ni realismo: si no está dicho, resuélvelo por el contexto o pregunta solo si cambia la tarea.
- Describe lo observable. No añadas ni quites desgaste, golpes, manchas u holguras salvo que estén pedidos o en la referencia; ancla marcas fijas a un punto del objeto (lado, posición, parte).
- Tamaño: si importa, da una medida o una comparación con algo conocido; un objeto sin escala se resuelve a ojo.
- Fondo y luz neutros y parejos son un **punto de partida** para una referencia reutilizable (que no herede la luz de una escena), no una regla. Eficacia sin verificar.

## Texto, logotipos y productos reales
- Texto o gráficos en el objeto (etiqueta, inscripción, número): exactos, con forma, color y colocación. Si no se pueden asegurar, dilo en lugar de prometerlos.
- Producto o marca real: no inventes características ni presentes como cierto lo que no consta (REGLAS §3). Sin marca real salvo que el encargo la aporte.

## Imágenes de referencia: alcance
Una imagen puede aportar varias cosas a la vez (forma, material, color, estado, escala…). Por cada imagen deja claro:
- **qué aporta**;
- **qué debe ignorarse** (fondo, mano que lo sostiene, otros objetos);
- **cuál prevalece** si dos referencias chocan.

Pregunta solo si el reparto es ambiguo **y** cambia el resultado (máx. 3 preguntas, agrupadas). Si el usuario ya lo ha indicado, no lo repitas. Con una imagen que ya lleva la identidad, usa un asa visual corta y gasta las palabras en lo que la imagen no dice.

## Editar y versiones
Modo editar: BASE (versión, con id) · CAMBIO · PROTEGER · REVISAR DESPUÉS.

**Una petición explícita autoriza el cambio que describe.** «Mantén la taza igual pero con el asa rota» → crea una variante con ese cambio (`OB01-v2`), conserva la versión anterior y no preguntes si se autoriza exactamente eso. Pero la variante solo se escribe con la base `aprobada`: si no lo está, dilo y entrega el prompt de la base.

Distingue:
- *Corrección del mismo recurso* (arreglar un fallo): sustituye la versión sin vida propia.
- *Variante de estado o apariencia:* versión nueva, la anterior se conserva.
- *Sustitución de la versión canónica* («cámbialo en todos los planos»): aclara el alcance o registra sus consecuencias.

**Pregunta solo si:**
- hay instrucciones incompatibles («no cambies el material y hazlo de cristal»);
- no está claro qué debe conservarse;
- se pide sustituir el diseño aprobado y no está claro el alcance sobre otros recursos o planos.

CAMBIOS PENDIENTES recoge impactos que necesitan revisión (planos o recursos que usan la versión afectada), no cualquier versión nueva.

## Separación de conceptos
Identidad del objeto (forma, material, marcas fijas) · estado (persistente en una secuencia: lleno, roto, sucio) · uso en plano (quién lo sostiene, con qué mano, dónde queda) no se mezclan. Estado y uso no alteran la identidad. La posición y la mano pertenecen al desglose y a la composición, no a la referencia, salvo que sea una referencia de escala.

## Entrega proporcionada
- **Petición suelta:** el prompt, listo para usar, en un único bloque de código. Referencias (lista numerada, lo que aporta cada una) y ajustes de la app solo cuando hagan falta, aparte del prompt.
- **Proyecto con continuidad:** lo anterior y una actualización breve de RECURSOS cuando haya cambios (id, rasgos fijos, estado, versión, origen de cada dato). Un prompt redactado no es una imagen creada: registra el estado de la REF con los de `# ESTADO` (`prompt escrito` · `imagen generada` · `aprobada`); al entregar un prompt, «prompt escrito», nunca «imagen generada».
- No añadas secciones obligatorias de «parte visual / adaptación técnica». Señala una carencia técnica (modelo, operación, sintaxis) solo si afecta materialmente al uso de la entrega.
- **Iteraciones:** entrega el prompt completo revisado; si cambian referencias, su orden o los ajustes necesarios, inclúyelo también.
- Si el perfil confirmado de la operación usa etiquetas de referencia en el texto, no las quites del prompt. Separa ajustes de interfaz de referencias usadas en el texto.
- El identificador del dossier no va en el prompt.
- **Petición suelta:** el prompt va solo, sin añadidos. **Proyecto con plan de referencias:** tras el bloque de código, una línea aparte con el estado de la REF (`prompt escrito`, nunca `imagen generada`) y el siguiente paso con la frase exacta para pegar. Si el usuario tiene foto real del objeto, indícalo: se usa como referencia directa, no se genera.

## Se detiene y pregunta si
- el reparto entre imágenes es ambiguo y cambia el resultado;
- hay instrucciones incompatibles, o no está claro qué conservar;
- se pide sustituir un diseño aprobado con alcance poco claro;
- se menciona una imagen no adjunta o ilegible;
- el tamaño o el texto del objeto son críticos para el plano y faltan.

## No hace
No genera, no elige modelo, no impone paneles ni acabado estético, no hereda prohibiciones universales de otras skills (REGLAS §11). No coloca el objeto en la escena (eso es composición de plano).

## Revisión (REGLAS §10, más)
- cada imagen tiene declarado qué aporta, qué se ignora y prioridad;
- los datos del dossier reproducen fielmente lo pedido (sin endurecer «algo gastado» en «muy gastado»); lo añadido consta como `propuesta`;
- identidad, estado y uso en plano no se mezclan;
- el texto o los gráficos del objeto son los pedidos, o se avisa de que no están asegurados;
- el prompt no se presenta como imagen existente;
- ninguna capacidad de modelo inventada.
