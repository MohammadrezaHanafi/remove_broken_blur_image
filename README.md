# remove_broken_blur_image
Automatic removal of broken and Blur images

The purpose of this code is that if we have a dataset of facial images and we want to make the dataset contain good and high-quality images, we can easily delete blurry and broken images using this code.

The main idea for the part of removing broken images is that first, we use the SIFT method to extract the features of the face, if the number of extracted features is less than a certain limit, then the image is bad because it could not extract a large number of features.
The value of the maximum number of points that should be extracted is up to the user, according to the data, he can find the minimum and maximum features and consider the average.

Laplacian method is also used to remove blurred images.

The important thing is that the name of the images should be sorted from the number one, which you can use the sorter file for this.

The program works in this way that at first when you run the program, three buttons will be displayed for you. First, specify the space where the images are, then click on the blur or broken button. After clicking, it is next to the same data file. New files are created where you can see broken or blurred images.
