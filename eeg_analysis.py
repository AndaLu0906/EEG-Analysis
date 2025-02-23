import mne
import matplotlib.pyplot as plt

# Load data from absolute path
file_path = "/Users/andalu/Desktop/eegmmidb/S001/S001R01.edf"
raw = mne.io.read_raw_edf(file_path, preload=True)

# Filter data (1-40 Hz)
raw.filter(l_freq=1, h_freq=40)

# Plot raw data and PSD
raw.plot(duration=10, n_channels=10, title="Filtered EEG - S001R01")
raw.plot_psd(fmax=50)
plt.show()
