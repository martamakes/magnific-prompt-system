# EX03a_EFECTOS — efectos de sonido y ambiente

Primer ejercicio de audio. Se hace **después de `EX03_AUDIO.md`** y de tener al menos un clip aprobado (EX02). Objetivo: crear los efectos y el ambiente de un plano y colocarlos por escrito.

## Límites (obligatorios)

| Qué | Límite |
|---|---|
| Clips | **1** (un plano ya aprobado de EX02) |
| Efectos de acción | **2** (un golpe seco y otro más suave, por ejemplo) |
| Ambiente | **1** (una textura continua) |
| Diálogo | **ninguno** |
| Música | **ninguna** |
| Variaciones por sonido | **4** para comparar (valor del tutorial de Magnific, `documentada`) |
| Intentos por sonido | **máximo 3** |

Un efecto con voz, música o diálogo = ejercicio no válido.

## Qué haces

1. **Elige un clip aprobado** y escucha mentalmente qué suena: qué acciones hay y cómo es el lugar.
2. **Anota en el desglose, por tipo:** 2 efectos de acción y 1 ambiente, cada uno con el plano al que va y el momento aproximado en que entra.
3. **Un prompt por sonido** (`audio-prompt`): `Amenábar, prompt de efectos de E01-P02`. Describe lo que **se oye**, no por qué ocurre.
4. **Duración orientativa y bucle**, aparte del prompt: efecto corto (el tutorial usa ~5 s para un golpe seco), ambiente largo (~10 s) y en bucle si es continuo.
5. **Genera 4 variaciones** de cada uno, escucha y elige una. Mira el coste antes de ejecutar.
6. **Escribe el plan de colocación:** en qué momento entra cada sonido y a qué nivel (el ambiente por debajo, el efecto por encima). Es estimación escrita; el ajuste real es del montaje.

## Qué entregas

- Los 3 sonidos anotados en el desglose (tipo, plano, momento).
- Los 3 prompts, cada uno con duración y bucle.
- El sonido elegido de cada uno y por qué (una línea).
- El plan de colocación (momento y nivel relativo de cada sonido).
- Tabla de créditos: sonido, intentos, créditos gastados.
- Una nota breve de lo que salió distinto de lo pedido.

## Ejemplo de prompting

*Ilustrativo, con el caso de la ceramista de EX00–EX02. No probado en la app. Prompts en inglés, explicaciones en tu idioma.*

**Regla de forma:** una frase corta y directa, sustantivos y acciones claros, sin historia.

| Mal (cuenta la historia) | Bien (dice lo que se oye) |
|---|---|
| *The potter feels nervous and picks up her favourite cup before the lesson* | *ceramic cup lifted off a wooden bench* |

**Efecto 1 — coger la taza** (plano P02, entra a ~00:02):
```
ceramic cup lifted off a wooden workbench
```
Ajustes: 3 s, sin bucle, 4 variaciones.

**Efecto 2 — pasos** (plano P01, entra a ~00:00):
```
footsteps on a wooden workshop floor, slow and steady
```
Ajustes: 4 s, sin bucle, 4 variaciones.

**Ambiente — el taller** (todos los planos):
```
quiet pottery workshop ambience, soft room tone, faint distant street noise
```
Ajustes: 10 s, **en bucle**, 4 variaciones.

**Si un sonido no encaja**, dile a Amenábar qué oyes y cambia una cosa:
```text
El efecto de la taza suena a metal, no a cerámica. Es el prompt del efecto 1.
```
Siguiente intento: cambiar solo «ceramic cup» por «unglazed clay cup» y anotar el resultado.

## Comprobación del profesor (solo texto)

- [ ] Un clip, 2 efectos y 1 ambiente; sin diálogo ni música.
- [ ] Cada sonido tiene su prompt propio, en una frase, describiendo lo que se oye.
- [ ] Duración y bucle indicados aparte; el ambiente en bucle y los efectos sin él.
- [ ] Se compararon variaciones antes de elegir.
- [ ] El plan de colocación indica momento y nivel de cada sonido.
- [ ] No más de 3 intentos por sonido, con un solo cambio entre intentos.
- [ ] La tabla de créditos está completa.

Es una comprobación del texto y de lo entregado; no valida la calidad sonora.

## Después

`EX03b_BANDA_SONORA.md`, o directamente al plan de montaje (`edit-plan`) y al módulo 5.
