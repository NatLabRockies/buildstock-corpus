<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/86199.pdf | status: osti_pdf | source_url: https://www.nlr.gov/docs/fy24osti/86199.pdf | publication_url: https://www.nlr.gov/docs/fy24osti/86199.pdf | corpus_version: fadc83e | corpus_path: upgrade_measures/measure_pdfs/86199.md | section: A.1 Appendix ASHP Boiler Performance Curve Generation | lines: 900-963 -->
## A.1 Appendix ASHP Boiler Performance Curve Generation

As discussed in Section 4.3, the heat pump model used in this measure has three performance curves for capturing the dependency of the heat pump performance on the operating conditions. Two of the curves, capacity as a function of temperature (CapFTemp) and energy input ratio (EIR) as a function of temperature (EIRFTemp) capture the dependency of heat pump capacity and efficiency on outdoor air temperature and hot water supply temperature. EIR as a function of part load ratio (EIRPLR) captures the dependency of the heat pump efficiency on heat pump loading and cycling.

Where QReference is the design heating capacity of the heat pump, PReference is the design power demand of the heat pump, QAvailable is the adjusted heating capacity, P is the adjusted power demand, Tcond,out   is the condenser outlet water temperature, Tair,in is the ambient air temperature, PLR is heat pump part load ratio,     a1, b1, c1, d1, e1 … c3 are performance curve coefficients that need to be extracted from operational data.

The two temperature-dependent performance curves, CapFTemp and EIRFTemp, were generated using performance data provided by Colmac. It is important to note that the efficiency of the heat pump is influenced not only by the operating temperature conditions but also by factors such as the load on the heat pump and its cycling frequency. During the development of the measurement, we encountered a challenge in obtaining manufacturer data to account for this dependency. As a result, we assumed a linear variation between EIR and PLR. According to this assumption, there is no reduction in efficiency when the PLR is one (indicating full load), and a 25% reduction in efficiency when the PLR is close to zero (indicating low load).

In order to evaluate the accuracy of the Colmac performance data, a comparison was made with data from Trane and Mitsubishi. Unfortunately, detailed data for the two units from Trane and Mitsubishi was not available. However, the capacity drop with outdoor air temperature observed in the Colmac unit appeared to be consistent with the data from Trane and Mitsubishi.

The results of the comparison are summarized in Table A-1 and Table A-2. According to the data, the capacity reductions for the Trane and Colmac units were found to be 44% and 50%, respectively, as the temperature decreased from 47°F to 0°F.on the other hand, the Mitsubishi data indicates a 31% capacity reduction as the outdoor air temperature decreases from 45°F to

20°F, while the Colmac unit shows a slightly lower reduction of 25% within the same temperature range.

Table A-1. Capacity Reduction With OAT for Trane and Colmac Units

|            |   Capacity at 50°F (Btu/hr) |   Capacity at 0°F (Btu/hr) | % Capacity Reduction From 50°F to 0°F   | COP         |
|------------|-----------------------------|----------------------------|-----------------------------------------|-------------|
| Colmac[14] |                      57,600 |                      31500 | 45%                                     | 2.70 @ 50°F |
| Trane [2]  |                             |                            | 50%                                     | 2.70 @ 47°F |

Table A-2. Capacity Reduction Comparison Between Mitsubishi and Colmac Units

|                 |   Capacity at 45°F (Btu/hr) |   Capacity at 20°F (Btu/hr) | % Capacity Reduction From 50°F to 20°F   | COP         |
|-----------------|-----------------------------|-----------------------------|------------------------------------------|-------------|
| Colmac[14]      |                      54,750 |                      42,200 | 23%                                      | 2.70 @ 50°F |
| Mitsubishi [10] |                     140,400 |                     117,234 | 25%                                      | 2.85 @ 45°F |

Table A-3 summarizes the performance curve coefficients that are estimated using the Colmac data. The curve outputs for different combination of condenser water leaving temperature and outdoor air temperature are indicated in Figure A- 1 and Figure A-2.

Table A-3. Performance Curve Coefficients

|    | CAPFT        | EIRFT        | EIRPLR   |
|----|--------------|--------------|----------|
| a  | 0.88302749   | 0.84177647   | 1.25     |
| b  | - 0.0016513  | 0.00648504   | - 0.25   |
| c  | 1.44E - 05   | - 8.68E - 06 | 0        |
| d  | 0.01833385   | - 0.0273677  |          |
| e  | 3.6396E - 05 | 0.00018754   |          |
| f  | - 2.04E - 05 | 0.0001082    |          |

Figure A-2. EIRFT performance curve output

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/86199.yaml
     source: 86199_images/image_000023_4ad212fd0237336c41b1be834c003d3aac4d7f989d6c462216bda5fea793110e.png
     method: vision-description
     described: 2026-08-21 -->

![Two contour plots reprinting the CAPFT and EIRFT performance curve output in Appendix A](86199_images/image_000023_4ad212fd0237336c41b1be834c003d3aac4d7f989d6c462216bda5fea793110e.png)

Figures A-1 and A-2 in a single bitmap: the same pair of filled contour plots printed earlier as Figures 10 and 11, with CAPFT rising from 0.45 to 1.50 and EIRFT falling from 1.80 to 0.60 across outdoor temperature -15 to 30C and condenser leaving water temperature 60 to 82C. Figure A-1's caption is printed inside the bitmap. Table A-3 lists the curve coefficients.

Figure A-3 illustrates the comparison between the actual heating capacity and EIR with the estimated values obtained using the performance curves for various combinations of outdoor air temperature and condenser water leaving temperature (CWLT). The figure demonstrates a satisfactory agreement between the two, providing assurance that we can confidently utilize the performance curves for modeling ASHP boilers.

Figure A-3. Comparisons of predicted and actual capacity and EIR

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/86199.yaml
     source: 86199_images/image_000024_c3ee03e60a2f20a02a8eded9fe3f57553454c75eef31aad4c830c65c2a32433d.png
     method: vision-description
     described: 2026-08-21 -->

![Two 3-D scatter plots comparing actual and predicted heating capacity and EIR](86199_images/image_000024_c3ee03e60a2f20a02a8eded9fe3f57553454c75eef31aad4c830c65c2a32433d.png)

Figure A-3: two three-dimensional scatter panels comparing actual against predicted values over outdoor air temperature (-20 to 30C) and condenser water leaving temperature (60 to 80C) - heating capacity in kW with RMSE 0.026, and EIR with RMSE 0.006. Predicted points track the actuals closely across the grid, which Section A.1 cites as validation of the curves.
