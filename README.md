# EPECscan: A Deep Learning-based Screening Model for Detecting Enteropathogenic Escherichia coli Bacteria From Microscopic Water Samples

## Project Abstract

Enteropathogenic Escherichia coli, commonly known as EPEC, is a gram-negative bacteria that can cause acute diarrhea in children and babies. EPEC most commonly found in water sources contaminated by faecal matter, particularly in third-world countries such as India and Bangladesh. However, the manual screening process for EPEC in water samples requires at least 12-48 hours and is prone to human error, which has led to large multistate outbreaks in the United States and causes 1.8 million deaths among children annually. In this study, we propose EcoliScan, a screening model designed to enhance the accuracy and efficiency of screening EPEC bacteria in microscopic images of water samples. Our model is developed based on a modified single RGB channel YOLOv8m architecture and is trained on a public dataset of microscopic images  with EPEC bacteria annotated into different classes. Our model achieves remarkable accuracy with a model accuracy of 98.3%, a mAP50 of 0.990, and a mAP50-95 of 0.794, with an average total processing time of 13.2 seconds for 70 test images. The model was further interpreted with Grad-CAM++ to produce a decision heatmap to explain the model's decision-making process. Results showed that our model is capable of detecting all instances of EPEC in both clean and noisy scenarios. Our findings show that EcoliScan reduces screening delays whilst increasing speed and capability in the detection of EPEC. This enables relevant departments to swiftly take action for the removal of EPEC from contaminated water sources, thus reducing the risk of EPEC infections.

## Results Preview

![image](https://github.com/Ehdunhackme/EcoliScan/assets/75579286/5fdfb80b-149b-454b-b417-a2d73c84283a) ![image](https://github.com/Ehdunhackme/EcoliScan/assets/75579286/bf9c9aa4-c0a0-4274-9031-06c8bdd385f4) ![image](https://github.com/Ehdunhackme/EcoliScan/assets/75579286/5a7f66cd-b9bb-41e7-988d-a20753455c95)


## Decision Heatmap Using GradCAM++

![output2](https://github.com/Ehdunhackme/EcoliScan/assets/75579286/feb230e4-0e05-4242-846e-769582d52473) ![output3](https://github.com/Ehdunhackme/EcoliScan/assets/75579286/b0a6cc6a-c16f-4db7-8984-a058ad5dc6f5) ![output16](https://github.com/Ehdunhackme/EcoliScan/assets/75579286/73184770-00b4-4d57-a46e-765e0fd9b896)





