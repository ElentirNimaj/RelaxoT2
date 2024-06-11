% demo for Image Processing chapter

% set up 4 X 1 homogenous coordinate matrix
% see http://bishopw.loni.ucla.edu/AIR5/homogenous.html


coords=ones(4,16);
coords(3,:)=1;
coords(1,:)=kron(1:4,ones(1,4))-2.5;
coords(2,:)=kron(ones(1,4),1:4)-2.5;


% translation

xtrans=0.5;
ytrans=0.2;
ztrans=0;
translation_matrix=eye(4);
translation_matrix(1:3,4)=[xtrans ytrans ztrans]';

for x=1:16,
    coords_translated(:,x) = translation_matrix*coords(:,x);
end;
clf
subplot(2,2,1)
scatter(coords(1,:),coords(2,:),'ko','MarkerFaceColor','k')
axis([-3 3 -3 3])
axis equal
hold on
scatter(coords_translated(1,:),coords_translated(2,:),'bo','MarkerFaceColor','b')
% for x=1:16,
%     plot([coords(1,x),coords_translated(1,x)],[coords(2,x),coords_translated(2,x)],'k -','MarkerFaceColor','k')
% end
% plot grid
for x=[-1.5:1.5],
    plot([-1.5,1.5],[x,x],'k -')
    plot([x,x],[-1.5,1.5],'k -')  
end;

for x=1:4:16,
    plot([coords_translated(1,x),coords_translated(1,x+3)],[coords_translated(2,x),coords_translated(2,x+3)],'b -')
end
for x=1:4,
    plot([coords_translated(1,x),coords_translated(1,x+12)],[coords_translated(2,x),coords_translated(2,x+12)],'b -')
end

title('Translation','FontSize',18)

% rotation

xrot=0; % pitch
yrot=0;  % roll
zrot=pi/8;  % yaw
rotation_matrix=eye(4)
rotation_matrix(1:3,1)=[cos(zrot)*cos(yrot)+sin(zrot)*sin(xrot)*sin(yrot) -1*sin(zrot)*cos(xrot) sin(zrot)*sin(xrot)*cos(yrot)-cos(zrot)*sin(yrot)]';
rotation_matrix(1:3,2)=[sin(zrot)*cos(yrot)-cos(zrot)*sin(xrot)*sin(yrot) cos(zrot)*cos(xrot) -1*cos(zrot)*sin(xrot)*cos(yrot)-sin(zrot)*sin(yrot)]';
rotation_matrix(1:3,3)=[cos(xrot)*sin(yrot) sin(xrot) cos(xrot)*cos(yrot)]';

for x=1:16,
    coords_rotated(:,x) = rotation_matrix*coords(:,x);
end;

subplot(2,2,2)

scatter(coords(1,:),coords(2,:),'ko','MarkerFaceColor','k')
axis([-3 3 -3 3])
axis equal
hold on
scatter(coords_rotated(1,:),coords_rotated(2,:),'bo','MarkerFaceColor','b')
% for x=1:16,
%     plot([coords(1,x),coords_rotated(1,x)],[coords(2,x),coords_rotated(2,x)],'k -','MarkerFaceColor','k')
% end
for x=[-1.5:1.5],
    plot([-1.5,1.5],[x,x],'k -')
    plot([x,x],[-1.5,1.5],'k -')  
end;

for x=1:4:16,
    plot([coords_rotated(1,x),coords_rotated(1,x+3)],[coords_rotated(2,x),coords_rotated(2,x+3)],'b -')
end
for x=1:4,
    plot([coords_rotated(1,x),coords_rotated(1,x+12)],[coords_rotated(2,x),coords_rotated(2,x+12)],'b -')
end

title('Rotation','FontSize',18)


% rescaling

xscale=1.2;
yscale=1.1;
zscale=1;
scaling_matrix=[xscale 0 0 0; 0 yscale 0 0; 0 0 zscale 0; 0 0 0 1];

for x=1:16,
    coords_scaled(:,x) = scaling_matrix*coords(:,x);
end;

subplot(2,2,3)

scatter(coords(1,:),coords(2,:),'ko','MarkerFaceColor','k')
axis([-3 3 -3 3])
axis equal
hold on
scatter(coords_scaled(1,:),coords_scaled(2,:),'bo','MarkerFaceColor','b')
% for x=1:16,
%     plot([coords(1,x),coords_scaled(1,x)],[coords(2,x),coords_scaled(2,x)],'k -','MarkerFaceColor','k')
% end
for x=[-1.5:1.5],
    plot([-1.5,1.5],[x,x],'k -')
    plot([x,x],[-1.5,1.5],'k -')  
end;

for x=1:4:16,
    plot([coords_scaled(1,x),coords_scaled(1,x+3)],[coords_scaled(2,x),coords_scaled(2,x+3)],'b -')
end
for x=1:4,
    plot([coords_scaled(1,x),coords_scaled(1,x+12)],[coords_scaled(2,x),coords_scaled(2,x+12)],'b -')
end
title('Scaling','FontSize',18)

% skewing/shearing

% method suggested by Ashburner & Friston in HBF chapter:

xshear=0;
yshear=0.5;
zshear=0;
shear_matrix=eye(4);
shear_matrix(1,2)=xshear;
shear_matrix(2,1)=yshear;
shear_matrix(3,2)=zshear;
%shear_matrix(4,:)=[xshear yshear zshear 1];
for x=1:16,
    coords_sheared(:,x) = shear_matrix*coords(:,x);
end;
subplot(2,2,4)

scatter(coords(1,:),coords(2,:),'ko','MarkerFaceColor','k')
axis([-3 3 -3 3])
axis equal
hold on
scatter(coords_sheared(1,:),coords_sheared(2,:),'bo','MarkerFaceColor','b')
% for x=1:16,
%     plot([coords(1,x),coords_sheared(1,x)],[coords(2,x),coords_sheared(2,x)],'k -','MarkerFaceColor','k')
% end
for x=[-1.5:1.5],
    plot([-1.5,1.5],[x,x],'k -')
    plot([x,x],[-1.5,1.5],'k -')  
end;

for x=1:4:16,
    plot([coords_sheared(1,x),coords_sheared(1,x+3)],[coords_sheared(2,x),coords_sheared(2,x+3)],'b -')
end
for x=1:4
    plot([coords_sheared(1,x),coords_sheared(1,x+12)],[coords_sheared(2,x),coords_sheared(2,x+12)],'b -')
end
title('Shearing','FontSize',18)

%print -depsc2 ../../img/ImageProcessing/AffineTransforms
