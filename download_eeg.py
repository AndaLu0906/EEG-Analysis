import os
import subprocess

folder = "eegmmidb"
os.makedirs(folder, exist_ok=True)
base_url = "https://physionet.org/files/eegmmidb/1.0.0/"
subprocess.run(["/Users/andalu/homebrew/bin/wget", "-r", "-np", "-nH", "--cut-dirs=3", "-P", folder, base_url])