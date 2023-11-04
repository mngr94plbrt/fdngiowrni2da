import subprocess
import time

# Data nama cluster dan docker image
data = [
"ClusterA1|hzalkq/aq:ku",
"DockerCloud|xvmdqm/my:ad",
"KontainerKingdom|jdniqu/ar:ti",
"CloudContainers|cddqjh/ju:ma",
"ECSMaster|mxouam/ro:ki",
"DockerDynasty|gpizkf/fa:ki",
"KontainerKubu|xrkbha/at:ab",
"ClusterCentral|uplnlb/bu:la",
"KontainerKloud|gkuyfi/ru:an",
"ECSWave|npcmkb/bu:an",
"Dockerville|ceukfb/bu:an",
"KubeHarbor|atwpsr/to:an",
"ElasticSwarm|bnsyiy/ab:va",
"KontainerCore|grrikq/qi:ku",
"ECSHive|ykrssl/ko:ra",
"DockerDelight|soltcg/ro:na",
"KubeNest|vjtlxs/mu:da",
"CloudCortex|gqdrke/li:an",
"ClusterNexa|brabma/ar:en",
"KontainerKonnect|hrabbz/lo:su"
]

# Split data menjadi list cluster_name dan docker_image
cluster_data = [entry.split('|') for entry in data]

# Membuat dan menjalankan 20 perintah cmd dengan penundaan 3 detik
for i in range(20):
    cluster_name, docker_image = cluster_data[i]
    cmd = f"python g.py {cluster_name} {docker_image}"  # Ganti 'script.py' dengan nama file script Anda
    subprocess.Popen(['start', 'cmd', '/k', cmd], shell=True)
    
    # Menambahkan penundaan 3 detik sebelum membuka cmd berikutnya
    time.sleep(8)

print("DONE!")
