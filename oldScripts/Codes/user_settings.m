% ============================================== %
% User settings pre processing
% Q. Duche for B.Prigent
% v 3, 13-Apr-2023
% ============================================== %

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%% Parameters that are invariant between testers  %%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Display messages 
VERBOSE = true;
% Ask before deleting a pre-processing file
ASK_BEFORE_DELETE = true;

NUM_SLICES = 54;
% Repetition Time (TR) in seconds
TR = 1.224;
% stabilize the signal) - By default 2 for Philips, 0 for Siemens***
% *** nEnd : Number of scans to discard at the end of the fMRI session 
% *** nBeg : Number of dummy scans to discard for IRMf sessions 
%NUM_IMG_STAB  = struct('sessName', {'se_motor','se_breathhold'},'nBeg',{0});
NUM_IMG_STAB  = struct('sessName', {'se_mid'},'nBeg',{0});
%NUM_IMG_TRUNC = struct('sessName', {'se_motor','se_breathhold'},'nEnd',{0});
NUM_IMG_TRUNC = struct('sessName', {'se_mid'},'nEnd',{0});

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%% Parameters corresponding to defaults_smri_preproc.m %%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% ------------------ 1) RE-DEFINITION OF SOME PARAMETERS ------------------

% ------------------ 2) UNTOUCHED PARAMETERS ------------------
% *** Segmentation ***
% Save inverse deformation fields (iy_T13D)
SEG_SAVE_INVDEFORM_FIELDS = false;
% Save unmodulated seg maps (wc1, wc2, ...)
SEG_SAVE_UNMODULATED_MAPS = false;
% Save modulated seg maps (mwc1, mwc2, ...)
SEG_SAVE_MODULATED_MAPS = false;
% Save Dartel Import Tissues (rc1, rc2, ...)
SEG_SAVE_DARTEL_IMPORTED_TISSUES = false;

% Mask anatomical MRI with GM+WM+CSF > MASK_ANAT_THRESH
% if FINE_MASK, GM+WM > MASK_ANAT_THRESH
MASK_ANAT_THRESH = 0.5;
FINE_MASK = false;
MASK_ANAT_FILE = false;


% Template files for GM, WM, CSF, BONE, SOFT and OTHER tissues
% If they are all empty, SPM template will be used
% Otherwise, at least GM and WM must be defined
GM_TEMPLATE = '';
WM_TEMPLATE = '';
CSF_TEMPLATE = '';
BONE_TEMPLATE = '';
SOFT_TEMPLATE = '';
OTHER_TEMPLATE = '';

% *** Structural normalization ***
% Bounding box (in mm) of the volume which is to be written (relative 
% to the anterior commissure). String or matrix :
% If 'default', the bounding box is the default SPM12 BB  = [-78 -112 -70; 78 76 85]) --> the cerebellum is not cut
% Otherwise, 2x3 matrix: e.g., [-78 -112 -50; 78 76 85] (default SPM8 BB) --> the cerebellum is cut
SN_BOUNDING_BOX = 'default';

% Voxel size (x,y,z) in mm of the written normalised images.
SN_VOXEL_SIZES = [1 1 1];

% DARTEL NORMALISATION
% Option to normalise segmented tissue volumes
DARTEL_NORM_TISSUE_FILES = false;
% Use modulation for tissue files warping
DARTEL_NORM_TISSUE_FILES_MODULATION = false;

% *** Smoothing ***
SMOOTH_FWHM_ANAT = [0 0 0]; % No smoothing by default

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%% Parameters corresponding to defaults_fmri_preproc.m %%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% ------------------ 1) RE-DEFINITION OF SOME PARAMETERS ------------------

% *** Spatial realignment ***
ALL_SESSIONS_TOGETHER = false;

% *** Distortion correction using field maps ***
% True to unwarp EPI images using field maps
UNWARP_EPI = false;

% *** Slice timing ***
% Toggles slice timing preprocessing step
SLICE_TIMING = true;
% Acquisition Time (TA) in seconds (Usually TR-(TR/nslices))
TA = TR-(TR/NUM_SLICES);
% Slice order (ascending, descending, interleaved)
SLICE_ORDER =  [
		1.1375,
		1.07,
		1.0025,
		0.9375,
		0.87,
		0.8025,
		0.735,
		0.67,
		0.6025,
		0.535,
		0.4675,
		0.4025,
		0.335,
		0.2675,
		0.2,
		0.135,
		0.0675,
		0,
		1.1375,
		1.07,
		1.0025,
		0.9375,
		0.87,
		0.8025,
		0.735,
		0.67,
		0.6025,
		0.535,
		0.4675,
		0.4025,
		0.335,
		0.2675,
		0.2,
		0.135,
		0.0675,
		0,
		1.1375,
		1.07,
		1.0025,
		0.9375,
		0.87,
		0.8025,
		0.735,
		0.67,
		0.6025,
		0.535,
		0.4675,
		0.4025,
		0.335,
		0.2675,
		0.2
		0.135,
		0.0675,
		0	];

% *** Smoothing ***
% Full width at half maximum (in x, y and z direction) of the Gaussian smoothing kernel in mm.
SMOOTH_FWHM = [6 6 6];

% ------------------ 2) UNTOUCHED PARAMETERS ------------------
% Echo times of field map sequence
ECHO_TIMES = [4.92 7.38];    
% Phase encoding direction: AP=antero-posterior, PA=postero-anterioir,
% other directions not supported
PHASE_ENCODING_DIR = 'AP';
% Readout Time : 
% echo_spacing (eg 0.69ms)*nb phase ecoding steps (eg 108) without parallel imaging
% echo_spacing (eg 0.69ms)*nb reference lines (eg 24)+ echo_spacing*(nb
% phase ecoding steps (eg 108) - ref lines (eg 24))/GRAPPA acceleration
% factor (eg 2)
TOTAL_EPI_READOUT_TIME = 45.54;
% True if field map sequence is EPI based
EPI_BASED = false;
MASK_BRAIN_VDM = 0;

% *** Coregistration ***
% True if functional data must be coregistered on grey matter (instead of
% whole T1 volume)
CO_WITH_GM = true;     
CO_WITH_MASKED = false;     

% *** Functional normalisation ***
% Voxel size (x,y,z) in mm of the written normalised images.
% This option will force the normalised functional volumes to have 
% the given resolution for the MNI normalisation only.
% /!\ ATTENTION : THIS OPTION IS ONLY COMPATIBLE WITH MNI NORMALISATION
% in other words IT IS IGNORED WITH DARTEL NORMALISATION and normalised
% functional volumes with DARTEL will have the input resolution
FN_VOXEL_SIZES = [2.5 2.5 2.5];

% *** Quantification of cerebral blood flow ***
CBF_QUANTIFICATION_TYPE = 5;% 2=Siemens / 4=Wang --> PASL / 5 = WhitePaper PCASL
SEQ_PASL = 0;
SEQ_PCASL = 1;
% Type of control image, boolean. True to use M0 file (first acquired
% file in Siemens PASL Q2TIPS sequence) in quantification, false to use
% mean of control images
CBF_USE_M0 = 0;
CBF_ACQ_M0 = 1; % to use a M0 image specifically acquired
% Changing TI2 with slice, boolean. True to have a specific acquisition
% time for each slice, false to use the same value for the volume
CBF_TI2_INCREASE_WITH_SLICE = false;
% Time required to acquire one ASL slice in s (default: 45ms)
ASL_SLICE_DELAY = 0.040; 
% Change negative values into zeros
QUANTIF_NEG_TO_ZERO = false;
% T1 BLOOD
CBF_T1BLOOD = 1650*10^-3;
% LAMBDA: PCASL = 0.9 / PASL = 0.9
CBF_LAMBDA = 0.9;
% ALPHA: PCASL = 0.85 / PASL = 0.95
CBF_ALPHA = 0.85;

% for PASL
ASL_TI2 = 1700*10^-3;
ASL_TI1 = 700*10^-3;
ASL_TE = 0.0177;

% for PCASL
CBF_PCASL_PLD = 1500*10^-3;
CBF_PCASL_TAU = 1500*10^-3;

% *** PVE-correction ***
PVE_TYPE = 6; %6 = tv filtering / 5 = Aslanni's pve filtering