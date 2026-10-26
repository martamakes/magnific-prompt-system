# EX01_STORYBOARD — de las referencias al storyboard

Segundo ejercicio. Se hace **después de `EX00_KISS.md`**. Objetivo: pasar de las referencias aprobadas a un **storyboard**: una imagen inicial aprobada por plano, sin gastar todavía en vídeo.

Parte de lo que ya tienes: las referencias aprobadas de personaje, localización y objeto. No se crean referencias nuevas, salvo que un plano lo exija.

## Límites (obligatorios)

| Qué | Límite |
|---|---|
| Planos | **de 3 a 5** |
| Personajes | los que ya tienes aprobados, **máximo 2** |
| Localizaciones | **1** |
| Objetos | **1** |
| Diálogo | **ninguno** |
| Sincronía labial (lip sync) | **ninguna** |
| Vídeo | **ninguno**: este ejercicio termina en imágenes |

Más planos, más personajes o un clip = ejercicio no válido.

## Qué haces

1. **Punto de partida.** Pega tu dossier con las referencias en estado `aprobada` y escribe: `Oye Amenábar, sigue mi proyecto. ¿Qué toca ahora?`. Una referencia de prioridad Alta sin aprobar bloquea el ejercicio: se aprueba antes.
2. **Lista de planos.** Un desglose corto de 3 a 5 planos, con **una acción principal por plano** y encuadre distinto en al menos dos de ellos. Si un plano lleva dos acciones, se divide.
3. **Imagen inicial por plano** (`shot-composer`), en el orden del desglose. En Magnific subes las referencias que ese plano muestra y pegas el prompt. Cada imagen pasa por `prompt escrito` → `imagen generada` → `aprobada`. Un prompt escrito no es una imagen.
4. **Si una imagen falla:** dile a Amenábar qué elemento y dónde (`repair`). Se diagnostica antes de regenerar, con **un cambio por intento**.
5. **Revisión en fila.** Con todas las imágenes aprobadas, míralas seguidas y responde por escrito (ver «Qué entregas»). Si algo no encaja, ajusta el desglose **antes** de ir a vídeo.
6. **Cierre.** Escribe: `Amenábar, comprueba coherencia`. Solo lee y lista conflictos entre guion, desglose y dossier.

**Atajo opcional (no obligatorio):** Variations → Storyboard en Magnific (Image Generator → Tools) genera una cuadrícula desde una sola imagen. Úsalo solo para explorar ángulos; no sustituye a las referencias aprobadas ni al desglose. Su coste en créditos: pendiente de verificar.

## Qué entregas

- El desglose de 3 a 5 planos, con la acción de cada uno.
- Una imagen inicial **aprobada** por plano.
- Las referencias que usó cada imagen (qué aportaba cada una).
- Respuesta a tres preguntas sobre la fila de imágenes:
  - ¿Se entiende la historia sin leer nada?
  - ¿Coinciden personaje, lugar, objeto y luz entre planos?
  - ¿Hay variedad de encuadres, o todos son iguales?
- Una nota breve de lo que salió distinto de lo pedido (sirve para mejorar las skills; no puntúa).

## Valores del ejercicio (`propuesta`, sin aprobar)

Hasta que los apruebes o cambies, no cuentan como decididos:
- **Planos:** 4.
- **Relación de aspecto:** la del destino del proyecto (`# PROYECTO`). Si es vertical, el sujeto en la franja central con aire arriba y abajo (`PLATAFORMAS.md`).
- **Criterio de aprobación de cada imagen:** muestra el estado **inicial** del plano (la acción aún no ha ocurrido), con el mismo personaje, lugar y objeto que las referencias, y sin nadie hablando.

## Ejemplo de prompting

*Ejemplo ilustrativo con el mismo caso inventado de EX00 (ceramista, taller, taza). No está probado en la app: sirve para ver la forma. Prompts pegables en inglés, explicaciones en tu idioma.*

**Desglose de ejemplo (3 planos, una acción principal cada uno):**

| Plano | Encuadre | Acción (la hará el vídeo) |
|---|---|---|
| P01 | plano general | la ceramista entra al taller |
| P02 | plano medio | mira la taza y la coge |
| P03 | primer plano | su mano deja la taza junto al torno |

**Regla clave: la imagen es el estado inicial.** Deja espacio para lo que hará el vídeo.

| Mal (es el resultado) | Bien (es el inicio) |
|---|---|
| *She holds the cup in her hands.* | *She looks down at the cup on the bench; her hands rest on the bench's edge.* |

**P01 — plano general** (referencias: personaje, taller):
```
Natural photograph, horizontal 16:9 wide shot, fixed camera, inside the ceramic workshop in the morning. The woman stands in the open doorway at the back right, one hand on the door frame, looking into the room. Window light from the left across the workbench in the centre. She is the only person in the frame.
```

**P02 — plano medio** (referencias: personaje, taller, taza):
```
Natural photograph, horizontal 16:9 medium shot, fixed camera, in the ceramic workshop. The woman stands behind the workbench, hands resting on its edge, looking down at the ochre cup on the bench in front of her. Morning window light from the left. She is the only person in the frame.
```

**P03 — primer plano** (referencias: taza, taller; la mano **aún no ha llegado**):
```
Natural photograph, horizontal 16:9 close-up, fixed camera. The ochre glazed cup stands on the wooden workbench, handle to the right. In the soft blurred background, the potter's wheel by the window. Morning light from the left. No person in the frame.
```

**Qué comprobar en la fila de imágenes:**
- Mismo rostro, delantal y taza en P01, P02 y P03.
- La luz entra siempre por la izquierda.
- Tres encuadres distintos (general, medio, primer plano).
- Ninguna imagen muestra la acción ya hecha.

**Si una imagen falla**, no la regeneres a ciegas. Díselo a Amenábar así:
```text
En E01-P02 la taza sale blanca, no ocre. Es la imagen inicial; la referencia de la taza estaba subida.
```
Se diagnostica (¿falta la referencia en el reparto?, ¿otra frase la pisa?) y se cambia **una sola cosa** en el siguiente intento.

## Comprobación del profesor (solo texto)

- [ ] De 3 a 5 planos; ninguno con dos acciones principales.
- [ ] Máximo 2 personajes, 1 localización y 1 objeto, todos con referencia `aprobada`.
- [ ] Ningún diálogo ni boca hablando en ningún prompt.
- [ ] Cada imagen se aprobó antes de pasar a la siguiente y sigue el orden del desglose.
- [ ] Cada imagen muestra el estado inicial del plano, no el resultado de la acción.
- [ ] Hay encuadres distintos entre planos.
- [ ] No se generó ningún vídeo.
- [ ] Las tres preguntas de la fila de imágenes están respondidas.

Es una comprobación del texto y de lo entregado; no valida la calidad visual.

## Después

Con el storyboard aprobado, se pasa al prompt de vídeo de cada plano (`video-prompt`), empezando por uno. Mira el coste antes de ejecutar.
