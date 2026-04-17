# Interactive Dashboards Project

This repository contains my current prototype work for the Brainhack project on interactive MRI surface dashboards.

## Project goal

The goal of this prototype is to explore how to build an interactive dashboard for MRI surface-based stats maps. The intended dashboard should allow users to:

- select a hemisphere
- select an ROI from an atlas
- load and visualize the corresponding surface-based stats map on a template brain

This project also explores tool choices for this workflow, especially Marimo, Nilearn, and ipyniivue / Niivue.

## What this prototype currently does

The current notebook explores how to:

- load fsaverage cortical surfaces with Nilearn
- read FreeSurfer `.annot` atlas files with NiBabel
- visualize atlas ROIs on surfaces such as `pial_left` and `infl_left`
- create an interactive brain view with `nilearn.plotting.view_surf`
- display a separate text legend for ROI names
- browse ROI names with a dropdown in Marimo

## What currently works

- fsaverage surface loading with Nilearn
- `.annot` atlas loading with NiBabel
- ROI name extraction from the atlas
- interactive brain visualization with `nilearn.plotting.view_surf`
- separate text legend for ROI names
- ROI dropdown selection in Marimo

## What still needs work

- linking hemisphere and ROI selection to a full stats-map workflow
- improving the overall dashboard layout
- testing or debugging `ipyniivue` further for mesh-based interactivity
- checking whether hover and click interactions can be used in the intended workflow



## Main files

- `notebooks/prototype_dashboard.py`  
  Main Marimo notebook containing the prototype

- `data/atlas/lh.HCP-MMP1.annot`
- `data/atlas/rh.HCP-MMP1.annot`  
  Atlas files used in the prototype

- `assets/hcp-mmp1-atlas_left-hemisphere.png`
- `assets/hcp-mmp1-atlas_left-pial.png`  
  Example screenshots from the current prototype

## Project structure

```text
interactive-dashboards-project/
├── README.md
├── pyproject.toml
├── uv.lock
├── notebooks/
│   └── prototype_dashboard.py
├── assets/
│   ├── hcp-mmp1-atlas_left-hemisphere.png
│   └── hcp-mmp1-atlas_left-pial.png
└── data/
    └── atlas/
        ├── lh.HCP-MMP1.annot
        └── rh.HCP-MMP1.annot
# interactive-dashboards-project
Create interactive dashboards using ipyniivue and Marimo

## Getting started
1. Install uv
2. Fork/clone repo
3. Install project dependencies `uv sync`
4. Edit file with `uv run marimo edit init_app.py`
5. Explore functionality of Python package ipyniivue
6. Get Glasser atlas and plot on fsaverage high resolution brain
