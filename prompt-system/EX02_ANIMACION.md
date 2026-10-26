# EX02_ANIMACION — del storyboard a los clips

Tercer ejercicio. Se hace **después de `EX01_STORYBOARD.md`**. Objetivo: animar las imágenes iniciales aprobadas, plano a plano, controlando el gasto de créditos.

Parte de lo que ya tienes: el storyboard aprobado. No se compone ninguna imagen nueva ni se cambia el desglose (si hace falta cambiarlo, se vuelve a EX01).

## Límites (obligatorios)

| Qué | Límite |
|---|---|
| Planos a animar | los del storyboard de EX01 (**de 3 a 5**); si no sobra saldo, **solo 2** |
| Movimiento de cámara por plano | **uno**, o cámara fija, con su motivo en una frase |
| Acción por plano | **una principal** |
| Diálogo | **ninguno** |
| Sincronía labial (lip sync) | **ninguna** |
| Audio | **sin audio** (o el que decidiste al empezar el proyecto) |
| Texto en pantalla | **ninguno**: títulos y rótulos van en el editor |
| Calidad al probar | **borrador (draft) o 480p**; la alta solo para el clip elegido |
| Borradores por plano | **2**, se elige el mejor; si ninguno sirve, `repair` y un tercero como máximo |
| Pasos a alta | **1** por plano (el elegido) |
| Intentos por plano | **máximo 3 borradores**; tras el tercero se simplifica el plano o se resuelve en el montaje |

Más intentos, más de un movimiento de cámara o diálogo = ejercicio no válido.

## Qué haces

1. **Puerta.** Comprueba que cada plano que vas a animar tiene su imagen inicial `aprobada`. Sin imagen aprobada no se pide vídeo de ese plano.
2. **Mira el coste antes de ejecutar.** Anota en tu nota: modelo, duración elegida, resolución (borrador/480p y alta) y créditos que muestra Magnific, y tu saldo. Si el coste es un dato que no ves, se dice «pendiente de verificar» y se decide tú.
3. **Un primer plano de prueba.** Empieza por **uno solo**: `Amenábar, prompt de vídeo de E01-P01`. El prompt describe solo lo que **cambia** (acción y cámara); no redescribe lo que ya está en la imagen.
4. **Genera 2 borradores, elige y sube a alta.** Pega el prompt en Magnific con la imagen inicial y genera **2 borradores** (draft/480p). Mira los dos clips enteros y elige el mejor. Solo ese pasa a alta. Mira el clip de alta entero antes de aprobar. Si falla, dile a `repair` **a qué segundo y qué elemento** (rostro, manos, objeto, fondo, cámara). Se diagnostica antes de regenerar y se cambia **una sola cosa por intento**.
5. **Repetir o resolver en el montaje.** Para cada defecto decide, y anótalo:
   - *repetir* (cuesta créditos);
   - *cortar antes del fallo* o usar solo la parte buena;
   - *cubrir con otro plano*;
   - *simplificar el plano* (acción, cámara o duración), si ya llevas varios intentos.
6. **El resto de planos.** Con el primero resuelto, sigue el orden del desglose. Un plano que continúa otro parte del fotograma final aprobado del anterior.
7. **Cámara con vocabulario.** Si usas Eye Candy (`PLATAFORMAS.md`): copia la **Recipe** y tradúcela a un movimiento observable (tipo, dirección, velocidad, encuadre al inicio y al final). Los tags de corte o efecto (`FLASH CUT`, `MATCH CUT`, `SPEED RAMP`…) se dejan para el montaje (`edit-plan`).
8. **Control de saldo.** Al terminar cada plano, apunta créditos gastados y saldo restante.

## Qué entregas

- Un clip por plano animado, **aprobado**, con su imagen inicial.
- Por plano, una línea: movimiento de cámara elegido y qué aporta (si no lo sabes, cámara fija).
- El **registro de intentos** de cada plano: qué prompt, qué falló (segundo y elemento), qué cambiaste y qué resultó.
- La decisión de cada defecto: repetir, cortar, cubrir o simplificar.
- **Tabla de créditos:** plano, borradores, pasos a alta, créditos gastados, saldo al final.
- Una nota breve de lo que salió distinto de lo pedido (sirve para mejorar las skills; no puntúa).

## Valores del ejercicio (`propuesta`, sin aprobar)

Hasta que los apruebes o cambies, no cuentan como decididos:
- **Duración por clip:** corta, dentro del mínimo y máximo del modelo que uses (`MODELOS.md`; si ese dato está pendiente de verificar, se dice y se elige tú).
- **Resolución:** borrador o 480p para probar (2 por plano); alta solo para el borrador elegido. Qué modos de baja calidad ofrece cada modelo: pendiente de verificar en `MODELOS.md`.
- **Pasar a alta:** si la app reutiliza el borrador o genera un clip nuevo (y puede salir distinto) está **pendiente de verificar**. Tras subir a alta, se vuelve a mirar el clip entero.
- **Relación de aspecto:** la de la imagen inicial / destino del proyecto.
- **Criterio de aprobación de cada clip:** hace la acción pedida; el personaje, el lugar y el objeto siguen siendo los de las referencias; la cámara hace lo que dijiste (o queda fija); nadie habla; no hay deformaciones visibles en rostro y manos durante todo el clip.

## Ejemplo de prompting

*Ejemplo ilustrativo con el mismo caso inventado de EX00 y EX01 (ceramista, taller, taza). No está probado en la app: sirve para ver la forma. Prompts pegables en inglés, explicaciones en tu idioma. Los tiempos son estimación escrita; solo la prueba real los comprueba.*

**Reglas de forma:**
- El prompt describe solo lo que **cambia**: acción y cámara. No redescribas el personaje, el taller ni la luz, que ya están en la imagen inicial.
- Una acción principal y un movimiento de cámara por plano. Si no sabes decir qué aporta el movimiento, cámara fija.
- Marca la acción con tiempos (`00:00`, `00:02`), una acción por tiempo.
- Cierre sin audio: *No music. No subtitles.*

**P01 — plano general. Cámara fija** (motivo: dar escala al taller):
```
Fixed camera. 00:00 The woman steps through the doorway into the workshop. 00:03 She walks toward the workbench in the centre. The window light stays constant. No music. No subtitles.
```

**P02 — plano medio. Acercamiento lento** (motivo: da peso al momento en que coge la taza):
```
Slow push-in toward the woman, ending in a medium close-up. 00:00 She looks at the cup. 00:02 She picks it up with her right hand and lifts it to chest height. The window light stays constant. No music. No subtitles.
```

**P03 — primer plano. Cámara fija** (motivo: ninguno; el plano quieto basta):
```
Fixed camera. 00:00 A hand enters from the right and sets the cup down beside the potter's wheel. 00:02 The hand withdraws out of frame. The cup stays where it is. No music. No subtitles.
```

**Con vocabulario de Eye Candy.** Si el tag es `DOLLY ZOOM`, copia su Recipe y tradúcela a movimiento observable (tipo, dirección, velocidad, encuadre inicial y final). No pegues el nombre del tag como si el modelo lo conociera. Si el tag es de corte (`FLASH CUT`, `MATCH CUT`), va al montaje, no al prompt.

**Si el clip falla**, dile a Amenábar el segundo y el elemento:
```text
En E01-P02, a los 3 segundos la mano derecha sale con seis dedos al coger la taza. Es el clip, la imagen inicial estaba bien.
```
El diagnóstico apunta a un movimiento demasiado cargado para la duración. **Un solo cambio** en el siguiente intento, por ejemplo acortar la acción:
```
Slow push-in toward the woman, ending in a medium close-up. 00:00 She looks at the cup. 00:02 She rests her hand on the cup. The window light stays constant. No music. No subtitles.
```
Si tras 3 intentos sigue fallando, se decide por escrito: cortar antes del fallo, cubrir con otro plano o simplificar. Anótalo en el registro de intentos junto con los créditos gastados.

## Comprobación del profesor (solo texto)

- [ ] Cada clip parte de una imagen inicial `aprobada`.
- [ ] Un movimiento de cámara por plano (o fija), con su motivo en una frase.
- [ ] Una acción principal por plano.
- [ ] Ningún diálogo, boca hablando ni texto en pantalla en ningún prompt.
- [ ] Se probó con 2 borradores por plano y solo el elegido pasó a alta.
- [ ] No más de 3 borradores por plano y un solo cambio entre intentos.
- [ ] Cada fallo indica segundo y elemento, y cada decisión (repetir, cortar, cubrir, simplificar) está justificada.
- [ ] La tabla de créditos está completa y el coste se miró antes de cada ejecución.
- [ ] Los tags de corte o efecto de Eye Candy no se pusieron dentro de un plano con otro movimiento.

Es una comprobación del texto y de lo entregado; no valida la calidad visual.

## Después

Con los clips aprobados, se pasa al **plan de montaje** (`edit-plan`: orden, uniones, ritmo, sonido y texto en pantalla) y al montaje en DaVinci Resolve (módulo 5).
