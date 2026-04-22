import pandas as pd
import numpy as np
import matplotlib as plt

df_cali_nscope = pd.read_csv("372-U1517A_cali-nscope.csv", skiprows = 4)
df_cali_nscope.head()

df_den_nscope = pd.read_csv("372-U1517A_den-nscope.csv", skiprows = 4)
df_den_nscope.head()

df_gr_gvr = pd.read_csv("372-U1517A_gr-gvr.csv", skiprows = 4)
df_gr_gvr.head()

df_gr_scope = pd.read_csv("372-U1517A_gr-nscope.csv", skiprows = 4)
df_gr_scope.head()

df_misc_gvr = pd.read_csv("372-U1517A_misc-gvr.csv", skiprows = 4)
df_misc_gvr.head()

df_por_nscope = pd.read_csv("372-U1517A_por-nscope.csv", skiprows = 4)
df_por_nscope.head()

df_res_atten_nscope = pd.read_csv("372-U1517A_res-atten-nscope.csv", skiprows = 4)
df_res_atten_nscope.head()

df_res_gvr = pd.read_csv("372-U1517A_res-gvr.csv", skiprows = 4)
df_res_gvr.head()

df_res_phase_nscope = pd.read_csv("372-U1517A_res-phase-nscope.csv", skiprows = 4)
df_res_phase_nscope.head()

df_tp_nscope = pd.read_csv("372-U1517A_tp-nscope.csv", skiprows = 4)
df_tp_nscope.head()

df_vel_nscope = pd.read_csv("372-U1517A_vel-sscope.csv", skiprows = 4)
df_vel_nscope.head()

df_cali_nscope = df_cali_nscope[["DEPTH_LSF", "UCAV"]]
df_den_nscope = df_den_nscope[["DEPTH_LSF", "RHON"]]
df_por_nscope = df_por_nscope[["DEPTH_LSF", "BPHI", "TNPH"]]
df_vel_nscope = df_vel_nscope[["DEPTH_LSF", "VCO", "VSH"]]
df_gr_gvr = df_gr_gvr[["DEPTH_LSF", "GR_RAB"]]
df_gr_scope = df_gr_scope[["DEPTH_LSF", "GRMA"]]
df_res_phase_nscope = df_res_phase_nscope[["DEPTH_LSF", "P16B"]]
df_res_atten_nscope = df_res_atten_nscope[["DEPTH_LSF", "A40B"]]

combined = df_cali_nscope
combined = combined.merge(df_den_nscope, on="DEPTH_LSF", how="outer")
combined = combined.merge(df_por_nscope, on="DEPTH_LSF", how="outer")
combined = combined.merge(df_vel_nscope, on="DEPTH_LSF", how="outer")
combined = combined.merge(df_gr_gvr, on="DEPTH_LSF", how="outer")
combined = combined.merge(df_gr_scope, on="DEPTH_LSF", how="outer")
combined = combined.merge(df_res_phase_nscope, on="DEPTH_LSF", how="outer")
combined = combined.merge(df_res_atten_nscope, on="DEPTH_LSF", how="outer")

combined.head()

fig, axes = plt.subplots(nrows=1, ncols=5, figsize=(15, 8), sharey=True)

# Example plots
axes[0].plot(combined["UCAV"], combined["DEPTH_LSF"])
axes[0].set_title("UCAV")

axes[1].plot(combined["GR_RAB"], combined["DEPTH_LSF"])
axes[1].set_title("GR")

axes[2].plot(combined["RHON"], combined["DEPTH_LSF"])
axes[2].set_title("Density")

axes[3].plot(combined["BPHI"], combined["DEPTH_LSF"])
axes[3].set_title("Porosity")

axes[4].plot(combined["VSH"], combined["DEPTH_LSF"])
axes[4].set_title("Velocity")

# 🔑 VERY IMPORTANT (geology plots go downward)
for ax in axes:
    ax.invert_yaxis()
    ax.grid()

plt.tight_layout()
plt.show()