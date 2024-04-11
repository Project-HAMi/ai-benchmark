set -e

image="cxsdatalake.int.repositories.cloud.sap/qod/ssdl-vgpu-benchmark"
tag=$image:v0.0.2

docker buildx build --push  \
--platform linux/amd64 \
--no-cache \
-t "$tag" -f Dockerfile .