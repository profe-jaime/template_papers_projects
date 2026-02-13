# Expert Report Project — Marco Causal Unificado

## Descripción General
Este proyecto genera perfiles de expertos en causalidad, prepara propuestas para publicación en revistas Q2/Q3, y crea materiales para solicitar revisión experta. Incluye análisis empíricos reproducibles, revisiones simuladas, y un paquete listo para envío a revisores.

## Estructura de Archivos
- `profiles/`: 20 perfiles de expertos en causalidad (generados automáticamente).
- `improved_proposal/`: Propuesta revisada, metadatos editoriales, figuras (DAG), checklist de envío.
- `empirical/`: Notebooks y scripts para estimación causal (IPTW, DML, TMLE), datos sintéticos, resultados de robustez.
- `reviewer_package/`: Paquete comprimido con propuesta, datos, cuestionario, invitación, revisiones simuladas y expandidas.
- `reviewer_package.zip`: Archivo ZIP listo para envío.

## Instrucciones de Uso
1. Descomprime `reviewer_package.zip` para acceder a los materiales.
2. Revisa `improved_proposal/proposal_v2.md` para la propuesta formal.
3. Ejecuta `empirical/02_estimators.ipynb` para reproducir análisis (requiere Python con dependencias instaladas).
4. Consulta `reviewer_package/simulated_reviews.md` y `expanded_reviews/` para feedback simulado.

## Instalación y Dependencias
Para cada nuevo directorio donde trabajes con este proyecto, instala un ambiente independiente usando `mamba` para evitar conflictos de versiones y desorden con Python.

### Crear y Activar Entorno con Mamba
1. Instala `mamba` si no lo tienes: `conda install mamba -c conda-forge`.
2. Crea el entorno desde `environment.yml`:
   ```bash
   mamba env create -f environment.yml
   ```
3. Activa el entorno:
   ```bash
   mamba activate expert-report-env
   ```
4. Para desactivar: `mamba deactivate`.

Esto asegura un entorno aislado por directorio/proyecto. Si necesitas añadir dependencias, edita `environment.yml` y recrea el entorno.

- Python 3.8+: Entorno incluye numpy, pandas, scikit-learn, statsmodels.
- Opcional: `econml` para DML, `zepid` para TMLE (ya incluidos en el entorno).

## Directorio de Creación
Esta carpeta `expert_report_project` se crea siempre en el directorio raíz del proyecto correspondiente. Por ejemplo:
- Para este caso: `/Users/enriquec/Developer/causal_framework_unificado/expert_report_project`.
- Ajusta el path según tu setup: reemplaza `/Users/enriquec/Developer/causal_framework_unificado` con el directorio de tu proyecto.
- Para cada nuevo directorio, configura un entorno `mamba` independiente siguiendo las instrucciones de "Instalación y Dependencias".

## Próximos Pasos
- Compilar 30 referencias (2015–2025) en `improved_proposal/references.bib`.
- Aplicar feedback simulado al manuscrito final.
- Enviar `reviewer_package.zip` a revisores reales para feedback adicional.

Fecha de generación: Febrero 12, 2026.