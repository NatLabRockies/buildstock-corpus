<!-- resstock resstock_amy2018_2025_release_1 | github_site | docs/resources/explanations/Number_of_samples.md | status: site_page | source_url: https://github.com/NatLabRockies/ResStock.github.io/blob/696c020d696137830ddae75abbfb477ae7af8eaa/docs/resources/explanations/Number_of_samples.md | publication_url: https://natlabrockies.github.io/ResStock.github.io/docs/resources/explanations/Number_of_samples.html | corpus_version: resstock_amy2018_2025_release_1-v1 | corpus_path: github_site/docs/resources/explanations/Number_of_samples.md | section: Number of Samples when Analyzing Timeseries Results | lines: 120-138 -->
## Number of Samples when Analyzing Timeseries Results
Timeseries analysis will generally require higher numbers of samples to reach the same level of certainty. These types of analyses often include assessing the timing or magnitude of peak electricity consumption. Calculating the standard error is an available and useful approach, though that is not done in this explanation. Here is a visual example instead.

In the ResStock team’s experience, uncertainty levels off by 1,000 samples for many common quantities of interest. This is why the ResStock team recommends using 1,000 or more samples for analysis when further specifics are not known.

![](../../../assets/images/ercot-peak-load-day-2018.png)

Above is Figure 386 from the [End Use Load Profiles Methodology report](https://docs.nlr.gov/docs/fy22osti/80889.pdf) which provides one example of the impact of number of samples on timeseries aggregate results in ResStock circa ResStock 2021 Release 1.

In the top row and top left figure, there are two samples used in the timeseries profile. The timeseries is spiky and dominated by the use of the cooking range and clothes dryer. The average 15-minute peak shown is over 1.2 kW per housing unit and occurs  around hour 22.

The figure in the top row middle uses 10 samples. These 10 samples result in a less spiky timeseries, but still show a 15-minute peak over 1.2 kW per housing unit and spikes from individual home appliance.

Moving to 100 samples, in the top right figure, the 15-minute peak load of the day is around 0.9 kW per home. The peak load is about 40% lower than with the 10 samples, and the timeseries average has begun to smooth out.

On the bottom row on the left, there are 1,000 samples. The load profile is much smoother, the 15-minute peak is around 0.9 kW per housing unit and occurs around hour 16-17. While the shape smooths out further at 10,000 and 38,300 samples, the value at each timestep is generally similar across all three lower subfigures. Some analyses will be fine with 100 samples in this example, some will prefer 1,000, and very few would need more than 1,000. Using less than 100 samples could result in a 40% difference in peak magnitude results.

This example is provided for illustrative purposes only. The results for every set of 1, 10, 100, 1,000, and so on samples will not match the above. However, in the team’s experience most quantities of interest converge with less than 1,000 samples and some will in many cases converge with 100 or even 10 samples.

