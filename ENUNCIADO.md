# Ejercicio práctico — Bib Up

En Bib Up recibimos calendarios de carreras de varias fuentes. Una misma carrera aparece con nombres, formatos y ciudades distintos, y hay que unificarla.

Te damos dos ficheros:

- `fuente_a_calendario.csv`: calendario tipo federación.
- `fuente_b_agregador.csv`: datos de una web agregadora.

Los datos son de ejemplo: nombres, fechas y precios no tienen por qué coincidir con la realidad.

## Qué tienes que hacer

1. **Normaliza** ambas fuentes a un esquema común: nombre, fecha (ISO), ciudad y distancia en km.
2. **Empareja** las carreras de A con las de B. Para cada par, da un nivel de confianza.
3. **Detecta** duplicados dentro de cada fuente, carreras que solo están en una fuente, y casos dudosos que debería revisar una persona.
4. **Entrega:**
   - Código en Python (Pandas opcional) con instrucciones para ejecutarlo.
   - `resultado.csv` con estas columnas: `a_id, b_id, resultado, confianza, motivo`. Valores de `resultado`: `match`, `match_baja_confianza`, `solo_A`, `solo_B`, `duplicado_A`, `duplicado_B`.
   - Un README corto (máximo 1 página) que explique tu criterio, qué casos te han parecido difíciles y qué mejorarías con más tiempo.

## Requisitos de ejecución

- El código debe recibir las rutas de los ficheros como parámetros y escribir el resultado. Por ejemplo:
  `python main.py --a fuente_a.csv --b fuente_b.csv --out resultado.csv`
- **En la revisión ejecutaremos tu código sobre otro conjunto de datos** con las mismas columnas pero carreras distintas. Constrúyelo para que funcione con datos que no has visto, no solo con estos.

## Condiciones

- Plazo: 72 horas. Tiempo orientativo: 3-4 horas. No hace falta que sea perfecto.
- Puedes usar cualquier librería y herramientas de IA. Si usas IA, dilo. En la revisión te pediremos que expliques cada decisión.
- Entrega en un .zip de tu repositorio Git, **incluyendo la carpeta `.git`** (queremos ver el historial de commits).

Valoramos más el criterio y la claridad que el número de aciertos.
