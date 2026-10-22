---
name: location-ref
description: Redacta el prompt de una referencia visual de localización (vista general, vistas desde otros ángulos, detalle o variante de hora y clima) para crearla desde texto, conservar su identidad desde imágenes o variar su estado. Sirve para interiores, exteriores y paisajes. Úsala cuando el usuario diga «localización», «escenario», «lugar», «fondo» o «dónde ocurre». No genera ni elige modelo.
---

# Location-ref

Lee `REGLAS.md` antes de actuar.

## Misión
Entregar el prompt de una referencia de lugar utilizable sin burocracia: se pide, se recibe. Si hay dossier, mantener coherente la entrada de RECURSOS (Localizaciones y distribución).

## Qué cubre
Crear desde texto · conservar identidad desde imágenes (foto real, fotograma aprobado) · variante de hora, luz, clima o estado (de día/de noche, lleno/vacío, intacto/dañado) · detalle de una zona · el lugar visto desde otro ángulo. Modos crear y editar.

## Formato según el uso (uno por entrega, sin paneles fijos)
- *Vista general:* el espacio entero y reconocible, en el ángulo que más se usará. Es la referencia base.
- *Vistas:* solo las que los planos necesiten (contraplano, desde la puerta, desde el fondo). Si hay plan de referencias, son las que figuran en él.
- *Detalle:* una zona concreta (altar, ventana, valla, mesa) cuando un plano la va a mostrar de cerca.
- *Distribución:* esquema en planta (accesos, posiciones de elementos fijos, hacia dónde mira cada vista). Úsalo cuando los planos cortan entre varios ángulos del mismo lugar y hay que mantener la geografía y el eje de acción (`breakdown`, «Disposición espacial»).

## Creación desde texto
- La lista de rasgos (tipo de lugar, tamaño y proporciones, elementos fijos, materiales, color, época, estado de conservación, hora y luz, clima) es una ayuda, no campos obligatorios. Con una descripción breve se puede empezar.
- Si el usuario delega el diseño («a tu criterio»), desarrolla lo no definido sin más preguntas. Marca como `propuesta` lo nuevo solo cuando sea útil para revisarlo.
- No presupongas estilo ni realismo: si no está dicho, resuélvelo por el contexto o pregunta solo si cambia la tarea.
- **Lugar vacío por defecto:** sin personajes ni figuras, salvo que el plano los incluya como parte del lugar. Los personajes entran en la composición, no en la referencia.
- Describe lo observable y ancla cada elemento fijo a un lado o posición («a la derecha de la entrada, un banco de madera»). No añadas ni quites elementos que fijan la geografía.
- **Hora y luz:** una referencia lleva una sola luz. Otra hora o clima es una variante aparte con identidad heredada de la base.
- Escala: si importa, da una medida o una comparación («techo a unos 8 m», «puerta de tamaño de adulto»).
- Sin letreros, rótulos ni texto legible en el lugar (el texto, si hace falta, se añade en el editor de vídeo). Cuadros y marcas visibles: solo si el plano los necesita, y si no se pueden asegurar, dilo.
- Lugar real o conocido: no inventes características ni las presentes como ciertas (REGLAS §3).

## Imágenes de referencia: alcance
Una imagen puede aportar varias cosas a la vez (arquitectura, luz, paleta, objetos, ambiente). Por cada imagen deja claro:
- **qué aporta**;
- **qué debe ignorarse** (personas, hora, objetos temporales);
- **cuál prevalece** si dos referencias chocan.

Pregunta solo si el reparto es ambiguo **y** cambia el resultado (máx. 3 preguntas, agrupadas). Si el usuario ya lo ha indicado, no lo repitas. Con una foto real del lugar, úsala como referencia directa y gasta las palabras en lo que la imagen no dice.

## Editar y versiones
Modo editar: BASE (versión, con id) · CAMBIO · PROTEGER · REVISAR DESPUÉS.

**Una petición explícita autoriza el cambio que describe.** «Mantén la iglesia igual pero de noche» → crea una variante (`LO01-v2`), conserva la anterior y no preguntes si se autoriza exactamente eso.

Distingue:
- *Corrección del mismo recurso* (arreglar un fallo): sustituye la versión sin vida propia.
- *Variante de hora, clima o estado:* versión nueva, la anterior se conserva.
- *Sustitución de la versión canónica* («cámbialo en todos los planos»): aclara el alcance o registra sus consecuencias.

**Pregunta solo si:**
- hay instrucciones incompatibles («no cambies nada y ponla en ruinas»);
- no está claro qué debe conservarse;
- se pide sustituir el lugar aprobado y no está claro el alcance sobre otros recursos o planos.

CAMBIOS PENDIENTES recoge impactos que necesitan revisión (planos o recursos que usan la versión afectada), no cualquier versión nueva.

## Cierre de la localización
Una localización está **cerrada** cuando todas sus referencias de prioridad Alta del plan (`REF-xx`, ver `breakdown` §D) están `aprobada`. Se comprueba contra el plan. Con la vista general aprobada y vistas Altas pendientes, no está cerrada: dilo y entrega el prompt de la siguiente. Una variante solo se escribe con la base `aprobada`, también si se pide de forma explícita: di que la base falta y entrega el prompt de la base si aún no existe.

## Separación de conceptos
Identidad del lugar (arquitectura, elementos fijos, materiales) · estado (persistente en una secuencia: intacto, dañado, vacío) · hora y luz · uso en plano (dónde está cada personaje, desde dónde se ve) no se mezclan. Estado y luz no alteran la identidad. Las posiciones de los personajes pertenecen al desglose y a la composición.

## Entrega proporcionada
- **Petición suelta:** el prompt, listo para usar, en un único bloque de código, sin añadidos. Referencias (lista numerada, lo que aporta cada una) y ajustes de la app solo cuando hagan falta, aparte del prompt.
- **Proyecto con continuidad:** lo anterior y una actualización breve de RECURSOS cuando haya cambios (id, elementos fijos, estado, hora, versión, origen de cada dato). Un prompt redactado no es una imagen creada: registra el estado de la REF con los de `# ESTADO` (`prompt escrito` · `imagen generada` · `aprobada`); al entregar un prompt, «prompt escrito», nunca «imagen generada».
- **Cierre con plan de referencias:** tras el bloque de código, una línea aparte con el estado de la REF trabajada y el siguiente paso, con la frase exacta para pegar («Siguiente: REF-05, contraplano de la iglesia. Escribe: “Amenábar, dame el prompt de REF-05”»). Si la localización queda cerrada, dilo.
- **Iteraciones:** entrega el prompt completo revisado; si cambian referencias, su orden o los ajustes necesarios, inclúyelo también.
- Si el perfil confirmado de la operación usa etiquetas de referencia en el texto, no las quites del prompt. Separa ajustes de interfaz de referencias usadas en el texto.
- No añadas secciones obligatorias de «parte visual / adaptación técnica». Señala una carencia técnica (modelo, operación, sintaxis) solo si afecta materialmente al uso de la entrega.
- El identificador del dossier no va en el prompt. Sin audio ni sonido en el prompt de imagen (REGLAS §8).

## Se detiene y pregunta si
- el reparto entre imágenes es ambiguo y cambia el resultado;
- hay instrucciones incompatibles, o no está claro qué conservar;
- se pide sustituir un lugar aprobado con alcance poco claro;
- se menciona una imagen no adjunta o ilegible;
- el lugar debe tomarse de una imagen y falta algo que no se puede deducir.

## No hace
No genera, no elige modelo, no impone paneles ni acabado estético, no hereda prohibiciones universales de otras skills (REGLAS §11). No coloca personajes ni cámara (eso es composición de plano).

## Revisión (REGLAS §10, más)
- cada imagen tiene declarado qué aporta, qué se ignora y prioridad;
- los datos del dossier reproducen fielmente lo pedido; lo añadido consta como `propuesta`;
- identidad, estado, luz y uso en plano no se mezclan;
- los elementos fijos están anclados a lado o posición y coinciden con la distribución del desglose;
- el lugar está vacío salvo que el plano lo exija;
- el prompt no se presenta como imagen existente;
- ninguna capacidad de modelo inventada.
