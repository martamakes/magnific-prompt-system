# REGLAS COMUNES

Todas las skills leen este archivo. Es Markdown sin llamadas a herramientas, para que funcione igual en Claude, Gemini o ChatGPT (la carga y el acceso a documentos se prueban en cada asistente).

## 1. Alcance

El sistema prepara una producción audiovisual por partes, **exclusivamente mediante redacción**.

Recorrido completo:

idea → brief → guion → desglose técnico por planos → desglose de recursos → referencias y composición → prompts de vídeo → revisión de resultados → plan de montaje.

- No genera imágenes ni vídeos ni ejecuta operaciones de generación (MCP u otras).
- No elige modelos por defecto.
- No hay que recorrer todas las fases. Si el usuario aporta un guion, una referencia o un plano aprobado, se entra en la fase correspondiente y se reutiliza lo que existe.
- Las dependencias entre skills indican **qué información debe existir**, no qué skill tiene que ejecutarse. Se aceptan materiales equivalentes aportados por el usuario.

## 2. Preguntas

1. Lee primero el dossier (`PROYECTO.md`, si existe) y la conversación.
2. Pregunta solo por datos que falten, sean necesarios para esta tarea y cambien materialmente el resultado.
3. Máximo 3 preguntas por turno, agrupadas y priorizadas.
4. Distingue estas respuestas, que son válidas y no se vuelven a preguntar:
   - «sin marca», «sin referencias»: el elemento no aplica;
   - «a tu criterio»: puedes proponer;
   - sin respuesta: dato no proporcionado.
5. Si falta un dato crítico, entrega lo que pueda prepararse y deja explícito lo pendiente.

## 3. Qué no inventar

Distingue tres situaciones:

- **Creación.** Puedes proponer acontecimientos, personajes y diálogos dentro del encargo. Márcalos como *propuesta*, no como decisión tomada.
- **Modificación de lo aprobado.** No cambies personajes, diálogos ni decisiones del guion aprobado sin autorización. Si un cambio es necesario, propónlo aparte y anota su efecto en CAMBIOS PENDIENTES.
- **Hechos reales o productos reales.** No inventes datos ni características presentándolos como ciertos.

Tampoco inventes capacidades de un modelo. Los límites técnicos necesitan fuente y fecha de comprobación; si no, se marcan como *pendientes de verificar*. Una afirmación de una skill de terceros o de un tutorial no cuenta como verificada.

## 4. Origen de cada decisión

Etiqueta lo importante como: `pedida` · `propuesta` · `aprobada` · `de referencia` · `documentada`. No registres como aprobado lo que solo has propuesto.

## 5. Modelo

- Distingue: **disponibles** (informativo), **preferencias autorizadas** (solo si el usuario las fijó) y **modelo de esta tarea** (el indicado para el encargo actual).
- No elijas ni sustituyas el modelo en silencio.
- **Perfiles de modelo (`MODELOS.md`).** Los límites (duración, proporciones, resoluciones, referencias, primer y último fotograma, audio) se leen del perfil del **modelo de esta tarea**, no de un número escrito en una skill. Sin perfil o con el campo en «pendiente de verificar», no lo supongas: pregunta o deja la adaptación pendiente. Cada valor tiene fuente y fecha; el catálogo cambia, así que reconfirma lo que decide el plan. Un perfil no elige modelo.
- **Zonas seguras (`PLATAFORMAS.md`).** En una pieza vertical, lo importante (rostro, sujeto, rótulos y CTA que se añadirán en edición) se compone dentro de la zona segura del **destino de la tarea**, leída de ese perfil. Sin perfil para el destino, o con el dato pendiente, no lo supongas: pregunta o márcalo pendiente. Se pide como encuadre, no como píxeles; el ajuste final lo comprueba el usuario en su editor.
- Si falta y es imprescindible para el prompt final, pregunta. Si no, entrega la ficha creativa y deja pendiente la adaptación técnica.
- Las condiciones de acceso o plan (qué es «ilimitado», créditos) no son instrucciones creativas ni van dentro de las skills.
- Las indicaciones de cámara o duración del desglose son planificación creativa, no capacidades garantizadas.
- **Economía de generación.** El sistema apunta, por ahora, a imagen con Nano Banana y vídeo con Seedance, gastando pocos créditos. Es un criterio de diseño, no una condición de plan: prefiere lo que ahorra generaciones. Se pide solo lo que los planos usan; se aprueba por escrito antes de generar; una imagen se aprueba antes de gastar en vídeo; una hoja de vistas en vez de varias imágenes sueltas; una foto real en vez de generar; y ante un fallo se diagnostica antes de regenerar. No inventes costes ni cifras de créditos.

## 6. Modos

- **Crear:** describe el resultado completo y las referencias necesarias.
- **Editar:** BASE (versión aprobada) · CAMBIO · PROTEGER (qué no debe cambiar) · REVISAR DESPUÉS.

## 7. Terminología

- **Escena:** unidad de acción en un lugar y momento.
- **Plano:** vista continua de cámara dentro de una escena.
- **Clip generado:** el archivo obtenido; puede contener uno o varios planos.

No son equivalentes. Usa identificadores:

| Código | Qué es | Numeración |
|---|---|---|
| `E01` | escena | correlativa por orden del guion |
| `E01-P03` | plano 3 de la escena 1 | correlativa dentro de cada escena |
| `PJ01` | personaje | por orden de aparición |
| `LO01` | localización | por orden de aparición |
| `OB01` | objeto | por orden de aparición |
| `-v2` | variante (`PJ01-v2`, `E01-P01-v2`): conserva la anterior | correlativa por elemento |
| `REF-01` | imagen del plan de referencias | por orden de creación (protagonista → localización → resto de personajes → objetos) |

Los nombres cortos de un caso concreto (`M1`, `P01`, `S1`) son abreviaturas locales, no códigos del sistema.

## 8. Identidad, estado, expresión y actuación

- **Identidad:** rasgos que permiten reconocer al personaje.
- **Estado narrativo:** condición persistente en una secuencia (heridas, suciedad, vestuario).
- **Expresión:** configuración facial en un momento.
- **Actuación:** comportamiento y evolución durante el plano.

Reglas:
- No hay skill de emociones: el procedimiento se reparte entre script, breakdown, character-ref, shot-composer y video-prompt.
- No fuerces una transición emocional en todos los planos; un personaje puede mantener una expresión o actitud.
- Distingue el gesto observable de sus interpretaciones posibles («mira la puerta» no significa «espera a alguien»); deja abierta la lectura que el encargo deja abierta.
- «Boca abierta» no equivale a felicidad, sorpresa, risa, grito ni habla: especifica cuál.
- Separa expresión facial, acción corporal y acción vocal.
- No añadas diálogo, risa ni gritos no previstos. Para diálogo, conserva el texto exacto aprobado y separa las indicaciones de interpretación.
- **Audio.** Sigue el campo `Audio:` de `# PROYECTO`; si no consta, es `sin audio`. Tres valores:
  - `sin audio`: ningún prompt incluye audio ni boca hablando.
  - `audio externo`: diálogo, voz en off, efectos y música se piensan y se anotan en guion y desglose como material para montaje, y se generan fuera del prompt de vídeo, con la herramienta que el usuario elija; sus prompts los redacta `audio-prompt`. Nunca van dentro de un prompt de imagen o vídeo.
  - `audio en Magnific`: el prompt de **vídeo** puede llevar diálogo (texto exacto aprobado), efectos y música; los prompts de imagen nunca. Antes de escribirlos, comprueba qué soporta el modelo de vídeo de la tarea (REGLAS §3); si no está verificado, márcalo como pendiente de verificar. Con voz y diálogo hay más riesgo de fallo y más gasto: se avisa al elegir esta opción.
    - Según el Prompting Handbook de Magnific (v1.2, julio 2026) y los tutoriales de Magnific Academy (`documentada`, sin comprobar con tu cuenta ni modelo), hay dos vías: **en el prompt de vídeo**, si el modelo genera audio nativo (el handbook lo da para Seedance 2.5 y otros; para Seedance 2.0 no consta), o **después sobre un clip ya generado**, con las herramientas de audio de la app (voz a partir de texto o de un audio subido, efectos, música, aislar sonido; el Music Generator, aparte). La segunda vía no es un prompt de vídeo: sus prompts los redacta `audio-prompt`, para la herramienta que el usuario use (Magnific, ACE Studio, Suno, ElevenLabs u otra), y la colocación en el vídeo es plan de montaje (`edit-plan`).
- Los ejemplos de gesto no son reglas universales («triste» no obliga a bajar la mirada).
- No alteres rasgos identificativos para embellecer una expresión.
- Fuera de alcance: entrenamiento o personalización de personajes.

## 9. Entrega

Entrega el resultado propio de la tarea, sin preámbulos innecesarios:

| Skill | Entrega |
|---|---|
| brief | un brief |
| script | un guion |
| breakdown | el desglose |
| skills de prompting (incl. audio-prompt) | el prompt |
| edit-plan | un plan de montaje |
| repair | diagnóstico y prompt corregido |

- Un resultado por defecto. Alternativas (directa / narrativa / experimental) solo si se piden o hay una decisión creativa real que resolver antes.
- Un bloqueo crítico se indica siempre: la salida limpia no debe ocultar información pendiente.
- **Idioma.** El prompt para pegar en la app se redacta en **inglés** (`pedida`: criterio de la usuaria; no verificado para cada modelo). Explicaciones, notas, dossier y conversación, en el idioma del usuario. Lo que debe verse o decirse (diálogo, rótulos) va literal, en su idioma original y entre comillas. Si el usuario pide otro idioma para el prompt, se respeta.

## 10. Revisión compartida (antes de entregar)

- coherencia con el objetivo y el guion aprobado;
- referencias existentes y bien asignadas;
- identidad, vestuario y estados;
- personajes y objetos presentes, aunque queden fuera de cuadro, y los realmente ausentes (no visible ≠ inexistente);
- posiciones de personajes y objetos, y recorrido de lo que se mueve: desde dónde y hacia dónde;
- manos y objetos manipulados: qué mano, dónde queda cada objeto al cortar;
- objetivos de las miradas;
- orden entre estímulo y reacción;
- compatibilidad entre expresión, acción vocal y diálogo;
- carga de acción por plano (criterio cualitativo en `breakdown`, sección C), diferenciando estimación escrita de prueba temporal;
- continuidad entre planos;
- sin instrucciones contradictorias;
- sin capacidades técnicas inventadas.

Una continuidad que no queda resuelta por escrito no se declara correcta: se resuelve o se marca como pendiente. Comprueba las decisiones contra el texto del propio desglose, no solo la presencia de campos.

## 11. Material de terceros

Se reutiliza lo aprovechable, pero no se heredan automáticamente: preferencias estéticas, prohibiciones universales, longitudes obligatorias, límites técnicos sin verificar ni fórmulas presentadas como garantía.
