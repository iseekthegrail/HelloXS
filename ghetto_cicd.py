#!/usr/bin/env python

import time, sys, os, subprocess, shlex
from colorama import Fore, Back, Style
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler

# local
container_name = 'di2020_wojke'
stop = 'docker stop ' + container_name
rm = 'docker rm -f ' + container_name
rmi = 'docker rmi -f ' + container_name
build = 'docker image build -t ' + container_name + ' .'
run = 'docker run --rm -ti --name ' + container_name + ' ' + container_name
prune = 'docker system prune -f'

class MyHandler(PatternMatchingEventHandler):
    patterns = ["*build*"]

    def process(self, event):
        """
        event.event_type
            'modified' | 'created' | 'moved' | 'deleted'
        event.is_directory
            True | False
        event.src_path
            path/to/observed/file
        """
        # the file will be processed there
        print (event.src_path, event.event_type)  # print degugging

    def on_modified(self, event):
        self.process(event)
        # Build and deploy conainer
        print (Fore.WHITE + Back.RED + "___STOPPING RUNNING CONTAINER: " + container_name + '___' + Style.RESET_ALL)
        stop_proc = subprocess.Popen(shlex.split(stop), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stop_proc.wait()
        print (Fore.WHITE + Back.RED + "___REMOVING CONTAINER: " + container_name + '___' + Style.RESET_ALL)
        rm_proc = subprocess.Popen(shlex.split(rm), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        rm_proc.wait()
        rmi_proc = subprocess.Popen(shlex.split(rmi), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        rmi_proc.wait()
        print (Fore.WHITE + Back.BLUE + "___BUILDING NEW IMAGE: " + container_name + '___' + Style.RESET_ALL)
        build_proc = subprocess.Popen(shlex.split(build))
        build_proc.wait()
        print (Fore.WHITE + Back.GREEN + "___RUNNING CONTIANER: " + container_name + '___' + Style.RESET_ALL)
        run_proc = subprocess.Popen(shlex.split(run))
        time.sleep(10)
        prune_proc = subprocess.Popen(shlex.split(prune), stdout=subprocess.PIPE)

    def on_created(self, event):
        self.process(event)
        
if __name__ == '__main__':
    args = sys.argv[1:]
    observer = Observer()
    observer.schedule(MyHandler(), path=args[0] if args else '.')
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()
