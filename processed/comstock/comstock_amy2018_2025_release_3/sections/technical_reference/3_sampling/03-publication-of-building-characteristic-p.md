<!-- comstock comstock_amy2018_2025_release_3 | technical_reference | documentation/reference_doc/3_sampling.tex | status: site_page | source_url: https://github.com/NatLabRockies/ComStock/blob/b77c60d341c9b68c58c5d51e51b06f08f293d3cb/documentation/reference_doc/3_sampling.tex | publication_url: https://natlabrockies.github.io/ComStock.github.io/assets/files/comstock_reference_documentation_2025_3.pdf | corpus_version: 0a2f61f | corpus_path: technical_reference/documentation/reference_doc/3_sampling.md | section: Publication of Building Characteristic Probability Distributions | lines: 285-371 -->
## Publication of Building Characteristic Probability Distributions

Some of the distributions described above cannot be published for contractual agreement reasons, but certain distributions can be published. The ComStock team has generated tab-separated values (tsv) files containing probabilities and dependencies. See Table “Building Characteristic Distributions Included in the ComStock Sampling Process, Including Probabilistic Dependencies and Descriptions” for the full list of building characteristic probability distributions. More detail on each building characteristic is provided later in this report.

| **Building Characteristic** | **Description** | **Data Source** | **Conditional On** |
|:---|:---|:---|:---|
| Simulation Year | Year used in simulations |  |  |
| Climate Zone | Climate zone as defined by American Society of Heating, Refrigerating and Air-Conditioning Engineers (ASHRAE) Standard 169-2006 | CoStar |  |
| County | County FIPS code (includes state specification) | CoStar | Climate Zone |
| State | State FIPS code | CoStar | County |
| Building Type | Primary building type of model | CoStar | County |
| Building Rentable Area | Building total floor area | CoStar | County, Building Type |
| Census Region | Census region | CoStar | State |
| Year of Construction | Year in which the building was constructed | CoStar | County, Building Type, Simulation Year |
| Year of Construction Bin | Year bin in which the building was constructed | CPUC DEER EULs | Year of Construction |
| Energy Code in Force When Constructed | Energy code applicable to building when constructed | State Code Adoption History | State, Year of Construction Bin |
| Building Subtype | If applicable, subtype of primary building type | NREL analysis of strip malls | Building Type |
| Ownership Status | Ownership and occupant status of the building | CBECS 2012 | Building Type |
| Party Responsible for Purchase Authority | Entity responsible for purchasing decisions | CBECS 2012 | Ownership Status |
| Party Responsible for Operation | Entity responsible for operation of the building | CBECS 2012 | Ownership Status |
| Number of Stories | Number of stories above grade | CoStar | County, Building Type |
| Window-to-Wall Ratio | Window-to-wall ratio | NFRC Commercial Fenestration Market Study | Building Type, Building Rentable Area, Energy Code in Force When Constructed |
| Building Shape | Building shape designation | CBECS 2012 | Building Type |
| Aspect Ratio | Aspect ratio of building | CBECS 2012 | Building Shape |
| Building Rotation | Rotation of building relative to North | CBECS 2012 |  |
| Space Heating Fuel | Principal heating fuel for the building | CBECS 2012 Plus ResStock Residential Heating Fuel by County | Building Type, County |
| Water Heating Fuel | Heating fuel for service water heating | CBECS 2012  | Space Heating Fuel, Building Type |
| HVAC System Type | Primary building HVAC system type | CBECS | Building Type, Space Heating Fuel, Census Region |
| HVAC Nighttime Variability | HVAC nighttime ventilation operation | NREL end-use data analysis | HVAC System Type, Building Type |
| Weekday Operation Start Time | Building weekday operation start time | NREL/Lawrence Berkeley National Laboratory (LBNL) AMI analysis | Building Type |
| Weekend Operation Start Time | Building weekend operation start time | NREL/LBNL AMI analysis | Building Type |
| Weekday Operational Duration | Building weekday operation duration | NREL/LBNL AMI analysis | Building Type, Weekday Operation Start Time |
| Weekend Operational Duration | Building weekend operation duration | NREL/LBNL AMI analysis | Building Type, Weekend Operation Start Time |
| Thermostat Set point for Heating | Heating set point during occupied hours | NREL Tstat data analysis | Building Type |
| Thermostat Setback for Heating | Heating setback during unoccupied hours | NREL Tstat data analysis | Building Type |
| Thermostat Set point for Cooling | Cooling set point during occupied hours | NREL Tstat data analysis | Building Type |
| Thermostat Setback for Cooling | Cooling setback during unoccupied hours | NREL Tstat data analysis | Building Type |
| Wall Construction Type | Building wall construction type | LightBox | Climate Zone, Number of Stories |
| Lighting Technology Size Bin | Building size classification for lighting technology type |  | Building Rentable Area |
| Plug Load Base-to-Peak Ratio type | Methodology for variability of plug load amplitude | NREL end-use data analysis | Building Type |
| Plug Load Weekday Base-to-Peak Ratio | Ratio between nominal and maximum weekday plug Load levels | NREL end-use data analysis | Building Type, Plug Load Base-to-Peak Ratio Type |
| Plug Load Weekend Base-to-Peak Ratio | Ratio between nominal and maximum weekend plug Load levels | NREL end-use data analysis | Building Type, Plug Load Base-to-Peak Ratio Type |
| Lighting Base-to-Peak Ratio Type | Methodology for variability of lighting load amplitude | NREL end-use data analysis | Building Type |
| Lighting Weekday Base-to-Peak Ratio | Ratio between nominal and maximum weekday lighting load levels | NREL end-use data analysis | Building Type, Lighting Base-to-Peak Ratio Type |
| Lighting Weekend Base-to-Peak Ratio | Ratio between nominal and maximum weekend lighting load levels | NREL end-use data analysis | Building Type, lighting Base-to-Peak Ratio Type |
| Code Compliance for Building Construction | Building energy code compliance when first constructed | Assumption | State |
| Code Compliance for Interior Lighting | Building energy code compliance for latest interior lighting replacement | Assumption | State |
| Code Compliance for Walls | Building energy code compliance for latest walls replacement | Assumption | State |
| Code Compliance for Service Water Heating | Building energy code compliance for latest service water heating replacement | Assumption | State |
| Code Compliance for Roof | Building energy code compliance for latest roof replacement | Assumption | State |
| Code Compliance for Exterior Lighting | Building energy code compliance for latest exterior lighting replacement | Assumption | State |
| Code Compliance for Interior Equipment | Building energy code compliance for latest interior equipment replacement | Assumption | State |
| Code Compliance for Windows | Building energy code compliance for latest window replacement | Assumption | State |
| Code Compliance for HVAC | Building energy code compliance for latest HVAC replacement | Assumption | State |
| Last Replacement Year for Interior Lighting | Year of most recent replacement of the interior lighting system | CPUC DEER EULs | Simulation Year, Year of Construction |
| Last Replacement Year for HVAC | Year of most recent replacement of the HVAC system | CPUC DEER EULs | Simulation Year, Year of Construction |
| Last Replacement Year for Service Water Heating | Year of most recent replacement of the service water heating system | CPUC DEER EULs | Simulation Year, Year of Construction |
| Last Replacement Year for Walls | Year of most recent replacement of the wall | CPUC DEER EULs | Simulation Year, Year of Construction |
| Last Replacement Year for Windows | Year of most recent replacement of the windows | CPUC DEER EULs | Simulation Year, Year of Construction |
| Last Replacement Year for Roof | Year of most recent replacement of the roof | CPUC DEER EULs | Simulation Year, Year of Construction |
| Last Replacement Year for Exterior Lighting | Year of most recent replacement of the exterior lighting system | CPUC DEER EULs | Simulation Year, Year of Construction |
| Last Replacement year for Interior Equipment | Year of most recent replacement of the interior equipment system | CPUC DEER EULs | Simulation Year, Year of Construction |
| Code in Force for Replacement of Interior Lighting | Energy code in force at time of last interior lighting renovation | State Code Adoption History | State, Last Replacement Year for Interior Lighting |
| Code in Force for Replacement of Windows | Energy code in force at time of last window renovation | State Code Adoption History | State, Last Replacement Year for Windows |
| Code in Force for Replacement of Roof | Energy code in force at time of last roof renovation | State Code Adoption History | State, Last Replacement Year for Roof |
| Code in Force for Replacement of HVAC | Energy code in force at time of last HVAC renovation | State Code Adoption History | State, Last Replacement Year for HVAC |
| Code in Force for Replacement of Walls | Energy code in force at time of last walls renovation | State Code Adoption History | State, Last Replacement Year for Walls |
| Code in Force for Replacement of Service Water Heating | Energy code in force at time of last service water heating renovation | State Code Adoption History | State, Last Replacement Year for Service Water Heating |
| Code in Force for Replacement of Interior Equipment | Energy code in force at time of last interior equipment renovation | State Code Adoption History | State, Last Replacement year for Interior Equipment |
| Code in Force for Replacement of Exterior Lighting | Energy code in force at time of last exterior lighting renovation | State Code Adoption History | State, Last Replacement Year for Exterior Lighting |
| Energy Code Followed for Building Construction | Energy code followed when building was constructed | State Code Adoption History Plus Year Built and Turnover | Energy Code in Force when Constructed, Code Compliance for Building Construction |
| Energy Code Followed for Replacement of Interior Lighting | Energy code followed when current interior lighting system installed | State Code Adoption History Plus Year Built and Turnover | Code in Force for Replacement of Interior Lighting, Code Compliance for Interior Lighting |
| Energy Code Followed for Replacement of Service Water Heating | Energy code followed when current service water heating system installed | State Code Adoption History Plus Year Built and Turnover | Code in Force for Replacement of Service Water Heating, Code Compliance for Service Water Heating |
| Energy Code Followed for Replacement of Windows | Energy code followed when current windows were installed | State Code Adoption History Plus Year Built and Turnover | Code in Force for Replacement of Windows, Code Compliance for Windows |
| Energy Code Followed for Replacement of Roof | Energy code followed when current roof was installed | State Code Adoption History Plus Year Built and Turnover | Code in Force for Replacement of Roof, Code Compliance for Roof |
| Energy Code Followed for Replacement of Interior Equipment | Energy code followed when current interior equipment installed | State Code Adoption History Plus Year Built and Turnover | Code in Force for Replacement of Interior Equipment, Code Compliance for Interior Equipment |
| Energy Code Followed for Replacement of HVAC | Energy code followed when current HVAC system installed | State Code Adoption History Plus Year Built and Turnover | Code in Force for Replacement of HVAC, Code Compliance for HVAC |
| Energy Code Followed for Replacement of Walls | Energy code followed when current walls were installed | State Code Adoption History Plus Year Built and Turnover | Code in Force for Replacement of Walls, Code Compliance for Walls |
| Energy Code Followed for Replacement of Exterior Lighting | Energy code followed when current exterior lighting system installed | State Code Adoption History Plus Year Built and Turnover | Code in Force for Replacement of Exterior Lighting, Code Compliance for Exterior Lighting |
| Lighting Technology Generation | Generation of lighting technology used in building | Lighting Market Characterization | Code in Force for Replacement of Interior Lighting, Last Replacement Year for Interior Lighting |
| Window Technology Type | Window technology type used in the building | NFRC Commercial Fenestration Market Study | Energy Code Followed for Replacement of Windows, Climate Zone |
| Economizer Drybulb Limit Fault | Presence of economizer drybulb limit control fault | Studies of HVAC equipment fault prevalence | HVAC System Type, Energy code followed when current HVAC system installed, Climate Zone |
| Economizer Damper Stuck Fault | Presence of economizer damper stuck fault | Studies of HVAC equipment fault prevalence | HVAC System Type |
| Includes Refrigeration | Presence of commercial refrigeration including walk-in coolers or refrigerated display cases | Assumption | Building Type |
| Refrigeration Technology Level | Efficiency level of the commercial refrigeration equipment | Historical DOE shipment reports for commercial refrigeration equipment | Includes Refrigeration, Last Replacement Year for Refrigeration, Size Bin |
| Last Replacement Year for Refrigeration | Year of most recent replacement of the refrigeration equipment | DOE EULs | Year of Construction, Size Bin, Simulation Year |

