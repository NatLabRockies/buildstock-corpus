<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/86199.pdf | status: osti_pdf | source_url: https://www.nlr.gov/docs/fy24osti/86199.pdf | publication_url: https://www.nlr.gov/docs/fy24osti/86199.pdf | corpus_version: 43ae2d4 | corpus_path: upgrade_measures/measure_pdfs/86199.md | section: 4.3  Modeling ASHP Boilers in OpenStudio | lines: 616-659 -->
## 4.3  Modeling ASHP Boilers in OpenStudio

During the measure development, we considered two heat pump models in OpenStudio; pumped condenser and plant loop EIR heat pump. The pumped condenser heat pump model is a combination of multiple objects, including a fan, a water tank, and an air-to-water heat pump coil object that is composed of a heat pump and a water circulation pump between the heat pump and the water tank [9]. This model doesn't allow a cutoff temperature below 23°F and this is way higher than the practical cutoff temperature by commercial heat pump boilers which could go as low as -25oF, especially the CO2-based heat pumps [1]. Because of this limitation, this model is not used in this version of the measure but could be considered in the future once the cutoff temperature limit is relaxed to a lower value.

The second option considered-and the model selected for this measure-is a plant loop heat pump energy efficiency ratio (EIR) heating model. The plant loop EIR heating heat pump object is a recently added object for modeling a heat pump. Unlike the pumped condenser heat pump, this object doesn't have a water tank that helps differentiate the heat pump from the main hot water loop. In addition, the current version is a constant flow model that requests full design flow from the plant [9]. Because of this limitation, this object could not be directly added to a hot water loop with a variable speed pump. To circumvent this, and to provide the necessary separation between the hot water loop and the heat pump, we added a heat pump loop (as shown in Figure 9) to the existing building model. The heat pump loop has a heat pump on the supply side and a fluid-to-fluid heat exchanger on the demand side. The same heat exchanger is connected in series to the existing boiler. As indicated in Figure 9, the heat exchanger is added before the boiler so that it will be the primary heating source while the boiler handles the rest. For multiple heat pumps in the heat pump loop, we used a 'sequentialLoad' control scheme, in which heat pumps are fired sequentially until the heating load is met. To avoid system inefficiency due to the addition of a heat exchanger, we used an 'ideal' heat exchanger (i.e., the effectiveness of the heat exchanger was assumed to be 1). We also used an 'UncontrolledOn' control scheme for the heat exchanger, which allows the heat exchanger to run whenever there is a nonzero flow in the main hot water loop.

Another limitation of this object is that it doesn't have a cutoff temperature. We used 'AvailabilityManagerLowTemperatureTurnOff' in the heat pump loop, which allows the loop to be disabled when the outdoor air temperature is below the cutoff temperature.

Figure 9. Configuration of heat pump and hot water loops

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/86199.yaml
     source: 86199_images/image_000010_5a97cb86c04ea095b17450da5d62d12511a21a051016eb21561f1836a9827cf7.png
     method: vision-description
     described: 2026-08-21 -->

![Diagram of a heat pump loop and hot water loop joined by a heat exchanger with a backup boiler](86199_images/image_000010_5a97cb86c04ea095b17450da5d62d12511a21a051016eb21561f1836a9827cf7.png)

Figure 9: block diagram of the modeled hydronic configuration. A heat pump boiler and its pump circulate a heat pump loop through a heat exchanger; on the other side the hot water loop carries its own pump, the heating coil, and a backup boiler downstream of the heat exchanger. Section 4.3 describes the OpenStudio implementation.

In this configuration, the heat pump will first attempt to lift the water temperature to the requested set point, followed by a backup heating element in the tank to address any remaining load not met by the heat pump.

The plant loop heat pump EIR heating model uses three performance curves-CapFTemp, EIRFTemp, and EIRPLR-to capture the impact of operating conditions on capacity and performance.

CapFTemp modifies the capacity of the heat pump based on the outdoor air and heat pump condenser outlet temperatures:

EIRFTemp modifies the EIR, which is the inverse of the coefficient of performance (COP), of the heat pump based on outdoor and heat pump condenser outlet temperatures:

EIRPLR modifies the EIR of the heat pump based on the part load ratio (PLR) and captures efficiency loss from compressor cycling:

We used data provided by Colmac [13] to generate the CapFTemp and EIRFTemp performance curves. During the measure development, we were not able to find performance data for EIRPLR. Thus, we assumed a linear variation between EIR and PLR that resulted in a 0% reduction in EIR at 1 PLR and a 25% reduction in EIR for a PLR close to zero. More detail about the performance curves is given in Appendix A.

Figure 10 and Figure 11 show how the CAPFT and EIRFT curve output values change with outdoor air temperature and hot water leaving temperature. As shown in Figure 10, the CAPFT value increases as the outdoor air temperature and condenser leaving water temperature increase. The EIRFT curve shown in Figure 11 shows a decrease in EIR (improvement in COP) as the outdoor temperature increases and the condenser leaving water temperature decreases.

Figure 11. EIRFT performance curve output

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/86199.yaml
     source: 86199_images/image_000011_37b5a8029131e34d324a805ee1a59ecc8c65ffdedc9b1cdeda53e8d327f66aa0.png
     method: vision-description
     described: 2026-08-21 -->

![Two contour plots, CAPFT and EIRFT curve output vs outdoor and condenser water temperature](86199_images/image_000011_37b5a8029131e34d324a805ee1a59ecc8c65ffdedc9b1cdeda53e8d327f66aa0.png)

Figures 10 and 11 in a single bitmap: two filled contour plots of performance curve output against outdoor temperature (-15 to 30C) and condenser leaving water temperature (60 to 82C). CAPFT rises from 0.45 to 1.50 as outdoor air warms; EIRFT falls from 1.80 to 0.60 as outdoor air warms and leaving water cools. Figure 10's caption is printed inside the bitmap between the panels.

