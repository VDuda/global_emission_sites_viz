from zipfile import ZipFile

# Define where the zipped file should be saved
save_to = "submission.zip"

# Define the list of files to include
include_files = [
    "submission_files_gcv/visual.png", 
    "submission_files_gcv/summary.pdf",
    "submission_files_gcv/report.pdf"
]

# Define the zip file object and add files
with ZipFile(save_to, "w") as zip_object:
    for file in include_files:
        zip_object.write(file)
