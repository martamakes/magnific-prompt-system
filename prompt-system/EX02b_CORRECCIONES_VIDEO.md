# EX02b_CORRECCIONES_VIDEO — diagnosticar y corregir un clip que falla

Se hace **después de `EX02_ANIMACION.md`**, con un clip que tenga un defecto. Objetivo: aprender a diagnosticar un fallo en vídeo y elegir la corrección más barata. Trabaja con `repair`.

No se compone ningún plano nuevo ni se cambia el desglose. Si el fallo viene del desglose, se anota y se vuelve a EX01.

## Límites (obligatorios)

| Qué | Límite |
|---|---|
| Clips a corregir | **1** (con un defecto real de EX02; si no tienes ninguno, el profesor aporta uno) |
| Defectos tratados | **1** (el que el alumno prioriza) |
| Cambios por intento | **uno solo** |
| Calidad al probar | **borrador/480p**; la alta solo para la versión elegida |
| Intentos de regeneración | **máximo 3** (en borrador) |
| Diálogo, lip sync, audio | **ninguno** |
| Versiones | se conservan todas (`E01-P02-v1`, `-v2`…); no se sobrescribe |

Más de un cambio por intento o más de 3 regeneraciones = ejercicio no válido.

## Qué haces

1. **Localiza el fallo observable:** segundo (o tramo) y elemento concreto (mano derecha, rostro, objeto, fondo, cámara). «Se ve raro» no vale. Extrae un fotograma del segundo indicado: vale más que la descripción.
2. **Protege lo que funciona:** anota qué está bien y no debe cambiar (personaje, luz, composición).
3. **Hipótesis de causa, ordenadas** (`propuesta`, un intento no las confirma): el prompt (ambiguo, cargado), las referencias (faltan o chocan), el plan (plano sobrecargado) o el modelo (solo si lo anterior no lo explica).
4. **Elige la corrección más barata**, en este orden, y anota por qué descartas las anteriores:
   1. *Resolver sin generar:* cortar antes del fallo, usar solo la parte buena, recortar o reencuadrar en el montaje (`edit-plan`).
   2. *Cubrir* con otro plano o un plano de recurso.
   3. *Regenerar con un solo cambio* en el prompt (versión `-v2`).
   4. *Corregir la imagen inicial* si el fallo nace ahí (antes de gastar en vídeo).
   5. *Simplificar el plano* (acción, cámara o duración) tras varios intentos sin mejora.
5. **Si regeneras:** mira el coste antes, cambia **una sola cosa**, escribe `-v2`, genera en borrador/480p (2 si quieres comparar) y compara con el fotograma del fallo. Solo la versión que corrige el fallo pasa a alta, y se vuelve a mirar entera.
6. **Decide por escrito** tras cada intento: aprobado, otro intento o cambio de estrategia. Tras el tercero sin mejora, simplifica o resuelve en el montaje.

## Qué entregas

- El fallo: segundo, elemento y fotograma (o descripción).
- Lo que se protege.
- Hipótesis de causa (`propuesta`) con la frase o referencia que la sugiere.
- La corrección elegida y por qué descartaste las más baratas.
- El registro de versiones: prompt, qué cambió, qué resultó.
- Tabla de créditos: intentos y gastados.
- La decisión final: aprobado, cortado, cubierto o simplificado.

## Repetir un clip con «Recreate»

Al abrir un vídeo generado, **Use video → Recreate** vuelve al generador con el prompt, los ajustes y las referencias originales ya cargados (dato del tutorial «Prompting for video» de Magnific; sin comprobar con tu cuenta). Sirve para generar otra versión cambiando **una sola cosa** (`-v2`), o probar la misma idea con otro modelo. Antes de generar, comprueba que se restauraron las referencias y la calidad (borrador/480p).

## Tipos de fallo frecuentes

Ayuda para localizar; no sustituye mirar el clip. Las causas son hipótesis.

| Fallo | Qué mirar | Primera corrección a considerar |
|---|---|---|
| Manos o dedos deformados | segundo exacto, qué mano | cortar antes del fallo; acortar o simplificar la acción |
| Rostro que deriva | desde qué segundo | referencia de personaje más clara; acción menos cargada |
| Objeto que cambia o desaparece | qué objeto y cuándo | repetir el rol del objeto en el prompt; objeto de referencia |
| Cámara que hace otra cosa | qué hace frente a lo pedido | un solo movimiento descrito de forma observable |
| Acción que no ocurre o va demasiado rápido | tiempos del prompt | menos acciones o más duración |
| Fondo o luz que cambian | qué cambia | añadir qué se mantiene constante |
| Lo que sale de la imagen inicial | qué difiere del primer fotograma | corregir la imagen inicial |

## Ejemplo de prompting

*Ilustrativo, con la ceramista de EX00–EX02. No probado en la app. Prompts en inglés, explicaciones en tu idioma.*

**Fallo (dicho a Amenábar):**
```text
En E01-P02, a los 3 segundos la mano derecha sale con seis dedos al coger la taza. Lo demás está bien. Es el clip; la imagen inicial estaba bien.
```

**Diagnóstico** (`propuesta`): acción demasiado cargada para la duración (coger y levantar). Protege: personaje, luz, push-in lento.

**v1 (el que falló):**
```
Slow push-in toward the woman, ending in a medium close-up. 00:00 She looks at the cup. 00:02 She picks it up with her right hand and lifts it to chest height. The window light stays constant. No music. No subtitles.
```

**v2 — un solo cambio, acortar la acción:**
```
Slow push-in toward the woman, ending in a medium close-up. 00:00 She looks at the cup. 00:02 She rests her right hand on the cup. The window light stays constant. No music. No subtitles.
```

**Si v2 sigue fallando:** antes de v3, considera cortar el clip antes de los 3 s y cubrir con un primer plano de la taza. Una regeneración cuesta créditos; el corte, no.

**Mal y bien al pedir un arreglo:**

| Mal | Bien |
|---|---|
| *Fix the hands and also make the camera slower and the light warmer* (tres cambios; no sabrás cuál funcionó) | *Same prompt, shorten the action to resting her hand on the cup* (un cambio) |
| *Make it look better* | segundo y elemento + un cambio concreto |

## Comprobación del profesor (solo texto)

- [ ] El fallo indica segundo y elemento, no «se ve raro».
- [ ] Hay lo que se protege.
- [ ] La causa figura como hipótesis, no como hecho.
- [ ] Se justifica por qué se descartó resolver en el montaje o cubrir antes de regenerar.
- [ ] Un solo cambio entre versiones, todas conservadas.
- [ ] No más de 3 regeneraciones; la decisión final está escrita.
- [ ] La tabla de créditos está completa y se miró el coste antes de cada intento.

Es una comprobación del texto y de lo entregado; no valida la calidad visual.

## Después

`EX03_AUDIO.md` o el plan de montaje (`edit-plan`).
