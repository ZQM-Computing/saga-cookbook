# SAGA Cookbook

<!-- ZQM-START -->
<!-- markdownlint-disable MD033 -->
<p align="center">
  <strong>ZQM Computing — Geospatial Engineering & Scientific Computing</strong><br>
  <a href="https://github.com/ZQM-Computing">ZQM Computing</a>
</p>
<!-- markdownlint-enable MD033 -->
<!-- ZQM-END -->

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

A **SAGA cookbook** for terrain analysis and geoscientific modeling from the command line. Patterns are drawn from the ZQM fleet's SAGA 9.12.4 installs (bundled with the QGIS stack). It is intended for GIS analysts who run terrain and grid tools in batch. Validate each pattern against your own data, software versions, and operating environment before adopting it.

## Repository role and status

**Status:** Active, public — seeding. Pattern passes land in follow-up work from fleet-verified setups; the tables below list what is planned, not what is already written.

**What this repository is:** SAGA patterns — see the table below.

**What it contributes:** Part of the ZQM Computing geospatial portfolio. The umbrella index for the series is [geospatial-cookbooks](https://github.com/ZQM-Computing/geospatial-cookbooks).

**Standing:** This repository is maintained independently. Automated checks cover only the paths and environments configured in its workflows; they do not establish production readiness or operational certification.

## Who this is for

GIS analysts who run terrain and grid tools in batch.

## Prerequisites

- SAGA 9.12.4 (saga_cmd)
- A DEM for your study area
- Bash

## Patterns (planned)

| # | Example | What it will demonstrate |
|---|---------|--------------------------|
| 01 | `01-cmd-basics` | Running saga_cmd tools and chaining them |
| 02 | `02-terrain-attributes` | Slope, aspect, curvature, and wetness from a DEM |
| 03 | `03-hydrology` | Flow routing and catchment tools |
| 04 | `04-grid-tools` | Resampling, mosaicking, and grid algebra |

## Repository layout

```text
saga-cookbook/
├── examples/          # pattern passes, landing in follow-up work
├── README.md
└── LICENSE
```

## Roadmap

- First pattern pass: the first two table rows
- Second pass: the remaining rows, from fleet-verified setups

## Contributing

A contributing guide lands with the first pattern pass. Report security issues to <zqmcomputing@gmail.com> — please do not open a public issue for those.

## More from this series

- [grass-cookbook](https://github.com/ZQM-Computing/grass-cookbook) — Geoscientific analysis, terrain, and watershed modeling
- [whitebox-cookbook](https://github.com/ZQM-Computing/whitebox-cookbook) — Terrain and hydrology analysis from the command line
- [gdal-cookbook](https://github.com/ZQM-Computing/gdal-cookbook) — GDAL/OGR conversion, reprojection, and raster/vector utilities
