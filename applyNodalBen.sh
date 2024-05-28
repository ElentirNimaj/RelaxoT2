#!/bin/bash
export PATH=$PATH:/home/elentir/fsl/bin/
export PATH=$PATH:/mnt/c/d/Anima-build/bin/
export PATH=$PATH:/mnt/c/d/Anima-Scripts-Public/bin/

FSLDIR=/home/elentir/fsl/
. ${FSLDIR}/etc/fslconf/fsl.sh
PATH=${FSLDIR}/bin:${PATH}
export FSLDIR PATH

# DATA dir
DATADIR=/mnt/c/Users/bprigent/Datas/NODALHV/relaxo
SCALINGTXT=/mnt/c/Users/bprigent/Anima/Scaling_Normal.txt
EXCITATIONTXT=/mnt/c/Users/bprigent/Anima/Excitation_Normal.txt

echo "$DATADIR"
for patient in $DATADIR/*; do     # FOR EACH SUBJECT
    clear
    COUNTER_SET=0
    patientID=$(basename "$patient")

    echo "$patientID"

    pIn="$patient"
    name=`basename $pIn`
  
    infile_B=${pIn}/allFilesRELAXO_B.txt

    #ls ${$pIn}/relaxo/*RELAXO_B*_8_e?.nii > ${infile_B}; ls  ${dir_data}/*RELAXO_B*_8_e??.nii >> ${infile_B}; more ${infile_B}
    ls ${pIn}/NODAL*.nii.gz > ${infile_B}; ls  ${pIn}/NODAL*.nii.gz >> ${infile_B}; more ${infile_B}
    sed -i 's+/mnt/c/+c:/+g' ${infile_B}
    infile_B=c:/Users/bprigent/Datas/NODALHV/relaxo/$patientID/allFilesRELAXO_B.txt
    
    # Parameter files
    weight=${pIn}/weightRelaxo_${patientID}.nii.gz # part des 3 compartiments myelin / eau /
    t2out=${pIn}/t2Val_${patientID}.nii.gz

    # Launch Relaxo processing
    animaGMMT2RelaxometryEstimation.exe --t2-flip 180 -e 10 -o ${t2out} -O ${weight} -i ${infile_B} -w 7.6 -p "$SCALINGTXT" -E "$EXCITATIONTXT"
    echo
    echo
done
