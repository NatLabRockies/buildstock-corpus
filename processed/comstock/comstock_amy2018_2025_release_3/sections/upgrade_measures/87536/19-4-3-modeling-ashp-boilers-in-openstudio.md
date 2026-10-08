<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/87536.pdf | status: osti_pdf | source_url: https://www.nlr.gov/docs/fy24osti/87536.pdf | publication_url: https://www.nlr.gov/docs/fy24osti/87536.pdf | corpus_version: 0396270 | corpus_path: upgrade_measures/measure_pdfs/87536.md | section: 4.3  Modeling ASHP Boilers in OpenStudio | lines: 462-503 -->
## 4.3  Modeling ASHP Boilers in OpenStudio

A heating model with a plant loop heat pump energy efficiency ratio (EIR) is used to model the ASHP boiler. However, the current version of this model does not support flow modulation and requires the full design flow from the plant [9]. Consequently, it cannot be directly integrated into a hot water loop with a variable speed pump. To overcome this limitation and provide the necessary separation between the hot water loop and the heat pump, we added a heat pump loop to the existing building model (refer to Figure 5). The heat pump loop consists of a heat pump on the supply side and a fluid-to-fluid heat exchanger on the demand side. This heat exchanger, connected in series with the existing boiler, serves as the primary heating source, while the boiler handles the remaining load.

To deal with multiple heat pumps in the heat pump loop, we implemented a "sequentialLoad" control scheme, where the heat pumps are activated in sequence until the heating load is met. To maintain the system efficiency despite the presence of a heat exchanger, we assumed an "ideal" heat exchanger, considering its effectiveness to be 1. Additionally, we utilized an "UncontrolledOn" control scheme for the heat exchanger, which allows it to operate whenever there is nonzero flow in the main hot water loop.

Furthermore, it is worth noting that this heat pump model lacks a cutoff temperature. To address this, we incorporated an "AvailabilityManagerLowTemperatureTurnOff" to the heat pump loop. This function turns off the loop when the outdoor air temperature drops below the specified cutoff temperature.

Figure 5. Configuration of heat pump and hot water loops

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/87536.yaml
     source: 87536_images/image_000011_5a97cb86c04ea095b17450da5d62d12511a21a051016eb21561f1836a9827cf7.png
     method: vision-description
     described: 2026-08-21 -->

![Piping diagram of the heat pump loop, heat exchanger and hot water loop with backup boiler](87536_images/image_000011_5a97cb86c04ea095b17450da5d62d12511a21a051016eb21561f1836a9827cf7.png)

Figure 5: piping diagram of the configuration of heat pump and hot water loops - ASHP boilers and a circulation pump on the heat pump loop, a heat exchanger coupling it to the hot water loop, and the Backup Boiler plus hot water pump serving the building coils. Section 4.3 explains that the heat exchanger request is what triggers heat pump operation.

The plant loop heat pump EIR heating model uses three performance curves-CapFTemp, EIRFTemp, and EIRPLR-to capture the impact of operating conditions on capacity and performance.

CapFTemp modifies the capacity of the heat pump based on the outdoor air and heat pump condenser outlet temperatures:

EIRFTemp modifies the EIR, which is the inverse of the coefficient of performance (COP), of the heat pump based on outdoor and heat pump condenser outlet temperatures:

EIRPLR modifies the EIR of the heat pump based on the part load ratio (PLR) and captures efficiency loss from compressor cycling:

We used data provided by Colmac [13] to generate the CapFTemp and EIRFTemp performance curves. During the measure development, we were unable to find performance data for EIRPLR. Thus, we assumed a linear variation between EIR and PLR that resulted in a 0% reduction in EIR at 1 PLR and a 25% reduction in EIR when PLR was near zero. More details on the performance curves can be found in Appendix A.

Figure 6 and Figure 7 show how the CAPFT and EIRFT curve output values change with outdoor air temperature and hot water outlet temperature. As shown in Figure 6, the CAPFT value increases with increasing outdoor temperature and condenser outlet temperature. The EIRFT curve shown in Figure 7 shows a decrease in EIR (improvement in COP) as the outdoor temperature increases and the condenser leaving water temperature decreases.

Figure 7. EIRFT performance curve output

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/87536.yaml
     source: 87536_images/image_000012_89a15313fedebe548224baa10f969c4f0c823305366a2f0c9fe54ac9c93d459b.png
     method: vision-description
     described: 2026-08-21 -->

![Contour plots of CAPFT and EIRFT curve output over outdoor air and condenser leaving water temp](87536_images/image_000012_89a15313fedebe548224baa10f969c4f0c823305366a2f0c9fe54ac9c93d459b.png)

Figures 6 and 7: paired filled-contour plots of CAPFT (capacity) and EIRFT (energy input ratio) curve output over outdoor air temperature, -15 to 30 degrees C, and condenser leaving water temperature, 60 to 82 degrees C. CAPFT's near-vertical contours climb 0.45 to 1.50 with outdoor temperature alone; EIRFT slants from 1.80 at cold air and hot water down to 0.60. Table A-3 lists the coefficients.

