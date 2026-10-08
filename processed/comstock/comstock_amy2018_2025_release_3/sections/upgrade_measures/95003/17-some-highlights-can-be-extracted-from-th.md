<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/95003.pdf | status: osti_pdf | source_url: https://docs.nlr.gov/docs/fy25osti/95003.pdf | publication_url: https://docs.nlr.gov/docs/fy25osti/95003.pdf | corpus_version: 0a2f61f | corpus_path: upgrade_measures/measure_pdfs/95003.md | section: Some highlights can be extracted from the gathered data: | lines: 308-365 -->
## Some highlights can be extracted from the gathered data:

- As shown in Figure 3 ( x -axis is in log scale), compared to air-cooled chillers, water-cooled chillers are more suitable for applications serving larger loads. Also, air-cooled chillers are ready to use off the shelf, as their condenser is integrated into the unit. In contrast, watercooled chillers require connection to a separate condenser.
- Scroll compressors are used in smaller applications (and are more common for air-cooled chillers) compared to screw and centrifugal compressors. Centrifugal compressors are used in the larger end of the applications and are more common for water-cooled chillers. This is reflected in Figure 3. To note, IPLV values were not available for water-cooled chillers using centrifugal compressors as shown in Figure 3.
- Water-cooled chillers have relatively higher EER values (for both full-load and part-load conditions) compared to air-cooled chillers, as they are leveraging a cooling tower. This is reflected in Figure 4. It is also important to note that when comparing the rated efficiencies of different types of chillers, the rating conditions vary due to differences in condenser fluids and temperatures.

Figure 3. Chiller performance comparison: compressor types

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/95003.yaml
     source: 95003_images/image_000004_e2cf4edbc5238219892d94e8565734432495da68c9c231ce1000a4a21a52cf6e.png
     method: vision-description
     described: 2026-08-21 -->

![Paired scatter plots of full-load EER and IPLV EER versus rated cooling capacity by compressor type](95003_images/image_000004_e2cf4edbc5238219892d94e8565734432495da68c9c231ce1000a4a21a52cf6e.png)

Figure 3: two scatter panels comparing chiller performance by compressor type - full-load EER at left, EER of IPLV at right - both against rated cooling capacity in tons on a log x-axis. Series are air-cooled scroll, air-cooled screw, and water-cooled centrifugal. Water-cooled centrifugal units cluster highest, roughly 21-26 full-load EER above 300 tons, while air-cooled units sit near 8-11. Table A-1 lists the underlying data.

Figure 4. Chiller performance comparison: air-cooled versus water-cooled

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/95003.yaml
     source: 95003_images/image_000005_09c3d3de95563d24b48befdfe948a2361d85a52cb903665ff3106c29015899ca.png
     method: vision-description
     described: 2026-08-21 -->

![Paired scatter plots of full-load and IPLV EER, air-cooled versus water-cooled scroll chillers](95003_images/image_000005_09c3d3de95563d24b48befdfe948a2361d85a52cb903665ff3106c29015899ca.png)

Figure 4: two scatter panels comparing air-cooled and water-cooled scroll chillers using R-410A, plotting full-load EER (left) and EER of IPLV (right) against rated cooling capacity from 0 to 250 tons. Water-cooled units run consistently higher in both metrics, about 16 versus 11 at full load, and their IPLV advantage widens with capacity. Table A-1 holds the gathered specifications.

- Chiller efficiencies at rated conditions are lower than those of part-load conditions, as IPLVs reflecting more weights on part-load conditions are higher than full-load EER values. This is reflected in Figure 4. Also, in real building applications, chillers are operated more often under part-load conditions.
- There are some products with either standard-efficiency or high-efficiency nameplate. Highefficiency products show better performance on part-load conditions (reflected with IPLV) rather than on rated/full-load conditions (reflected with full-load EER). This is reflected in Figure 5. These high-efficiency products commonly include variable-speed compressors that often operate more efficiently under part-load conditions.

Figure 5. Chiller performance comparison: manufacturer specs (standard/high efficiency) versus ComStock baseline for air-cooled chillers

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/95003.yaml
     source: 95003_images/image_000006_bc280251e57a3d1367df0eff29343c760aa6a85a0a619681dd21451c554d63b9.png
     method: vision-description
     described: 2026-08-21 -->

![Paired scatter plots of air-cooled chiller EER: standard and high-efficiency specs versus baseline](95003_images/image_000006_bc280251e57a3d1367df0eff29343c760aa6a85a0a619681dd21451c554d63b9.png)

Figure 5: two scatter panels for air-cooled chillers plotting full-load EER (left) and EER of IPLV (right) against rated cooling capacity up to about 560 tons, with three series - manufacturer standard efficiency, manufacturer high efficiency, and the ComStock baseline. The few ComStock baseline points sit at or below the standard-efficiency cloud, most visibly in IPLV near 9-13 against high-efficiency values around 18-21.

- Full-load EER and IPLV EER values applied in ComStock baseline models are slightly less efficient than performances gathered from the latest manufacturer specification datasheets. This is reflected in Figure 5 (for air-cooled chillers) and Figure 6 (for water-cooled chillers). Some water-cooled chillers only included full-load EER and not IPLV EER, thus only providing half of the information, as reflected in Figure 6. ComStock baseline values in these figures are extracted and slightly simplified (i.e., using averaged capacity instead of min/max range values) from the ComStock Reference Documentation [4]. And as shown in Figure 6, full-load EER of the upgrade chiller (e.g., 24) can be twice as efficient as some low-end baseline full-load EER values (e.g., 12).

Figure 6. Chiller performance comparison: manufacturer specs versus ComStock baseline for water-cooled chillers

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/95003.yaml
     source: 95003_images/image_000007_8c9f85455bd0f1407503f355f666d4da9aa560ad1a92b3367cb57ea51d341f71.png
     method: vision-description
     described: 2026-08-21 -->

![Paired scatter plots of water-cooled chiller EER, manufacturer specs versus ComStock baseline](95003_images/image_000007_8c9f85455bd0f1407503f355f666d4da9aa560ad1a92b3367cb57ea51d341f71.png)

Figure 6: two scatter panels for water-cooled chillers plotting full-load EER (left) and EER of IPLV (right) against rated cooling capacity out to about 3,000 tons, comparing manufacturer specifications with the ComStock baseline. Baseline points concentrate below 600 tons and overlap the lower manufacturer range at full load, while manufacturer units above 1,000 tons reach EERs near 21-23.

- Besides Daikin products, data are extracted from manufacturer webpages in January 2025. Daikin products are extracted from older (2014-2016) materials that were still publicly available because the performance metrics (i.e., EER) were not available in the latest specification datasheet documents. Although these products are from 10 years ago, their performance, as indicated in the spec sheets, remains comparable to the latest models. Therefore, they were included to expand the data pool for later averaging.
- While full-load EER and IPLV EER were relatively easy (but not 'always' available) from manufacturer specification datasheets, only one manufacturer provided EER values under varying operating conditions (i.e., performance maps), which makes it difficult to generalize part-load operating characteristics between products across different manufacturers.

