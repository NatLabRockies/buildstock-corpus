<!-- comstock 2025-3 | technical_reference | documentation/reference_doc/4_1_introduction.tex -->
# ComStock Building Models

ComStock uses about 30 high-level, whole-building characteristics to describe each building, as discussed in Section <a href="#chap:3_sampling" data-reference-type="ref" data-reference="chap:3_sampling">[chap:3_sampling]</a>. However, whole-building energy models, such as the EnergyPlus<sup>®</sup> model used by ComStock, typically require thousands of inputs to describe a building for simulation. The purpose of the subsequent sections is to describe the assumptions, conventions, and data sources used to transform the high-level descriptions into inputs with the level of detail needed by EnergyPlus. Although the software used to implement this transformation is critical to the workflow, the focus is on the model inputs, not on the software workflow.

One question that often arises is why more of the input assumptions documented in this section are not incorporated directly into the sampling framework described in Section <a href="#chap:3_sampling" data-reference-type="ref" data-reference="chap:3_sampling">[chap:3_sampling]</a>. This is an especially common question for those familiar with ResStock (Wilson et al. 2017), the residential building stock modeling tool that ComStock is based on. After all, ResStock uses more than 100 building characteristics to describe residential dwelling units, which are arguably less complex than commercial buildings. There are two main drivers behind the decision to limit the number of building characteristics: (1) handling complexity and (2) data availability for commercial buildings.

From a complexity standpoint, there is significantly more diversity among commercial buildings than among residential buildings. At one extreme, there are buildings like large hospitals, which may be several hundred thousand square feet, encompass spaces ranging from operating rooms to cafeterias, and be served by a complex array of HVAC systems. At the other extreme, there are buildings like small standalone retail stores, which may consist of just one retail space, a small storage room, and a restroom. Accounting for the diversity in lighting power density for each space type across all commercial building types in ComStock would alone require more than 100 building characteristics, many of which would not be applicable for certain building types. Multiply this by the number of characteristics that vary between building types, and the number of building characteristics required quickly becomes untenable.

From a data availability standpoint, there is simply much less information available for commercial buildings than there is for residential buildings. This means that modeling the commercial building stock requires more assumptions than modeling the residential building stock. Compounding this lack of data is the fact that most commercial building data sources handle complexity by focusing on a single building type (e.g., offices), providing information only at the whole-building level, or providing percentages of floor area associated with a given characteristic. Rather than making engineering estimates to generate probability distributions for every building characteristic, we have chosen to make point estimates for certain parameters. Proponents of stochastic modeling may disagree with this approach, but we believe it is warranted, given the model complexity that is avoided.

The end result is that many of the intra-building characteristics of commercial buildings must be inferred from whole-building characteristics. Rather than adding these to the input layer, they are set in the process that expands these whole-building characteristics into energy model inputs.

<div id="refs" class="references csl-bib-body hanging-indent">

<div id="ref-resstock" class="csl-entry">

Wilson, Eric J., Craig B. Christensen, Scott G. Horowitz, Joseph J. Robertson, and Jeffrey B. Maguire. 2017. *Energy Efficiency Potential in the u.s. Single-Family Housing Stock*. National Renewable Energy Laboratory. <https://doi.org/10.2172/1414819>.

</div>

</div>
