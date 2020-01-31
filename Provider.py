#!/usr/bin/env python3
import subprocess
from pprint import pprint
from cloudmesh.common.util import banner


class Provider:
    def __init__(self, name, *, command: str = 'multipass', sudo: bool = False):
        self.name = name
        self.__base_command = [command]
        if sudo:
            self.__base_command.insert(0, 'sudo')

    def __exec(self, operation: str = 'list', *args):
        try:
            command = self.__base_command.copy()
            command.append(operation)
            command.extend(args)
            subprocess.call(command)
        except OSError as e:
            print(f"Error while executing command: {e}")

    def list(self):
        banner("Running list")
        self.__exec('list')

    def exec(self, *command):
        banner(f"Executing commands on VM {self.name}")
        self.__exec('exec', self.name, *command)

    def start(self):
        banner(f"Starting {self.name}...")
        self.__exec('start', self.name)

    def stop(self):
        banner(f"Stopping {self.name}...")
        self.__exec('stop', self.name)

    def restart(self):
        banner(f"Restarting {self.name}...")
        self.__exec('stop', self.name)


if __name__ == "__main__":
    p = Provider('ubuntu-lts', sudo=True)
    p.list()
    p.exec('date')
