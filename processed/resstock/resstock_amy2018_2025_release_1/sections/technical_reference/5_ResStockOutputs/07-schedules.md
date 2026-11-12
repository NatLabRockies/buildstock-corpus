<!-- resstock resstock_amy2018_2025_release_1 | technical_reference | docs/technical_reference_guide/5_ResStockOutputs.tex | status: site_page | source_url: https://github.com/NatLabRockies/resstock/blob/3888e2ff0a4764eb57de65ad0d103870330eb542/docs/technical_reference_guide/5_ResStockOutputs.tex | publication_url: https://natlabrockies.github.io/ResStock.github.io/assets/trd/ResStockTechnicalReferenceGuide_2025_1.pdf | corpus_version: resstock_amy2018_2025_release_1-v1 | corpus_path: technical_reference/docs/technical_reference_guide/5_ResStockOutputs.md | section: Schedules | lines: 396-425 -->
## Schedules

ResStock optionally outputs schedules into the timeseries files. These schedules include energy use schedules as fractions (0-1) and unavailable period schedules from HVAC, power outage, and vacancy periods.

<div id="tab:schedule_outputs" data-source="5_ResStockOutputs.tex">

| **Field Name** | **Units** | **Field Description** |
|:---|:---|:---|
| out.schedules_ceiling_fan | frac | Ceiling fan energy use schedule. |
| out.schedules_clothes_dryer | frac | Clothes dryer energy use schedule. |
| out.schedules_clothes_washer | frac | Clothes washer energy use schedule. |
| out.schedules_cooking_range | frac | Cooking range and oven energy use schedule. |
| out.schedules_dishwasher | frac | Dishwasher energy use schedule. |
| out.schedules_hot_water_clothes_washer | frac | Clothes washer hot water use schedule. |
| out.schedules_hot_water_dishwasher | frac | Dishwasher hot water use schedule. |
| out.schedules_hot_water_fixtures | frac | Fixtures (sinks, showers, baths) hot water use schedule. |
| out.schedules_lighting_garage | frac | Garage lighting energy use schedule. |
| out.schedules_lighting_interior | frac | Interior lighting energy use schedule. |
| out.schedules_no_space_cooling | 0,1 | Cooling unavailable period. |
| out.schedules_no_space_heating | 0,1 | Heating unavailable period. |
| out.schedules_occupants | frac | Occupant heat gain schedule. |
| out.schedules_plug_loads_other | frac | Other plug load energy use schedule. |
| out.schedules_plug_loads_tv | frac | Television plug load energy use schedule. |
| out.schedules_power_outage | 0,1 | Power outage unavailable period. |
| out.schedules_vacancy | 0,1 | Vacancy unavailable period. |

ResStock schedule output field names, units, and descriptions

</div>

