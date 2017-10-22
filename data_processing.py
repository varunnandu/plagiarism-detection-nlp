import os, sys

# Open a file
path = "DATA-NLP"
dirs = os.listdir( path )

question_mapping = dict() # Mapping to question dictionary
student_answer = dict() # Mapping to student as key and answer as value

for file in dirs:
    path_to_file = "DATA-NLP/"
    file_name = file
    split_name = file.split('_')
    student_name = split_name[0]
    question_number = split_name[1].split('.')[0]
    path_to_file = path_to_file + file_name
    with open(path_to_file, 'r') as content_file:
        content = content_file.read()
        student_answer[student_name] = content
        question_mapping[question_number] = student_answer

# for key, value in question_mapping.iteritems():
#     for k, v in value.iteritems():
#         print key , " - ", k, " : ", v





