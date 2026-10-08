<!-- comstock comstock_amy2018_2025_release_3 | technical_reference | documentation/reference_doc/2_workflow.tex | status: site_page | source_url: https://github.com/NatLabRockies/ComStock/blob/b77c60d341c9b68c58c5d51e51b06f08f293d3cb/documentation/reference_doc/2_workflow.tex | publication_url: https://natlabrockies.github.io/ComStock.github.io/assets/files/comstock_reference_documentation_2025_3.pdf | corpus_version: fadc83e | corpus_path: technical_reference/documentation/reference_doc/2_workflow.md | section: ComStock Workflow | lines: 2-22 -->
# ComStock Workflow

Accurately representing commercial building energy usage is complex because of how subsystems of a building interact with one another and with the surrounding environment. Every aspect of a commercial building can influence its energy consumption, so it is difficult to identify which aspects of a building are critical for a given energy-related metric and climate without simulation. To achieve its fundamental goal of representing the U.S. commercial building stock across all energy-related metrics, ComStock must capture the diversity and variability of the building stock. This requires a robust modeling and publishing workflow.

At the heart of ComStock are the approximately 350,000 building energy models (BEMs) that collectively represent the commercial building stock in the United States (roughly 6 million buildings). These models do not represent specific individual buildings (for example, there is no ComStock model for the Empire State Building). Modeling individual buildings would be impractical given the difficulty of compiling accurate data on the U.S. building stock at a national scale. Identifying distributions of characteristics is a more tractable problem. For example, the EIA’s Commercial Buildings Energy Consumption Survey (CBECS) (U.S. Energy Information Administration 2012) provides information on how many buildings by type have specific heating, ventilating, and air-conditioning (HVAC) system characteristics (e.g., an office building with a chiller). Combining this information with a building’s size and when and where it was built has allowed the ComStock team to develop statistical distributions that determine the characteristics for each of the 350,000 models.

Creating and running the 350,000 BEMs that lie at the heart of ComStock—and then sharing the results—requires significant infrastructure. The workflow that defines, executes, and post-processes these BEMs is shown in Figure <a href="#fig:comstock_workflow" data-reference-type="ref" data-reference="fig:comstock_workflow">1.1</a>. The remainder of this section contains an abridged discussion of the elements of this workflow and their role in creating the ComStock BEMs and the results data set. Each aspect of the workflow is revisited in detail in Section 4 as modeling assumptions and algorithms are discussed.

<figure id="fig:comstock_workflow" data-latex-placement="h!">
<img src="figures/comstock_workflow.png" />
<figcaption>Flowchart of the ComStock workflow.</figcaption>
</figure>

ComStock accomplishes its goal of accurately representing the U.S. building stock through a three-part workflow process:

1.  ComStock creates samples that represent the U.S. commercial building stock.

2.  These samples are translated into BEMs and modified to represent either the baseline U.S. commercial building stock or an altered version thereof (i.e., modeling the impact of an efficiency or electrification measure).

3.  The physics-based BEMs are evaluated through an energy simulation engine that uses high-performance computing to simulate each model. The resulting data are made available to a wide range of stakeholders.

