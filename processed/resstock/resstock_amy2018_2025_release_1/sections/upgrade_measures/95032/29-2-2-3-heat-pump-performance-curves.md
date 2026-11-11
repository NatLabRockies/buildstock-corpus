<!-- resstock resstock_amy2018_2025_release_1 | upgrade_measures | measure_pdfs/95032.pdf | status: osti_pdf | source_url: https://docs.nlr.gov/docs/fy26osti/95032.pdf | publication_url: https://docs.nlr.gov/docs/fy26osti/95032.pdf | corpus_version: resstock_amy2018_2025_release_1-v1-pre | corpus_path: upgrade_measures/measure_pdfs/95032.md | section: 2.2.3  Heat Pump Performance Curves | lines: 439-468 -->
## 2.2.3  Heat Pump Performance Curves

The curves previously used to represent the performance of the heat pump used when modeling GHP systems are based on a series of curves published in a master's thesis specifically for use in EnergyPlus (Tang 2005). However, these curves are based on an older product line, the ClimateMaster Genesis series (ClimateMaster 2023a). As this was an existing product when the thesis work was performed, these curves are based on technology that is now at least 20 years old, and the Genesis series is no longer available. To account for this, we regenerated curves for the GHP based on spec sheets for a newer product line available on the market today, the Tranquility TS series single-stage GHP (ClimateMaster 2023b), shown in Figure 2. These units are from the same U.S.-based manufacturer as was used for the previous curve derivation.

Figure 2. Full spec sheet used for generating performance curves

<!-- figure described by overlay: resstock_resstock_amy2018_2025_release_1/upgrade_measures/measure_pdfs/95032.yaml
     source: 95032_images/image_000003_381d498b4366598371b9b4b5db9daadf054c7171ba773c4bdc70c6cc1e079d37.png
     method: vision-description
     described: 2026-11-11 -->

![Manufacturer performance data sheet for a geothermal heat pump at 1,200 cfm nominal airflow](95032_images/image_000003_381d498b4366598371b9b4b5db9daadf054c7171ba773c4bdc70c6cc1e079d37.png)

Figure 2: scanned manufacturer performance table, headed '1,200 CFM Nominal (Rated) Airflow Cooling, 1,200 CFM Nominal (Rated) Airflow Heating'. Rows are entering water temperature from 20 to 120°F; column groups are cooling at 80/67°F entering air (capacities, kW, EER) and heating at 70°F (capacity, kW, COP). Cooling at 20°F and heating at 100°F and above are marked 'Operation not recommended'. Cell values are too small to read here.

See ClimateMaster 2017 and 2023b

The project leveraged the Auxiliary Program: HVAC Performance Curve Fit Tool for generating the curves for air-to-air heat pumps in both heating and cooling operation (U.S. DOE 2022). These tools are generically designed to fit curves of the appropriate form to two independent variables and therefore can also be applied to a GHP by using a water temperature to replace an air temperature. Appendix C shows comparisons between the output of the curves and the manufacturer's data that was used to validate this approach before simulations were performed. In the intervening years, the performance of this product has generally increased since the initial curves were generated, with higher performance at rated conditions as shown in Table 2. This indicates that some improvements have been made, which may be reflected in the performance at off-rated conditions as well.

Table 2. Rated Performance of the Products Used for Developing Performance Curves 16

EER = energy efficiency ratio

|                      |   Cooling Rated EER (Btu/Wh) |   Heating Rated COP (W/W) |
|----------------------|------------------------------|---------------------------|
| Original Genesis GS  |                         16.4 |                       3.4 |
| Newer Tranquility TS |                         19.1 |                       4.1 |

EnergyPlus requires as inputs the efficiency and capacity at a set of nominal conditions, along with performance curves that are used to modify the performance at off-rated conditions of different incoming water temperatures and air temperatures. These performance curves are biquadratic curves, and take the form of:

