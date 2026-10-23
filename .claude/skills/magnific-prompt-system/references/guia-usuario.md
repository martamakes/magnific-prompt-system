# Guía de uso: de la idea al plan de montaje

Guía para quien usa el sistema; no la leen las skills. Se trabaja con la palabra **Amenábar**: él lee tu proyecto, te dice en qué fase estás y cuál es el siguiente paso, con la frase exacta que tienes que escribir.

**Si empiezas, haz primero `references/ex00-kiss.md`:** un ejercicio con 1 personaje, 1 localización, 1 objeto, sin diálogo ni lip sync.

Alcance: brief → guion → desglose → plan de referencias → referencias (personajes, localizaciones, objetos, hoja de vestuario opcional) → composición → prompts de vídeo → revisión de resultados (`repair`) → plan de montaje (`edit-plan`). También hay prompts de audio. El sistema solo redacta: tú pegas los prompts en Magnific (y en la herramienta de audio que uses). **Audio:** tú eliges al empezar: sin audio, audio externo (lo pones tú fuera de Magnific) o audio en Magnific. **Texto en imagen o vídeo:** no se pide en los prompts; títulos y rótulos se añaden después en el editor de vídeo.

---

## Cómo empezar

Proyecto nuevo:

```text
Oye Amenábar, quiero empezar un proyecto nuevo. Mi idea: [idea en 1-3 frases].
```

Proyecto en marcha (en una conversación nueva, con el dossier pegado debajo):

```text
Oye Amenábar, sigue mi proyecto. ¿Qué toca ahora?

[tu dossier]
```

Amenábar responde con un parte corto (fase actual, qué está aprobado, qué falta) y termina siempre con:

> **Siguiente paso:** … Escribe: «…»

Copia esa frase tal cual. No ejecuta nada por su cuenta: espera tu orden.

## Las fases

1. **Brief.** Responde a sus preguntas (máx. 3). «A tu criterio» y «sin marca» valen. Te preguntará por el audio: la opción recomendada es **sin audio**; las otras son **audio externo** y **audio en Magnific** (más gasto y más riesgo de fallo).
2. **Guion.** Lo inventado va como `propuesta`. El desglose no empieza sin que apruebes el guion.
3. **Desglose.** Planos y recursos. Revisa duraciones y «Decisiones pendientes».
   - *Opcional, antes del plan de referencias:* **revisión de estilo.** Si el desglose te sale estático, di `Amenábar, revisa con estilo redes`. Recibes un diagnóstico con cifras y propuestas por plano; eliges cuáles se aplican. Estilo disponible hoy: `redes` (vídeo corto vertical); otros irán en `references/estilos/`.
4. **Plan de referencias.** Tras aprobar el desglose te da la lista `REF-01, REF-02…`: qué imágenes hay que crear y en qué orden. Las vistas salen de los planos.
5. **Referencias.** Una REF cada vez. Para cada una recibes un prompt; lo generas en Magnific y vuelves a decir si queda aprobada.

6. **Composición y vídeo.** Imágenes de cada plano a partir de las referencias aprobadas; después el prompt de vídeo. Un vídeo necesita su imagen inicial aprobada. Los límites (duración, referencias) salen de `references/modelos.md`; cualquier valor «pendiente de verificar» se te dice, no se supone.
7. **Revisión.** Si un resultado falla, dile a qué segundo y qué elemento (o, en una imagen, qué elemento y dónde): se diagnostica antes de regenerar.
8. **Montaje.** Orden, uniones, sonido y texto en pantalla, como plan escrito para tu editor.

Para aprobar o corregir, en cualquier fase:

```text
Aprobado. [O: cambia X por Y.]
```

## Estados de cada entregable

`propuesta` → `prompt escrito` → `imagen generada` → `aprobada`

**Un prompt escrito no es una imagen.** Hasta que no generes la imagen y la apruebes, la referencia no cuenta como hecha. Una referencia de prioridad Alta sin aprobar bloquea la fase siguiente.

## Referencias: qué esperar

- **Personaje:** si necesita 2 o más vistas, se hace una **hoja de vistas** (frente, perfil, espaldas). Con una sola imagen aprobada el personaje no está cerrado.
- **Localización:** vista general vacía; otras vistas solo si los planos las usan. Otra hora o clima es una variante aparte.
- **Objeto:** si tienes una foto real del producto, se usa como referencia directa; no se genera una nueva.
- **Variantes** (otro vestuario, otro estado): se hacen cuando la versión base está aprobada.
- **Códigos:** `E01` escena, `E01-P03` plano, `PJ01` personaje, `LO01` localización, `OB01` objeto, `-v2` variante, `REF-01` referencia del plan (detalle en `references/reglas.md` §7).
- **Visuales:** hoja de vestuario y dirección visual (luz, color, óptica) son opcionales; "sin look definido" también vale.

Si lo que te da Amenábar no lo entiendes o no encaja, escríbelo con tus palabras: «no lo entiendo, explícamelo más simple» o «esto no es lo que quería: [qué]».

---

## Reglas

- **Una conversación nueva por fase**, con el dossier pegado (plantilla en `references/proyecto.md`). Así no se pierde el hilo.
- **Dossier grande:** el guion y el desglose pueden vivir en su propio archivo (`guion.md`, `desglose.md`); el dossier conserva un puntero con versión y estado. Si trabajas en una conversación nueva, pega también ese archivo.
- **Lo propuesto no es aprobado** hasta que lo digas.
- **Comprobar coherencia:** al cerrar una fase, o cuando guion, desglose y dossier hayan cambiado por separado, di `Amenábar, comprueba coherencia`. Solo lee y te lista los conflictos con archivo y línea; no corrige nada hasta que elijas.
- Si en algún momento no sabes qué hacer: «Oye Amenábar, ¿en qué fase estoy?».
