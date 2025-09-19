# Warping
## 0. Introduction
In **computer vision**, filtering and warping are two fundamental techniques for transforming images, but they differ significantly in their operation and purpose. Simply put, **filtering changes the values of pixels, while warping changes their location.**

**Filtering**
<img width="1670" height="1104" alt="filters" src="https://github.com/user-attachments/assets/f267c34a-b88d-4189-a157-b25a6999e626" />

**Filtering** is the process of modifying the value of each pixel in an image based on the values of its neighboring pixels. It manipulates properties like brightness and color without altering the image's geometric shape. This is typically achieved by applying a small matrix called a **kernel** (or mask) and performing a convolution operation across the entire image.

- **Core Principle:** Modifying the pixel values (the range).
- **Main Purposes:**

  - **Noise Reduction:** Using filters like a Gaussian blur to smooth an image and reduce noise
  - **Image Sharpening:** Enhancing edges to make an image appear clearer.
  - **Edge Detection:** Using filters like Sobel or Canny to identify the boundaries of objects.
  - **Feature Extraction:** Highlighting specific patterns or textures.

- **Examples:**

  -  Applying a blur effect.
  -  Sharpening the details in a photo.
  -  Emphasizing certain colors in a grayscale image.

---

**Warping**
<img width="1280" height="1152" alt="image" src="https://github.com/user-attachments/assets/bc4d065b-1447-4fda-ab0a-1d428d7b1fd8" />


**Warping** is the process of geometrically transforming an image by remapping the coordinates of its pixels, without changing the pixel values themselves. This technique distorts or alters the shape of the image

- **Core Principle:** Modifying the pixel locations (the domain).
- **Main Purposes:**

    - **Geometric Correction:** Correcting distortions caused by camera lenses or perspective (e.g., straightening a photo taken with a fisheye lens).
    - **Image Alignment & Registration:** Aligning multiple images into a single coordinate system, such as when creating a panorama or combining medical scans (MRI, CT).
    - **Special Effects:** Creating artistic effects by bending or stretching an image.

- **Examples:**

    - Rotating, scaling, or translating an image.
    - Applying a perspective transform to make a tilted object appear as if viewed from directly above.
    - Correcting lens distortion in a photograph.
---
