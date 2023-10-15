from django import forms


status = (
			("created" , "CREATED"),
			("in progress", "IN PROGRESS"),
			("complete" , "COMPLETE")
		)


class TaskCreateForm(forms.Form):
	task = forms.CharField(label=False, max_length=255, required=True, 
						   widget=forms.TextInput(attrs={"class" : "form-control", 
						   								 "placeholder" : "Enter Task ...",}))


class UpdateTaskForm(forms.Form):
	task = forms.CharField(label="Task Name ", max_length=255, required=True,
							widget=forms.TextInput(attrs={"class" : "form-control col-md-8"}))
	status = forms.ChoiceField(label="Status", choices=status, widget=forms.Select(attrs= {"class" : "form-control"}))



