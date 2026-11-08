# IndusSphere Pakistan — Integrated Water, Climate & Strategic Intelligence Explorer

**Creator:** Engr. Syed Hassan Iqbal Shah ![Pakistan Engineering Council monogram](https://upload.wikimedia.org/wikipedia/commons/e/ea/Peclogo.jpg) (ELECT/28314) ![ISPR Pakistan monogram](https://upload.wikimedia.org/wikipedia/commons/2/2d/Ispr_new_logo.jpg) **Dedicated to ISPR**

A reference-style Streamlit dashboard for Pakistan's provinces/territories, rivers, dams, barrages, link canals, lakes, deserts, climate regions, mountain systems, forests, parks, disaster-risk context, socio-economic/agro-economic analysis, hydropower portfolios, IWT research, ESG/ISO/SDG/MDG/Vision 2030 alignment, and input-driven analytics.


## Agentic AI Command Centre (CrewAI)

The **🤖 Agentic AI Command Centre (CrewAI)** runs a sequential three-agent workflow: (1) planning and evidence-gap analysis, (2) domain-specific technical analysis, and (3) independent risk/evidence review. The user supplies the goal and context, chooses Groq or OpenAI, confirms human review, and can download the final report as Markdown. The workflow is advisory; it does not control infrastructure, send alerts, perform live web research, or establish legal conclusions.

### Configure the LLM provider

- Install dependencies with `pip install -r requirements.txt`.
- For Groq, configure `GROQ_API_KEY` in Streamlit Community Cloud **App settings → Secrets** or enter it in the Agentic AI page. The default model option is `llama-3.3-70b-versatile`; choose a model currently available to your Groq account if that changes.
- For OpenAI, configure `OPENAI_API_KEY` in Streamlit Secrets or enter it in the page.
- A blank `.streamlit/secrets.toml` template is included for local development and is excluded from Git by `.gitignore`. Add your own keys locally. For Streamlit Cloud, paste the required key/value pairs into **App settings → Secrets**. Never commit real API keys to GitHub. `.streamlit/secrets.toml.example` contains placeholders only.
- Review all generated recommendations and independently verify engineering calculations, current statistics, citations, legal interpretations and safety-related claims.

## Provinces / territories
- Gilgit-Baltistan
- Khyber Pakhtunkhwa (KPK/KP)
- Punjab
- Sindh
- Balochistan
- Azad Jammu & Kashmir
- Islamabad Capital Territory (ICT)

## Main modules
- Water and terrain inventory: rivers, upstream/downstream relationships, confluences, dams, barrages/headworks, link canals, lakes and deserts.
- Climate regions: Temperate, Tropical, Polar, Arid and Highland.
- Mountain ranges: Northern Highlands (Karakoram, Himalayas, Hindu Kush, Hindu Raj) and Western/Southern Border Ranges (Spīn Ghar/Koh-e-Safed, Sulaiman, Kirthar, Toba Kakar, Salt Range), with peaks, geology, tourism and rivers.
- Disaster-risk context: hydro-meteorological, tectonic, climatological/emerging, anthropogenic, exposure/vulnerability and scenario definitions.
- Socio-economic: food security, employment, urban growth, tourism, domestic/industrial utility, climate vulnerability and energy generation.
- Agro-economic: IBIS, Rabi/Kharif crop seasons, crop types, apiculture, aquaculture and editable regional data.
- Geo-political/strategic: Kashmir hydro-politics, Punjab-Sindh water disputes, IRSA/CCI/Article 155, maritime trade, CPEC hydropower and Indian upstream project/IWT research.
- China hydropower: Karot, Suki Kinari, Kohala and Azad Pattan project portfolio.
- India upstream/IWT: Pakal Dul, Ratle, technical issues, Head Marala/crop-impact documentation and PCA timeline.
- IWT legal/data exchange: Article VI/VIII/IX baseline, exchange audit, timeline, evidence and descriptive dispute-resolution pathways.
- Forests and parks: forest types, notable forests, national/protected/recreational areas, and representative-location park maps in the **Select a park for details** tab.
- ESG / ISO / UN SDGs / MDGs / Vision 2030 crosswalk.
- Engineering simulation engines: hydrology, flood, crop-water, climate, Monte Carlo and network routing.
- File analytics: CSV, PDF, XLSX and XLS; selectable-text/table PDFs plus OCR pathway for scanned PDFs.
- Graphs: bar, pie, scatter and line charts from actual uploaded or edited data.
- River-basin telemetry: average variance by basin and downloadable Python visualization script.
- Water quality: dissolved oxygen (DO), pH, turbidity, TDS, conductivity, temperature, nitrate, BOD, COD and coliform when present in uploaded data.
- Spatial uploads: CSV/PDF/Excel data can be mapped when latitude/longitude fields are present.
- Indus Delta environmental analytics reference: EMI survey, interpolated EC, pH, ESP and soil salinity.

## Run locally
```bash
pip install -r requirements.txt
streamlit run app.py
```

Windows helper: `run_app.bat`

## Streamlit Community Cloud
Use `app.py` as the main file and keep `requirements.txt` and `packages.txt` in the repository root. `packages.txt` includes the system dependency used by the OCR pathway.

## Important data/legal note
The application distinguishes source-derived facts, party positions, reported concerns, model calculations and uploaded evidence. In particular, IWT and Indian-project sections do not automatically determine legal violations or causation. Use the current treaty text, PCA awards/orders, authoritative project documents and hydrological datasets for formal analysis.

Map points are representative visualization coordinates unless a source explicitly provides a boundary. They are not cadastral or engineering survey data.

## Streamlit Community Cloud deployment checklist

1. Upload the **contents** of this folder to the root of a GitHub repository.
2. Confirm that `app.py`, `requirements.txt`, `packages.txt`, `runtime.txt`, and `.streamlit/config.toml` are in the repository root.
3. In Streamlit Community Cloud, choose **Deploy an app**, select the repository and branch, and set the main file to `app.py`.
4. Wait for dependency installation. The first build may take longer because PDF/OCR dependencies are installed.
5. If you do not need scanned-PDF OCR, you may remove `pytesseract`, `Pillow`, `PyMuPDF`, and `packages.txt`; CSV, XLSX, XLS, and selectable-text PDF workflows will still be available.

### Troubleshooting

- **ModuleNotFoundError:** verify that every `.py` file is in the same repository root as `app.py`.
- **Excel upload error:** keep both `openpyxl` and `xlrd` in `requirements.txt` for `.xlsx` and legacy `.xls` support.
- **Scanned PDF OCR warning:** confirm that `packages.txt` contains `tesseract-ocr`; OCR is a fallback and may be slower than normal text extraction.
- **Large upload rejected:** the included Streamlit configuration allows uploads up to 200 MB, subject to the hosting platform's own limits.
- **Slow first load:** Streamlit installs dependencies during the first deployment; subsequent runs should be faster.

The models are screening/educational tools. Validate engineering, legal, environmental, and statistical conclusions against authoritative data before professional use.

## Expanded simulation and agro-economic modules

The Streamlit-ready package now includes additional executable Python modules:

- `hydrology_engine.py` — reservoir and water-balance screening
- `flood_engine.py` — rainfall/runoff and flood-capacity screening
- `crop_water_engine.py` — Rabi/Kharif crop-water requirements
- `climate_engine.py` — climate scenario/sensitivity screening
- `monte_carlo_engine.py` — uncertainty simulation
- `network_engine.py` — river/canal network routing
- `additional_simulation_engines.py` — groundwater, drought, sediment, water-quality, irrigation and socio-agro projection engines
- `iwt_compliance_engine.py` — IWT data-exchange documentation screening
- `iwt_timeline_engine.py` — documented PCA/IWT timeline
- `iwt_evidence_engine.py` — evidence ledger
- `iwt_scenario_engine.py` — IWT scenario matrix
- `simulation_registry.py` — central executable-engine catalog

The Agro-Economic domain now contains explicit Rabi/Kharif tables with the requested fields `season`, `crop`, `typical_window`, and `engineering_water_note`, plus structured Apiculture and Aquaculture indicator tables.

The Socio-Economic and Agro-Economic domains share an editable input table with province/region, cultivated area, crop production, employment, honey production and aquaculture production. Users can choose Bar, Pie, Scatter or Line charts and the requested metric fields. A separate projection engine responds to the entered data and annual change assumption.

The Parks Details tab shows an interactive representative-location map with a highlighted selected-park marker.

### Streamlit deployment note

`requirements.txt` explicitly includes NumPy because the Monte Carlo engine uses it. `runtime.txt`, `packages.txt`, and `.streamlit/config.toml` are included for Streamlit Community Cloud deployment.

## WAPDA telecommunication network integration

This release adds `telecommunication.py` and `telecom_network_engine.py` plus the two supplied WAPDA PDF source documents under `source_documents/`.

The app includes a new **📡 WAPDA Telecommunication Networks** section covering:
- High Frequency Radio Network — Western Rivers
- Wireless Network — Eastern Rivers
- source-document traceability and CSV exports
- visualization-only approximate map points where a named location could be mapped; these coordinates are explicitly not claimed to come from the PDFs

The supplied diagrams list network locations but do not define GIS coordinates or an explicit link topology, so the application does not invent network connections.


## Pakistan Solar Projects
The application now includes a dedicated `☀️ Pakistan Solar Projects` section and a solar layer on the interactive Pakistan map. The dataset covers Punjab, Sindh, Khyber Pakhtunkhwa, Balochistan, Gilgit-Baltistan, Azad Jammu & Kashmir and Islamabad Capital Territory. It distinguishes utility-scale PV, institutional/public-sector solarization, agricultural solarization, mini-grids and solar-home-system programs. Capacity is source-derived where published; otherwise it is intentionally left unspecified.

## Solar Map Label-Overlap Fix (2026-10-05)

The Pakistan solar map now uses a collision-safe label strategy for all seven represented administrative regions (Punjab, Sindh, Khyber Pakhtunkhwa, Balochistan, Gilgit-Baltistan, Azad Jammu & Kashmir, and Islamabad Capital Territory).

- All solar projects remain visible as markers.
- Project names are available on hover instead of being printed over every marker.
- A single project can be selected for a permanent highlighted label.
- The dedicated solar page includes province/region, status, and solar-type filters.
- No project names are inferred or repositioned; the source inventory remains unchanged.

## Simulated Live Weather, Rainfall & 12-Month Telemetry

The project now includes `weather_hydraulic.py` and `telemetry_engine.py` for transparent synthetic screening at:
- Sialkot — Chenab basin
- Jhelum — Jhelum basin
- Lahore — Ravi basin

The module provides simulated current weather/rainfall, river discharge, water level, hydraulic hazard screening and 12 monthly telemetry observations. These values are explicitly synthetic and are not operational observations or flood warnings.

## 🛰️ SEBAL Evapotranspiration — Indus Basin

The project now includes a Google Earth Engine + geemap + GeoPandas evapotranspiration workspace based on the **Surface Energy Balance Algorithm for Land (SEBAL)**.

### Workflow

1. Authenticate and initialize Google Earth Engine.
2. Identify the Indus main basin chain from **WWF HydroSHEDS Level 7** using the Indus outlet point.
3. Inspect the basin geometry locally with **GeoPandas**.
4. Query **Landsat 8/9 Collection 2 Level 2** surface reflectance and land-surface temperature.
5. Query **ERA5-Land hourly** radiation, air temperature and wind fields.
6. Estimate albedo, NDVI, emissivity, net radiation, soil heat flux, sensible heat flux, latent heat flux and instantaneous ET rate.
7. Visualize ET, land-surface temperature, NDVI and the basin boundary through **geemap**.
8. Export basin-level statistics as CSV.

### Important scientific note

This is a transparent **SEBAL-style research implementation** for the Indus Basin. It is not represented as a locally calibrated or independently validated operational SEBAL product. Hot/cold pixel selection, aerodynamic resistance, emissivity and atmospheric inputs should be validated against appropriate Pakistan/Indus Basin observations before use for operational irrigation scheduling, water accounting or engineering decisions.

The official Earth Engine catalog contains OpenET **geeSEBAL**, an Earth Engine implementation of SEBAL, but the catalogued OpenET geeSEBAL products are CONUS-focused. Therefore this project does not incorrectly apply the CONUS asset to Pakistan; instead it computes the energy balance directly over the Indus Basin using globally available Landsat and ERA5-Land inputs.

### Authentication

For local development/Colab, authenticate Earth Engine once with the Earth Engine Python client and initialize it with a Google Cloud project. For deployed applications, use an appropriate secure Google Cloud/Earth Engine credential mechanism and never commit private keys to the repository.

### Upload CSV/Excel analytics in the SEBAL page (added 2026-10-09)

The SEBAL page now has two independent parts:

**A. Upload data — charts, analytics and coordinate map**
- Upload CSV, XLSX or XLS files without authenticating Earth Engine.
- Select one file or combine multiple uploads into a single table (a `source_file` field is added to help track records).
- Build interactive bar charts (sum/mean/count), pie charts, scatter plots and line charts from the uploaded columns.
- If latitude/longitude fields are detected (including common `lat`/`lon`, `latitude`/`longitude`, `lng`, decimal-coordinate and `x`/`y` aliases), the page displays an interactive map and allows download of valid mapped rows.
- Invalid or missing coordinates are excluded from the map, not deleted from the original dataset.
- Download the analysed table as CSV.

**B. Satellite-based SEBAL model (Google Earth Engine)**
- Requires a registered Earth Engine project and authorized credentials.
- Select single-scene or monthly composite processing, then run the Landsat/ERA5-Land energy-balance workflow.
- Uploaded data analytics do not automatically calculate ET. They visualize the fields present in the file; satellite SEBAL ET is computed by the authenticated GEE workflow.

`sample_sebal_upload.csv` is an illustrative template for field names and map/chart behaviour. Its values are examples for interface testing, not observed or validated evapotranspiration measurements.

### Indus Waters Treaty reference modules
The sidebar now includes six additional reference pages: **1960 Dam Design**, **Western Rivers Pakistan**, **IWT Main points**, **Impact on Transboundary Water Cooperation**, **The IWT Treaty**, and **Article XII(3) Modification by Consent**. These pages summarize the Treaty and relevant engineering/cooperation concepts in neutral language, provide primary-source links, and include the user-supplied Article XII(3) infographic on the matching page. Legal positions are attributed rather than presented as dashboard adjudications.


## Expanded river inventory (9 October 2026)
The Rivers section now includes the additional river/stream names and aliases requested by the project owner, including upper-Indus tributaries, KP rivers, western Balochistan drainage, and the Hakra palaeochannel. It also includes the Hunza–Gilgit, Shyok–Indus and Ravi–Chenab confluences, plus Jinnah Barrage and Kurram Tangi Dam in the infrastructure inventory. Smaller-stream basin descriptions and schematic map traces are indicative and should be checked against official hydrography before engineering use.

## PEC and ISPR Branding

The dashboard displays the Pakistan Engineering Council (PEC) emblem and the ISPR Pakistan logo in the sidebar and header. The project dedication reads **Dedicated to ISPR**. The ISPR logo is referenced from [Wikimedia Commons — Ispr new logo.jpg](https://commons.wikimedia.org/wiki/File:Ispr_new_logo.jpg); the PEC emblem is referenced from [Wikimedia Commons — Peclogo.jpg](https://commons.wikimedia.org/wiki/File:Peclogo.jpg). The use of these emblems is for project identification/dedication and does not imply official sponsorship, endorsement, or affiliation by PEC or ISPR.

Project creator: **Engr. Syed Hassan Iqbal Shah** [Pakistan Engineering Council monogram](https://commons.wikimedia.org/wiki/File:Peclogo.jpg) **(ELECT/28314)** [ISPR Pakistan monogram](https://commons.wikimedia.org/wiki/File:Ispr_new_logo.jpg) **Dedicated to ISPR**.


## Strategic Water Security, Flood Response & Agricultural Water Governance

A new sidebar module covers Pakistan's stated IWT / water-security position, dated flood-relief reporting, SIFC / Green Pakistan Initiative / LIMS programme descriptions, corporate farming and land-review issues, and inter-provincial canal disputes. It includes a downloadable claim-by-claim evidence register.

**Evidence handling:** statements are attributed to the institution making them; news reports are identified as reporting; supplied figures (including water-use shares, water-loss percentages, irrigation savings, acreage, investment amounts and profit-sharing terms) are labelled for verification unless a primary source is attached. Dated court reporting is not presented as current legal status.

Module source review date: 21 October 2026.


## Mining & Dry Fruit Sectors

The interactive `⛏️ Mining & Dry Fruit Sectors` page covers mineral-resource profiles, selected projects, provincial-governance review prompts, dry-fruit and dates value chains, export-compliance checklists, and supporting source links. Several numerical figures supplied in the project brief are explicitly marked provisional and should be checked against current official sources.

## Creator and institutional attribution
The dashboard includes the supplied engineer portrait in the footer, followed by three credit rows: **Created by Engr. Syed Hassan Iqbal Shah**, **PEC: ELECT/28314**, and **Dedicated to ISPR**. The portrait is bundled under `assets/engr_syed_hassan_iqbal_shah.jpg`. The footer's PEC/ISPR circles are clearly labeled emblem placeholders; replace them with official authorized logo image files if exact official artwork is required.

## Dashboard reference image and creator footer

The app bundles the user-provided dashboard reference image at `assets/dashboard_reference.png` and the engineer portrait at `assets/engineer_portrait.jpg`. Open **“View supplied dashboard reference image”** near the bottom of the app to view the reference. The app footer displays the creator credit, PEC registration line, and ISPR dedication. The reference image is a design guide; maps, filters, sector navigation, charts, and analysis tools remain interactive Streamlit components.


### Header portrait fix (2026-10-24)
The creator portrait is rendered with Streamlit `st.image()` using a path resolved relative to `app.py`; it no longer relies on an HTML data-URI image, avoiding broken-image icons in the header. Deploy the complete `build_final` folder, including `assets/`.


## Dam Gross Command Area (GCA) and Cultivable Command Area (CCA)

The **Dams & Barrages** page now includes editable GCA and CCA fields for each dam/associated irrigation command. Both values are recorded in hectares. The page validates that CCA does not exceed GCA, calculates CCA/GCA percentage and the non-cultivable portion of GCA, provides a chart and CSV export, and preserves user-entered values during the Streamlit session.

No missing command-area values are fabricated. Enter values only from verified WAPDA, provincial Irrigation Department, project feasibility, or other traceable engineering records. A sample template is included as `sample_dam_command_areas.csv`. Reusable calculations are in `command_area_engine.py`; tests can be run with `python -m unittest test_command_area_engine.py -v`.

### Reservoir storage–command-area matching and Punjab examples (2026-11-08)

The **Dams & Barrages** page now explains the engineering workflow for matching live reservoir storage to an irrigation command and includes an interactive screening calculator. The calculator estimates gross seasonal demand as `CCA × net seasonal irrigation depth ÷ overall irrigation efficiency`, converts acre-feet to cubic metres, and compares the result with user-entered available live storage. Its defaults are illustrative inputs only; crop-wise demand, dependable inflows, reservoir operating rules, canal capacity, environmental releases, sedimentation and multi-season reliability must be assessed for a real scheme.

A source-labelled reference table is included in `reference_dam_cca_punjab.csv`. It reproduces selected dam-specific CCA and live-storage figures published by the Government of Punjab's Jhelum district small-dams page. Where the page does not provide live storage, the field is blank. These examples are not substituted for the GCA/CCA values of the major dams in the national dam inventory. Verify design values against current PC-I, feasibility, completion and Irrigation Department records before professional use.

Source: https://jhelum.punjab.gov.pk/small_dams


## Reservoir DEM & Storage–Elevation Analysis

The **Reservoir DEM & Storage–Elevation Curves** page accepts a georeferenced DEM GeoTIFF and a reservoir basin / maximum-pool boundary in GeoJSON (EPSG:4326 longitude/latitude). It reprojects the DEM to a selected Pakistan WGS 84 / UTM CRS (EPSG:32641, 32642 or 32643), transforms the boundary using explicit longitude/latitude axis order, and rasterizes that boundary on the same output grid. It then estimates water-surface area and storage at user-selected elevation intervals and provides CSV and interactive Plotly curves.

**CRS guidance:** EPSG:4326 is suitable for coordinate exchange, not planar area/volume calculations. UTM 41N/42N/43N are local metric choices according to longitude. EPSG:3857 is intended for web display, not engineering area/volume. Legacy Kalianpur coordinates must not be re-labelled as WGS 84; verify datum and transformation metadata first.

**Coordinate integrity and limitations:** the DEM must have correct CRS/geotransform metadata and metre-based elevations. The GeoJSON boundary is assumed to be EPSG:4326. The analysis warps the DEM once, then rasterizes the transformed polygon using the exact same affine grid to avoid separate-grid alignment drift. Confirm the DEM vertical datum, pixel resolution, NoData coverage, boundary overlap and survey control points. The output is a terrain-derived estimate and does not model sedimentation, seepage, outlet hydraulics, operational rules or surveyed reservoir capacity.


### Extracting Storage-Elevation Curves Without Coordinate Drift

The Reservoir DEM page includes an explicit engineering workflow and alignment audit. It transforms the GeoJSON boundary to the selected Pakistan UTM CRS using explicit longitude/latitude axis order, warps the DEM once, and rasterizes the polygon on the exact same affine grid and dimensions. The output reports the analysis transform, pixel size, bounds, projected/rasterized boundary area, valid DEM area and valid-data coverage. It rejects boundaries that do not overlap the DEM and warns when valid-data coverage is below 95%. Review `STORAGE_ELEVATION_NO_COORDINATE_DRIFT_GUIDE.md` for input preparation, equations, quality checks and limitations.

The calculation assumes elevations in metres and does not automatically transform vertical datums. Confirm the DEM vertical datum against survey/gauge levels. For large or multi-zone reservoirs, do not force a single UTM zone without geodetic review. This is a terrain-derived estimate, not a replacement for bathymetry or official capacity surveys.

## Integrated Water Resources, Hill Torrents & Groundwater Recharge (2026-11-08)

A new sidebar page, **💧 Integrated Water Resources & Groundwater Recharge**, adds eight tabs:

- **Hill Torrent Conservation:** culturable-wasteland area and annual conservation-potential table by region, source subtotals, charts and CSV export.
- **Aquifer Recharge Methods:** spreading basins, recharge pits, ditches/trenches, recharge wells, conjunctive use/wells and percolation tanks / earthen bunds; includes hydrogeological suitability, pretreatment, clogging, water-quality and maintenance considerations.
- **Proposed Indus Storage:** Bunji, Diamer Bhasha, Dasu, Thakot HPP, Pattan, Yulbo, Tungus, Skardu and Shyok/Yugo, with supplied storage and status fields.
- **Population vs Water Availability:** 1951, 2010, 2020 and 2025 population and per-capita availability series, with the commonly cited 1,000 m³/person/year water-stress threshold.
- **Average Annual River Flows:** historical Western Rivers (145 MAF), Eastern Rivers (27 MAF) and combined pre-1947 context (172 MAF) as stated in a 2015 PBC/PEF presentation, plus CSV upload/template for verified river- or gauge-specific flow data. Individual tributary flow figures are not fabricated.
- **Reservoir Sedimentation:** original capacity, 2009 remaining capacity/loss and cumulative loss estimates for 2012 and 2025 for Tarbela, Mangla and Chashma.
- **Integrated Reservoir Management:** supplied historical Kotri-flow and potential-development figures with explicit assumptions and limitations.
- **River Flows and Storage Potential:** a combined comparison of historical river-system flow references and the proposed storage portfolio, with interactive charts, source-labelled tables, downloadable reference data and separate CSV uploads for updated flow and storage records. A storage-to-annual-flow ratio is shown only as a volume comparison—not as dependable yield or water availability.

### Data reconciliation and provenance

The supplied hill-torrent table repeats FATA under both the Federal and NWFP/KP subtotals. The grand total is reconciled by counting the FATA row once: 6,935,560 ha, 17,130,833 acres, 18.690 MAF and 23,036 MCM. The page retains the two original subtotal rows and flags the duplicate instead of silently rewriting the source.

The nine supplied proposed Indus storage values total 18.04 MAF, while the source-reported total is 18.50 MAF. The 0.46 MAF difference is displayed as an unresolved discrepancy; no project value is adjusted.

The population/per-capita series and historical river-group flow figures are cross-checked against the [Pakistan Business Council / Pakistan Economic Forum Water Presentation](https://www.pbc.org.pk/wp-content/uploads/Water-Presentation-PEF-III-.pdf). That 2015 presentation states 145 MAF for the Western Rivers, 27 MAF for the Eastern Rivers, and a combined 172 MAF in a pre-14 August 1947 context; these are historical presentation figures, not current gauge measurements or a modern climatological normal. The 1,000 m³/person/year threshold is a broad water-stress indicator associated with Falkenmark & Widstrand (1992), not a full measure of water security.

The sedimentation values are historical estimates from a published table and related proceedings: [Journal of Climate and Community Development](https://www.joccd.com/index.php/joccd/article/download/33/29/75) and [8th Asian Regional Conference proceedings](https://www.dwri.gov.np/files/document/20210419071354.pdf). The 2025 values are estimates/projections in the historical literature, not a new hydrographic survey. For current reservoir capacity, use the latest WAPDA hydrographic survey and official operating data.

The supplied hill-torrent, proposed-storage-project and IWRM/Kotri planning figures did not include a traceable original source document. They are identified in the application as project-owner-supplied historical/reference data and require source verification before formal planning use.

For river flows, 145 MAF/year is displayed only as a historical basin/system aggregate reference, not as a present-year measured flow or an individual tributary/gauge value. Users can upload verified gauge-level data using `average_annual_indus_basin_flows_template.csv` and `average_annual_indus_basin_flows_reference.csv`.

### New modules and files

- `water_resources_engine.py` — structured reference datasets and arithmetic reconciliation checks.
- `test_water_resources_engine.py` — tests for FATA deduplication, proposed-storage discrepancy, population threshold and sedimentation totals.
- `hill_torrent_conservation_potential.csv`
- `proposed_indus_storage_projects.csv`
- `population_water_availability.csv`
- `reservoir_sedimentation_reference.csv`
- `aquifer_recharge_methods.csv`
- `average_annual_indus_basin_flows_template.csv`
- `river_flows_storage_potential_reference.csv` — combined historical flow and proposed storage comparison reference.

Run the full automated test suite from the project root with `pytest -q`.

**Additional hill-torrent unit check:** the supplied grand total reports 18.690 MAF and 23,036 MCM. Using 1 MAF = 1,233.48184 MCM, 18.690 MAF is approximately 23,059 MCM, a difference of about 23 MCM from the reported figure. The app retains both supplied values and flags this small conversion discrepancy for source review.

## Interactive Map & All-Sector Agentic AI Upgrade (2026-11-08)

- The **Interactive Pakistan Water Map** now includes a dedicated asset search field, search-filtered inventory tables, clearer map-use guidance, and retains the draggable/collapsible layer legend, regional focus, layer toggles, hover details, pan and scroll zoom.
- A reusable **Sector Agentic AI — Ask, Analyse & Visualise** workspace is available from every sector page (inside an expander). Select any sector playbook, type a custom decision question, set geography and assessment horizon, attach evidence, and run the CrewAI Planner → Analyst → Reviewer workflow.
- Sector AI answers are displayed in the app and can be downloaded as Markdown. CSV/Excel evidence is separately rendered as interactive bar, line, scatter or histogram charts, with pictorial KPI summaries. PDF/text evidence informs the written analysis but is not silently converted into fabricated numerical chart data.
- Configure `GROQ_API_KEY` or `OPENAI_API_KEY` in Streamlit Secrets, or enter a key in the sector workspace. Never commit keys to GitHub.
- AI responses are decision-support drafts requiring human review. Charts use uploaded table values; units, time periods, geographic coverage and source provenance should be checked before interpretation.

## Indus Plain table rendering fix (2026-11-08)
- Corrected the **Upper versus Lower Indus Plain** comparison table. Four rows had been written as Python sets rather than dictionaries, which caused a Pandas `AttributeError` during page rendering.
- All five rows now use consistent `Feature`, `Upper`, and `Lower` columns.
- Checked all `pd.DataFrame([...])` literal rows in `app.py` for set entries; none remain.
- Verified Python compilation and the project test suite (27 passed).
