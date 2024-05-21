>Note: This repository is a fork of the original [AI-Benchmark](https://github.com/houseofai/ai-benchmark)

# Intro

[AI Benchmark Alpha](http://ai-benchmark.com/alpha) is an open source python library for evaluating AI performance of various hardware platforms, including CPUs, GPUs and TPUs. The benchmark is relying on [TensorFlow](https://www.tensorflow.org) machine learning library, and is providing a lightweight and accurate solution for assessing inference and training speed for key Deep Learning models.</br></br>

In its entirety, AI Benchmark is executed on the following test scenarios:

- Classification
  - MobileNet-V2
  - Inception-V3
  - Inception-V4
  - Inception-ResNet-V2
  - ResNet-V2-50
  - ResNet-V2-152
  - VGG-16
- Image-to-Image Mapping
  - SRCNN 9-5-5
  - VGG-19 Super-Res
  - ResNet-SRGAN
  - ResNet-DPED
  - U-Net
  - Nvidia-SPADE
- Image Segmentation
  - ICNet
  - PSPNet
  - DeepLab
- Inpainting
  - Pixel-RNN
- Sentence Sentiment Analysis
  - LSTM-Sentiment

For more information and results, please visit the project website: [http://ai-benchmark.com/alpha](http://ai-benchmark.com/alpha)</br></br>

# Quick Start

## How to run locally

Install the required packages:

```bash
pip install --no-cache-dir -r requirements.txt
```

Run the benchmark:

```bash
python main.py
```

## How to run in k8s

Build the docker image

```bash
sh build.sh
```

Apply the k8s deployment

```bash
# k apply -f benchmark-job.yml
apiVersion: batch/v1
kind: Job
metadata:
  name: ai-benchmark
  namespace: gpu-test-workloads
  labels:
    app: ai-benchmark
spec:
  parallelism: 1
  completions: 2
  template:
    metadata:
      labels:
        app: ai-benchmark
    spec:
      restartPolicy: Never
      containers:
        - name: ai-benchmark
          image: vgpu-benchmark:v0.0.1
          resources:
            limits:
              cpu: "11"
              memory: "60Gi"
              nvidia.com/gpu: '1'
            requests:
              cpu: "11"
              memory: "60Gi"
          terminationMessagePath: /dev/termination-log
          terminationMessagePolicy: File
          imagePullPolicy: IfNotPresent
      tolerations:
        - key: nvidia.com/gpu
          operator: Exists
          effect: NoSchedule
      priorityClassName: system-cluster-critical
```

## Sample Output

```bash
>>   AI-Benchmark-v.0.1.2   
>>   Let the AI Games begin..

*  TF Version: 2.16.1
*  Platform: Linux-6.1.77-gardenlinux-amd64-x86_64-with-glibc2.35
*  CPU: N/A
*  CPU RAM: 1007 GB
*  GPU/0: NVIDIA H100 80GB HBM3
*  GPU RAM: 77.1 GB
*  CUDA Version: 12.3
*  CUDA Build: V12.3.107

The benchmark is running...
The tests might take up to 20 minutes
Please don't interrupt the script
##### Config Done

1/18. MobileNet-V2

1.1 - training  | batch=50, size=224x224: 34.8 ± 0.8 ms

2/18. Inception-V3

2.1 - training  | batch=20, size=346x346: 43.2 ± 0.5 ms

3/18. Inception-V4

3.1 - training  | batch=10, size=346x346: 43.4 ± 0.8 ms

4/18. Inception-ResNet-V2

4.1 - training  | batch=8, size=346x346: 50.9 ± 0.5 ms

5/18. ResNet-V2-50

5.1 - training  | batch=10, size=346x346: 24.1 ± 0.4 ms

6/18. ResNet-V2-152

6.1 - training  | batch=10, size=256x256: 37.4 ± 0.6 ms

7/18. VGG-16

7.1 - training  | batch=2, size=224x224: 15.6 ± 0.5 ms

8/18. SRCNN 9-5-5

8.1 - training  | batch=10, size=512x512: 57.7 ± 0.7 ms

9/18. VGG-19 Super-Res

9.1 - training  | batch=10, size=224x224: 38.3 ± 19.5 ms

10/18. ResNet-SRGAN

10.1 - training  | batch=5, size=512x512: 32.7 ± 0.7 ms

11/18. ResNet-DPED

11.1 - training  | batch=15, size=128x128: 33.4 ± 0.6 ms

12/18. U-Net

12.1 - training  | batch=4, size=256x256: 35.5 ± 0.5 ms

13/18. Nvidia-SPADE

13.1 - training  | batch=1, size=128x128: 25.2 ± 0.4 ms

14/18. ICNet

14.1 - training  | batch=10, size=1024x1536: 232 ± 2 ms

15/18. PSPNet

15.1 - training  | batch=1, size=512x512: 23.5 ± 0.5 ms

16/18. DeepLab

16.1 - training  | batch=1, size=384x384: 26.8 ± 0.6 ms

17/18. Pixel-RNN

17.1 - training  | batch=10, size=64x64: 977 ± 40 ms

18/18. LSTM-Sentiment

18.1 - training  | batch=10, size=1024x300: 581 ± 10 ms

Device Training Score: 56922
```
