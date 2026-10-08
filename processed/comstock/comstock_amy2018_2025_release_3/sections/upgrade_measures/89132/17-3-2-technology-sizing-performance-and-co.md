<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/89132.pdf | status: osti_pdf | source_url: https://www.nlr.gov/docs/fy24osti/89132.pdf | publication_url: https://www.nlr.gov/docs/fy24osti/89132.pdf | corpus_version: 0a2f61f | corpus_path: upgrade_measures/measure_pdfs/89132.md | section: 3.2  Technology Sizing, Performance, and Configuration | lines: 234-248 -->
## 3.2  Technology Sizing, Performance, and Configuration

In this measure, the existing zone-level equipment is replaced with an air loop containing two coils intended to emulate the water-to-air heat pump and a Fan:OnOff object. The fan's nominal pressure rise is adjusted to account for the limited (or nonexistent) ductwork. The source side of the coils is tied to the common condenser water loop, which is coupled with a ground heat exchanger. The modeled heat pump configuration is shown in Figure 1. In the system configurations in which ventilation is supplied by a DOAS, the fan in the modeled heat pump cycles on and off with the heating or cooling load in the space. When ventilation is provided by the unit itself, the fan is modeled as running constantly during occupied hours to provide ventilation.

Figure 1. Modeled heat pump configuration, with the optional cooling tower shown in a dashedline box

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/89132.yaml
     source: 89132_images/image_000007_e735e3f9553bb281a72569d26ce4a4ebcb8c6f17baa64624663097c4edda9230.png
     method: vision-description
     described: 2026-08-20 -->

![Figure 1. Schematic of the modeled console water-to-air heat pump configuration: a ground loop with ground heat exchanger, coupled through a water-to-water heat exchanger to a condenser loop that serves two zone heat pumps, with an optional cooling tower shown in a dashed box](89132_images/image_000007_e735e3f9553bb281a72569d26ce4a4ebcb8c6f17baa64624663097c4edda9230.png)

System schematic for the Console GHP measure, drawn as three stacked hydronic loops with supply and demand sides labeled on both ends of each loop and circulation pumps shown as circled symbols. The top loop is the ground loop, terminating in a Ground Heat Exchanger. It couples to the middle Condenser loop through a Water Water Heat Exchanger. A Cooling Tower is drawn on the condenser loop inside a dashed orange box, indicating it is optional supplemental heat rejection used only when the ground heat exchanger is sized below the dominant load. The condenser loop supplies two Water-to-air heat pump blocks (orange), each containing a green Pre-heat coil, representing the electric preheat coil that tempers outdoor air brought directly through the console unit. Each heat pump discharges into its own air loop: Air Loop 1 serving Zone 1 and Air Loop 2 serving Zone 2. Blue arrows mark flow direction between the supply and demand sides. The diagram shows the measure's key architecture: zone-level non-ducted console heat pumps on a shared condenser loop, ground rejection as the primary sink, and electric preheat plus an optional cooling tower as the supplemental equipment.

