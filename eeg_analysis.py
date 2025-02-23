import mne
import matplotlib.pyplot as plt

file_path = "/Users/andalu/Desktop/eegmmidb/S001/S001R01.edf"
raw = mne.io.read_raw_edf(file_path, preload=True)
raw.filter(l_freq=1, h_freq=40)

plt.figure(1)
raw.plot(duration=10, n_channels=10, title="Filtered EEG - S001R01")
plt.savefig("raw_eeg.png")
plt.show()

plt.figure(2)
raw.plot_psd(fmax=50)
plt.savefig("psd_plot.png")
plt.show()
