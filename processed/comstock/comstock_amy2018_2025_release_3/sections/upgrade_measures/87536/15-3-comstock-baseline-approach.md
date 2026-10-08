<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/87536.pdf | status: osti_pdf | source_url: https://www.nlr.gov/docs/fy24osti/87536.pdf | publication_url: https://www.nlr.gov/docs/fy24osti/87536.pdf | corpus_version: fadc83e | corpus_path: upgrade_measures/measure_pdfs/87536.md | section: 3  ComStock Baseline Approach | lines: 273-371 -->
## 3  ComStock Baseline Approach

The current version of the boilers in ComStock are gas-fired, noncondensing boilers. Their efficiencies were determined using the U.S. Department of Energy's reference building templates and capacities. The values are summarized in Table 1 [3]. Three different cubic performance curves based on the part load ratio (PLR) are used to adjust the boiler efficiency, as shown in Table 2. Figure 2 shows the variations of boiler efficiency multipliers with PLR based on the three performance curves, a graphical representation of the curves' output. All ComStock boilers have a heating set point of 180°F and can modulate flow based on heating load.

Table 1. Boiler Efficiency and Performance Curve Assignment

<!-- table recovered from measure_pdfs/87536.pdf p.11
     overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/87536.yaml
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

Table 2. Boiler Performance Curves

<!-- table recovered from measure_pdfs/87536.pdf p.11
     overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/87536.yaml
     method: vision-transcription -->

| Name | Form | Dependent Variable | Independent Variable 1 | coeff_1 | coeff_2 | coeff_3 | coeff_4 | Notes |
|---|---|---|---|---|---|---|---|---|
| Boiler Constant Efficiency Curve | Cubic | Efficiency Multiplier | Part Load Ratio | 1 | 0 | 0 | 0 | From DOE Reference Building |
| Boiler with Minimum Turndown | Cubic | Efficiency Multiplier | Part Load Ratio | 0.7791 | 1.4745 | -2.5795 | 1.3467 | From Regression of Prototype Building EMS |
| Boiler with No Minimum Turndown | Cubic | Efficiency Multiplier | Part Load Ratio | 0.7463 | 1.3196 | -2.2154 | 1.1674 | From Regression of Prototype Building EMS |

Figure 2. Boiler performance curves

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/87536.yaml
     source: 87536_images/image_000008_761fa8382000bfe82d38d118ecb461549bc748c6a5bdb4ad42ff0f41ec7a796a.png
     method: vision-description
     described: 2026-08-21 -->

![Scatter plot of boiler efficiency multiplier against boiler part load ratio for three curves](87536_images/image_000008_761fa8382000bfe82d38d118ecb461549bc748c6a5bdb4ad42ff0f41ec7a796a.png)

Figure 2: scatter plot of boiler performance curves, with boiler part load ratio from 0 to 1.4 on the x-axis and boiler efficiency multiplier from 0 to 1.4 on the y-axis. One series is flat at 1.0 across the range while the other two dip to roughly 0.75-0.85 at low part load and rise above 1.2 near a ratio of 1.3. The tables above give the curve assignments and coefficients.

