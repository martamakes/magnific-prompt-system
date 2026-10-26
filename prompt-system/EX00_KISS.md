# EX00_KISS — primer ejercicio (Keep It Simple, Stupid)

Ejercicio inicial obligatorio. Se hace antes que cualquier otro. Objetivo: aprender lo básico de Magnific con lo mínimo. **No se crean 25 personajes: se crea uno.**

Parte de lo que ya has generado: no empiezas de cero, **simplificas**.

## Límites (obligatorios)

| Qué | Límite |
|---|---|
| Personajes | **1** |
| Localizaciones | **1** |
| Objetos | **1** |
| Diálogo | **ninguno** |
| Sincronía labial (lip sync) | **ninguna**: nadie habla ni mueve la boca para hablar |

Nada fuera de la tabla cuenta. Si tu material tiene más, **eliges uno de cada** y dejas el resto fuera. Un segundo personaje, otra localización u otro objeto = ejercicio no válido.

## Qué haces

1. **Elige de lo que ya tienes** un personaje, una localización y un objeto. Anota cuál has elegido y por qué (una línea cada uno). Lo demás queda descartado.
2. **Pasa la idea por el sistema** con esa selección: `Oye Amenábar, quiero empezar un proyecto nuevo.` y pega tu material elegido. Responde «sin audio» cuando pregunte por el audio.
3. **Referencias:** una imagen aprobada del personaje, una de la localización y una del objeto (o foto real del objeto, si la tienes: no se genera otra).
4. **Una acción simple** con ese personaje, ese lugar y ese objeto, sin hablar.
5. **Imagen inicial del plano** (`shot-composer`): una sola, con las tres referencias aprobadas. Se aprueba antes de gastar en vídeo.
6. **Clip del plano** (`video-prompt`): un plano, la acción simple y **un movimiento de cámara** con su motivo en una frase (qué aporta; si no lo sabes, cámara fija). Sin hablar.
7. **Aprueba cada paso antes de gastar en el siguiente** (un prompt escrito no es una imagen aprobada ni un clip).

## Qué entregas

- Las tres elecciones, con una línea de motivo cada una.
- Las tres referencias aprobadas.
- La imagen inicial aprobada del plano.
- El clip de tu acción simple, con una línea: movimiento de cámara elegido y qué aporta.
- Una nota breve de lo que salió distinto de lo pedido (sirve para mejorar las skills; no puntúa).

## Valores del ejercicio (`propuesta`, sin aprobar)

Hasta que los apruebes o cambies, no cuentan como decididos:
- **Planos:** 1.
- **Duración:** corta, dentro del máximo del modelo que uses (`MODELOS.md`; si ese dato está pendiente de verificar, se dice y se elige tú).
- **Resultado final:** un clip, con su imagen inicial aprobada.
- **Criterio de aprobación:** el clip muestra la acción pedida con el mismo personaje, lugar y objeto que las referencias; la cámara hace lo que dijiste (o queda fija si lo dijiste); nadie habla. Si falla, se diagnostica con `repair` antes de regenerar.

## Ejemplo de prompting

*Ejemplo ilustrativo con un caso inventado (una ceramista, su taller y una taza). No está probado en la app: sirve para ver la forma, no para copiar el contenido. Los prompts pegables van en inglés y las explicaciones en tu idioma (`REGLAS.md` §9).*

**Reglas de forma:** describe lo que se ve (gesto observable, no interpretación), sin nadie hablando, sin texto en pantalla, y di qué aporta cada referencia.

**1. Personaje** (hoja de vistas):
```
Character reference sheet on a plain light grey background: the same adult woman shown in four views (front, left profile, right profile, back), full body, neutral standing pose, arms relaxed. Short dark hair tied back, olive skin, dark green apron over a white shirt, grey trousers, brown boots. Even soft light.
```

**2. Localización** (vista general vacía):
```
Wide view of an empty ceramic workshop in the morning. Natural light from a large window on the left, a long wooden workbench in the centre, shelves with unglazed pots on the right wall, a potter's wheel at the back. Warm, calm light. No people.
```

**3. Objeto** (si no tienes foto real):
```
Product shot of an ochre glazed ceramic cup with a single handle, on a plain light background, soft side light, three-quarter view.
```

**4. Imagen inicial del plano** (estado de **inicio**, no el resultado de la acción):
```
Natural photograph, horizontal 16:9 medium shot, fixed camera, in the ceramic workshop. The woman stands behind the workbench, hands resting on its edge, looking down at the ochre cup on the bench in front of her. Morning window light from the left. She is the only person in the frame.
```
Referencias que se suben a Magnific (en este orden):
1. Hoja de vistas del personaje: **aporta** la identidad; **se ignora** el fondo gris.
2. Vista del taller: **aporta** el lugar y la luz; **se ignora** que esté vacío.
3. Taza: **aporta** forma y esmalte; **se ignora** el fondo.

**5. Clip** (solo lo que **cambia**: acción y cámara; no se repite lo que ya está en la imagen). Movimiento de cámara elegido: acercamiento lento. Motivo: da peso al momento en que coge la taza.
```
Slow push-in toward the woman, ending in a medium close-up. 00:00 She looks at the cup. 00:02 She picks it up with her right hand and lifts it to chest height. The window light stays constant. No music. No subtitles.
```
Ajustes: 4 s (`propuesta`), 16:9. El cierre «No music. No subtitles.» es el de `video-prompt` para proyectos sin audio o con audio externo (handbook de Magnific, `documentada`).

## Comprobación del profesor (solo texto)

- [ ] Exactamente 1 personaje, 1 localización, 1 objeto.
- [ ] Ningún diálogo ni boca hablando en ningún prompt.
- [ ] El material parte de lo ya generado y se simplificó.
- [ ] Cada imagen se aprobó antes del siguiente paso.
- [ ] Un solo plano y un solo movimiento de cámara (o cámara fija), con su motivo en una frase.
- [ ] El clip se pidió con imagen inicial aprobada.

Es una comprobación del texto y de lo entregado; no valida la calidad visual.
