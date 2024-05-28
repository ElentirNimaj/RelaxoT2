% Make some figures of convolved signals that illstrate the properties of
% LTI


%change this path to where SPM is, since it uses spm_hrf
addpath /Users/jeanettemumford/Documents/Research/matlabcode


%Illustrate that twice the neural input gives twice the BOLD output
TR=.1;
t=0:TR:60;

hrf=48*spm_hrf(TR);  %scaling hrf so figure looks nice.


er2=zeros(size(t));
time_er2=50:250:500;
er2(time_er2(1:2:end))=1;
er2(time_er2(2:2:end))=2;
er2_conv=conv(er2, hrf);
er2_conv=er2_conv(1:length(t));
[t_fix_er2, er2_fix]=make_blocks(t, er2);



%Illustrate that the signals add linearally 
er3=zeros(size(t));
time_er3=[50 100 200 400 420];
er3(time_er3)=1;

er3_conv=conv(er3, hrf);
er3_conv=er3_conv(1:length(t));
[t_fix_er3, er3_fix]=make_blocks(t, er3);





subplot(2,1,1)
plot(t_fix_er2,er2_fix, 'r-', 'linewidth', 1)
hold on
plot(t,er2_conv, 'blue-', 'linewidth', 2)
hold off
axis([ 0 60 -0.5, 2.4])
xlabel('Time (s)', 'fontsize', 16)
leg=legend('Neural Response', 'BOLD activation');
set(leg,'FontSize',16)

subplot(2,1,2)
plot(t,er3_conv, 'green-', 'linewidth', 1) 
hold on
plot(t_fix_er3,er3_fix, 'r-', 'linewidth', 1)
for i=1:length(time_er3)
    stim_loop=zeros(size(t));
    stim_loop(time_er3(i))=1;
    stim_loop_conv=conv(stim_loop, hrf);
    stim_loop_conv=stim_loop_conv(1:length(t));
    plot(t, stim_loop_conv, 'g-', 'linewidth', 1)
end 
plot(t,er3_conv, 'blue-', 'linewidth', 2)
hold off
axis([ 0 60 -0.5, 2.4])
xlabel('Time (s)', 'fontsize', 16)
leg=legend('Individual task response');
set(leg,'FontSize',16)


