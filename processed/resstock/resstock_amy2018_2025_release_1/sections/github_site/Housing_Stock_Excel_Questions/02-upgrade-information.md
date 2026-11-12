<!-- resstock resstock_amy2018_2025_release_1 | github_site | docs/resources/how-to-guides/Housing_Stock_Excel_Questions.md | status: site_page | source_url: https://github.com/NatLabRockies/ResStock.github.io/blob/696c020d696137830ddae75abbfb477ae7af8eaa/docs/resources/how-to-guides/Housing_Stock_Excel_Questions.md | publication_url: https://natlabrockies.github.io/ResStock.github.io/docs/resources/how-to-guides/Housing_Stock_Excel_Questions.html | corpus_version: resstock_amy2018_2025_release_1-v1 | corpus_path: github_site/docs/resources/how-to-guides/Housing_Stock_Excel_Questions.md | section: Upgrade Information | lines: 129-173 -->
## Upgrade Information

As a reminder, these are the two questions we are looking to answer using the upgrade information.
1.	How does site energy change before and after the upgrade has been applied by housing vintage?
2.	Do natural gas energy bills change before and after the upgrade has been applied by housing vintage?

For the site energy question, looking through the data dictionary shows two options, one that subtracts power produced by PV or generators, and one that is just total site energy. Let’s look at the total site energy, which would be **out.site_energy.total.energy_consumption.kwh**. Again, this is just the total amount, not the impact from the upgrade. Going back to the results file and searching for “out.site_energy” you eventually find a column titled **out.site_energy_net.energy_consumption.kwh.savings**, which is what we want for this example.

Then, for the natural gas bills on the data dictionary, we have one option **out.bills.natural_gas.usd**, but we want to know the savings, not just the total bills. Look back at the CO_upgrade02_metadata_and_annual_results file, and search for “out.bills.natural_gas”. There are actually two listings, one is **out.bills.natural_gas**, and the other is **out.bills.natural_gas.usd.savings**, which is what we actually want. Therefore, let’s use the **out.bills.natural_gas.usd.savings**. We’ll use Excel and PivotTable to answer the questions about the upgrade information too. As a first step, insert a new <ins>PivotTable</ins> following the same steps as the baseline housing.

![](../../../assets/images/newpivot.png)

The blank <ins>PivotTable</ins> will look like this.

![](../../../assets/images/blankpivot.png)

The ResStock columns are on the right, and we will start to pull the fields into the four boxes on the bottom to begin the analysis.

We want to look at the three questions by Single-Family Detached homes only, so let’s start with that first filter. In the fields table, click and drag **in.geometry_building_type_recs** into the <ins>Filters</ins> box. Then, where it says (All), we need to only select Single-Family Detached.

![](../../../assets/images/onlysfd.png)

The models that have been upgraded, or homes that were eligible to receive the cold-climate heat pump with the electric backup, can be identified by the **applicability** column. Drag applicability from the list of fields to the <ins>Filters</ins> box, like we did with **in.geometry_building_type_recs**, and from the down arrow next to the it, choose True. The table now looks like this.

![](../../../assets/images/applicability.png)

When describing the housing segment, it may be useful to exclude vacant units, or separate them into their own subsegment, as they have very low energy usage and may skew the average values. Vacant homes only have energy consumption from baseloads, like refrigerators and freezers, and some heating loads to prevent frozen pipes. For this example, we will exclude vacant homes. Looking back at the data_dictionary.tsv, we see that line 173 has a field called **in.vacancy_status** that describes if there are occupants in the home or not. Go back to the <ins>PivotTable</ins>, and drag **in.vacancy_status** to the Filters box just like we did for the other two filters, and choose Occupied. All three filters together now look like this.

![](../../../assets/images/occupied.png)

Now that all of our filters have been applied, we can start looking at the site energy and natural gas bills by vintage. Drag **in.vintage** to the Rows box to get started.

Let’s head to the question: How does site energy change before and after the upgrade has been applied by housing vintage? Choose **out.site_energy.total.energy_consumption.kwh.savings** and drag it into the <ins>Values</ins> box. Similar to the previous steps, change the value from <ins>Count</ins> to <ins>Sum</ins>. The PivotTable now looks like this.

![](../../../assets/images/sumsite.png)

The total amount of kWh saved through this upgrade package applied to applicable houses is "3,865,594" kWh.

Finally, to answer our last question about the savings from natural gas bills. Similar to the first two columns, we drag the column name **out.bills.natural_gas.usd.savings** to the values box and change the field value to <ins>Sum</ins>, not <ins>Count</ins>. Your table will now look like this.

![](../../../assets/images/finalupgrade.png)

The annual natural gas bill savings for all of the single-family homes that were upgraded was modeled to be "$1,483,849".

Now you have seen examples of how to use PivotTable and answer potential questions about how an upgrade would impact a portion of the housing stock. In general, these are just a few questions that can be answered using the baseline housing results and the upgrade results. If you have more questions about how ResStock could be used for your residential building stock analysis, check out the [Contact](docs/contact.md) page.
