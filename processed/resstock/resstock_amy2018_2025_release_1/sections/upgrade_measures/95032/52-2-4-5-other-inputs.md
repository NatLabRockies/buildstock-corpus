<!-- resstock resstock_amy2018_2025_release_1 | upgrade_measures | measure_pdfs/95032.pdf | status: osti_pdf | source_url: https://docs.nlr.gov/docs/fy26osti/95032.pdf | publication_url: https://docs.nlr.gov/docs/fy26osti/95032.pdf | corpus_version: resstock_amy2018_2025_release_1-v1-pre | corpus_path: upgrade_measures/measure_pdfs/95032.md | section: 2.4.5 Other Inputs | lines: 1085-1157 -->
## 2.4.5 Other Inputs

While some of the key inputs and their values are discussed above, Table 11 summarizes inputs for the GHP measure in ResStock and OpenStudio-HPXML.

[27 https://www.energystar.gov/most-efficient/me-certified-geothermal-heat-pumps/results?is\_most\_efficient\_filter=Most%20Efficient](https://www.energystar.gov/most-efficient/me-certified-geothermal-heat-pumps/results?is_most_efficient_filter=Most%20Efficient)

Table 11. Summary of the GHP, Geothermal Loop, and Soil Inputs

| Input                                             | Value                                                                                      | Source                                                                 |
|---------------------------------------------------|--------------------------------------------------------------------------------------------|------------------------------------------------------------------------|
| Geothermal loop borefield configuration           | Rectangle                                                                                  | OpenStudio-HPXML Geothermal Loops default 28                           |
| Geothermal loop boreholes diameter                | 5 in                                                                                       | G-Function Library for Modeling Vertical Bore Ground Heat Exchanger 29 |
| Geothermal loop boreholes spacing                 | 16.4 ft                                                                                    | G-Function Library for Modeling Vertical Bore Ground Heat Exchanger    |
| Geothermal loop boreholes count                   | Autosized (in ft)                                                                          | Based on ACCA manual J and S load calculations 30                      |
| Geothermal loop boreholes length                  | Autosized (in ft)                                                                          | Based on ACCA manual J and S load calculations                         |
| Geothermal loop boreholes length min/max          | Min=78.74 ft, max=498 ft                                                                   | OpenStudio-HPXML Geothermal Loops default                              |
| Geothermal loop configuration                     | Vertical                                                                                   | The measure definition                                                 |
| Geothermal loop flow rate                         | 3 times heating/cooling capacity in tons, minimum of 3 gal/min (Meline and Kavanaugh 2019) | OpenStudio-HPXML Geothermal Loops default                              |
| Geothermal loop fluid                             | 80% water, 20% propylene glycol 31                                                         | OpenStudio-HPXML Geothermal Loops default                              |
| Geothermal loop grout type                        | Thermally enhanced 1.2 Btu/hr-ft-°F                                                        | OpenStudio-HPXML Geothermal Loops default                              |
| Geothermal loop min/max exiting fluid temperature | min=32°F, max=95°F 32                                                                      | OpenStudio-HPXML Geothermal Loops default                              |
| Geothermal loop pipe borehole burial depth        | 6.74 ft                                                                                    | G-Function Library for Modeling Vertical Bore Ground Heat Exchanger    |
| Geothermal loop pipe diameter                     | 1.25 in                                                                                    | OpenStudio-HPXML Geothermal Loops default                              |
| Geothermal loop pipe roughness                    | 0.000001                                                                                   | High density polyethylene roughness                                    |
| Geothermal loop pipe type                         | Thermally enhanced 0.4 Btu/hr-ft-°F                                                        | OpenStudio-HPXML Geothermal Loops default                              |
| Geothermal loop shank spacing                     | U-tube spacing + pipe outer diameter                                                       | OpenStudio-HPXML Geothermal Loops default                              |
| Ground heat exchanger g-functions                 | Auto-calculated                                                                            | G-Function Library for Modeling Vertical Bore Ground Heat Exchanger    |
| Heat pump airflow defect ratio                    | 0                                                                                          | OpenStudio-HPXML Ground-to-Air Heat Pump default 33                    |

[28  https://openstudio-hpxml.readthedocs.io/en/v1.9.1/workflow\_inputs.html#hpxml-geothermal-loops](https://openstudio-hpxml.readthedocs.io/en/v1.9.1/workflow_inputs.html#hpxml-geothermal-loops)

[29 https://gdr.openei.org/submissions/1325](https://gdr.openei.org/submissions/1325)

[30  https://www.acca.org/home](https://www.acca.org/home)

[31  Based on a common heat transfer fluid for GHPs: https://www.chempoint.com/products/dow/dowfrost-glycol-thermal-fluids/dowfrost-propylene-glycol-thermal-fluids/dowfrost-geo-20](https://www.chempoint.com/products/dow/dowfrost-glycol-thermal-fluids/dowfrost-propylene-glycol-thermal-fluids/dowfrost-geo-20)

32  Recommended from Technical Advisory Group in the Acknowledgements

[33  https://openstudio-hpxml.readthedocs.io/en/v1.9.1/workflow\_inputs.html#ground-to-air-heat-pump](https://openstudio-hpxml.readthedocs.io/en/v1.9.1/workflow_inputs.html#ground-to-air-heat-pump)

| Input                                    | Value                                                              | Source                                             |
|------------------------------------------|--------------------------------------------------------------------|----------------------------------------------------|
| Heat pump backup type                    | None                                                               | The measure definition                             |
| Heat pump charge defect ratio            | 0                                                                  | OpenStudio-HPXML Ground-to-Air Heat Pump default   |
| Heat pump cooling capacity               | Autosized                                                          | Based on ACCA manual J and S load calculations     |
| Heat pump cooling compressor type        | Single-stage                                                       | The measure definition                             |
| Heat pump cooling efficiency type        | EER                                                                | N/A                                                |
| Heat pump cooling efficiency             | 18.6                                                               | ENERGY STAR 2025 Most Efficient List               |
| Heat pump cooling sensible heat fraction | 0.73 34                                                            | OpenStudio-HPXML Ground-to-Air Heat Pump default   |
| Heat pump fan power                      | 0.5 W/cfm if COP ≤ 8.75/3.2, else 0.375 W/cfm 35                   | OpenStudio-HPXML Ground-to-Air Heat Pump default   |
| Heat pump fraction cooling load served   | 1                                                                  | Serves the entire cooling load                     |
| Heat pump fraction heat load served      | 1                                                                  | Serves the entire heating load                     |
| Heat pump heating capacity               | Autosized                                                          | Based on ACCA manual J and S load calculations     |
| Heat pump heating efficiency             | 3.8                                                                | ENERGY STAR 2025 Most Efficient List               |
| Heat pump heating efficiency type        | COP                                                                | N/A                                                |
| Heat pump is shared system               | FALSE                                                              | OpenStudio-HPXML Ground-to-Air Heat Pump default   |
| Heat pump power                          | 80 W/ton 36                                                        | OpenStudio-HPXML Ground-to-Air Heat Pump default   |
| Heat pump sizing methodology             | MaxLoad                                                            | OpenStudio-HPXML Ground-to-Air Heat Pump default   |
| Heat pump type                           | Water-to-air                                                       | The measure definition                             |
| Heat pump unit location                  | Conditioned space                                                  | OpenStudio-HPXML Ground-to-Air Heat Pump default   |
| Soil conductivity                        | Distribution that varies by ASHRAE climate and moisture zone       | Southern Methodist University Geothermal Lab, USDA |
| Soil undisturbed temperature             | Varies by location. Uses a lookup table based on the L. Xing model | L. Xing appendix A-3 (Xing 2014)                   |
| Soil volumetric heat capacity            | 771,245 (J/K-m 3 )                                                 | OpenStudio-HPXML Site default 37                   |

[34 https://openstudio-hpxml.readthedocs.io/en/v1.9.1/workflow\_inputs.html#id718](https://openstudio-hpxml.readthedocs.io/en/v1.9.1/workflow_inputs.html#id718)

[35 https://openstudio-hpxml.readthedocs.io/en/v1.9.1/workflow\_inputs.html#id720](https://openstudio-hpxml.readthedocs.io/en/v1.9.1/workflow_inputs.html#id720)

[36 https://openstudio-hpxml.readthedocs.io/en/v1.9.1/workflow\_inputs.html#id978](https://openstudio-hpxml.readthedocs.io/en/v1.9.1/workflow_inputs.html#id978)

37 https://openstudio-hpxml.readthedocs.io/en/v1.9.1/workflow\_inputs.html#hpxml-site. Calculated from other values.

