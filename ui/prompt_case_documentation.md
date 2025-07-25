# Using Prompt to Generate Frontend Code Based on an Image

## Introduction
    In this case study, we demonstrate how to use prompts to collaborate with AI to generate frontend code based on a provided image. Through two interactions, we successfully created a UI interface that meets the requirements.

## Preparation
1. Prepare an image that shows the design of the target UI interface.
2. Prepare a Markdown file describing the relevant information and file structure of the project.
3. Add the image and Markdown file to the chat for AI reference.

## Process
### Step 1: Initial Prompt
**Prompt Content:**
```
Can you generate frontend code based on the image I provided? The entire UI should be scalable; QLineEdit should be editable, and when a QLineEdit is selected, it should display a blue underline at the bottom; QTextEdit should be non-editable. "Dashboard Template and output path:", "Reference:", "MIP Input file path:", "CMP Input file path:", and "Messages:" are all Labels.
```
**AI Response:**
The AI generated the frontend code and returned Image 1, showing the generated UI.

### Step 2: Layout Adjustment
**Prompt Content:**
```
All Labels except for "Messages:" should be displayed on the same horizontal line as their corresponding QLineEdit. The "Run Report" button should not occupy the full row, but should only be displayed on the right half of the layout.
```
**AI Response:**
The AI adjusted the code layout and returned Image 2, showing the updated UI.

## Results
### First Generated UI
Image 1 shows the initially generated UI interface, where all labels and input fields are vertically aligned.

### Second Generated UI
Image 2 shows the adjusted UI interface, where labels and input fields are on the same horizontal line, and the "Run Report" button is positioned on the right half.

This case study highlights the efficiency and flexibility of prompt-driven development. The AI can quickly generate code based on user requirements and make adjustments based on feedback, ultimately producing results that meet expectations.
