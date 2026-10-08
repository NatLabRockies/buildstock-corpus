<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/95013.pdf | status: osti_pdf | source_url: https://docs.nlr.gov/docs/fy26osti/95013.pdf | publication_url: https://docs.nlr.gov/docs/fy26osti/95013.pdf | corpus_version: 0396270 | corpus_path: upgrade_measures/measure_pdfs/95013.md | section: 3.1.1 Demand Flexibility Measures Applicability | lines: 294-310 -->
## 3.1.1 Demand Flexibility Measures Applicability

The two upgrades share the same building types-office buildings (small, medium, and large), warehouses, and schools (primary and secondary). But although the lighting control upgrade assumes that all the lighting systems in the applicable buildings are controllable for the measure to be applied (some existing old lighting systems might require additional retrofitting/controls to implement the measure), the thermostat control measure will only affect thermostats associated with electric heating, ventilating, and air-conditioning (HVAC) equipment in a building, as shown in Figure 2. Overall, the package is applicable to 67.26% of the stock floor area.

Figure 2. Prevalence of building types and applicability for each building type (for both scenarios) and HVAC fuel type (for the thermostat control scenario)

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/95013.yaml
     source: 95013_images/image_000003_e64522bd53ae584f7350422ec0942b28f3be55741f65f5df4b3aad4aa940ae9f.png
     method: vision-description
     described: 2026-08-20 -->

![Two-panel horizontal bar chart of percent stock floor area by building type and the applicability of the measure](95013_images/image_000003_e64522bd53ae584f7350422ec0942b28f3be55741f65f5df4b3aad4aa940ae9f.png)

Figure 2. Two-panel horizontal bar chart. Left panel: % of Stock Floor Area by ComStock building type, x-axis 0 to 30%. Values: FullServiceRestaurant 1.52%, Hospital 3.79%, LargeHotel 5.66%, LargeOffice 8.54%, MediumOffice 6.42%, Outpatient 2.91%, PrimarySchool 8.54%, QuickServiceRestaurant 0.48%, RetailStandalone 8.57%, RetailStripmall 8.10%, SecondarySchool 8.84%, SmallHotel 0.98%, SmallOffice 6.77%, and Warehouse 28.71% (by far the largest share). Right panel: Applicability % of Building Type Area, split into 'Applicability - electric HVAC' (cool only / heat & cool / not applicable) and 'Applicability - building type' (applicable / not applicable) with percentages stacked to 100% per row. Establishes that the measure applies to most floor area, with warehouses dominating the stock. (Dense small labels -- flag exact percentages for QA.)

Both upgrade measures will identify the building types for each ComStock baseline model, with the same building type applicability criteria. If the building type passes the applicability check, the thermostat control measure will then extract all the thermostats of the model and check the fuel sources of the associated HVAC systems. The measure will identify and adjust the temperature set point schedules of the thermostats controlling the electric heating systems or the electric cooling systems.

