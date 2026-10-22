# Pruebas: plan de referencias, prompts de recursos, audio-prompt y character-ref D
**Qué son:** aplicaciones escritas de las skills sobre «La segunda taza» v0.5, hechas por quien las redactó; no se ha visto ninguna imagen ni audio. Todo es `propuesta`. El caso declaró trabajar **sin referencias visuales**; este plan es un ensayo de lo que saldría si se quisieran (no un requisito del caso).

---

## 1. Plan de referencias (breakdown §D) — ejecutada (texto)
Las vistas salen de los planos: los tres tienen la cámara del mismo lado del eje, así que la cocina solo necesita **una** vista; P02 y P03 son recortes de ella.

| REF | Qué | Vistas o estados | Lo justifica | Prioridad | Estado |
|---|---|---|---|---|---|
| REF-01 | M1 con su vestuario (prenda de casa, un color) | frente y perfil derecho (hoja) | P01 de perfil mirando a la derecha; P03 de frente | Alta | propuesta |
| REF-02 | Cocina, mesa pequeña, silla B, puerta | vista general desde el lado de cámara | P01–P03 | Alta | propuesta |
| REF-03 | M2 con su vestuario (ropa de calle, color distinto) | frente y perfil izquierdo (hoja) | P02 de pie, mirando a la izquierda; P03 en primer término | Alta | propuesta |
| REF-04 | Taza 2 (ocre) | vista general | P01–P03 | Alta | propuesta |
| REF-05 | Taza 1 (blanca lisa) | vista general | P01, P03 | Media | propuesta |

Sin contraplano de cocina, sin vistas extra de personaje, sin variantes. Cinco imágenes en total. Orden: protagonista → localización → resto de personajes → objetos.

**Resultado:** cumple las reglas de §D. **Hallazgo L3:** la prioridad Alta se define como «bloquea planos de varias escenas o el protagonista»; en una pieza de **una sola escena** esa frase no decide nada para la cocina ni para las tazas. Los he puesto Alta porque bloquean los tres planos, que es una interpretación mía.

## 2. Prompts de las cinco referencias — ejecutada (texto)
Imagen en inglés (REGLAS §9). Ajustes de la app: 16:9 para la cocina, 1:1 para el resto, `propuesta`. Rasgos de personaje, de vestuario y de objeto: `propuesta` (el caso solo fija «adulta», «distinta de M1», ropa de casa / de calle y color).

**REF-01 — M1** (hoja de vistas)
```
Character reference sheet on a plain neutral background with soft even light: the same adult woman in two views side by side, front view and right-profile view, full body, arms relaxed. She is in her forties with shoulder-length dark brown hair, an oval face with straight eyebrows and a calm, neutral expression. She wears a loose, soft, mustard-yellow cotton house cardigan over a plain cream T-shirt and dark trousers, flat house shoes. Both views show exactly the same person and clothes.
```

**REF-02 — Cocina**
```
Interior reference photograph of a small, ordinary kitchen on a morning, seen from a fixed camera at eye level on the near side of the room. A small square wooden table stands in the centre of the room. To the right of the table an empty wooden chair is seen in profile, facing left. At the back left of the room an open door leads to a dimly lit hallway. A window on the left wall lets in soft natural morning light that falls across the table. Pale painted walls, warm wooden floor, a few simple worn cupboards along the back wall. The room is empty of people, and the table is bare. About 3 by 4 metres, ceiling at about 2.5 metres.
```

**REF-03 — M2** (hoja de vistas)
```
Character reference sheet on a plain neutral background with soft even light: the same adult woman in two views side by side, front view and left-profile view, full body, arms relaxed. She is in her late twenties with a straight black bob, a rounder face with full eyebrows and a calm, neutral expression. She wears simple street clothes: a navy-blue coat over a white shirt, grey trousers and brown leather shoes. Both views show exactly the same person and clothes. She looks clearly different from a woman with brown shoulder-length hair.
```

**REF-04 — Taza 2**
```
Reference photograph of a single ceramic coffee cup standing upright on a flat surface, three-quarter view from slightly above. Hand-thrown look: rounded body, widest at the middle and narrowing gently to the base, a thick rim that is slightly uneven. A single loop handle on the right, joined at the rim and at the lower body. Plain ochre glaze, semi-gloss, a little darker where it pools near the base, with no pattern or markings. About 9 cm tall, the size of an ordinary coffee cup held in one adult hand. Plain neutral background, soft even light. Only the cup is in the frame.
```

**REF-05 — Taza 1**
```
Reference photograph of a single plain white ceramic coffee cup standing upright on a flat surface, three-quarter view from slightly above. Smooth, glossy white glaze, a straight-sided classic shape, a simple loop handle on the right, no pattern or markings. About 8 cm tall, the size of an ordinary coffee cup held in one adult hand. Plain neutral background, soft even light. Only the cup is in the frame.
```
- Si el usuario tiene fotos reales de las tazas o de su cocina, se usan como referencia directa y no se generan (REF-02, 04 y 05).
- Hojas de vistas: «misma persona» se afirma en el texto; que los dos paneles conserven la identidad no está comprobado.
- **Hallazgo L4:** «She looks clearly different from a woman with brown shoulder-length hair» nombra a M1 dentro del prompt de M2 para forzar la diferencia. Es una negación indirecta; su efecto es incierto. Más limpio: describir a M2 y confiar en la diferencia de rasgos. Lo dejo así hasta ver imagen; si molesta, se quita.

## 3. audio-prompt — sonidos de los tres planos — ejecutada (texto)
`Audio: audio externo`, sin diálogo, sin música (restricciones del caso). Herramienta sin decidir. Una pieza por prompt; duraciones y variaciones aparte.

| Pieza | Plano | Prompt | Ajustes |
|---|---|---|---|
| S1 ambiente | P01–P03 | `quiet kitchen ambience on a morning, soft room tone, faint fridge hum` | 15 s · bucle sí · 4 variaciones |
| S2 pasos | P01 | `footsteps of one person walking across a wooden floor, then stopping` | 4 s · bucle no |
| S3 taza | P01 | `a ceramic cup set down on a wooden table, one soft clink` | 2 s · bucle no |
| S4 silla | P02 | `a wooden chair scraping softly as someone sits down` | 3 s · bucle no |
| S5 roce | P03 | `a ceramic cup slid a short distance across a wooden table, soft scrape` | 3 s · bucle no |

Cada bloque va solo en su código al entregarse; aquí van en tabla por brevedad. Los momentos de entrada son estimación escrita y su colocación real es de `edit-plan`.

**Resultado:** cumple (frase corta, qué suena + qué hace + dónde; un tipo de sonido por prompt; sin voz, sin música; sin límites de herramienta inventados). **Hallazgo A1:** S2, S3, S4 y S5 suponen un suelo y una mesa de madera, que sale de la propuesta de REF-02; si la cocina cambia, cambian los sonidos. **Hallazgo A2:** el caso no dice cuántas capas ni cuánto dura cada una; la duración total (15 s) es la del encargo, pero el reparto 5/5/5 de los clips y su solape pertenecen al montaje.

## 4. character-ref, prueba D — ejecutada (texto)
**D1. Sin indicar reparto.** Entrada: «Combínalas» + dos fotos de rostro (una de cada actriz). Esperado: no redacta; pregunta qué aporta cada imagen, qué se ignora y cuál prevalece. Salida: «Dos preguntas: ¿qué tomo de cada foto (rostro, peinado, ropa…) y qué ignoro? Si chocan (rasgos del rostro), ¿cuál prevalece?» → **cumple**.

**D2. Con reparto ya dicho.** Entrada: «De la primera, solo el rostro; de la segunda, solo el peinado y la ropa. El rostro manda.» Esperado: no repregunta; redacta con cada imagen declarada. Salida: bloque con «Reference image 1 gives the face and facial structure, which take priority. Reference image 2 gives hair and clothing only; ignore its face, background and pose.» → **cumple**.

---

## Hallazgos
- **L1** (de la prueba anterior, sigue abierta): contradicción en `location-ref` entre petición explícita y base sin aprobar. Pendiente de tu decisión.
- **L3.** Prioridad Alta no está definida para una pieza de una sola escena. Propuesta: leer «varias escenas» como «varios planos».
- **L4.** Negación indirecta en el prompt de M2; efecto incierto.
- **A1, A2.** Dependencias de audio con la cocina propuesta y con el montaje.
- **Sin probar:** nada de esto se ha visto en imagen o audio. Falta ver si las hojas de vistas conservan identidad, si las tazas son reconocibles y si el inglés rinde.
