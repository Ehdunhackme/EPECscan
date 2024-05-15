# EcoliScan: A Rapid Screening Model for Detecting Escherichia coli Bacteria From Water Samples Using Deep Learning

## Project Abstract

Escherichia coli, commonly known as E. coli, is a gram-negative bacteria that can cause severe illnesses such as food poisoning, pneumonia and urinary tract infections in humans. E. coli is most commonly found in water contaminated by faecal matter, particularly in third-world countries such as India and Bangladesh. However, the manual screening process for E. coli in water samples requires at least 12-48 hours and is prone to human error, which has led to large multistate outbreaks in the United States and causes 1.8 million deaths among children annually. In this study, we propose EcoliScan, a rapid screening model designed to enhance the accuracy and efficiency of screening E. coli bacteria in microscopic images of water samples. Our model is based on a modified two RGB channel YOLOv8m architecture and is trained on a public dataset of microscopic images containing positive and negative image samples with E. coli bacteria annotated into different classes. Our model achieves remarkable accuracy with a model accuracy of 97.1%, a mAP50 of 0.985, and a mAP50-95 of 0.793, with an average total processing time of 13.2 seconds for 70 test images. The model was further interpreted with Grad-CAM++ and LIME to explain the model's decision-making process. Results showed that our model is capable of detecting all instances of E. coli in the test images. Our findings show that EcoliScan reduces screening delays whilst increasing speed and capability in the detection of E. coli. This enables relevant departments to swiftly take action for the removal of E. coli from contaminated water sources, thus reducing the risk of E. coli infections.

## Results Preview

![image](https://github.com/Ehdunhackme/EcoliScan/assets/75579286/5fdfb80b-149b-454b-b417-a2d73c84283a) ![image](https://github.com/Ehdunhackme/EcoliScan/assets/75579286/bf9c9aa4-c0a0-4274-9031-06c8bdd385f4) ![image](https://github.com/Ehdunhackme/EcoliScan/assets/75579286/5a7f66cd-b9bb-41e7-988d-a20753455c95)


