# Banana Farm Weed Detection using YOLOv5

## Project Overview

This project focuses on detecting weeds in banana farms using computer vision and deep learning.

A YOLOv5 object detection model is trained to identify weeds from images and live webcam/camera input. The system can detect weeds and display bounding boxes around the detected areas.

## Objectives

- Detect weeds in banana farm environments.
- Use YOLOv5 for real-time object detection.
- Test weed detection using images.
- Perform live detection using a webcam/camera.
- Provide a foundation for future agricultural automation.

## Features

- YOLOv5-based weed detection
- Single-class detection: `weed`
- Image-based detection
- Live webcam/camera detection
- Bounding boxes around detected weeds
- Confidence score support
- Future deployment possibility on Raspberry Pi 5

## Technologies Used

- Python
- YOLOv5
- PyTorch
- OpenCV
- NumPy
- Computer Vision
- Deep Learning

## Dataset

The model was trained using a custom banana-farm weed dataset.

### Class

```text
0 - weed
```
