<!-- comstock comstock_amy2018_2025_release_3 | technical_reference | documentation/reference_doc/4_4_geometry.tex | status: site_page | source_url: https://github.com/NatLabRockies/ComStock/blob/b77c60d341c9b68c58c5d51e51b06f08f293d3cb/documentation/reference_doc/4_4_geometry.tex | publication_url: https://natlabrockies.github.io/ComStock.github.io/assets/files/comstock_reference_documentation_2025_3.pdf | corpus_version: 0a2f61f | corpus_path: technical_reference/documentation/reference_doc/4_4_geometry.md | section: Window-to-Wall Ratio (WWR) | lines: 97-119 -->
## Window-to-Wall Ratio (WWR)

The ComStock window-to-wall ratio (WWR) assumptions were created as part of the EULP project. WWR is defined as the fraction of abovegrade wall area that is covered by fenestration. Previously, ComStock used the WWR from the DOE prototype building models. Although each building type had a different WWR, there was no variability within each building type, which is not representative of the building stock. To address this issue, we referenced the NFRC Commercial Fenestration Market Study conducted by Guidehouse (Ciraulo et al. 2021). The study characterized the national commercial window stock through data collection and analysis. Six primary data sources representing all regions of the United States were used in the study—a 2020 Guidehouse survey, NEEA CBSA, DOE Code Study, CAEUS, CBECS, and RECS (multifamily). A variety of window properties were collected, including WWR, number of panes, frame material, glazing type, low-emissivity coating, gas fill, and many others. In total, the database contained approximately 16,000 samples, each with an appropriate weighting factor based on the coverage, completeness, and fidelity of each data source. We incorporated the WWR results from this study into the ComStock model, and we may incorporate other fields in the future to further refine our window modeling methodology.

From the Guidehouse data, we developed a WWR distribution for each combination of building type, floor area, and vintage. We first analyzed the WWRs separately by building type, floor area, geographic location, and vintage to determine which filters were appropriate to use for the final distributions. Geographic location did not have a significant impact on WWR, so it was left out of the final distributions. As can be seen in Figures “Window-to-wall ratio by rentable floor area.” and “Window-to-wall ratio by building vintage.”, there is a noticeable change in the WWR of buildings built after 2014, indicating that new buildings are trending toward larger windows. Similarly, there is a distinct trend in the WWR as a function of floor area; larger buildings tend to have more windows. Whereas the previous methodology only varied WWR by building type, these new distributions introduce more WWR variability by considering vintage and floor area.

The WWR distributions for all buildings before and after incorporating the NFRC data are shown in Figure “Window-to-wall ratio distribution in all building types before and after incorporating NFRC data.”. The distinct bins in the graph are a result of the way WWR is binned in the CBECS Show Card: 0%–1% WWR is binned to 0.0, 2%–10% to 0.06, 11%–25% to 0.18, 26%–50% to 0.38, 51%–75% to 0.63, and 76%–100% to 0.88. The final distributions do not change the stock total energy consumption significantly, but they do add realistic variability within building types. For example, previously, all large offices had the same WWR of 0.15, whereas using the new distributions, large office WWRs vary from 0.01 to 0.88.

<figure id="fig:wwr_by_rentable_area" data-latex-placement="h">
<img src="figures/wwr_by_rentable_area.png" />
<figcaption>Window-to-wall ratio by rentable floor area.</figcaption>
</figure>

<figure id="fig:wwr_by_building_vintage" data-latex-placement="h">
<img src="figures/wwr_by_building_vintage.png" />
<figcaption>Window-to-wall ratio by building vintage.</figcaption>
</figure>

<figure id="fig:wwr_before_after_all_buildings" data-latex-placement="h!">
<img src="figures/wwr_before_after_all_buildings.png" />
<figcaption>Window-to-wall ratio distribution in all building types before and after incorporating NFRC data.</figcaption>
</figure>

