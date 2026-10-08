<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/89130.pdf | status: osti_pdf | source_url: https://www.nlr.gov/docs/fy24osti/89130.pdf | publication_url: https://www.nlr.gov/docs/fy24osti/89130.pdf | corpus_version: 43ae2d4 | corpus_path: upgrade_measures/measure_pdfs/89130.md | section: 2  ComStock Baseline Approach | lines: 605-674 -->
## 2  ComStock Baseline Approach

This measure replaces existing gas-fired cooking equipment in kitchen space types with comparable electric equipment. The measure only applies to building types in ComStock that already have kitchens:

- Hospital
- Large hotel
- Primary school
- Secondary school
- Strip mall
- Quick service restaurant
- Full-service restaurant.

Figure 7 shows the fraction of buildings by type that include various food service types according to CBECS 2012 [4]. This data suggests that medium/large offices and outpatient buildings may have some prevalence of cooking equipment; however, these models do not currently contain 'kitchen' space types and are therefore not modeled with cooking equipment. Cooking equipment may be added to these building types in future ComStock work. Note that food service building types in CBECS do not use these metrics, so they show 0%, when in reality they are 100%.

Figure 7. Weighted fraction of stock floor area with food service by building type. Data is from CBECS 2012 [4]. CBECS samples can include more than one food service type, so total stock percentage may exceed 100%.

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/89130.yaml
     source: 89130_images/image_000017_20e74705323d9edf861029cfd41e31870472a213a8da158d00ff560ec7f715ab.png
     method: vision-description
     described: 2026-08-21 -->

![Stacked bar chart of weighted stock percentage with food service by ComStock building type](89130_images/image_000017_20e74705323d9edf861029cfd41e31870472a213a8da158d00ff560ec7f715ab.png)

Figure 7: stacked bar chart of weighted stock percent by building type, each bar split into buildings with a snack bar, fast food, a cafeteria and a commercial kitchen, so totals can exceed 100%. Hospital is highest at about 146%, then strip mall near 90% (mostly fast food) and secondary school at 74%; the restaurant types read 0% by CBECS convention. Data from CBECS 2012.

The ComStock baseline uses building-type-specific probability distributions of commercial cooking equipment. Multiple data sources were used to derive these distributions, which include both gas and electric equipment. The prevalence of gas versus electric fuel types for each equipment type and the rated power for each gas and electric appliance are shown in Table 15, and the derivation of these values was described in Section 1.

Table 15. Gas Versus Electric Prevalence and Rated Power for Each Cooking Appliance

| Appliance   |   % Gas |   % Electric |   Rated Power - Gas (Btu/h) |   Rated Power - Electricity (kW) |
|-------------|---------|--------------|-----------------------------|----------------------------------|
| Broiler     |    0.91 |         0.09 |                      96,000 |                             10.8 |
| Griddles    |    0.58 |         0.42 |                      90,000 |                             17.1 |
| Fryers      |     0.5 |          0.5 |                      80,000 |                             14.0 |
| Ovens       |    0.55 |         0.45 |                      44,000 |                             12.1 |
| Ranges      |    0.91 |         0.09 |                     145,000 |                             21.0 |
| Steamers    |    0.33 |         0.67 |                     200,000 |                             27.0 |

The breakdown of equipment types and quantities for each ComStock building type was done using a dataset of equipment counts per restaurant type [7]. While this data source is from 1996, there is limited literature on this topic, and it is not expected that the breakdown of equipment types in a restaurant would have changed drastically over the past few decades. The restaurant types were mapped to ComStock building types, and probability distributions and equipment quantities for each restaurant type were generated for sampling. In addition, the breakdowns of gas versus electric equipment were also added via the sampling process based on the percentages in Table 1.

Figure 8 shows the final sampled breakdowns of equipment type fractions for each restaurant type. Note that the percentages shown in the breakdown represent the percentage of the total count of equipment, not the percentage of energy consumed. As can be seen, some restaurant types assume vastly different breakdowns of equipment than others based on what type of food is served in each establishment. In addition, not every restaurant type has all six types of cooking equipment. This methodology adds realistic and data-driven diversity to kitchen space types in ComStock modeling, as opposed to modeling all kitchens in all building types the same way. Scaling factors are added in the ComStock workflow to scale equipment counts based on kitchen floor area. The specific methods and probability distributions used to generate the cooking equipment quantities for each building type are discussed in the ComStock Reference Documentation [17].

Figure 8. Fraction (by equipment count) of cooking equipment types by restaurant type

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/89130.yaml
     source: 89130_images/image_000018_3ea9e2674e380a7d04a491ce9ca2f9f427749c1552b6dd5cd0c85ea19322d5a9.png
     method: vision-description
     described: 2026-08-21 -->

![Horizontal 100% stacked bar chart of cooking equipment mix by restaurant type](89130_images/image_000018_3ea9e2674e380a7d04a491ce9ca2f9f427749c1552b6dd5cd0c85ea19322d5a9.png)

Figure 8: horizontal 100% stacked bar chart titled Breakdown of Cooking Equipment by Restaurant Type, one row per restaurant type with segments for broilers, fryers, griddles, ovens, ranges and steamers. Fryers dominate the fish, chicken and donut rows, and several types carry no broilers or steamers at all. Section 2 notes these are equipment counts, not energy shares.

The ComStock workflow then uses the equipment quantities and equipment fuels from the sample, and the rated power values from Table 15, to generate equipment objects in the model. Each type of equipment is modeled as its own object using a design level value in watts (gas equipment Btu/h values are converted to W). Note that there are separate object types for gas and electric equipment, but the inputs are the same. The quantity of equipment is included in the name of the object, and the design level is calculated by multiplying the quantity by the rated input power for that appliance from Table 15.

In addition, a 'Miscellaneous Electric Kitchen Equipment' object is included in each kitchen space type to account for non-major electrical appliances found in kitchens, such as microwaves, heating lamps, toasters, coffee machines, electric kettles, etc. This miscellaneous load is calculated such that it represents 10% of the total kitchen electric load.

An example screenshot of a gas equipment object from a model is shown in Figure 9. As can be seen, the quantity of the equipment is found in the object name. The design level field represents the rated input power of the appliance multiplied by the quantity. Note that the quantities in the models can be fractional, which is a result of the equipment quantity calculations based on kitchen size.

Figure 9. Example of gas equipment object from OpenStudio ®

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/89130.yaml
     source: 89130_images/image_000019_25d21eb6e66dba2e40388aef90a20f9b09680773039a537fd0c7da7abe032464.png
     method: vision-description
     described: 2026-08-21 -->

![Screenshot of an OpenStudio GasEquipment Definition object for a gas fryer](89130_images/image_000019_25d21eb6e66dba2e40388aef90a20f9b09680773039a537fd0c7da7abe032464.png)

Figure 9: screenshot of the OpenStudio OS:GasEquipment:Definition editor for the object gas_fryer_equipment_definition_bldg_quantity=1.0. The design level calculation method is EquipmentLevel with a design level of 48,100 W, watts per floor area and per person left blank, and fraction latent 0.1, radiant 0.2 and lost 0.7 - the values Table 14 assigns.

