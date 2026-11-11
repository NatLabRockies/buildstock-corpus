<!-- resstock resstock_amy2018_2025_release_1 | technical_reference | docs/technical_reference_guide/3c_ResStockInputs.tex | status: site_page | source_url: https://github.com/NatLabRockies/resstock/blob/3888e2ff0a4764eb57de65ad0d103870330eb542/docs/technical_reference_guide/3c_ResStockInputs.tex | publication_url: https://natlabrockies.github.io/ResStock.github.io/assets/trd/ResStockTechnicalReferenceGuide_2025_1.pdf | corpus_version: resstock_amy2018_2025_release_1-v1-pre | corpus_path: technical_reference/docs/technical_reference_guide/3c_ResStockInputs.md | section: Hot Water Fixtures | lines: 469-514 -->
## Hot Water Fixtures

Following the OpenStudio-HPXML default assumption, ResStock models hot water fixtures as 60% faucets and 40% showers and baths, operating at a mixed water temperature of 105° F for all housing units. None of the fixtures are assumed to be low-flow. However, low-flow options are available as upgrades.

The fraction of low-flow fixtures adjusts the demand to account for fixture efficiency. The demand is also multiplied by a fixture usage multiplier to add diversity. The hot water fixture usage multiplier is given by a log-normal distribution of values ranging from 40% to 200% (with mean at 80%[^1]) derived from the field data of 1,700 residential electric resistance water heaters in a demand management program in the U.S. Northeast census division.

### Hot Water Fixtures

#### Description

Hot water fixture usage and flow levels.

#### Distribution Data Sources

- Field data from a demand management program with 1,700 residential electric resistance water heaters in the Northeast U.S. census division.

#### Direct Conditional Dependencies

- Usage Level.

#### Options

The Hot Water Fixtures options are usage bins ranging from “50% Usage” to “200% Usage” at 10% increments. For the ResStock baseline, the options are log-normally distributed between 40% and 200%, with the peak at 80%. All options have both `water_fixtures_shower_low_flow` and `water_fixtures_sink_low_flow` set to false. `water_fixtures_usage_multiplier` is set according to their option names.

For the argument definitions, see Table “The ResStock argument definitions set in the Hot Water Fixtures characteristic”. See the OpenStudio-HPXML [Water Fixtures](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#hpxml-water-fixtures) documentation for the available HPXML schema elements, default values, and constraints.

<div id="table:hc_arg_def_hot_water_fix" data-source="3c_ResStockInputs.tex">

| Name | Required | Units | Type | Choices | Description |
|:---|:---|:---|:---|:---|:---|
| `water_fixtures_shower_low_flow` | true |  | Boolean | true, false | Whether the shower fixture is low flow. |
| `water_fixtures_sink_low_flow` | true |  | Boolean | true, false | Whether the sink fixture is low flow. |
| `water_fixtures_usage_multiplier` | false |  | Double | auto | Multiplier on the hot water usage that can reflect, e.g., high/low usage occupants. |

The ResStock argument definitions set in the Hot Water Fixtures characteristic

</div>

#### Distribution Assumptions

- A log-normal distribution was shown to match the distribution of annual energy consumption.

- The data shows appoximately a log-normal distribution. From the data, the average multiplier is 0.8 and the standard deviation is 0.2. The average multiplier was mean-shifted from 0.8 to 1 average usage.

- Low, Medium, and High usage is assigned based on the lower 25th percent, middle 50th percent, and upper 25th percent.

