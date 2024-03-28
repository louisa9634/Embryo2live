
# Embryo2live: Deep learning-based embryo assessment of static images can reduce the time to live birth in in vitro fertilization

## Environment
1. python 3.7
2. Tensorflow-GPU 2.6.0
3. keras 2.6.0
4. vit-keras 0.1.2

## Dataset and Weights:
1.  Please refer to https://github.com/qqwweee/keras-yolo3 to deploy the YOLO-V3 model
2.  Public silver training set and gold test set: https://doi.org/10.6084/m9.figshare.20123153.v3 
3.  Pretrained weights for embryo detection, cilinical pregancy prediction and live birth prediction: https://doi.org/10.6084/m9.figshare.25479469.v1
``` model=tf.keras.models.load_model('model weights',compile=False) ```


## Content: 
* Folder [preprocess](preprocess):
1.  ([Detector.py](/preprocess/Detector.py)) to detect embryo from noisy background and our pretrained weights can be accessed via https://doi.org/10.6084/m9.figshare.20123153.v3;
2.   input the Detection_results.csv file to ([crop_yolo_image.py](/preprocess/crop_yolo_image.py)) to crop your embryo. 
 
* Folder [grading](grading):
*   public dataset can be downloaded via https://doi.org/10.6084/m9.figshare.20123153.v3;
1.  training the expansion of degree ([traing1.ipynb](/grading/traing1.ipynb));
2.  inner cell mass ([traing2.ipynb](/grading/traing2.ipynb))
3.  trophectoderm ([traing3.ipynb](/grading/traing3.ipynb))
4.  the prediction results ([pred.csv](/grading/pred.csv));


* Folder [fresh](fresh):
1.  training clinical pregnancy prediction model for fresh embryo samples ([trainfrepreg.ipynb](/fresh/trainfrepreg.ipynb));
2.  training live birth prediction model for fresh embryo samples ([trainfrelb.ipynb](/fresh/trainfrelb.ipynb)) (the pretrained weights on all frozen samples was uploaded to https://doi.org/10.6084/m9.figshare.25479469.v1);
3.  figures for fresh emrbyo prediction were produced via ([figure.ipynb](/fresh/figure.ipynb)) and the results include clinical pregnancy accuracy ([pregfreacc.csv](/fresh/pregfreacc.csv)), live birth accuracy ([lbfreacc.csv](/fresh/lbfreacc.csv)) and clinical pregnancy and live birth probability ([fre.csv](/fresh/fre.csv))     


* Folder [fropredict](fropredict):
1.  training clinical pregnancy prediction model for frozen embryo samples:
      random forest baseline models: fresh grade, frozen grade, fresh & frozen grades ([fro_preg-rfgrade.ipynb](/fropredict/fro_preg-rfgrade.ipynb))
      embryo2live (input post-warmed image):([fro_preg-img.ipynb](/fropredict/fro_preg-img.ipynb))
      embryo2live (input post-warmed image & post-warmed grade):([fro_preg-frograde.ipynb](/fropredict/fro_preg-frograde.ipynb))
      embryo2live (input post-warmed image & fresh grade):([fro_preg-fregrade.ipynb](/fropredict/fro_preg-fregrade.ipynb))
2.  training live birth prediction model for frozen embryo samples:
      random forest baseline models: fresh grade, frozen grade, fresh & frozen grades ([fro_LB-rfgrade.ipynb](/fropredict/fro_LB-rfgrade.ipynb))
      embryo2live (input post-warmed image):([fro_LB-img.ipynb](/fropredict/fro_LB-img.ipynb))
      embryo2live (input post-warmed image & post-warmed grade):([fro_LB-frograde.ipynb](/fropredict/fro_LB-frograde.ipynb))
      embryo2live (input post-warmed image & fresh grade):*   training clinical pregnancy prediction model for frozen embryo samples:
      random forest baseline models: fresh grade, frozen grade, fresh & frozen grades ([fro_preg_rfgrade.ipynb](/fropredict/fro_preg_rfgrade.ipynb))
      embryo2live (input post-warmed image):([fro_preg-img.ipynb](/fropredict/fro_preg-img.ipynb))
      embryo2live (input post-warmed image & post-warmed grade):([fro_preg-frograde.ipynb](/fropredict/fro_preg-frograde.ipynb))
      embryo2live (input post-warmed image & fresh grade):([fro_preg-fregrade.ipynb](/fropredict/fro_preg-fregrade.ipynb))
3.   evaluate model performance: ([evaluate.ipynb](/fropredict/evaluate.ipynb))
4.   figures for frozen emrbyo prediction were produced via ([figure.ipynb](/fropredict/figure.ipynb))
  


