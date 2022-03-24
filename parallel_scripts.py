import re

files_to_include = ['my_class.py', 'dir/other_file.py', 'main.py']

output_file = 'bundled_code.py'

if __name__ == "__main__":

    all_code = []

    for file_name in files_to_include:
        with open(file_name, 'r') as file:
            code = file.readlines()

        ignore = []
        for file_name in files_to_include:
            file_name_no_dir_no_extension = file_name.split('.py')[0].split(
                '/')[-1]

            for line_of_code in code:
                if re.findall(
                        f'(import|from).*{file_name_no_dir_no_extension}.*',
                        line_of_code):
                    ignore += [line_of_code]

        code = [line for line in code if line not in ignore]

        all_code += code

    with open(output_file, 'w+') as file:
        file.write(''.join(all_code))
