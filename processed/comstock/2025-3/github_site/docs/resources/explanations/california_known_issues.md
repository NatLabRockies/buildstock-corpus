<!-- comstock 2025-3 | github_site | docs/resources/explanations/california_known_issues.md -->
# California Model Known Issues

# California Models Known Issues

## Underrepresentation of HVAC energy in California warehouse models

A known issue in **ComStock 2025 Release 1 and earlier datasets** affects the representation of warehouse buildings in California. Although the metadata for these models may indicate the presence of HVAC systems, all California warehouse models are effectively unconditioned. This discrepancy arises from the underlying DEER warehouse prototypes used in the modeling process, which do not include conditioned space types. Since the ComStock modeling workflow only applies HVAC systems to conditioned space types within warehouses such as an office space, and not to general unconditioned warehouse areas, no HVAC systems are ultimately assigned to these models.

This limitation leads to an underrepresentation of energy use for heating, cooling, and ventilation in California warehouse models, affecting the energy, emissions, and utility bills included in ComStock datasets. The issue has been identified and is scheduled to be resolved in a future ComStock dataset release, which will revise the modeling approach to more accurately reflect conditioned spaces within California warehouses.

## Likely overestimation of equipment power densities in California models

**In ComStock 2024 Release 2 and earlier**, the equipment power densities in models in CA are higher than those in the same building types in the rest of the country. Roughly, mercantile building types are 150-200%, food service buildings are 100-200%, and education buildings are 200-300% of the equipment power densities in the rest of the country. Warehouse equipment is much lower, around 0.33%. This is a result of using the equipment power densities from the circa 2017 DEER prototype models. While we do not have definitive evidence to show that these values are incorrect, we do observe that the HVAC end use intensities (EUIs), particularly for cooling, are higher than CBECS and higher than the rest of the country on an area-weighted cooling degree day basis. This overestimate likely overstates the relative importance of energy consumption, associated savings potential, and emissions associated with interior equipment in California. As part of a planned change, releases of ComStock starting in mid/late 2025 will use the same equipment power density assumptions as the rest of the country instead of the values from DEER.

## Overestimation of ventilation in California models

**In ComStock 2023 Release 2 and earlier**, for models in California, the modeled outdoor air ventilation rate was significantly above that required by Title 24. Title 24 specifies minimum ventilation rates on a per-area and per-occupant basis, with the instruction to take the higher of the two. ComStock erroneously modeled this as the sum of the two, leading to unrealistically high ventilation. This is most noticeable when plotting HVAC heating or cooling EUIs vs. heating or cooling degree days; the models in CA show a trend of heating/cooling EUIs roughly twice as high as the rest of the country. **This doubling of ventilation was corrected before ComStock 2024 release 1.**
