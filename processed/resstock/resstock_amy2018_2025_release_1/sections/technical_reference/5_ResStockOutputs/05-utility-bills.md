<!-- resstock resstock_amy2018_2025_release_1 | technical_reference | docs/technical_reference_guide/5_ResStockOutputs.tex | status: site_page | source_url: https://github.com/NatLabRockies/resstock/blob/3888e2ff0a4764eb57de65ad0d103870330eb542/docs/technical_reference_guide/5_ResStockOutputs.tex | publication_url: https://natlabrockies.github.io/ResStock.github.io/assets/trd/ResStockTechnicalReferenceGuide_2025_1.pdf | corpus_version: resstock_amy2018_2025_release_1-v1-pre | corpus_path: technical_reference/docs/technical_reference_guide/5_ResStockOutputs.md | section: Utility Bills | lines: 362-389 -->
## Utility Bills

The ResStock workflow is able to accept a limited range of utility rate inputs and output the corresponding utility bills. The inputs available are fixed charges and volumetric rates for each modeled fuel (typically electricity, natural gas, propane, and fuel oil). These can vary by any one housing characteristic, such as State. Multiple scenarios may be specified. For the list of utility bill outputs, see Table “ResStock cost multiplier output field names, units, and descriptions”.

Our most common approach within the ResStock workflow for utility rates for electricity and natural gas is to use a single scenario, using both a flat charge and a per-consumption charge. We typically use data downloaded from [NREL’s Utility Rate Database](https://openei.org/wiki/Utility_Rate_Database) to calculate the customer-weighted average fixed monthly electricity charge across all utilities in the database, which comes out to approximately \$10/customer/month or \$120/customer/year. For natural gas, we use the American Gas Association’s 2015 value of \$11.25/customer/month for the fixed portion of the utility bill (generally referred to as the “customer charge”). We additionally use EIA state-level information on revenue, sales, and number of customers to calculate the average per-consumption electricity and natural gas rate for each state with the fixed charges removed. The total electricity and natural gas bills for each housing unit model sample are then calculated by summing the flat charge and the product of the per-consumption charge and the total consumption. For example, this process may result in a flat charge of \$120/year and a per-consumption electricity rate of \$0.20/kWh—for a housing unit with a full year electricity consumption of 3000 kWh, the total electricity bill would be \$120 + (3,000 kWh \* \$0.20/kWh) = \$720. If a housing unit has uses no natural gas for the year, the flat charge is not included as it is presumed not to have natural gas service.

Our most common approach within the ResStock workflow for utility rates for propane and fuel oil is to use a single scenario using weekly volumetric rate data from the EIA, averaged over a year (either a calendar year or a winter). When state-level data are not available, we use data from the state’s Petroleum Administration for Defense Districts (PADD) region. When PADD region data are not available, we use U.S. national average values. We then calculate propane and fuel oil bills by multiplying the fuel consumption for each housing unit model by the volumetric rate for that fuel and state. An example of this is in ResStock dataset 2024.1 (Present et al. 2024).

In public ResStock datasets, these fields are prefixed with “out.bills.”

We do not currently commonly model other on-site fuel use in ResStock, such as on-site use of wood or coal, or district steam, and we do not have a common approach for calculating associated bills.

<div id="table:hc_cost_multipliers" data-source="5_ResStockOutputs.tex">

| **Field Name** | **Units** | **Description** |
|:---|:---|:---|
| out.bills.all_fuels.usd | \$ | Annual total charges for electricity, fuel oil, natural gas, and propane |
| out.bills.electricity.usd | \$ | Annual total charges for electricity |
| out.bills.fuel_oil.usd | \$ | Annual total charges for fuel oil |
| out.bills.natural_gas.usd | \$ | Annual total charges for natural gas |
| out.bills.propane.usd | \$ | Annual total charges for propane |

ResStock utility bill output field names, units, and descriptions

</div>

ResStock results can also be used as inputs to calculate utility bills using other rate structures, such as time-of-use electricity rates or tiered rates. However, these calculations are currently not included in the primary ResStock workflow or any published datasets.

