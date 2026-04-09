# Processed Well Log Data

## Overview
This dataset contains processed well log data from IODP Expedition 372 (Hole U1517A). Raw data from multiple logging tools were combined, cleaned, and interpolated to create a unified dataset for analysis and visualization.

---

## Processing Steps
I applied steps were applied to the raw data:

- Combined multiple datasets using DEPTH_LSF as the common reference
- Set DEPTH_LSF as the index to align logs
- Converted all columns to numeric values
- Replaced invalid placeholder values (like -999.25) with NaN
- Converted velocity units:
  - VCO (P-wave velocity) from km/s → m/s
  - VSH (S-wave velocity) from km/s → m/s
- Interpolated missing values to create continuous logs
- Sorted data by depth

---

## Variables

| Variable | Description | Units | (in this order)
-----------------------------------
| DEPTH_LSF | Depth below seafloor | m |
| UCAV | Caliper (borehole diameter) | inches |
| GR_RAB | Gamma Ray (GeoVision tool) | gAPI |
| GRMA | Gamma Ray (Neoscope tool) | gAPI |
| RHON | Bulk density | g/cm³ |
| BPHI | Bulk porosity | % |
| TNPH | Neutron porosity | % |
| RES_BD | Deep resistivity | ohm·m |
| P16B | Medium resistivity | ohm·m |
| A40B | Shallow resistivity | ohm·m |
| VCO | P-wave velocity | m/s |
| VSH | S-wave velocity | m/s |

---

## Notes
- Missing values are represented as NaN
- Some logs were originally sampled at different depth intervals and were interpolated
- Velocity data originally contained placeholder values (-999.25), which were removed

---

## Author
Gigi Albers | April 2026

---

## Question answered
# What is well-logging?
Well-logging is when you measure physical, chemical, and structural properties of subsurface materials within a borehole. In this particular study, logging was conducted using logging-while-drilling (LWD), which collects data in real time as the drill moves through the seabed/seafloor. These measurements provide continuous records of properties such as resistivity, porosity, density, and velocity, helping geophysists and scientists alike understand subsurface conditions.
# What data are you going to be looking at, and where did it come from?
 All of this data comes from IODP Expedition 372A at Site U1517 along the Hikurangi margin offshore New Zealand. The dataset includes LWD measurements (such as resistivity, gamma ray, porosity, and velocity as shown in the plots), physical core samples and downhole temperature and pressure measurements. This data was collected through many drilling operations, with onboard laboratory analysis, and prior geophysical surveys.
# What are these data used for? What are some scientific/societal applications?
 This data is used to study subsurface processes such as gas hydrate behavior, sediment stability, and fluid flow. Scientifically, this helps researchers understand submarine landslides and deformation processes in subduction zones (super cool!). Societally, this information is important for assessing geohazards like underwater landslides also and potential tsunamis, and understanding methane storage in gas hydrates and its role in climate systems.
# What is usually the format of this data?
It's primarily in the form of 1D depth profiles, where measurements are recorded with depth. Core samples provide discrete measurements tied to specific depths, creating a combination of 1D, 2D, 3D, and point-based datasets.
# What are some common tools used for analyzing and interpreting these data?
Logging-while-drilling instruments for data collection and laboratory techniques for analyzing core samples. Seismic interpretation software is used to analyze subsurface structures, for example. Researchers also use computational tools such as Python, MATLAB, and GIS software to visualize, process, and integrate different datasets.

---

## More Questions (about the dataset)
# Write a couple of paragraphs discussing what you see in the data, how the variable are related, and justifying your observations and conclusions.
The link between lithology and physical characteristics with depth is pretty stable, from looking at the log suite. Gamma ray levels are comparatively higher and more varied at the surface (0– roughly 50 mbsf), which indicates the presence of more clay-rich or fine-grained sediments. Higher porosity and lower density are associated with unconsolidated, clay-rich materials because they tend to retain more pore spaceand have lower bulk densities. Both P-wave (Vp) and S-wave (Vs) velocities are lower throughout this same interval, indicating weaker, less consolidated material. While density rises and porosity falls with increasing depth (inverse relationship), gamma ray readings progressively decline and stabilize, suggesting growing compaction and a move toward more consolidated sediments.
Resistivity slightly rises and becomes less variable further in the section (roughly 100–200 mbsf), which is consistent with lower porosity and less conductive pore fluids. There is an obvious inverse link between porosity and both density and velocity: intervals of lower porosity relate to higher density and higher seismic velocities, indicating reduced fluid content and tighter grain packing. Adding on to that, the idea of rising lithification and mechanical stiffness is supported by the fact that Vp and Vs often rise with depth. The logs show a change from softer, more porous near-surface sediments to more compacted and mechanically stronger materials at depth.

