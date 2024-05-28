 docker run --rm -it \
        -v /local/bprigent/BIDS/rawdata:/bids:ro\
        -v /local/bprigent/BIDS/rawdata/derivates:/prep:ro\
        -v /local/bprigent/GLM:/out\
        -v /local/bprigent/workdir:/wdir\
        poldracklab/fitlins:latest /bids /out dataset -d /prep -w /wdir --estimator nilearn -m /bids/models/model-002_smdl.json
     