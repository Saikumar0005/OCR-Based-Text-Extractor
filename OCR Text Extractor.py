import easyocr
import cv2
import numpy as np
import matplotlib.pyplot as plt
from google.colab import files
from IPython.display import display, HTML
import torch
from docx import Document

gpu_available = torch.cuda.is_available()
print(f'GPU available: {gpu_available}')

def preprocess_image(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    _, thresh = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    return thresh

def draw_boxes_on_image(image, results):
    for (bbox, text, prob) in results:
        top_left = tuple([int(val) for val in bbox[0]])
        bottom_right = tuple([int(val) for val in bbox[2]])
        cv2.rectangle(image, top_left, bottom_right, (0, 255, 0), 2)
        cv2.putText(image, text, (top_left[0], top_left[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
    return image

def ocr_and_display_text(image_path):
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError(f"The image at path {image_path} does not exist.")
    preprocessed_image = preprocess_image(image)
    reader = easyocr.Reader(['en'], gpu=gpu_available)
    results = reader.readtext(preprocessed_image)
    annotated_image = draw_boxes_on_image(image, results)
    plt.imshow(cv2.cvtColor(annotated_image, cv2.COLOR_BGR2RGB))
    plt.axis('off')
    plt.show()
    structured_text = "\n".join([text for (_, text, _) in results])
    print("\nRecognized Text Layout:")
    print(structured_text)
    download_choice = input("\nDo you want to download the recognized text as a Word document? (yes/no): ").strip().lower()
    if download_choice == 'yes':
        doc = Document()
        for (_, text, _) in results:
            doc.add_paragraph(text)
        word_file_path = 'recognized_text_layout.docx'
        doc.save(word_file_path)
        print(f"\nRecognized text saved to Word document: {word_file_path}")
        files.download(word_file_path)

uploaded = files.upload()
image_path = next(iter(uploaded))

ocr_and_display_text(image_path)