<!-- resstock resstock_amy2018_2025_release_1 | github_site | docs/FAQ.md | status: site_page | source_url: https://github.com/NatLabRockies/ResStock.github.io/blob/696c020d696137830ddae75abbfb477ae7af8eaa/docs/FAQ.md | publication_url: https://natlabrockies.github.io/ResStock.github.io/docs/FAQ.html | corpus_version: resstock_amy2018_2025_release_1-v1 | corpus_path: github_site/docs/FAQ.md | section: Modeling Methods, Assumptions, and Documentation | lines: 227-295 -->
## Modeling Methods, Assumptions, and Documentation

### Where can I find information about input data sources, modeling methodology, and assumptions?

ResStock reference documentation is available in the Published Datasets section of the [Data page](docs/data.md). This includes baseline and upgrade measure information. We generally publish an updated version with every dataset release.

Upgrade measure documentation is also available on the [Data page.](docs/data.md)

### Where is there documentation on what technologies are available in the upgrade measures?

The [Data page](docs/data.md) links to each dataset and the dataset technical documentation which covers the technologies and upgrades that are available.

### Does ResStock model rooftop solar PV?

Yes, ResStock does model rooftop solar PV. See more details on rooftop PV, assumptions, and limitations on [this explanation](docs/resources/explanations/PV_System_Assignment_and_Distributions.md).We recommend using [PVWatts](https://pvwatts.nlr.gov/) or [ReOPT](https://www.nlr.gov/reopt) to evaluate PV for a more comprehensive analysis.

### Are there electric vehicle (EV) charging profiles in the dataset?

Yes, there are EV profiles starting in the ResStock 2025 Release 1 dataset. See the [report](https://docs.nlr.gov/docs/fy25osti/93766.pdf) for more information.

### How are leap years modeled?

ResStock results using leap year weather are generated using weather files that contain 8784 hours.

Starting in ResStock 2025 Release 1, ResStock datasets are all 365 days. For datasets generated using leap year weather (i.e., AMY 2012), the dataset starts on January 1, includes February 29, and ends on December 30 instead of December 31. However, data from December 31 simulations are used when converting data into Eastern Standard Time for publication. Please see *What is the timezone of timestamps?* FAQ for more information.

In previous datasets that include results generated using leap year weather (AMY2012 in ResStock 2021 Release 1 and ResStock 2022 Release 1), ResStock datasets span 366 days or 8784 hours. Here is the relevant [OS-HPXML documentation](https://openstudio-hpxml.readthedocs.io/en/latest/workflow_inputs.html#id4).

### Are costs modeled?

ResStock models the cost of running the equipment, or the cost impact on the utility bill. None of the ResStock datasets include the first costs (also called upgrade or measure costs).

See the [ResStock technical reference documentation](assets/trd/ResStockTechnicalReferenceGuide_2025_1.pdf) for more information on how utility bills are calculated for the most recent release. Utility bill calculation methods may differ between releases.

### Does ResStock model water heaters in one location, or can the location vary?

The location can vary. They could be located in the attic, mechanical room, crawlspace, garage, basement, living area, outside, or in an unheated basement. More information can be found in the [ResStock technical reference documentation](assets/trd/ResStockTechnicalReferenceGuide_2025_1.pdf). Before the 2024 Release 2, we generally used this logic: in cold climates, the water heater was in the basement if there was one, living space otherwise. For hot climates, it'd be the garage if there was one, living space otherwise.

### Does ResStock consider duct sizing impacts with any HVAC upgrades?

When retrofitting a home with a heat pump, sometimes duct size needs to change because of a higher flow rate and a lower supply temperature. ResStock assumes that the duct size increases in all datasets up to and including the 2024 Release 2 dataset. However, this may not be done in practice.

### Partial air conditioning is being referenced from RECS 2009. Why has this not been updated?

We have not found a more recent dataset with the necessary data resolution. This includes RECS 2015 and RECS 2020. The dependencies of this characteristic’s distribution, such as cooling type, use more recent data, so the final distributions of partial air conditioning does not match RECS 2009 even though this is the data source.

### The lighting options available are 100% CFL or 100% of one lighting type. This is unlikely to be the case in buildings. How can I explain this to our clients?

This is a limitation of ResStock, we are not able to do a mixed lighting scenario because there are data limitations in RECS 2015. In reality, some homes may not have 100% of a certain type of lighting. If you are looking at this data, consider our other guidance on the number of samples recommended in order to draw conclusions.

### How are multifamily common areas modeled?

The residential housing units in multifamily buildings are modeled in ResStock and are not in ComStock.  All energy consumption specific to the housing unit is included in the modeled results, such as lighting, appliances, window air conditioners, and HVAC and water heaters that serve a single housing unit.

HVAC and water heating that serves multiple housing units are also included, with energy consumption allocated to the unit served and with adjustment factors applied to account for the energy consumption differences of shared equipment. These adjustment factors are set by OpenStudio-HPXML and from ANSI/RESNET 301.

Electric vehicle charging energy consumption from common areas is also included in ResStock results, allocated directly to the unit that is associated with each electric vehicle.

All other energy that provides services to common areas in multifamily buildings is not included in either ResStock or ComStock. Examples of this would include common area lighting, common laundry facilities, pools, and hot tubs, and elevators.

### How are wall cavity R-values determined?

Wall cavity R-values are determined through one-dimensional heat transfer within OS-HPXML. See [this explanation](docs/resources/explanations/Wood_Stud_Depth.md) for more information.

### What year of U.S. Census geography (e.g., counties, PUMAs) do ComStock and ResStock use?

ComStock and ResStock datasets reflect the 2010 National Historical GIS (NHGIS) GISJOIN standard codes for counties, PUMAs, and Census Tracts. Some model input data sources use 2020 Census geographies, and these are translated to 2010 before being integrated into the ComStock and ResStock workflows. However, 2020 geographic codes are not currently available in the ComStock and ResStock datasets.

For more information about geographic fields and codes used in the models, please refer to the [ComStock](https://natlabrockies.github.io/ComStock.github.io/docs/resources/explanations/reference_geographic_codes.html) and [ResStock](docs/resources/explanations/Geographic_Fields_and_Codes.md) user resources.
