<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/95009.pdf | status: osti_pdf | source_url: https://docs.nlr.gov/docs/fy25osti/95009.pdf | publication_url: https://docs.nlr.gov/docs/fy25osti/95009.pdf | corpus_version: 267e3ea | corpus_path: upgrade_measures/measure_pdfs/95009.md | section: 3.10  GHEDesigner Workflow | lines: 715-731 -->
## 3.10  GHEDesigner Workflow

GHEDesigner is a software tool available as a Python package for designing ground heat exchangers used with GHP systems [21]. The GHP upgrade measures leverage GHEDesigner for sizing the vertical ground heat exchangers used in the ComStock models. GHEDesigner is executed within the GHP measures. Figure 1 shows the full ComStock GHP measure workflow. First, the GHP measure is applied , which replaces the existing system with one of the GHP configurations. An initial sizing run determines the annual loads the ground heat exchanger needs to supply. The ground loads are exported to GHEDesigner in the form of a JavaScript Object Notation (JSON) file. GHEDesigner then performs calculations to determine the size of the ground heat exchanger in the model. A final EnergyPlus ®  simulation is performed with the ground heat exchanger size set to the value determined by GHEDesigner. See the individual measure documents (Central Hydronic GHP, Packaged GHP, Console GHP) for more detail about the GHEDesigner workflow.

Figure 1. ComStock GHEDesigner workflow

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/95009.yaml
     source: 95009_images/image_000002_f62710097e886dc5f91c0e47e81458aa0a51b94a6a62bd90fd8b6def45632c64.png
     method: vision-description
     described: 2026-08-20 -->

![Figure 1. Flow diagram of the ComStock GHEDesigner workflow, from applying the GHP retrofit measure through initial load calculations and borefield sizing to the final simulation](95009_images/image_000002_f62710097e886dc5f91c0e47e81458aa0a51b94a6a62bd90fd8b6def45632c64.png)

Figure 1 is a left-to-right flow diagram set inside a single wide arrow labeled "ComStock simulation," showing how ground heat exchanger sizing is embedded in the ComStock run. Four boxes proceed in sequence: "Apply measure retrofitting existing system with GHP", "Initial load calculations", the external "GHEDesigner Tool" (drawn below the main arrow), and "Final simulation". The initial load calculations pass "Hourly ground loads for borefield sizing" down to GHEDesigner, and GHEDesigner returns a "g-function for ground heat exchanger" up to the final simulation. The diagram makes the two-pass structure explicit: ComStock must first simulate the retrofitted building to obtain ground loads, hand those to GHEDesigner to size the borefield, then re-simulate with the resulting g-function.

All figures created by the authors, unless noted otherwise.

