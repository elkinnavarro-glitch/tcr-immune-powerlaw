# TCR Immune PowerLaw

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
![Python Version](https://img.shields.io/badge/python-3.8+-blue)
![Status](https://img.shields.io/badge/status-alpha-orange)

A Python package for **power-law analysis of TCR clonotypes and immune dynamics**. Implements heavy-tailed distribution fitting with robust statistical inference and neutral model comparison using the methodology of Clauset, Shalizi & Newman (2009).

## Features

- **Robust Power-Law Fitting**: Implementation of CSN methodology for accurate α and x_min estimation
- **Bootstrap Inference**: Confidence intervals and sensitivity analysis for fitted parameters
- **Model Comparison**: Likelihood ratio tests against lognormal, exponential, and truncated power-law alternatives
- **Neutral Models**: Comparison with Yule process and pure-birth models to test deviations from neutrality
- **Data Loaders**: Direct integration with VDJdb and MSK-IMPACT TCGAdatabases
- **Publication-Ready Visualizations**: CCDF plots, bootstrap distributions, and robustness analysis

## Installation

### From GitHub (Development)

```bash
git clone https://github.com/elkinnavarro-glitch/tcr-immune-powerlaw
cd tcr-immune-powerlaw
pip install -e .
```

### With Development Dependencies

```bash
pip install -e ".[dev]"
```

## Quick Start

```python
from immunepack.powerlaw.fitting import fit_powerlaw_robust
from immunepack.powerlaw.visualization import plot_distribution_comparison

# Load your TCR clonotype frequency data
import pandas as pd
data = pd.read_csv('tcr_frequencies.csv')['frequency'].values

# Fit power-law model
results = fit_powerlaw_robust(data, discrete=True, verbose=True)

print(f"Exponent α: {results['alpha']:.3f}")
print(f"Threshold x_min: {results['xmin']}")
print(f"Kolmogorov-Smirnov D: {results['ks_stat']:.4f}")
print(f"p-value (KS test): {results['ks_pval']:.4f}")

# Plot results
fig = plot_distribution_comparison(
    data=data,
    results=results,
    save_path='power_law_fit.png'
)
```

## Core Modules

### `immunepack.powerlaw`
Robust power-law fitting and analysis:
- `fitting.py`: Core fitting algorithms with bootstrap inference
- `comparison.py`: Model comparison against alternative distributions  
- `visualization.py`: Publication-quality plots

### `immunepack.models`
Neutral and evolutionary models:
- `yule_process.py`: Pure-birth process simulation and comparison

### `immunepack.loaders`
Data ingestion from public databases:
- `vdjdb.py`: VDJdb TCR-epitope data loader
- `tcga.py`: MSK-IMPACT TP53 mutation loader

### `immunepack.pipelines`
End-to-end analysis workflows:
- `heavy_tailed_analysis.py`: Complete power-law analysis pipeline

## Use Cases

### TCR Immune Repertoire Analysis
Analyze clonotype frequency distributions in T-cell repertoires:

```python
from immunepack.loaders.vdjdb import load_vdjdb_ebv_data
from immunepack.pipelines.heavy_tailed_analysis import run_full_analysis

tcr_data = load_vdjdb_ebv_data(local_path='/path/to/vdjdb')
results = run_full_analysis(tcr_data, output_dir='results/')
```

### Mutation Burden Analysis
Examine power-law properties of somatic mutations:

```python
from immunepack.loaders.tcga import load_msk_impact_tp53

tp53_mutations = load_msk_impact_tp53(cancer_type='OV')
results = fit_powerlaw_robust(tp53_mutations['mutation_counts'].values)
```

## Documentation

For detailed documentation, see:
- [Package Structure](./PACKAGE_STRUCTURE.md) - Complete module breakdown
- [Installation Guide](./docs/installation.md) - Setup and troubleshooting
- [API Reference](./docs/api_reference.md) - Function signatures and parameters
- [Methodology](./docs/methodology.md) - Statistical details and theory

## Dependencies

- numpy >= 1.20.0
- pandas >= 1.3.0  
- scipy >= 1.7.0
- scikit-learn >= 1.0.0
- matplotlib >= 3.4.0
- seaborn >= 0.11.0
- powerlaw >= 1.4.6

## Citation

If you use this package in your research, please cite:

```bibtex
@software{navarro2025tcr,
  title={tcr-immune-powerlaw: Power-law analysis of TCR clonotypes and immune dynamics},
  author={Navarro, Elkin},
  year={2025},
  url={https://github.com/elkinnavarro-glitch/tcr-immune-powerlaw}
}
```

## References

- Clauset, A., Shalizi, C. R., & Newman, M. E. (2009). "Power-law distributions in empirical data." *SIAM review*, 51(4), 661-703.
- Antimonov, D., Pogorelyuk, V., & Pyzik, P. (2022). "VDJdb: a curated database of T-cell receptor sequences..." *Nucleic acids research*, 50(D1), D1047-D1053.

## License

MIT License - see [LICENSE](./LICENSE) for details.

## Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Contact

Elkin Navarro - [@elkinnavarro-glitch](https://github.com/elkinnavarro-glitch)

Universidad Simón Bolívar, Barranquilla, Colombia

---

**Note**: This package is in **alpha** stage. APIs may change before v1.0 release. For feedback or issues, please open a GitHub issue.
