<!-- resstock resstock_amy2018_2025_release_1 | upgrade_measures | measure_pdfs/95032.pdf | status: osti_pdf | source_url: https://docs.nlr.gov/docs/fy26osti/95032.pdf | publication_url: https://docs.nlr.gov/docs/fy26osti/95032.pdf | corpus_version: resstock_amy2018_2025_release_1-v1-pre | corpus_path: upgrade_measures/measure_pdfs/95032.md | section: Where: | lines: 559-578 -->
## Where:

ff: Fraction of nominal airflow rate

Qfaf : Multiplier on heating/cooling capacity as a function of airflow rate

EIRfaf : Multiplier on efficiency as a function of airflow rate

Airflow rate curves and the coefficients used in the model are shown below:

Figure 8. Normalized single-stage GHP capacity as a function of airflow

![Image](95032_images/image_000006_9fd4a9d9d0d51492d2d3a745371f30847dba7f41211210885e29b9dc4d37cfd2.png)

Figure 9. Normalized single-stage GHP efficiency as a function of airflow

![Image](95032_images/image_000007_8e91835e9eedff3807fb19af0a4acdfddb59ca8d776842e86343f49d15c6a5b0.png)

The normalized capacity and EIR results shown above allow some impact to be seen in the event that airflow is reduced, either due to faults at installation or degradation over time (such as fouling of the ducts). During these reduced airflow conditions, the EIR (which is one over COP) increases, which means the efficiency of the unit goes down, as does the capacity, capturing the impact these faults may have on operation. The current default for ResStock is to assume that no faults occur in GHP upgrade cases. This corresponds to assuming ducts are in good working order and installation is performed correctly. However, future scenarios could take advantage of the ability to model faults if looking at performance over time or existing GHP installations if good data for the number of homes experiencing faults were available.

