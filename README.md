# Warping
## 0. Introduction
In **computer vision**, filtering and warping are two fundamental techniques for transforming images, but they differ significantly in their operation and purpose. Simply put, **filtering changes the values of pixels, while warping changes their location.**

**Filtering**
<img width="1670" height="1104" alt="filters" src="https://github.com/user-attachments/assets/f267c34a-b88d-4189-a157-b25a6999e626" />

**Filtering** is the process of modifying the value of each pixel in an image based on the values of its neighboring pixels. It manipulates properties like brightness and color without altering the image's geometric shape. This is typically achieved by applying a small matrix called a **kernel** (or mask) and performing a convolution operation across the entire image.
