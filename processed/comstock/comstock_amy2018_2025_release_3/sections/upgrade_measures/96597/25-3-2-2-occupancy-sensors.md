<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/96597.pdf | status: osti_pdf | source_url: https://docs.nlr.gov/docs/fy26osti/96597.pdf | publication_url: https://docs.nlr.gov/docs/fy26osti/96597.pdf | corpus_version: fadc83e | corpus_path: upgrade_measures/measure_pdfs/96597.md | section: 3.2.2  Occupancy Sensors | lines: 302-407 -->
## 3.2.2  Occupancy Sensors

Occupancy sensors are more difficult to represent realistically in energy modeling. Occupancy is modeled in ComStock as an occupant density per space type. Occupancy schedules represent the fraction of the full occupancy that is present during each hour of the day. Occupancy schedules in the baseline are already coordinated with lighting schedules, such that when occupancy is low, the lighting schedule is likely already reduced at that time. In a way, this represents the concept of occupancy sensors but is more so just a reflection of manual or timed lighting controls in which the lights are turned off during nonbusiness hours. True occupancy controls would mean that lights could turn off periodically throughout the day in unoccupied spaces using sensors by monitoring sound, heat, or motion. This level of detail is very difficult to capture in energy models (which cannot accurately model the movement of people throughout a building).

ASHRAE 90.1-2019 (Table G3.1 - Modeling Requirements for Calculating Proposed and Baseline Building Performance) defines modeling requirements for automatic lighting controls, including occupancy sensors [11]. This methodology involves 'reducing the lighting schedule each hour by the occupancy sensor reduction factors in Table G3.7.' Table G3.7 - Performance Rating Method Lighting Power Density Allowances and Occupancy Sensor Reductions Using the Space-by-Space Method defines a percent reduction in LPD for many different space types [11]. The space types in Table G3.7 were mapped to ComStock space types to determine the percent LPD reduction to be applied in the model. Table 3 lists each space type modeled in ComStock building types (including DEER models, which are used in California buildings), as well as the percent LPD reduction due to occupancy sensors derived from ASHRAE 90.1-2019.

Table 3. LPD Reduction by Space Type as Defined in ASHRAE 90.1-2019 Table G3.7 [11]

| Building Type   | Space Type                |   % LPD Reduction |                  | OfficeLarge Main Data Center   | 0     |
|-----------------|---------------------------|-------------------|------------------|--------------------------------|-------|
|                 | Auditorium                |                10 |                  | Corridor                       | 25    |
|                 | Cafeteria                 |                35 |                  | Elec/MechRoom                  | 30    |
|                 | Classroom                 |                30 |                  | ElevatorCore                   | 0     |
|                 | ComputerRoom              |                25 |                  | Exercise                       | 35    |
|                 | Corridor                  |                25 |                  | GuestLounge                    | 0     |
|                 | Gym                       |                35 |                  | GuestRoom123Occ                | 0     |
|                 | Kitchen                   |                30 |                  | GuestRoom123Vac                | 45    |
|                 | Library                   |                15 |                  | Laundry                        | 10    |
|                 | Lobby                     |                25 |                  | Mechanical                     | 30    |
|                 | Mechanical                |                30 |                  | Meeting                        | 0     |
|                 | Office                    |                15 |                  | Office                         | 15    |
| SecondarySchool | Restroom                  |                45 |                  | PublicRestroom                 | 45    |
|                 | Cafeteria                 |                35 |                  | StaffLounge                    | 0     |
|                 | Classroom                 |                30 |                  | Stair                          | 75    |
|                 | ComputerRoom              |                25 | SmallHotel       | Storage                        | 45    |
|                 | Corridor                  |                25 |                  | Banquet                        | 35    |
|                 | Gym                       |                35 |                  | Basement                       | 0     |
|                 | Kitchen                   |                30 |                  | Cafe                           | 35    |
|                 | Library                   |                15 |                  | Corridor                       | 25    |
|                 | Lobby                     |                25 |                  | GuestRoom                      | 45    |
|                 | Mechanical                |                30 |                  | Kitchen                        | 30    |
|                 | Office                    |                15 |                  | Laundry                        | 10    |
| PrimarySchool   | Restroom                  |                45 |                  | Lobby                          | 25    |
|                 | WholeBuilding - Sm        |                   |                  | Mechanical                     | 30    |
| SmallOffice     | Office                    |                15 |                  | Retail                         | 0     |
|                 | WholeBuilding - Md Office |                15 | LargeHotel       | Storage                        | 45    |
|                 | OfficeLarge Data          |                   |                  | Bulk                           | 45 45 |
| MediumOffice    | Center                    |                 0 | Warehouse        | Fine Office                    | 15    |
|                 | WholeBuilding - Lg        |                   |                  | Back_Space                     | 10    |
|                 | Office                    |                15 |                  | Entry                          | 0     |
|                 | OfficeLarge Data          |                   |                  | Point_of_Sale                  | 0     |
| LargeOffice     | Center                    |                 0 | RetailStandalone | Retail                         | 10    |

|                        | Strip mall - type 1 10   |       |                            | Classroom              | 30    |
|------------------------|--------------------------|-------|----------------------------|------------------------|-------|
|                        | Strip mall - type 2      | 10    |                            | CorridorStairway       | 25    |
|                        | Strip mall - type 3 10   |       |                            | Dining                 | 35    |
|                        | Dining                   | 35    | DEER Education             | Gymnasium              | 35    |
| RetailStripmall        |                          | 30    |                            | Kitchen                |       |
|                        | Kitchen                  |       | Primary School             |                        | 30    |
|                        | Dining                   | 35    |                            | Classroom              | 30    |
| QuickServiceRestaurant | Kitchen                  | 30    |                            | CompRoomClassRm        | 25    |
| FullServiceRestaurant  | Dining                   | 35    |                            | CorridorStairway       | 25    |
|                        | Kitchen                  | 30    |                            | Dining Gymnasium       | 35    |
|                        | Basement                 | 0 25  | DEER Education             | Kitchen                | 35 30 |
|                        | Corridor Dining          |       | Secondary School           | OfficeGeneral          | 15    |
|                        |                          | 35 10 |                            | DEER                   |       |
|                        | ER_Exam ER_NurseStn      | 10    |                            | HospitalSurgOutptLab   | 10    |
|                        | ER_Trauma                | 10    |                            | Dining                 | 35    |
|                        | ER_Triage                | 10    |                            | Kitchen                |       |
|                        | ICU_NurseStn             | 10    |                            | OfficeGeneral          | 30    |
|                        | ICU_Open                 | 10    | DEER Hospital              | PatientRoom            | 15 10 |
|                        | ICU_PatRm                | 10    |                            | Dining                 | 35    |
|                        |                          | 30    |                            | BarCasino              | 35    |
|                        | Kitchen Lab              | 10    |                            | HotelLobby             | 25    |
|                        | Lobby                    | 25    |                            | OfficeGeneral          | 15    |
|                        | NurseStn                 | 10    |                            | GuestRmCorrid          | 25    |
|                        | Office                   | 15    |                            | Laundry                | 10    |
|                        | OR                       | 10    |                            | GuestRmOcc             | 0     |
|                        | PatCorridor              | 25    |                            | GuestRmUnOcc           | 45    |
| Hospital               | PatRoom                  | 10    | DEER Hotel                 |                        | 30 15 |
|                        | PhysTherapy              | 10 10 |                            | Kitchen OfficeGeneral  |       |
|                        | Radiology Anesthesia     | 10    |                            | GuestRmCorrid Laundry  | 25    |
|                        | BioHazard                | 10    |                            | GuestRmOcc             | 10    |
|                        | Cafe                     | 35    | DEER Motel                 | GuestRmUnOcc           | 0 45  |
|                        | CleanWork                | 10    |                            | LobbyWaiting           | 25    |
|                        | Conference               | 0 10  |                            | OfficeSmall OfficeOpen | 30    |
|                        | Elec/MechRoom            | 30    | DEER Office Large          |                        | 15    |
|                        | DressingRoom             |       |                            | MechElecRoom           | 30    |
|                        | ElevatorPumpRoom         | 0     |                            | Hall                   | 25    |
|                        | Exam                     | 10    | DEER Office Small          | OfficeSmall Dining     | 30 35 |
|                        | IT_Room                  | 25    |                            | Kitchen                |       |
|                        | Hall                     | 25    |                            |                        | 30    |
|                        | Janitor                  | 45    | DEER Restaurant Fast       | LobbyWaiting           | 25    |
|                        | Lobby                    | 25    | Food                       | Restroom               | 45    |
|                        | LockerRoom               | 25    |                            | Restroom               | 45    |
|                        | Lounge                   |       |                            | Dining                 | 35    |
|                        | MedGas                   | 0 10  | DEER Restaurant Sit        | LobbyWaiting           | 25    |
|                        | MRI                      | 10    | Down                       | Kitchen                | 30    |
|                        | MRI_Control              | 10    | Retail                     | RetailSales            |       |
|                        | NurseStation             | 10    | DEER Three Story           |                        | 0     |
|                        | Office OR                | 15 10 |                            | OfficeGeneral Work     | 15 10 |
|                        | PACU                     | 10    |                            | StockRoom              | 45    |
|                        |                          |       |                            | RetailSales            | 0     |
|                        | PhysicalTherapy          | 10 10 |                            | Kitchen                | 30    |
|                        | PreOp                    | 10    | DEER Retail Large          |                        |       |
|                        | ProcedureRoom            |       |                            | RetailSales            | 0     |
|                        | Reception                | 25    | DEER Retail Small          | StockRoom              | 45    |
|                        | Soil Work                | 10    | DEER Storage               |                        |       |
|                        | Stair                    | 75    | Conditioned                | WarehouseCond          | 45 45 |
|                        | Toilet Undeveloped       | 45 0  | DEER Storage Unconditioned | WarehouseUnCond        |       |

As a reminder, ComStock models several different types of lighting, including General Lighting, General Lighting (High Bay), Task Lighting, Supplemental Lighting, and Wall Wash Lighting. We made the decision to apply the occupancy sensor LPD reductions only to General Lighting

(including High Bay) objects in the model. This is because occupancy sensors are unlikely to be connected to task lights, wall wash lighting, or other forms of specialized supplemental lighting. The measure loops through each space and applies the percent LPD reduction to all General Lighting objects. As a result, the LPD will be reduced by the specified percentage during each hour of the day, in alignment with the ASHRAE 90.1 methodology for modeling occupancy sensors.

