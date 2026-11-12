<!-- resstock resstock_amy2018_2025_release_1 | upgrade_measures | measure_pdfs/96414.pdf | status: osti_pdf | source_url: https://docs.nlr.gov/docs/fy26osti/96414.pdf | publication_url: https://docs.nlr.gov/docs/fy26osti/96414.pdf | corpus_version: resstock_amy2018_2025_release_1-v1-pre | corpus_path: upgrade_measures/measure_pdfs/96414.md | section: 1.2.1.8  Electrical Requirements | lines: 223-252 -->
## 1.2.1.8  Electrical Requirements

This section summarizes the electrical information for the dual fuel heat pump upgrade. Electrical information in ResStock is used to assess whether the home's electrical panel would become space-constrained or over-capacity due to this upgrade. Section 3.3 describes the electrical panel constraint modeling in more detail.

The power rating of a ducted heat pump system is the sum of the power ratings of the compressor, the air handler, and any electric backup allowed to operate simultaneously, as summarized in Table 1. The heat pump compressor power rating is estimated based on its design heating capacity using a regression equation derived from product labels. The air handler power rating is estimated from the design airflow rate and the OS-HPXML assumption of fan power. The electric resistance backup power rating is directly converted from its heating capacity at an efficiency of 100%. For more information on the modeling assumptions, see the Technical Reference Document (Reyna, et al. 2025).

Table 1. Default Power Rating of Ducted Heat Pump System Components

| Component            | Power Rating [W]                                  | Note                                                          |
|----------------------|---------------------------------------------------|---------------------------------------------------------------|
| Heat Pump Compressor | (0.631 * Heating_Capacity [kBtu/h] + 1.615) * 240 | Regression of Minimum Circuit Amp, multiplied by voltage      |
| Air Handler          | Air_Flow [cfm] * Fan_Power [W/cfm]                | Default to OS-HPXML assumptions                               |
| Electric Backup      | Heating_Capacity [kBtu/h] * 293.07                | Convert heating capacity directly to power at 100% efficiency |

Ducted heat pumps require at least one 208/240V circuit, each protected by a double-pole breaker. The specific number of circuits depend on whether the heat pump has backup heating (dual fuel or electric) and how the indoor and outdoor units, along with the backup, are configured. Table 2 summarizes the wiring configurations for ducted heat pumps assumed in ResStock. For example, a dual fuel heat pump is assumed to have a 120V air handler on one circuit and a separate 240V circuit for the compressor. For heat pumps with electric backup, the air handler is commonly 240V to allow the strip heat to be on the same circuit; this is also the assumption in ResStock. The maximum overcurrent protection allowed per circuit is assumed to be up to 50A. Therefore, more circuits may be required for larger heat pump systems, which correspond to the use of multiple compressors and/or heat kits in practice.

While a heat pump upgrade replaces both heating and cooling, it may require more circuits and breaker spaces to install than are freed up by removing the existing HVAC systems. The heat pump upgrade may also add more connected load to the panel, especially when the backup is sized for emergency use. The power rating of heat pump systems is determined by their heating configuration and the presence of electric resistance backup. Therefore, homes in colder climates are more likely to face a capacity constraint when upgrading to a heat pump since a backup is often required to supplement the heat pump performance and these homes are more likely to have previously used fuel heating.

Table 2. Default Voltage and Breaker Space for Ducted Heat Pumps

(Note: ckt: circuit, ODU: outdoor unit or heat pump compressor, IDU: indoor unit or air handler)

| Heat Pump System                                   | Circuits                                   | Breaker Spaces                                                                                   |
|----------------------------------------------------|--------------------------------------------|--------------------------------------------------------------------------------------------------|
| Air-to-air / ground-to- air, ducted, dual fuel     | ckt 1: 240V, ODU ckt 2: 120V, IDU          | ckt 1: 2 * round_up(ODU power [W] / 12000) ckt 2: 1                                              |
| Air-to-air / ground-to- air, ducted, no backup     | ckt 1: 240V, ODU ckt 2: 240V, IDU          | ckt 1: 2 * round_up(ODU power [W] / 12000) ckt 2: 2                                              |
| Air-to-air, ground-to-air, ducted, electric backup | ckt 1: 240V, ODU ckt 2: 240V, IDU + backup | ckt 1: 2 * round_up(ODU power [W] / 12000) ckt 2: 2 * round_up((IDU + backup) power [W] / 12000) |

For natural gas systems, the load calculation generally does not include any electrical load from non-electric equipment or appliances. However, because heating and cooling loads in ResStock are determined based on individual HVAC components, gas furnaces are assigned a small service rating based on the air handler power, which is determined by the design air flow rate. Additionally, the air handler is typically on a 120V circuit, which uses a single-pole breaker. Upgrading to a natural gas furnace does not add any constraint to the electrical panel or service; instead, it frees up panel capacity and space for homes that previously used electric heating.

