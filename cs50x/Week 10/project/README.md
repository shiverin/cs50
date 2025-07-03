# PDFILEdit: A Flask-Based PDF Editor Web Application
#### Video Demo:  (https://www.youtube.com/watch?v=Cmx4PfkaMPE)

## Overview

**PDFILEdit** is a feature-rich web application that addresses a common, frustrating problem that students, working professionals, and educators face every day—**editing and managing PDF files with ease and flexibility**.

Most online tools for PDF editing are either limited, filled with intrusive ads, expensive, or require clunky installations. PDF Master offers a **clean, efficient, and intuitive web-based solution**, empowering users to handle a variety of PDF tasks with just a few clicks—all directly in their browser.

Created as my final project for Harvard's CS50x course, this application reflects both a personal response to a real-world pain point and a demonstration of scalable, secure web application design.

---

## What It Does

PDFILEdit allows users to upload one or more PDF files via a file input. These files are stored on the server in a **unique session-specific directory**, ensuring **user isolation and scalability** for concurrent users.

Before accepting any uploads, the server performs strict validation to ensure only `.pdf` files are accepted using a combination of extension checks and `secure_filename` sanitization to prevent malicious file uploads.

After uploading, the app checks the number of files in the user’s session directory:

- **If one file is uploaded**, the user is shown tools suited for individual files—such as:
  - Signing the PDF
  - Extracting individual pages
  - Converting the PDF to other formats (e.g., images)
- **If multiple files are uploaded**, the user is shown the **Merge** button to combine them into a single document.

This dynamic behavior is powered by the way session tracking and file management were architected—ensuring that uploaded files remain accessible and visible across different routes/pages throughout the app.


### Full Feature List

- **Secure PDF Upload** with session-based isolation
- **Remove File / Clear All** options for managing uploads
- **PDF Merging** when multiple files are uploaded
- **PDF Signature Tool**:
  - Draw your signature using HTML5 Canvas
  - Resize and drag signature onto the rendered PDF
  - Apply and download signed PDF
- **PDF Page Extraction** (extract selected pages from a PDF)
- **PDF Conversion** (e.g., PDF to images or text)
- **ZIP PDFs Together**: Compress all uploaded PDFs into a single `.zip`
- **Session Persistence** for uploaded files across different tools/pages
- **Instant Download** of all output files

---

## Why It’s Impactful

The design philosophy behind PDF Master is rooted in **enhancing workflow and productivity**. Whether you're a student preparing assignments or a professional handling contracts, PDF Master simplifies your interaction with PDFs without needing to jump between multiple platforms.

Moreover, every technical decision was made with **scalability**, **usability**, and **user control** in mind—from secure file uploads to advanced PDF interaction tools.

What sets this application apart is not just its powerful set of features, but also the thoughtful user experience it delivers. With clean session-based file handling and an intuitive interface, users are able to **toggle seamlessly between different functions**—such as signing, merging, extracting, and converting—without needing to re-upload or reset their workflow. This makes the application feel truly integrated, enabling users to complete complex PDF tasks quickly and efficiently, all in one place.

Ultimately, this project empowers users with a free, reliable, and efficient tool that improves their productivity and streamlines a task that has long been a hassle.

---

## Key Challenges & Solutions

### 1. **Managing Uploaded Files**

Handling user-uploaded files on the server proved more complex than expected. A major challenge was figuring out **how to clear uploaded files** when a user was done using them—without disrupting their session prematurely.

I experimented with a **JavaScript browser event listener** to detect tab closes, but it was too sensitive—it deleted files even on a simple page refresh, which wasn't acceptable.

To address this, I designed a **two-way cleanup system**:
- **Client-side**: Users can remove individual files via a **remove button** or clear all uploads instantly using a **"Clear All"** button—putting file control in the user’s hands.
- **Server-side**: A scheduled background task (to be integrated) will detect files last modified past a certain threshold and clean them up. This hybrid model ensures files don’t linger indefinitely without burdening users during their session.

### 2. **Integrating Signature Features**

The **PDF signature feature** was particularly challenging. I had to:
- Render a PDF inside the browser using a custom **PDF renderer**.
- Overlay an **HTML5 canvas** to collect user input for signatures—either drawn or uploaded.
- Allow users to **drag** and **resize** the signature on top of the rendered PDF page.
- Finally, **merge the signature onto the selected page** and provide a downloadable signed PDF.

Researching the correct libraries and methods to layer these components was a significant learning process, but the resulting functionality offers users a seamless and intuitive signature experience.

---

## Installation Instructions

To run PDFILEdit locally:

```bash
# Clone the repo
git clone https://github.com/yourusername/pdfiledit.git
cd pdfiledit

# Set up a virtual environment
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py
