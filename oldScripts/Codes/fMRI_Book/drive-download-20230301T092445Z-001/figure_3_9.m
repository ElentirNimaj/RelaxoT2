clf
t1=randn(1,10)*5+100;
p=plot(0:2:18,t1,'LineWidth',2)
hold on
interp_t1=(t1(2:10)+t1(1:9))/2; 
p2=plot(1:2:18,interp_t1,'ro:','LineWidth',2,'MarkerFaceColor','r','MarkerSize',8)
xlabel('Time (seconds)','FontSize',18)
ylabel('MRI signal','FontSize',18)