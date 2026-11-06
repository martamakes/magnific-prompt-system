# PROYECTO (plantilla del dossier)

Un único archivo por defecto. **Secciones largas en archivo aparte:** si `# GUION` o `# DESGLOSE TÉCNICO` crecen y el dossier deja de caber cómodo, pueden vivir en su propio archivo (`guion.md`, `desglose.md`, junto al dossier). El dossier conserva el encabezado de la sección con una línea de puntero (archivo, versión, estado y origen) y una fila en `# ESTADO`; el contenido vive solo en el archivo aparte, nunca duplicado. Las skills lo leen y lo escriben ahí. **`prompts.md`** (junto al dossier) guarda los prompts entregados; ver el final de este archivo. Es una opción, no una obligación: nada se mueve sin que lo pida el usuario. No rellenes todo por obligación para un prompt suelto, y no registres como aprobado lo que solo está propuesto. Cada decisión importante lleva su origen (`pedida` · `propuesta` · `aprobada` · `de referencia` · `documentada`).

---

## # ESTADO
Lo primero que lee el director. Una fila por entregable; se actualiza al cerrar cada paso.

**Tres ejes de estado, que no se mezclan** (un estado de un eje nunca vale por el de otro):
- **Documento** (brief, guion, desglose, plan de montaje, animática, lista de acabado): `propuesta` → `aprobada`. Aprueba el usuario.
- **Recurso** (referencia, imagen, clip, audio): `prompt escrito` → `generado` → `revisado` → `aprobada` o `descartado`. Un prompt escrito no es un archivo: pasa a `generado` cuando existe el archivo (`imagen generada` es el mismo paso para imágenes) y a `revisado` y `aprobada` solo con lo que el usuario ha visto u oído.
- **Entrega** (la pieza): `en montaje` → `en revisión` → `correcciones` → `exportado` → `verificado`. `exportado` y `verificado` (archivo reproducido completo) los confirma el usuario con evidencia.

| Entregable | Tipo (documento · recurso · entrega) | Estado (del eje de su tipo) | Lo justifica (planos) | Prioridad |
|---|---|---|---|---|
| Brief | fase | | | |
| Guion | fase | | | |
| Desglose | fase | | | |
| Animática | fase | | | |
| Primer montaje | fase | | | |
| Acabado y entrega | fase | | | |
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
- Audio (`sin audio` · `audio externo` · `audio en Magnific`; si no consta, `sin audio`; el brief propone según el objetivo y lo marca `propuesta`):
  - Qué se oye (voz · efectos · ambiente · música) y cómo se produce cada uno:
- Alcance (100 % generativa · híbrida, con material propio):
- Recursos disponibles (créditos o presupuesto, herramientas, material del usuario):
- Plazo:
- Reserva para regenerar:
- Criterio de éxito:

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

## # PROCEDENCIA
Una fila por recurso que no se genera desde cero ni es del usuario, y por cada referencia que podría llegar a la pieza final:

| Recurso | Papel (referencia · recurso final) | Origen y titular | Condiciones de uso | Autorización | Estado |
|---|---|---|---|---|---|

Estados: `consta` · `pendiente de verificar`. Una referencia que solo guía el aspecto no es un recurso final. Sin autorización conocida de un tercero (marca, voz, música, persona), no se da por permitido.

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

## produccion.md (registro de producción)
Archivo aparte, junto al dossier; empieza cuando se genera el primer clip o sonido. Lo mantiene el usuario o la skill que reciba sus datos; nada se inventa: el coste y la duración real los trae el usuario.

| Archivo | Versión | Plano o pieza | Duración real | Intervalo útil | Coste | Saldo | Estado |
|---|---|---|---|---|---|---|---|
| (E01-P02-v2.mp4) | v2 | E01-P02 | 5,1 s | 0:00–3:20 | | | elegido · descartado · pendiente |

El saldo se compara con la reserva del brief. El intervalo útil lo usa `edit-plan` para elegir tramos.

**Borrador primero, calidad final después.** Si el modelo ofrece un modo de borrador (Seedance lista «Draft», `MODELOS.md`), itera en él y pasa a la calidad final solo la toma elegida. El modo no es un estado: se anota en la columna Versión (`v2 · Draft`, `v2 · 1080p`) y el Estado sigue siendo el de siempre. Los intentos en borrador que se descartan también llevan su fila y su coste, para que el saldo sea real. Criterio del caso de Magnific (Originals «Smoke»); `documentada` como caso. Ese mismo caso declara unas 9 generaciones por plano final: úsalo solo como orden de magnitud al fijar la reserva del brief, nunca como norma ni como cifra de tu modelo.

## prompts.md (registro de prompts)
Archivo aparte, junto al dossier. Es lo que el usuario abre para pegar en la app. Lo escribe la skill que entrega el prompt (REGLAS §9); el dossier solo lleva el estado en `# ESTADO`.

Arriba, una tabla con **lo vigente** (un prompt por fila):

| Entregable | Versión | Estado | Herramienta |
|---|---|---|---|
| (REF-01 hoja A) | v2 | prompt escrito | (imagen) |

Estados (eje recurso): `prompt escrito` · `generado` (`imagen generada`) · `revisado` · `aprobada` · `descartado` · `sustituido`. Debajo, una entrada por prompt, la vigente primero y las anteriores al final:

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
