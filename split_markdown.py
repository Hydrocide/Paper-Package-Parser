from constants import MD_FOLDER_PATH

import os

def split_markdown_file(input_file, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    chapter_num = 0
    chapter_lines = []
    for line in lines:
        if line.startswith("######## Chapter "):  # Assuming chapters are denoted by level 1 headings
            if chapter_lines:  # Write previous chapter if exists
                output_file = os.path.join(output_dir, f"chapter_{chapter_num}.md")
                with open(output_file, 'w', encoding='utf-8') as f_out:
                    f_out.writelines(chapter_lines)
                chapter_num += 1
                chapter_lines = []

        chapter_lines.append(line)

    # Write the last chapter
    if chapter_lines:
        output_file = os.path.join(output_dir, f"chapter_{chapter_num}.md")
        with open(output_file, 'w', encoding='utf-8') as f_out:
            f_out.writelines(chapter_lines)




if __name__ == "__main__":
    # Example usage:
    folder_path = MD_FOLDER_PATH
    for file_name in os.listdir(folder_path):
        file_name = file_name.replace(".pdf","")
        output_dir = f"Markdowns\{file_name} chapters"
        file_path = folder_path + "\\" + file_name
        split_markdown_file(file_path, output_dir)
