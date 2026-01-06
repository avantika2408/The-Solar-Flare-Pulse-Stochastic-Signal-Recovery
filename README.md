# The-Solar-Flare-Pulse-Stochastic-Signal-Recovery
Bayesian inference of a stellar flare time series using a physically motivated analytical model. Metropolis–Hastings MCMC is used to estimate the flare amplitude, quench time, and oscillation frequency from noisy data, with trace plots, posteriors, and MAP estimates provided.

## Requirements
Install project dependencies listed in `requirements.txt` (recommended in a virtual environment):

PowerShell commands:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

> Note: `cobaya` (the MCMC framework) and `getdist` are required for running the notebook end-to-end.

## Run instructions

1. Ensure the dataset `flare_data.csv` is present in the repository root.
2. Activate the virtual environment (see commands above).
3. Start Jupyter Notebook and open `mcmc.ipynb`:

```powershell
jupyter notebook mcmc.ipynb
```

4. Walk through cells in `mcmc.ipynb` to:
	- Load and visualize the data
	- Configure the Cobaya run (sampling options are in the notebook)
	- Run MCMC (this may take a while depending on `Max_Samples`)
	- Generate trace plots, posterior plots, and the MAP best-fit

5. Output and chain files are written to `stats/chains/Flare/` (see filename root `poly_deg{n}`).

## 💡 Tips
- If you only want to view previously computed results, skip the Cobaya sampling cells and run the plotting cells that read from `stats/chains/Flare/`.
- Use `Burn_In` and `Max_Samples` settings in the notebook to control sampling and plotting behavior.
