<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/87542.pdf | status: osti_pdf | source_url: https://www.nlr.gov/docs/fy24osti/87542.pdf | publication_url: https://www.nlr.gov/docs/fy24osti/87542.pdf | corpus_version: 0a2f61f | corpus_path: upgrade_measures/measure_pdfs/87542.md | section: 2  ComStock Baseline Approach | lines: 334-373 -->
## 2  ComStock Baseline Approach

The ComStock baseline includes energy recovery in air handling units only when required by the governing energy code standard. The fraction of floor area conditioned by energy/heat recovery in ComStock is summarized in Table 2 by building type and energy code year. Note that older code years do not include heat/energy recovery, as they were not required by these energy codes. Also note that California models generally do not include heat/energy recovery because these models follow California Title 24 energy codes, which do not have heat/energy recovery requirements. The operation and performance of heat/energy recovery systems in the ComStock baseline are not discussed  in  this  work  because  existing  heat/energy  recovery  systems  are  not  affected  by  this measure. More information about the ComStock baseline heat/energy recovery systems can be found in the ComStock documentation [17].

The prevalence of heat/energy recovery in the ComStock baseline directly impacts the results of this analysis, as the measure will only be applied to AHUs that do not already include heat/energy recovery. Note that ComStock adds heat/energy recovery to models on an AHU-by-AHU basis, meaning a ComStock baseline model may have some AHUs with heat/energy recovery and some without, based on the code requirements. This measure is also applied on an AHU basis, so it may be  partially  applicable  to  some  ComStock  models.  The  ComStock  code-driven  approach  for applying  heat/energy  recovery  is  reasonable  but  difficult  to  validate.  The  most  prominent commercial building stock assessment, the Commercial Buildings Energy Consumption Survey (CBECS), does not include prevalence of heat/energy recovery systems [18]. Because heat/energy recovery  code  requirements  often  depend  on  system  size,  ComStock's  estimates  may  either overstate or underestimate the prevalence of existing systems with heat/energy recovery due to zoning assumptions. This, in turn, affects the number of systems that this measure upgrades and subsequently impacts the overall energy-saving potential of the technology in building stock.

The  benefits  of  heat/energy  recovery  systems  depend  on  routing  exhaust  air  through  the  heat exchanger. As discussed, some portion of the exhaust air in buildings may not be routed back to the  central  exhaust  or  heat  exchanger,  either  due  to  duct  leakage  or  separate  exhaust  fans. ComStock includes exhaust fans in some space types, summarized in Table 1. Note that some prominent  building  types,  such  as  small/medium/large  office,  warehouse,  and  retail,  do  not currently include any zone exhaust, so all exhaust air is assumed to return to the AHUs and become available for heat/energy recovery benefits, when applicable. Furthermore, ComStock models do not  currently  include  duct  leakage.  These  factors  may  overestimate  the  amount  of  exhaust  air available for heat/energy recovery in ComStock models.

Table 1. Building and Space Types in ComStock Modeled With Zone Exhaust Fans

| Building Type           | Space Type   |
|-------------------------|--------------|
| Full-Service Restaurant | Kitchen      |
| Hospital                | Kitchen      |
| Large Hotel             | Kitchen      |
| Outpatient              | Anesthesia   |
| Outpatient              | MRI          |
| Outpatient              | MRI Control  |
| Outpatient              | Soil Work    |
| Outpatient              | Toilet       |

| Building Type            | Space Type                        |
|--------------------------|-----------------------------------|
| Primary School           | Restroom                          |
| Primary School           | Kitchen                           |
| Primary School           | Kitchen                           |
| Quick-Service Restaurant | Kitchen                           |
| Secondary School         | Restroom                          |
| Secondary School         | Kitchen                           |
| Small Hotel              | Public Restroom                   |
| No Zone Exhaust Fans     | No Zone Exhaust Fans              |
| Retail                   | None                              |
| Retail Strip Mall        | None (except those with kitchens) |
| Small Office             | None                              |
| Medium Office            | None                              |
| Large Office             | None                              |
| Warehouse                | None                              |

Table 2. Fraction of ComStock Floor Area Conditioned by Systems With Heat/Energy Recovery by Building Type and Code Year. DEER stands for the Database of Energy Efficiency Resources, which is used to implement Title 24 energy codes in ComStock California models.

