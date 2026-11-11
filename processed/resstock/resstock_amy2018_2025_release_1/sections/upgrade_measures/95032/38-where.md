<!-- resstock resstock_amy2018_2025_release_1 | upgrade_measures | measure_pdfs/95032.pdf | status: osti_pdf | source_url: https://docs.nlr.gov/docs/fy26osti/95032.pdf | publication_url: https://docs.nlr.gov/docs/fy26osti/95032.pdf | corpus_version: resstock_amy2018_2025_release_1-v1-pre | corpus_path: upgrade_measures/measure_pdfs/95032.md | section: Where: | lines: 645-678 -->
## Where:

ff: Fraction of nominal airflow rate

Qfaf : Multiplier on heating/cooling capacity as a function of airflow rate

EIRfaf : Multiplier on efficiency as a function of airflow rate

Airflow rate curves and the coefficients used in the model are shown below:

Figure 8. Normalized single-stage GHP capacity as a function of airflow

<!-- figure described by overlay: resstock_resstock_amy2018_2025_release_1/upgrade_measures/measure_pdfs/95032.yaml
     source: 95032_images/image_000006_9fd4a9d9d0d51492d2d3a745371f30847dba7f41211210885e29b9dc4d37cfd2.png
     method: vision-description
     described: 2026-11-11 -->

![Scatter plot of normalized heat pump capacity against fraction of airflow, with quadratic fits](95032_images/image_000006_9fd4a9d9d0d51492d2d3a745371f30847dba7f41211210885e29b9dc4d37cfd2.png)

Figure 8: scatter plot titled 'Normalized Capacity'. X-axis is fraction of airflow, 0 to 1.4; y-axis is capacity multiplier, 0.92 to 1.04. Two series with dotted quadratic fits: total capacity (y = -0.3165x^2 + 0.8099x + 0.5068) and heating capacity (y = -0.1234x^2 + 0.3642x + 0.7594). Both pass through 1.0 at full airflow; at about 0.72 airflow total capacity falls to about 0.925 and heating capacity to about 0.957.

Figure 9. Normalized single-stage GHP efficiency as a function of airflow

<!-- figure described by overlay: resstock_resstock_amy2018_2025_release_1/upgrade_measures/measure_pdfs/95032.yaml
     source: 95032_images/image_000007_8e91835e9eedff3807fb19af0a4acdfddb59ca8d776842e86343f49d15c6a5b0.png
     method: vision-description
     described: 2026-11-11 -->

![Scatter plot of normalized EIR against fraction of airflow, with quadratic fits](95032_images/image_000007_8e91835e9eedff3807fb19af0a4acdfddb59ca8d776842e86343f49d15c6a5b0.png)

Figure 9: scatter plot titled 'Normalized EIR'. X-axis is fraction of airflow, 0 to 1.4; y-axis is EIR multiplier, 0 to 1.6. Two series with quadratic fits: cooling normalized EIR (y = 0.5789x^2 - 1.6182x + 2.0184) and heating normalized EIR (y = 1.3858x^2 - 3.0886x + 2.796). Cooling EIR falls from about 1.15 at 0.72 airflow to about 0.96 above full airflow; heating points scatter from 0.96 to 1.33.

The normalized capacity and EIR results shown above allow some impact to be seen in the event that airflow is reduced, either due to faults at installation or degradation over time (such as fouling of the ducts). During these reduced airflow conditions, the EIR (which is one over COP) increases, which means the efficiency of the unit goes down, as does the capacity, capturing the impact these faults may have on operation. The current default for ResStock is to assume that no faults occur in GHP upgrade cases. This corresponds to assuming ducts are in good working order and installation is performed correctly. However, future scenarios could take advantage of the ability to model faults if looking at performance over time or existing GHP installations if good data for the number of homes experiencing faults were available.

