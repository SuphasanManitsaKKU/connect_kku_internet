Objective: For servers that need to run and want to connect to the KKU internet for a long time

on linux
Step 1: nano connect.sh

    #!/bin/bash
	sudo docker run --rm -ti -d --name connect-script-arm64 -e U_U='username' -e S_S='password' suphasan40/connect_kku_internet:arm64
	sudo docker exec connect-script-arm64 python run.py

Step 2: chmod +x connect.sh


then you can run: ./connect.sh


--------------------------------------------------
on windows

Step 1: New-Item -ItemType File -Name connect.bat

    docker run --rm -ti -d --name connect-script-amd64 -e U_U='username' -e S_S='password' suphasan40/connect_kku_internet:amd64
	docker exec connect-script-amd64 python run.py

then you can run ./connect.bat

if you want to see log in container you can run:

Step 1 run:

    docker exec -it connect-script-amd64 /bin/bash

Step 2: tmux a or cat log.csv

!!! If your computer has an arm64 architecture, change amd64 to arm64  !!!