<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/89340.pdf | status: osti_pdf | source_url: https://www.nlr.gov/docs/fy24osti/89340.pdf | publication_url: https://www.nlr.gov/docs/fy24osti/89340.pdf | corpus_version: 0a2f61f | corpus_path: upgrade_measures/measure_pdfs/89340.md | section: 5.1.1  Daily Peak Window Variation | lines: 428-442 -->
## 5.1.1  Daily Peak Window Variation

Figure 3 shows the load profiles for five consecutive days from several simulations corresponding to different buildings, weather locations, and scenarios (baseline or with default dispatch strategy) for comparison. Comparison between the baseline profile and the load shed events (appearing as valleys) in the default load shed profile illustrates the timing of the peak window each day. Figure 3 shows that peak windows are highly dependent on individual building characteristics and weather. Even identical buildings (Building 1) in slightly different climate zones (3A and 3B) result in different load profiles. Diversity in the stock models (e.g., location-based weather, internal heat gains, building operation hours, building envelope performance) results in different load profiles, and thus the peak windows each day for each building are also different.

Figure 3. Daily load profile (baseline and load shed) comparison for two buildings with two climate zones

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/89340.yaml
     source: 89340_images/image_000004_9b64138ceab7412fe9fdc09d57f67fbd6dbe0c5bd7507ceae6f8ba155c5d7de7.png
     method: vision-description
     described: 2026-08-20 -->

![Three stacked line charts of hourly load over five days in mid-July comparing baseline and default load shed profiles for Building 1 in ASHRAE climate zone 3A, Building 1 in zone 3B, and Building 2 in zone 3B](89340_images/image_000004_9b64138ceab7412fe9fdc09d57f67fbd6dbe0c5bd7507ceae6f8ba155c5d7de7.png)

Figure 3 of the ComStock thermostat-control-for-load-shedding measure documentation shows that peak windows are building- and weather-specific. Three vertically stacked panels plot hourly load (kWh, axis 50 to 350) for five consecutive days, 7/16 through 7/20: 'Building 1, ASHRAE Climate Zone 3A', 'Building 1, ASHRAE Climate Zone 3B', and 'Building 2, ASHRAE Climate Zone 3B'. Each panel overlays a dashed baseline profile with a solid 'Load shed, Default' profile. Building 1 in zone 3A peaks near 200 kWh daily; the same model in zone 3B peaks slightly lower, near 190 kWh; Building 2 in zone 3B has a much sharper profile peaking near 290 kWh with deeper overnight troughs. In every panel the load-shed curve tracks the baseline except for a distinct daily valley where the shed event occurs, and the timing and depth of that valley reveal the dispatched peak window. It falls at a different hour and has a different shape in each panel. Even the identical building in slightly different climate zones produces different profiles, so stock diversity in weather, internal gains, operating hours, and envelope performance yields a different daily peak window for every model.

