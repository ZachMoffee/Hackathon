import pandas as pd
def lowercase_all_text(filename="new.csv"):
    df = pd.read_csv(filename)

    # Convert all characters in both columns to lowercase
    df['statement'] = df['statement'].astype(str).str.lower()
    df['status'] = df['status'].astype(str).str.lower()

    # Save the modified file in place
    df.to_csv(filename, index=False)
    print(f"✅ All text converted to lowercase and saved back to '{filename}'.")

if __name__ == "__main__":
    lowercase_all_text()


import pandas as pd

def capitalize_first_word(text):
    if not isinstance(text, str) or not text.strip():
        return text
    words = text.strip().strip('"').split()
    if not words:
        return text
    words[0] = words[0].capitalize()
    return ' '.join(words)

def capitalize_first_words_in_place(filename="new.csv"):
    df = pd.read_csv(filename)

    # Apply capitalization function to both 'statement' and 'status' columns
    df['statement'] = df['statement'].astype(str).apply(capitalize_first_word)
    df['status'] = df['status'].astype(str).apply(capitalize_first_word)

    # Save the modified DataFrame back to the same file
    df.to_csv(filename, index=False)
    print(f"✅ Capitalized first word in both columns and updated '{filename}' in place.")

if __name__ == "__main__":
    capitalize_first_words_in_place()
def fix_commas_in_place(filename="new.csv"):
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    fixed_lines = []
    for line in lines:
        parts = line.strip().split(',')

        if len(parts) == 3:
            # Merge first two fields
            merged = f'"{parts[0].strip()} {parts[1].strip()}",{parts[2].strip()}'
            fixed_lines.append(merged + '\n')

        elif len(parts) == 4:
            # Merge first three fields
            merged = f'"{parts[0].strip()} {parts[1].strip()} {parts[2].strip()}",{parts[3].strip()}'
            fixed_lines.append(merged + '\n')

        else:
            # Leave all other lines unchanged
            fixed_lines.append(line)

    with open(filename, 'w', encoding='utf-8') as file:
        file.writelines(fixed_lines)

    print(f"✅ Fixed lines with 3 or 4 comma-separated values. Updated '{filename}' in place.")

if __name__ == "__main__":
    fix_commas_in_place()
