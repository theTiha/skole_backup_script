# skole_backup_script
Backup script to H4
""" WORK IN PROGRESS """

Description:
Simple full filesystem backups are done through the main.py script. Backups are created from a CSV file that is located in the repository. The backup script ONLY works on the host there it's located, and is designed to work automatically with the help of a cronjob or Windows Task Scheduler. 

Important:
Make sure that there is a full backup before you try to make a Differential Backup. 

Usage:
The script creates the entire folder structure within the backup folder and then creates syncs recursively for all files within the source folders. Use the CSV file to create the customers names and path to the files/directory you want to backup.

Before running the script make sure to change the "path_to_backup_folder" so the script place your backup at the correct place. 

