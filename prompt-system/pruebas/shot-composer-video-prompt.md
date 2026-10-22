# PRUEBA 2 — shot-composer y video-prompt sobre E01-P02 de «La segunda taza»
Prueba por escrito, aplicando las skills tal como están, sobre el plano más cargado del caso (`la-segunda-taza.md` v0.5). Solo comprueba coherencia de las skills; no la eficacia de los prompts ni imagen/vídeo reales. Nada de lo aquí escrito está `aprobado`.

## 1. Puertas (cómo reaccionan las skills)
- El plano usa **imagen inicial + vídeo** (vía propuesta del desglose) → shot-composer aplica.
- Referencias del plano (M2, vestuario M2, taza 2, cocina): todas `pendiente`; el caso declara además «sin referencias visuales» → no bloquea (H1, aplicado); se avisa de que la identidad entre clips no queda anclada.
- Ensayo en seco solo con texto, `propuesta`.

## 2. shot-composer — imagen inicial de E01-P02 (propuesta, texto sin referencias)
Estado inicial: M2 ya dentro, de pie junto a la silla B, mirada al frente; taza 2 sobre la mesa; silla B vacía; puerta abierta al fondo a la izquierda; M1 presente fuera de cuadro a la izquierda.

```
Natural photograph, horizontal 16:9 medium-wide shot, fixed camera, in a kitchen on a morning with natural window light. On the right side of a small kitchen table stands an empty wooden chair, seen in profile and facing left. On the table, on the side nearest the chair, an ochre glazed ceramic cup with a handle. An adult woman in simple street clothes stands beside the chair on its near side, arms relaxed at her sides, gaze level toward the middle of the room. At the back left, an open door. She is the only person in the frame.
```
- Referencias: ninguna. Ajuste de la app: relación de aspecto 16:9.
- Estado: `prompt escrito` (no imagen).
- Decisiones del prompt (`propuesta`): M2 junto a la silla por su lado cercano a cámara, brazos sueltos, mirada al frente (la mirada a la taza es lo que hace el vídeo); M1 no se menciona (fuera de cuadro); sin rasgos de rostro porque el caso no los fija; sin negaciones («she is the only person in the frame»).

## 3. video-prompt — E01-P02, imagen a vídeo, 5 s (propuesta)
```
Fixed camera. 00:00 The woman beside the chair lowers her gaze to the ochre cup on the table. 00:02 She lifts her eyes to the left, out of frame. 00:03 She sits down in the chair, facing left. The cup stays where it is. The window light stays constant. No music. No subtitles.
```
- Referencias: la imagen inicial del apartado 2, una vez aprobada. Ajustes: 5 s (estimación escrita), 16:9.
- Audio: `audio externo` → ningún sonido descrito; cierre «No music. No subtitles.» (documentada, handbook de Magnific; la skill pide avisarlo).
- Beats con tiempo: forma del handbook de Magnific; los tiempos son estimación escrita.
- Carga: tres acciones sucesivas en 5 s (antes cuatro). Sigue siendo el plano más cargado; solo la prueba temporal lo confirma.

## 4. Hallazgos
- **H1 (aplicado).** «Sin referencias» declarado no bloquea la composición; se avisa del riesgo de identidad. Sin reprobar tras el cambio.
- **H2 (resuelto).** Puerta al fondo izquierda (v0.4); con M2 ya dentro (v0.5) desaparece el cruce corto que no justificaba 5 s.
- **H3 (resuelto).** `Audio: audio externo`.
- **H4 (resuelto, REGLAS §9).** Prompts pegables en inglés; explicaciones en el idioma del usuario. Que el inglés rinda mejor no está verificado: criterio de la usuaria.
- **H5 (nuevo).** El handbook de Magnific cierra sus prompts con «No music. No subtitles.» incluso cuando el sonido va a montaje. Aplicado en `video-prompt` para `audio externo`; si no se quiere, quitar esa línea de la skill.
- **H6 (nuevo).** La entrada de M2 queda fuera de plano; coincide con la regla del handbook «lo que sale de cuadro no vuelve en la misma toma».
- Lo que funcionó: separación imagen (estado inicial) / vídeo (solo cambio); M1 fuera de cuadro sin entrar en el prompt visual; negación evitada.
- Sin reprobar: ni los prompts en inglés ni los beats con tiempo se han probado en la app.
