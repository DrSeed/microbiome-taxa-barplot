import os,numpy as np,matplotlib;matplotlib.use("Agg")
import matplotlib.pyplot as plt
os.makedirs("figures",exist_ok=True);os.makedirs("results",exist_ok=True)
rng=np.random.default_rng(8)
taxa=["Firmicutes","Bacteroidetes","Proteobacteria","Actinobacteria","Verrucomicrobia","Other"]
samples=[f"S{i+1}" for i in range(8)]
data=rng.dirichlet(np.array([5,4,1.5,1,0.5,0.5]),8).T  # taxa x samples
bottom=np.zeros(8)
plt.figure(figsize=(8,4.5))
for i,t in enumerate(taxa):
    plt.bar(samples,data[i],bottom=bottom,label=t);bottom+=data[i]
plt.ylabel("relative abundance");plt.title("Microbiome composition (demo data)")
plt.legend(bbox_to_anchor=(1.01,1),loc="upper left",fontsize=8)
plt.tight_layout();plt.savefig("figures/demo.png",dpi=150)
open("results/summary.txt","w").write("8 samples, 6 taxa\n");print("ok")