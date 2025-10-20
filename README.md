# A quantitative evaluation of Optical vs. SAR-based Wave Kinematic Bathymetry (WKB) for deriving ocean depth in the surf-zone

## Project overview
The goal of this project is to derive bathymetric maps by WKB from both optical and SAR imagery from four environmentally diverse coastal areas, then use high-resolution multibeam echosounder (MBES) survey for ground-truthing to compute the Root Mean Square Error (RMSE) for each map, to determine the strengths and weaknesses of each method.

- Step 1: Determine four Areas of Interest (AOI)

    - Select for available NCEI MBES bathymetry DEMs at a variety of locations with diverse environmental conditions, and identify coordinates for a bounding box
        - Latitude
        - Exposure to marine processes
        - Seafloor features (reefs, sandbars, canyons, heavy slope)

    - Compile a list of time windows around NCEI MBES survey time with active swell, filter for a variety of parameters
        - Use WaveWatch III and Copernicus Marine Service models to filter for
            - Wave height
            - Period
            - Direction

- Step 2: Find, load, and match datasets

    - Filter potential datasets based on AOI bounding box and list of time windows

    - Load Sentinel 1, Sentinel 2, and NCEI datasets datasets

    - Match the dimensionality (Datum / CRS / Projection) for each dataset so overlayed pixels correspond spatially

- Step 4: Derive bathymetry

    - Optical
        - Randon transform > discrete Fourier transform > wave celerity > linear dispersion [1]

    - SAR
        - 2D Fast Fourier transform > wavelength estimation > linear dispersion [2]

    - Generate map figures for each

- Step 5: Evaluation

    - Record wave characteristics from wave model.

    - Calculate “visibility index” based on the unique requirements for identifying surface waves from optical and SAR imagery.
        - Sentinel 2 - Glint score & cloud coverage
        - Sentinel 1 - Backscatter and L-min

    - Compute root mean squared difference for each bathymetric derivation against MBES DEM.

    - Generate a difference map using RMS error for each pixel

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