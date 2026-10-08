<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/98345.pdf | status: osti_pdf | source_url: https://docs.nlr.gov/docs/fy26osti/98345.pdf | publication_url: https://docs.nlr.gov/docs/fy26osti/98345.pdf | corpus_version: 267e3ea | corpus_path: upgrade_measures/measure_pdfs/98345.md | section: 2  ComStock Baseline Approach | lines: 273-308 -->
## 2  ComStock Baseline Approach

Currently, only multizone (not single-zone) VAV systems are represented in the ComStock baseline [14]. 3 In the ComStock baseline, VAV fans are modeled with the Fan:VariableVolume object from EnergyPlus, which characterizes fan power draw with a curve representing power as a function of flow, without explicit modeling of fan pressure rise [12]. In EnergyPlus, airflows are dictated based on ventilation requirements and zone loads, and limits on airflow are set in the terminal unit objects rather than in the fan itself. Since duct pressure is not explicitly modeled in ComStock, VAV terminal units are analogous to pressure-independent boxes.

ComStock incorporates the OpenStudio® Standards approach for implementing SP resets, which reflects the applicable version of ANSI/ASHRAE/IES 4 Standard 90.1. Based on the applicable template, multizone VAV fans in ComStock and OpenStudio Standards are modeled with a curve reflective of an SP reset or without an SP reset. The assignment logic is listed in Table 1. Where the criteria for an SP reset are met, an SP reset is implemented in OpenStudio Standards and the ComStock baseline. Where only a fan threshold is listed, any fan with rated motor input power exceeding the threshold will have an SP reset implemented. Where a cooling capacity is also listed, that threshold must also be met for an SP reset to be implemented. For buildings with templates of an older vintage than ANSI/ASHRAE/IESNA Standard 90.1 2004 in the ComStock baseline, no SP resets are implemented.

Table 1. OpenStudio Standards Logic for Fan Curve Assignment

| Template                  | Motor Input Power Threshold (horsepower)   | Cooling Capacity Threshold (Btu/h)   |
|---------------------------|--------------------------------------------|--------------------------------------|
| DOE Ref Pre-1980          | N/A                                        | N/A                                  |
| DOE Ref 1980-2004         | N/A                                        | N/A                                  |
| ASHRAE 90.1 2004          | 9.9                                        | N/A                                  |
| ASHRAE 90.1 2007 and 2010 | 7.54                                       | N/A                                  |
| ASHRAE 90.1 2013          | DX cooling: 0                              | DX cooling: 110,000                  |
| ASHRAE 90.1 2013          | Chilled water/evaporative: 0.25            | Chilled water/evaporative: N/A       |

Multizone VAV fans in ComStock without an SP reset are modeled with the 'Multi Zone VAV with discharge dampers' curve from OpenStudio Standards [15]. Discharge dampers are a means of regulating airflow from VAV fans that reduces the extent to which individual VAV box dampers need to modulate. They are less energy-efficient than an SP reset. A minimum flow fraction of 25% is applied with ComStock's implementation of this fan curve [15]. In EnergyPlus, this minimum flow fraction is used only to calculate power draw, not to calculate airflows [12]. Figure 2 shows the fan curve used in multizone VAV models without an SP reset in ComStock, along with curves emulating SP resets.

3  Single-zone VAV systems are not represented in the ComStock baseline but are implemented through some measures [23]. This measure is not applicable to single-zone VAV systems. In single-zone VAV systems, airflow can modulate to meet the load of the zone served, so there is not a need for static pressure control [21].

4  ANSI = American National Standards Institute; ASHRAE = American Society of Heating, Refrigerating and AirConditioning Engineers; IES = Illuminating Engineering Society

Figure 2. Comparison of VAV fan curve without SP reset from ComStock baseline with curves emulating SP resets

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/98345.yaml
     source: 98345_images/image_000003_93be8e8d31c6d8d70a84a3d6c5714d78f641eb692c93929042e9027717c9b693.png
     method: vision-description
     described: 2026-08-21 -->

![Line chart comparing the ComStock multizone VAV baseline fan curve against two curves emulating static pressure resets, power fraction versus airflow fraction.](98345_images/image_000003_93be8e8d31c6d8d70a84a3d6c5714d78f641eb692c93929042e9027717c9b693.png)

Figure 2. Fan power fraction, vertical axis 0 to 1.2, against airflow fraction, horizontal axis 0 to 1.0, comparing the curve used for multizone VAV systems without a static pressure reset against two curves emulating resets. Three series are plotted at 0.1 airflow intervals. The blue series, MZ VAV with Discharge Dampers, is the ComStock baseline and reads about 0.229, 0.275, 0.302, 0.399, 0.476, 0.559, 0.655, 0.760 and 0.880 from airflow 0.0 through 0.8, where it stops. The red series, Good SP Reset, reads about 0.064, 0.073, 0.078, 0.101, 0.137, 0.20, 0.284, 0.403, 0.563 and 0.770 from 0.0 through 0.9. The green series, Perfect SP Reset, is lowest throughout at about 0.032, 0.032, 0.041, 0.060, 0.096, 0.151, 0.238, 0.362, 0.527 and 0.738. A vertical purple line at airflow 0.25 spans the full height, labeled ComStock Baseline Min Flow: the 25% minimum flow fraction applied to the baseline curve, which in EnergyPlus affects only power draw, not airflow. A note below the figure defines MZ as multizone. At 40% airflow the plotted baseline and good-reset values are about 0.48 and 0.14, a ratio near 0.29, consistent with the roughly 30% quoted in Section 5.6.

MZ = multizone

