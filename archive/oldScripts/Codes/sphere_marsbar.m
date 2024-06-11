% Sphere creation auto

name = ["S1D1";"S1D2";"S2D3";"S3D1";"S3D4";"S4D2";"S4D4";"S4D5";...
        "S5D4";"S5D6";"S6D4";"S6D6";"S6D7";"S7D5";"S7D7";"S8D6";...
        "S8D7"];

marsbar('on');
my_centers = [...
    -37.12499613	46.60754134	27.19376253;
    -24.19228535	43.47584547	42.94486918;
    -30.55872421	-0.166498327	61.93747885;
    -32.85348781	54.34637626	22.74928593;
    -12.08939319	56.86718601	31.21430466;
    -7.730492831	45.83263847	48.8854319;
    0.100891008	51.48514409	41.59934398;
    6.402445116	44.85402683	49.95750305;
    -0.064292749	61.66839527	20.53251656;
    8.896842024	66.05365761	3.226200365;
    9.958602118	56.97197705	33.15587492;
    18.91973689	61.35723939	15.84955872;
    29.98075061	51.39274248	28.65625691;
    19.11071068	41.09295454	48.88828478;
    32.83130506	42.14483724	36.0305077;
    26.92422748	60.14238305	-0.349693025;
    37.9852412	50.17788614	12.45700516;
];

radius = 5;
rois = {};
A15_path = "c:/users/bprigent/Documents/Pro/MIDFID_Experiment/Data/EtudesfNIRS_1415/A15Sphere/";
spm_file = load(A15_path+"SPM.mat");
func_path = "swcraFonct_su_A15_task-midnirs_bold_2.5_2.5_2.5_roi.mat";
func = load(A15_path+func_path);

for pt_no = 1:size(my_centers, 1)
    params = struct('centre', my_centers(pt_no, :), 'radius', radius);
    roi = maroi_sphere(params);
    rois{end+1} = roi;
    saveroi(roi, sprintf([A15_path+'A15_05mm/sphere_%s_roi.mat'], name(pt_no)));
    roi_comb = roi & func.roi;
    saveroi(roi_comb, sprintf([A15_path+'A15_05mm/sphere_corr_%s_roi.mat'], name(pt_no)));
%     D = mardo(spm_file);
%     Y = get_marsy(roi_comb,D,'mean');
%     E = estimate(D,Y);
%     
end
disp('/* END OF THE SCRIPT *\')

