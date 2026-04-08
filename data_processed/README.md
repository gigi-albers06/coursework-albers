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