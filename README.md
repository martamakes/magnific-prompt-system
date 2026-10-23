# Magnific prompt system

Sistema de skills **solo de redacción** para preparar producciones audiovisuales con IA. Te entrega prompts listos para pegar en [Magnific](https://www.magnific.com) (imagen con Nano Banana, vídeo con Seedance) y, si lo pides, prompts de audio para la herramienta que uses.

**Qué no hace:** no genera imágenes, vídeo ni audio, no ejecuta operaciones en Magnific y no elige modelo por ti. Escribe; tú pegas, generas y apruebas.

## Qué incluye

Una skill coordinadora (el director, que se activa con la palabra **Amenábar**) y las que deriva:

| Fase | Skill |
|---|---|
| Idea → objetivo | `brief` |
| Guion | `script` |
| Planos y recursos | `breakdown` |
| Revisión de estilo del desglose (opcional) | `review` + `estilos/` |
| Comprobación de coherencia (solo lectura) | `coherencia` |
| Referencias | `character-ref`, `prop-ref`, `location-ref` |
| Imagen inicial de un plano | `shot-composer` |
| Prompt de vídeo | `video-prompt` |
| Prompt de música, efectos, voz o ambiente | `audio-prompt` |
| Previsualización 3D (solo especificación, opcional) | `scene-previz` |
| Resultado que falla | `repair` |
| Orden, uniones y sonido en montaje | `edit-plan` |

Documentos comunes: `REGLAS.md` (reglas de todas las skills), `PROYECTO.md` (plantilla del dossier), `MODELOS.md` y `PLATAFORMAS.md` (límites por modelo y zonas seguras por destino), `EX00_KISS.md` (ejercicio inicial) y `FLUJO-idea-a-storyboard.md` (guía de uso paso a paso).

## Instalación

El código fuente está en `prompt-system/`. Para usarlo se empaqueta en **una sola skill** (`magnific-prompt-system`: el director como `SKILL.md` y el resto en `references/`).

### Claude Code

1. Genera el paquete (necesita Python 3):

   ```bash
   python3 build-dist.py
   ```

   Crea `dist/magnific-prompt-system/` y `dist/magnific-prompt-system.zip`.

2. Copia la carpeta a donde Claude Code lea skills:
   - solo en un proyecto: `<proyecto>/.claude/skills/magnific-prompt-system/`
   - para todos tus proyectos: `~/.claude/skills/magnific-prompt-system/`

   ```bash
   mkdir -p .claude/skills
   cp -R dist/magnific-prompt-system .claude/skills/
   ```

3. Abre una conversación nueva y escribe `Oye Amenábar, ¿en qué fase estoy?`.

Este repositorio ya incluye una copia instalada en `.claude/skills/magnific-prompt-system/`. Tras cambiar algo en `prompt-system/`, regenera y reinstala, y comprueba que la copia coincide con el paquete:

```bash
python3 build-dist.py && rm -rf .claude/skills/magnific-prompt-system && cp -R dist/magnific-prompt-system .claude/skills/ && python3 check-sync.py
```

`check-sync.py` solo prueba que la copia instalada coincide con el paquete recién generado; no prueba cómo se comporta la skill.

### Otros asistentes (Gemini, ChatGPT, etc.)

Los archivos son Markdown portable, sin dependencias de Claude. Pega en la conversación `references/reglas.md` junto con el archivo de la fase en que estés. Es un uso **pendiente de verificar**: no hay notas de instalación por asistente ni pruebas hechas fuera de Claude.

El zip de `dist/` no se ha probado como subida a ninguna interfaz web (pendiente de verificar).

## Uso

1. Si empiezas, haz primero `prompt-system/EX00_KISS.md`: un ejercicio con 1 personaje, 1 localización y 1 objeto, sin diálogo.
2. Proyecto nuevo:

   ```text
   Oye Amenábar, quiero empezar un proyecto nuevo. Mi idea: [idea en 1-3 frases].
   ```

3. Proyecto en marcha, en una conversación nueva con el dossier pegado debajo:

   ```text
   Oye Amenábar, sigue mi proyecto. ¿Qué toca ahora?
   ```

4. Cada respuesta termina con un **Siguiente paso** y la frase exacta para pegar. El director no ejecuta nada por su cuenta: espera tu orden.
5. Aprueba o corrige en cualquier fase: `Aprobado.` o `Cambia X por Y.`

La guía completa, fase por fase, está en `prompt-system/FLUJO-idea-a-storyboard.md`.

## Principios

- **Lo propuesto no es aprobado** hasta que lo digas. Estados: `propuesta` → `prompt escrito` → `imagen generada` → `aprobada`. Un prompt escrito no es una imagen.
- **Prompts pegables en inglés**; explicaciones en tu idioma.
- **Nada de texto dentro de imágenes o vídeo**: títulos y rótulos se añaden en el editor.
- **Datos de terceros** (límites de modelos, controles de herramientas) se marcan como `documentada` o *pendiente de verificar*. Nada se inventa.
- **Una conversación nueva por fase**, con el dossier pegado (plantilla en `PROYECTO.md`).

## Estado

Todo está escrito y comprobado solo por escrito: ninguna skill se ha validado todavía con generaciones reales. `MODELOS.md` y `PLATAFORMAS.md` son borradores que debes contrastar con tu cuenta y con la app antes de fiarte de un límite.

## Estructura

```text
prompt-system/      fuente de las skills y documentos comunes
  pruebas/          casos de prueba escritos
  estilos/          estilos para la skill review
build-dist.py       genera dist/ (no versionado)
check-sync.py       compara la copia instalada con un build nuevo
.claude/skills/     copia instalada para Claude Code
```
