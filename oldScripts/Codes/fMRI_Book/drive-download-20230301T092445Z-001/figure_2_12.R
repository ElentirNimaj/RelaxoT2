# example of fourier analysis

# create some ar(1) noise

noise=array(data=0,dim=1000)
arcoef=0.4

noise[1]=rnorm(1)
for (x in 2:1000) {
	noise[x]=noise[x-1]*arcoef + rnorm(1)
	}
	
#foo=rnorm(1000)+0.6*sin(1:1000/(pi*2))
#foo=noise+0.6*sin(1:1000/(pi*2))
foo=noise
foo=foo-mean(foo)

s=spectrum(foo)
foo.lo=loess(foo~c(1:1000),span=0.02)
sl=spectrum(foo.lo$fitted)
foo.hi=foo-foo.lo$fitted
sh=spectrum(foo.hi)


layout(matrix(c(1:6),3,2,byrow=TRUE))
plot(foo[1:100],type='l',xlab="Time",ylab="Value",ylim=c(-3,3),main="Original data")
plot(s$freq,s$spec,type='l',xlab="Frequency",ylab="Power",ylim=c(0,12))

plot(foo.lo$fitted[1:100],type='l',xlab="Time",ylab="Value",ylim=c(-3,3),main="Low pass filtered")
plot(sl$freq,sl$spec,type='l',xlab="Frequency",ylab="Power",ylim=c(0,12))

plot(foo.hi[1:100],type='l',xlab="Time",ylab="Value",ylim=c(-3,3),main="High pass filtered")
plot(sh$freq,sh$spec,type='l',xlab="Frequency",ylab="Power",ylim=c(0,12))

