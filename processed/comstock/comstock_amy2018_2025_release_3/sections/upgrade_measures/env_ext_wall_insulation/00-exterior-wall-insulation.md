<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | docs/upgrade_measures/env_ext_wall_insulation.md | status: site_page | source_url: https://github.com/NatLabRockies/ComStock.github.io/blob/bacf551bc5d2f595d2b3c41a57de0beea23ec6be/docs/upgrade_measures/env_ext_wall_insulation.md | publication_url: https://natlabrockies.github.io/ComStock.github.io/docs/upgrade_measures/env_ext_wall_insulation.html | corpus_version: 43ae2d4 | corpus_path: upgrade_measures/unpublished_docs/upgrade_measures/env_ext_wall_insulation.md | section: Exterior Wall Insulation | lines: 2-47 -->
# Exterior Wall Insulation

Authors: Andrew Parker and Amy LeBar

#  Executive Summary

Building on the successfully completed effort to calibrate and validate the U.S. Department of Energy's ResStock™ and ComStock™ models over the past three years, the objective of this work is to produce national data sets that empower analysts working for federal, state, utility, city, and manufacturer stakeholders to answer a broad range of analysis questions.

The goal of this work is to develop energy efficiency and demand flexibility end-use load shapes that cover a majority of the high-impact, market-ready (or nearly market-ready) measures. "Measures" refers to energy efficiency variables that can be applied to buildings during modeling.

An *end-use savings shape* is the difference in energy consumption between a baseline building and a building with an energy efficiency or demand flexibility measure applied. It results in a timeseries profile that is broken down by end-use and fuel (electricity or on-site gas, propane, or fuel oil use) at each timestep.

ComStock is a highly granular, bottom-up model that uses multiple data sources, statistical sampling methods, and advanced building energy simulations to estimate the annual subhourly energy consumption of the commercial building stock across the United States. The baseline model intends to represent the U.S. commercial building stock as it existed in 2018. The methodology and results of the baseline model are discussed in the final technical report of the [End-Use Load Profiles](https://www.nlr.gov/buildings/end-use-load-profiles.html) project.

This documentation focuses on a single end-use saving shape measure---exterior wall insulation. This measure resulted in increased R-value across the stock, and 2.52% (100 TBtu) stock energy savings. The majority of cooling energy savings came from cooling-dominant climate zones, and heating savings from heating-dominant climate zones.

# 1.  Introduction

This documentation covers exterior wall insulation upgrade methodology and briefly discusses key results. Results can be accessed on the ComStock data lake "[end-use-load-profiles-for-us-building-stock](https://data.openei.org/s3_viewer?bucket=oedi-data-lake&prefix=nrel-pds-building-stock%2Fend-use-load-profiles-for-us-building-stock%2F)" or via the Data Viewer at [comstock.nlr.gov.](https://comstock.nlr.gov/)

|---|---|
| **Measure Title** | Exterior Wall Insulation |
| **Measure Definition** | This measure applies extruded polystyrene foam insulation to applicable building models. |
| **Applicability** | Models with mass, steel-framed, or wood-framed walls |
| **Not Applicable** | • Models with metal walls.<br> • Models whose existing wall insulation already meets or exceeds Advanced Energy Design Guide (AEDG) recommendations.<br> • Required exterior insulation thickness is less than 0.5 in. |
| **Release** | EUSS 2023 Release 1 |

# 2.  Technology Summary

Exterior wall insulation is, as the name suggests, attached to the exterior of the structural elements in the existing wall and covered by a cladding system. For purposes of this document, it refers to rigid or semi-rigid board insulation, not to spray-applied insulation. Common materials include expanded polystyrene foam (EPS), extruded polystyrene foam (XPS), polyisocyanurate foam, and mineral fiber board. These materials typically come in 4 ft x 8 ft sheets with thicknesses of 1 in., 1.5 in., or 2 in., and can be applied in multiple layers up to 8 in. of thickness if desired \[1\].

Application approaches vary depending on the structure of the existing wall system. For existing wood-framed and steel-framed walls, the existing cladding is removed, the insulation board is put into place, vertical wood furring or metal hat channel is put on top of the insulation board and fastened through the insulation board to the studs of the existing wall system, then a new cladding system is applied to the furring strips or hat channel. For existing masonry walls, any existing cladding is removed, vertical wood furring is fastened to the masonry walls directly, the insulation board is put into place, another set of vertical wood furring or metal hat channel is put on top of the insulation board and fastened through the insulation board to the first layer of wood furring, then a new cladding system is applied to the furring strips or hat channel. In all applications, water management and drainage planes must be detailed correctly to ensure long-term durability. In the past, it was common for the exterior insulation and finish system (EIFS) application approach to be detailed incorrectly, leading to premature failures. However, with correct detailing, exterior insulation can be installed in a durable manner \[2\].

Exterior insulation has been applied to many buildings, and continuous insulation is included as a requirement for many climate zones in newer versions of ASHRAE 90.1. Problems with insulation performance tend to stem from improper water management design or installation, so this analysis assumes those issues are handled correctly.

Table 1 shows the typical thermal performance characteristics of the most common exterior board insulation materials.

Table 1. Thermal Performance of Common Insulation Board Materials

| **Insulation Type** | **R-Value per Inch (hr-ft2-°F / Btu)** |
|---|---|
| Expanded polystyrene (EPS) | 4 |
| Extruded polystyrene (XPS) | 5 |
| Polyisocyanurate (Polyiso) | 6 |
| Mineral fiber board | 4.2 |

