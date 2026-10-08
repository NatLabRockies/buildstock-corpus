<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | assets/files/ComStock Measure Doc_HP RTU Higher Compressor Lockout.pdf | status: site_page | source_url: https://github.com/NatLabRockies/ComStock.github.io/blob/bacf551bc5d2f595d2b3c41a57de0beea23ec6be/assets/files/ComStock%20Measure%20Doc_HP%20RTU%20Higher%20Compressor%20Lockout.pdf | publication_url: https://natlabrockies.github.io/ComStock.github.io/assets/files/ComStock%20Measure%20Doc_HP%20RTU%20Higher%20Compressor%20Lockout.pdf | corpus_version: b5faf42 | corpus_path: upgrade_measures/unpublished_docs/upgrade_measures/ComStock Measure Doc_HP RTU Higher Compressor Lockout.md | section: 3.2.1  Reasoning for Selecting 32°F Compressor Lockout Temperature | lines: 206-266 -->
## 3.2.1  Reasoning for Selecting 32°F Compressor Lockout Temperature

Our previous work analyzing the HP-RTU with standard performance used the setting of 0°F compressor lockout temperature following the common specifications of prevalent products in the current market. This means if the outdoor air temperature falls below the compressor lockout temperature, the heat pump is disabled and supplemental heating is exclusively used to address the entire heating load. However, based on our review of product documentation and informal discussion with manufacturer representatives, there are two scenarios that can happen. The first is when the product offers a range of temperature (with default setting) so that the actual product's lockout temperature can be set during the commissioning stage. Table 1 shows some of the actual descriptions of lockout temperature from manufacturer documentation [3], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13], [14]. As shown in Table 1, the available minimum and maximum lockout temperatures vary between products and the default setting also varies between 15 ° F and 35 ° F, which is range that can have a large impact on the performance of the heat pump system in some climates. The second scenario is when there is no setting for the lockout temperature, but the controller shuts off the compressor based on the suction pressure level. This lockout occurs on low pressure, and its purpose is to maintain compressor reliability. The specific description of this reliability feature (i.e., low pressure switch) is also available in manufacturer publications [3], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13], [14]. Note: While most of the manufacturer's documentation clearly indicated whether the specific lockout temperature was intended for locking the mechanical heating (and using a temperature delta to set the cooling lockout), the documentation from Carrier was not clear enough. We made our best judgment to interpret the values in the table as the lockout for the mechanical heating operation. PRE-PUBLICATION

Table 1. Descriptions of Compressor Lockout Temperature in Manufacturer Manuals [3], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13], [14]

<!-- table recovered from assets/files/ComStock Measure Doc_HP RTU Higher Compressor Lockout.pdf p.15
     overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/assets/files/ComStock Measure Doc_HP RTU Higher Compressor Lockout.yaml
     method: vision-transcription -->

**Carrier**

| Brand from data | Model name | Keywords | Lockout description in actual manuals |
|---|---|---|---|
| Carrier | WeatherMaker 50FCQ | EcoBlue | adjustable from -45°F (-43°C) to 80°F (27°C), set at a factory default of 32°F (0°C). |
| Carrier | WeatherMaster 50GCQ | EcoBlue | adjustable from -45°F (-43°C) to 80°F (27°C), set at a factory default of 32°F (0°C). |
| Carrier | WeatherMaker 50TCQ | Std efficiency | adjustable from -45°F to 80°F (-43°C to 27°C), set at a factory default of 32°F (0°C). |
| Carrier | WeatherMaster 50HCQ | High efficiency | adjustable from -45°F (-43°C) to 80°F (27°C), set at a factory default of 32°F (0°C). |

**Lennox**

| Brand from data | Model name | Keywords | Lockout description in actual manuals |
|---|---|---|---|
| Lennox | Enlight | High efficiency | min = -50F, default = -15F, max = 0F. This parameter controls when heat pump operation will be locked-out. If mechanical heating is already active and OAT drops to or below this setpoint, mechanical heating will be stopped. |
| Lennox | Xion | Std efficiency | N/A |

**Trane**

| Brand from data | Model name | Keywords | Lockout description in actual manuals |
|---|---|---|---|
| Trane | Impack | 2-5 tons | N/A |
| Trane | Precedent | 3-25 tons | The factory default setpoint is 0°F, but is user adjustable between -18 and 45°F. |

**Rheem**

| Brand from data | Model name | Keywords | Lockout description in actual manuals |
|---|---|---|---|
| Rheem | Resolute line classic | Std efficiency | Compressor lockout sensor on the unit controller is factory set at 35°F and is adjustable from 30°F (-1°C) to 50°F (10°C) and resets the cooling lockout at 5°F (+2.7°C) above the set point. |
| Rheem | Renaissance line classic | High efficiency | N/A |
| Rheem | Endeavor line classic | 2-5 tons | N/A |
| Rheem | Commercial classic | - | Compressor lockout sensor on the unit controller is factory set at 35°F and is adjustable from 30°F (-1°C) to 50°F (10°C) and resets the cooling lockout at 5°F (+2.7°C) above the set point. |

**Daikin**

| Brand from data | Model name | Keywords | Lockout description in actual manuals |
|---|---|---|---|
| Daikin | Rebel | High efficiency | Default 0°F and range -20°F-50°F. 45°F if 100% OA unit w/o ER and range 45°F-50°F. |
| Daikin | Maverick | Std efficiency |  |

**YORK**

| Brand from data | Model name | Keywords | Lockout description in actual manuals |
|---|---|---|---|
| YORK | Sun Core | 3-10 tons | N/A based on compressor suction pressure |
| YORK | Sun Pro | 6.5-12.5 tons | N/A |
| YORK | Sunline | 15-20 tons | N/A |

Emphasis in the source, which a pipe table cannot carry: the lockout value taken from each manual is printed in bold red - "32°F (0°C)" in all four Carrier rows, "-15F" for the Lennox Enlight, "0°F" for the Trane Precedent, "35°F" for both Rheem rows, and "0°F" for the Daikin Rebel.

Additionally, based on the feedback from the NREL reviewers of this report, the stock-level impact of HP-RTUs with a 0°F compressor lockout temperature (i.e., HP-RTUs with 0°F lockout temperature applied to 34% of the total stock floor area) may be too ideal because the minimum lockout temperature in the field may be higher, forcing heat pumps to switch to supplemental heating at higher outdoor air temperatures. Because there is uncertainty in how the lockout temperature will be set during equipment commissioning, we want to understand the implications of modification on the building stock. However, it is also unclear if there is a reasonable lockout temperature we can apply to heat pumps modeled across different sizes of buildings and under different climates. Thus, this analysis includes the impact of different lockout temperatures (i.e., 0°F, 5°F, 10°F, 17°F, and 32°F) on reduced stock models to provide a context around sensitivity and also provides the full stock modeling results (via data release) by selecting one of the temperatures (i.e., 32°F). Because we already published a dataset with 0°F lockout temperature, the data released in this analysis will be a comparable dataset to the previous dataset. PRE-PUBLICATION

