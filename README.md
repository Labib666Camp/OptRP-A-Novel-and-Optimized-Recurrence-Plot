# OptRP: A Novel and Optimized Recurrence Plot
This work is part of the publication "OptRPC: A novel and optimized recurrence plot-based system for ECG beat classification" DOI: https://doi.org/10.1016/j.bspc.2021.103328


For any signal <img src="https://latex.codecogs.com/svg.image?X{\in&space;\Re^1}" title="X{\in \Re^1}" />, we reconstruct its phase space using the Takens Embedding theorem in the following way.
<img src="https://latex.codecogs.com/svg.image?V_{\text&space;{recon&space;}}^{d}=\left(\vec{v}_{t}(d,&space;\tau)&space;\mid&space;t=0,1,2,&space;\ldots,&space;N-d&space;\tau\right)" title="V_{\text {recon }}^{d}=\left(\vec{v}_{t}(d, \tau) \mid t=0,1,2, \ldots, N-d \tau\right)" /> 

<img src="https://latex.codecogs.com/svg.image?\vec{v}_{t}(d,&space;\tau)=\left(x_{t&plus;k&space;\tau}&space;\in&space;X&space;\mid&space;k=0,1,2,&space;\ldots,&space;d-1\right)" title="\vec{v}_{t}(d, \tau)=\left(x_{t+k \tau} \in X \mid k=0,1,2, \ldots, d-1\right)" />

Now, We define a new and optimized Recurrence Plot (RP)

<img src="https://latex.codecogs.com/svg.image?R_{i&space;j}=\Theta_{opt}\left(\epsilon-\left\|\vec{v}_{i}-\vec{v}_{j}\right\|\right)" title="R_{i j}=\Theta_{opt}\left(\epsilon-\left\|\vec{v}_{i}-\vec{v}_{j}\right\|\right)" />

<img src="https://latex.codecogs.com/svg.image?\begin{aligned}&\Theta_{o&space;p&space;t}(x&space;;&space;\epsilon)=-a&space;\ln&space;(c&space;x)&space;;&space;\forall&space;x>\epsilon&space;\\&C=\frac{1}{\max&space;(D)}&space;\\&a=-\frac{\theta}{\ln&space;\left(c&space;x_{i&space;n}\right)}\end{aligned}" title="\begin{aligned}&\Theta_{o p t}(x ; \epsilon)=-a \ln (c x) ; \forall x>\epsilon \\&C=\frac{1}{\max (D)} \\&a=-\frac{\theta}{\ln \left(c x_{i n}\right)}\end{aligned}" />

where the thresholding parameter <img src="https://latex.codecogs.com/svg.image?\epsilon" title="\epsilon" /> is optimized. Lets assume there is a random variable <img src="https://latex.codecogs.com/svg.image?Z_{\epsilon}" title="Z_{\epsilon}" /> which explains the probabilistic nature of the recurrence plot 

<img src="https://latex.codecogs.com/svg.image?H\left(Z_{\epsilon}\right)=-\frac{\left(\sum_{k=1}^{n}&space;P_{Z_{\epsilon}}\left(z_{k}\right)&space;\log&space;\left(P_{Z_{\epsilon}}\left(z_{k}\right)\right)\right)}{|U|}" title="H\left(Z_{\epsilon}\right)=-\frac{\left(\sum_{k=1}^{n} P_{Z_{\epsilon}}\left(z_{k}\right) \log \left(P_{Z_{\epsilon}}\left(z_{k}\right)\right)\right)}{|U|}" />

<img src="https://latex.codecogs.com/svg.image?\epsilon_{o&space;p&space;t}=\arg&space;\max&space;_{\epsilon&space;\in&space;E}&space;H\left(Z_{\epsilon}\right)" title="\epsilon_{o p t}=\arg \max _{\epsilon \in E} H\left(Z_{\epsilon}\right)" />

![image info](RP.png)
