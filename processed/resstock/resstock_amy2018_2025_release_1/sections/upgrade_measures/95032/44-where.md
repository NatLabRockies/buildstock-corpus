<!-- resstock resstock_amy2018_2025_release_1 | upgrade_measures | measure_pdfs/95032.pdf | status: osti_pdf | source_url: https://docs.nlr.gov/docs/fy26osti/95032.pdf | publication_url: https://docs.nlr.gov/docs/fy26osti/95032.pdf | corpus_version: resstock_amy2018_2025_release_1-v1-pre | corpus_path: upgrade_measures/measure_pdfs/95032.md | section: Where: | lines: 782-817 -->
## Where:

𝐶𝐶𝑎𝑎𝑝𝑝 𝐻𝐻 : Heating capacity of the heat pump (W)

𝐶𝐶𝑎𝑎𝑝𝑝 𝐶𝐶

: Cooling capacity of the heat pump (W)

𝐶𝐶𝐶𝐶𝑃𝑃 𝐻𝐻 : Heating coefficient of performance (-)

𝐶𝐶𝐶𝐶𝑃𝑃 𝐶𝐶 : Cooling coefficient of performance (-)

𝑅𝑅 𝑠𝑠 : Ground resistivity (Km/W)

Rp: Pipe thermal resistivity (Km/W)

𝑅𝑅𝑅𝑅𝜋𝜋 𝑓𝑓 , 𝐻𝐻 : Runtime fraction in heating (-)

𝑅𝑅𝑅𝑅𝜋𝜋 𝑓𝑓 , 𝐶𝐶 : Runtime fraction in cooling (-)

𝑓𝑓 𝑠𝑠 : Loop temperature in cooling (K)

𝑓𝑓 𝐻𝐻 : Loop temperature in heating (K)

𝑓𝑓 𝑒𝑒 : Undisturbed ground temperature (K)

𝑃𝑃 𝐶𝐶 : 𝑃𝑃 ength of the ground heat exchanger based on cooling requirements (m)

𝑃𝑃 𝐻𝐻 : Length of the ground heat exchanger based on heating requirements (m)

The L2 methods uses six pulses per year (three pulses for each heating and cooling season: annual, monthly, and a peak of user-specified duration). The L3 methods uses monthly peak pulses, and finally, the L4 methods uses hourly simulations. The time step resolution used in the design methodology has a significant effect on the accuracy of the predicted size requirements.

OpenStudio-HPXML currently uses an L1 approach to characterize the ground heat exchanger; see Appendix B for more details on the methodology. Residential building HVAC sizing is often determined by design-day calculations (ACCA Manual J). This approach results in a peak load calculation and a resulting HVAC system size to meet the peak load. The methods specified in ACCA Manual J and ACCA Manual S are implemented in OpenStudio-HPXML. See Section 2.4.2 GHP Sizing Methodology for the load inputs for the ground heat exchanger sizing.

During the HVAC sizing routine, no information about the monthly or hourly building loads is present. The result is that L2 through L4 approaches cannot be easily integrated into OpenStudio-HPXML. The integration of L2 to L4 approaches would require that the EnergyPlus model be simulated with an ideal load system to get an estimate of the time-series building loads. These loads would then need to get processed into the inputs necessary for the L2 to L4 approach. Then the ground heat exchanger L2 to L4 approach could be calculated. The impact of this level of integration would double the runtime of the OpenStudio-HPXML models as two annual simulations and file input/output would be required. The increase in runtime is the main reason OpenStudio-HPXML is staying with the Level 1 ground heat exchanger characterization algorithm.

