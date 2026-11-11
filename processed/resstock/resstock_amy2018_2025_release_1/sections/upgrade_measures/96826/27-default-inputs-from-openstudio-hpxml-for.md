<!-- resstock resstock_amy2018_2025_release_1 | upgrade_measures | measure_pdfs/96826.pdf | status: osti_pdf | source_url: https://docs.nlr.gov/docs/fy26osti/96826.pdf | publication_url: https://docs.nlr.gov/docs/fy26osti/96826.pdf | corpus_version: resstock_amy2018_2025_release_1-v1-pre | corpus_path: upgrade_measures/measure_pdfs/96826.md | section: Default Inputs From OpenStudio-HPXML for the Measure Upgrade Name | lines: 389-434 -->
## Default Inputs From OpenStudio-HPXML for the Measure Upgrade Name

The ResStock inputs in the table above are sent to OpenStudio-HPXML. Any values that are not specified by ResStock are calculated using the defaults in the BuildResidentialHPXML

OpenStudio measure. These details can also be found in the OpenStudio-HPXML documentation v1.10.0.

Table 6. HPXML Default Values for the HPWH Upgrade

<!-- table recovered from measure_pdfs/96826.pdf p.19
     overlay: resstock_resstock_amy2018_2025_release_1/upgrade_measures/measure_pdfs/96826.yaml
     method: vision-transcription
     supersedes the extractor's own table here (values 2a1748bd4697…):
       The extractor merged the sub-rows of two variables into single cells and lost values. Standby Loss read '3.6 4.0 4.7' in one cell. Nominal Heating Capacity read '6,887 2.02 7,203 2.11 7,334': the 80-gal value 2.15 kW and the '80-gal, 3.98 UEF' label were dropped, and the Btu/h and kW values ran together with nothing tying each to its tank size. The Notes column was also split in two with most notes duplicated. In the PDF each tank size has its own sub-row (50-gal: 6,887 Btu/h, 2.02 kW; 66-gal: 7,203 Btu/h, 2.11 kW; 80-gal: 7,334 Btu/h, 2.15 kW). One row per printed value; the shared note is repeated. -->

**Standby Loss to Fraction Domestic Hot Water Load Served**

| HPXML Default Variable | Value | Units | Notes: HPWH option | Notes |
|---|---|---|---|---|
| Standby Loss | 3.6 | Btu/h°F | 50-gal, 3.78 UEF | Based on values from lab testing of different sized HPWHs (Kvaltine & Larson, 2015) |
| Standby Loss | 4.0 | Btu/h°F | 66-gal, 3.95 UEF | Based on values from lab testing of different sized HPWHs (Kvaltine & Larson, 2015) |
| Standby Loss | 4.7 | Btu/h°F | 80-gal, 3.98 UEF | Based on values from lab testing of different sized HPWHs (Kvaltine & Larson, 2015) |
| Is Shared System | No | - |  | Whether it serves multiple units or shared laundry room |
| Fraction Domestic Hot Water Load Served | 1.0 | - |  | For a house with more than one water heater, this specifies the fraction of total hot water load a water heater is serving. |

**Nominal Heating Capacity**

| HPXML Default Variable | Value | Units | Notes: HPWH option | Notes |
|---|---|---|---|---|
| Nominal Heating Capacity | 6,887 | Btu/h | 50-gal, 3.78 UEF | Value is a function of the heat pump COP, which is converted from UEF using the usage bin. |
| Nominal Heating Capacity | 2.02 | kW | 50-gal, 3.78 UEF | Value is a function of the heat pump COP, which is converted from UEF using the usage bin. |
| Nominal Heating Capacity | 7,203 | Btu/h | 66-gal, 3.95 UEF | Value is a function of the heat pump COP, which is converted from UEF using the usage bin. |
| Nominal Heating Capacity | 2.11 | kW | 66-gal, 3.95 UEF | Value is a function of the heat pump COP, which is converted from UEF using the usage bin. |
| Nominal Heating Capacity | 7,334 | Btu/h | 80-gal, 3.98 UEF | Value is a function of the heat pump COP, which is converted from UEF using the usage bin. |
| Nominal Heating Capacity | 2.15 | kW | 80-gal, 3.98 UEF | Value is a function of the heat pump COP, which is converted from UEF using the usage bin. |

**Backup Heating Capacity to Tank Model Type**

| HPXML Default Variable | Value | Units | Notes: HPWH option | Notes |
|---|---|---|---|---|
| Backup Heating Capacity | 15,355 or 4.5 | Btu/h kW |  | - |
| Has Flue or Chimney In Conditioned Space | Depends on the heating system | - |  | (Atmospheric) flue vent is assumed to be shared between space heating and water heating. The flue vent remains when the (existing) fuel heater is in the conditioned space and has an annual fuel utilization efficiency (AFUE) or equivalent efficiency rating of <89%, even as water heating no longer needs it. |
| Number of Bedrooms Served | N/A | - |  | Not applicable as it is only used if the water heater is a shared system. |
| HPWH Operating Mode | Hybrid | - |  | In the hybrid mode, the backup only turns on when heat pump is not producing enough hot water. |
| Uses Desuperheater | False | - |  | - |
| Tank Model Type | Stratified | - |  | This means the tank does not assume uniform water temperature throughout. Instead, a realistic thermal gradient exists when hot water is drawn, and different heating components come on accordingly based on the thermostatic control. |

