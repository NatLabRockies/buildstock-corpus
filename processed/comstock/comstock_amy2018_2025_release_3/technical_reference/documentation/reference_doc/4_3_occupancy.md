<!-- comstock 2025-3 | technical_reference | documentation/reference_doc/4_3_occupancy.tex -->
# Hours of Operation and Occupancy

## Hours of Operation

### Overview

Hours of operation are added to the model using operation start time and duration inputs. The start times and durations are assigned to each model through the sampling process using a set of distributions based on building type. They are then further broken down by weekday and weekend (Figure <a href="#fig:start_time" data-reference-type="ref" data-reference="fig:start_time">1</a> and Figure <a href="#fig:duration" data-reference-type="ref" data-reference="fig:duration">2</a>). When applied to the model, the start time and duration are used to establish operating hour start and end times. These times are used to adjust the other schedules in the model (e.g., lighting, thermostat). This is achieved by stretching or shrinking the schedule on the temporal axis to align all schedules with the operating hours for the model. Note that because the weekday and weekend start times and durations are sampled independently, they are not aligned in a given building model.

### Hours of Operation Derivation

We derived the hours of operation by applying the method introduced in (Bianchi et al. 2020) to 1 year of AMI data from 6,070 buildings spread across eight utilities (the commercial schedules AMI data set). We first extracted the two-dimensional distribution of *High Load Start Time* and *High Load Duration* from this AMI data set, as an approximation of the schedule of hours of operations for each building type. Then, we compared this distribution with the inputs of ComStock at the start of the [End-Use Load Profiles](https://www.nrel.gov/buildings/end-use-load-profiles.html) (EULP) calibration.

Figure <a href="#fig:utility_building_type" data-reference-type="ref" data-reference="fig:utility_building_type">[fig:utility_building_type]</a> lists the number of buildings for each building type from each utility’s AMI data set that was considered during the EULP project. The utility data sets and names are listed in Table 10 of the EULP Final Technical Report (Wilson et al. 2022). Among the 15 building types considered in ComStock, 14 can be found in the commercial schedules AMI data set. The only exception is secondary schools, because all schools were grouped together in the AMI data.

We compared the distribution extracted from the commercial schedules AMI data set with the inputs of ComStock at the start of the EULP calibration. The results of the small office building type are presented in Figure <a href="#fig:small_office_season" data-reference-type="ref" data-reference="fig:small_office_season">[fig:small_office_season]</a> to illustrate the process, because this building type has the largest sample size in the AMI data set. We considered two day types, working day vs. non-working day, and two season definitions—one defined by month, and the other defined by daily average outdoor air temperature. The distribution of hours of operation is more diffuse in the AMI data set than in the ComStock inputs at the start of EULP calibration. Also, the duration of high load is smaller in the real AMI data than in the previous ComStock assumptions.

We explored whether and how the hours of operation are influenced by season (in Figure <a href="#fig:small_office_season" data-reference-type="ref" data-reference="fig:small_office_season">[fig:small_office_season]</a>) and by utility (in Figure <a href="#fig:small_office_utility" data-reference-type="ref" data-reference="fig:small_office_utility">[fig:small_office_utility]</a>). Some differences can be observed; however, due to the modeling complexity and the desire to create a nationally applicable approach that avoids overfitting to a specific utility region, we combined the AMI data across seasons and utilities to generate a distribution of hours of operation for each building type. These new distributions were applied to ComStock in place of the existing distributions.

## Occupancy

### Occupancy Density

Occupants are assigned to individual space types as an occupancy density (people/1000 ft<sup>2</sup>). This value, when multiplied by the total zone floor area, determines the maximum number of people in a zone. show the occupancy densities for all space types included in ComStock.

The majority of the ComStock occupancy density values are from the DOE prototype models. These are derived primarily from ASHRAE 62.1-2004 (ASHRAE 2004), with some space type densities originating from the International Building Code 2003 (International Code Council 2003). Prototype hotel guest rooms were assumed to have 1.5 occupants each, and occupancy rates for the two hotel models were assumed to be 65% to align with the industry average occupancy rate and (Jiang et al. 2008). Rooms were randomly assigned occupants so that 65% of the rooms were occupied. Most of the DOE prototype hospital and outpatient space type occupancy densities were replaced with values from the 2007 Green Guide for Healthcare (GGHC), which includes typical occupancy densities for healthcare space types (Healthcare 2007).

### Occupancy Schedules

The maximum number of people in a zone (calculated from occupancy density and zone floor area) is multiplied by an hourly occupancy schedule with values ranging from zero to one to capture the variation in building occupancy throughout the day. Figures <a href="#fig:occupancy_schedules_1" data-reference-type="ref" data-reference="fig:occupancy_schedules_1">3</a> and <a href="#fig:occupancy_schedules_2" data-reference-type="ref" data-reference="fig:occupancy_schedules_2">4</a> show the national base occupancy schedules used in ComStock, broken down by building type. For the California occupancy schedules, please see figures <a href="#fig:occupancy_schedules_deer_1" data-reference-type="ref" data-reference="fig:occupancy_schedules_deer_1">[fig:occupancy_schedules_deer_1]</a> and <a href="#fig:occupancy_schedules_deer_2" data-reference-type="ref" data-reference="fig:occupancy_schedules_deer_2">[fig:occupancy_schedules_deer_2]</a> in the Appendix. For buildings in all states except California, the base schedules are the DOE prototype occupancy schedules. California uses schedules from DEER prototype models (California Public Utilities Commission 2021). The DOE prototype documentation (Deru et al. 2011) notes that there are few data sources that provide operating schedules for use in building energy simulations. Thus, the schedules in the prototype models were derived from two primary data sources: the Advanced Energy Design Guide Technical Support Documents (Jiang et al. 2008; Bonnema et al. 2010; Liu et al. 2007; Pless et al. 2007) and ASHRAE 90.1-1989 Section 13 (ASHRAE 1989). These schedules were then modified to account for real-world building operation, based on the experience of the engineers who created the DOE prototype models. Classroom occupancy schedules for primary and secondary schools were adjusted by factors of 0.75 and 0.70, respectively, to meet the student numbers documented in (Pless et al. 2007). Table <a href="#tab:occupancy_schedule_source" data-reference-type="ref" data-reference="tab:occupancy_schedule_source">[tab:occupancy_schedule_source]</a> lists the data sources for occupancy schedules in each of the prototype buildings (both DOE and DEER). Occupancy schedules in ComStock buildings are further adjusted so that the total daily occupancy in the building stock does not exceed the average daily occupancy of the United Stated building stock as derived from analysis of locations in the American Time Use Survey (U.S. Bureau of Labor Statistics (BLS) 2018) Activity file. This adjustment applies a 23% reduction factor to all occupant schedule values, resulting in a peak daily total occupancy in ComStock models of approximatly 115M people.

These base occupancy schedules are stretched, compressed, or shifted in time to reflect the model’s assigned hours of operation. For example, the base occupancy schedule for large offices is 9 a.m.–5 p.m. (8 hours of operation). If one large office model is assigned a start time of 8 a.m. and an operating duration of 10 hours, the base schedules in the model will be stretched so that the occupied period is an additional two hours long. All schedules in the model (occupancy, lighting, thermostat, plug load, etc.) are modified in the same manner to ensure coordination between occupancy, lighting, etc.

### Occupancy Activity Schedules

Occupancy activity schedules represent the total heat gain per person, including convective, radiant, and latent heat. An internal EnergyPlus algorithm determines the fraction of the total load that is sensible and latent. The sensible portion is further divided into radiant and convective using the default fraction radiant value. DOE prototype activity levels are fixed for a given building type and range from 120-132 watts per person across the various building types. DEER prototype activity levels vary by space type and range from 117-331 watts per person. Table <a href="#tab:activity_schedule" data-reference-type="ref" data-reference="tab:activity_schedule">[tab:activity_schedule]</a> lists the occupancy activity schedules used in ComStock.

<figure id="fig:start_time">
<img src="figures/start_time.png" style="width:100.0%" />
<figcaption>Operating hours’ start time distributions.</figcaption>
</figure>

<figure id="fig:duration">
<img src="figures/duration.png" style="width:100.0%" />
<figcaption>Operating hours’ duration distributions.</figcaption>
</figure>

<figure id="fig:occupancy_schedules_1">
<img src="figures/occupancy_schedules_1.png" style="width:90.0%" />
<figcaption>National base occupancy schedules for food service, lodging, healthcare, and education ComStock building types, excluding California. See Figure <a href="#fig:occupancy_schedules_deer_1" data-reference-type="ref" data-reference="fig:occupancy_schedules_deer_1">[fig:occupancy_schedules_deer_1]</a> for California.</figcaption>
</figure>

<figure id="fig:occupancy_schedules_2">
<img src="figures/occupancy_schedules_2.png" style="width:90.0%" />
<figcaption>National base occupancy schedules for retail, office, and warehouse ComStock building types, excluding California. See Figure <a href="#fig:occupancy_schedules_deer_2" data-reference-type="ref" data-reference="fig:occupancy_schedules_deer_2">[fig:occupancy_schedules_deer_2]</a> for California.</figcaption>
</figure>

<div id="refs" class="references csl-bib-body hanging-indent">

<div id="ref-ashrae_1989" class="csl-entry">

ASHRAE. 1989. *Energy Efficient Design of New Buildings Except Low-Rise Residential Buildings*. <a href="https://ashrae.iwrapper.com/ASHRAE_PREVIEW_ONLY_STANDARDS/STD_90.1_1989" class="uri">Https://ashrae.iwrapper.com/ASHRAE_PREVIEW_ONLY_STANDARDS/STD_90.1_1989</a>.

</div>

<div id="ref-ashrae_62.1_2004" class="csl-entry">

ASHRAE. 2004. *Ventilation for Acceptable Indoor Air Quality*. <a href="https://ashrae.iwrapper.com/ASHRAE_PREVIEW_ONLY_STANDARDS/STD_62.1_2019" class="uri">Https://ashrae.iwrapper.com/ASHRAE_PREVIEW_ONLY_STANDARDS/STD_62.1_2019</a>.

</div>

<div id="ref-bianchi2020modeling" class="csl-entry">

Bianchi, Carlo, Liang Zhang, David Goldwasser, Andrew Parker, and Henry Horsey. 2020. “Modeling Occupancy-Driven Building Loads for Large and Diversified Building Stocks Through the Use of Parametric Schedules.” *Applied Energy* 276: 115470.

</div>

<div id="ref-doebber_2009" class="csl-entry">

Bonnema, B, I Doebber, S Pless, and P Torcellini. 2010. *Technical Support Document: Development of the Advanced Energy Design Guide for Small Hospitals and Healthcasre-30% Energy Savings*. NREL/TP-550-46314. National Renewable Energy Laboratory. <https://www.nrel.gov/docs/fy10osti/46314.pdf>.

</div>

<div id="ref-cpuc_deer" class="csl-entry">

California Public Utilities Commission. 2021. *Database for Energy Efficient Resources*. <a href="http://deeresources.com/" class="uri">Http://deeresources.com/</a>.

</div>

<div id="ref-deru_2011" class="csl-entry">

Deru, M, K Field, D Studer, et al. 2011. *U.s. Department of Energy Commercial Reference Building Models of the National Building Stock*. NREL/TP-5500-46861. National Renewable Energy Laboratory. <https://www.nrel.gov/docs/fy11osti/46861.pdf>.

</div>

<div id="ref-gghc_2007" class="csl-entry">

Healthcare, Green Guide for. 2007. *Green Guide for Healthcare: Best Practices for Creating High Performance Healing Environments*. <a href="http://www.gghc.org" class="uri">Http://www.gghc.org</a>.

</div>

<div id="ref-icc_2003" class="csl-entry">

International Code Council. 2003. *2003 International Building Code*. <a href="https://codes.iccsafe.org/content/IBC2018?site_type=public" class="uri">Https://codes.iccsafe.org/content/IBC2018?site_type=public</a>.

</div>

<div id="ref-jiang_2008" class="csl-entry">

Jiang, Wei, Ronald E Jarnagin, Krishnan Gowri, M McBride, and Bing Liu. 2008. *Technical Support Document: The Development of the Advanced Energy Design Guide for Highway Lodging Buildings*. PNNL-17875. Pacific Northwest National Laboratory. <https://www.pnnl.gov/main/publications/external/technical_reports/pnnl-17875.pdf>.

</div>

<div id="ref-liu_2007" class="csl-entry">

Liu, B, R. E Jarnagin, W Jiang, and K Gowri. 2007. *Technical Support Document the Development of the Advanced Energy Design Guide for Small Warehouse and Self-Storage Buildings*. PNNL-17056. Pacific Northwest National Laboratory. <https://www.pnnl.gov/main/publications/external/technical_reports/PNNL-17056.pdf>.

</div>

<div id="ref-pless_2007" class="csl-entry">

Pless, S, P Torcellini, and N Long. 2007. *Technical Support Document: Development of the Advanced Energy Design Guide for k-12 Schools-30% Energy Savings*. NREL/TP-550-42114. National Renewable Energy Laboratory. <https://www.nrel.gov/docs/fy07osti/42114.pdf>.

</div>

<div id="ref-atus2018" class="csl-entry">

U.S. Bureau of Labor Statistics (BLS). 2018. *American Time Use Survey (ATUS), 2018*. Https://www.bls.gov/tus/.

</div>

<div id="ref-eulp_final_report" class="csl-entry">

Wilson, Eric J. H., Andrew Parker, Anthony Fontanini, et al. 2022. *End-Use Load Profiles for the u.s. Building Stock: Methodology and Results of Model Calibration, Validation, and Uncertainty Quantification*. National Renewable Energy Laboratory. <https://doi.org/10.2172/1854582>.

</div>

</div>
