# My Code
def get_content_file():
    file = open('my_test.py', 'r')
    result_read = file.readlines()
    file.close()
    return result_read

#def replacing(result_read):
#    coors = result_read.find('def ' or 'import ' or 'from ')
#    result_read.replace(coors,'')
#    return result_read

def save_result_file(lines):
    file = open('my_result.py', 'w', encoding='utf-8')
    for line in lines:
        if "def " in line or "import " in line or "from " in line:
            continue
        file.write(line)
    file.close()

result_read = get_content_file()
#result_read = replacing(result_read)
save_result_file(result_read)



# Veronika's Code
# your_code =  '''def code_filter(your_code): 
#     result = [] 
#     lines_your_code = your_code.split('\n') 
#     for line in lines_your_code: 
#             if 'def ' in line or 'import ' in line or 'from ' in line: 
#               continue 
#             else: 
#               result += line 
#     return result '''
 
# def code_filter(your_code): 
#     result = [] 
#     lines_your_code = your_code.split('\n') 
#     for line in lines_your_code: 
#             if 'def' in line or 'import' in line or 'from' in line: 
#               continue 
#             else: 
#               result.append(line)
#     return result
# for line in code_filter(your_code):
#     print(line)



# Victor's Code
# def delete_prints_and_inputs(input_file, output_file):
#     with open(input_file, 'r') as file:
#         lines = file.readlines()

#     with open(output_file, 'w') as file:
#         for line in lines:
#             if 'print(' in line or 'input(' in line:
#                 continue
#             file.write(line)

# input_file = 'my_test.py'
# output_file = 'my_result.py'

# delete_prints_and_inputs(input_file, output_file)
