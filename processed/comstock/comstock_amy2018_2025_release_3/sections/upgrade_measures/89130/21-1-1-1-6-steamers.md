<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/89130.pdf | status: osti_pdf | source_url: https://www.nlr.gov/docs/fy24osti/89130.pdf | publication_url: https://www.nlr.gov/docs/fy24osti/89130.pdf | corpus_version: fadc83e | corpus_path: upgrade_measures/measure_pdfs/89130.md | section: 1.1.1.6  Steamers | lines: 500-552 -->
## 1.1.1.6  Steamers

The last type of cooking equipment modeled in ComStock is commercial steamers. There are two main types of steamers: atmospheric (pressure-less) steamers and pressure steamers.

Atmospheric steamers can cook larger volumes of food and therefore may be more suitable for commercial kitchens, so this is what our model assumes.

Figure 6. Typical commercial atmospheric steamer [8]

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/89130.yaml
     source: 89130_images/image_000015_8ab194fb619557cbdb82535a2e448de47a21d681f9d4ab13fa49d0e40d0ae874.png
     method: vision-description
     described: 2026-08-21 -->

![Annotated photograph of a commercial atmospheric steamer labeling its compartments and boiler](89130_images/image_000015_8ab194fb619557cbdb82535a2e448de47a21d681f9d4ab13fa49d0e40d0ae874.png)

Figure 6: annotated photograph of a typical commercial atmospheric steamer - two stacked steam compartments above a cabinet, with arrows labeling "Steam Compartments" and "Boiler". Reproduced from reference 8. Tables 11 and 12 give steamer rated input power and commercially available specifications; Section 1.1.1.6 notes ASHRAE's values run well below the other three sources.

Table 11 shows the rated input assumptions from the four sources. Notably, the ASHRAE values are substantially lower than the other three sources, which has not been the case with any other appliances.

Table 11. Comparison of Steamer Rated Input Power from Four Sources

| Source                           | Gas (Btu/h)     | Electric (Btu/h)   |
|----------------------------------|-----------------|--------------------|
| 2015 DOE Report [8]              | 210,000         | 81,891             |
| FSTC 2002 [9]                    | 170,000-250,000 | 61,000-123,000     |
| ASHRAE 2017 [6]                  | 26,000          | 33,400             |
| PG&E Production Test Kitchen [7] | 200,000         | 92,000             |

We researched commercial atmospheric steamers to determine if the power values were more aligned with ASHRAE or the other three sources.

Table 12. Specifications of Commercially Available Gas and Electric Steamers [10]

<!-- table recovered from 89130_images/image_000016_2b0ca833fda5b20e1f093f6a3f063fc426ceb3c1280268be4769a202d7f7edf9.png
     overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/89130.yaml
     method: pdf-text-layer (values) + vision-transcription (product names) -->

| Image | Cleveland 24-CGM-200 Classic Series Natural Gas 6 Pan Convection Floor | Cleveland 24-CGP-10 SteamCraft Power Natural Gas 10 Pan Floor Convection |
|---|---|---|
| Fuel | Gas | Gas |
| Rated Input (Btu/h) | 200,000 | 240,000 |

| Image | Cleveland (2) 22CET3.1 SteamChef 3 Double Deck 6 Pan Electric Floor Steamer - | Cleveland 24CEA10 SteamCraft Gemini 10 Pan Electric Floor Steamer - 240V, |
|---|---|---|
| Fuel | Electric | Electric |
| Rated Input (kW) | 24 | 32 |
| Rated Input (Btu/h) | 81,900 | 109,000 |

All four product names are cut off mid-phrase in the source and are transcribed as printed. Each header cell also carries a product photograph and a fuel or voltage badge ("NATURAL GAS", "240 VOLTS"); neither is transcribed.

Based on the commercially available products we found, the rated input power values align much more closely with the DOE, FSTC, and PG&amp;E sources than with ASHRAE. We concluded that the ASHRAE Fundamentals source must be assuming a much smaller steamer model or a different type of steamer product, because the values are several times lower than the other three sources. Therefore, we have chosen for this appliance to use the PG&amp;E source as the basis for our rated power assumptions. While the DOE and PG&amp;E values were close in magnitude, the PG&amp;E values assumed a more conservative efficiency improvement from gas to electric, so we selected this one to avoid overestimating savings in our results. Therefore, the gas and electric steamer rated input power values are assumed to be 200,000 Btu/h and 92,000 Btu/h, respectively.

The ENERGY STAR Product Finder [14] contains product specifications for commercial steamers that list cooking efficiency for various gas and electric steamers. Five products of each fuel type were selected, and the average cooking efficiencies were calculated. For gas steamers, the average efficiency was 46%, whereas for electric, the average efficiency was 68%. This means that electric steamers are about 54% more efficient on average compared to gas steamers. The rated input values we selected-200,000 Btu/h for gas and 92,000 Btu/h for electricrepresent an electric steamer that is 48% more efficient than its gas counterpart. This efficiency difference aligns closely with the ENERGY STAR products, further validating that our rated power assumptions are reasonable. Once again, we feel comfortable using the slightly more conservative efficiency assumption to avoid overestimating savings.

