import os
import shutil
from PyPDF2 import PdfMerger
import time


def clear_uploads(UPLOAD_FOLDER, user_id):
    count=0
    if user_id == 1:
        folder=UPLOAD_FOLDER
        for subfolder in os.listdir(folder):
            subfolder_path = os.path.join(folder, subfolder)
            if os.path.isdir(subfolder_path):  # Only clear directories
                try:
                    shutil.rmtree(subfolder_path)  # Delete folder and all its contents
                    count += 1
                except Exception as e:
                    return {"status": "error", "message": str(e), "count": count}
        return {"status": "success", "message": f"{count} files cleared!", "count": count}
    else:
        folder = os.path.join(UPLOAD_FOLDER, user_id)
        if not os.path.isdir(folder):
            return {
            "status": "error",
            "message": f"Directory not found: {folder}",
            "count": count
            }
        else:
            for filename in os.listdir(folder):
                file_path = os.path.join(folder, filename)
                try:
                    if os.path.isfile(file_path):
                        os.remove(file_path)
                        count+=1
                except Exception as e:
                    return {"status": "error", "message": str(e), "count": count}
            shutil.rmtree(folder)
            return {"status": "success", "message": f"{count} files cleared!", "count": count}


def merge_pdfs_h(UPLOAD_FOLDER, user_id, merged_name):
    folder = os.path.join(UPLOAD_FOLDER, user_id)

    if not os.path.exists(folder):
        return {"status": "error", "message": "User folder not found", "count": 0}

    user_folder = os.path.join('static', user_id)  # Save merged file under static/{user_id}

    # Check if the user folder exists, if not, create it
    if not os.path.exists(user_folder):
        os.makedirs(user_folder)  # Create the folder if it doesn't exist

    # Collect all PDF files in the user's folder
    pdf_files = [f for f in os.listdir(folder) if f.endswith('.pdf')]

    if not pdf_files:
        return {"status": "error", "message": "No PDF files to merge", "count": 0}

    # Merge the PDFs
    merger = PdfMerger()

    for pdf in pdf_files:
        pdf_path = os.path.join(folder, pdf)
        merger.append(pdf_path)

    # Output merged PDF
    merged_pdf_path = os.path.join(user_folder, f"{merged_name}.pdf")
    merger.write(merged_pdf_path)
    merger.close()

    return {"status": "success", "message": "PDFs merged successfully", "count": len(pdf_files), "merged_pdf": merged_pdf_path, "name": merged_name}


def clear_uploads2(UPLOAD_FOLDER, user_id):
    count = 0
    now = time.time()
    threshold = 24 * 60 * 60  # 24 hours in seconds

    if user_id == 1:
        folder = UPLOAD_FOLDER
        for subfolder in os.listdir(folder):
            subfolder_path = os.path.join(folder, subfolder)
            if os.path.isdir(subfolder_path):
                try:
                    # Check last modified time
                    last_modified = os.path.getmtime(subfolder_path)
                    if now - last_modified > threshold:
                        shutil.rmtree(subfolder_path)
                        count += 1
                except Exception as e:
                    return {
                        "status": "error",
                        "message": str(e),
                        "count": count
                    }
        return {
            "status": "success",
            "message": f"{count} folders cleared!",
            "count": count
        }
