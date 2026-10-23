# PROYECTO (plantilla del dossier)

Un único archivo por defecto. **Secciones largas en archivo aparte:** si `# GUION` o `# DESGLOSE TÉCNICO` crecen y el dossier deja de caber cómodo, pueden vivir en su propio archivo (`guion.md`, `desglose.md`, junto al dossier). El dossier conserva el encabezado de la sección con una línea de puntero (archivo, versión, estado y origen) y una fila en `# ESTADO`; el contenido vive solo en el archivo aparte, nunca duplicado. Las skills lo leen y lo escriben ahí. **`prompts.md`** (junto al dossier) guarda los prompts entregados; ver el final de este archivo. Es una opción, no una obligación: nada se mueve sin que lo pida el usuario. No rellenes todo por obligación para un prompt suelto, y no registres como aprobado lo que solo está propuesto. Cada decisión importante lleva su origen (`pedida` · `propuesta` · `aprobada` · `de referencia` · `documentada`).

---

## # ESTADO
Lo primero que lee el director. Una fila por entregable; se actualiza al cerrar cada paso.

Estados: `propuesta` · `prompt escrito` · `imagen generada` · `aprobada`. Un prompt escrito no es una imagen: solo pasa a `imagen generada` cuando existe el archivo, y a `aprobada` cuando el usuario lo confirma.

| Entregable | Tipo | Estado | Lo justifica (planos) | Prioridad |
|---|---|---|---|---|
| Brief | fase | | | |
| Guion | fase | | | |
| Desglose | fase | | | |
| (PJ01 …) | personaje / vista | | | Alta · Media · Baja |

- Fase actual:
- Siguiente paso:
- Una referencia Alta sin aprobar bloquea la fase de composición.

## # PROYECTO
- Objetivo:
- Público:
- Destino y formato (incluye relación de aspecto):
- Duración objetivo:
- Estilo y marca:
- Dirección visual (opcional; luz · color y paleta · óptica y encuadre general · textura o acabado; referencias de look):
- Restricciones:
- Audio (`sin audio` · `audio externo` · `audio en Magnific`; por defecto `sin audio`):

## # GUION
- Concepto o premisa:
- Sinopsis (si aporta):
- Escenas o bloques:
- Qué vemos / qué oímos:
- Versión y estado de aprobación:

## # RECURSOS
- Identificadores:
- Personajes y rasgos fijos:
- Vestuario y estados narrativos:
- Referencias de expresión (si hacen falta):
- Props y estados:
- Localizaciones y distribución:
- Archivos de referencia (versión, aprobación):

## # DESGLOSE TÉCNICO
Un bloque por plano:
- Escena y plano (`E01-P01`):
- Función:
- Acción:
- Disposición espacial y eje de acción (solo si hay interacción espacial relevante; posiciones de personajes y objetos, acceso, cámara respecto al eje si los cortes lo requieren):
- Encuadre y cámara:
- Duración orientativa:
- Sonido (por tipo; `—` en lo que no aplique; marca «externo» o «Magnific» según `Audio:`):
  - Diálogo / voz en off (texto exacto):
  - Efectos de acción:
  - Ambiente:
  - Música:
- Recursos y estados:
- Actuación (cuando proceda):
- Continuidad:
- Vía de producción:
- Unidad de generación (plano independiente / secuencia):
- Alternativa más sencilla:
- Versión y aprobación:

## # CONFIGURACIÓN
- Modelos disponibles (informativo, sin selección automática):
- Preferencias autorizadas:
- Modelo de la tarea actual:
- Perfil técnico y fecha de comprobación:

## # CAMBIOS PENDIENTES
- Decisión modificada:
- Recursos y planos afectados:
- Revisión necesaria:

---

## prompts.md (registro de prompts)
Archivo aparte, junto al dossier. Es lo que el usuario abre para pegar en la app. Lo escribe la skill que entrega el prompt (REGLAS §9); el dossier solo lleva el estado en `# ESTADO`.

Arriba, una tabla con **lo vigente** (un prompt por fila):

| Entregable | Versión | Estado | Herramienta |
|---|---|---|---|
| (REF-01 hoja A) | v2 | prompt escrito | (imagen) |

Estados: `prompt escrito` · `imagen generada` · `aprobada` · `descartado` · `sustituido`. Debajo, una entrada por prompt, la vigente primero y las anteriores al final:

```
## REF-01 hoja A · v2 — prompt escrito
- Sustituye a: v1 (motivo)
- Herramienta y ajustes: (operación, modelo de la tarea, relación de aspecto…)
- Referencias, en orden: 1. archivo — qué aporta · 2. …
- Prompt (para pegar):
  (bloque de código, en inglés)
- Resultado: (archivo o nombre en la app; vacío hasta que exista)
- Notas: (qué falló o qué se aprobó)
```
