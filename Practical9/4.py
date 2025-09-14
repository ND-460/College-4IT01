print("By 22IT460")
import os
directory = input("Enter the directory name:")
report_file = input("Enter the file name for the merged results:")
with open(report_file,"w") as report:
    report.write("File Size Report\n")
    report.write("=" * 50 + "\n")
    report.write(f"{'Filename':30} {'Bytes':>10} {'KB':>10} {'MB':>10}\n")
    report.write("-" * 50 + "\n")
    for filename in os.listdir(directory):
        filepath = os.path.join(directory,filename)
        if os.path.isfile(filepath):
            size_bytes = os.path.getsize(filepath)
            size_kb = size_bytes / 1024
            size_mb = size_kb / 1024
            report.write(f"{filename:30} {size_bytes:10} {size_kb:10.2f} {size_mb:10.4f}\n")