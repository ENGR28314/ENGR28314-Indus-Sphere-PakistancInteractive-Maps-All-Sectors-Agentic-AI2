# IndusSphere Pakistan — Interactive Maps and Sector Agentic AI

## Interactive map
1. Open **Interactive Pakistan Water Map**.
2. Choose a regional focus and enable/disable map layers.
3. Search for a river, dam, barrage, confluence, lake or mapped asset.
4. Scroll to zoom, drag to pan, hover over map features for details, and use the movable layer panel to control visibility.
5. Expand **Search results and mapped asset inventory** to inspect the filtered records.

Map coordinates and simplified linework are visualization references. They are not a replacement for authoritative GIS, survey, cadastral or engineering data.

## Agentic AI from every sector page
1. Open any sector page and expand **Sector Agentic AI — Ask, Analyse & Visualise**.
2. Select the sector playbook and write a custom question.
3. Set geographic scope and assessment horizon; add assumptions or constraints.
4. Upload CSV/Excel/PDF/text evidence where available.
5. Configure `GROQ_API_KEY` or `OPENAI_API_KEY` in Streamlit Secrets (recommended), or enter a key in the UI.
6. Confirm human review and run the Planner → Sector Analyst → Independent Reviewer workflow.
7. Read the generated answer and download its Markdown report.
8. When CSV/Excel evidence is attached, select fields and generate interactive bar, line, scatter or histogram charts, plus KPI cards and an optional indicator comparison graphic.

## Evidence and chart safeguards
- The LLM is instructed to distinguish measured, modelled, user-supplied, illustrative, inferred and unavailable values.
- Uploaded CSV/Excel data are the source for chart values. Narrative AI output is not automatically treated as a numeric dataset.
- The indicator comparison graphic should only be used when the compared units are compatible.
- No live operational control, emergency alerting, legal advice or certified engineering determination is performed.
- Verify sources, dates, units, coordinate accuracy and model assumptions before professional use.
