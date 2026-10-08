<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/89239.pdf | status: osti_pdf | source_url: https://www.nlr.gov/docs/fy24osti/89239.pdf | publication_url: https://www.nlr.gov/docs/fy24osti/89239.pdf | corpus_version: fadc83e | corpus_path: upgrade_measures/measure_pdfs/89239.md | section: 3.3  GHEDesigner Workflow | lines: 363-398 -->
## 3.3  GHEDesigner Workflow

GHEDesigner is a Python package for designing ground heat exchangers used with geothermal heat pump systems [17]. The geothermal heat pump upgrade measures leverage GHEDesigner for sizing the vertical ground heat exchangers used in the ComStock models. GHEDesigner is called and runs within the GHP measures. Figure 3 shows the full ComStock GHP measure workflow. First, the GHP measure is applied, which replaces the existing system with one of the GHP configurations. An initial sizing run determines the annual loads the ground heat exchanger needs to supply. The ground loads are exported to GHEDesigner in the form of a JavaScript Object Notation (JSON) file. GHEDesigner runs calculations to determine the g-function, which is used to size the ground heat exchanger in the model. A final simulation is run with the ground heat exchanger sized to the full building load. Each step is described in more detail below.

Figure 3. ComStock GHEDesigner workflow

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/89239.yaml
     source: 89239_images/image_000009_8e3b0eeb1669b4b0ca6da3e26c5fac81b5feda84d326e1b58b63960915dfb524.png
     method: vision-description
     described: 2026-08-21 -->

![Flow diagram of the ComStock GHEDesigner workflow from measure application to final simulation](89239_images/image_000009_8e3b0eeb1669b4b0ca6da3e26c5fac81b5feda84d326e1b58b63960915dfb524.png)

Figure 3: left-to-right flow diagram inside a ComStock simulation banner. Applying the measure to retrofit the existing system with GHP feeds initial load calculations, which pass hourly ground loads for borefield sizing to the external GHEDesigner tool; GHEDesigner returns a g-function for the ground heat exchanger to the final simulation. Section 3.3 describes each step.

First, the GHP measure is applied. As part of the GHP retrofit, a ground loop is added to the model where the ground heat exchanger will be installed. To properly size the ground heat exchanger, the GHEDesigner tool needs to know the building's hourly heating and cooling loads for the entire year. To achieve this, a temporary 'dummy' ground heat exchanger is added to the ground loop in the form of a PlantComponent:TemperatureSource object.

The temperature source object regulates the water supply temperature to meet the building demand for every hour of the annual simulation. In turn, this object outputs the hourly heating and cooling loads to be met by the ground heat exchanger. By passing the ground loads directly from the ComStock initial sizing run, we are inherently sizing the ground heat exchanger to meet the entire building load with the GHP. In other words, we are sizing to the larger of the heating or cooling loads. Other sizing approaches, such as sizing to the smaller load and providing supplemental heating or cooling, could be used to attempt to minimize the size of the borefield. However, this workflow currently sizes the heat pumps to meet the full building load. The hourly loads are exported to a JSON file, and the GHEDesigner Python package is called within the measure.

In addition to the hourly ground loads, the JSON file contains assumptions related to borefield and soil properties. Table C-1 in Appendix C summarizes the GHEDesigner input assumptions used by the ComStock model and gives a brief description or justification of why that assumption was selected. Some of the inputs are GHEDesigner recommended defaults while others are modified from the default values for this application. Internal and external subject matter experts were consulted to ensure reasonable assumptions. In addition, the ComStock team worked closely with other ongoing GHP projects to align assumptions where possible across modeling efforts.

One important reminder is that ComStock is a representative model of the U.S. commercial building stock, not a model of specific buildings. GHP and borefield design can be site-specific and include soil properties, land constraints, etc. However, the ComStock model has limited geographic integrity below the county level and does not have site-specific data for every location to inform custom design choices. Therefore, some assumptions must be made more broadly across climate zones or nationally. The assumptions for undisturbed ground temperatures and soil conductivity are summarized in Table C-2 and Figure C-1 in Appendix C.

When the GHEDesigner tool receives the JSON file, it uses the properties and hourly loads to size the borefield and generate a g-function. Temperature response functions, known as gfunctions, are a computationally efficient method for simulating ground heat exchangers, used with GHP systems, either as part of a whole-building energy simulation or as part of a dedicated ground heat exchanger design tool [18]. GHEDesigner sends a JSON file back to the ComStock simulation containing the key parameters such as number of boreholes, borehole length and radius, ground properties, and g-function values. The ComStock measure then replaces the temporary 'dummy' ground heat exchanger object with an actual vertical ground heat exchanger object. The measure parses the information from the JSON and inputs it into the GroundHeatExchanger:Vertical object. The annual simulation is then rerun with the new configuration. This second annual run generates the results that are used for analysis. Figure 4 shows an example illustration of the full workflow.

Figure 4. Example plant loop configuration showing location of ground loop and temperature source/vertical ground heat exchanger object

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/89239.yaml
     source: 89239_images/image_000010_e572c47fbf894622447d271dccdf1ceddae178a9826377ccb75649a05958c7aa.png
     method: vision-description
     described: 2026-08-21 -->

![Paired plant-loop diagrams contrasting a temperature-source object with a vertical ground heat exchanger](89239_images/image_000010_e572c47fbf894622447d271dccdf1ceddae178a9826377ccb75649a05958c7aa.png)

Figure 4: side-by-side EnergyPlus plant-loop diagrams of the same three-loop arrangement, the left version using a PlantComponent:TemperatureSource object and the right a vertical ground heat exchanger. Plant Loop 1 links heat pump to borefield heat exchanger, Loop 2 heat pump to heat exchanger, and Loop 3 heat exchanger to heating coils. Labeled arrows show timeseries ground loads into and the g-function out of GHEDesigner.

