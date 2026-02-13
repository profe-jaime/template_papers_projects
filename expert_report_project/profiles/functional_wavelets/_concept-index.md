# Índice de Conceptos Wavelets y Functional Data

**Generado:** 2026-02-11
**Estado:** Actualizado con perfiles principales extraídos

---

## CÓMO USAR ESTE ÍNDICE

Este índice organiza conceptos clave de wavelets y análisis funcional según cómo los mencionan diferentes investigadores. Para cada concepto:
1. **Buscar en perfiles** para ver perspectivas específicas
2. **Comparar enfoques** entre investigadores
3. **Identificar debates** donde hay desacuerdos
4. **Encontrar referencias** a papers específicos

---

## CONCEPTOS FUNDAMENTALES

### Wavelet Denoising
- **Fleming**: Estructuras coherentes en finanzas, denoising para preservar patrones
- **Razak**: Comparación DWT vs SWT, denoising adaptativo
- **Chen**: Coeficientes vecinos, thresholding local
- **Donoho**: Thresholding óptimo, universal threshold
- **Wang**: Métodos híbridos wavelet-SVD para imágenes
- **Mallat**: Matching pursuit para sparsidad

### Functional PCA
- **Dey**: Para datos no gaussianos/truncados
- **Ramsay**: Functional principal components, análisis de curvas
- **Silverman**: Smoothing antes de PCA funcional

### Multiresolution Analysis
- **Daubechies**: Fundamentos matemáticos, construcción de bases
- **Donoho**: Aplicaciones prácticas, denoising
- **Meyer**: Teoría de frames y wavelets
- **Mallat**: Algoritmos de descomposición

### Continuous Wavelet Transform
- **Flandrin**: Análisis tiempo-frecuencia óptimo
- **Miladinov**: Señales biomédicas, ECG analysis
- **Malyugina**: Series temporales económicas

---

## CONCEPTOS METODOLÓGICOS

### Wavelet Basis Selection
- **Daubechies**: Wavelets ortogonales compactos
- **Cohen**: Frames redundantes adaptativos
- **Vetterli**: Bases para compresión óptima

### Functional Smoothing
- **Ramsay**: B-splines smoothing
- **Silverman**: Métodos adaptativos no paramétricos
- **Fleming**: Smoothing para datos funcionales irregulares

### Boundary Effects
- **Daubechies**: Problemas de boundary en wavelets
- **Rioul**: Algoritmos eficientes para boundaries
- **Vetterli**: Oversampling para evitar efectos

### Software Implementation
- **Rioul**: Algoritmos fast wavelet transform
- **Vetterli**: MATLAB Sampling Toolbox
- **Flandrin**: Time-Frequency Toolbox

---

## CONCEPTOS APLICADOS

### Data Preprocessing
- **Wang**: Denoising híbrido para imágenes médicas
- **Miladinov**: Preprocesamiento de señales cardíacas
- **Malyugina**: Análisis multiresolución de datos económicos

### Feature Interpretation
- **Fleming**: Interpretación de coeficientes wavelet en finanzas
- **Ramsay**: Componentes principales funcionales
- **Mallat**: Sparse representations

### Integration with ML
- **Donoho**: Wavelets como preprocesamiento para ML
- **Mallat**: Dictionary learning con wavelets
- **Cohen**: Frames para machine learning

### Domain-Specific Adaptation
- **Miladinov**: Wavelets para cardiología
- **Malyugina**: Wavelets para econometría
- **Wang**: Wavelets para procesamiento de imágenes

---

## DEBATES Y CONTROVERSIAS

### Theory vs Application Balance
- **Daubechies/Meyer**: Énfasis en fundamentos matemáticos
- **Donoho/Fleming**: Balance práctico para aplicaciones
- **Mallat/Rioul**: Enfoque algorítmico-computacional

### Statistical Validation
- **Silverman**: Métodos estadísticos rigurosos
- **Ramsay**: Validación con datos funcionales reales
- **Donoho**: Universal thresholds vs adaptativos

### Scalability Concerns
- **Vetterli**: Teoría de muestreo para big data
- **Rioul**: Algoritmos eficientes para tiempo real
- **Flandrin**: Métodos para señales largas

### Interpretability
- **Fleming**: Interpretación financiera de coeficientes
- **Ramsay**: Interpretación biológica de componentes
- **Mallat**: Interpretación física de descomposiciones

---

## MATRIZ DE PERSPECTIVAS

| Concepto | Daubechies | Donoho | Mallat | Ramsay | Silverman | Meyer | Flandrin | Vetterli |
|----------|------------|--------|--------|--------|-----------|--------|----------|----------|
| **Wavelet Theory** | ⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐ | ⭐ | ⭐ | ⭐⭐⭐ | ⭐⭐ | ⭐⭐ |
| **Applications** | ⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐ | ⭐ | ⭐⭐⭐ | ⭐⭐⭐ |
| **Algorithms** | ⭐⭐ | ⭐⭐ | ⭐⭐⭐ | ⭐ | ⭐ | ⭐ | ⭐⭐ | ⭐⭐⭐ |
| **Statistics** | ⭐ | ⭐⭐ | ⭐ | ⭐⭐⭐ | ⭐⭐⭐ | ⭐ | ⭐⭐ | ⭐ |
| **Software** | ⭐⭐ | ⭐⭐ | ⭐⭐ | ⭐⭐ | ⭐⭐ | ⭐ | ⭐⭐ | ⭐⭐ |

⭐ = Énfasis menor, ⭐⭐ = Énfasis moderado, ⭐⭐⭐ = Énfasis fuerte

---

## INSTRUCCIONES PARA ACTUALIZAR

1. **Después de extraer cada perfil:**
   - Identificar conceptos clave mencionados
   - Extraer citas relevantes
   - Documentar posturas específicas

2. **Para cada concepto en este índice:**
   - Buscar en todos los perfiles completados
   - Resumir perspectivas diferentes
   - Señalar acuerdos y desacuerdos

3. **Mantener actualizado:**
   - Revisar mensualmente
   - Agregar nuevos conceptos según perfiles
   - Actualizar matriz de perspectivas

---

## PRÓXIMOS PASOS

1. [x] Extraer perfiles principales de wavelets/FDA
2. [ ] Completar perfiles restantes del archivo wavelet.md
3. [ ] Actualizar _processing-log.md
4. [ ] Probar sistema con consultas de prueba
5. [ ] Integrar con workflows de Copilot

---

## NOTAS

- Este índice se actualiza manualmente después de extraer perfiles
- Usar `search-tda-profiles.py` para búsquedas específicas
- Mantener coherencia con `_processing-log.md`
- Integrar con `copilot-instructions.md` cuando esté completo