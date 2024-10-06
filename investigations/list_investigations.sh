#!/bin/bash

# Define the path to the file
output_file="investigations/investigations.md"

# Remove the description
sed -i '' "/Updated at build time/d" "$output_file"

# Start writing to the file
echo "" >> "$output_file"

# Loop through each folder in the investigations directory
for directory in investigations/*/ ; do
  # Check if the directory exists and is a folder, suppressing errors
  if [ -d "$directory" ] 2>/dev/null; then
    # Extract the folder name (remove the path)
    folder_name=$(basename "$directory")
    
    # Create a hyperlink in Markdown format with a trailing slash in the link
    echo "- [$folder_name]($folder_name/)" >> "$output_file"
  fi
done

echo "List added to $output_file"
