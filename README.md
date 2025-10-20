# A quantitative evaluation of Optical vs. SAR-based Wave Kinematic Bathymetry (WKB) for deriving ocean depth in the surf-zone

## Project overview
The goal of this project is to derive bathymetric maps by WKB from both optical and SAR imagery from four environmentally diverse coastal areas, then use high-resolution multibeam echosounder (MBES) survey for ground-truthing to compute the Root Mean Square Error (RMSE) for each map, to determine the strengths and weaknesses of each method.

- Data
    - Optical - Sentinel-2
    - SAR - Sentinel-1
    - MBES - NOAA NCEI

- Processing
    - Optical
        - Randon transform > discrete fourier transform > wave celerity > linear dispersion [1]
    - SAR
        - 2D Fast fourier transform > wavelength estimation > linear dispersion [2]

- Evaluation
    - RMSE metrics
    - Plots for derived and ground-truth bathymetry

## Setup

Prereqs
- Python 3.11 (recommended)
- Git

Create and activate a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\\Scripts\\activate
```

Install dependencies
```bash
pip install -r requirements.txt
```

Optional: install dev tooling
```bash
pip install pytest ruff black mypy
```

## Works cited

- [1] E. W. J. Bergsma, R. Almar, and P. Maisongrande, “Radon-Augmented Sentinel-2 Satellite Imagery to Derive Wave-Patterns and Regional Bathymetry,” Remote Sensing, vol. 11, no. 16,
p. 1918, Jan. 2019, doi: 10.3390/rs11161918.

- [2] S. D. Mudiyanselage, B. Wilkinson, and A. Abd-Elrahman,
“Automated High-Resolution Bathymetry from Sentinel-1 SAR Images in Deeper Nearshore Coastal Waters in Eastern Florida,” Remote Sensing, vol. 16, no. 1, p. 1, Jan. 2024, doi: 10.3390/rs16010001.

## License

This project is licensed under the MIT License — see the `LICENSE` file for details.
© 2025 Marcel Rodriguez-Riccelli