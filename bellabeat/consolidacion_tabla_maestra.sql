-- =====================================================================
-- Consolidación de tabla maestra: actividad diaria + sueño
-- Proyecto: Caso de Estudio BellaBeat
-- Fuente: FitBit Fitness Tracker Data (Kaggle)
-- Motor: Google Cloud BigQuery
-- =====================================================================

SELECT 
  A.Id,
  A.ActivityDate AS Fecha,
  A.TotalSteps AS PasosTotales,
  A.Calories AS Calorias,
  A.VeryActiveMinutes AS MinutosMuyActivos,
  A.FairlyActiveMinutes AS MinutosModerados,
  A.LightlyActiveMinutes AS MinutosLigerosActividad,
  A.SedentaryMinutes AS MinutosSedentarios,
  PARSE_DATE('%m/%d/%Y', SPLIT(S.SleepDay, ' ')[OFFSET(0)]) AS FechaSueno,
  S.TotalMinutesAsleep AS MinutosDormidos,
  S.TotalTimeInBed AS MinutosEnLaCama

FROM `mi-proyecto-analisis-499721.bellabeat_casestudy.daily_activity` AS A
INNER JOIN `mi-proyecto-analisis-499721.bellabeat_casestudy.sleep_day` AS S
  ON A.Id = S.Id
  AND A.ActivityDate = PARSE_DATE('%m/%d/%Y', SPLIT(S.SleepDay, ' ')[OFFSET(0)]);

-- Resultado: tabla_maestra_bellabeat_v2 — 413 registros, sin valores nulos.
--
-- Nota: una versión anterior de esta query vinculaba por error la columna
-- TotalDistance en lugar de TotalMinutesAsleep para el campo de sueño.
-- Esta versión ya incluye la corrección.
