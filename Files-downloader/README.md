# Files downloader
Script that authenticate you in a sharepoint site, and download files from different sources.

- [Files downloader](#files-downloader)
- [Problem description](#problem-description)
- [Restrictions](#restrictions)
- [Solution](#solution)
- [To-do](#to-do)

# Problem description
One of the responsabilities that you can have as a analyst is ming data, data from different sources in order to take decissions efficiently and keep a history to analyse them. At least in this organization one of the main source of information is in the sharepoint site. Easly you can enter to the site trhu your web browser and download manually but is no the mos efficient way because is a lot of time consumming.

# Restrictions
- The files are not standard, each one have a different name structure
- All the data are distributed, different links
- The files are saved in different places in the disk
- The extensions between files is different
- Rename the information one is dowloaded (this to follow a information standar)
- The data is uploaded daily, weekly, monthly, twice a week, completly different

# Solution
Actually this is a work in progress I'm going to update this script and their description as I complete it
 
# To-do
- [x] Authenticate a user in orderd to download any file
- [x] When the file is downladed, rename it to follow a standar name structure
- [x] Use a single data dictionary to download the files
- [ ] Identify when a file has already been downloaded
- [ ] Download multiple files at the same time