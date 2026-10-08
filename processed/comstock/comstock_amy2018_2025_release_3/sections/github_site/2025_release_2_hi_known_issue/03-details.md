<!-- comstock comstock_amy2018_2025_release_3 | github_site | docs/resources/explanations/2025_release_2_hi_known_issue.md | status: site_page | source_url: https://github.com/NatLabRockies/ComStock.github.io/blob/bacf551bc5d2f595d2b3c41a57de0beea23ec6be/docs/resources/explanations/2025_release_2_hi_known_issue.md | publication_url: https://natlabrockies.github.io/ComStock.github.io/docs/resources/explanations/2025_release_2_hi_known_issue.html | corpus_version: 0396270 | corpus_path: github_site/docs/resources/explanations/2025_release_2_hi_known_issue.md | section: Details | lines: 12-19 -->
## Details
The weather files used for Hawaii models in ComStock 2025 Release 2 - 2012 Weather, appear incorrect. As shown below, the temperatures in these weather files drop below 0°C (32°F), which is unrealistic for Hawaii’s climate. These weather files resulted in approximately 25% higher heating energy in the state compared to 2018 Weather ComStock releases.

Unfortunately, the weather file issue was discovered after the simulations were run and the dataset was released, and the Hawaii models cannot be rerun with corrected weather files.

![](../../../assets/images/2025_2_hi_known_issue_1.png)
![](../../../assets/images/2025_2_hi_known_issue_2.png)

