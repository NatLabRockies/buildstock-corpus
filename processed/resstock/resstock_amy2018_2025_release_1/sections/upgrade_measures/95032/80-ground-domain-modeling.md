<!-- resstock resstock_amy2018_2025_release_1 | upgrade_measures | measure_pdfs/95032.pdf | status: osti_pdf | source_url: https://docs.nlr.gov/docs/fy26osti/95032.pdf | publication_url: https://docs.nlr.gov/docs/fy26osti/95032.pdf | corpus_version: resstock_amy2018_2025_release_1-v1-pre | corpus_path: upgrade_measures/measure_pdfs/95032.md | section: Ground Domain Modeling | lines: 1333-1475 -->
## Ground Domain Modeling

Based on the cooling load calculated according to ACCA Manual J and ACCA Manual S, a length for the ground heat exchanger is calculated (ACCA 2016) (ACCA 2014). As the first step, the ground heat exchanger length per ton of required heating or cooling is calculated. This calculation uses the pipe, ground and grout R-value to calculate an overall R-value for the borehole:

Where:

𝑑𝑑 𝑝𝑝 , 𝑎𝑎

: the pipe outside diameter

𝑑𝑑 𝑝𝑝 , 𝑎𝑎

: the pipe inside diameter

𝑘𝑘 𝑝𝑝

: the pipe thermal conductivity

Where:

𝑥𝑥 𝑏𝑏

: borehole spacing (assumed to be constant at 20 feet)

𝑑𝑑 𝑏𝑏

: borehole diameter (assumed to be constant at 5 inches)

𝑘𝑘 𝑒𝑒𝑟𝑟

: ground conductivity

Where:

𝑘𝑘 𝑒𝑒𝑟𝑟

: grout conductivity

𝑑𝑑 𝑝𝑝 , 𝑎𝑎

: pipe outside diameter

𝛽𝛽0 and 𝛽𝛽1 are shape factor parameters, determined based on the U-tube spacing type as described in (Paul 1996) based on experimental data (Paul 1996). In OpenStudio-HPXML, values for 'a' (closely spaced), 'b' (moderately spaced), and 'c' (maximum spacing) spacing types are included, although by default the 'b' configuration is always assumed.

Figure B-1. Borehole spacing types. In OpenStudio-HPXML, the 'B' configuration is used by default.

![Image](95032_images/image_000044_309c78f8214ea20ad7f6b3a11be676b34cfc149b25920517f03386412e7539c4.png)

From (Spitler and Javed 2016) (J. D. Spitler 2016).

The overall borehole resistance is then calculated as:

Note that the convection resistance is neglected as testing has shown it has a negligible impact when compared to GLHEPro results (J. Spitler 2000). The nominal borehole lengths for heating and cooling are then calculated as:

Where:

h denotes heating and c denotes cooling

𝐸𝐸𝐸𝐸𝑅𝑅

: the nominal energy input ratio

𝑅𝑅𝑓𝑓𝐹𝐹

: the estimated run time fraction

𝑓𝑓 𝑠𝑠𝑎𝑎 , 𝑟𝑟𝑟𝑟𝑠𝑠

: the design cold water temperature into the heat pump (in °F)

: the design hot water temperature into the heat pump (in °F)

𝑓𝑓 ℎ𝑎𝑎 , 𝑟𝑟𝑟𝑟𝑠𝑠

∆𝑓𝑓 𝑟𝑟𝑟𝑟𝑠𝑠

: the design temperature difference (constant at 10°F)

𝑓𝑓 𝑟𝑟𝑏𝑏 , 𝑓𝑓𝑓𝑓𝑓𝑓 : the annual average temperature

The larger of the two lengths is then used to ensure that the ground heat exchanger is large enough for operation in both heating and cooling. The design cold and hot water temperatures are calculated as simple functions based on weather data:

Where:

𝑓𝑓 𝑟𝑟 , 𝑠𝑠

: the outdoor air temperature at design cooling conditions

𝑓𝑓 𝑟𝑟 , ℎ : the outdoor air temperature at design heating conditions

Note that while a 30% concentration of glycol is assumed by default for the fluid in the ground heat exchanger, a lower limit of 45°F will be applied if pure water is used instead to avoid any potential freeze issues. Runtime fractions are calculated as:

Where:

𝑓𝑓 𝑗𝑗𝑓𝑓𝑓𝑓

: average outdoor temperature in January

𝑓𝑓 𝑗𝑗𝐵𝐵𝑎𝑎

: average outdoor temperature in July

ℎ𝑡𝑡𝑑𝑑

: difference between the actual setpoint and heating design setpoint (71°F)

𝑐𝑐𝑡𝑡𝑑𝑑 : difference between the actual setpoint and cooling design setpoint (76°F)

The approach described above is essentially a normalized version of the Level 1 (a method using two pulses with a single heating and cooling season design period) methodology, with more detail on this methodology seen in Section 2.2.7. For example, the equation for the heating length used in Level 1 is:

This maps directly to what is implemented in OpenStudio-HPXML, with the following assumptions being made:

- The equation used in OpenStudio-HPXML is normalized by capacity.
- 𝑓𝑓 𝑒𝑒 is equal to the annual average outdoor air temperature.
- 𝑓𝑓 𝐿𝐿 is the average temperature of fluid in the heat exchanger during cooling.

This approach makes several simplifying assumptions in terms of the runtime fraction. The ground temperature has been updated in what is currently implemented in ResStock to use the undisturbed deep ground temperature during the design time of year rather than the annual average dry-bulb temperature.

The normalized values then get multiplied by the required equipment size to determine the total borehole length required. With the total length required, the number of boreholes can then be calculated. To calculate the number of boreholes required, an initial guess of one borehole for every ton of required capacity is used before some geometry parameters are enforced. Each borehole must have a minimum depth of 3 feet (0.15 times the borehole spacing, assumed to be 20 feet), so that the g-function values used later will be valid. A maximum depth of 345 feet is also assumed, based on the maximum depth before a mining permit is required in certain states. If necessary, these constraints will add or remove a borehole, up to a maximum of 10 boreholes. Based on the number of boreholes, the configuration of the bore field is then determined. The full list of valid ground heat exchanger configurations is given in Table B-1, with the default value denoted. Error checking is also in place to ensure that a g-function exists for the borehole configuration and number of boreholes calculated.

G-functions exist for spacing to depth ratios of &lt;0.02, 0.02-0.03, 0.03-0.05, 0.05-0.1, and &gt;0.1. All g-function values are for the same array of: 𝑙𝑙𝜋𝜋 ( 𝑡𝑡 / 𝑡𝑡 𝑠𝑠 ) : [-8.5, -7.8, -7.2, -6.5, -5.9, -5.2, -4.5, -3.963, -3.27, -2.864, -2.577, -2.171, -1.884, -1.191, -0.497, -0.274, -0.051, 0.196, 0.419, 0.642, 0.873, 1.112, 1.335, 1.679, 2.028, 2.275, 3.003].

Where:

𝑡𝑡 : time

𝑡𝑡 𝑠𝑠 : characteristic time of the ground heat exchanger For the g-functions, an existing table of values is used in the code. This table is likely based on GLHEPro runs, although there is some uncertainty on its source.

Table B-1. Prior Ground Heat Exchanger Configurations in OpenStudio-HPXML. The Current Configuration Used is Shown in Bold.

|   Number of Boreholes | Configurations                         |
|-----------------------|----------------------------------------|
|                     1 | Single                                 |
|                     2 | Line                                   |
|                     3 | Line , "L"                             |
|                     4 | Line, "L", Rectangle                   |
|                     5 | Line, "L", "U"                         |
|                     6 | Line , "L", Rectangle                  |
|                     7 | Line , "U"                             |
|                     8 | Line , "L2", Open Rectangle, Rectangle |
|                     9 | Line , "U", Rectangle                  |
|                    10 | Line , "L2", Open Rectangle, Rectangle |

