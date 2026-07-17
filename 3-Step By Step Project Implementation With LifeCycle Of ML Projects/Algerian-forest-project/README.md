# Forest Fire Weather Index (FWI) Prediction

A machine learning web application that predicts the **Fire Weather Index (FWI)** — a composite score indicating how readily a fire could ignite and spread — using real-time weather and fuel-moisture readings. Built with a regression model trained on the **Algerian Forest Fires Dataset** and served through a Flask web interface.

---

## Overview

Forest fires are strongly influenced by weather conditions and fuel dryness. The **Canadian Forest Fire Weather Index (FWI) System** combines several sub-indices — each capturing a different aspect of fire danger — into scores that fire management agencies use to anticipate risk. This project trains a regression model to predict the final FWI score directly from raw weather observations and intermediate FWI components, then exposes the model through a simple web form.

## Dataset

**Source:** Algerian Forest Fires Dataset

The dataset contains **244 instances** covering two regions of Algeria over the period **June 2012 to September 2012**:

| Region | Location | Instances |
|---|---|---|
| Bejaia | Northeast Algeria | 122 |
| Sidi Bel-abbes | Northwest Algeria | 122 |

Of the 244 total instances, **138 are classified as Fire** and **106 as Not Fire**.

### Attributes

| # | Attribute | Description | Range |
|---|---|---|---|
| 1 | Date | Day, month (June–September), year (2012) | — |
| 2 | Temperature | Noon temperature (max) in °C | 22 – 42 |
| 3 | RH | Relative Humidity (%) | 21 – 90 |
| 4 | Ws | Wind speed (km/h) | 6 – 29 |
| 5 | Rain | Total rainfall for the day (mm) | 0 – 16.8 |
| 6 | FFMC | Fine Fuel Moisture Code | 28.6 – 92.5 |
| 7 | DMC | Duff Moisture Code | 1.1 – 65.9 |
| 8 | DC | Drought Code | 7 – 220.4 |
| 9 | ISI | Initial Spread Index | 0 – 18.5 |
| 10 | BUI | Buildup Index | 1.1 – 68 |
| 11 | FWI | Fire Weather Index *(target for regression)* | 0 – 31.1 |
| 12 | Classes | Fire / Not Fire | binary |

**Encoding used in this app:**
- `Classes` → `0 = Not Fire`, `1 = Fire`
- `Region` → `0 = Bejaia`, `1 = Sidi Bel-abbes`

## Project Structure

```
├── artifacts/              # Saved model & preprocessing objects (pickle files)
├── notebook/                # EDA and model training notebooks
├── src/
│   ├── components/          # Data ingestion, transformation, model training
│   ├── pipeline/             # Prediction pipeline
│   └── utils.py
├── templates/
│   ├── index.html            # Landing page
│   └── home.html              # Prediction form + result
├── application.py             # Flask app entry point
├── requirements.txt
└── README.md
```

## How It Works

1. **Input:** The user submits weather readings and FWI sub-component values through the web form (`Temperature`, `RH`, `Ws`, `Rain`, `FFMC`, `DMC`, `ISI`, `Classes`, `Region`).
2. **Preprocessing:** Inputs are scaled using the same scaler fit during training.
3. **Prediction:** The trained regression model estimates the FWI score.
4. **Output:** The predicted FWI value is displayed back to the user on the same page.

## Tech Stack

- **Python** — model training and backend logic
- **Flask** — web framework serving the prediction endpoint
- **scikit-learn** — regression model and preprocessing (scaler)
- **Pandas / NumPy** — data handling
- **HTML/CSS** — front-end form and result display

## Getting Started

### Prerequisites
- Python 3.8+
- pip

### Installation

```bash
git clone <repository-url>
cd <repository-folder>
pip install -r requirements.txt
```

### Run the app

```bash
python application.py
```

Then open `http://127.0.0.1:5000` in your browser.

### Usage

1. Navigate to the prediction page.
2. Enter the required weather and FWI component values.
3. Select the appropriate **Classes** and **Region** options.
4. Click **Run Prediction** to view the predicted FWI score.

## Model

The regression model was trained on the 244-instance Algerian Forest Fires dataset after cleaning and merging the two regional subsets, with `FWI` as the continuous target variable. Feature scaling was applied prior to training, and the fitted scaler and model are serialized for use at inference time.

## Acknowledgements

- **Dataset:** Algerian Forest Fires Dataset, covering the Bejaia and Sidi Bel-abbes regions (June–September 2012).
- **FWI System:** Based on the Canadian Forest Fire Weather Index (FWI) System methodology.

## License

This project is intended for educational and research purposes.