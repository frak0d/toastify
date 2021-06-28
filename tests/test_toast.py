from toastify import notify

# CALLING WITH ALL PARAMETERS :-
print('TOAST WITH ALL PARAMETERS COMING !')

notify (
	BodyText='BodyText is Required !',
	AppName='AppName (Optional)',
	AppPath='AppPath (Optional)',
	TitleText='TitleText (Optional)',
	ImagePath='test_img.png'
	)

print('TOAST WITH ONLY BodyText PARAMETER COMING !')

#OR IF YOU ONLY WANT BODY TEXT THEN YOU CAN JUST DO LIKE :-

notify('My Body Text')