<!-- resstock resstock_amy2018_2025_release_1 | upgrade_measures | measure_pdfs/94464.pdf | status: osti_pdf | source_url: https://docs.nlr.gov/docs/fy26osti/94464.pdf | publication_url: https://docs.nlr.gov/docs/fy26osti/94464.pdf | corpus_version: resstock_amy2018_2025_release_1-v1 | corpus_path: upgrade_measures/measure_pdfs/94464.md | section: Demand Flexibility Approach | lines: 356-402 -->
## Demand Flexibility Approach

The 'Efficient EV Adoption With L2 Charging and DF' measure references peak period definition files, detailed in the following subsection, and sets the charging schedule to zero during peak hours as shown in Figure 5. Although this behavior may resemble a load-shedding event, where energy consumption is curtailed without a compensatory increase in other periods, it works more like a shift event because the battery model compensates, within its limits, by extending the charging duration after the peak period. EVs can still be fully charged before the next driving event in most cases when charging overnight. This distinction arises because the charging availability schedule solely dictates when the vehicle is plugged in, whereas actual energy consumption is governed by the battery model. This situation is illustrated in Figure 5 for a single building test run. During the peak period, the charging availability schedule is set to zero. This setting results in charging being suspended during the peak period, after which the vehicle completes charging. In we can see that the charging energy consumption in this measure (middle graph) is same as that in an equivalent measure without DF (top graph) - only split into two sessions by the peak period. Because this measure includes the adoption of L2 charging, EVs are likely to fully charge before their next driving event, even when the charging start time is shifted.

Figure 5. EV charging schedule modification by DF measure, where the interrupted charging is resumed after the peak period

<!-- figure described by overlay: resstock_resstock_amy2018_2025_release_1/upgrade_measures/measure_pdfs/94464.yaml
     source: 94464_images/image_000006_eca1374fe5b1a4a748b7ac734f70950430394cd53d483b54b3f945287404c39d.png
     method: vision-description
     described: 2026-11-11 -->

![Three step charts showing EV charging interrupted by a peak period and resumed after it](94464_images/image_000006_eca1374fe5b1a4a748b7ac734f70950430394cd53d483b54b3f945287404c39d.png)

Figure 5: three step charts from 08:00 to 23:45 with a shaded peak period from about 17:30 to 21:30: EV charging power in kW without DF, the same with DF, and the occupancy schedule. Without DF the car charges at about 5.7 kW from about 14:00 to 15:30 and from 17:15 to 18:45. With DF the second session stops when the peak begins and resumes after it, from about 21:30 to 22:45.

kWh = kilowatt-hour

Depending on the timing of the peak period in relation to the vehicle charging/discharging schedule, there may not always be sufficient time to charge the vehicle to completion after the peak period-the occupant might leave before the charging is completed. This phenomenon is illustrated in Figure 6. The charging is interrupted around 18:00 due to the peak period, but by the time the peak period ends, the occupant is no longer at home, and the EV can no longer be charged. This by itself is not a problem if the vehicle has sufficient charge to meet the driving need. However, if that's not the case, the insufficient charge will register unmet driving hours. In this example, we can tell the charge was not sufficient because after the charging resumes at midnight, the charging power consumption profile in this measure (Figure 6 middle graph) matches the charging consumption of the measure without DF (top graph). This outcome could have occurred only if the EV was completely depleted in both scenarios. The two hours and 15 minutes of missed charging due to the peak shift in this case translates to greater unmet driving hours during the unoccupied period. If such conditions happen frequently and to multiple units, we can see a significant increase in unmet driving hours. The extent to which charging DF introduces unmet driving hours is further discussed in Section 5.

Figure 6. An example DF situation where charging is interrupted due to the peak period but make-up charging is not possible due to the occupant not being at home

<!-- figure described by overlay: resstock_resstock_amy2018_2025_release_1/upgrade_measures/measure_pdfs/94464.yaml
     source: 94464_images/image_000007_c17607a0598f289f059e060249ddd25e9aef6aa460e8033507f665b407a51ea5.png
     method: vision-description
     described: 2026-11-11 -->

![Three step charts showing EV charging interrupted by a peak period with no makeup charging that evening](94464_images/image_000007_c17607a0598f289f059e060249ddd25e9aef6aa460e8033507f665b407a51ea5.png)

Figure 6: three step charts from 12:00 to about 11:00 the next day with a shaded peak period from about 17:30 to 21:00: EV charging power in kW without DF, the same with DF, and the occupancy schedule. Without DF the car charges from about 15:00 to 20:30. With DF it stops when the peak begins, and because the occupant leaves before the peak ends, charging resumes only at about 00:00.

kWh = kilowatt-hour

To apply the DF schedule to existing charging schedules, the 'Demand Flexibility Electric Vehicle' parameter is set to 'Enabled' in ResStock. As shown in Table 3, setting that parameter to 'Enabled' will set the ev\_flex\_enabled argument to 'True' and the flex\_random\_shift\_minutes argument to 30 in ResStockArgumentsPostHPXML, where the EV DF module is called. The flex\_random\_shift\_minutes argument is used to avoid coincident peak by offsetting the peak period randomly by up to ±30 minutes for each building. This offset will make some buildings start their peak period up to 30 minutes early or up to 30 minutes late (i.e., the shift can be any of the following: +30 min, +15 min, 0 min, -15 min, -30 min). This random shifting is assigned on a building-by-building basis and not on a per-event basis. In a real deployment, this staggering of individual homes would be accomplished through a combination of intentional control and inherent time delays and equipment states found across the portfolio at any point in time. Although this measure may create new concurrent peaks, this feature limits the unrealistic scenario in which all EV charging loads start simultaneously. A similar approach is applied in the ResStock thermostat DF measure.

Table 3. Mapping of ResStock Options to ResStockArgumentsPostHPXML Measure Arguments

<!-- table recovered from measure_pdfs/94464.pdf p.23
     overlay: resstock_resstock_amy2018_2025_release_1/upgrade_measures/measure_pdfs/94464.yaml
     method: extracted grid, with the cells named in `why` corrected from the PDF text layer
     supersedes the extractor's own table here (values 8cffe8bf15e3…):
       Every cell is right, but the argument value -15 carries a space where the PDF breaks the line ('- 15'), which reads as a separate dash and a positive 15. The cell text is the extractor's own with that value joined. The Parameter cell is merged over both rows in the PDF and is repeated on each; the two arguments in a cell are run together, as extracted. -->

| Parameter | Option | ResStockArgumentsPostHPXML Measure Arguments | Description |
|---|---|---|---|
| Demand Flexibility Electric Vehicle | Enabled | ev_flex_enabled = True flex_random_shift_minutes = {30, 15, 0, -15, or -30} | All EV chargers provide load flexibility by turning charging off during the peak period |
| Demand Flexibility Electric Vehicle | Disabled | ev_flex_enabled = False flex_random_shift_minutes = 0 | EV chargers do not provide load flexibility; charging schedules are entirely driven by occupancy status |

