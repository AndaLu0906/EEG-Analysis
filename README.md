# EEG Analysis Tool
Analyzes EEG data from PhysioNet.

## Setup
- `pip3 install -r requirements.txt`
- Download data: `python3 download_eeg.py` (~3.4/ GB)
- Run: `python3 eeg_analysis.py`

## Features
- Downloads dataset (~60min at 1MB/s)
- Loads EDF files
- Filters 1-40 Hz
- Plots raw and PSD in one figure

## Data
[PhysioNet EEG](https://physionet.org/content/eegmmidb/)

## Example Output
![EEG Analysis](eeg_analysis.png)

