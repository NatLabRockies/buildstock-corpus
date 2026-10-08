<!-- comstock comstock_amy2018_2025_release_3 | technical_reference | documentation/reference_doc/5_outputs.tex | status: site_page | source_url: https://github.com/NatLabRockies/ComStock/blob/b77c60d341c9b68c58c5d51e51b06f08f293d3cb/documentation/reference_doc/5_outputs.tex | publication_url: https://natlabrockies.github.io/ComStock.github.io/assets/files/comstock_reference_documentation_2025_3.pdf | corpus_version: 0a2f61f | corpus_path: technical_reference/documentation/reference_doc/5_outputs.md | section: Utility Bills | lines: 165-289 -->
## Utility Bills

ComStock estimates utility bills for several of the primary fuels consumed in buildings. Although the rest of ComStock represents the building stock circa 2018, the utility bill estimates reflect utility rates circa 2022, which was the most recent year of data available from EIA at the time of implementation. We made this choice because most users of the data were assumed to prefer bills that most closely reflect the present for decision making.

### Electric Bills

The primary resource for the electric utility rates is the Utility Rate Database (URDB) (Ong and McKeel 2012). This database contains machine-readable descriptions of electric rate structures which have been compiled by manually processing utility rate documentation published by utilities.

#### Rate Selection

URDB contains electric rates that span all sectors (residential, commercial, industrial, etc.), so we limited the rates to those applicable to commercial buildings. First, we filtered down to rates identified as serving the commercial sector and not supplied at transmission voltage. Second, we processed the utility rate names to eliminate rates serving non-building loads based on certain keywords. The list of keywords included Agriculture, Irrigation, Farming, Pump, Snow, Vehicle, Oil, Cotton Gin, Outdoor Light, Security Light, Street, Wholesale, Recreation, Heating (typically found in names of heating-only rates), Substation, and Electric Motor Standby. We downloaded the detailed rate structure data in JSON format for the selected 13,923 rates.

Next, we fed each utility rate and an 8,760-hour electric consumption profile from a Small Hotel building energy model to NREL PySAM (NREL 2023) to calculate an annual electric bill. We eliminated rates with an annual average blended price below \$0.01/kWh. Upon reading the names and comments included with these rates, we found that they were mostly fixed rates for individual pieces of equipment such as cable or internet infrastructure that are not metered. We also eliminated rates with an annual average blended price above \$0.45/kWh, except in the case of AK or HI, which legitimately have high rates. Some of the high rates appeared to be data entry errors. We also removed rates where PySam could not calculate an annual bill based on the rate data. Overall, this process resulted in 10,623 remaining rates spread across 2,658 utilities. 90% of the utilities have 8 or fewer rates. The remainder have more rates, with the most ( 200) belonging to Southern California Edison. These rates cover 85% of the buildings and 85% of the floor area in ComStock. Rates are stored in machine-readable JSON format and organized by EIA Utility Identifier.

A distribution of blended rates calculated using URDB was compared to a distribution of the blended rates calculated using data from EIA (U.S. Energy Information Administration 2022a). The median blended price in the URDB rates was about \$0.08/kWh, while the median blended price reported to EIA in 2022 was \$0.12/kWh, which is about 50% higher than URDB. An analysis of the start date fields for the rates selected from URDB showed a median start date of 2013, which is more than ten years old at the time of writing.

In order to understand the change in rates between 2013 and 2022, a pairwise analysis of the utilities reporting to EIA (U.S. Energy Information Administration 2022a) in both years was performed, and a state-wide average annual change was calculated. The median increase was 1-3% per year. Thus in many cases the rates have increased by (2%/yr \* (2022-2013)) = 18% or more between 2013 and 2022.

#### Electric Utility Assignment

To assign an electric rate to a building in ComStock, we need to know which electric utility serves it. We joined the U.S. DOE Electric Utility Companies and Rates Look-up by Zipcode (Huggins 2021) with the U.S. HUD USPS ZIP Code Crosswalk Files (HUD PD&R 2023) to create a mapping between census tracts and utilities. This was done using both 2010 and 2020 census tracts, because ComStock uses a mix of both. As previously described, rates are assigned to 85% of the buildings in ComStock, and cover 85% of the weighted floor area. There are approximately 37,734 ZIP Codes in the United States. The dataset does not have an electric utility assignment for 738 of these ZIP Codes, which are spread across many states. There are 3,946 census tracts covered by these ZIP Codes which therefore do not have an electric utility assigned. Manually filling these missing mappings could be done in future work.

#### Bill Calculation

At runtime, an 8,670-hour electric load profile is extracted from the building energy model. The annual min and max demand (kW) and annual energy consumption (kWh) are calculated. The final census tract to which the simulation’s results will be allocated is not known at simulation time, but the range of possible tracts is known based on the sampling region. For all possible census tracts, the electric utility EIA identifier is looked up. If rates are found for this utility, the rates are downselected based on the observed load profile any min/max demand or energy consumption qualifiers the rate may have. For example, some rates only apply to buildings with a minimum annual peak demand of 500 kW. For each of the remaining applicable rates, the annual bill is calculated using the 8,760 load profile and the PySAM utility rate calculation engine. This engine accounts for complex rate structures with demand charges, lookback periods, time-of-use rates, etc. To adjust for the lag in the rates on the URDB, the start date for rate is collected and the number of years between the start date and 2022 is calculated. The average annual price increase for the state where the building is located, which was calculated from Form EIA861 data as previously described, is looked up. The annual bill is multiplied by this increase to estimate an adjustment to current 2022 rates.

A median bill cost is calculated from the set of all costs from all applicable rates. Any bill that is lower than 25% of the median or higher than 200% of the median is eliminated to avoid extreme bills. Although uncommon, in testing these extreme bills were found to be associated with rates whose names indicate they are likely not applicable to the building. For example, a “large secondary general” rate which has a high minimum demand charge is not likely applicable to a small retail customer. This step typically only affects the mean bill for a building +/- 10%, so the other applicability criteria appear to be downselecting appropriate rates effectively. The minimum, maximum, and mean bills area reported along with the URDB rate label for the applicable rate, which can be used to locate details of the rate with the URDB API or via a URL, e.g.: "https://apps.openei.org/USURDB/rate/view/\[rate_label\]". If the number of applicable rates is even, a single median bill will not have a specific applicable rate (being the average of the middle two values). Thus in all cases, a ’median_low’ and ’median_high’ bill and applicable rate label are reported, representing the two central values in the bill results if the total number is even, or the duplicated true median value if the total number is odd. For tracts where no electric utility assigned, or for buildings where none of the stored rates for the utility are applicable, the annual bill is estimated using the 2022 EIA Form861 (U.S. Energy Information Administration 2022a) average prices based on the state the building is located in. While this method does not reflect the detailed rate structures and demand charges, it is a fallback for the 15% of buildings in ComStock with no utility assigned.

After simulation, when individual results are allocated to tracts and weights computed, the applicable bills are weighted accordingly. The weighted bills are summed when the tract results area aggregated by geographies (e.g. by PUMA, County or State), and aggregate bill savings are calculated.

### Natural Gas Bills

Natural gas bills are calculated using state-level, volumetric rates due to a lack of detailed public databases of natural gas rates. 2022 U.S. EIA Natural Gas Prices  Commercial Price and U.S. EIA Heat Content of Natural Gas Delivered to Consumers (U.S. Energy Information Administration 2022b) were used to create an energy price in dollars per kBtu. State-level prices range from \$0.007/kBtu in ID to \$0.048/kBtu in HI, with a mean of \$0.012/kBtu nationally.

### Propane and Fuel Oil Bills

Propane and fuel oil bills are calculated using volumetric rates due to a lack of detailed public databases of rates. Rates are state-level where this data is available, and use national average pricing where not. These fuels are typically delivered in batches, so in any given year the number of deliveries could vary. Minimum charges per delivery are assumed to be included in the volumetric price. 2022 U.S. EIA residential No. 2 Distillate Prices by Sales Type and U.S. EIA residential Weekly Heating Oil and Propane Prices (October  March) (U.S. Energy Information Administration 2023) were downloaded, along with the EIA assumed heat content for these fuels. Residential prices were used because commercial prices are only available at the national scale. Additionally, most commercial buildings using these fuels are assumed to be smaller buildings where a residential rate is likely realistic. These data were used to create an energy price in dollars per kBtu for both fuels.

For states where state-level pricing was available, these prices are used directly. For other states, Petroleum Administration for Defense District (PADD)-average pricing was used. For states where PADD-level pricing was not available, national average pricing was used. For propane, prices ranged from \$0.022/kBtu in ND to \$0.052 in FL, with a mean of \$0.032/kBtu nationally. For fuel oil, prices ranged from \$0.027/kBtu in NE to \$0.036 in DE, with a mean of \$0.033/kBtu nationally. The mean national price for both fuels is roughly three times the mean national price of natural gas.

### District Heating and District Cooling Bills

No resources with utility rates for district heating and cooling were identified. Because there are several hundred district systems across the U.S., many of which are university or healthcare campuses, gathering individual rates manually was deemed impractical. Therefore, utility bills for these fuels are not calculated.

<div id="refs" class="references csl-bib-body hanging-indent">

<div id="ref-GAGNON2022103915" class="csl-entry">

Gagnon, Pieter, and Wesley Cole. 2022. “Planning for the Evolution of the Electric Grid with a Long-Run Marginal Emission Rate.” *iScience* 25 (3): 103915. <https://doi.org/10.1016/j.isci.2022.103915>.

</div>

<div id="ref-cambium2022" class="csl-entry">

Gagnon, Pieter, Brady Cowiestoll, and Marty Schwarz. 2023. *Cambium 2022 Scenario Descriptions and Documentation*. NREL/TP-6A40-84916. National Renewable Energy Laboratory. <https://www.nrel.gov/docs/fy23osti/84916.pdf>.

</div>

<div id="ref-cambium2021" class="csl-entry">

Gagnon, Pieter, Will Frazier, Wesley Cole, and Elaine Hale. 2021. *Cambium Documentation: Version 2021*. NREL/TP-6A40-81611. National Renewable Energy Laboratory. <https://www.nrel.gov/docs/fy22osti/81611.pdf>.

</div>

<div id="ref-lrmer_data2022" class="csl-entry">

Gagnon, Pieter, Elaine Hale, and Wesley Cole. 2022. *Long-Run Marginal Emission Rates for Electricity - Workbooks for 2021 Cambium Data*. National Renewable Energy Laboratory. <https://doi.org/10.7799/1838370>.

</div>

<div id="ref-tract_to_zip" class="csl-entry">

HUD PD&R. 2023. *HUD USPS ZIP CODE CROSSWALK FILES*. U.S. Department of Housing; Urban Development Office of Policy Development; Research. <https://www.huduser.gov/portal/datasets/usps_crosswalk.html>.

</div>

<div id="ref-zip_to_util" class="csl-entry">

Huggins, Jay. 2021. *U.s. Electric Utility Companies and Rates: Look-up by Zipcode (2021)*. National Renewable Energy Laboratory. <https://catalog.data.gov/dataset/u-s-electric-utility-companies-and-rates-look-up-by-zipcode-2021>.

</div>

<div id="ref-pysam" class="csl-entry">

NREL. 2023. *NREL-PySAM Documentation*. <https://nrel-pysam.readthedocs.io/en/main/>.

</div>

<div id="ref-urdb" class="csl-entry">

Ong, Sean, and Ryan McKeel. 2012. *National Utility Rate Database: Preprint*. National Renewable Energy Laboratory. <https://doi.org/10.2172/1050105>.

</div>

<div id="ref-eia_electricity" class="csl-entry">

U.S. Energy Information Administration. 2022a. *Monthly Energy Review*. <https://www.eia.gov/totalenergy/data/browser/index.php?tbl=T07.06#/?f=A>.

</div>

<div id="ref-eia_natural_gas" class="csl-entry">

U.S. Energy Information Administration. 2022b. *Natural Gas Explained*. <https://www.eia.gov/energyexplained/natural-gas/use-of-natural-gas.php>.

</div>

<div id="ref-eia_fuel_oil_and_propane" class="csl-entry">

U.S. Energy Information Administration. 2023. *Petroleum and Other Liquids*. <https://www.eia.gov/dnav/pet/pet_pri_dist_a_epd2_prt_dpgal_a.htm>.

</div>

<div id="ref-egrid2020" class="csl-entry">

U.S. Environmental Protection Agency (EPA). 2022. *Emissions and Generation Resource Integrated Database (eGRID), 2020*. Https://www.epa.gov/egrid.

</div>

<div id="ref-epa_ap42" class="csl-entry">

U.S. Environmental Protection Agency (EPA). 2024. *AP-42: Compilation of Air Emissions Factors from Stationary Sources, 2024*. Https://www.epa.gov/air-emissions-factors-and-quantification/ap-42-compilation-air-emissions-factors-stationary-sources.

</div>

</div>
