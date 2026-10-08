<!-- comstock comstock_amy2018_2025_release_3 | technical_reference | documentation/reference_doc/4_9_hvac.tex | status: site_page | source_url: https://github.com/NatLabRockies/ComStock/blob/b77c60d341c9b68c58c5d51e51b06f08f293d3cb/documentation/reference_doc/4_9_hvac.tex | publication_url: https://natlabrockies.github.io/ComStock.github.io/assets/files/comstock_reference_documentation_2025_3.pdf | corpus_version: b5faf42 | corpus_path: technical_reference/documentation/reference_doc/4_9_hvac.md | section: Thermostat Set Points | lines: 397-488 -->
## Thermostat Set Points

Thermostat set points, both heating and cooling, dictate the target indoor temperature range for the HVAC system to satisfy. The cooling thermostat set point will set the upper temperature limit, whereas the heating thermostat set point will set the lower temperature limit.

Thermostat set points are implemented in ComStock through square-wave schedules. Each model is assigned a set point temperature, which is the temperature the HVAC system must maintain during occupied hours, and a setback temperature, which is the temperature the HVAC system must maintain during unoccupied hours (note that some models have no setback temperature). The set point and setback temperatures used in the models are described later in this section. The timing of the set point and setback temperatures align with the building occupancy schedules discussed in Section “Hours of Operation and Occupancy”.

### Thermostat Set Points Informed by Building Automation System Data

This section outlines the ComStock thermostat set point assignment methodology for the following building types: full service restaurant, large office, medium office, primary school, quick service restaurant, retail standalone, retail strip mall, secondary school, and small office.

All ComStock building types, excluding hospitals, outpatient, warehouses, and hotels, utilize building automation system (BAS) data to inform distributions of thermostat set points. The methodology behind this approach is described in this section. The intent is to include heating and cooling thermostat set point variability between ComStock models to reflect the thermostat set point variability between real buildings. For example, some offices could be expected to set their heating thermostat to 72°F, whereas others might set it to 70°F. The ComStock methodology allows this variation to exist in the models.

Building automation data from three industry-provided private data sources with over 3,700 buildings were used to derive the distributions of thermostat set points that are used to assign set points to the applicable ComStock models. Table “Building Counts With Thermostat Data by Building Type” shows the counts of buildings with thermostat data available in the data set by building type. The data set includes the time series heating and cooling set points that were used to determine the occupied heating and cooling set points for each building. In turn, these were used to create probability distributions of thermostat set points by building type when aggregating across the data set. For building types with less than 25 samples in the data set, the distribution for all building types was used, as smaller sample sizes cannot reliably be extrapolated to represent a population. The resulting heating and cooling probability distributions, per applicable building type, are shown in Figure “Heating thermostat set point (Fahrenheit) distributions per building type.” and Figure “Cooling thermostat set point (Fahrenheit) distributions per building type.”, respectively. Note that some outliers exist in the data set at very low prevalence, such as offices with heating set points of 61°F. These outliers are incorporated into ComStock models at a similar low prevalence to reflect the wide diversity of commercial buildings.

<div id="tab:bas_thermostat_count_by_btype" data-source="tables/thermostat_bas_count.tex">

| **Building Type**       | **Building Count** |
|:------------------------|:-------------------|
| Food Service/Restaurant | 1,817              |
| Mercantile Retail       | 1,692              |
| Food Sales/Grocery      | 164                |
| Office                  | 31                 |
| School                  | 16                 |
| Warehouse               | 4                  |
| Hotel                   | 4                  |
| Hospital                | 2                  |
| Outpatient              | 2                  |

Building Counts With Thermostat Data by Building Type

</div>

<figure id="fig:htg_therm_setpoints">
<img src="figures/heating_setpoints.png" style="width:100.0%" />
<figcaption>Heating thermostat set point (Fahrenheit) distributions per building type.</figcaption>
</figure>

<figure id="fig:clg_therm_setpoints">
<img src="figures/cooling_setpoints.png" style="width:100.0%" />
<figcaption>Cooling thermostat set point (Fahrenheit) distributions per building type.</figcaption>
</figure>

### Unoccupied Thermostat Setbacks

An unoccupied thermostat setback defines the difference in the temperature set point from the occupied thermostat set point, for either heating or cooling, which is used during periods where the building is unoccupied. For example, an office might have an occupied heating set point of 71°F, but an unoccupied thermostat setback of 6°F for when the building is unoccupied, resulting in an unoccupied thermostat set point of 65°F (71°F - 6°F). This setback would be expected to save HVAC energy by relaxing the temperature requirements when there are no occupants in the building. This section describes ComStock’s methodology for assigning unoccupied thermostat setback prevalence, as well as the setback temperature delta, for both heating and cooling.

The prevalence of thermostat setbacks in ComStock models is determined by building type using CBECS 2012. Each building type has some fraction of buildings with a thermostat setback, and some fraction without. The CBECS survey does not provide details on thermostat set point and setback temperatures, but it does provide survey responses as to whether heating and cooling setbacks are used, and whether these setbacks are manual. The survey responses are summarized by building type in Figure “Percentage of buildings with thermostat setbacks by building type from the CBECS 2012 survey.”. However, it seems likely that many respondents who claim to implement manual setbacks do not reliably do so; we made a conservative assumption that only 20% of manual setbacks would be counted as reliably practicing thermostat setbacks (manually adjusting the thermostat every night before leaving and every morning upon entering). The fraction of ComStock models that include thermostat setbacks is shown in Table “Fraction of ComStock Buildings With Thermostat Setbacks by Building Type”. Note that the timing of the thermostat setbacks coincides with the assigned hours of operation for a specific model, the methodology for which is described in Section “Hours of Operation and Occupancy”.

<div id="tab:thermostat_setback_prev" data-source="tables/thermostat_setback_prev.tex">

| **Building Type**      | **Fraction of Models With Thermostat Setback** |
|:-----------------------|:-----------------------------------------------|
| FullServiceRestaurant  | 0.57                                           |
| Grocery                | 0.63                                           |
| LargeOffice            | 0.77                                           |
| MediumOffice           | 0.76                                           |
| PrimarySchool          | 0.9                                            |
| QuickServiceRestaurant | 0.46                                           |
| RetailStandalone       | 0.63                                           |
| RetailStripmall        | 0.9                                            |
| SecondarySchool        | 0.95                                           |
| SmallOffice            | 0.77                                           |
| Warehouse              | 0.56                                           |

Fraction of ComStock Buildings With Thermostat Setbacks by Building Type

</div>

### Unoccupied Thermostat Setbacks Informed by Building Automation System Data

The method for determining the magnitude of the temperature setback for buildings with unoccupied temperature setbacks is described in this section. This methodology is used for the following building types: full service restaurant, large office, medium office, primary school, quick service restaurant, retail standalone, retail strip mall, secondary school, small office, and warehouse. In warehouse buildings, this methodology only applies to the office space type within the building.

The magnitudes of the temperature setbacks are determined using the same data sets and methods described in Section “Thermostat Set Points Informed by Building Automation System Data” for thermostat set points; probability distributions are created for each building type. The relationship between the thermostat set points and the delta setbacks is shown in Figure “Thermostat heating and cooling set point-setback delta correlation from BAS data sources; all building types.”. The resulting heating and cooling thermostat delta setback temperature probability distributions, for each applicable building type, are shown in Figure “Thermostat heating setback delta temperature probability distributions per building type.” and Figure “Thermostat cooling setback delta temperature probability distributions per building type.”, respectively.

<figure id="fig:therm_heating_setback">
<img src="figures/heating_setbacks.png" style="width:100.0%" />
<figcaption>Thermostat heating setback delta temperature probability distributions per building type.</figcaption>
</figure>

<figure id="fig:therm_cooling_setback">
<img src="figures/cooling_setbacks.png" style="width:100.0%" />
<figcaption>Thermostat cooling setback delta temperature probability distributions per building type.</figcaption>
</figure>

### Thermostat Setpoints Not Informed by Building Automation System Data

The following ComStock building types do not infer thermostat setpoints from the BAS data, and therefore each have there own methodology previously described in this section: Hospitals, Outpatient, Warehouses, Small Hotels, and Large Hotels.

#### Warehouses

Heating thermostat setpoints for warehouse storage spaces are adjusted from the DOE/DEER prototype model defaults in order to better calibrate warehouse energy consumption to the CBECS truth data set, informed by CBECS 2018 (U.S. Energy Information Administration 2018a) responses to the “Percent Heated” and “Percent Cooled” questions as well as engineering judgement. The default DOE prototype setpoint value of 45°F (50°F for buildings built after 2004) was increased, and the default DEER prototype setpoint value of 70°F was decreased, both to a new heating setpoint of 61°F. Cooling thermostat setpoints remained unchanged, except for California (DEER prototype) warehousees, which are modeled as heated-only.

