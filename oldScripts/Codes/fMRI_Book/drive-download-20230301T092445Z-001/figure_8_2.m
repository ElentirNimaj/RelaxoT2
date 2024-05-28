% demo for beta series correlation

% first, show how it can avoid activation-induced correlations

% 1 trial every 20 secs
% time resolution of model = 0.5 secs
% 24 trials total

ntrials=25;
%addpath /Applications/fmri_progs/spm8/
respsize1=randn(1,ntrials)+5;
X1=zeros(1,1000);
X1(1:40:1000)=respsize1;
X1c=conv(X1,spm_hrf(0.5));
X1=X1c(1:1000);

respsize2=randn(1,ntrials)+5;
X2=zeros(1,1000);
X2(1:40:1000)=respsize2;
X2c=conv(X2,spm_hrf(0.5));
X2=X2c(1:1000);

corr(respsize1',respsize2')

corr(X1',X2')


figure()
subplot(2,1,1)
plot(X1, 'linewidth', 2)
axis([0,1000,-0.2,1])
set(gca, 'FontSize', 12)
subplot(2,1,2)
plot(X2, 'linewidth', 2)
axis([0,1000,-0.2,1])
title(sprintf('r = %0.3f',corr(X1',X2')))
set(gca, 'FontSize', 12)
%print -depsc2 convplots.eps

% make beta series design matrix
Xbs=zeros(1000,20);
hrf=spm_hrf(0.5);

for t=1:ntrials,
    onset=(t-1)*40+1;
    Xbs(onset:onset+64,t)=hrf;
end
Xbs=Xbs(1:1000,:);

corr(X1',X2')


bs_hat1=pinv(Xbs'*Xbs)*Xbs'*X1';
bs_hat2=pinv(Xbs'*Xbs)*Xbs'*X2';
title(sprintf('r = %0.3f',corr(bs_hat1,bs_hat2)))

corr(bs_hat1,bs_hat2)

figure()
imagesc(Xbs)
colormap(gray)
%print -depsc2 'full_bsc_desmtx.eps'

figure()
plot(Xbs(1:200,1),'k','LineWidth',3) 
hold on
plot(Xbs(1:200,2)-0.2,'k','LineWidth',3)
plot(Xbs(1:200,3)-0.4,'k','LineWidth',3)
plot(Xbs(1:200,4)-0.6,'k','LineWidth',3)
axis off
%print -depsc2 'closeup_desmtx_plot.eps'

figure()
subplot(2,1,1)
plot(bs_hat1, 'linewidth', 2)
set(gca, 'FontSize', 12)
axis([0,25,2,9])
subplot(2,1,2)
plot(bs_hat2, 'linewidth', 2)
set(gca, 'FontSize', 12)
axis([0,25,3,7])
title(sprintf('r = %0.3f',corr(bs_hat1,bs_hat2)))
%print -depsc2 respplots.eps




