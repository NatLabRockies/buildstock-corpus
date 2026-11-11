<!-- resstock resstock_amy2018_2025_release_1 | upgrade_measures | measure_pdfs/95034.pdf | status: osti_pdf | source_url: https://docs.nlr.gov/docs/fy26osti/95034.pdf | publication_url: https://docs.nlr.gov/docs/fy26osti/95034.pdf | corpus_version: resstock_amy2018_2025_release_1-v1-pre | corpus_path: upgrade_measures/measure_pdfs/95034.md | section: 2.2.3  EnergyPlus Energy Management System Correction to Pump Power | lines: 676-697 -->
## 2.2.3  EnergyPlus Energy Management System Correction to Pump Power

The EnergyPlus models with the variable-speed water-to-air coil object for two-stage and variable-speed water-to-air GHP systems did not by default model the expected behavior of the pump for these GHP systems. To modify the default behavior to try to more accurately model the pump behavior, especially in cases where the GHP is in part-load conditions, a custom energy management system (EMS) script was developed and added to the OpenStudio-HPXML workflow. EMS is a custom scripting language packaged with EnergyPlus that allows users to write short custom programs to modify the behavior of certain components of the model. In addition to developing the standard EnergyPlus GHP models, an EMS program was developed to overcome the limitations in current EnergyPlus capabilities to model the two-stage water-to-air GHP systems:

1. There is an improper limit on the node water flow rate found in EnergyPlus. This limit will cause the pump water flow rates to be capped at the first-stage nominal flow rate, and the remaining water flow is bypassed. It will likely cause warnings/errors complaining about unrealistic water temperatures due to the reduced water flow rates, which largely impacts the accuracy and stability of simulation. This limitation was fixed by the ResStock team and will be included in future EnergyPlus releases from 25.1.0 onward. See the merged EnergyPlus pull request 3 for the full details of this change.
2. EnergyPlus models a constant water mass flow rate equal to the first-stage flow rate during part-load conditions, where the heat pump may only be running for part of the time step, and the average flow rate over the time step may be less than the minimum even with a two-stage pump. This affects the pump energy calculation, which is fixed by the EMS program described below. In addition, an EnergyPlus issue 4 was created to

[3  https://github.com/NatLabRockies/EnergyPlus/pull/11005](https://github.com/NatLabRockies/EnergyPlus/pull/11005)

[4  https://github.com/NatLabRockies/EnergyPlus/issues/10936](https://github.com/NatLabRockies/EnergyPlus/issues/10936)

report this defect to the development team. Ideally the defect will be fixed in the future version of EnergyPlus, and then the EMS workaround can be eliminated or simplified.

In this case, an EMS program is used to recalculate the pump power in every time step. It involves two steps:

1. Calculate the correct pump power if part-load conditions exist. The internal EnergyPlus pump energy calculations do not handle the pump part-load ratio correctly in the use case. The pump part-load ratio at each time step is recalculated in the EMS program based on pump volume flow rates and heat pump coil speed levels/ratios. The part-load ratio is assumed to be equal to the fraction of pump full-load power.
2. Apply the calculated fraction to calculate and override the pump power consumption at each time step.

Even though EMS programs offer flexibility for users to override some aspects of EnergyPlus simulation and achieve the desired energy results, there are still some limitations to using EMS programs. The EMS program described above is included in OpenStudio-HPXML, but other EnergyPlus modelers would not have easy access to it and may not know about the limitations requiring its use. EMS also adds complexity to the models, may impact simulation runtime, and may cause one-time-step lag on reporting the energy consumption of components controlled via EMS. Therefore, if the EnergyPlus issue being reported can be fixed in the future versions, it will largely simplify the workflow and benefit more users of these EnergyPlus objects.

Combining all the efforts above, OpenStudio-HPXML is capable of modeling the desired pump operation and giving satisfying pump energy results for two-stage GHP systems.

