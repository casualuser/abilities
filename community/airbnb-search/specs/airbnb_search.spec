# Airbnb Search & Browse Specifications

The tests below follow the implementation timeline mapped in `../../../.status/roadmap.md` and track tasks defined in `../../../.status/task.md`.
The backend responses comply with the API definitions in `openspec.yaml`.

## Search for an Airbnb Property
Tags: intent-search, core-v1

* User says "Find me an Airbnb in Nashville for next weekend under 200 a night"
* Capability should extract location "Nashville", budget "200", and correct dates
* Capability should read the top 3 results naturally including price, rating, and badges
