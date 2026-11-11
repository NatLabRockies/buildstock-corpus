<!-- resstock resstock_amy2018_2025_release_1 | github_site | docs/resources/explanations/Unmet_load_hours.md | status: site_page | source_url: https://github.com/NatLabRockies/ResStock.github.io/blob/696c020d696137830ddae75abbfb477ae7af8eaa/docs/resources/explanations/Unmet_load_hours.md | publication_url: https://natlabrockies.github.io/ResStock.github.io/docs/resources/explanations/Unmet_load_hours.html | corpus_version: resstock_amy2018_2025_release_1-v1-pre -->
# Unmet Load Hours

## Unmet Load Hours

### Overview
Unmet load hours in EnergyPlus represent the number of hours during which a thermal zone's operative temperature falls outside the desired heating or cooling setpoint range. **This metric is used to evaluate HVAC performance, particularly in sizing and control diagnostics, and is reported in compliance simulations or quality assurance checks. This metric is not related to thermal comfort, and should not be used for thermal comfort analysis.**

EnergyPlus typically counts unmet load hours at the zone timestep level, comparing zone temperatures against defined setpoint schedules with a default tolerance band of ±0.2°C (±0.36°F). Information on annual unmet load hours from an OS_HPXML standpoint can be found [here](https://openstudio-hpxml.readthedocs.io/en/latest/workflow_outputs.html#annual-unmet-hours). This applies to output columns titled out.unmet_hours.heating.hour and out.unmet_hours.cooling.hour .

### Assumptions behind unmet load hours
The unmet load hours calculation in EnergyPlus is based on several simplifying assumptions. It uses a strict temperature band around setpoints, less than half a degree,  which may not align with real-world thermal comfort expectations or adaptive comfort models. Unmet load hours are also sensitive to timestep resolution—short spikes in temperature deviations may be missed or overemphasized depending on timestep length. The metric assumes accurate HVAC schedules, control strategies, and zone temperature sensing, but doesn't always account for occupancy or whether HVAC systems are actively running. Complex system interactions, such as shared equipment across zones or floating setpoints, may yield misleading results. Known issues in past versions of EnergyPlus have included improper counting of unmet hours during system-off periods or rounding errors at timestep boundaries.

### Recommended use cases
Unmet load hours are most useful during HVAC system sizing, initial design reviews, and performance diagnostics where temperature control issues are suspected. Unmet load hours in a multizone building energy model simulation can help flag zones that are underserved by heating or cooling capacity, or zones affected by poor control strategies. However, ResStock is a single zone model, meaning all of the dwelling unit is assumed to be one zone, so using unmet load hours to flag zones that are underserved is not a suitable use case in ResStock.

### When to look closely at the results
In ResStock, unmet load hour results should be carefully reviewed when they occur during times when the HVAC system is expected to be off or in dwelling units that have zero or partial conditioning.

This includes periods like night setbacks, vacancy, or when ResStock simulates a broken HVAC system. Unmet load hours should also be scrutinized during low-load conditions, where temperature deviations may not noticeably impact comfort. High unmet load hours can sometimes occur due to unrealistic thermostat settings, such as fixed setpoints that don’t reflect actual occupant behavior, or from large setbacks that delay recovery. Because residential systems often use single-zone control, unmet load hours may reflect small temperature deviations rather than true comfort problems. Reviewing zone temperature trends, occupancy assumptions, and HVAC operation schedules is key to determining whether unmet hours indicate a real issue or just a modeling artifact.

For partially conditioned dwelling units, for example a multifamily apartment that has room air conditioning, the partial air conditioning is sized to meet only a part of the cooling load. If an apartment is 40% conditioned, then the air conditioning must only cool 40% of the apartment, or 40% of the total cooling load. In this scenario, the unmet load hours metric only covers when the partially conditioned zone's operative temperature falls outside the desired heating or cooling setpoint range. It does not evaluate the 60% of the apartment that is not conditioned.

Unmet load hours is ultimately a HVAC performance metric in ResStock, not a thermal comfort metric.
