<!-- resstock resstock_amy2018_2025_release_1 | upgrade_measures | measure_pdfs/95032.pdf | status: osti_pdf | source_url: https://docs.nlr.gov/docs/fy26osti/95032.pdf | publication_url: https://docs.nlr.gov/docs/fy26osti/95032.pdf | corpus_version: resstock_amy2018_2025_release_1-v1-pre | corpus_path: upgrade_measures/measure_pdfs/95032.md | section: 2.2.4   Representing Cycling Within a Simulation Timestep | lines: 552-586 -->
## 2.2.4   Representing Cycling Within a Simulation Timestep

EnergyPlus allows users to enter a curve that impacts the efficiency of equipment at part load. This curve modifies the efficiency of the unit during times when the equipment only needs to run for a portion of the timestep and generally accounts for any losses that may occur due to cycling of equipment. 17 EnergyPlus uses the part load factor (which is related to the part load ratio by a user defined curve, with the specific curve used for GHPs shown in Figure 7) to determine the impact of cycling on HVAC equipment, with the efficiency directly proportional to the part load factor (which ranges from 0 -1).

A new approach to modeling cycling losses is being applied to GHPs in ResStock that differs significantly from the approach used for other residential HVAC systems such as air conditioners and ASHPs. Traditional air-to-air systems in EnergyPlus use a simplified method based on the coefficient of degradation (cd), typically derived from laboratory testing. A cd value of 0 indicates no degradation in performance due to cycling, and if the value is not known, EnergyPlus assumes a conservative default of 0.25, representing relatively high losses during part-load operation.

For GHPs, curves that relate the part load factor and part load ratio can therefore be used to have EnergyPlus account for any cycling losses that might occur for this equipment. For air-to-air equipment, a test to determine the coefficient of degradation (cd) is generally performed and reported. A cd value of 0 would represent no cycling losses, and if cd is not reported, a worst-case value of 0.25 is assumed. However, cd is generally not reported for water-to-air coils like those used for GHPs. Nevertheless, a European standard test, EN14825 (European Committee for Standardization (CEN) 2022) does capture the impact of cycling and allows for determining a way to model these impacts on the overall efficiency of the unit. They report a standby loss coefficient Cc. Unlike cd for air-to-air equipment, a value of 1.0 for Cc would represent no cycling losses, and a default worst-case value of 0.9 is used if it is not reported (Piechurski, Szulgowaska-Zgrzywa and Danielewicz 2018). Part load factor, part load ratio, and the standby loss coefficient can be related to each other using:

Where:

PLF : Part load factor

PLR : Part load ratio

Cc : Standby loss coefficient

For the GHP model for single-stage systems, this relationship was used with an assumed worstcase value of 0.9 for Cc. EnergyPlus is generally expecting curves to be in a polynomial form (up to a cubic) and so a curve fit was used to relate the exact equation shown above to a cubic relationship EnergyPlus could use, as shown in Figure 7. The curve fit is limited so that values can never be greater than 1.0 or less than 0.7 to avoid unreasonably large part-load impacts during low part-load conditions.

17 ResStock simulates 15-minute timesteps.

Figure 7. Curve used for the part load factor (PLF) as a function of part load ratio (PLR) for GHPs

<!-- figure described by overlay: resstock_resstock_amy2018_2025_release_1/upgrade_measures/measure_pdfs/95032.yaml
     source: 95032_images/image_000005_4dfb61b921b84d56dee7f26c56923efe615391f76fdf44f7bb2b4a1840031c3e.png
     method: vision-description
     described: 2026-11-11 -->

![Scatter plot of part load factor against part load ratio with a cubic fit, Cc = 0.9](95032_images/image_000005_4dfb61b921b84d56dee7f26c56923efe615391f76fdf44f7bb2b4a1840031c3e.png)

Figure 7: scatter plot titled 'Part Load Factor, Cc = 0.9'. X-axis is part load ratio (PLR), 0 to 1; y-axis is part load factor (PLF), -0.2 to 1.2. Points rise steeply from 0 at PLR 0, then flatten toward 1.0. A dotted fitted curve, y = 3.0626x^3 - 6.0299x^2 + 3.8941x + 0.1186 (R^2 = 0.9701), is held at a floor of 0.7 below PLR 0.2.

The implication of using this new method is that GHPs may appear to suffer energy losses during cycling, especially in climates with highly unbalanced thermal loads (e.g., predominantly heating- or cooling-dominated regions) or with long swing seasons or mild climates. In these climates, part-load operation occurs more frequently, and the steeper part-load factor penalty results in a higher modeled energy use. Single-stage GHP systems are impacted more than twostage and variable-speed compressor systems.

For GHPs, additional curves can also be used to set the efficiency and capacity as a function of water flow rate and airflow rate. These curves allow performance to be corrected for airflow rates and water flow rates different from the nominal conditions. However, care must be taken that these relationships are not double-counting the impact of cycling, which is generally handled by the part load factor. While manufacturer spec sheets do report efficiency and capacity at different water and airflow rates, single-stage equipment generally operates at a single flow rate, where the exact flow rate used might vary based on the equipment size and application. Only three water flow rates are reported in the spec sheet for this unit, while a wider variety of airflow rates are reported. Curves for different water flow rates are not used, with the assumption that any cycling losses are fully captured by the part load factor and a purely single-stage pump would always be used with a single-stage GHP. Curves for airflow, however, are provided to allow for the possibility of a variable-speed fan with a single-stage system. Curves for airflow also allow for the model to account for faults that may impede airflow that can occur in real equipment over time or due to poor installation. When these curves are used for airflow, they use quadratic relationships:

