# TCR Immune PowerLaw - Estructura del Paquete

## Descripción General

`tcr-immune-powerlaw` es un paquete Python para análisis de colas pesadas (power-law) en clonotipos TCR y dinámica inmunológica. Implementa ajuste robusto de power-law con inferencia bootstrap y comparación con modelos neutros.

**Repositorio:** https://github.com/elkinnavarro-glitch/tcr-immune-powerlaw
**Versión:** 0.1.0
**Licencia:** MIT

---

## Estructura del Proyecto

```
tcr-immune-powerlaw/
├── immunepack/                      # Paquete principal
│   ├── __init__.py                  # Inicializador del paquete
│   │
│   ├── powerlaw/                    # Módulo de análisis power-law
│   │   ├── __init__.py
│   │   ├── fitting.py               # Funciones de ajuste robusto
│   │   │   └── fit_powerlaw_robust()
│   │   │   └── bootstrap_alpha()
│   │   │   └── sensitivity_analysis_xmin()
│   │   │   └── subsampling_stability()
│   │   ├── comparison.py            # Comparación con alternativas
│   │   │   └── compare_to_lognormal()
│   │   │   └── compare_to_exponential()
│   │   │   └── compare_to_truncated_powerlaw()
│   │   ├── visualization.py         # Visualización
│   │   │   └── plot_distribution_comparison()
│   │   │   └── plot_robustness_analysis()
│   │   │   └── plot_bootstrap_intervals()
│   │   └── utils.py                 # Utilidades
│   │       └── estimate_xmin()
│   │       └── calculate_kolmogorov_smirnov()
│   │
│   ├── models/                      # Modelos matemáticos
│   │   ├── __init__.py
│   │   ├── yule_process.py          # Proceso de Yule
│   │   │   └── simulate_yule_process()
│   │   │   └── compare_to_neutral_model()
│   │   └── evolutionary_models.py   # Otros modelos
│   │
│   ├── loaders/                     # Cargadores de datos
│   │   ├── __init__.py
│   │   ├── vdjdb.py                 # Cargador VDJdb
│   │   │   └── load_vdjdb_ebv_data()
│   │   │   └── filter_by_antigen()
│   │   └── tcga.py                  # Cargador TCGA/MSK-IMPACT
│   │       └── load_msk_impact_tp53()
│   │       └── load_tp53_by_cancer_type()
│   │
│   ├── utils/                       # Utilidades generales
│   │   ├── __init__.py
│   │   ├── data_utils.py            # Procesamiento de datos
│   │   │   └── normalize_data()
│   │   │   └── remove_outliers()
│   │   └── file_io.py               # E/S de archivos
│   │       └── save_results()
│   │       └── load_results()
│   │
│   └── pipelines/                   # Pipelines integrados
│       ├── __init__.py
│       ├── heavy_tailed_analysis.py # Pipeline principal
│       │   └── run_full_analysis()
│       │   └── run_bootstrap_analysis()
│       └── tcr_dynamics.py          # Análisis específico TCR
│           └── analyze_tcr_clonotypes()
│
├── tests/                           # Tests unitarios
│   ├── __init__.py
│   ├── test_powerlaw.py
│   ├── test_models.py
│   ├── test_loaders.py
│   └── test_pipelines.py
│
├── examples/                        # Ejemplos y notebooks
│   ├── quick_start.py               # Script rápido
│   ├── quick_start.ipynb            # Notebook Jupyter
│   └── full_analysis_tcr_ebv.ipynb  # Análisis completo TCR EBV
│
├── docs/                            # Documentación
│   ├── installation.md              # Guía de instalación
│   ├── api_reference.md             # Referencia de API
│   ├── tutorial.md                  # Tutorial
│   ├── methodology.md               # Detalles metodológicos
│   └── examples/                    # Ejemplos documentados
│
├── README.md                        # Descripción del proyecto
├── setup.py                         # Configuración setuptools
├── pyproject.toml                   # Configuración PEP 517/518
├── requirements.txt                 # Dependencias pip
├── requirements-dev.txt             # Dependencias desarrollo
├── .gitignore                       # Excepciones Git
├── LICENSE                          # Licencia MIT
├── PACKAGE_STRUCTURE.md             # Este archivo
└── .github/
    └── workflows/
        └── tests.yml                # CI/CD con GitHub Actions
```

---

## Módulos Principales

### 1. `immunepack.powerlaw` - Análisis Power-Law

Núcleo del análisis de colas pesadas:

```python
from immunepack.powerlaw.fitting import fit_powerlaw_robust

results = fit_powerlaw_robust(
    data=clonotype_frequencies,
    discrete=True,
    verbose=True
)

print(f"Alpha: {results['alpha']:.3f} ± {results['alpha_ci']}")
print(f"KS: {results['ks_stat']:.4f}")
```

### 2. `immunepack.models` - Modelos Neutros

Comparación con modelos de referencia:

```python
from immunepack.models.yule_process import compare_to_neutral_model

p_value, observed_alpha, neutral_alphas = compare_to_neutral_model(
    data=data,
    n_simulations=1000
)
```

### 3. `immunepack.loaders` - Cargadores de Datos

Acceso a fuentes de datos públicas:

```python
from immunepack.loaders.vdjdb import load_vdjdb_ebv_data

tcr_data = load_vdjdb_ebv_data(local_path='/data/vdjdb')
```

### 4. `immunepack.pipelines` - Pipelines Integrados

Análisis end-to-end:

```python
from immunepack.pipelines.heavy_tailed_analysis import run_full_analysis

results = run_full_analysis(
    tcr_file='tcr_data.csv',
    output_dir='results/',
    plot=True
)
```

---

## Instalación

### Desde GitHub (desarrollo)

```bash
git clone https://github.com/elkinnavarro-glitch/tcr-immune-powerlaw
cd tcr-immune-powerlaw
pip install -e .
```

### Con dependencias de desarrollo

```bash
pip install -e ".[dev]"
```

---

## Próximos Pasos

- [ ] Implementar módulos powerlaw/* (fitting, comparison, visualization)
- [ ] Implementar módulos models/* (Yule, evolutionary models)
- [ ] Implementar loaders/* (VDJdb, TCGA/MSK-IMPACT)
- [ ] Crear tests unitarios completos
- [ ] Agregar ejemplos Jupyter notebooks
- [ ] Configurar CI/CD (GitHub Actions)
- [ ] Escribir documentación Sphinx
- [ ] Publicar en PyPI

---

## Dependencias

- numpy >= 1.20.0
- pandas >= 1.3.0
- scipy >= 1.7.0
- scikit-learn >= 1.0.0
- matplotlib >= 3.4.0
- seaborn >= 0.11.0
- powerlaw >= 1.4.6

---

## Referencias

- Clauset, A., Shalizi, C. R., & Newman, M. E. (2009). Power-law distributions in empirical data. SIAM review, 51(4), 661-703.
- Antimonov, D., Pogorelyuk, V., & Pyzik, P. (2022). VDJdb: a curated database of T-cell receptor sequences with known antigen specificity. Nucleic acids research, 50(D1), D1047-D1053.
