<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/87536.pdf | status: osti_pdf | source_url: https://www.nlr.gov/docs/fy24osti/87536.pdf | publication_url: https://www.nlr.gov/docs/fy24osti/87536.pdf | corpus_version: b5faf42 | corpus_path: upgrade_measures/measure_pdfs/87536.md | section: 4.2  ASHP Sizing | lines: 427-461 -->
## 4.2  ASHP Sizing

Heat pump sizing is a critical step to consider when retrofitting a boiler with an ASHP boiler. The sizing process requires consideration of several factors, such as: [2]

- Design heating water supply temperature
- Design heating outdoor temperature
- Equipment costs
- Operating costs

- Electrical infrastructure cost to support the higher peak demand from switching to an electric heating source from a gas-fired heating source
- Carbon emission reduction.

Optimal sizing is a balance of the above factors and should be based on the priorities of the building owner. Most commercially available ASHP boilers are relatively small and require cascading for higher capacities. Aside from requiring more space for installation, cascading provides flexibility, improves efficiency at part load operation, and increases system redundancy and resiliency.

Two ASHP sizing methods are offered for this measure. In the first method the ASHP is sized based on the percentage of the peak load, with the ASHP target capacity determined as a percentage of the design heating load (DHL) on the heating load line as shown in Figure 4. The heat load line is defined as the line connecting the zero-heating load at the heat enabling outdoor temperature, assumed to be 60°F, and the DHL at the winter heating design day outdoor temperature, while the DHL is assumed to be the same as the heating capacity of the existing boiler.

In the second method, sizing is based on a specified outdoor temperature. In this method, the target ASHP capacity is determined by selecting a point on a heating load line that corresponds to the outdoor air temperature.

Figure 4. Heat pump sizing approach

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/87536.yaml
     source: 87536_images/image_000010_c9a84f78d017a8ec87fc72178afd0162a1fceb01e58f913ffc30f00fc11c451e.png
     method: vision-description
     described: 2026-08-21 -->

![Schematic of the heat pump sizing approach relating design heating load to design outdoor air](87536_images/image_000010_c9a84f78d017a8ec87fc72178afd0162a1fceb01e58f913ffc30f00fc11c451e.png)

Figure 4: schematic of the heat pump sizing approach, plotting heating load against outdoor air temperature and marking the design heating load (DHL), the sizing fraction (%DHL), the heat pump design temperature (HDT), the target capacity and the design outdoor air temperature, with the curve pinned at 60 degrees F. Section 4.2 gives the sizing rules and the backup boiler cutoff.

Note that with current technology, heat pump capacity changes with outdoor temperature. Most heat pump manufacturers specify the heat pump rated capacity at a certain condition, usually at an outdoor temperature of 47 o F. Thus, the target capacity estimated by either method must be converted to the required capacity at the design conditions. To estimate the required rated capacity of the heat pump at the design outdoor temperature, we used a performance curve called 𝐶𝐶𝐶𝐶𝐶𝐶𝐶𝐶𝐶𝐶 [9] that captures the variation of a heat pump's capacity with outdoor air temperature and hot water set point. The target capacity at the design outdoor air temperature (Target Capacity @ Design OAT) is estimated as:

where a, b, c, d, e, and f are CapFT performance curve coefficients, and Tcondout is the hot water temperature at the condenser outlet of the heat pump (which is equivalent to the hot water heating set point).

For more detail information on sizing, readers are encouraged to refer the measure documentation for boiler replacement with air source heat pump boiler and electric boiler backup from Commercial EUSS 2023 Release 1.

