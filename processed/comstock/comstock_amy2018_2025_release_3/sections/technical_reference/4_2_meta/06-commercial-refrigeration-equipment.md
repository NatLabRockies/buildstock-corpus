<!-- comstock comstock_amy2018_2025_release_3 | technical_reference | documentation/reference_doc/4_2_meta.tex | status: site_page | source_url: https://github.com/NatLabRockies/ComStock/blob/b77c60d341c9b68c58c5d51e51b06f08f293d3cb/documentation/reference_doc/4_2_meta.tex | publication_url: https://natlabrockies.github.io/ComStock.github.io/assets/files/comstock_reference_documentation_2025_3.pdf | corpus_version: 267e3ea | corpus_path: technical_reference/documentation/reference_doc/4_2_meta.md | section: Commercial Refrigeration Equipment | lines: 130-153 -->
## Commercial Refrigeration Equipment

<figure id="fig:refrigeration_survival_curves" data-latex-placement="ht!">
<img src="figures/refrigeration_survival_curves_combined.png" />
<figcaption>Weibull survival curves for commercial refrigeration equipment in large and small/medium grocery buildings.</figcaption>
</figure>

We represent commercial refrigeration equipment lifetimes using Weibull survival functions fit to effective useful lives (EULs) informed by the U.S. Department of Energy’s *Commercial Refrigeration Equipment* Technical Support Document (U.S. Department of Energy 2024). Consistent with the TSD’s market framing and industry practices, we differentiate between large grocery buildings (often owned or operated by national chains) and medium/small grocery buildings (more often independently owned).

For large groceries, we assume earlier replacement decisions driven by risk management, reliability requirements, and chain-wide retrofit programs that standardize fleets. We therefore assign a shorter EUL of 10 years. For medium and small groceries, where equipment is commonly retained until failure or when repair costs become prohibitive, we assign a longer EUL of 15 years. These assumptions align with the ownership and operations context underlying DOE’s CRE analyses and shipments modeling (U.S. Department of Energy 2024).

We parameterize shifted-Weibull survival functions such that (i) 50% survival occurs at the EUL (our operational definition of EUL), and (ii) a minimum lifespan threshold of roughly 60% of the EUL avoids unrealistic early whole-system failures. The resulting parameters are listed in Table <a href="#tab:refrigeration_eul_distributions" data-reference-type="ref" data-reference="tab:refrigeration_eul_distributions">4</a>. These distributions produce the combined survival curves shown in Figure <a href="#fig:refrigeration_survival_curves" data-reference-type="ref" data-reference="fig:refrigeration_survival_curves">4</a> and are used to schedule replacements and retirements in ComStock’s stock-turnover logic.

<div id="tab:refrigeration_eul_distributions">

| **EUL** | **Shape (beta)** | **Scale (alpha)** | **Shift (gamma)** |
|:-------:|:----------------:|:------------------|:------------------|
|   10    |      6.995       | 10.691            | 1.0               |
|   15    |      7.343       | 21.300            | 1.0               |

Commercial Refrigeration Equipment Weibull Distribution Parameters

</div>

