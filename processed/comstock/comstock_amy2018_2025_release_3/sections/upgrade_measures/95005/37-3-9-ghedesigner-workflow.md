<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/95005.pdf | status: osti_pdf | source_url: https://docs.nlr.gov/docs/fy25osti/95005.pdf | publication_url: https://docs.nlr.gov/docs/fy25osti/95005.pdf | corpus_version: 0a2f61f | corpus_path: upgrade_measures/measure_pdfs/95005.md | section: 3.9 GHEDesigner Workflow | lines: 652-668 -->
## 3.9 GHEDesigner Workflow

GHEDesigner is a software tool available as a Python package for designing ground heat exchangers used with GHP systems [20]. The GHP upgrade measures leverage GHEDesigner for sizing the vertical ground heat exchangers used in the ComStock models. GHEDesigner is executed within the GHP measures. Figure 1 shows the full ComStock GHP measure workflow. First, the GHP measure is applied , which replaces the existing system with one of the GHP configurations. An initial sizing run determines the annual loads the ground heat exchanger needs to supply. The ground loads are exported to GHEDesigner in the form of a JavaScript Object Notation (JSON) file. GHEDesigner then performs calculations to determine the size of the ground heat exchanger in the model. A final EnergyPlus ®  simulation is performed with the ground heat exchanger size set to the value determined by GHEDesigner. See the individual measure documents (Central Hydronic GHP, Packaged GHP, Console GHP) for more detail about the GHEDesigner workflow.

Figure 1. ComStock GHEDesigner workflow

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/95005.yaml
     source: 95005_images/image_000004_ae54adc04ee9dd19149b9e25877f84978407b7eeb5cb47efc268eac589b3353d.png
     method: vision-description
     described: 2026-08-21 -->

![Flow diagram of the ComStock GHEDesigner workflow for sizing ground heat exchangers](95005_images/image_000004_ae54adc04ee9dd19149b9e25877f84978407b7eeb5cb47efc268eac589b3353d.png)

Figure 1: left-to-right flow diagram of the ComStock GHP simulation workflow. Boxes run from applying the measure that retrofits the existing system with a GHP, through initial load calculations, out to the GHEDesigner tool and back to a final simulation; the arrows are labeled hourly ground loads for borefield sizing and g-function for ground heat exchanger. Section 3.9 walks through the same steps.

All figures created by the authors, unless noted otherwise.

