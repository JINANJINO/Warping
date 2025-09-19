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
## 1. Coordinate Transformation

<img width="273" height="267" alt="image" src="https://github.com/user-attachments/assets/58214b16-3e13-496c-849b-884f6a057724" />

The goal is to find a matrix that transforms a point $$P(x, y)$$ to a new point $$P'(x', y')$$ by rotating it counter-clockwise around the origin by an angle $$θ$$. The derivation relies on basic trigonometry.

*1. Define the Initial Point using Trigonometry*

First, let's express the coordinates of our initial point $$P(x, y)$$ using polar coordinates.
Let $$r$$ be the distance from the origin to the point $$P$$, and let $$ϕ$$ (phi) be the angle that the line segment from the origin to P makes with the positive x-axis.

From basic trigonometry, we can define $$x$$ and $$y$$ as:

$$x=rcos(ϕ)$$
$$y=rsin(ϕ)$$

*2. Define the Rotated Point*

Now, we rotate the point $$P$$ by an angle $$θ$$ to get the new point $$P'(x', y')$$.
The rotation is around the origin, so the distance $$r$$ from the origin remains the same. The new angle with the positive x-axis is the original angle $$ϕ$$ plus the rotation angle $$θ$$.

So, the new coordinates $$x'$$ and $$y'$$ can be expressed as:

$$x′=rcos(ϕ+θ)$$
$$y'=rsin(ϕ+θ)$$

*3. Apply Angle Sum Identities*

To connect the new coordinates $$(x', y')$$ with the original ones $$(x, y)$$, we use the trigonometric angle sum identities:

- $$cos(A+B)=cosAcosB−sinAsinB$$
- $$sin(A+B)=sinAcosB+cosAsinB$$

*4. Formulate the Rotation Matrix*

We now have a system of two linear equations:
$$x′=xcosθ−ysinθ$$
$$y′=xsinθ+ycosθ$$

This system can be written in matrix form, $$P′=RP$$, where $$R$$ is the ```rotation matrix```.

$$\begin{pmatrix} x' \\\\ y' \end{pmatrix}
=\begin{pmatrix}
\cos\theta & -\sin\theta \\\\
\sin\theta & \cos\theta
\end{pmatrix}
\begin{pmatrix} x \\\\ y \end{pmatrix}
$$

Thus, the 2D counter-clockwise rotation matrix $$R$$ is:

$$
R = \begin{bmatrix} \cos\theta & -\sin\theta \\\\ \sin\theta & \cos\theta \end{bmatrix}
$$


