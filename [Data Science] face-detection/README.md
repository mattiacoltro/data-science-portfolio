# Face Detection System for a Digital Camera

### Project Context

**ProCam S.p.A.** is preparing to launch a new compact digital camera designed to be affordable and trendy for young photography enthusiasts. The product's primary goal is to simplify the shooting experience, specifically for solo or group selfies.

### The Challenge

You have been hired as a **Data Scientist** to develop a **face detection system**. This system will assist technicians in automatically optimizing camera settings during selfie captures. Your task is to create a pipeline that identifies faces within images and returns the coordinates of the **bounding boxes** where those faces are located. If no faces are detected, the pipeline must return an empty list.

This is a **Computer Vision** problem—specifically, **Face Detection**.

### Project Requirements

**Objective:** Build a face detection system using **Scikit-learn**. The pipeline must be capable of:

1. Receiving an input image.
2. Returning a list of bounding box coordinates for all detected faces.
3. Returning an empty list if no faces are present in the image.

**Constraints:**

* **Dataset:** No dataset is provided. You must find a suitable dataset online or, if no alternatives are available, construct one yourself.
* **Pre-trained Models:** The use of pre-trained models is **strictly prohibited**. The face detection model must be trained from scratch using Scikit-learn.
* **Computing Resources:** You will work on a system with limited computational capacity. The model must be optimized for low resource consumption.
* **Documentation:** The solution must be thoroughly documented. Every decision made (choice of algorithms, preprocessing, optimization techniques) must be explained. Furthermore, all external resources used (academic papers, blog posts, GitHub code) must be cited.
* **Literature Review:** Since detailed implementation instructions are not provided, it is essential to conduct an in-depth **literature review** to identify the best solutions. You will need to analyze existing approaches and adapt them to the project's constraints.

### Technologies
- Python
- Computer Vision
- Scikit-learn
