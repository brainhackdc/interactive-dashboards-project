import marimo

__generated_with = "0.23.1"
app = marimo.App(width="medium")


@app.cell
def _():
    from pathlib import Path

    import marimo as mo
    from nilearn import datasets, surface, plotting
    import nibabel as nib
    import matplotlib.pyplot as plt
    import ipyniivue

    return Path, datasets, mo, nib, plotting, plt


@app.cell
def _(Path, datasets):
    repo_dir = Path(__file__).resolve().parents[1]

    fsavg = datasets.fetch_surf_fsaverage(mesh="fsaverage")

    atlas_dir = repo_dir / "data" / "atlas"
    lh_annot = atlas_dir / "lh.HCP-MMP1.annot"
    rh_annot = atlas_dir / "rh.HCP-MMP1.annot"

    atlas_dir, lh_annot.exists(), rh_annot.exists()
    return fsavg, lh_annot


@app.cell
def _(lh_annot, nib):
    labels, ctab, names = nib.freesurfer.io.read_annot(str(lh_annot))
    len(names), [n.decode("utf-8") for n in names[:10]]
    return ctab, labels, names


@app.cell
def _(names):
    roi_names = [n.decode("utf-8") for n in names]
    clean_roi_names = [name for name in roi_names if name != "???"]

    len(clean_roi_names), clean_roi_names[:10]
    return clean_roi_names, roi_names


@app.cell
def _(ctab, roi_dropdown, roi_names):
    roi_id_map = dict(zip(roi_names, ctab[:, -1]))
    selected_name = roi_dropdown.value
    selected_id = roi_id_map[selected_name]

    selected_name, selected_id
    return selected_id, selected_name


@app.cell
def _(fsavg, labels, plotting, plt, selected_id, selected_name):
    def _():
        roi_mask = (labels == selected_id).astype(int)

        fig = plt.figure(figsize=(8, 6))

        plotting.plot_surf_roi(
            surf_mesh=fsavg["infl_left"],
            roi_map=roi_mask,
            hemi="left",
            view="lateral",
            bg_map=fsavg["sulc_left"],
            cmap="tab20",
            colorbar=False,
            figure=fig,
            title=selected_name,
        )
        return plt.show()


    _()
    return


@app.cell
def _(fsavg):
    from ipyniivue import NiiVue

    nv = NiiVue()
    nv.load_meshes([{"path": fsavg["pial_left"], "rgba255": [255, 192, 203, 255]}])
    nv
    return


@app.cell
def _(fsavg):
    fsavg["pial_left"]
    return


@app.cell
def _(fsavg):
    fsavg
    return


@app.cell
def _(fsavg):
    def _():
        from ipyniivue import NiiVue

        nv = NiiVue()
        nv.load_meshes([{"path": fsavg["infl_left"], "rgba255": [255, 192, 203, 255]}])
        return nv


    _()
    return


@app.cell
def _(Path, datasets):
    def _():
        repo_dir = Path(__file__).resolve().parents[1]

        fsavg = datasets.fetch_surf_fsaverage(mesh="fsaverage")

        atlas_dir = repo_dir / "data" / "atlas"
        lh_annot = atlas_dir / "lh.HCP-MMP1.annot"
        rh_annot = atlas_dir / "rh.HCP-MMP1.annot"
        return lh_annot.exists(), rh_annot.exists()


    _()
    return


@app.cell
def _(fsavg, plotting):
    brain_view = plotting.view_surf(
        surf_mesh=fsavg["pial_left"],
        bg_map=fsavg["sulc_left"],
        hemi="left",
        title="Left pial surface",
    )

    brain_view
    return (brain_view,)


@app.cell
def _(brain_view):
    brain_view.open_in_browser()
    return


@app.cell
def _(lh_annot, nib):
    def _():
        labels, ctab, names = nib.freesurfer.io.read_annot(str(lh_annot))
        roi_names = [n.decode("utf-8") for n in names]
        return len(roi_names), roi_names[:10]


    _()
    return


@app.cell
def _(fsavg, labels, plotting):
    atlas_view = plotting.view_surf(
        surf_mesh=fsavg["infl_left"],
        surf_map=labels.astype(float),
        bg_map=fsavg["sulc_left"],
        hemi="left",
        cmap="tab20",
        symmetric_cmap=False,
        colorbar=False,
        title="HCP-MMP1 atlas on left hemisphere",
    )

    atlas_view
    return (atlas_view,)


@app.cell
def _(atlas_view):
    atlas_view.open_in_browser()
    return


@app.cell
def _(clean_roi_names, mo):
    mo.md("### ROI legend\n" + "\n".join([f"- {name}" for name in clean_roi_names[:20]]))
    return


@app.cell
def _(Path, datasets, nib):
    def _():
        repo_dir = Path(__file__).resolve().parents[1]

        fsavg = datasets.fetch_surf_fsaverage(mesh="fsaverage")

        atlas_dir = repo_dir / "data" / "atlas"
        lh_annot = atlas_dir / "lh.HCP-MMP1.annot"

        labels, ctab, names = nib.freesurfer.io.read_annot(str(lh_annot))
        roi_names = [n.decode("utf-8") for n in names]
        clean_roi_names = [name for name in roi_names if name != "???"]
        return len(clean_roi_names), clean_roi_names[:10]


    _()
    return


@app.cell
def _(fsavg, labels, plotting):
    pial_atlas_view = plotting.view_surf(
        surf_mesh=fsavg["pial_left"],
        surf_map=labels.astype(float),
        bg_map=fsavg["sulc_left"],
        hemi="left",
        cmap="tab20",
        symmetric_cmap=False,
        colorbar=False,
        title="HCP-MMP1 atlas on left pial surface",
    )
    return (pial_atlas_view,)


@app.cell
def _(pial_atlas_view):
    pial_atlas_view.open_in_browser()
    return


@app.cell
def _(clean_roi_names, mo):
    legend_md = "### ROI legend\n\n" + "\n".join(
        f"- {name}" for name in clean_roi_names
    )

    mo.md(legend_md)
    return


@app.cell
def _(clean_roi_names, mo):
    roi_dropdown = mo.ui.dropdown(
        options=clean_roi_names,
        value=clean_roi_names[0],
        label="Find an ROI",
    )

    roi_dropdown
    return (roi_dropdown,)


@app.cell
def _(mo, roi_dropdown):
    mo.md(f"### Selected ROI\n\n**{roi_dropdown.value}**")
    return


if __name__ == "__main__":
    app.run()
