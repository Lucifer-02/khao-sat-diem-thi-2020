import subprocess

result = subprocess.check_output('curl -F "sobaodanh=02000001" diemthi.hcm.edu.vn/Home/Show', shell= True)

print(result)