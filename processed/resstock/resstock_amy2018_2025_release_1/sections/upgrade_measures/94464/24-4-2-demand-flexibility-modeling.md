<!-- resstock resstock_amy2018_2025_release_1 | upgrade_measures | measure_pdfs/94464.pdf | status: osti_pdf | source_url: https://docs.nlr.gov/docs/fy26osti/94464.pdf | publication_url: https://docs.nlr.gov/docs/fy26osti/94464.pdf | corpus_version: resstock_amy2018_2025_release_1-v1-pre | corpus_path: upgrade_measures/measure_pdfs/94464.md | section: 4.2  Demand Flexibility Modeling | lines: 307-314 -->
## 4.2  Demand Flexibility Modeling

This measure introduces flexible EV charging schedules through updates to the ResStockArgumentsPostHPXML workflow step. As shown in Figure 4, this step runs after the HPXML file has been created in the ResStock workflow, which enables adjustments for DF. This step accesses the HPXML building description and schedule files created in OpenStudioHPXML and modifies them as necessary prior to simulation. To model charging schedule flexibility for EVs, we extended ResStockArgumentsPostHPXML to include a new EV DF module. The following subsections describe how EV demand shifting is implemented within this framework.

Figure 4. ResStock workflow diagram showing the order in which measures are run. ResStockArgumentsPostHPXML allows for adjustments of building inputs and schedules during the baseline model generation or in a measure.

![Image](94464_images/image_000005_afa7a23e0660cf105bbf1256b614f3e85414163f6443d6924002b8385e5a4ccf.png)

