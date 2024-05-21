set -e

image="vgpu-benchmark"
tag=$image:v0.0.1

docker buildx build --push  \
--platform linux/amd64 \
--no-cache \
-t "$tag" -f Dockerfile .