OCR Text Detection and Recognition with EasyOCR

This repository provides a Python implementation for Optical Character Recognition (OCR) using the EasyOCR library. The code allows users to upload an image, extract text, display annotated images with detected text, and save the recognized text as a Word document.

Features:
1.Image Preprocessing: Images are preprocessed for improved OCR accuracy using grayscale conversion, Gaussian blur, and thresholding.
2.Text Recognition: Leveraging EasyOCR for text detection and recognition.
3.Visual Feedback: Detected text regions are highlighted with bounding boxes and displayed.
4.Text Export: Recognized text can be saved into a Word document.
5.GPU Support: GPU acceleration is enabled if available.

Usage:
Run the script ocr_text_extraction.ipynb in Google Colab or locally:
1. Upload an image using the provided upload feature.
2. The script will preprocess the image and detect text using EasyOCR.
3. Detected text is displayed both visually (with bounding boxes) and as console output.
4. Optionally, save the recognized text as a Word document.

Execution:
1.For the executing the code first we want to install some packages(if you running this code Google Colab)
->easyocr(pip install easyocr)
->python-docx(pip install python-docx #it is used for downloading the recognized text in the format of word document)
2.Then select the file/image for the execution.
3.If you to download the recognied text then type yes or otherwise no.

Sample outputs:
Input1:-![Sample1](https://github.com/user-attachments/assets/34034393-f3cf-4907-b04d-7db5d6f93e33)
Output:a b c d e f 9 h i j k l m
       n o P q r $ 8 t U V w X Y z

Input2:-![Sample2](https://github.com/user-attachments/assets/1d5b1ba0-1e2d-471d-bb7f-8aedcbcc0f9c)
Output:- It was the best of
        times; it was the worst
        of times, it was the age
        of wisdom; it was the
        age of foolishness_

Acknowledgments:
EasyOCR
OpenCV
Google Colab for GPU-powered execution.


