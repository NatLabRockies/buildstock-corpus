<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/86602.pdf | status: osti_pdf | source_url: https://www.nlr.gov/docs/fy24osti/86602.pdf | publication_url: https://www.nlr.gov/docs/fy24osti/86602.pdf | corpus_version: b5faf42 | corpus_path: upgrade_measures/measure_pdfs/86602.md | section: 2.6 Boilers | lines: 487-562 -->
## 2.6 Boilers

The current version of boilers in ComStock are gas-fired, noncondensing boilers. The efficiencies of the boilers are assigned based on the U.S. Department of Energy's reference buildings templates and capacities; Table 6 summarizes the values [3]. As indicated in Table 6, three different performance curves were used to adjust the efficiency of the boiler based on part load ratio. All ComStock boilers have a heating set point of 180°F with a capacity to modulate flow.

Table 6. Boiler Efficiency and Performance Curve Assignment

<!-- table recovered from measure_pdfs/86602.pdf p.17
     overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/86602.yaml
     method: vision-transcription -->

**Pre-1980**

| Template | Minimum Capacity (Btu/hr) | Maximum Capacity (Btu/hr) | Minimum Annual Fuel Utilization Efficiency (AFUE) | Minimum Thermal Efficiency (%) | Minimum Combustion Efficiency (%) | Efficiency Function of Part Load Ratio (EFFFPLR) | Notes |
|---|---|---|---|---|---|---|---|
| Pre-1980 | - | 299,999 |  | 0.73 |  | Boiler Constant Efficiency Curve | From DOE Reference Buildings |
| Pre-1980 | 300,000 | no max |  | 0.74 |  | Boiler Constant Efficiency Curve | From DOE Reference Buildings |
| Pre-1980 | 250,000,000 | 249,999,999 |  | 0.76 |  | Boiler Constant Efficiency Curve | From DOE Reference Buildings |

**1980-2004**

| Template | Minimum Capacity (Btu/hr) | Maximum Capacity (Btu/hr) | Minimum Annual Fuel Utilization Efficiency (AFUE) | Minimum Thermal Efficiency (%) | Minimum Combustion Efficiency (%) | Efficiency Function of Part Load Ratio (EFFFPLR) | Notes |
|---|---|---|---|---|---|---|---|
| 1980-2004 | - | 299,999 | 0.8 |  |  | Boiler Constant Efficiency Curve | From 90.1-1989 |
| 1980-2004 | 300,000 | 249,999,999 |  |  | 0.8 | Boiler Constant Efficiency Curve | From 90.1-1989 |

**90.1-2004**

| Template | Minimum Capacity (Btu/hr) | Maximum Capacity (Btu/hr) | Minimum Annual Fuel Utilization Efficiency (AFUE) | Minimum Thermal Efficiency (%) | Minimum Combustion Efficiency (%) | Efficiency Function of Part Load Ratio (EFFFPLR) | Notes |
|---|---|---|---|---|---|---|---|
| 90.1-2004 | - | 299,999 | 0.8 |  |  | Boiler with No Minimum Turndown | From 90.1-2004 |
| 90.1-2004 | 300,000 | 249,999,999 |  | 0.75 |  | Boiler with No Minimum Turndown | From 90.1-2004 |
| 90.1-2004 | 250,000,000 | no max |  |  | 0.8 | Boiler with No Minimum Turndown | From 90.1-2004 |

**90.1-2007**

| Template | Minimum Capacity (Btu/hr) | Maximum Capacity (Btu/hr) | Minimum Annual Fuel Utilization Efficiency (AFUE) | Minimum Thermal Efficiency (%) | Minimum Combustion Efficiency (%) | Efficiency Function of Part Load Ratio (EFFFPLR) | Notes |
|---|---|---|---|---|---|---|---|
| 90.1-2007 | - | 299,999 | 0.8 |  |  | Boiler with No Minimum Turndown | From 90.1-2007 |
| 90.1-2007 | 300,000 | 249,999,999 |  | 0.8 |  | Boiler with No Minimum Turndown | From 90.1-2007 |
| 90.1-2007 | 250,000,000 | no max |  |  | 0.82 | Boiler with No Minimum Turndown | From 90.1-2007 |

**90.1-2010**

| Template | Minimum Capacity (Btu/hr) | Maximum Capacity (Btu/hr) | Minimum Annual Fuel Utilization Efficiency (AFUE) | Minimum Thermal Efficiency (%) | Minimum Combustion Efficiency (%) | Efficiency Function of Part Load Ratio (EFFFPLR) | Notes |
|---|---|---|---|---|---|---|---|
| 90.1-2010 | - | 299,999 | 0.8 |  |  | Boiler with No Minimum Turndown | From 90.1-2010 |
| 90.1-2010 | 300,000 | 249,999,999 |  | 0.8 |  | Boiler with No Minimum Turndown | From 90.1-2010 |
| 90.1-2010 | 250,000,000 | no max |  |  | 0.82 | Boiler with No Minimum Turndown | From 90.1-2010 |

**90.1-2013**

| Template | Minimum Capacity (Btu/hr) | Maximum Capacity (Btu/hr) | Minimum Annual Fuel Utilization Efficiency (AFUE) | Minimum Thermal Efficiency (%) | Minimum Combustion Efficiency (%) | Efficiency Function of Part Load Ratio (EFFFPLR) | Notes |
|---|---|---|---|---|---|---|---|
| 90.1-2013 | - | 299,999 | 0.82 |  |  | Boiler with No Minimum Turndown | From 90.1-2013; From 90.1-2016 |
| 90.1-2013 | 300,000 | 999,999 |  | 0.8 |  | Boiler with No Minimum Turndown | From 90.1-2013; From 90.1-2016 |
| 90.1-2013 | 1,000,000 | 249,999,999 |  | 0.8 |  | Boiler with Minimum Turndown | From 90.1-2013; From 90.1-2016 |
| 90.1-2013 | 250,000,000 | no max |  |  | 0.82 | Boiler with Minimum Turndown | From 90.1-2013; From 90.1-2016 |

**90.1-2016**

| Template | Minimum Capacity (Btu/hr) | Maximum Capacity (Btu/hr) | Minimum Annual Fuel Utilization Efficiency (AFUE) | Minimum Thermal Efficiency (%) | Minimum Combustion Efficiency (%) | Efficiency Function of Part Load Ratio (EFFFPLR) | Notes |
|---|---|---|---|---|---|---|---|
| 90.1-2016 | - | 299,999 | 0.82 |  |  | Boiler with No Minimum Turndown | From 90.1-2013; From 90.1-2016 |
| 90.1-2016 | 300,000 | 999,999 |  | 0.8 |  | Boiler with No Minimum Turndown | From 90.1-2013; From 90.1-2016 |
| 90.1-2016 | 1,000,000 | 249,999,999 |  | 0.8 |  | Boiler with Minimum Turndown | From 90.1-2013; From 90.1-2016 |
| 90.1-2016 | 250,000,000 | no max |  |  | 0.82 | Boiler with Minimum Turndown | From 90.1-2013; From 90.1-2016 |

**90.1-2019**

| Template | Minimum Capacity (Btu/hr) | Maximum Capacity (Btu/hr) | Minimum Annual Fuel Utilization Efficiency (AFUE) | Minimum Thermal Efficiency (%) | Minimum Combustion Efficiency (%) | Efficiency Function of Part Load Ratio (EFFFPLR) | Notes |
|---|---|---|---|---|---|---|---|
| 90.1-2019 | - | 299,999 | 0.84 |  |  | Boiler with No Minimum Turndown | From 90.1-2019 |
| 90.1-2019 | 300,000 | 999,999 |  | 0.8 |  | Boiler with No Minimum Turndown | From 90.1-2019 |
| 90.1-2019 | 1,000,000 | 249,999,999 |  | 0.8 |  | Boiler with Minimum Turndown | From 90.1-2019 |
| 90.1-2019 | 250,000,000 | no max |  |  | 0.82 | Boiler with Minimum Turndown | From 90.1-2019 |

