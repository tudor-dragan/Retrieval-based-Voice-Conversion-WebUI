from huggingface_hub import hf_hub_download
import os

files = [
"hubert_base.pt", "rmvpe.pt", "rmvpe.onnx",
"pretrained_v2/f0D40k.pth", "pretrained_v2/f0G40k.pth",
"pretrained_v2/f0D48k.pth", "pretrained_v2/f0G48k.pth",
"uvr5_weights/HP2_all_vocals.pth", "uvr5_weights/VR-DeEchoNormal.pth"
]

for f in files:
	print(f"Downloading {f}...")
	os.makedirs(os.path.dirname(f) if os.path.dirname(f) else ".", exist_ok=True)
	hf_hub_download(repo_id="lj1995/VoiceConversionWebUI", filename=f, local_dir=".", local_dir_use_symlinks=False)
print("Done.")