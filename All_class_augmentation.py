from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img
import os

datagen = ImageDataGenerator(
        rotation_range=40,
        width_shift_range=0.2,
        height_shift_range=0.2,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True,
        fill_mode='nearest')

data_path = 'C:\\Users\\Hp\\pmr_yoke_classes'
classes_folder = os.listdir(data_path) #storing the folder of different class images as list

result_path_dir = 'augmentation_results'
result = os.listdir(result_path_dir) #storing the result folder in the main folder as list

# the loop for augmentation of all the samples of ech class
for j in range(len(classes_folder)):
    classes_list = os.listdir(os.path.join(data_path,classes_folder[j])) # storing the images in each class folder as list
    
    #augmentation of each sample in all the class
    for k in range(len(classes_list)):
        img = load_img(os.path.join(os.path.join(data_path,classes_folder[j]),classes_list[k]))  # this is the k'th image in the j'th folder
        x = img_to_array(img)  # this is a Numpy array with shape (3, 150, 150)
        x = x.reshape((1,) + x.shape)  # this is a Numpy array with shape (1, 3, 150, 150)

        #prefixes for the augmented image names
        results_prefixes = ['blackspot_aug','burr_aug','dent_aug','edge_aug','grindinglines_aug','halfsurface_aug','notcover_aug','ok_samples_aug','scratch_aug']

        # the .flow() command below generates batches of randomly transformed images
        # and saves the results to the `preview/` directory
        i = 0
        for batch in datagen.flow(x, batch_size=1,
                                  save_to_dir=os.path.join(result_path_dir,result[j]), save_prefix=str(k)+results_prefixes[j], save_format='jpeg'):
            i += 1
            if i > 2:  # number of augmented images per sample
                break  # otherwise the generator would loop indefinitely
