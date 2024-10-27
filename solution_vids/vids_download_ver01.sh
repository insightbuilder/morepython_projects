#!/bin/bash

# Base URL for the downloads
base_url="https://ptgmedia.pearsoncmg.com/imprint_downloads/informit/bookreg/9780134123486"

# Prompt user for start and end range
read -p "Enter the starting file number (e.g., 0): " start
read -p "Enter the ending file number (e.g., 49): " end

# Define file type prefixes
prefixes=("Solution" "Intro" "Part")

# Loop over each prefix and range
for prefix in "${prefixes[@]}"; do
  for i in $(seq "$start" "$end"); do
    # Format the filename based on prefix and index
    file="/media/uberdev/fdrv/tempVids01/LMorePy3/LMorePy3THW_Ex${i}_${prefix}.mp4"
    dfile="LMorePy3THW_Ex${i}_${prefix}.mp4"
    
    # Check if the file already exists and has a non-zero size
    if [[ -f "$file" && -s "$file" ]]; then
      echo "File ${file} already exists and is non-zero in size. Skipping download."
      continue
    fi

    # Download with up to 2 retries
    retries=2
    count=0
    success=0
    
    while [[ $count -le $retries ]]; do
      # Attempt download
      wget "${base_url}/${dfile}" -O "${file}"
      
      if [[ $? -eq 0 && -s "$file" ]]; then
        echo "Downloaded ${file} successfully"
        success=1
        break
      else
        echo "Failed to download ${file} (Attempt $((count + 1)) of $((retries + 1)))"
        ((count++))
      fi
    done

    # Check if download was successful after retries
    if [[ $success -ne 1 ]]; then
      echo "Failed to download ${file} after ${retries} retries."
    fi
  done
done
