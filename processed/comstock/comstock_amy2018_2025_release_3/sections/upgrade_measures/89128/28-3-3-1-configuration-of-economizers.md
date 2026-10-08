<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/89128.pdf | status: osti_pdf | source_url: https://www.nlr.gov/docs/fy24osti/89128.pdf | publication_url: https://www.nlr.gov/docs/fy24osti/89128.pdf | corpus_version: 43ae2d4 | corpus_path: upgrade_measures/measure_pdfs/89128.md | section: 3.3.1  Configuration of Economizers | lines: 538-573 -->
## 3.3.1  Configuration of Economizers

Specifics of a newly added economizer through an upgrade are applied in the same way as in models that already have economizers. In other words, configurations (e.g., control type and limit setting) are guided by the requirements of the energy code that was in force when the HVAC system was last updated. Each version of energy code (i.e., ASHRAE 90.1 or Title 24) includes best practices for leveraging economizers (depending on HVAC system size) as well as configuring economizers (depending on the climate zone). For example, ASHRAE 90.1-2010 includes information on preferrable control types, prohibited control types, and high limits for fixed control types as shown in Table 5. While some details vary between versions, these suggestions largely reflect physical reasonings such as considering temperature as well as humidity (i.e., prohibiting dry-bulb controls) measurements when the building is in humid regions (e.g., 1a, 2a, 3a, or 4a). More details on ComStock's economizer implementations are described in the ComStock Reference Documentation [4].

Table 5 . Economizer C onfiguration S uggestions in ASHRAE 90.1-2010

<!-- table recovered from measure_pdfs/89128.pdf p.24
     overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/89128.yaml
     method: vision-transcription -->

**TABLE 6.5.1.1.3A High-Limit Shutoff Control Options for Air Economizers**

| Climate Zones | Allowed Control Types | Prohibited Control Types |
|---|---|---|
| 1b, 2b, 3b, 3c, 4b, 4c, 5b, 5c, 6b, 7, 8 | Fixed dry bulb; Differential dry bulb; Electronic enthalpy (a); Differential enthalpy; Dew-point and dry-bulb temperatures | Fixed enthalpy |
| 1a, 2a, 3a, 4a | Fixed enthalpy; Electronic enthalpy; Differential enthalpy; Dew-point and dry-bulb temperatures | Fixed dry bulb; Differential dry bulb |
| 5a, 6a | Fixed dry bulb; Differential dry bulb; Fixed enthalpy; Electronic enthalpy (a); Differential enthalpy; Dew-point and dry-bulb temperatures |  |

(a) Electronic enthalpy controllers are devices that use a combination of humidity and dry-bulb temperature in their switching algorithm.

**TABLE 6.5.1.1.3B High-Limit Shutoff Control Settings for Air Economizers**

| Device Type | Climate | Required High Limit (Economizer Off When): Equation | Required High Limit (Economizer Off When): Description |
|---|---|---|---|
| Fixed dry bulb | 1b, 2b, 3b, 3c, 4b, 4c, 5b, 5c, 6b, 7, 8 | T_OA > 75°F | Outdoor air temperature exceeds 75°F |
| Fixed dry bulb | 5a, 6a | T_OA > 70°F | Outdoor air temperature exceeds 70°F |
| Differential dry bulb | 1b, 2b, 3b, 3c, 4b, 4c, 5a, 5b, 5c, 6a, 6b, 7, 8 | T_OA > T_RA | Outdoor air temperature exceeds return air temperature |
| Fixed enthalpy | 2a, 3a, 4a, 5a, 6a | h_OA > 28 Btu/lb (a) | Outdoor air enthalpy exceeds 28 Btu/lb of dry air (a) |
| Electronic enthalpy | All | (T_OA , RH_OA) > A | Outdoor air temperature/RH exceeds the "A" setpoint curve (b) |
| Differential enthalpy | All | h_OA > h_RA | Outdoor air enthalpy exceeds return air enthalpy |
| Dew-point and dry-bulb temperatures | All | DP_oa > 55°F or T_oa > 75°F | Outdoor air dry bulb exceeds 75°F or outside dew point exceeds 55°F (65 gr/lb) |

(a) At altitudes substantially different than sea level, the Fixed Enthalpy limit shall be set to the enthalpy value at 75°F and 50% relative humidity. As an example, at approximately 6000 ft elevation the fixed enthalpy limit is approximately 30.7 Btu/lb.

(b) Setpoint "A" corresponds to a curve on the psychrometric chart that goes through a point at approximately 75°F and 40% relative humidity and is nearly parallel to dry-bulb lines at low humidity levels and nearly parallel to enthalpy lines at high humidity levels.

