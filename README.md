# GreenEyeAssignment

First of all I decided to save the data in three seperate dictionaries, where the keys are the name and the values are the ground truths,
predictions and images. This way the access is quick.

For every detection by the precdiction or ground truth, I drew a rectangle on the image, representing the detection.
RED - will be the truth while BLUE - will be the prediction.

Regarding the metric, I counted for each image the number of missed detections by checking the diference between the prediction and truth detections.

I tried in the time constraint to try and use pickle so that the code will run by you. I am working on it now anyway.




