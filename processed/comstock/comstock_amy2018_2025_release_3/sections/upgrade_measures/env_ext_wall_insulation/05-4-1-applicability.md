<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | docs/upgrade_measures/env_ext_wall_insulation.md | status: site_page | source_url: https://github.com/NatLabRockies/ComStock.github.io/blob/bacf551bc5d2f595d2b3c41a57de0beea23ec6be/docs/upgrade_measures/env_ext_wall_insulation.md | publication_url: https://natlabrockies.github.io/ComStock.github.io/docs/upgrade_measures/env_ext_wall_insulation.html | corpus_version: 267e3ea | corpus_path: upgrade_measures/unpublished_docs/upgrade_measures/env_ext_wall_insulation.md | section: 4.1  Applicability | lines: 459-498 -->
## 4.1  Applicability

Based on the many examples readily identified through a cursory search, it appears that exterior insulation is readily applied to mass, wood-framed, and steel-framed walls. Although it is hypothetically possible to install on the exterior of metal buildings, in practice this was judged to be unlikely to occur, given the construction approaches used for metal buildings. For those buildings, interior insulation appears much more practical and likely. Based on Figure 1, metal building wall construction only applies to a small fraction of the building stock, so inapplicability of exterior wall insulation to buildings with metal walls will have an insignificant impact on national scale results.

#
![Timeline Description automatically generated](./media/9da535c0-88ac-4627-a9e0-30bfbb96c6a5.png)

Figure 3. Floor area by energy code followed during last wall replacement and wall construction type

For modeling purposes, the thickness of XPS insulation necessary to bring the wall assembly up to the AEDG recommendation for each climate zone is calculated. When the existing walls already meet or exceed the AEDG recommendations shown in Table 2, this measure is not applicable. When the required insulation thickness is less than 0.5 in., this measure is not applicable. For required thicknesses greater than 0.5 in., the selected thickness is rounded to the nearest inch using standard rounding to reflect commonly available products, as shown in Table 4. Because the amount of insulation to be applied varies based on the existing condition and the climate zone, the savings will vary based on these same characteristics as well.

Table 9. Insulation Thickness Selection Approach

| **Required Thickness (in.)** | **Modeled Thickness (in.)** |
|---|---|
| 0.4 | Not applicable |
| 0.5 | 1 |
| 0.9 | 1 |
| 1.1 | 1 |
| 1.4 | 1 |
| 1.5 | 2 |
| 1.9 | 2 |
| 2.1 | 2 |
| …and so forth |

# 5.  Output Variables

Table 10 includes a list of output variables that are calculated in ComStock. These variables are important in terms of understanding the differences between buildings with and without the exterior wall insulation measure applied. Additionally, these output variables can also be used for understanding the economics (e.g., return of investment) of the upgrade if cost information (i.e., material, labor, and maintenance cost for technology implementation) is available.

Table 10. Output Variables Calculated From the Measure Application

| **Variable Name** | **Description** |
|---|---|
| Target R-value | Target insulation R-value based on climate zone (ft2-hr-R/Btu) |
| Insulation R-value per Inch | XPS R-value per inch (ft2-hr-R/Btu per inch) |
| Required Insulation Thickness | Insulation thickness required to meet target R-value (in.) |
| Exterior Wall Insulation Area | Area of insulation added (ft2) |

# 6.  Results

