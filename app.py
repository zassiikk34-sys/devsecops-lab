import hashlib, subprocess, shlex, os

API_KEY = os.environ.get("API_KEY")

def run(cmd):
    return subprocess.call(shlex.split(cmd))

def strong_hash(p):
    return hashlib.sha256(p.encode()).hexdigest()
