% example of convolution
% R. Poldrack, 10/16/08

% make a random signal

foo=randn(1,50);
foo=foo-mean(foo);
% make some convolution filters

norm1=pdf('norm',[-6:0.5:6],0,1);
norm2=pdf('norm',[-6:0.5:6],0,2);

cnorm1=conv(foo,norm1);
cnorm2=conv(foo,norm2);

% make identity convolution
ident=zeros(1,25);
ident(13)=1;
cident=conv(foo,ident)

figure()
plot(cident(13:62),'k','LineWidth',2)
hold on
plot(cnorm1(13:62),'r','LineWidth',2)
plot(cnorm2(13:62),'g','LineWidth',2)
print -depsc2 ConvolutionExample

figure()
plot(norm1,'r','LineWidth',2)
hold on
plot(norm2,'g','LineWidth',2)
plot(ident*0.5,'k','LineWidth',2)

print -depsc2 ConvolutionKernels

