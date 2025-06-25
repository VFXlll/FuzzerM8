import requests
import os

def get_user_extensions():
    """Interactive input of file extensions"""
    print("Enter file extensions separated by spaces (e.g. php txt html):")
    extensions = input("> ").strip().split()
    return [ext.lower() for ext in extensions]

def filter_links_by_extension(links, extensions):
    """Filtering links by extensions"""
    filtered = []
    for link in links:
# Check if the link ends with any of the extensions
        if any(link.lower().endswith(f".{ext}") for ext in extensions):
            filtered.append(link)
    return filtered

def main():
# Input data
    file_name = input("File with links (relative path): ").strip()
    base_url = input("Base URL (e.g. https://site.com): ").rstrip('/')

    try:
# Reading links from a file with proper closing
        with open(file_name, 'r') as f:
            links = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found")
        return
    except Exception as e:
        print(f"Error reading file: {str(e)}")
        return

    if not links:
        print("No links to check")
        return

# Getting extensions from the user
    extensions = get_user_extensions()
    if not extensions:
        print("No extensions specified for search")
        return

# Filtering links
    filtered_links = filter_links_by_extension(links, extensions)

    if not filtered_links:
        print("No links with the specified extensions")
        return

# Checking the availability of links
    results = []
    for link in filtered_links:
        target_url = f"{base_url}/{link}" if not link.startswith('/') else f"{base_url}{link}"

        try:
            response = requests.get(
                target_url,
                timeout=5,
                headers={'User-Agent': 'Mozilla/5.0'}
            )

            if response.status_code == 200:
                print(f"[FOUND] {target_url}")
                results.append(target_url)
            elif response.status_code != 404:
                print(f"[UNKNOWN STATUS {response.status_code}] {target_url}")
                results.append(target_url)

        except requests.exceptions.RequestException as e:
            print(f"[ERROR] {target_url} - {str(e)}")

# Save results with proper file closing
    if results:
        try:
            output_file = open("file.txt", "w")
            for result in results:
                output_file.write(result + "\n")
            output_file.close() # Explicit file closing
            print(f"\nFound {len(results)} files. Results saved to file.txt")
        except IOError as e:
            print(f"Error saving results: {str(e)}")
    else:
        print("No accessible files found")

if __name__ == "__main__":
    main()
