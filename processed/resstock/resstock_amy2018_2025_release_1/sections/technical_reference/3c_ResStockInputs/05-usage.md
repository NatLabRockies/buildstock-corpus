<!-- resstock resstock_amy2018_2025_release_1 | technical_reference | docs/technical_reference_guide/3c_ResStockInputs.tex | status: site_page | source_url: https://github.com/NatLabRockies/resstock/blob/3888e2ff0a4764eb57de65ad0d103870330eb542/docs/technical_reference_guide/3c_ResStockInputs.tex | publication_url: https://natlabrockies.github.io/ResStock.github.io/assets/trd/ResStockTechnicalReferenceGuide_2025_1.pdf | corpus_version: resstock_amy2018_2025_release_1-v1-pre | corpus_path: technical_reference/docs/technical_reference_guide/3c_ResStockInputs.md | section: Usage | lines: 523-552 -->
## Usage

### Modeling Approach

ResStock models the diversity of appliance usage in a couple of ways. The first way is through scaling the energy by usage multipliers. There are three usage levels—low, medium, and high—which are used to assign usage multipliers. The characteristics that use appliance-specific usage multipliers are clothes dryer, clothes washer, cooking range, dishwasher, hot water fixtures, plug load diversity, refrigerator, misc extra refrigerator, and misc freezer. See each of these subsections for the specific multipliers used to diversify their energy consumption.

The second way is through the number and timing of appliance events throughout the year, which is dealt with in the stochastic schedule generator. See Section “Schedule Creation” for more information about when and how long the events occur for different schedules.

### Usage Level

#### Description

Usage of major appliances relative to the national average.

#### Distribution Data Source(s)

Engineering judgment and calibration.

#### Direct Conditional Dependencies

None.

#### Options

The options are low, medium, and high. The distribution values are 25% for low, 50% for medium, and 25% for high. These options do not assign ResStock arguments.

#### Distribution Assumption(s)

None.

