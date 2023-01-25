set models_path="./my_models/"
webui.bat --server-name="0.0.0.0" --port=8080 --models_path=%models_path%
rem --ckpt-dir="${models_path}Stable-diffusion" --embeddings-dir="${models_path}embeddings" --hypernetwork-dir="${models_path}hypernetworks" --deepdanbooru --clip-models-path="${models_path}BLIP"

