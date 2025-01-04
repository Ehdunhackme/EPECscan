# EPECscan: A Deep Learning-based Screening Model for Detecting and Classifying the Growth Stage of Enteropathogenic Escherichia coli Bacteria From Microscopic Water Samples

## Project Abstract

(This project is presented in Science and Technology Symposium for Youths 2024 hosted by Chung Ling High School)

Enteropathogenic Escherichia coli, commonly known as EPEC, is a gram-negative bacteria that causes acute diarrhoea in children and babies. EPEC is most commonly found in water sources contaminated by faecal matter, particularly in third-world countries such as India and Bangladesh. However, the manual screening process for EPEC in water samples requires at least 12-48 hours and is prone to human error. This has led to large multistate outbreaks in the United States and causes 1.8 million deaths among children annually. In this study, we propose EPECscan - a screening model designed to enhance the accuracy and efficiency of screening in microscopic images of water samples. Our model is developed based on a modified single RGB channel YOLOv8m architecture and is trained on a public dataset of microscopic images with EPEC bacteria annotated into different growth stages. Our model achieves remarkable accuracy with a model accuracy of 95.4%, a mAP50 of 0.990, and a mAP50-95 of 0.794, with a total processing time of 13.2 seconds for 70 test images. The model was further interpreted with Grad-CAM++ to produce a decision heatmap to explain the model's decision-making process. Results showed that our model is capable of detecting all instances of EPEC in both clean and noisy scenarios. Additionally, we built and deployed a user-friendly web interface using Gradio on the Hugging Face platform. Our findings show that EcoliScan reduces screening delays whilst increasing speed and capability in detecting EPEC and EPEC growth stage classification. This enables relevant departments to swiftly take action for the removal of EPEC from contaminated water sources, thus reducing the risk of EPEC infections.

## Model Deployment

https://huggingface.co/spaces/EPECScan/EPECScan

## Results Preview

![image](https://github.com/user-attachments/assets/de43aa53-5fae-45f3-bb91-ef61b5ba2d60) ![image](https://github.com/user-attachments/assets/ac53e797-957b-4a8e-af9b-c1091bdb92e8)

## Decision Heatmaps Preview Using GradCAM++

![output2](https://github.com/Ehdunhackme/EcoliScan/assets/75579286/feb230e4-0e05-4242-846e-769582d52473) ![output3](https://github.com/Ehdunhackme/EcoliScan/assets/75579286/b0a6cc6a-c16f-4db7-8984-a058ad5dc6f5) ![output16](https://github.com/Ehdunhackme/EcoliScan/assets/75579286/73184770-00b4-4d57-a46e-765e0fd9b896)

## PR curve
![PR_curve](https://github.com/user-attachments/assets/458d9337-dc0c-44ff-8ff6-6b46d0bf725b)



## Confusion Matrix
![confusion matrix](https://github.com/user-attachments/assets/a1a2f70b-02aa-43ca-bd0f-a5fe8fcee200)


## Model inference time histogram
![Model Inference Histogram With CPU](https://github.com/user-attachments/assets/1bf4b583-96f8-441e-9a2e-9ba79715ef55)






