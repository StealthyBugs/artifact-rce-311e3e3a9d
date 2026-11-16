import os,pathlib,subprocess
p=pathlib.Path(os.environ['RUNNER_TEMP'])/'artifact-rce-6c8d3b834ab2ef881bdec5a7'/'id-result.txt'
with p.open('wb') as f: subprocess.run(['id'],stdout=f,stderr=subprocess.DEVNULL,check=True)
