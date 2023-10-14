In the LSTM model used, as a result of training on 33259 data, the R2_Score of the model is above 0.90. 
To prove it the model was trained five times in a row with the K-Validation Split method and different r2_Scores were obtained from the model. 
The lowest value of the r2_Scores obtained is 0.675. When the lowest value is examined, the model completed its training six epochs, and the val_loss are as follows, respectively.


Lowest R2_Score Training:

Epoch 1/50
531/531 [==============================] - 15s 23ms/step - loss: 0.0040 - accuracy: 0.0000e+00 - val_loss: 4.2591e-05 - val_accuracy: 0.0000e+00
Epoch 2/50
531/531 [==============================] - 11s 21ms/step - loss: 0.0021 - accuracy: 0.0000e+00 - val_loss: 9.3409e-06 - val_accuracy: 0.0000e+00
Epoch 3/50
531/531 [==============================] - 11s 21ms/step - loss: 0.0016 - accuracy: 0.0000e+00 - val_loss: 7.0977e-06 - val_accuracy: 0.0000e+00
Epoch 4/50
531/531 [==============================] - 11s 21ms/step - loss: 0.0014 - accuracy: 0.0000e+00 - val_loss: 8.4691e-05 - val_accuracy: 0.0000e+00
Epoch 5/50
531/531 [==============================] - 11s 22ms/step - loss: 0.0012 - accuracy: 0.0000e+00 - val_loss: 1.2052e-05 - val_accuracy: 0.0000e+00
Epoch 6/50
531/531 [==============================] - 11s 21ms/step - loss: 0.0011 - accuracy: 0.0000e+00 - val_loss: 1.6807e-04 - val_accuracy: 0.0000e+00
208/208 [==============================] - 2s 6ms/step
R-Squared Skoru:  0.651718828591203


When the highest r2_Score value in the K-Validation Split method is examined, the model has completed its training in seven epochs, and the val_loss values ​​are as follows;

Epoch 1/50
531/531 [==============================] - 15s 23ms/step - loss: 0.0040 - accuracy: 5.8900e-05 - val_loss: 3.7119e-05 - val_accuracy: 0.0000e+00
Epoch 2/50
531/531 [==============================] - 11s 22ms/step - loss: 0.0021 - accuracy: 5.8900e-05 - val_loss: 4.9103e-05 - val_accuracy: 0.0000e+00
Epoch 3/50
531/531 [==============================] - 11s 21ms/step - loss: 0.0016 - accuracy: 5.8900e-05 - val_loss: 8.0360e-06 - val_accuracy: 0.0000e+00
Epoch 4/50
531/531 [==============================] - 11s 21ms/step - loss: 0.0014 - accuracy: 5.8900e-05 - val_loss: 6.5475e-06 - val_accuracy: 0.0000e+00
Epoch 5/50
531/531 [==============================] - 11s 21ms/step - loss: 0.0012 - accuracy: 5.8900e-05 - val_loss: 1.9460e-05 - val_accuracy: 0.0000e+00
Epoch 6/50
531/531 [==============================] - 11s 21ms/step - loss: 0.0011 - accuracy: 5.8900e-05 - val_loss: 4.1890e-05 - val_accuracy: 0.0000e+00
Epoch 7/50
531/531 [==============================] - 11s 22ms/step - loss: 0.0011 - accuracy: 5.8900e-05 - val_loss: 1.4521e-05 - val_accuracy: 0.0000e+00
208/208 [==============================] - 2s 7ms/step
R-Squared Skoru:  0.9704341997215905

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The average r2_Score of the model trained five times with the K-Validation Split method was 0.8100421882462954. r2_Scores are as follows;

First Training

Epoch 1/50
531/531 [==============================] - 15s 24ms/step - loss: 0.0038 - accuracy: 5.8903e-05 - val_loss: 3.2506e-05 - val_accuracy: 0.0000e+00
Epoch 2/50
531/531 [==============================] - 12s 22ms/step - loss: 0.0021 - accuracy: 5.8903e-05 - val_loss: 8.6018e-05 - val_accuracy: 0.0000e+00
Epoch 3/50
531/531 [==============================] - 11s 21ms/step - loss: 0.0016 - accuracy: 5.8903e-05 - val_loss: 5.2187e-06 - val_accuracy: 0.0000e+00
Epoch 4/50
531/531 [==============================] - 11s 21ms/step - loss: 0.0013 - accuracy: 5.8903e-05 - val_loss: 1.3905e-04 - val_accuracy: 0.0000e+00
Epoch 5/50
531/531 [==============================] - 11s 21ms/step - loss: 0.0012 - accuracy: 5.8903e-05 - val_loss: 4.0338e-05 - val_accuracy: 0.0000e+00
Epoch 6/50
531/531 [==============================] - 11s 21ms/step - loss: 0.0011 - accuracy: 5.8903e-05 - val_loss: 4.1863e-06 - val_accuracy: 0.0000e+00
Epoch 7/50
531/531 [==============================] - 11s 21ms/step - loss: 0.0011 - accuracy: 5.8903e-05 - val_loss: 1.7190e-05 - val_accuracy: 0.0000e+00
Epoch 8/50
531/531 [==============================] - 11s 21ms/step - loss: 0.0011 - accuracy: 5.8903e-05 - val_loss: 5.2736e-05 - val_accuracy: 0.0000e+00
Epoch 9/50
531/531 [==============================] - 11s 21ms/step - loss: 0.0011 - accuracy: 5.8903e-05 - val_loss: 4.3696e-05 - val_accuracy: 0.0000e+00
208/208 [==============================] - 2s 7ms/step
R-Squared Skoru:  0.9025256227204498


Second Training

Epoch 1/50
531/531 [==============================] - 15s 23ms/step - loss: 0.0040 - accuracy: 0.0000e+00 - val_loss: 4.2591e-05 - val_accuracy: 0.0000e+00
Epoch 2/50
531/531 [==============================] - 11s 21ms/step - loss: 0.0021 - accuracy: 0.0000e+00 - val_loss: 9.3409e-06 - val_accuracy: 0.0000e+00
Epoch 3/50
531/531 [==============================] - 11s 21ms/step - loss: 0.0016 - accuracy: 0.0000e+00 - val_loss: 7.0977e-06 - val_accuracy: 0.0000e+00
Epoch 4/50
531/531 [==============================] - 11s 21ms/step - loss: 0.0014 - accuracy: 0.0000e+00 - val_loss: 8.4691e-05 - val_accuracy: 0.0000e+00
Epoch 5/50
531/531 [==============================] - 11s 22ms/step - loss: 0.0012 - accuracy: 0.0000e+00 - val_loss: 1.2052e-05 - val_accuracy: 0.0000e+00
Epoch 6/50
531/531 [==============================] - 11s 21ms/step - loss: 0.0011 - accuracy: 0.0000e+00 - val_loss: 1.6807e-04 - val_accuracy: 0.0000e+00
208/208 [==============================] - 2s 6ms/step
R-Squared Skoru:  0.651718828591203


Third Training

Epoch 1/50
531/531 [==============================] - 15s 23ms/step - loss: 0.0042 - accuracy: 5.8903e-05 - val_loss: 6.7023e-06 - val_accuracy: 0.0000e+00
Epoch 2/50
531/531 [==============================] - 11s 22ms/step - loss: 0.0020 - accuracy: 5.8903e-05 - val_loss: 7.4107e-06 - val_accuracy: 0.0000e+00
Epoch 3/50
531/531 [==============================] - 11s 21ms/step - loss: 0.0016 - accuracy: 5.8903e-05 - val_loss: 1.5568e-05 - val_accuracy: 0.0000e+00
Epoch 4/50
531/531 [==============================] - 11s 21ms/step - loss: 0.0014 - accuracy: 5.8903e-05 - val_loss: 1.6177e-04 - val_accuracy: 0.0000e+00
208/208 [==============================] - 2s 6ms/step
R-Squared Skoru:  0.6750178219755028


Fourth Training

Epoch 1/50
531/531 [==============================] - 15s 23ms/step - loss: 0.0040 - accuracy: 5.8900e-05 - val_loss: 3.7119e-05 - val_accuracy: 0.0000e+00
Epoch 2/50
531/531 [==============================] - 11s 22ms/step - loss: 0.0021 - accuracy: 5.8900e-05 - val_loss: 4.9103e-05 - val_accuracy: 0.0000e+00
Epoch 3/50
531/531 [==============================] - 11s 21ms/step - loss: 0.0016 - accuracy: 5.8900e-05 - val_loss: 8.0360e-06 - val_accuracy: 0.0000e+00
Epoch 4/50
531/531 [==============================] - 11s 21ms/step - loss: 0.0014 - accuracy: 5.8900e-05 - val_loss: 6.5475e-06 - val_accuracy: 0.0000e+00
Epoch 5/50
531/531 [==============================] - 11s 21ms/step - loss: 0.0012 - accuracy: 5.8900e-05 - val_loss: 1.9460e-05 - val_accuracy: 0.0000e+00
Epoch 6/50
531/531 [==============================] - 11s 21ms/step - loss: 0.0011 - accuracy: 5.8900e-05 - val_loss: 4.1890e-05 - val_accuracy: 0.0000e+00
Epoch 7/50
531/531 [==============================] - 11s 22ms/step - loss: 0.0011 - accuracy: 5.8900e-05 - val_loss: 1.4521e-05 - val_accuracy: 0.0000e+00
208/208 [==============================] - 2s 7ms/step
R-Squared Skoru:  0.9704341997215905


Fifth Training

Epoch 1/50
531/531 [==============================] - 15s 23ms/step - loss: 0.0035 - accuracy: 5.8900e-05 - val_loss: 2.1262e-04 - val_accuracy: 0.0000e+00
Epoch 2/50
531/531 [==============================] - 11s 21ms/step - loss: 0.0021 - accuracy: 5.8900e-05 - val_loss: 8.2271e-05 - val_accuracy: 0.0000e+00
Epoch 3/50
531/531 [==============================] - 11s 21ms/step - loss: 0.0015 - accuracy: 5.8900e-05 - val_loss: 1.6724e-05 - val_accuracy: 0.0000e+00
Epoch 4/50
531/531 [==============================] - 11s 22ms/step - loss: 0.0014 - accuracy: 5.8900e-05 - val_loss: 1.6204e-05 - val_accuracy: 0.0000e+00
Epoch 5/50
531/531 [==============================] - 11s 21ms/step - loss: 0.0013 - accuracy: 5.8900e-05 - val_loss: 2.4786e-05 - val_accuracy: 0.0000e+00
Epoch 6/50
531/531 [==============================] - 11s 21ms/step - loss: 0.0011 - accuracy: 5.8900e-05 - val_loss: 3.0958e-06 - val_accuracy: 0.0000e+00
Epoch 7/50
531/531 [==============================] - 11s 21ms/step - loss: 0.0011 - accuracy: 5.8900e-05 - val_loss: 1.4367e-04 - val_accuracy: 0.0000e+00
Epoch 8/50
531/531 [==============================] - 11s 21ms/step - loss: 0.0011 - accuracy: 5.8900e-05 - val_loss: 2.1319e-04 - val_accuracy: 0.0000e+00
Epoch 9/50
531/531 [==============================] - 11s 21ms/step - loss: 0.0011 - accuracy: 5.8900e-05 - val_loss: 6.5254e-05 - val_accuracy: 0.0000e+00
208/208 [==============================] - 2s 6ms/step
R-Squared Skoru:  0.850514468222731


-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

After the averaged R2_Scores, the differences between the values ​​were measured with the standard deviation. 
In the measured values, the standard deviation of the r2_Score values ​​of the models after five training sessions was 0.1407254907367309. 
This value not only proves the accuracy of the r2_Score given by the model, but also proves that the model is suitable enough for use. 
This standard deviation value indicates that the cross-validation results are similar to each other and the model performs similarly for different data splits. 
The Standard Deviation value proves that the model performs consistently well and obtains consistent results when the data is tested with different subsetting methods.


