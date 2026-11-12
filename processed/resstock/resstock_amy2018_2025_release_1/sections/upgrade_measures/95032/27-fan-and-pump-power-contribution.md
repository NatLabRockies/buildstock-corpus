<!-- resstock resstock_amy2018_2025_release_1 | upgrade_measures | measure_pdfs/95032.pdf | status: osti_pdf | source_url: https://docs.nlr.gov/docs/fy26osti/95032.pdf | publication_url: https://docs.nlr.gov/docs/fy26osti/95032.pdf | corpus_version: resstock_amy2018_2025_release_1-v1 | corpus_path: upgrade_measures/measure_pdfs/95032.md | section: Fan and Pump Power Contribution | lines: 361-406 -->
## Fan and Pump Power Contribution

In the OpenStudio-HPXML workflow, an electronically commutated motor (ECM) fan, with a power consumption ( 𝑃𝑃 𝑓𝑓𝑓𝑓𝑓𝑓 , 𝑓𝑓𝑎𝑎𝑎𝑎𝑓𝑓𝑎𝑎𝑎𝑎𝑎𝑎 ) of 0.375 W/cfm, is assumed if the net COP of the unit is above 2.73, and below that a permanent split capacitor (PSC) fan with a power of 0.5 W/cfm is assumed. This assumption is based on assumptions made in Home Energy Score (U.S. DOE 2021). The fan airflow rate is sized to be 400 cfm/ton of capacity. The rated fan power per cubic feet per minute (cfm) of airflow is estimated to be half of the total fan power. This is because about 50% of the fan's power is assumed to overcome the resistance in the ductwork. 14

Where:

𝑃𝑃 𝑓𝑓𝑓𝑓𝑓𝑓 , 𝑓𝑓𝑎𝑎𝑎𝑎𝑓𝑓𝑎𝑎𝑎𝑎𝑎𝑎

:

Power consumed by the fan per airflow rate (W/cfm)

𝐹𝐹 𝑓𝑓𝑓𝑓𝑓𝑓 , 𝑠𝑠𝑟𝑟𝑓𝑓𝑟𝑟𝑎𝑎𝑠𝑠 :

Adjustment factor to overcome resistance in the ductwork (50%)

𝑃𝑃 𝑓𝑓𝑓𝑓𝑓𝑓 , 𝑎𝑎𝑓𝑓𝑟𝑟𝑟𝑟𝑟𝑟 :

Rated power of the fan per airflow rate (W/cfm)

𝐹𝐹 𝑓𝑓𝑓𝑓𝑓𝑓 , 𝑓𝑓𝑎𝑎𝑎𝑎𝑓𝑓𝑎𝑎𝑎𝑎𝑎𝑎

:

Fan airflow rate per ton of capacity (400 cfm/ton)

𝐶𝐶 𝑟𝑟𝑎𝑎𝑓𝑓 , 𝐵𝐵𝑟𝑟𝐵𝐵 / ℎ𝑎𝑎

: Unit conversion from tons to Btu/hr = 12,000 (Btu/hr)/ton

𝑃𝑃 𝑓𝑓𝑓𝑓𝑓𝑓

: Rated power of the fan in W/(Btu/hr) of capacity

The pump is assumed to consume 80 W/ton of capacity 15 ( 𝐹𝐹 𝑝𝑝𝐵𝐵𝑝𝑝𝑝𝑝 ).

: Pump power per capacity (80 W/ton)

Where:

𝐹𝐹 𝑝𝑝𝐵𝐵𝑝𝑝𝑝𝑝

14  ANSI/RESNET/ICC 301 says 0.2 W/cfm is the fan power associated with ductwork but does not specify if that was a PSC or BPM fan.

15 This value was determined based on a rough manufacture website search and some internal discussion.

