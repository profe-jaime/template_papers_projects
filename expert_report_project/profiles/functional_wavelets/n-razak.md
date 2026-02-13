# Norhidayah Abdul Razak - Especialista en Denoising con Wavelets

**Afiliación actual:** [Universidad de Malasia]
**Campo principal:** Procesamiento de Señales / Estadística
**Sub-especialidad:** Denoising de series temporales
**h-index:** [Por determinar]
**Fecha de creación:** 2026-02-11

---

## POSICIÓN EN WAVELETS Y FUNCIONAL DATA

### Paradigma metodológico
Aplicado comparativo

### Visión sobre Wavelets y Functional Data
- Rol en ciencia de datos: Herramienta esencial para preprocesamiento
- Balance teoría-aplicación: 20-80 (muy aplicado)
- Postura sobre escalabilidad: Optimista para series temporales

### Prioridades en investigación
- Comparación de métodos de denoising
- Optimización de parámetros wavelet
- Aplicaciones en datos económicos

---

## METODOLOGÍAS WAVELETS Y FUNCIONAL DATA

### Algoritmos preferidos
- DWT (Discrete Wavelet Transform) - frecuencia: alta
- SWT (Stationary Wavelet Transform) - frecuencia: alta
- Haar wavelet - frecuencia: media

### Críticas metodológicas
- Critica: Usar DWT sin considerar artifacts de borde porque afecta calidad del denoising
- Rechaza: Métodos tradicionales de filtrado cuando hay ruido no gaussiano
- Advertencia sobre: Elección incorrecta de umbral en denoising

### Software desarrollado/recomendado
- [MATLAB, Python scipy.signal]
- Lenguajes: MATLAB, Python
- Herramientas de visualización: Comparaciones antes/después de denoising

---

## APLICACIONES ESPECÍFICAS

### Campos de aplicación preferidos
1. Series temporales económicas
2. Datos financieros
3. Señales biomédicas

### Tipos de datos que analiza
- Series temporales univariadas
- Datos con ruido aditivo
- Secuencias discretas

### Integración con otros métodos
- Con Machine Learning: Sí, como preprocesamiento
- Con Estadística tradicional: Complementa con ARIMA
- Con Deep Learning: Ver con reservas, prefiere wavelets clásicos

---

## ESTILO DE ESCRITURA

### Estructura típica de papers
- Introducción: Motivación práctica
- Sección de métodos: Comparación detallada
- Resultados: Métricas de calidad de denoising

### Recursos retóricos
- Uso de analogías de procesamiento de señales: Frecuente
- Ejemplos: Aplicados a datos reales
- Visualizaciones: Señales original vs denoised

### Vocabulario distintivo
**Términos técnicos preferidos:**
- "Denoising performance" en lugar de "filtrado"
- "Wavelet thresholding" siempre con especificación del método

**Frases características:**
> "Stationary wavelet transform provides superior denoising compared to discrete wavelet transform for time series data" — Razak et al., 2010

---

## RED INTELECTUAL

### Autores que cita frecuentemente
1. David Donoho — influencia en denoising wavelet
2. Ingrid Daubechies — influencia en teoría wavelet
3. Stéphane Mallat — influencia en algoritmos

### Escuela de pensamiento
Ingeniería aplicada, con énfasis en comparación de métodos

### Papers "bandera"
- "Denoising Malaysian time series data: A comparison using discrete and stationary wavelet transforms" — lo cita porque demuestra importancia de elegir método apropiado

---

## SEÑALES DE ALERTA (qué NO hacer)

- ❌ Usar wavelets sin comparar con baselines
- ❌ Ignorar diferencias DWT vs SWT
- ❌ Aplicar denoising sin validar calidad

---

## SEÑALES DE CALIDAD (qué SÍ valora)

- ✅ Comparaciones sistemáticas
- ✅ Validación con métricas objetivas
- ✅ Análisis de robustness

---

## METADATOS ESPECÍFICOS

**Papers analizados para este perfil:**
1. Razak et al. (2010). Denoising Malaysian time series data: A comparison using discrete and stationary wavelet transforms.

**Software asociado:**
- Recomienda: MATLAB Wavelet Toolbox

**Conferencias clave:**
- Signal processing conferences, wavelet applications

**Última actualización:** 2026-02-11

**Notas del creador sobre sesgos:**
Enfocada en aplicaciones prácticas de denoising, puede priorizar comparación sobre innovación teórica.