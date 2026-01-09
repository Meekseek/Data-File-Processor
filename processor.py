import sys

def invert_dictionary_file(input_file, output_file):
    """
    Reads a dictionary-style text file, inverts the keys and values,
    and writes the results to a new file.
    """
    original_dict = {}

    try:
        print(f"[*] Reading from {input_file}...")
        
        # Step 1: Reading from the file
        with open(input_file, 'r') as f_in:
            for line in f_in:
                clean_line = line.strip()
                # Skip empty lines or lines without a colon separator
                if not clean_line or ':' not in clean_line or clean_line in ['{', '}']:
                    continue
                
                # Split line into Key and Value
                key_str, val_str = clean_line.split(':', 1)
                key = key_str.strip()
                # Remove commas from values for cleaner processing
                value = val_str.strip().replace(',', '')
                
                original_dict[key] = value
                
        # Step 2: Inverting the dictionary
        # We use a list for values because multiple keys might have the same value
        inverted_dict = {}
        for key, value in original_dict.items():
            if value not in inverted_dict:
                inverted_dict[value] = []
            inverted_dict[value].append(key)
            
        # Step 3: Writing to the output file
        print(f"[*] Inverting data and writing to {output_file}...")
        with open(output_file, 'w') as f_out:
            f_out.write('{\n')
            for key, val_list in inverted_dict.items():
                # Join list items into a string separated by commas
                item_string = ', '.join(val_list)
                f_out.write(f'{key}: {item_string}\n')
            f_out.write('}\n')
        
        print(f"[+] Success! Data processed.")
        
    except FileNotFoundError:
        print(f"[!] Error: The file '{input_file}' was not found.")
    except PermissionError:
        print(f"[!] Error: Permission denied for '{input_file}' or '{output_file}'.")
    except Exception as e:
        print(f"[!] An unexpected error occurred: {e}")

if __name__ == '__main__':
    # Default filenames
    input_filename = 'input.txt'
    output_filename = 'output.txt'
    
    # Create a dummy input file if one doesn't exist (for demonstration)
    try:
        with open(input_filename, 'x') as f:
            f.write("apple: red\nbanana: yellow\ncherry: red\nspinach: green\n")
            print("[*] Created sample input.txt file.")
    except FileExistsError:
        pass

    invert_dictionary_file(input_filename, output_filename)
