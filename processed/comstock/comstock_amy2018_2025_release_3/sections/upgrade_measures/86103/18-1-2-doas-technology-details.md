<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/86103.pdf | status: osti_pdf | source_url: https://www.nlr.gov/docs/fy24osti/86103.pdf | publication_url: https://www.nlr.gov/docs/fy24osti/86103.pdf | corpus_version: fadc83e | corpus_path: upgrade_measures/measure_pdfs/86103.md | section: 1.2  DOAS Technology Details | lines: 274-307 -->
## 1.2  DOAS Technology Details

VRF systems typically do not provide their own outdoor ventilation air. Therefore, outdoor air must be provided by a separate system, most often using a DOAS. A DOAS can provide preconditioned ventilation air directly to the spaces, which is known as a 'decoupled' system, or can be integrated into the return air path of the VRF indoor terminal head directly, which is known as a 'coupled' system. The decoupled system provides the added benefit of allowing the airflow in the VRF indoor terminal head to modulate fully off when there is no need for heating or cooling, which has been shown to be more efficient than coupled configurations [6]. However, because the outdoor ventilation is supplied directly to the space, it is recommended that the DOAS supply fully conditioned air to avoid zone discomfort and to allow the VRF system to address sensible zone loads only [6].

DOAS ventilation air can be conditioned in multiple ways. The first option considered should be exhaust air energy or heat recovery, which uses exhaust air to precondition incoming outdoor air using a heat exchanger. Compared to traditional heating and cooling methods, energy/heat recovery can reduce ventilation loads by up to 80% [7]. Energy recovery systems generally provide sensible and latent energy exchange through motor-controlled enthalpy wheels or through counterflow fixed-plate membrane heat exchangers. Alternatively, heat recovery systems provide sensible heat exchange through aluminum fixed-plate heat exchangers or heat pipes [8]. Energy recovery is often used in humid climate zones where transferring latent energy is beneficial, while heat recovery is usually considered in drier climate zones where transferring sensible energy is beneficial.

Energy/heat recovery is often rated by the effectiveness of the heat exchange between the supply and exhaust airstreams. The effectiveness determines the fraction of latent, sensible, or total energy exchanged between the air streams. ASHRAE Standard 90.1-2019 requires an enthalpy recovery ratio of at least 50% for applicable climates, while the ASHRAE Advanced Energy Design Guide recommends a total effectiveness of 72%-75% for humid climate zones or 72%75% sensible effectiveness for dry climate zones [8]. The Northwest Energy Efficiency Association (NEEA) defines the heat recovery portion of a 'very high efficiency' DOAS as having a sensible effectiveness over 82% [6]. An example product sheet for the Ventacity VS1000RT Energy/Heat recovery system is shown in Figure 3, which illustrates the range of effectiveness values between heating and cooling as well as sensible and latent energy for different airflow ranges [9]. The Ventacity system uses an aluminum plate heat exchanger for heat recovery or a membrane plate heat exchanger for energy recovery (the Ventacity system does not use a motor-powered enthalpy wheel).

Figure 3. Product data from Ventacity Energy/Heat Recovery System

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/86103.yaml
     source: 86103_images/image_000009_a9260b5ce9c67d8dca1b73a0bddb370444ad1f759c076b8274ca929957996a01.png
     method: vision-description
     described: 2026-08-22 -->

![Figure 3: five-panel Ventacity ERV/HRV product data - fan curve and effectiveness versus flow](86103_images/image_000009_a9260b5ce9c67d8dca1b73a0bddb370444ad1f759c076b8274ca929957996a01.png)

Figure 3: five-panel manufacturer data sheet for the Ventacity energy/heat recovery ventilator. The first panel plots external static pressure (in. W.C.) against flow rate over 175-1,020 CFM with a shaded recommended operating range; the rest plot HRV sensible and ERV latent, sensible and total effectiveness (%) versus flow for heating and cooling modes at AHRI 1060 conditions. Effectiveness falls as flow rises. Modeled values in Table 4.

Figure from [9]. Note that NREL does not endorse any commercial system or product; this is shown as an instructional example only.

A DOAS most often will require additional heating/cooling capacity beyond the capability of the energy/heat recovery system. Especially cold conditions may require a heating coil to ensure the discharge air temperature is hot enough, while especially warm or humid conditions may require a cooling coil to ensure the discharge air temperature is cold/dry enough. The ASHRAE DOAS Design Guide recommends a linear outdoor air float scheme controlled to discharge 52°F when outdoor temperatures are above 52°F, and 67°F when temperatures are below 45°F, floating linearly in between (illustrated in Figure 4) [8]. Note that energy/heat recovery systems can include bypass systems to ensure the air is not overheated prior to being supplied to the zone.

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/86103.yaml
     source: 86103_images/image_000010_23c13416ee6e93e06344ef66e1781216cc4174297da848149737913c948bbf52.png
     method: vision-description
     described: 2026-08-22 -->

![Figure 4: ASHRAE DOAS discharge air temperature setpoint versus outdoor dry-bulb temperature](86103_images/image_000010_23c13416ee6e93e06344ef66e1781216cc4174297da848149737913c948bbf52.png)

Figure 4: single-line control schedule from the ASHRAE DOAS Design Guide plotting DOAS discharge dry-bulb temperature setpoint (deg F, with deg C on the left axis) against outdoor dry-bulb temperature. The setpoint holds at 67 deg F below about 45 deg F outdoors, ramps down through the 45-55 deg F band, then holds at 52 deg F above 55 deg F. Reprinted as Figure 13 for Section 4.2.2.

Figure 4. DOAS temperature control scheme recommendation from ASHRAE DOAS Design Guide

