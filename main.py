# -*- coding: utf-8 -*-
import subprocess
import sys
import unittest

from usecases.ConnectWebinar import ConnectWebinar

import click
@click.command()
@click.option("--type", "-t", "type", required=True, help="Type of conference [webinar, freeconferencecall]")
@click.option("--name", "-n", "name", required=True, help="The name of the person who enters the conference")
@click.option("--url", "-u", "url", required=True, help="Link to the conference")
@click.option("--wait-time", "wait_time", required=False, type=click.INT, default=60, help="Time to wait for connection to the conference in seconds (default 60 sec)")
@click.option("--presence-time", "presence_time", required=False, type=click.INT, default=4805, help="Time to be presence at the conference in seconds (default 1 h 35 min)")
@click.option("--key", "-k", "key", required=False, help="If the conference has a key, you may specify it")
@click.option("--no-headless", "no_headless", is_flag=True, help="With GUI, if this flag is true")
@click.option("--no-sandbox", "no_sendbox", is_flag=True, help="Use it, running an app as a root user (for example, in Docker container)")
def process(no_sendbox, no_headless, type, name, url, wait_time, presence_time, key):
    if type == 'webinar':
        action = ConnectWebinar(no_sendbox, not no_headless, name, url, wait_time, presence_time, key)
        action.perform()

if __name__ == '__main__':
    process()
    
