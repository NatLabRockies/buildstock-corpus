<!-- resstock resstock_amy2018_2025_release_1 | upgrade_measures | measure_pdfs/95032.pdf | status: osti_pdf | source_url: https://docs.nlr.gov/docs/fy26osti/95032.pdf | publication_url: https://docs.nlr.gov/docs/fy26osti/95032.pdf | corpus_version: resstock_amy2018_2025_release_1-v1-pre | corpus_path: upgrade_measures/measure_pdfs/95032.md | section: 2.2.8 G-Function Library Integration | lines: 876-1005 -->
## 2.2.8 G-Function Library Integration

G-function values have been updated both to allow for documenting the source of g-functions going forward and to take advantage of recently published g-functions covering additional borehole configurations. The new g-functions come from a recently published library: OpenEI Geothermal Data Repository's 'G-Function Library for Modeling Vertical Bore Ground Heat Exchanger' 22 (Spitler, et al. 2021). This library includes a large number (over 34,000) of precomputed g-functions for a variety of borehole geometries, including several different shapes and five different depths. G-functions are geometry-specific and depend on the following parameters:

[22 https://gdr.openei.org/submissions/1325](https://gdr.openei.org/submissions/1325)

- 𝐵𝐵 : Borehole spacing (m)
- 𝐻𝐻 : Active borehole depth (m)
- 𝐷𝐷 : Depth from ground surface to the top of the active depth of the borehole (m)
- 𝑟𝑟 𝑏𝑏 : Borehole radius (m)

Table 5 gives some geometry parameters used in the g-function library.

Table 5. Borehole Depths and Diameters in the G-Function Library

|   Borehole Depth (m) |   Borehole Diameter (m) |
|----------------------|-------------------------|
|                   24 |                    0.15 |
|                   48 |                    0.15 |
|                   96 |                    0.15 |
|                  192 |                    0.16 |
|                  384 |                   0.175 |

While these physical parameters define the ground heat exchanger, the actual g-function values depend on dimensionless parameters:

- 𝑡𝑡 / 𝑡𝑡 𝑠𝑠 : Dimensionless time
- 𝑟𝑟 𝑏𝑏 / 𝐻𝐻 : Ratio of borehole radius to borehole length
- 𝐵𝐵 / 𝐻𝐻 : Ratio of borehole spacing to borehole length
- 𝐷𝐷 / 𝐻𝐻 : Ratio of the depth of the top of the borehole to borehole length

Since we are specifically modeling residential buildings with smaller loads than many commercial buildings, only a relatively small subset of the precalculated g-functions for 10 or less boreholes will be directly leveraged in this work, as this corresponds to the loads seen in residential buildings. The library supports the following shapes: rectangles, zoned rectangles, open rectangles, C, L, U, and Lopsided U (Figure 14). The original g-function library has the g-functions listed in JSON files for hundreds of possible combinations for each of the seven configurations (Rectangle, L, C, U, LopU, OpenRectangle, and Zoned Rectangle). There are 34,321 in total across all configurations.

Figure 14. Examples of the top view of some ground heat exchanger configurations 23

<!-- figure described by overlay: resstock_resstock_amy2018_2025_release_1/upgrade_measures/measure_pdfs/95032.yaml
     source: 95032_images/image_000012_c26098c96bf2d74e4306840eb471fc8a462a3d4f20213b734ea1614320d259c1.png
     method: vision-description
     described: 2026-11-11 -->

![Nine top-view dot plots of borehole field layouts: rectangle, C, L, zoned rectangle, U, lopsided U, open rectangle](95032_images/image_000012_c26098c96bf2d74e4306840eb471fc8a462a3d4f20213b734ea1614320d259c1.png)

Figure 14: nine top-view dot plots of borehole layouts, each with x and y axes in metres and a title giving its dimensions and number of boreholes (NBH). The labelled shapes are Rectangle (5x8, NBH 40), C (8x12, NBH 33), L (7x13, NBH 19), Zoned Rectangle (10x15, NBH 49), two U layouts (NBH 23 and 72), LopU (NBH 17) and two Open Rectangle layouts (NBH 42 and 44).

Each library requires one or two JSON keys to access a specific layout of a borehole configuration. In terms of representing the ground heat exchanger layouts in a JSON file, each configuration uses one or two keys to describe the actual layout of each borehole configuration.

Table 6 describes the meaning of first and second key in the JSON files that represent borehole configurations similar to those shown in Figure 15.

23 Reprinted from (Spitler, et al. 2021). NBH=Number of boreholes. M×N is the form of representation of the borehole layout where M is the maximum number of boreholes along the horizontal (x) axis and N is the maximum number of boreholes along the vertical (y) axis.

Table 6. Overview of the G-Function Library Contents

Reprinted from (Spitler, et al. 2021)

| Configuration Name   | Notes                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|----------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Rectangle            | Standard M×N cases (i.e., M columns, N rows) with uniform spacing. Only one key is required to access a specific configuration.                                                                                                                                                                                                                                                                                                                                               |
| Zoned Rectangle      | Similar to the Rectangle configurations, this configuration type has had rows/columns removed from the interior zone to represent configurations where the interior spacing of the ground heat exchanger is greater than that of the exterior (or perimeter) spacing. This library defines a specific configuration using the N and M values for the exterior as well as Ni and Mi values for the interior section. Two keys are required to access a specific configuration. |
| Open Rectangle       | These configurations represent N by M rectangular cases where boreholes are only around the perimeter, but the perimeter can have more than one row of boreholes. The number of rows around the perimeter is specified with the key 't.' Two keys are required to access a specific configuration.                                                                                                                                                                            |
| C                    | This type of configuration may be thought of as an open rectangle configuration that has had some number of boreholes removed from the top side. The current C configurations in the library all have one row of boreholes around the perimeter. The number of boreholes removed is represented by the key 'r.' Two keys are required to access a specific configuration.                                                                                                     |
| L                    | These configurations consist of a line N boreholes long and M boreholes wide. The L cases have a single row of boreholes. Only one key is required to access a specific configuration.                                                                                                                                                                                                                                                                                        |
| U                    | This type of configuration is U-shaped, with an opening at the top. The U may have up to 3 perimeter rows of boreholes around all sides of the U. The number of perimeter rows is represented with 't.' Two keys are required to access a specific configuration.                                                                                                                                                                                                             |
| LopU (Lopsided U)    | These configurations consist of U cases that have had some number of boreholes removed from their right side. These configurations all have a single row of perimeter boreholes. The number of boreholes removed is represented by 'r.' Two keys are required to access a specific configuration.                                                                                                                                                                             |

Figure 15. Example of JSON file structures that represent a Rectangle borehole configuration (left) and a C configuration (right) 24

<!-- figure described by overlay: resstock_resstock_amy2018_2025_release_1/upgrade_measures/measure_pdfs/95032.yaml
     source: 95032_images/image_000013_3d56b6b5e0e4eec8b2d2083e2394ac7995cf49b0a6f8cd07920b0bb3b8976eea.png
     method: vision-description
     described: 2026-11-11 -->

![Code editor screenshot of rectangle_5m_v1.0.json with an arrow on the single layout key](95032_images/image_000013_3d56b6b5e0e4eec8b2d2083e2394ac7995cf49b0a6f8cd07920b0bb3b8976eea.png)

Figure 15, left panel: dark-theme code editor screenshot of rectangle_5m_v1.0.json under HPXMLtoOpenStudio/resources/g_functions. One orange arrow points at the top-level key "1_1", the single key that selects a Rectangle layout. Beneath it are bore_locations, a g block whose entries are keyed like "5._192._0.08", and logtime; further collapsed layout keys follow ("1_10", "1_2", "1_3" and so on).

<!-- figure described by overlay: resstock_resstock_amy2018_2025_release_1/upgrade_measures/measure_pdfs/95032.yaml
     source: 95032_images/image_000014_84cf7c06986c50e5750fa755d4e89891cbb125ff420ec268adefbf09c943dfd7.png
     method: vision-description
     described: 2026-11-11 -->

![Code editor screenshot of C_configurations_5m_v1.0.json with arrows on its two layout keys](95032_images/image_000014_84cf7c06986c50e5750fa755d4e89891cbb125ff420ec268adefbf09c943dfd7.png)

Figure 15, right panel: dark-theme code editor screenshot of C_configurations_5m_v1.0.json under HPXMLtoOpenStudio/resources/g_functions. Two orange arrows point at the nested keys "3_3" and "1", the two keys that together select a C layout. Inside are collapsed bore_locations, g and logtime entries, followed by a second top-level key "3_4" with its own "1" entry. The file runs to 430 lines.

Only the down-selected components of the JSON files with 10 or less boreholes are downloaded from the repository to be stored under the 'HPXMLtoOpenStudio/resources/g\_functions' module in the OpenStudio-HPXML repository (currently under development in the 'geothermal\_loop' branch at the time of writing of this report). This down-selection is done so that the live repository is not strained in terms of memory allocation for maintaining the g-function library contents that are irrelevant at a residential dwelling unit scale. The user is given the degree of freedom to choose the specific type of configuration (U vs. L, etc.). The actual layout of boreholes within each configuration type is then chosen by OpenStudio-HPXML based on whichever layout has the minimum land area dimensions requirement at the ground level.

The documentation distributed together with the g-function library (Spitler, et al. 2021) describes the interpolation methodology that a design tool can use to iteratively adjust and choose a suitable depth for a correctly sized ground heat exchanger. Each layout within each configuration in the original g-function library provides g-functions for five different segments of depth for each borehole, for the depths of 24 m (79 ft), 48 m (157 ft), 96 m (315 ft), 192 m (630 ft) and 384 m (1,260 ft). In actual energy simulation using OpenStudio-HPXML (using the EnergyPlus simulation engine), the borehole configurations generated will have different borehole depths than one of the discrete bins provided in the OpenEI g-function library. Hence, interpolation is necessary between the values given in the g-function library for an OpenStudio-HPXML run.

24 The orange arrows show the location of the keys within each JSON file that specify the exact layout within each borehole configuration. Screenshots taken from Visual Studio Code text editor.

Interpolation is performed in accordance with the methodology laid out in (Spitler, et al. 2021). The procedure for determining the final interpolated g-function values to a specific borehole configuration, borehole depth, and borehole radius is depicted in the Figure 16 below.

Figure 16. Summary of the g-function interpolation procedure From (Spitler, et al. 2021)

<!-- figure described by overlay: resstock_resstock_amy2018_2025_release_1/upgrade_measures/measure_pdfs/95032.yaml
     source: 95032_images/image_000015_4e0e834577ca62244b368024ba1389acc61c4f5f161cfff94fd31840a94d19dc.png
     method: vision-description
     described: 2026-11-11 -->

![Flowchart of the four-step g-function interpolation procedure](95032_images/image_000015_4e0e834577ca62244b368024ba1389acc61c4f5f161cfff94fd31840a94d19dc.png)

Figure 16: flowchart of four boxes joined by downward arrows. Step 1: configuration selected with B, H, rb and B/H. Step 2: interpolate g-function values based on B/H, and the corresponding values of rb/H (to be used in the correction) and D/H (informational only). Step 3: calculate rb (interpolated value). Step 4: correct g-function values for the actual rb using Equation 1. No data are shown.

An example of a 5×8 rectangular borefield has also been provided in the g-function library User Guide, which was used to validate the functionality of the new approach implemented in the OpenStudio-HPXML workflow. For this validation purpose, the '5\_8 Rectangle' configuration has been retained in the down-selected g-function library, even though the total number of boreholes in this configuration exceeds the upper limit of 10 boreholes being modeled with OpenStudio-HPXML. Using one of the test files in the original OpenStudio-HPXML repository called 'base-hvac-test-case.xml,' an upgrade was implemented such that the heating and cooling system of this HPXML file was upgraded with a GHP system of the same capacity. The g-functions for this upgraded GHP system, as calculated with the new workflow implementation in OpenStudio-HPXML, were then compared against the values provided in the g-function library documentation (User Guide) example for the 5×8 rectangular borehole configuration. Figure 17 illustrates the validation of the g-functions from the new OpenStudio-HPXML run for the upgraded 'base-hvac-test-case.xml' case against the g-function library documentation results.

<!-- figure described by overlay: resstock_resstock_amy2018_2025_release_1/upgrade_measures/measure_pdfs/95032.yaml
     source: 95032_images/image_000016_aa3e725d033f56a66ececb988e75a63754ddf0f16fe8d8c8035c1b6eef7561b2.png
     method: vision-description
     described: 2026-11-11 -->

![Table image of g-function values A and B at 27 values of ln(t/ts)](95032_images/image_000016_aa3e725d033f56a66ececb988e75a63754ddf0f16fe8d8c8035c1b6eef7561b2.png)

Figure 17, left panel: a table rendered as an image, with columns ln(t/ts), A and B and 27 rows from ln(t/ts) = -8.5 to 3.003. A is the g-function from the OpenStudio-HPXML run and B the library documentation example. The two agree to about three decimal places throughout, from 2.6191 and 2.6190 in the first row to 43.8846 and 43.8850 in the last. The right panel plots the same values.

Figure 17. Validation of g-function outputs from the example 5x8 rectangular borehole configuration. 25  The 'A' dots are the expected g-function data and 'B' is the interpolated g-function.

<!-- figure described by overlay: resstock_resstock_amy2018_2025_release_1/upgrade_measures/measure_pdfs/95032.yaml
     source: 95032_images/image_000017_099c716c5f0ef5cfa411df2378251f51da8bc43dbd09baac7b3143045bfa52d4.png
     method: vision-description
     described: 2026-11-11 -->

![Line and scatter chart of g-function value against ln(t/ts), series A on series B](95032_images/image_000017_099c716c5f0ef5cfa411df2378251f51da8bc43dbd09baac7b3143045bfa52d4.png)

Figure 17, right panel: chart titled 'g-function validation'. X-axis is ln(t/ts), -10 to 4; y-axis is g-function value, 0 to 50. Series A is plotted as dots and series B as a line. Both trace one S-shaped curve, from about 2.6 at ln(t/ts) = -8.5 to about 44 at 3, steepest between -4 and 0; the dots sit on the line. The left panel tabulates the values.

For this upgrade measure the default configuration ground heat exchanger is assumed to be rectangular in ResStock, although advanced users can specify alternate configurations. From the g-function library, the borehole spacing, B, is assumed to be 5 m and the depth, 𝐷𝐷 , will be assumed to be 2 m. The values for dimensionless time 𝑡𝑡 / 𝑡𝑡 𝑠𝑠 are taken directly from the library (which corresponds to the existing array of dimensionless time). A maximum number of boreholes of 10, consistent with the current implementation of the ground domain, will also be enforced.

Note that in some cases, multiple borehole placements can occur for the same configuration. For example, a 'Rectangle' for six boreholes can be either 1x6 or 2x3. There are currently no plans to implement the ability to specify the exact configuration of the ground heat exchanger, just the shape of the configuration. When a default must be chosen, OpenStudio-HPXML will default to the configuration closest to a square, making the implicit assumption that this will reduce the required land area at the expense of having more interaction between boreholes. In the example of six boreholes, the default configuration for 'Rectangle' would be 2x3 rather than 1x6.

25  A = g-functions generated from the upgraded OpenStudio-HPXML example file 'base-hvac-test-case.xml'; B = g-function library documentation example for interpolated and corrected g-function values for the 5x8 rectangular configuration (M=5, N=8, B=7m, H=150m, D=2m, rb = 80 mm).

