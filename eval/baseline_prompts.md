# Bare-Claude baseline prompts — ComStock 2025-3

Paste each question into a fresh Claude chat with no attachments and no project context, then grade the reply against the facts listed under it. This is the same baseline `bsc eval --answer --judge` automates; it exists so the comparison can be run without an API key.

## df_load_shift_defaults  (measure_parameters)

```text
In ComStock, what is the default setpoint adjustment and the default duration of pre-conditioning for the thermostat control for load shifting measure, and which setpoints does the study actually adjust?
```

A correct answer must contain:
- -1°C
- 1 hour
- pre-cooling only

## df_load_shift_applicability  (measure_parameters)

```text
Which ComStock building type is the thermostat control for load shifting measure applied to, what HVAC requirement must a building meet, and what share of ComStock floor area is that?
```

A correct answer must contain:
- large office
- electric HVAC
- 9.72%

## df_shed_vs_shift_reports  (provenance)

```text
ComStock documents thermostat control for load shedding and thermostat control for load shifting as two separate measures. Which NREL report number documents each one?
```

A correct answer must contain:
- 89340
- 89341

## ca_swh_known_issue_2025r3  (release_specific)

```text
Is there a known issue with service water heating in California in ComStock 2025 Release 3, and if so what does the ComStock team recommend?
```

A correct answer must contain:
- service water heating was not modeled
- California
- 2025 Release 2

## roof_insulation_savings  (numeric)

```text
What aggregate site energy savings does ComStock's roof insulation measure show across the modeled U.S. commercial building stock, and to what share of buildings was it applicable?
```

A correct answer must contain:
- 112 TBtu
- 3%
- >99%

## hvac_heating_fuel_category_table  (dense_table)

```text
In the ComStock reference documentation, what heating fuel category is assigned to the "PSZ-AC with gas coil" HVAC system type, and what category is used for DOAS with fan coil district chilled water with district hot water?
```

A correct answer must contain:
- Fuel
- District_Heating

## hvac_type_probability_source  (methodology)

```text
What data does ComStock use to derive its HVAC system type probability distributions, and what variables do those distributions depend on?
```

A correct answer must contain:
- CBECS 2012
- CBECS 2018
- building type
- census division
- heating fuel

## new_sampling_first_release  (release_specific)

```text
Starting with which ComStock standard dataset release did the new sampling methodology take effect, and what does it let a single energy model represent?
```

A correct answer must contain:
- 2024 Release 2
- census tract

## roof_aedg_r_values_by_climate_zone  (dense_table)

```text
What are the target roof assembly R-values by climate zone that ComStock's roof insulation measure brings roofs up to?
```

A correct answer must contain:
- R-20
- climate zone 8

> Known corpus gap — the index cannot answer this either. KNOWN GAP. Tables 5 and 6 of env_roof_insulation.md are images in the Jekyll source, so only the surrounding narrative ("XPS at R-5/inch", "AEDG for Small to Medium Office Buildings") survived extraction — no per-climate-zone R-value exists anywhere in the processed corpus. Retrieval returns the right document with the numbers missing, which is the failure mode most likely to produce a confident wrong answer. Fixing it needs OCR or the upstream table data; that is why this entry stays in the set.

## measures_missing_documentation  (coverage)

```text
Which ComStock 2025-3 upgrade measures do not yet have published documentation?
```

A correct answer must contain:
- hvac_0021
- pkg_0012
- dr_0004

> Known corpus gap — the index cannot answer this either. KNOWN GAP. The answer exists in the pipeline (manifest gaps.measures = dr_0004, dr_0007-dr_0011, hvac_0021, pkg_0012; crosswalk counts 65 measures / 57 covered / 8 gaps) but crosswalk.json and manifest.json are not chunked into the index, so retrieval cannot reach it. Either index the structured artifacts as synthesized text or answer coverage questions from the manifest directly.
