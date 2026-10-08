<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/89130.pdf | status: osti_pdf | source_url: https://www.nlr.gov/docs/fy24osti/89130.pdf | publication_url: https://www.nlr.gov/docs/fy24osti/89130.pdf | corpus_version: 267e3ea | corpus_path: upgrade_measures/measure_pdfs/89130.md | section: 3.2  Methodology | lines: 693-718 -->
## 3.2  Methodology

This measure replaces gas commercial cooking equipment with electric equipment where applicable. More specifically, the measure loops through the space types in the model to find any kitchen space types. If a building does not have a kitchen space type, the measure is deemed not applicable. Next, the measure loops through the equipment objects in the kitchen space types to find gas equipment objects. If none are found, this means the kitchen is already all electric, and the model is deemed not applicable.

There may be up to six gas equipment objects, each representing one of the six types of modeled cooking equipment (broilers, fryers, griddles, ovens, ranges, and steamers). The gas equipment object will contain the quantity of that type of equipment, the total design level (in watts), and fractions of latent, radiant, and lost heat. All gas equipment objects found in the model are replaced with the comparable electric equipment using the rated power values in the rightmost column of Table 16.

Table 16. Equipment Power of Existing Gas Equipment Converted to kW, Compared With Equipment Power of New Electric Equipment

| Appliance   | Existing Gas Equipment Power   | Existing Gas Equipment Power   | New Electric Equipment Power   |
|-------------|--------------------------------|--------------------------------|--------------------------------|
|             | Rated Power (Btu/h)            | Rated Power (kW)               | Rated Power (kW)               |
| Broiler     | 96,000                         | 28.1                           | 10.8                           |
| Griddles    | 90,000                         | 26.4                           | 17.1                           |
| Fryers      | 80,000                         | 23.4                           | 14.0                           |
| Ovens       | 44,000                         | 12.9                           | 12.1                           |
| Ranges      | 145,000                        | 42.5                           | 21.0                           |
| Steamers    | 200,000                        | 58.6                           | 27.0                           |

The measure will extract the equipment quantity from the original gas equipment object and use this to calculate the design level for the new electric equipment object. For example, if the original model had a quantity of two fryers, the new object would have a design level of 26,400 * 2 = 52.800 watts (equivalent to two electric fryers). This same methodology is repeated for each of the gas cooking appliances in the baseline model.

In addition to changing the design level, the measure will replace the fractions of latent, radiant, and lost heat with the electric equipment fractions from Table 14. The schedules for the kitchen equipment will not be altered, as we want to represent a direct replacement of equipment with no change to operation. Hence, minor differences in standby operation of gas versus electric equipment are not captured by this measure as schedules remain the same before and after the swap out.

One important note is that this measure does not touch water heating equipment in kitchens. For this reason, the measure is called 'Electric Cooking Equipment' as opposed to 'All-Electric Kitchens' (or something that implies that the entire kitchen is electricity-powered). There could still be gas-powered water heating equipment in the building after the measure is applied. 'AllElectric Kitchens' could be a future measure developed in a later cycle.

In addition, a 'Miscellaneous Electric Kitchen Equipment' object is included in each kitchen space type to account for non-major electrical appliances found in kitchens, such as microwaves, heating lamps, toasters, coffee machines, electric kettles, etc. This miscellaneous load is calculated in the baseline such that it represents 10% of the total kitchen electric load. This miscellaneous electric load object in kitchens is not altered by the Electric Cooking Equipment measure. However, because the total kitchen load changes from applying the measure, the miscellaneous load will no longer represent 10% of the total kitchen electric load in the final model. The kitchen's electric load increases substantially because of the Electric Cooking Equipment measure, therefore the miscellaneous electric kitchen equipment object will represent less than 10% of the kitchen's electric load in the final model.

