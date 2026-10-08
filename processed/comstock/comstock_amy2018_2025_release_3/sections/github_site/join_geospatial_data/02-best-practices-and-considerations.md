<!-- comstock comstock_amy2018_2025_release_3 | github_site | docs/resources/tutorials/join_geospatial_data.md | status: site_page | source_url: https://github.com/NatLabRockies/ComStock.github.io/blob/bacf551bc5d2f595d2b3c41a57de0beea23ec6be/docs/resources/tutorials/join_geospatial_data.md | publication_url: https://natlabrockies.github.io/ComStock.github.io/docs/resources/tutorials/join_geospatial_data.html | corpus_version: 0a2f61f | corpus_path: github_site/docs/resources/tutorials/join_geospatial_data.md | section: Best Practices and Considerations | lines: 19-76 -->
## Best Practices and Considerations

ComStock building characteristics are sampled at the county-level. As
such, the assignment of building characteristics (and corresponding
energy results) have a high level of confidence at geospatial
resolutions of county-level and larger (state, census region, climate
zone, etc.). ComStock data also includes more granular geospatial
information for each model using common geospatial units: U.S. Census
PUMAs and Tracts. As defined by the U.S. Census, PUMAs, or Public Use
Microdata Areas, are "non-overlapping, statistical geographic areas that
partition each state or equivalent entity into geographic areas
containing no fewer than 100,000 people each." Census Tracts are "small,
relatively permanent statistical subdivisions of a county or
statistically equivalent entity that can be updated by local
participants prior to each decennial census as part of the Census
Bureau's Participant Statistical Areas Program (PSAP)."

Census PUMA and Tract are assigned to ComStock models *after* sampling
based on building type and building floor area distributions. There are
many Tracts within a single county, as is the case for many PUMAs
especially in densely populated areas. Building characteristics and
energy results analyzed at these geographic levels therefore have
*lower* confidence. There are relatively few ComStock models in single
counties, and separating the models further can lead to unrealistic
results. For example, consider a single county with around 300 building
models in it representing 14 building types and 80+ other building
characteristics included in ComStock. When ComStock places these models
into PUMAs or Tracts, the size of the building and the type of the
building are considered, but nothing else. This can have unintended
consequences when using this data at a PUMA or Tract level.

To better explain these consequences, let's consider a county that has
multiple Secondary Schools. Each school likely has different interior
lighting technologies, including but not limited to LEDs. However, a
single Secondary School ComStock model may be assigned to a PUMA or
Tract, and for the sake of this example let us assume this school is
modeled with LEDs. None of the decisions on which ComStock models are
assigned to a PUMA or Tract relied on data sources specifying which
lighting technology belongs in which Census Tract or PUMA. This makes
statements like "All schools in PUMA/Tract X have LEDs" problematic. The
geographic resolution of the ComStock lighting system-type attribute is
specified at a higher geographic resolution than a Tract or PUMA. As
such, it is entirely possible that instead of LED lighting technology,
the school(s) in the Tract/PUMA have not been updated since the 1980s,
and vice versa.

While this example used interior lighting, this issue is relevant for
all ComStock model properties and should be considered for every
analysis at the sub-county geographic level.

All this to say: Take care when analyzing ComStock data and joining
external datasets to results at sub-county geographic levels. When
possible, join data at a county-level or larger.

\*\*Note: Future iterations of ComStock sampling will assign building
characteristics at more geographically granular levels. This document
will be kept up-to-date as new features are rolled out.

