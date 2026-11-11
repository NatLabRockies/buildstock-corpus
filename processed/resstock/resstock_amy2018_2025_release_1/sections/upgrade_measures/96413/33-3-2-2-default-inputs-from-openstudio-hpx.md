<!-- resstock resstock_amy2018_2025_release_1 | upgrade_measures | measure_pdfs/96413.pdf | status: osti_pdf | source_url: https://docs.nlr.gov/docs/fy26osti/96413.pdf | publication_url: https://docs.nlr.gov/docs/fy26osti/96413.pdf | corpus_version: resstock_amy2018_2025_release_1-v1-pre | corpus_path: upgrade_measures/measure_pdfs/96413.md | section: 3.2.2  Default Inputs From OpenStudio-HPXML for the Measure Upgrade Name | lines: 382-432 -->
## 3.2.2  Default Inputs From OpenStudio-HPXML for the Measure Upgrade Name

OpenStudio-HPXML will receive the ResStock inputs from Table 4 via the ResStockArguments OpenStudio Measure. Any values that are not specified by ResStock will be calculated using defaults in the BuildResidentialHPXML OpenStudio measure. Table 5 describes the HPXML default values calculated by this measure. These values are calculated in the defaults.rb file with many called Ruby methods being defined in the hvac.rb file. OpenStudio-HPXML documentation covering these elements can be found here.

Table 5. HPXML Default Values for the Typical Cold Climate Heat Pump Upgrade

<!-- table recovered from measure_pdfs/96413.pdf p.20
     overlay: resstock_resstock_amy2018_2025_release_1/upgrade_measures/measure_pdfs/96413.yaml
     method: pdf-text-layer
     supersedes the extractor's own table here (values af07d2bf2385…):
     and its continuation grid(s) (values 08455984ac30…):
       The table runs over pages 20 to 22 and was extracted as two grids, the second with the data row 'Rated fan power' as its header. Its last row, on page 22, was dropped: 'Heating energy input ratio as a function of flow fraction', [[1, 0, 0]]; [[1, 0, 0]]; [[1, 0, 0]], was absent from the document, with only its note stranded as a paragraph under section 3.4. The cells that were extracted matched the pages. The table's own sub-header rows (Cooling Curve Values, Heating Curve Values and so on) are used as the header rows of five sub-tables. -->

**HPXML defaults**

| HPXML Default | Value | Unit | Notes |
|---|---|---|---|
| Net sensible heat ratio | 0.78 |  |  |
| Crankcase heater power | 50 | W | Based on RESNET Publication No. 002-2017, heater warms lubricating oil pan |
| Fan power | 0.375 | W/cfm | Based on electronically commutating motor—a more efficient type of blower that allows for variable speeds and not on/off binary operation like permanent split capacitor blowers |
| Rated fan power | 0.18 | W/cfm | Based on ASHRAE 1449-RP |

**Cooling curve values**

| Cooling Curve Values | Value | Unit | Notes |
|---|---|---|---|
| Rated cfm per ton | [400, 400] | cfm/ton | Typical rated cfm per ton |
| Cycling degradation coefficient | 0.25 |  | The degradation coefficient encapsulates inefficiencies involved with system cycling, heating the coils, and distributing fluid. This value is derived from conversations with experts and engineering judgment |
| Gross sensible heat ratio | Calculated as a function of rated conditions, nominal cfm/ton, the coil Ao factor also known as the coil bypass factor, and the net sensible heat ratio. (the coil Ao factor is the effective coil surface area) |  | See the calculation for this here. |

**Cooling capacity and COP coefficients as a function of flow fraction**

| Cooling Capacity and COP Coefficients as a Function of Flow Fraction | Value | Unit | Notes |
|---|---|---|---|
| Cooling capacity as a function of flow fraction | [[1, 0, 0]]; [[1, 0, 0]] |  | No flow fraction coefficients are necessary because temperatures at min and max compressor speeds account for airflows |
| Cooling energy input ratio as a function of flow fraction | [[1, 0, 0]]; [[1, 0, 0]] |  | No flow fraction coefficients are necessary because temperatures at min and max compressor speeds account for airflows |

**Heating curve values**

| Heating Curve Values | Value | Unit | Notes |
|---|---|---|---|
| Rated cfm per ton | [400, 400, 400] | cfm/ton |  |
| Nominal to max ratio | 0.972 |  | This is the value for variable-speed compressors |

**Heating capacity and COP coefficients as a function of flow fraction**

| Heating Capacity and COP Coefficients as a Function of Flow Fraction | Coefficients |  | Notes |
|---|---|---|---|
| Heating capacity as a function of flow fraction | [[1, 0, 0]]; [[1, 0, 0]]; [[1, 0, 0]] |  | The functions of flow fraction are 1 because the blower is assumed to have constant flow |
| Heating energy input ratio as a function of flow fraction | [[1, 0, 0]]; [[1, 0, 0]]; [[1, 0, 0]] |  | The functions of flow fraction are 1 because the blower is assumed to have constant flow |

