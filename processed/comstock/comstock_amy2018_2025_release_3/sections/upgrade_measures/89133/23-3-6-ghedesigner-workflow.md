<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/89133.pdf | status: osti_pdf | source_url: https://www.nlr.gov/docs/fy24osti/89133.pdf | publication_url: https://www.nlr.gov/docs/fy24osti/89133.pdf | corpus_version: 267e3ea | corpus_path: upgrade_measures/measure_pdfs/89133.md | section: 3.6 GHEDesigner Workflow | lines: 273-287 -->
## 3.6 GHEDesigner Workflow

GHEDesigner is a software tool available as a Python package for designing ground heat exchangers used with GHP systems [17]. The GHP upgrade measures leverage GHEDesigner for sizing the vertical ground heat exchangers used in the ComStock models. GHEDesigner is executed within the GHP measures. Figure 1 shows the full ComStock GHP measure workflow. First, the GHP measure is applied, which replaces the existing system with one of the GHP configurations. An initial sizing run determines the annual loads the ground heat exchanger needs to supply. The ground loads are exported to GHEDesigner in the form of a JavaScript Object Notation (JSON) file. GHEDesigner then performs calculations to determine the size of the ground heat exchanger in the model. A final EnergyPlus simulation is performed with the ground heat exchanger size set to the value determined by GHEDesigner. See the individual measure documents for more detail about the GHEDesigner workflow.

Figure 1. ComStock GHEDesigner workflow

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/89133.yaml
     source: 89133_images/image_000008_96b39ad802ac5caae47ce0c949a1cca564ada875ec7a4f4268ad476072bf4e86.png
     method: vision-description
     described: 2026-08-20 -->

![Process flow diagram of the ComStock GHEDesigner workflow for sizing geothermal heat pump ground loops](89133_images/image_000008_96b39ad802ac5caae47ce0c949a1cca564ada875ec7a4f4268ad476072bf4e86.png)

Figure 1. Process flow diagram titled 'ComStock simulation' of the GHEDesigner workflow. The flow: 'Apply measure retrofitting existing system with GHP' leads to 'Initial load calculations', which passes hourly ground loads for borefield sizing to the 'GHEDesigner Tool'; the GHEDesigner Tool returns a g-function for the ground heat exchanger, feeding the 'Final simulation'. Illustrates how ComStock couples an initial load-calculation pass with the external GHEDesigner tool to size the borefield before the final energy simulation.

