This module is very lightweight and only takes about 50kb after installation.

**GitHub Repo :** https://github.com/Tanishq-Banyal/toastify

**Install Using :** `pip install toastify`

**#+++++++++------EXAMPLE------++++++++++#**

```python
from toastify import notify

# CALLING WITH ALL PARAMETERS :-
notify (
	BodyText='BodyText is Required !',
	AppName='AppName (Optional)',
	AppPath='AppPath (Optional)',
	TitleText='TitleText (Optional)',
	ImagePath='optional_image_path(jpg/png/bmp/ico)'
	)
```

***OR IF YOU ONLY WANT BODY TEXT THEN YOU CAN JUST DO :-***
```python
notify('My Body Text')
```

**#+++++++++-------NOTES-------++++++++++#**

1. NOTIFICATION TIME IS SYSTEM DEAFULT (5sec)

2. The function is blocking by default but you can use threading/asyncio

3. StartMenu Shortcut will be created for your app. (this is a requirement set by microsoft for Toast Notifications)

4. BodyText argument is required !! , rest of the arguments are optional.

5. App Icon Is Set Automatically, it is same as icon of the application that the AppName shortucut in start menu is pointing.
