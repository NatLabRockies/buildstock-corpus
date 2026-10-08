<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/95119.pdf | status: osti_pdf | source_url: https://docs.nlr.gov/docs/fy25osti/95119.pdf | publication_url: https://docs.nlr.gov/docs/fy25osti/95119.pdf | corpus_version: 267e3ea | corpus_path: upgrade_measures/measure_pdfs/95119.md | section: 3.2.7  Fan Power and Operation | lines: 418-445 -->
## 3.2.7  Fan Power and Operation

Here, the modeled HP-RTUs utilize a multispeed fan system. During ventilation-only mode, when no heating or cooling is required but the building still requires outdoor ventilation air, the fan defaults to a speed that is either the higher of (1) the design outdoor air flow rate or (2) 59%

of the maximum. The design outdoor air flow rate is prescribed by ANSI/ASHRAE Standard 62.1 in ComStock and therefore varies substantially across the stock. This can result in a fan speed greater than 59% for systems with especially high outdoor air requirements.

Fan power varies as a function of fan speed and is modeled using a fan power as a function of flow fraction curve in EnergyPlus. The output of this curve is multiplied by the design fan power, lowering fan power with flow rate. The fan power curve modeled in this work is illustrated in Figure 6.

Table 3. Fan Flow Fractions for Various Heat Pump Operation Stages

| Stage   | Stage Mode       | Stage Name   | Fan Flow Fraction                 |
|---------|------------------|--------------|-----------------------------------|
| 1H      | Heating          | High         | 1                                 |
| 2C      | Cooling          | High         | 1                                 |
| 1C      | Cooling          | Low          | 0.59                              |
| 1V      | Ventilation-only | Vent         | 𝑀𝑀𝑀𝑀𝑀𝑀 (design OA fraction, 0.40) |

Figure 6. Fan power curve as a function of flow fraction. The output of this curve is multiplied by the design fan power to determine the realized fan power for each time step.

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/95119.yaml
     source: 95119_images/image_000007_99f3650c5a66eb564fe2f538c62d208871e1db7f943021774de44d1863b7ea23.png
     method: vision-description
     described: 2026-08-20 -->

![Figure 6. Scatter plot of fan power multiplier as a function of flow fraction with a quadratic curve fit and a minimum flow reference line](95119_images/image_000007_99f3650c5a66eb564fe2f538c62d208871e1db7f943021774de44d1863b7ea23.png)

Figure 6 plots Power Multiplier (dimensionless) on the y-axis from 0 to about 1.2 against Flow Fraction (dimensionless) on the x-axis from 0 to 1. A legend gives two series: Measured Data (blue circles, spelled "Meaured Data" in the source) and Curve Fit (Poly) as a red line. The printed quadratic fit is y = 1.6238x^2 - 0.8782x + 0.2479. Measured points run from roughly (0.40, 0.15) and (0.44, 0.18) through (0.55, 0.27), (0.67, 0.40), (0.78, 0.55), and (0.89, 0.75) up to (1.00, 1.00), and the red curve passes through them closely. A horizontal dashed line labeled "Minimum Flow" sits at a power multiplier of about 0.40. Per the caption, the output of this curve is multiplied by the design fan power to determine realized fan power at each time step. The strongly convex shape is the practical point: dropping flow to 55% of design cuts fan power to about 27% of design, so part-load fan operation is where much of the measure's fan energy savings comes from.

