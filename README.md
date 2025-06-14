# k-means palette reducer

This tool generates different artistic styles by reducing the number of colours in an image using the [k-means clustering algorithm](https://en.wikipedia.org/wiki/K-means_clustering). It's useful for creating a simplified colour palette or for image compression.

---

## Setup

1.  **Prerequisites**

    * Python 3.6 or higher
    * The following Python libraries:
        * scikit-learn (`pip install scikit-learn`)
        * NumPy (`pip install numpy`)
        * Pillow (PIL) (`pip install pillow`)

2.  **Installation**

    * Install the required libraries in a virtual environment:

        ```bash
        pip install scikit-learn numpy pillow
        ```

3.  **Usage**

    * Input file `image.jpg` is in the root directory
    * Configure `n_colours_to_reduce_to` with the number of colours you want in the reduced palette
    * Output images are saved in `/output_images`

    See examples in `/output_images` for different results

<br>

## Image credit

Photo by [Simon Berger](https://unsplash.com/@simon_berger?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash) on [Unsplash](https://unsplash.com/photos/landscape-photography-of-mountains-twukN12EN7c?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash)
