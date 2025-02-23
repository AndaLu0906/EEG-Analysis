import mne
import matplotlib.pyplot as plt

# Load data
file_path = "/Users/andalu/Desktop/eegmmidb/S001/S001R01.edf"
raw = mne.io.read_raw_edf(file_path, preload=True)

# Filter
raw.filter(l_freq=1, h_freq=40)

# Plot and save raw EEG
raw.plot(duration=10, n_channels=10, title="Filtered EEG - S001R01")
plt.savefig("plot.png")  # Saves the plot as plot.png
plt.close()  # Closes the figure to free memory

# Optional: Show PSD interactively
raw.plot_psd(fmax=50)
plt.show()
