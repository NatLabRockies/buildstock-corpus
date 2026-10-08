<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | docs/upgrade_measures/hvac_doas_mshp.md | status: site_page | source_url: https://github.com/NatLabRockies/ComStock.github.io/blob/bacf551bc5d2f595d2b3c41a57de0beea23ec6be/docs/upgrade_measures/hvac_doas_mshp.md | publication_url: https://natlabrockies.github.io/ComStock.github.io/docs/upgrade_measures/hvac_doas_mshp.html | corpus_version: 0a2f61f | corpus_path: upgrade_measures/unpublished_docs/upgrade_measures/hvac_doas_mshp.md | section: 4.2  Technology Specifics Such as Sizing, Performance, and Configuration | lines: 90-199 -->
## 4.2  Technology Specifics Such as Sizing, Performance, and Configuration

### 4.2.1  MSHP Modeling

The MSHPs are modeled as four-stage multi-speed objects. Both the fan and compressor can modulate speeds between the four speeds, allowing for high operating efficiencies. During the simulation, the unit speed is determined based on the predicted load for the timestep and the available capacity of each stage after capacity reductions (e.g., reduced capacity at lower temperatures). The rated coefficient of performance (COP), airflow fraction, and capacity fractions for heating and cooling are shown in Table 1 and Table 2, respectively. These parameters were derived from lab testing data of an MSHP and are intended to represent a premium efficiency unit suitable for cold climates with SEER \>30 and HSPF \>14.

Table 1. Parameters for the Four Direct Exchange (DX) Heating Stages

| **Speed** | **Test Unit COP** | **COP Fraction** | **Test Unit Airflow** | **Airflow Fraction** | **Test Unit Capacity** | **Capacity Fraction** |
|-------|---------------|--------------|-------------------|------------------|--------------------|-------------------|
| 4     | 5.45          | 1.00         | 0.26              | 1.00             | 5743.02            | 1.00              |
| 3     | 5.98          | 1.10         | 0.20              | 0.78             | 3828.68            | 0.67              |
| 2     | 6.52          | 1.20         | 0.17              | 0.67             | 2871.51            | 0.50              |
| 1     | 8.20          | 1.50         | 0.14              | 0.56             | 1914.34            | 0.33              |

Table 2. Parameters for the Four DX Cooling Stages

| **Speed** | **Test Unit COP** | **COP Fraction** | **Test Unit Airflow** | **Airflow Fraction** | **Test Unit Capacity** | **Capacity Fraction** | **Test Unit Sensible Heat Ratio** |
|-----------|-------------------|------------------|-----------------------|----------------------|------------------------|-----------------------|-----------------------------------|
| 4         | 6.09              | 1.00             | 0.27                  | 1.00                 | 5743.02                | 1.00                  | 0.70                              |
| 3         | 8.29              | 1.36             | 0.21                  | 0.76                 | 4041.38                | 0.70                  | 0.76                              |
| 2         | 9.91              | 1.63             | 0.18                  | 0.65                 | 3190.57                | 0.56                  | 0.80                              |
| 1         | 11.48             | 1.88             | 0.14                  | 0.53                 | 2339.75                | 0.41                  | 0.86                              |

Five performance curve modifier types are used to model the direct exchange (DX) multi-speed heating objects. The performance curves were derived from lab testing of a variable speed MSHP coupled with iterative calculations for target SEER and HSPF. For multi-speed objects, these modifiers are specific to the applied speed, so each performance curve type may have four curves for a multi-speed unit. They are described as follows.

1.  **Energy input ratio (EIR) as a function of part load ratio** --
    Uses the calculated part load ratio to determine an EIR modifier
    from compressor cycling, which is multiplied by the full-load EIR
    for the stage (Figure 4). Note that the EIR is the inverse of the
    COP, so decreasing the EIR increases the realized efficiency.

2.  **Capacity as a function of temperature** -- Uses outdoor and indoor
    dry bulb temperature (indoor wet bulb for cooling) to predict a
    capacity modifying factor that is multiplied by the rated capacity
    for each stage (Figure 6). For heat pump heating, the available
    capacity generally decreases with temperature.

3.  **COP as a function of temperature** -- Uses outdoor and indoor dry
    bulb temperature (indoor wet bulb for cooling) to determine a COP
    for the timestep (Figure 5). Note that this COP can still be
    affected by other modifiers that affect efficiency.

4.  **Capacity as a function of flow** -- Modifies capacity based on the
    determined flow rate for a timestep. Because capacity and efficiency
    are already modified by the properties defined at each stage, this
    curve is not used.

5.  **EIR as a function of flow** -- Modifies EIR based on the
    determined flow rate for a timestep. Because capacity and efficiency
    are already modified by the properties defined at each stage, this
    curve is not used.

![](./media/imaaffe4aab-21e8-4c31-8df5-4161af1877cfge4.jpeg)

Figure 4. MSHP part load factor as a function of part load ratio for heating and cooling. The resulting part load factor is used to effectively increase the EIR (decrease efficiency) for the timestep for compressor speed 1 to represent cycling losses.

![](./media/49d4020c-4a91-42f9-9c93-eb8ec9caf8e3.jpeg)

Figure 5. MSHP heating COP (compressor-only) as a function of indoor and outdoor air dry bulb temperature for the four speeds of heating. Note that these curves suggest performance that surpasses even premium units on the market.

![](./media/47a45de6-fb7d-402b-ad4d-71b9b2f7fdd0.jpeg)

Figure 6. MSHP heating capacity fraction as a function of indoor and outdoor dry bulb temperature for the four stages of heating. These values are multiplied by the rated capacity for the given stage to determine the actual capacity for the timestep.

This study attempts to utilize the best available data, as described previously, as this will notably impact the results. However, it should be emphasized that complete heat pump performance data is still limited at the time of this study, especially for premium efficiency variable speed units. This limits our understanding of heat pump performance and operation in this analysis. Further research on heat pump performance could increase confidence in heat pump modeling, and this study may be updated as more data becomes available.

Similar to heating, another five performance curve modifier types are used to model the DX cooling system. The only structural difference between the cooling curve properties and the previously-described heating curve properties is that the DX cooling curves use indoor air wet bulb temperature in place of dry bulb temperature. Like the heating curves, the DX cooling curves were derived from lab testing data for an MSHP.

### 4.2.2  MSHP Sizing, Backup Heat, and Compressor Lockout

The methodology for sizing a heat pump, as well as the compressor lockout temperature, can notably impact heat pump modeling results. Heat pump sizing is nontrivial, as the heating and cooling coils use the same refrigerant system. Furthermore, heating capacity can be reduced at lower temperatures, which can also coincide with the highest heating needs for a building \[6\],\[7\]. Additionally, compressor lockout controls are often implemented in heat pump systems, which disables heat pump operation below a certain temperature threshold. If the design heating temperature for a building is below this threshold, or if the heat pump is not sized such that the available capacity at the design heating temperature can meet the design heating load (considering lost capacity at lower temperatures), then a backup heating system may be required to address any unmet load.

There are many sizing mythologies that can be considered when sizing heat pumps \[6\]. Some suggest sizing the system to the cooling load and using a backup heating system to address the remaining load. This may require additional backup heating equipment, but may also reduce the upfront cost of the heat pump if it permits the purchase of a lower-capacity unit. However, this may cause reduced operational efficiency, as an electric resistance backup heating system will generally have a lower COP compared to the heat pump, and this sizing scheme may increase the prevalence of backup heating operation. Alternatively, there are sizing pathways that size the heat pump to ensure that loads are met at a specific temperature, or that loads are met at the design temperature. However, it is suggested that the unit not be sized too far beyond the cooling design load to avoid excessive cycling operation \[6\],\[7\]. The Natural Resources Canada heat pump sizing guide suggests sizing single-stage systems only up to 125% of the design cooling load \[6\]. However, using a multi-speed or variable speed system can reduce cycling losses, as the unit has a better ability to modulate output capacity \[6\], \[7\].

MSHPs do not always include built-in backup heating systems. If this is the case, another heating system---such as electric baseboards---may need to be implemented, which may not be desired. Furthermore, the MSHPs modeled in this study are meant to represent premium efficiency variable speed systems that would be less impacted by cycling losses, which makes them more viable for sizing beyond the design cooling load. For these reasons, the sizing scheme used in this study attempts to reduce the use of backup heat by sizing the MSHPs up to 135% of the design cooling load, when needed. The compressor lockout temperature is modeled at −15°F, which aligns with some of the lowest limits available on the market \[8\]. This configuration will increase the utilization of the higher-efficiency MSHP (relative to a backup electric resistance heating coil) while reducing the need for the backup heating system. The backup heating system is modeled as an electric resistance coil with a COP of 1.

### 4.2.3  DOAS ERV/HRV Design

This measure models a DOAS ERV or HRV for each zone in the building to provide the required outdoor air ventilation. In practice, this allows a one-to-one replacement of RTUs, taking advantage of existing ductwork \[1\]. The existing ductwork may be oversized for the ventilation airflow only, as it would have previously been sized for space conditioning as well as ventilation. However, this could be beneficial, as it would allow lower static pressure fan operation. Alternatively, a single ERV could be used to replace several RTUs, but this would require additional linking of duct runs between thermal zones, which would increase cost and complexity, and would not address zone autonomy. Both ERVs and HRVs are available in a wide range of airflow sizes. They can additionally both include heating and cooling equipment to ensure appropriate discharge air conditions (temperature and humidity), but this is not always necessary \[1\].

An HRV is a plate and frame heat exchanger system with a supply/exhaust fan system capable of sensible (temperature-only) heat recovery, with little effectiveness for latent heat removal \[9\]. An ERV is similar, except the heat exchanger is an enthalpy wheel capable of both sensible and latent energy recovery. This wheel requires electrical power to turn. The Northwest Energy Efficiency Alliance (NEEA) describes a very high-efficiency HRV or ERV as one that has a sensible effectiveness greater than 82% \[1\].

DOAS ERV or HRV configurations can be classified as either **coupled** or **decoupled** systems (illustrated in Figure 7) \[1\]. A coupled system ducts the outdoor air directly to the return air side of the zone terminal units (which are mini split heat pumps for this study). This allows the outdoor air to receive additional conditioning before discharging to the space and can save duct space. However, this setup requires the heat pump to run continuously whenever the building is occupied to satisfy commercial building ventilation requirements. Decoupled systems, on the other hand, duct the outdoor air from the ERV directly to the space or to the supply side of the zone terminal heat pump. This allows ventilation air delivery regardless of the heat pump's operation, essentially allowing the heat pumps to cycle on only when needed to maintain thermostat set point. A Red Car Analytics study found that a coupled DX-DOAS/ERV (a DOAS ERV with integrated direct expansion cooling) system increases energy costs by 19% on average compared to the decoupled system \[1\]. However, the decoupled system does not provide additional conditioning to the ventilation air being supplied from the ERV, which may require the ERV system to use integrated heating and cooling equipment beyond the energy recovery for reasonable discharge air temperature and humidity. This can add cost and complexity to the ERV system \[1\].

Humidity is a primary consideration for DOAS design \[1\]. A simple plate and frame heat exchanger HRV-DOAS would be the cheapest first cost system with the smallest footprint, but this may only be appropriate in drier climates (ASHRAE climate zones 3B, 3C, 4B, 4C, 5B, 5C, 6B) where humidity is not as much of a concern, as ERV heat exchangers alone are not appropriate for removing humidity \[1\]. An enthalpy energy recovery wheel found in an ERV-DOAS could better address humidity concerns, but these can be costly. Another option is to add a DX system to the DOAS, for a DX/ERV-DOAS or DX/HRV-DOAS, which has been found to be slightly more costly than an ERV system with an enthalpy wheel \[1\].

![Diagram Description automatically generated](./media/114594f7-4643-4649-b747-8810ced6a817.png)

Figure 7. Airflow configurations for dedicated outdoor air systems. Image from \[1\].

For maximum heat recovery benefit, the DOAS design should route most or all exhaust air directly through the ERV system, which is shown for all configurations in Figure 7. Some designs exhaust to other locations, which diminishes the heat recovery capabilities of the system by effectively making the DOAS a once-through system \[1\]. This is less avoidable in some cases, such as bathroom or kitchen exhaust, which would be difficult and sometimes undesirable to route back to the DOAS system. However, it is preferable to route exhaust air through the DOAS wherever possible when using HRV or ERV to facilitate productive energy exchange between the exhaust and the incoming outdoor air. The ComStock baseline generally assumes this to be the case, with the only exceptions being transfer air for kitchens and some restroom exhaust fans. This may slightly overestimate stock ERV/HRV savings potential, as ComStock does not account for the prevalence of once-through systems.

Frost control is required for ERV systems in colder climates where the outdoor air temperature falls below the dewpoint of the exhaust \[10\]. This is especially true for HRV systems where humid return air is exhausted. Some manufacturers defrost the exhaust by bypassing the inlet to the ERV, and therefore exhausting warm air from the building directly to melt the coils. Another method is to use an electric resistance coil on the inlet to ensure the exhaust air is warm enough, preventing frost formation in the first place. This study will use the bypass method.

### 4.2.4  ERV Modeling

All DOAS ERVs/HRVs modeled in this study will be decoupled per NEEA's recommendations. Frost control will use supply air bypass. As discussed previously, it is imperative for the ERV or HRV to provide reasonably conditioned air to the space, as the decoupled setup discharges air directly to the zones. For drier western climates (ASHRAE climate zones 2B, 3B, 3C, 4B, 4C, 5B, 5C, 6B), a decoupled HRV-DOAS will be used. For all other climate zones, an ERV-DOAS will be used for enhanced latent load managment.

The DOAS units will be controlled using a linear outdoor air float scheme. ERV DOAS systems, which are modeled in climate zones with higher humidity concerns, will be controlled to discharge 55°F when outdoor temperatures are above 55°F, and 67°F when temperatures are below 45°F, floating linearly in between. This is similar to what is recommended in the ASHRAE DOAS Design Guide (illustrated in Figure 8), with the exception of the lower temperature being set to 55°F as opposed to 52°F. This is because RTUs in the ComStock baseline are set to discharge 55°F, which might skew the comparison. HRV DOAS systems in drier climates are modeled the same, except for the lower discharge air temperature being set to 60°F. This may not always be required, as described in \[1\], but it is being modeled for all HRVs in this study to ensure reasonable discharge air conditions across the wide variety of models in the ComStock baseline.

The ensure that the DOAS temperature control set points are met, all systems will be modeled with an electric resistance heating coil and a DX cooling coil. A heat pump DOAS could also be used and may be considered for future studies. The heating coil is modeled with a COP of 1, whereas the DX cooling coil is modeled to align with ASHRAE Standard
90.1-2016.

![Chart, line chart Description automatically generated](./media/de02986b-5cb9-4234-99b3-5b9e39e486a9.png)

Figure 8. DOAS temperature set point recommendations form ASHRAE DOAS Design Guide.

A sensible effectiveness of 82% is applied to the HRVs, mirroring the recommendations by NEEA and other studies on the topic \[1\]. Because these systems use an aluminum exchanger with no moisture transfer, 0% latent effectiveness is used. A sensible effectiveness of 78% is applied to ERVs, which is slightly lower than that of the HRVs because the moisture-transferring membrane in ERVs can be less effective at transferring heat than the aluminum construction of HRVs. A latent effectiveness of 65% is used for the ERVs, which is the middle of the typical range suggested by the ASHRAE HVAC Handbook \[7\].

