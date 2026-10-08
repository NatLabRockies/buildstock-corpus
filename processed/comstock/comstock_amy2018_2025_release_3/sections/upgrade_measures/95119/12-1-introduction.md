<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/95119.pdf | status: osti_pdf | source_url: https://docs.nlr.gov/docs/fy25osti/95119.pdf | publication_url: https://docs.nlr.gov/docs/fy25osti/95119.pdf | corpus_version: fadc83e | corpus_path: upgrade_measures/measure_pdfs/95119.md | section: 1  Introduction | lines: 248-268 -->
## 1  Introduction

Packaged rooftop units (RTUs) are one of the most prominent HVAC system types in the United States, making them an impactful segment of the building stock for energy usage, energy bill costs, and electricity grid load shape. Most existing RTUs in the U.S. building stock use gasfired heating, with a lesser proportion using electric resistance heating (among other less common options).

Heat pumps offer a higher-performance electric option for commercial building space heating. They can deliver space heating 2-4 times more efficiently than electric resistance options. Based on the 2018 Commercial Buildings Energy Consumption Survey (CBECS) data estimates, fewer than 15% of commercial buildings utilize heat pumps for space heating equipment, and when they are in use, they are more commonly found in the warmer southern region of the United States [1].

This study investigates the mass replacement of existing gas-fired or electric-resistance RTUs

in the U.S commercial building stock with heat pump RTUs (HP-RTU). The ComStock public dataset already includes several similar iterations of this scenario, including:

- [Advanced performance variable-speed HP-RTUs [1]](https://docs.nrel.gov/docs/fy24osti/86585.pdf)
- [Advanced performance variable-speed HP-RTUs with supplemental heating matching the existing fuel type of the building [2]](https://docs.nrel.gov/docs/fy24osti/87570.pdf)
- [Advanced performance variable-speed HP-RTUs with exhaust air energy recovery [3]](https://docs.nrel.gov/docs/fy24osti/89481.pdf)
- [Standard performance HP-RTUs [4]](https://www.nrel.gov/docs/fy25osti/89042.pdf)

Like the existing ComStock measure scenario for 'Standard Performance' HP-RTUs, this study models commercially available off-the-shelf HP-RTUs with electric supplemental heating. However, this study leverages NREL laboratory testing data of a 7.5-ton HP-RTU to inform performance. Alternatively, the existing 'Standard Performance' ComStock measures in the ComStock public dataset use published data tables from multiple manufacturers and unit sizes. Therefore, this study serves as another option that improves our confidence in modeling the performance of HP-RTUs.

To date, there has been limited published laboratory testing data on the performance of HPRTUs. Air-source heat pump performance is more sensitive to key assumptions compared to gas or electric resistance coils. This is because they rely on ambient air to transfer heat, which can vary in temperature substantially during heating hours, impacting both heat pump efficiency and capacity. In contrast, gas and electric resistance systems generate heat directly, making their performance less dependent on external temperature variations and thus more predictable. The testing data used in this study adds confidence to our HP-RTU energy modeling, as we can confirm performance against real operational data.

There are several available options for standard performance HP-RTUs on the market. A more detailed review of these systems is provided in [4]. Generally, these systems include multiple staged compressors, a multispeed fan, and some form of a supplemental heating coil (electric or gas, sometimes hydronic). Defrosting of the outdoor coil is usually achieved using a reverse cycle operation. There is a compressor lockout that prevents the heat pump from operating when conditions are very cold; this can be a specific minimum temperature, often between 0°F and 32°F, or some condition in the refrigerant system (e.g., a suction pressure exceeding threshold).

