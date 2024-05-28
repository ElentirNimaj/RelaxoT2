# Try Brain extraction

import brainextractor
import nibabel as nib

input_img = nib.load("C:/Users/bprigent/Datas/testFolder/Shanoir-download_1ds_22-05-2024_15h2334/pouet.nii")
output_img = "C:/Users/bprigent/Resultats/Mask/maskrecon.nii.gz"

bet = brainextractor.BrainExtractor(img=input_img)
bet.run()
bet.save_mask(output_img)