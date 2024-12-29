# pca_art
Dimensionality Reduction for Artwork Exploration

## Introduction
When curating a collection of artworks or selecting pieces for a portfolio or digital gallery, it's often challenging to decide which works to include. I wanted a way to visualize the entirety of my creative output—including failed experiments—over the course of a year. This approach provides a complete picture of my artistic journey, highlighting the categories I've explored, where my interests lie, and which directions have been most productive.

Principal Component Analysis (PCA) seemed like a great tool for uncovering underlying patterns in my work. Instead of analyzing the pixel data of the artwork images, I opted to use a dataset of descriptive characteristics I created for each piece. This allows for more interpretive and conceptual insights.

---

## How to Use

### 0. Clone the Repository
Begin by cloning this repository to your local machine:

```bash
git clone https://github.com/lauraporta/pca_art.git
cd pca_art
pip install .
```

### 1. Add Your Artworks
Place your images in the folder `docs/photos/`. Ensure the filenames follow the format `IMG_XXXX.png`, where `XXXX` matches the `id` column in your dataset.

### 2. Create Your Dataset
Replace the `docs/data/dataset.csv` file with your own dataset, containing details for each piece. The dataset should include the following columns:

| Column            | Description                                                                 |
|-------------------|-----------------------------------------------------------------------------|
| `id`              | A unique identifier matching the image filename (e.g., `IMG_332.png`).    |
| `realistic`       | A float (0 to 1) indicating the realism level of the work.                |
| `subject_general` | General subject category: portrait, landscape, still life, composite, etc.|
| `reference`       | Source of inspiration: photo, live drawing, imagination/memory.           |
| `palette`         | Main colors used or "grayscale".                                          |
| `materials`       | List of materials used (e.g., `"acrylic, paper"`).                        |
| `size`            | Approximate size: small, medium, or big.                                  |
| `exercise`        | Whether the work is an exercise (1 for yes, 0 for no).                   |
| `subject`         | Specific subject depicted (e.g., "man", "buildings", "pot, box").         |
| `satisfaction`    | How satisfied you are with the piece, rated from 1 (low) to 5 (high).     |

#### Example:

```csv
id,realistic,subject_general,reference,palette,materials,size,exercise,subject,satisfaction
332,1,still life,live painting,grayscale,"acrylic, paper",small,1,"pot, box",4
397,1,portrait,live painting,"brown, blue","acrylic, canvas board",medium,1,man,3
399,1,landscape,photo,"black, white red","acrylic, paper",small,0,buildings,2
```

### 3. Install Dependencies and Run the Script
Create a virtual environment, activate it, and install the required packages:

```bash
conda create -n pca_art python=3.11
conda activate pca_art
```
Then execute `python pca_art/compute_pca.py` to run the PCA analysis on your dataset. This script processes your dataset and generates a JSON file containing PCA results. 

In my dataset, the PCA revealed two primary axes that I interpreted as:
- **Experimental/Traditional**
- **Painting/Drawing**

Depending on your work, the main principal components (PCs) may change and require different interpretations. Explore the generated plot to uncover patterns specific to your dataset.

### 4. Visualize the Plot
Open `docs/index.html` using a Python server (e.g., `python -m http.server`) or a VSCode Live Server extension. This will display an interactive PCA visualization of your artworks.

If the PCA identifies different axes for your dataset, feel free to modify the axis labels in the HTML file to better reflect your findings.

---

## Contributions
Have a feature request or an idea to improve the project? Open an issue or submit a pull request to contribute.

---

## Notes
- The effectiveness of the PCA depends on the quality and consistency of the labels in your dataset.
- The visualization is highly customizable; you can tweak the HTML and CSS for your specific needs.
