<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/96597.pdf | status: osti_pdf | source_url: https://docs.nlr.gov/docs/fy26osti/96597.pdf | publication_url: https://docs.nlr.gov/docs/fy26osti/96597.pdf | corpus_version: 43ae2d4 | corpus_path: upgrade_measures/measure_pdfs/96597.md | section: 1  Introduction | lines: 187-204 -->
## 1  Introduction

Lighting control is a method of conserving lighting energy and costs in buildings by reducing or turning off artificial lighting when it is not necessary. There are many types of lighting control methods, including [1]:

- Daylighting controls . Reduce lighting usage during daylight hours by dimming or turning off lights in spaces where enough natural light is present
- Manual dimmers . Reduce lighting wattage and output when full brightness is not required; some types of lights are not compatible with dimmers, or do not become more efficient when dimmed
- Occupancy sensors . Turn on/off lights by detecting indoor activity in a space; occupancy sensors can work in various ways, including detecting sound, heat, or motion
- Vacancy sensors . Similar to occupancy sensors, but require occupants to manually turn on the lights
- Motion sensors . Turn off lights by detecting when someone walks into a space, then turning them off a short while later; commonly used for security or utility lighting, but not as useful indoors except in infrequently occupied spaces like closets or other storage areas
- Timers . Programming lights to turn off or on at certain times; most useful if there are consistent hours when a space is used or not used, but timers do not respond to changes in day-to-day activities
- Manual control . The simplest form of lighting control; an occupant turning lights on and off when they are not required.

This measure will implement Daylighting Controls and Occupancy Sensors, as we determined these lighting controls methods to be the most realistic to be implemented in commercial buildings, as well as the most appropriate for modeling in ComStock. The other lighting controls methods listed can be effective in reducing lighting energy use; however, we found there are too many variables that contribute to how these control strategies are deployed and therefore would be difficult to implement effectively in building energy models.

The energy and cost savings potential of lighting controls may vary greatly from building to building. For example, buildings with spaces that are unoccupied for large periods of time can have higher savings potential with occupancy sensors, whereas buildings with large amounts of natural light can benefit more from daylighting sensors. ASHRAE 90.1 and Title 24 standards require lighting controls in some spaces in new construction buildings. This measure will consider that certain spaces may already have code-required lighting controls and will not apply to these spaces. This will be discussed in further detail in Section 3.

In the ComStock baseline, interior lighting accounts for 9% of total stock site energy [2]. Therefore, the energy savings potential for this measure is somewhat limited. However, reducing lighting energy, particularly during unoccupied times or during peak electricity periods, can benefit the grid and save lighting energy and utility costs in commercial buildings. In addition, lighting controls can impact heating, ventilating, and air conditioning energy use, as turning off lighting during summer reduces internal heat gains, and therefore, cooling requirements. However, the reverse is also true -turning off lights in the winter reduces internal gains and increases heating requirements.

