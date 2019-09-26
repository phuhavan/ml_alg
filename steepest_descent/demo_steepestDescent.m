% f(x,y) = 2xy + 2x - x^2 -2y^2
close all; clc; clear all;

% Function
func = @(x,y) -(2.*x.*y + 2.*x - x.^2 -2.*y.^2);

% Initial guess
x0 = 4;
y0 = 4;

% Algorithm parameters
dx = 0.001;
dy = 0.001;
alpha = 0.1;

x = linspace(-1,+5,1000);
y = linspace(-1,+5,1000);
[Y,X] = meshgrid(y,x);
F = func(X,Y);
surf(x,y,F');
shading interp;

% Perform algorithm
tol = 1e-6;
g = [inf;inf];
while norm(g) > tol
    
    % Visualize
    imagesc(x, y, F');
    axis equal tight;
    hold on;
    plot(x0,y0,'ok');
    hold off;
    drawnow;
    
    % compute gradient
    f1 = func(x0-dx/2, y0);
    f2 = func(x0+dx/2, y0);
    gx = (f2 - f1)/dx;
    
    f1 = func(x0, y0-dy/2);
    f2 = func(x0, y0+dy/2);
    gy = (f2 - f1)/dy;
    
    g = [gx; gy];
    
    % Update position of guess
    x0 = x0 - alpha*gx;
    y0 = y0 - alpha*gy;
end

[x0, y0]