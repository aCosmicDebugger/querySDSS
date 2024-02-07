# QuerySDSS - Retrieve and Analyze SDSS Data

QuerySDSS is a Python script that utilizes the Astropy and Astroquery libraries to retrieve data from the Sloan Digital Sky Survey (SDSS) Data Release 18 (DR18). This script fetches information about celestial objects including their nature (galaxy, star, quasar), redshift, coordinates, positions, and flux values.

## Requirements

- Python 3.x
- Astroquery
- Astropy

You can install the required packages using the following command:

```bash
pip install astroquery astropy
```

## How to Install

Clone this repository to your local machine using the following command:
```bash
git clone https://github.com/aCosmicDebbuger/querySDSS.git
cd querySDSS
```
or you can use pip

```bash
pip install querySDSS
```

## Usage:

Just opena a terminal where the file is located and run

```bash
python3 querySDSS.py
```

or if you need to import it:
```python
from querySDSS.querySDSS.querySDSS import query_sdss_data

a = query_sdss_data(num_observations=3000)
print(a)
```



You'll get a table of SDSS data.
