# Traffic Sign Recognition Neural Network

## Overview
This project implements a convolutional neural network (CNN) to classify traffic signs from the German Traffic Sign Recognition Benchmark (GTSRB) dataset. The model is trained to recognize 43 different types of traffic signs.

## Experimentation Process

### Initial Approach
I started with a simple CNN architecture to establish a baseline. The reasoning was to understand how the basic building blocks (convolution, pooling, and dense layers) perform on this classification task before attempting more complex variations.

### Model Architecture
The final implemented model consists of:
- **Two Convolutional Blocks**: Each block contains a Conv2D layer followed by MaxPooling2D
  - First block: 32 filters with 3x3 kernel
  - Second block: 64 filters with 3x3 kernel
- **Flattening Layer**: Converts 2D feature maps to 1D
- **Dense Layers**:
  - Hidden layer with 128 units and ReLU activation
  - Dropout layer with 0.5 rate for regularization
  - Output layer with 43 units (one per category) and softmax activation

### Design Decisions

**Convolutional Layers**: Used 32 and 64 filters respectively. This progression allows the network to learn increasingly complex features. Starting with 32 filters reduces computational cost while 64 filters in the second layer provide enough capacity for more abstract feature representations.

**Pooling Layers**: Applied 2x2 MaxPooling after each convolutional block. This reduces spatial dimensions and helps the network become more robust to small translations in the input images, which is important for real-world traffic sign variations.

**Dropout**: Added a 0.5 dropout rate before the output layer. This helps prevent overfitting, which is crucial when training on a dataset with 43 categories where some categories may have limited training samples.

**Activation Functions**:
- ReLU for hidden layers: Non-linear activation that helps the network learn complex patterns
- Softmax for output layer: Appropriate for multi-class classification, providing probability distributions across all 43 classes

### What Worked Well
- **Conv2D + MaxPooling combination**: This is a proven architecture for image classification tasks. The combination effectively extracts hierarchical features from images.
- **Dropout regularization**: The 0.5 dropout rate effectively prevents overfitting without significantly harming accuracy.
- **Adam optimizer**: Adaptive learning rates work well for this type of problem without requiring manual learning rate tuning.

### What Didn't Work Well
- **Too few filters**: Initial attempts with fewer filters (16-32 total) struggled to achieve good accuracy.
- **Too many dense layers**: Adding excessive dense layers after flattening increased computation without proportional accuracy gains and risked overfitting.
- **No regularization**: Models without dropout showed signs of overfitting on the training data.

### Observations
1. **Image Size**: The 30x30 resize is quite small, but it's sufficient for this task. Larger sizes would increase computational cost significantly.
2. **Categorical Distribution**: Different traffic sign categories likely have different numbers of training samples. The model handles this reasonably well with the current architecture.
3. **Training Convergence**: With 10 epochs, the model shows reasonable training behavior. More epochs might improve accuracy but could lead to overfitting.
4. **Platform Independence**: Using `os.path.join()` ensures the data loading works on Windows, macOS, and Linux without modification.

### Future Improvements
- Experiment with more convolutional layers for deeper feature extraction
- Try different filter sizes and quantities
- Implement data augmentation to handle class imbalance
- Experiment with batch normalization after convolutional layers
- Increase the number of training epochs
- Use callbacks like EarlyStopping to prevent overfitting
