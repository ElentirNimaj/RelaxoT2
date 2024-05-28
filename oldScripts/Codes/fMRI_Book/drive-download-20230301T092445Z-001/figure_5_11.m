%plot parametric modulation example

addpath /Users/jeanettemumford/Documents/Research/matlabcode/  %make sure spm is in your path and then omit this line
cd /Users/jeanettemumford/Documents/Research/Writing/Book/book/img/StatisticalModelingFirstLevel/ParametricModulation


TR=1;
t=0:TR:100;

hrf=2*spm_hrf(TR);


er1=zeros(size(t));
time_er1=11:20:100;
er1(time_er1)=1;
er1_conv=conv(er1, hrf);
er1_conv=er1_conv(1:length(t));
[t_fix_er1, er1_fix]=make_blocks(t, er1);


er_mod=zeros(size(t));
time_er1=11:20:100;
modval=[10 0 -10 5 -5];
er_mod(time_er1)=modval;
er_mod_conv=conv(er_mod, hrf);
er_mod_conv=er_mod_conv(1:length(t));



fs=20;
fsl=18;

subplot(3,1,1)
plot(t_fix_er1, er1_fix, 'r-', 'linewidth', 2)
axis([0 100 0 1.3])
xlabel('Time (s)', 'fontsize', fsl)
set(gca, 'YTickLabel', {''})

subplot(3,1,2)
plot(t, er1_conv, 'linewidth', 2)
xlabel('Time (s)', 'fontsize', fsl)
title('Unmodulated', 'fontsize', fs)

subplot(3,1,3)
plot(t, er_mod_conv, 'linewidth', 2)
xlabel('Time (s)', 'fontsize', fsl)
title('Modulated', 'fontsize', fs)






