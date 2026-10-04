# HoloSift

A structure and ligand explorer for members of The Insilico Lab, part of the CADD Toolkit at https://www.theinsilicolab.org/cadd-toolkit.

The name comes from *holo* structure (a protein with its ligand bound) and *sift* (keeping only what you need).

## What it does

**Protein structures**
- Fetches any entry from the RCSB Protein Data Bank by ID, or opens your own PDB, mmCIF, PQR or PDBQT file.
- Shows the title, resolution, method, R-work/R-free, organism, release date, mass, chains with UniProt links, co-crystallised ligands with full names, and the primary citation.
- Lets you tick the chains, ligands, sugars, ions, buffer molecules and waters to keep, then downloads the cleaned complex, the protein only, or the ligands only (PDB or SDF).
- Shows each chain's sequence with unmodelled gaps and binding-site residues. Clicking a residue shows it in 3D.

**Molecule files**
- Opens SDF, MOL, MOL2, PDBQT, PDB, PQR and XYZ files, including multi-molecule files and docking poses.
- Lists every molecule with formula, molecular weight, heavy atoms and any score in the file, and downloads the chosen ones in the original format or as SDF, PDB or XYZ.

## Files

| File | Purpose |
|---|---|
| `app.py` | Streamlit app that shows HoloSift full-width and reads `?pdb=` and `?view=` from the address |
| `holosift.html` | The tool itself: interface, 3D viewer, file readers and writers. The logo and brand colours are built in |
| `requirements.txt` | Python packages for Streamlit Cloud (only Streamlit) |
| `.streamlit/config.toml` | Brand colours, the same as the Molecular Workspace |
| `logo_icon.png` | Browser-tab icon |

HoloSift does its work in the visitor's browser, so nothing is installed on the server and no `packages.txt` is needed.

## Run locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Deploy

1. Create a public GitHub repository called `til-holosift` and upload every file in this folder, including the `.streamlit` folder.
2. At https://share.streamlit.io choose **Create app** → **Deploy a public app from GitHub**. Repository `akinwumiishola5000/til-holosift`, branch `main`, main file `app.py`, App URL `insilicolab-holosift`.
3. Embed `https://insilicolab-holosift.streamlit.app/?embed=true` on a HoloSift subpage under CADD Toolkit in Google Sites.

## Links for teaching

- Open a structure directly: `https://insilicolab-holosift.streamlit.app/?pdb=1M17`
- Open the molecule files workspace: `https://insilicolab-holosift.streamlit.app/?view=mols`

## Outside services

RCSB PDB (`files.rcsb.org`, `data.rcsb.org`, `models.rcsb.org`) for structures, annotations and ligand SDFs; 3Dmol.js 2.4.2 from `cdn.jsdelivr.net`; Source Sans 3 and Material Symbols from Google Fonts. Files people open are never uploaded.

## Credits

Built for The Insilico Lab (theinsilicolab.org). Structure data: RCSB Protein Data Bank (Berman et al., Nucleic Acids Res. 2000). 3D graphics: 3Dmol.js (Rego and Koes, Bioinformatics 2015).
