docker run --user 1000 --rm -it --entrypoint  bash^
       -v c:/users/bprigent/Documents/Pro/MIDFID_Experiment/Data/BIDS/rawdata:/bids:ro^
       -v c:/users/bprigent/Documents/Pro/MIDFID_Experiment/Data/BIDS/rawdata/derivates:/prep:ro^
       -v c:/users/bprigent/Documents/Pro/MIDFID_Experiment/Data/GLM:/out^
       -v c:/users/bprigent/Documents/Pro/MIDFID_Experiment/Data/workdir:/wdir^
        poldracklab/fitlins:latest /bids /out dataset -d /prep -w /wdir --estimator nilearn -m /bids/models/model-002_smdl.json
     