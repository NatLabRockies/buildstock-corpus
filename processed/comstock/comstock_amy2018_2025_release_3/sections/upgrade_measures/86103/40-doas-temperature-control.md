<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/86103.pdf | status: osti_pdf | source_url: https://www.nlr.gov/docs/fy24osti/86103.pdf | publication_url: https://www.nlr.gov/docs/fy24osti/86103.pdf | corpus_version: fadc83e | corpus_path: upgrade_measures/measure_pdfs/86103.md | section: DOAS Temperature Control | lines: 622-640 -->
## DOAS Temperature Control

The DOAS units will be controlled using a linear outdoor air reset scheme. ERV DOAS, which are modeled in climate zones with higher humidity concerns, will be controlled to discharge 55°F when outdoor temperatures are above 55°F, and 67°F when temperatures are below 45°F, floating linearly in between. This is like what is recommended in the ASHRAE DOAS Design Guide (illustrated in Figure 10), apart from the lower temperature being set to 55°F as opposed to

52°F. This is to provide a fair comparison, because RTUs in the ComStock baseline are set to discharge 55°F. HRV DOAS in drier climates are modeled the same, except for the lower discharge air temperature being set to 60°F. This may not always be required, as described in [6], but it is being modeled for all HRVs in this study to ensure reasonable discharge air conditions across the wide variety of models in the ComStock baseline.

To ensure that the DOAS temperature control set points are met, all systems will be modeled with an electric resistance heating coil and a DX cooling coil. A heat pump DOAS could also be used and may be considered for future studies. The heating coil is modeled with a COP of 1, whereas the DX cooling coil is modeled to align with ASHRAE Standard 90.1-2016.

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/86103.yaml
     source: 86103_images/image_000019_94a263dda12eb4ab3ab74aca137e75e0abff0e37170afb1b1ec546692c1d1539.png
     method: vision-description
     described: 2026-08-22 -->

![Figure 13: ASHRAE DOAS discharge temperature setpoint schedule, same graphic as Figure 4](86103_images/image_000019_94a263dda12eb4ab3ab74aca137e75e0abff0e37170afb1b1ec546692c1d1539.png)

Figure 13: the ASHRAE DOAS Design Guide discharge-temperature schedule, plotting DOAS discharge dry-bulb setpoint (deg F and deg C) against outdoor dry-bulb temperature: 67 deg F below about 45 deg F outdoors, a ramp through 45-55 deg F, then 52 deg F above 55 deg F. This is the same graphic printed earlier as Figure 4; it documents the control described in Section 4.2.2.

Figure 13. DOAS temperature set point recommendations form ASHRAE DOAS Design Guide

