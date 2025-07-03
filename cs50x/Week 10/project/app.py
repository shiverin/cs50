import os
import secrets
from flask import Flask, flash, redirect, render_template, request, send_from_directory, session, send_file, after_this_request, url_for
import uuid
from werkzeug.utils import secure_filename
from helpers import clear_uploads, merge_pdfs_h,clear_uploads2
import zipfile
from io import BytesIO
from pdf2image import convert_from_path
from PyPDF2 import PdfReader
import pdf2docx
import threading
import time
import PyPDF2

# Configure application
app = Flask(__name__)

app.config['SECRET_KEY'] = secrets.token_hex(16)

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/", methods=["GET", "POST"])
def index():
    # Ensure a unique session ID is assigned if it doesn't exist
    if "user_id" not in session:
        session["user_id"] = str(uuid.uuid4())  # Generate a unique session ID

    # Handle file uploads
    if request.method == "POST":
        # Get the user's unique session ID
        user_id = session["user_id"]
        user_folder = os.path.join(UPLOAD_FOLDER, user_id)

        # Create a folder for the user if it doesn't exist
        if not os.path.exists(user_folder):
            os.makedirs(user_folder)

        uploaded_files = request.files.getlist("file[]")
        for file in uploaded_files:
            if file:
                filename = secure_filename(file.filename)
                if filename.lower().endswith('.pdf'):  # Check for PDF extension
                    file_path = os.path.join(user_folder, filename)
                    file.save(file_path)
                    flash(f"File {filename} uploaded successfully!", "success")
                else:
                    flash(f"File {filename} is not a PDF and was not uploaded.", "error")
        return redirect(request.referrer)

    # Get the list of files for the current user
    user_id = session["user_id"]
    user_folder = os.path.join(UPLOAD_FOLDER, user_id)
    files = os.listdir(user_folder) if os.path.exists(user_folder) else []
    return render_template("index.html", files=files)

@app.route("/convert", methods=["GET", "POST"])
def convert():
    user_id = session.get("user_id", None)  # Get the user's unique session ID
    if user_id is None:
        return redirect("/")
    user_folder = os.path.join(UPLOAD_FOLDER, user_id)
    files = os.listdir(user_folder) if os.path.exists(user_folder) else []
    return render_template("convert.html", files=files)

@app.route('/zip', methods=['GET','POST'])
def zip():
    user_id = session.get("user_id", None)  # Get the user's unique session ID
    if user_id is None:
        return redirect("/")

    user_folder = os.path.join(UPLOAD_FOLDER, user_id)
    files = os.listdir(user_folder) if os.path.exists(user_folder) else []
    return render_template("zip.html", files=files)

@app.route("/signature", methods=["GET", "POST"])
def signature():
    user_id = session.get("user_id", None)  # Get the user's unique session ID
    if user_id is None:
        return redirect("/")
    user_folder = os.path.join(UPLOAD_FOLDER, user_id)
    files = os.listdir(user_folder) if os.path.exists(user_folder) else []
    return render_template("signature.html", files=files)

@app.route("/extract", methods=["GET", "POST"])
def extract():
    user_id = session.get("user_id", None)  # Get the user's unique session ID
    if user_id is None:
        return redirect("/")
    user_folder = os.path.join(UPLOAD_FOLDER, user_id)
    files = os.listdir(user_folder) if os.path.exists(user_folder) else []
    return render_template("extract.html", files=files)

@app.route("/text", methods=["GET", "POST"])
def text():
    user_id = session.get("user_id", None)  # Get the user's unique session ID
    if user_id is None:
        return redirect("/")
    user_folder = os.path.join(UPLOAD_FOLDER, user_id)
    files = os.listdir(user_folder) if os.path.exists(user_folder) else []
    return render_template("text.html", files=files)

@app.route("/rename", methods=["GET", "POST"])
def rename():
    user_id = session.get("user_id", None)  # Get the user's unique session ID
    if user_id is None:
        return redirect("/")
    user_folder = os.path.join(UPLOAD_FOLDER, user_id)
    files = os.listdir(user_folder) if os.path.exists(user_folder) else []
    return render_template("rename.html", files=files)

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    user_id = session.get("user_id", None)  # Get the user's unique session ID
    if user_id is None:
        return redirect("/")
    user_folder = os.path.join(UPLOAD_FOLDER, user_id)
    return send_from_directory(user_folder, filename)

# Route to delete a file
@app.route('/delete/<filename>', methods=['POST'])
def delete_file(filename):
    """Delete the uploaded file from the user's specific folder."""
    user_id = session.get("user_id", None)  # Get the user's unique session ID
    if user_id is None:
        return redirect("/")

    user_folder = os.path.join(UPLOAD_FOLDER, user_id)
    file_path = os.path.join(user_folder, filename)

    # Check if the file exists, and delete it if found
    try:
        if os.path.exists(file_path):
            os.remove(file_path)  # Delete the file
            flash(f'File "{filename}" deleted successfully!', "success")
        else:
            flash(f'File "{filename}" not found!', "error")
    except Exception as e:
        flash(f'Error deleting file: {e}', "error")

    return redirect(request.referrer)  # Redirect back to home page after deletion

@app.route("/merge", methods=["GET", "POST"])
def merge(): # merge page
    # Ensure a unique session ID is assigned if it doesn't exist
    if "user_id" not in session:
        session["user_id"] = str(uuid.uuid4())  # Generate a unique session ID

    # Get the list of files for the current user
    user_id = session["user_id"]
    user_folder = os.path.join(UPLOAD_FOLDER, user_id)
    files = os.listdir(user_folder) if os.path.exists(user_folder) else []
    return render_template("merge.html", files=files)

@app.route('/merge_pdfs', methods=['GET', 'POST'])
def merge_pdfs(): #merge pdf
    result = None  # Initialize result to None
    if request.method == 'POST':
        merged_name = request.form.get("merged_name", "merged")
        if merged_name=="":
            merged_name="merged"

        user_id = session.get('user_id')
        if user_id is None:
            flash("Merging failed, try again!")
            return redirect("/")  # If no user session, redirect to home
        # Call the merge function
        result = merge_pdfs_h(UPLOAD_FOLDER, user_id, merged_name)
        return render_template("merge_pdfs.html", result=result)

@app.route('/download/static/<path:filename>')
def download_file(filename): #download file
    user_id = session.get("user_id", None)
    if user_id is None:
        flash("Session expired, please upload your files again.", "error")
        return redirect("/")
    @after_this_request
    def cleanup_after_download(response):
        if user_id:
            result = clear_uploads('static', user_id)  # Clean user-specific files
        # Flash result of cleanup operation
        if result["status"] == "success":
            flash(result["message"])
        else:
            flash(f"Error: {result['message']}", "error")
        return response
    return send_from_directory('', filename)

@app.route('/clearall', methods=['GET','POST'])
def clearall(): #rubbish managment to remove folders in uploads, users indv, admin 1 all
    if request.method=='POST':
        user_id = session.get("user_id", None)
        if user_id is None:
            return redirect(request.referrer)
        result=clear_uploads(UPLOAD_FOLDER, user_id)
        if result["status"] == "success":
            flash(result["message"])
        else:
            flash(f"Error: {result['message']}")
        return redirect(request.referrer)
    else:
        result=clear_uploads(UPLOAD_FOLDER, 1)
        if result["status"] == "success":
            flash(f"{result['message']} from uploads!")
        else:
            flash(f"Error: {result['message']}")
        result=clear_uploads('static', 1)
        if result["status"] == "success":
            flash(f"{result["message"]} from static!")
        else:
            flash(f"Error: {result['message']}")
        return redirect("/")

@app.route('/cleardown', methods=['GET','POST'])
def cleardown(): #manages rubbish from downloads (static) folder, user post removes indv fold and admin 1 removes all folder
    if request.method=='POST':
        user_id = session.get("user_id", None)
        if user_id is None:
            return redirect("/")
        result=clear_uploads('static', user_id)
    else:
        result=clear_uploads('static', 1)
    if result["status"] == "success":
        flash(result["message"])
    else:
        flash(f"Error: {result['message']}")
    return redirect("/")

@app.route('/convert/<filename>/<format>', methods=['GET'])
def convert_pdf(filename, format):
    user_id = session.get("user_id", None)
    if user_id is None:
        flash("Session expired, please upload your files again.", "error")
        return redirect("/")
    file_path = os.path.join(UPLOAD_FOLDER, user_id, filename)

    if not os.path.exists(file_path):
        flash('File does not exist!', 'error')
        return redirect('/')

    if format == 'image':
        return convert_pdf_to_images(file_path)
    elif format == 'text':
        return convert_pdf_to_text(file_path)
    elif format == 'word':
        return convert_pdf_to_word(file_path)
    else:
        flash('Unsupported format!', 'error')
        return redirect('/')

def convert_pdf_to_images(file_path):
    user_id = session.get("user_id", None)
    if user_id is None:
        return redirect("/")
    # Convert PDF to images (one image per page)
    images = convert_from_path(file_path)
    image_files = []

    for i, image in enumerate(images):
        image_path = os.path.join(app.config['UPLOAD_FOLDER'], f'page_{i + 1}.png')
        image.save(image_path, 'PNG')
        image_files.append(image_path)

    # Create a zip of all images
    from zipfile import ZipFile
    zip_name = os.path.join(UPLOAD_FOLDER, user_id, 'images.zip')
    with ZipFile(zip_name, 'w') as zipf:
        for img in image_files:
            zipf.write(img, os.path.basename(img))
            os.remove(img)  # Clean up individual image files

    @after_this_request
    def cleanup(response):
        try:
            os.remove(zip_name)
            print(f"Deleted the word file: {zip_name }")
        except Exception as e:
            print(f"Error deleting word file: {e}")
        return response
    return send_file(zip_name, as_attachment=True)

def convert_pdf_to_text(file_path):
    # Convert PDF to text using PyPDF2
    pdf_reader = PdfReader(file_path)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()

    # Send text as a downloadable file
    text_file = BytesIO()
    text_file.write(text.encode('utf-8'))
    text_file.seek(0)

    return send_file(text_file, as_attachment=True, download_name="extracted_text.txt", mimetype="text/plain")

def convert_pdf_to_word(file_path):
    user_id = session.get("user_id", None)
    if user_id is None:
        return redirect("/")
    # Convert PDF to Word using pdf2docx
    docx_file_path = os.path.join(UPLOAD_FOLDER, user_id, 'converted.docx')
    pdf2docx.parse(file_path, docx_file_path)
    @after_this_request
    def cleanup(response):
        try:
            os.remove(docx_file_path)
            print(f"Deleted the word file: {docx_file_path}")
        except Exception as e:
            print(f"Error deleting word file: {e}")
        return response
    return send_file(docx_file_path, as_attachment=True)

@app.route("/download_zip", methods=["GET", "POST"])
def download_zip():
    user_id = session.get("user_id", None)
    if user_id is None:
        return redirect("/")

    if request.method == 'POST':
        user_folder = os.path.join(UPLOAD_FOLDER, user_id)

        if not os.path.exists(user_folder) or not os.listdir(user_folder):
            flash("No files to zip!", "error")
            return redirect(request.referrer)

        name = request.form.get("zipped_name", "zip") or "zip"
        zip_filename = f"{name}.zip"
        zip_file_path = os.path.join(user_folder, zip_filename)

        # Create the zip file
        with zipfile.ZipFile(zip_file_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for filename in os.listdir(user_folder):
                file_path = os.path.join(user_folder, filename)

                # Skip hidden files and the zip file itself
                if (
                    not os.path.isfile(file_path) or
                    filename.startswith('.') or
                    filename.endswith(('.log', '.tmp', '.bak')) or
                    filename == zip_filename
                ):
                    continue

                zipf.write(file_path, arcname=filename)

        @after_this_request
        def cleanup(response):
            try:
                os.remove(zip_file_path)
                print(f"Deleted the zip file: {zip_file_path}")
            except Exception as e:
                print(f"Error deleting zip file: {e}")
            return response

        return send_file(zip_file_path, as_attachment=True)


@app.route("/extract_pages", methods=["POST"])
def extract_pages():
    user_id = session.get("user_id", None)
    if user_id is None:
        return redirect("/")
    # Get the file name and page numbers from the form
    file_name = request.form.get("file_name")
    page_numbers = request.form.get("page_numbers")

    # Validate and process page numbers
    try:
        page_numbers = [int(num.strip()) - 1 for num in page_numbers.split(",")]  # Convert to 0-indexed
    except ValueError:
        flash("Invalid page numbers", "error")
        return redirect(request.referrer)

    # Define the file path for the uploaded PDF
    file_path = os.path.join(UPLOAD_FOLDER, user_id, file_name)
    if not os.path.exists(file_path):
        flash("File does not exist!", "error")
        return redirect(request.referrer)

    # Open the PDF and extract the requested pages
    try:
        with open(file_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            pdf_writer = PyPDF2.PdfWriter()

            # Extract the specified pages
            for page_num in page_numbers:
                if 0 <= page_num < len(pdf_reader.pages):
                    pdf_writer.add_page(pdf_reader.pages[page_num])

            # Create an in-memory PDF output
            output_pdf = BytesIO()
            pdf_writer.write(output_pdf)
            output_pdf.seek(0)

            return send_file(output_pdf, as_attachment=True, download_name="extracted_pages.pdf", mimetype='application/pdf')

    except Exception as e:
        flash(f"Error processing the PDF: {e}", "error")
        return redirect(request.referrer)

def schedule_clear_uploads():
    def run():
        while True:
            result = clear_uploads2(UPLOAD_FOLDER, 1)
            flash(f"[ClearUploads] {result['message']}")
            result = clear_uploads2('static', 1)
            flash(f"[ClearUploads] {result['message']}")
            time.sleep(300)  # Run every 5 minutes (300 seconds)

    thread = threading.Thread(target=run, daemon=True)
    thread.start()

def log_files():
    """Function to log files in 'uploads' and 'static' every 5 minutes"""
    while True:
        # List files in the 'uploads' directory
        uploads_files = os.listdir('uploads')
        print("[Uploads Folder] Files:", uploads_files)

        # List files in the 'static' directory
        static_files = os.listdir('static')
        print("[Static Folder] Files:", static_files)

        # Sleep for 5 minutes (300 seconds)
        time.sleep(300)  # 5 minutes

def schedule_log_files():
    """Function to schedule the file logging in a separate thread"""
    thread = threading.Thread(target=log_files, daemon=True)
    thread.start()

if __name__ == "__main__":
    app.run(debug=True)
