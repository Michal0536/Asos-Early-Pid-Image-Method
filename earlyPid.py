from earlyPIDutils import *
import logging

logging.basicConfig(filename='app.log', filemode='w', format='%(levelname)s - %(message)s')


def search(startPID, endPID,taskID):
    taskID = str(taskID)
    log(f"Started {taskID}. task")
    c=0
    for pid in range(startPID, endPID):
        try:
            if c % 100 == 0:
                with open(f'TASK{taskID}.txt','w') as save:
                    save.write(str(pid))

            c+=1
            CorrectPID = scrap(pid)
            if CorrectPID:
                response = check(pid)
                if not response.ok:
                    log_success(f"[TASK {taskID}] [{pid}] Product Page not loaded.")
                    link = fetch_link(pid)

                    with open("PIDS.txt",'r') as file:
                        x = [line.rstrip() for line in file.readlines()]

                    if str(pid) not in str(x):
                        if checkImage(link) == "SUCCESS":
                            log_success(f"[TASK {taskID}] [{pid}] image may contain shoe!")
                            with open("PIDS.txt",'a') as file:
                                file.write(f"[{pid}] {link}\n")                   
        except Exception as er:
            logging.warning(f'[{datetime.now()}] {pid} - {er}')

if __name__ == '__main__':
    with open("PIDS.txt",'a') as file:
        file.write(f"\n{datetime.now()}\n\n")

    for file in range(1,100):
        try:
            with open(f'TASK{file}.txt','r') as f:
                lastPID = int(f.readline())

            with open(f'TASK{file+1}.txt','r') as f:
                nextlastPID = int(f.readline())

        except FileNotFoundError:
            nextlastPID = 209999999


        _thread = threading.Thread(target=search,args=(lastPID,nextlastPID,file,))
        _thread.start()
