<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/89128.pdf | status: osti_pdf | source_url: https://www.nlr.gov/docs/fy24osti/89128.pdf | publication_url: https://www.nlr.gov/docs/fy24osti/89128.pdf | corpus_version: 43ae2d4 | corpus_path: upgrade_measures/measure_pdfs/89128.md | section: 3.4.1 Applicability | lines: 595-617 -->
## 3.4.1 Applicability

Hotels and restaurants will not be modified by the measure. Hotels typically have either single zone unitary systems (e.g., PTAC, PTHP) or DOAS meeting HVAC needs, neither of which are suitable for DCV. Air loops that serve a space type without a code-defined per-person ventilation rate will not have this measure applied. Due to high concentration of heat and effluents, kitchens and restaurants often require the design outdoor airflow rate all day to maintain indoor air quality and should not have the outdoor airflow reduced at periods of lower occupancy.

There are also certain space types for which DCV is not appropriate and will be skipped in this measure. The following space types will not be modified:

- Kitchens
- Dining
- Laboratories
- Healthcare patient spaces
- Corridors and stairwells
- Mechanical rooms
- Data centers
- High exhaust spaces, such as restrooms and locker rooms.

For the reasons listed above, kitchens in non-restaurant buildings will not have DCV applied. Dining areas in these buildings will also not have DCV applied because these areas frequently use transfer air from kitchens.

In hospitals, proper ventilation and indoor air quality must be maintained to ensure infection control and patient safety. For this reason, hospital space types dealing with patient care will not have DCV applied (e.g., patient, radiology, exam, and surgical rooms). Non-patient space types such as offices will have DCV applied. Additionally, laboratory space types found in hospitals will not have DCV applied per energy code guidance.

Air loops that serve both applicable and inapplicable space types will have DCV applied but will only function in spaces that are applicable. To do this, inapplicable space types will have their outdoor air rates converted to 100% per-area to avoid triggering the EnergyPlus function.

In addition to the space type and building type applicability constraints above, any model with a DOAS will not have DCV applied at this time. In addition, models with single-zone unitary systems (e.g., PTAC, PTHP) will not have DCV applied because they are entirely reliant on occupants to manually control the ventilation air and are unable to be controlled using occupancy or CO2 sensors. Models with ERVs are not required by ASHRAE 90.1 to have DCV, but it will be added to models with ERV in this measure to represent optimal operating conditions.

