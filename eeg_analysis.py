import mne
import matplotlib.pyplot as plt
import numpy as np

file_path = "/Users/andalu/Desktop/eegmmidb/S001/S001R01.edf"
raw = mne.io.read_raw_edf(file_path, preload=True)
raw.filter(l_freq=1, h_freq=40)

# Create figure with subplots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8), height_ratios=[2, 1])
fig.suptitle("EEG Analysis - S001R01", fontsize=14)

# Raw EEG plot (manual plotting on ax1)
data, times = raw[:, :int(10 * raw.info['sfreq'])]  # First 10 seconds
for i in range(min(10, data.shape[0])):  # Plot up to 10 channels
    ax1.plot(times, data[i] + i * 0.001, label=raw.ch_names[i])  # Offset for visibility
ax1.set_title("Filtered EEG (10s)")
ax1.set_xlabel("Time (s)")
ax1.set_ylabel("Amplitude")
ax1.legend(loc="upper right", fontsize=8)

# PSD plot on ax2
psd = raw.compute_psd(fmax=50)
psd.plot(axes=ax2, show=False)  # Compute and plot PSD on ax2
ax2.set_title("Power Spectral Density (PSD)")

plt.tight_layout()
plt.savefig("eeg_analysis.png", dpi=300)
plt.show()
