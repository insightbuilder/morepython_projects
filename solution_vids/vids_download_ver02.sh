#!/bin/bash

# Base URL for the downloads
base_url="https://ptgmedia.pearsoncmg.com/imprint_downloads/informit/bookreg/9780134123486"

# Prompt user for start and end range
read -p "Enter the starting file number (e.g., 0): " start
read -p "Enter the ending file number (e.g., 49): " end

# Prompt user for the file type prefixes
# prefixes=("part" "Intro" "Solution")
read -p "Enter the prefix of the video ('part' 'Intro' 'Solution' ''): " prefix

# Log file
log_file="download_status.log"

# Clear the log file at the start
> "$log_file"

for i in $(seq "$start" "$end"); do
  # Format the filename based on prefix and index
  # we can update the file location is required
  file="LMorePy3THW_${prefix}${i}.mp4"
  dfile = "~/LmPython/LMorePy3THW_${prefix}${i}.mp4"
  
  # Check if the file already exists and has a non-zero size
  if [[ -f "$file" && -s "$file" ]]; then
    echo "File ${file} already exists and is non-zero in size. Skipping download." >> "$log_file"
    continue
  fi

  # Download with up to 2 retries
  retries=2
  count=0
  success=0
  
  while [[ $count -le $retries ]]; do
    # Attempt download and append output to log file
    wget "${base_url}/${file}" -O "${dfile}" >> "$log_file" 2>&1
    
    if [[ $? -eq 0 && -s "$file" ]]; then
      echo "Downloaded ${file} successfully" >> "$log_file"
      success=1
      break
    else
      echo "Failed to download ${file} (Attempt $((count + 1)) of $((retries + 1)))" >> "$log_file"
      ((count++))
    fi
  done

  # Check if download was successful after retries
  if [[ $success -ne 1 ]]; then
    echo "Failed to download ${file} after ${retries} retries." >> "$log_file"
  fi
done

