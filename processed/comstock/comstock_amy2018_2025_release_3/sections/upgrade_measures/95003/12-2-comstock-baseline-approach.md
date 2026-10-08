<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/95003.pdf | status: osti_pdf | source_url: https://docs.nlr.gov/docs/fy25osti/95003.pdf | publication_url: https://docs.nlr.gov/docs/fy25osti/95003.pdf | corpus_version: 0396270 | corpus_path: upgrade_measures/measure_pdfs/95003.md | section: 2  ComStock Baseline Approach | lines: 247-278 -->
## 2  ComStock Baseline Approach

The characteristics of existing chiller-equipped HVAC systems in ComStock™ are based on a combination of when the buildings were built and how the HVAC equipment has been assumed to have been updated over time. This is described in detail in the ComStock Reference Documentation [4]. HVAC equipment performance is assumed to meet the energy code requirements in force at the time and place of installation. The in-force energy code for the ComStock baseline is shown as total applicable floor area (and percentage) in Figure 1. Applicable floor area for this analysis includes ComStock buildings with HVAC system types that have either air-cooled or water-cooled chillers. Most ComStock baseline chillers follow energy code requirements from the early 2000s.

Figure 1. ComStock baseline in-force energy code followed as a percentage of applicable floor area.

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/95003.yaml
     source: 95003_images/image_000002_fb0d19afdce3609f9a0f723bb137726bc1877e77b4a8d3ce8879ec2e870b006f.png
     method: vision-description
     described: 2026-08-21 -->

![Table-and-bar chart of chiller stock floor area by in-force energy code and cooling type](95003_images/image_000002_fb0d19afdce3609f9a0f723bb137726bc1877e77b4a8d3ce8879ec2e870b006f.png)

Figure 1: Tableau table-with-bars listing ComStock baseline in-force energy code groups (DOE Ref pre-1980 through 90.1-2013 and California DEER standards) split by air-cooled versus water-cooled chillers, with paired bars for stock floor area in sqft and as a percentage. DOE Ref 1980-2004 dominates at 29.91% water-cooled and 15.98% air-cooled; every other group falls below 7%.

Applicable floor area includes ComStock buildings with chillers. DEER stands for Database for Energy Efficiency Resources, which represents building characteristics for California models following Title 24.

Air-cooled chillers provide chilled water for building cooling systems by using an air-cooled condenser for heat rejection, eliminating the need for a separate condenser water loop. The aircooled chiller efficiencies, both full-load and part load, are assigned based on the building code and capacity, aligning with ASHRAE-90.1 standards. ComStock models air-cooled chiller performance using three curve types: capacity as a function of leaving chilled water temperature and the entering condenser fluid temperature, energy input ratio (EIR) as a function of leaving chilled water temperature and the entering condenser fluid temperature, and EIR as a function of part-load ratio. These modifiers adjust the chiller's rated EIR and capacity for each time step to determine modified efficiency and capacity based on operating conditions. Below is a list of HVAC system types in ComStock that include air-cooled chillers:

- Dedicated outdoor air system (DOAS) with fan coil air-cooled chiller with baseboard electric

- DOAS with fan coil air-cooled chiller with boiler
- DOAS with fan coil air-cooled chiller with district hot water
- DOAS with fan coil chiller with baseboard electric
- Variable air volume (VAV) air-cooled chiller with parallel fan power (PFP) boxes
- VAV air-cooled chiller with district hot water reheat
- VAV air-cooled chiller with gas boiler reheat.

Water-cooled chillers provide chilled water for building cooling systems using a water-cooled condenser. These systems require condenser water to dissipate heat to the ambient air through cooling towers or fluid coolers. They are used in various HVAC configurations, such as DOAS and VAV systems, and can incorporate different heating options, including electric baseboards, boilers, and district hot water. Similar to air-cooled chillers, the efficiency of water-cooled chillers, both at full load and part load, is determined based on HVAC code templates and capacity, in accordance with ASHRAE 90.1 standards. ComStock models water-cooled chiller performance using the same three curve types as air-cooled chillers. Cooling towers, essential components of water-cooled chiller systems, reject heat from condenser water loops and are integrated into multiple ComStock HVAC configurations. The HVAC system types in ComStock that include water-cooled chillers are identical to those that incorporate air-cooled chillers, as previously listed.

More details on modeling HVAC systems including chillers can be found from the ComStock Reference Documentation [4].

