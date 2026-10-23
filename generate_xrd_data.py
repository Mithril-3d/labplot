import os
import numpy as np

os.makedirs("sample_data", exist_ok=True)
np.random.seed(42)

def pseudo_voigt(x, x0, intensity, fwhm, eta=0.5):
    """Pseudo-Voigt peak function"""
    sigma = fwhm / (2 * np.sqrt(2 * np.log(2)))
    gamma = fwhm / 2.0
    gauss = np.exp(-((x - x0) ** 2) / (2 * sigma ** 2))
    lorentz = 1.0 / (1.0 + ((x - x0) / gamma) ** 2)
    return intensity * (eta * lorentz + (1 - eta) * gauss)

# 1. Silicon standard (Sharp peaks, High intensity, Low noise)
x = np.arange(10.0, 80.01, 0.02)
bg = 150 + 200 * np.exp(-x / 15.0) - 0.5 * x
si_peaks = [
    (28.44, 15000, 0.12),  # (111)
    (47.30, 8500, 0.14),   # (220)
    (56.12, 5000, 0.16),   # (311)
    (69.13, 1200, 0.18),   # (400)
    (76.38, 1800, 0.20),   # (331)
]
y1 = bg.copy()
for x0, I, w in si_peaks:
    y1 += pseudo_voigt(x, x0, I, w, eta=0.4)
noise1 = np.random.normal(0, np.sqrt(np.maximum(y1, 1)) * 0.3)
y1 = np.maximum(y1 + noise1, 0)
np.savetxt("sample_data/01_xrd_silicon_standard.csv", np.column_stack([x, y1]),
           delimiter=",", header="2theta_deg,Intensity_Counts", comments="", fmt="%.2f,%.1f")

# 2. Anatase TiO2 nanoparticles (Broadened peaks due to Scherrer effect)
bg2 = 180 + 350 * np.exp(-x / 12.0)
anatase_peaks = [
    (25.28, 8000, 0.75),   # (101)
    (36.95, 800, 0.80),    # (103)
    (37.80, 1800, 0.80),   # (004)
    (38.58, 600, 0.80),    # (112)
    (48.05, 2800, 0.85),   # (200)
    (53.89, 1600, 0.90),   # (105)
    (55.06, 1700, 0.90),   # (211)
    (62.69, 1200, 0.95),   # (204)
    (68.76, 500, 1.00),    # (116)
    (70.31, 450, 1.00),    # (220)
    (75.03, 900, 1.05),    # (215)
]
y2 = bg2.copy()
for x0, I, w in anatase_peaks:
    y2 += pseudo_voigt(x, x0, I, w, eta=0.6)
noise2 = np.random.normal(0, np.sqrt(np.maximum(y2, 1)) * 0.5)
y2 = np.maximum(y2 + noise2, 0)
np.savetxt("sample_data/02_xrd_tio2_anatase_nanoparticles.csv", np.column_stack([x, y2]),
           delimiter=",", header="2theta_deg,Intensity_Counts", comments="", fmt="%.2f,%.1f")

# 3. Rutile TiO2 (Crystalline)
bg3 = 180 + 320 * np.exp(-x / 13.0)
rutile_peaks = [
    (27.44, 9000, 0.22),   # (110)
    (36.09, 4500, 0.24),   # (101)
    (39.19, 700, 0.25),    # (200)
    (41.23, 2100, 0.26),   # (111)
    (44.05, 800, 0.28),    # (210)
    (54.32, 5400, 0.32),   # (211)
    (56.64, 1800, 0.33),   # (220)
    (62.74, 900, 0.36),    # (002)
    (64.04, 850, 0.37),    # (310)
    (69.01, 1600, 0.40),   # (301)
    (69.79, 1300, 0.40),   # (112)
]
y3 = bg3.copy()
for x0, I, w in rutile_peaks:
    y3 += pseudo_voigt(x, x0, I, w, eta=0.5)
noise3 = np.random.normal(0, np.sqrt(np.maximum(y3, 1)) * 0.4)
y3 = np.maximum(y3 + noise3, 0)
np.savetxt("sample_data/03_xrd_tio2_rutile_crystalline.csv", np.column_stack([x, y3]),
           delimiter=",", header="2theta_deg,Intensity_Counts", comments="", fmt="%.2f,%.1f")

# 4. Amorphous silicate glass with incipient nanocrystallites
# Broad amorphous halo centered at 22 deg and a smaller one at 44 deg
halo1 = 3500 * np.exp(-((x - 22.0) ** 2) / (2 * (4.5 ** 2)))
halo2 = 900 * np.exp(-((x - 44.0) ** 2) / (2 * (7.0 ** 2)))
bg4 = 200 + 400 * np.exp(-x / 10.0) + halo1 + halo2

devitrification = [
    (21.98, 900, 0.35),
    (28.42, 350, 0.40),
    (31.46, 420, 0.40),
    (36.11, 280, 0.45),
]
y4 = bg4.copy()
for x0, I, w in devitrification:
    y4 += pseudo_voigt(x, x0, I, w, eta=0.3)
noise4 = np.random.normal(0, np.sqrt(np.maximum(y4, 1)) * 0.5)
y4 = np.maximum(y4 + noise4, 0)
np.savetxt("sample_data/04_xrd_amorphous_glass_with_nucleation.csv", np.column_stack([x, y4]),
           delimiter=",", header="2theta_deg,Intensity_Counts", comments="", fmt="%.2f,%.1f")

# 5. In-situ High-Temperature Series (Phase transition & Thermal lattice expansion)
temperatures = [25, 200, 400, 600, 800]
series_data = [x]
headers = ["2theta_deg"]

for T in temperatures:
    headers.append(f"Intensity_{T}C")
    shift = -0.00045 * (T - 25)
    
    if T <= 400:
        f_anatase = 1.0
        f_rutile = 0.0
    elif T == 600:
        f_anatase = 0.45
        f_rutile = 0.55
    else:  # 800
        f_anatase = 0.05
        f_rutile = 0.95
        
    bg_T = 150 + 250 * np.exp(-x / 12.0)
    y_T = bg_T.copy()
    
    if f_anatase > 0:
        for x0, I, w in anatase_peaks:
            w_eff = max(w * (1.0 - 0.0003 * (T - 25)), 0.25)
            y_T += f_anatase * pseudo_voigt(x, x0 * (1 + shift), I, w_eff, eta=0.6)
            
    if f_rutile > 0:
        for x0, I, w in rutile_peaks:
            w_eff = max(w * (1.0 - 0.0002 * (T - 25)), 0.20)
            y_T += f_rutile * pseudo_voigt(x, x0 * (1 + shift), I, w_eff, eta=0.5)
            
    noise_T = np.random.normal(0, np.sqrt(np.maximum(y_T, 1)) * 0.4)
    y_T = np.maximum(y_T + noise_T, 0)
    series_data.append(y_T)

stacked_series = np.column_stack(series_data)
fmt_list = ["%.2f"] + ["%.1f"] * len(temperatures)
np.savetxt("sample_data/05_xrd_in_situ_temperature_series.csv", stacked_series,
           delimiter=",", header=",".join(headers), comments="", fmt=",".join(fmt_list))

print("Successfully generated 5 XRD CSV datasets in sample_data/")
