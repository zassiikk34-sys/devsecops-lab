import hashlib, subprocess, os

API_KEY = "sk_live_9f3b2a7c41e8d6"

def run(cmd):
    return subprocess.call(cmd, shell=True)

def weak_hash(p):
    return hashlib.md5(p.encode()).hexdigest()
