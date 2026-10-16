<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | assets/files/ComStock Measure Doc_Low Priority Device Switching During Peak Hours.pdf | status: site_page | source_url: https://github.com/NatLabRockies/ComStock.github.io/blob/2036a73dc9b7a5dccb8b62fe835cdcbc777175fa/assets/files/ComStock%20Measure%20Doc_Low%20Priority%20Device%20Switching%20During%20Peak%20Hours.pdf | publication_url: https://natlabrockies.github.io/ComStock.github.io/assets/files/ComStock%20Measure%20Doc_Low%20Priority%20Device%20Switching%20During%20Peak%20Hours.pdf | corpus_version: comstock_amy2018_2025_release_3-v3 | corpus_path: upgrade_measures/unpublished_docs/upgrade_measures/ComStock Measure Doc_Low Priority Device Switching During Peak Hours.md | section: 3.3. Limitations and Concerns | lines: 209-220 -->
## 3.3. Limitations and Concerns

Several limitations and concerns of the measure are identified as follows.

- The measure assumes that low-priority devices are controllable (either via deviceintegrated controls or via communication with BAS), which is idealistic and dependent on the adoption of these control technologies.
- The plug load reduction event is applied for every day throughout the year. In reality, demand response programs are structured to limit events to a small number of days and total hours, but the dispatch strategy is not part of this study and will be analyzed in postprocessing by another tool.
- The start of the peak period is defined by the seasonal peak hour of the aggregated state-

level load profile from Cambium data, which does not necessarily align with the peak hour of a particular electricity system or individual building. Besides, any demand-side improvements on building energy consumption is not reflected in the Cambium loads, so if these improvements are significant enough to alter the peak timings, it's not captured in the dispatch assumptions.

- The measure can only be applicable to those schedules in scheduleRuleSet format, but this is likely to cover all models in ComStock.

