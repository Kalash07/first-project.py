import csv
def write_into_csv(info_list):
	with open('student_info.csv','a',newline=' ')as csv_file:
		writer=csv.writer(csv_file)
		
		if csv_file.tell( )==0:
				writer.writerow(["Name","Age","Contact number","E-mail ID"])
			
			writer.writerow(info_list)
			
if __name__=='__main__':
	 condition=True
	 student_num=1
	 
	 	while(condition):
	 		student_info=input("Enter student information for student #{ } in the following format (Name Age Contact number E-mail ID):".format(student_num))
	 		
	 		student_info_list=student_info.splits(' ')
	 		
	 		print("\nThe entered information is \nName: { } \nAge: { }\nContact_number: { }\nE-mail ID:  {}"
	 		.format(student_info_list[0],student_info_list[1],student_info_list[2],student_info_list[3]))

choice_check=input("Is entered information is correct?(Yes/No):")


if choice_check=="Yes":
	write_info_csv(student_info_list)
	
	condition_check=input("Enter(Yes/No) if you want to enter information for another student: ")
	if condition_check=="Yes":
		condition=True
		student_num=student_num+1
		elif condition_check=="No":
			Condition=False
			elif choice_check=="No":
				print("\nPlease re-enter the values!")
			
