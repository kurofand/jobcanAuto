# jobcanAuto
Jobcan timecard system automatization script.<br>
The goal is develop semi-automatic script for "push" button in timecard system provided by Jobcan.<br>
The script accepts user's email and password as arguments(--email, --password).
The script can be executed manually or by cron.<br><br>
Script run params:<br>
	--email str - user's email for login to system<br>
	--password str - user's password<br>
	--randomizeTime int - param for randomize execution time in minutes. e.g. --randomizeTime 5 will "push" button in 0-5 minutes from script execution<br>
	--groupId int - manually sets user's group id. If not setted script will be use default option<br>
	--nightShift bool(0 or 1) - manually sets night shift param. Default 0<br>
	--notice str - manually sets notice param. Default empty
