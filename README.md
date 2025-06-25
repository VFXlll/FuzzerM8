# FuzzerM8
# Fuzzer with the ability to search files by extensions, with interactive input and file descriptor management

# Key features:

# Interactive extension input:

# The user can enter any number of extensions separated by spaces

# Input example: php txt html js

# Link filtering:

# Checks the end of each link for compliance with the specified extensions

# Considers both relative (/admin.php) and absolute (admin.php) paths

# Proper file handling:

# Using a context manager (with) for the input file

# Explicit closing (close()) for the output file

# I/O error handling

# Search flexibility:

# Checks all HTTP statuses except 404

# Saves all found URLs, including those that returned a non-standard status

# Output format:

# Clear process logging

# Saving only valid results


# Example of use:
# File with links (relative path): wordlist.txt
# Base URL (e.g. https://site.com): http://test.com
# Enter file extensions separated by spaces (e.g. php txt html):
# > php txt
