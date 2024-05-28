hrf=spm_hrf(0.1);

plot(hrf(1:20:300)*1/max(hrf),'LineWidth',2)
hold on
plot(hrf(10:20:300)*1/max(hrf),'r','LineWidth',2) 
plot(hrf(19:20:300)*1/max(hrf),'k','LineWidth',2)
l=legend('Slice 1','Slice 2', 'Slice 8')
set(l,'FontSize',18,'LineWidth',2)

foo=get(l,'Children')
set(foo(2),'LineWidth',2)
set(foo(5),'LineWidth',2)
set(foo(8),'LineWidth',2)
a=gca;
set(a,'XTick',[0:2:14])
set(a,'YTick',[0:0.5:1])
axis([0  15 -0.3 1.1])
set(a,'FontSize',16)

print -dpdf '../SliceTimingHRF.pdf'